#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pyyaml>=6.0",
#     "click>=8.0",
# ]
# ///
"""Generate redirect files from old Jupyter Book v1 URLs to new MyST URLs.

This script reads a MyST table of contents and creates HTML redirect pages
that map old URLs (e.g., overview.html) to new MyST URLs (e.g., /overview/).

This is useful when migrating from Jupyter Book v1 to MyST/Jupyter Book v2,
as the URL structure changes from .html files to directory-based URLs.

Index File Detection
--------------------
The first file in your table of contents is automatically detected as the
index/landing page and will redirect to the base URL. For example:
- If your first TOC entry is "intro.md" → redirects "intro.html" to base URL
- If your first TOC entry is "index.md" → redirects "index.html" to base URL
- Works with any filename as the first TOC entry

MyST URL Sanitization
---------------------
MyST applies the following transformations to file paths when generating URLs:
1. Lowercase: Converts entire path to lowercase
2. Spaces and underscores: Replaced with hyphens
3. Multiple hyphens: Collapsed to a single hyphen
4. Leading/trailing hyphens: Stripped from each path component

Examples:
- "Test With Spaces.md" → "test-with-spaces"
- "TestMixedCase.md" → "testmixedcase"
- "test_with_underscores.md" → "test-with-underscores"
- "_LeadingUnderscore.md" → "leadingunderscore"
- "Multiple___Special.md" → "multiple-special"

Usage:
    # With uv (recommended):
    uv run scripts/generate_redirects.py --base-url https://example.com/ --output-dir _build/redirects

    # Direct execution:
    python scripts/generate_redirects.py --base-url https://example.com/ --output-dir _build/redirects

    # With custom myst.yml location:
    python scripts/generate_redirects.py --base-url https://example.com/ --myst-config path/to/myst.yml

Examples:
    # Generate redirects for Jupyter governance docs:
    uv run scripts/generate_redirects.py --base-url https://jupyter.org/governance/

    # Specify custom output directory:
    uv run scripts/generate_redirects.py --base-url https://example.com/ --output-dir public/redirects
"""
import re
import sys
from pathlib import Path
from typing import List, Dict, Any

import yaml
import click


def flatten_toc(toc: List[Dict[str, Any]]) -> List[str]:
    """Recursively extract all file paths from the table of contents.

    Args:
        toc: The table of contents structure from myst.yml

    Returns:
        A flat list of all file paths referenced in the TOC
    """
    files = []
    for item in toc:
        if 'file' in item:
            files.append(item['file'])
        if 'children' in item:
            files.extend(flatten_toc(item['children']))
    return files


def sanitize_for_myst_url(path: str) -> str:
    """Sanitize a file path to match MyST's URL slug format.

    MyST applies these transformations when converting file paths to URLs:
    1. Lowercase the entire path
    2. Replace spaces and underscores with hyphens
    3. Collapse multiple consecutive hyphens into a single hyphen
    4. Strip leading and trailing hyphens from each path component

    Args:
        path: The file path to sanitize (with or without extension)

    Returns:
        The sanitized URL slug matching MyST's behavior

    Examples:
        >>> sanitize_for_myst_url("Test With Spaces")
        'test-with-spaces'
        >>> sanitize_for_myst_url("TestMixedCase")
        'testmixedcase'
        >>> sanitize_for_myst_url("test_with_underscores")
        'test-with-underscores'
        >>> sanitize_for_myst_url("_LeadingUnderscore")
        'leadingunderscore'
        >>> sanitize_for_myst_url("Multiple___Special")
        'multiple-special'
        >>> sanitize_for_myst_url("charters/MediaStrategyCharter")
        'charters/mediastrategycharter'
    """
    # Convert to lowercase
    slug = path.lower()

    # Replace spaces and underscores with hyphens
    slug = slug.replace(' ', '-').replace('_', '-')

    # Collapse multiple consecutive hyphens
    slug = re.sub(r'-+', '-', slug)

    # Strip leading/trailing hyphens from each path component
    # This preserves directory structure while cleaning each component
    parts = slug.split('/')
    parts = [part.strip('-') for part in parts]
    slug = '/'.join(parts)

    return slug


def create_redirect_html(old_slug: str, new_url: str, output_root: Path) -> Path:
    """Create an HTML redirect file with meta refresh tag.

    Args:
        old_slug: The old URL path (e.g., 'overview.html')
        new_url: The new URL to redirect to (e.g., 'https://example.com/overview/')
        output_root: The root directory where redirect files should be created

    Returns:
        Path to the created redirect file
    """
    # Ensure the output directory exists
    output_file = output_root / old_slug
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Write a simple HTML redirect
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="refresh" content="0; url={new_url}">
    <meta charset="utf-8">
    <title>Redirecting...</title>
</head>
<body>
    <p>This page has moved. Redirecting to <a href="{new_url}">{new_url}</a></p>
</body>
</html>
"""
    output_file.write_text(html)
    return output_file


def load_myst_toc(myst_config_path: Path) -> List[str]:
    """Load and extract file paths from a MyST configuration file.

    Args:
        myst_config_path: Path to the myst.yml configuration file

    Returns:
        List of file paths from the table of contents

    Raises:
        FileNotFoundError: If the config file doesn't exist
        KeyError: If the config file doesn't have the expected structure
    """
    if not myst_config_path.exists():
        raise FileNotFoundError(f"MyST config file not found: {myst_config_path}")

    with open(myst_config_path) as f:
        config = yaml.safe_load(f)

    if 'project' not in config or 'toc' not in config['project']:
        raise KeyError("MyST config must have 'project.toc' structure")

    return flatten_toc(config['project']['toc'])


def generate_redirects(
    base_url: str,
    output_root: Path,
    myst_config_path: Path,
    verbose: bool = True
) -> int:
    """Generate all redirect files based on MyST configuration.

    The first file in the TOC is treated as the index/landing page and redirects
    to the base URL. All other files redirect to their sanitized URL paths.

    Args:
        base_url: The base URL of the site (e.g., 'https://example.com/')
        output_root: Directory where redirect files will be created
        myst_config_path: Path to the myst.yml configuration file
        verbose: Whether to print progress messages

    Returns:
        Number of redirect files created
    """
    # Ensure base_url ends with /
    if not base_url.endswith('/'):
        base_url += '/'

    # Load file paths from MyST TOC
    file_paths = load_myst_toc(myst_config_path)

    if not file_paths:
        if verbose:
            click.echo("⚠️  No files found in TOC", err=True)
        return 0

    # Auto-detect index file: the first file in the TOC is typically the landing page
    # Remove extension and sanitize to get the slug that MyST will generate
    index_file_path = file_paths[0]
    index_slug = sanitize_for_myst_url(
        index_file_path.replace('.md', '').replace('.ipynb', '')
    )

    if verbose:
        click.echo(f"ℹ️  Detected index file: {index_file_path} (slug: {index_slug})")

    # Generate redirects for each file
    count = 0
    for file_path in file_paths:
        # Old URL: path/to/file.md -> path/to/file.html
        # This preserves the original filename case from Jupyter Book v1
        old_slug = file_path.replace('.md', '.html').replace('.ipynb', '.html')

        # New URL: path/to/file.md -> /path/to/file/
        # Remove file extension first, then apply MyST's sanitization rules
        path_without_ext = file_path.replace('.md', '').replace('.ipynb', '')
        new_slug = sanitize_for_myst_url(path_without_ext)

        # The first file in the TOC becomes the root index
        new_url = base_url if new_slug == index_slug else base_url + new_slug + '/'

        create_redirect_html(old_slug, new_url, output_root)
        if verbose:
            click.echo(f"✓ {old_slug} → {new_url}")
        count += 1

    return count


@click.command()
@click.option(
    '--base-url',
    required=True,
    help='Base URL of the website (e.g., https://jupyter.org/governance/)',
)
@click.option(
    '--output-dir',
    type=click.Path(path_type=Path),
    default='_build/redirects',
    help='Directory where redirect files will be created (default: _build/redirects)',
)
@click.option(
    '--myst-config',
    type=click.Path(exists=True, path_type=Path),
    default='docs/myst.yml',
    help='Path to the myst.yml configuration file (default: docs/myst.yml)',
)
@click.option(
    '--quiet',
    is_flag=True,
    help='Suppress progress output',
)
def main(base_url: str, output_dir: Path, myst_config: Path, quiet: bool):
    """Generate HTML redirect files for Jupyter Book v1 to MyST migration.

    This script helps maintain backward compatibility when migrating from
    Jupyter Book v1 (which uses .html URLs) to MyST/Jupyter Book v2
    (which uses directory-based URLs).

    The script reads your myst.yml table of contents and creates redirect
    files that map old .html URLs to the new directory-based structure.
    """
    try:
        count = generate_redirects(
            base_url=base_url,
            output_root=output_dir,
            myst_config_path=myst_config,
            verbose=not quiet
        )

        if not quiet:
            click.echo(f"\n✨ Generated {count} redirect files in {output_dir}")
            click.echo(f"\nNext steps:")
            click.echo(f"1. Copy the redirect files to your web server")
            click.echo(f"2. Ensure .html files are served with the redirect HTML")
            click.echo(f"3. Test the redirects work correctly")

    except FileNotFoundError as e:
        click.echo(f"❌ Error: {e}", err=True)
        sys.exit(1)
    except KeyError as e:
        click.echo(f"❌ Error: {e}", err=True)
        click.echo("Make sure your myst.yml has a 'project.toc' structure", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"❌ Unexpected error: {e}", err=True)
        sys.exit(1)


if __name__ == "__main__":
    main()

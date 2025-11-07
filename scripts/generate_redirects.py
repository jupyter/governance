#!/usr/bin/env python3
"""Generate redirect files from old Jupyter Book v1 URLs to new MyST URLs.

This script reads the MyST table of contents and creates HTML redirect pages
that map old URLs (e.g., overview.html) to new MyST URLs (e.g., /overview).

Usage:
    python generate_redirects.py [base_url] [output_dir]

Example:
    python generate_redirects.py "https://jupyter.org/governance/" "docs/_build/redirects"
"""
import os
import sys
import yaml


def flatten_toc(toc):
    """Recursively extract all file paths from the table of contents."""
    files = []
    for item in toc:
        if 'file' in item:
            files.append(item['file'])
        if 'children' in item:
            files.extend(flatten_toc(item['children']))
    return files


def create_redirect_html(old_slug, new_url, output_root):
    """Create an HTML redirect file with meta refresh tag."""
    # Ensure the output directory exists
    output_file = os.path.join(output_root, old_slug)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

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
    with open(output_file, 'w') as f:
        f.write(html)

    return output_file


def main():
    # Configuration
    myst_config = 'docs/myst.yml'
    base_url = sys.argv[1] if len(sys.argv) > 1 else "https://jupyter.org/governance/"
    output_root = sys.argv[2] if len(sys.argv) > 2 else "_build/redirects"

    # Read the table of contents from myst.yml
    with open(myst_config) as f:
        config = yaml.safe_load(f)

    file_paths = flatten_toc(config['project']['toc'])

    # Generate redirects for each file
    count = 0
    for file_path in file_paths:
        # Old URL: path/to/file.md -> path/to/file.html
        old_slug = file_path.replace('.md', '.html').replace('.ipynb', '.html')

        # New URL: path/to/file.md -> /path/to/file
        # Special case: intro.md becomes the root index
        new_slug = file_path.replace('.md', '').replace('.ipynb', '')
        new_url = base_url if new_slug == 'intro' else base_url + new_slug

        create_redirect_html(old_slug, new_url, output_root)
        print(f"✓ {old_slug} → {new_url}")
        count += 1

    print(f"\n✨ Generated {count} redirect files in {output_root}")


if __name__ == "__main__":
    main()

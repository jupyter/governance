"""Nox sessions for building MyST documentation."""

import nox

nox.options.reuse_existing_virtualenvs = True
nox.options.default_venv_backend = "uv"


@nox.session
def docs(session):
    """Build the MyST documentation."""
    session.install("-r", "requirements.txt")
    session.chdir("docs")
    session.run("myst", "build", "--html", "--strict")


@nox.session(name="docs-live")
def docs_live(session):
    """Build a live server with MyST documentation."""
    from pathlib import Path

    # Check if generated leadership files exist
    generated_dir = Path("docs/_includes/generated")
    if not generated_dir.exists() or not any(generated_dir.iterdir()):
        session.log(
            "⚠️  WARNING: Generated leadership files are missing!",
            "   Run 'nox -s generate-leadership' first to generate them.",
            "   The documentation build may fail without these files.",
        )

    session.install("-r", "requirements.txt")
    session.chdir("docs")
    session.run("myst", "start")


@nox.session(name="redirects")
def redirects(session):
    """Generate redirects for built docs."""
    session.run(
        "uv",
        "run",
        "https://raw.githubusercontent.com/jupyter-book/jb1-redirect-generator/main/generate_redirects.py",
        "--base-url",
        "https://jupyter.org/governance/",
        "--output-dir",
        "docs/_build/html",
        external=True,
    )


@nox.session(name="generate-leadership")
def generate_leadership(session):
    """Generate leadership include files from YAML data."""
    session.install("-r", "requirements.txt")
    session.run("python", "docs/_scripts/generate_leadership_sections.py")

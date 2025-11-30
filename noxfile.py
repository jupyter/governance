"""Nox sessions for building MyST documentation."""

import nox

nox.options.reuse_existing_virtualenvs = True
nox.options.default_venv_backend = "uv"


@nox.session
def docs(session):
    """Build the MyST documentation."""
    session.install("-r", "requirements.txt")
    session.chdir("docs")
    session.run("npm", "install", external=True)
    session.run("myst", "build", "--html")


@nox.session(name="docs-live")
def docs_live(session):
    """Build a live server with MyST documentation."""
    session.install("-r", "requirements.txt")
    session.chdir("docs")
    session.run("npm", "install", external=True)
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

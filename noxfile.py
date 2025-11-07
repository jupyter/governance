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
    """Build and serve the documentation with live reload."""
    session.install("-r", "requirements.txt")
    session.chdir("docs")
    session.run("myst", "start")

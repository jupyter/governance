# Project Jupyter Governance

The purpose of this repository is to formalize the governance process for Project Jupyter. The governance documents are best viewed at https://jupyter.org/governance. They may also be built from the files in this repository by following the instructions below.

## License of Governance Documents

See [the governance introduction](intro.md) for license information.

## Infrastructure for this repository

The content in this repository is hosted online with `github-pages`, and the HTML
files are built with [MyST](https://mystmd.org). To build and preview
these documents locally, you can use [nox](https://nox.thea.codes):

```bash
# Build the documentation
nox -s docs

# Or serve with live reload
nox -s docs-live
```

Alternatively, install MyST directly and build manually:

```bash
pip install -r requirements.txt
cd docs
myst build --html
```

The resulting website will be in `docs/_build/html`, which you can explore by opening
any of the `.html` files that are created.

## Leadership Directory Data

The Leadership Directory is generated from structured data in `docs/_data/`.
See `docs/_data/README.md` for more information.

# Project Jupyter Governance

The purpose of this repository is to formalize the governance process for Project Jupyter. The governance documents are best viewed at https://jupyter.org/governance. They may also be built from the files in this repository by following the instructions below.

## License of Governance Documents

See [the governance introduction](intro.md) for license information.

## Infrastructure for this repository

The content in this repository is hosted online with `github-pages`, and the HTML
files are built with [jupyter-book](https://jupyterbook.org). To build and preview
these documents locally, install the latest version of Jupyter Book with:

```
pip install -U jupyter-book
```

and build the book with:

```
cd path/to/this/repo
jupyter-book build .
```

The resulting website will be in `_build/html`, which you can explore by opening
any of the `.html` files that are created.

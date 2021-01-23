# Project Jupyter Governance

The purpose of this repository is to formalize the governance process that the IPython/Jupyter project
has used informally since its inception in 2001. This document clarifies how decisions are made
and how the various elements of our community interact, including the relationship between
open source collaborative development and work that may be funded by for-profit or non-profit entities.

The governance documents are best-viewed at https://jupyter.org/governance

## Table of Contents

* [Main Governance Document](governance.md)
* [Current Steering Council and Institutional Partners](people.md)
* [New Subproject Incubation Process](newsubprojects.md)
* [Process for Authoring Jupyter Related Academic Papers](papers.md)

## License of Governance Documents

See [the governance introduction](intro.md) for license information.

## Jupyter organizations

The following organizations on GitHub contain Project Jupyter repos:

- [jupyter](https://github.com/jupyter)
- [ipython](https://github.com/ipython)
- [jupyterhub](https://github.com/jupyterhub)
- [jupyterlab](https://github.com/jupyterlab)
- [jupyter-widgets](https://github.com/jupyter-widgets)
- [jupyter-server](https://github.com/jupyter-server)

## Infrastructure for this repository

The content in this repository is hosted online with `github-pages`, and the HTML
files are built with [jupyter-book](https://jupyterbook.org). To build and preview
these documents locally, install the latest version of Jupyter Book with:

```
pip install -U git+https://github.com/executablebooks/jupyter-book.git
```

and build the book with:

```
cd path/to/this/repo
jupyter-book build .
```

The resulting website will be in `_build/html`, which you can explore by opening
any of the `.html` files that are created.

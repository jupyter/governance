(list-of-subprojects)=
# List of Official Jupyter Subprojects

Jupyter software development is carried out in [Software Subprojects](./software_subprojects). Within the Official Jupyter Subproject designation, there are two types of Subprojects: ones with a formal Subproject Council and SSC representation, and smaller, less active ones whose Subproject Council is the SSC itself. This document enumerates Subprojects of these two types.

## Official Subprojects with SSC representation

The following Jupyter Subprojects have their own formal Subproject Council that elects and maintains an SSC representative:

- [Jupyter Frontends](https://github.com/jupyterlab/frontends-team-compass)
  - [JupyterLab](https://github.com/jupyterlab/jupyterlab)
  - [Jupyter Notebook](https://github.com/jupyter/notebook)
  - [JupyterLite](https://github.com/jupyterlite/jupyterlite)
- [JupyterHub and Binder](https://github.com/jupyterhub/team-compass)
  - [JupyterHub](https://github.com/jupyterhub/jupyterhub)
  - [Binder](https://github.com/jupyterhub/binder)
  - [BinderHub](https://github.com/jupyterhub/binderhub)
  - [JupyterHealth](https://github.com/jupyterhealth)
- [Voilà](https://voila-dashboards.github.io/)
- [Jupyter Server](https://github.com/jupyter-server/team-compass)
  - [Jupyter Server](https://github.com/jupyter-server/jupyter_server)
  - [Enterprise Gateway](https://github.com/jupyter/enterprise_gateway)
  - [Kernel Gateway](https://github.com/jupyter/kernel_gateway)
- [Jupyter Widgets](https://github.com/jupyter-widgets/team-compass)
- [Jupyter Kernels](https://github.com/jupyter/kernels-team-compass)
  - [jupyter-xeus](https://github.com/jupyter-xeus/)
  - [IPykernel](https://github.com/ipython/ipykernel)
  - [IPython](https://github.com/ipython/ipython)
- [Jupyter Foundations and Standards](https://github.com/jupyter/foundations-and-standards-team-compass)
- [Jupyter Security](https://github.com/jupyter/security)
- [Jupyter Accessibility](https://github.com/jupyter/accessibility)
- [Jupyter Book](https://github.com/jupyter-book/team-compass)

## Official Subprojects without SSC representation

The following official Jupyter Subprojects are smaller and less active. As such their formal Subproject Council will be the SSC and they will not have an independent SSC delegate. Our expectation is that these smaller teams will basically continue working as they do today, making decisions using the consensus-seeking phase of the Jupyter Decision-Making Guidelines. Even though the SSC has decision-making authority over these projects, the SSC delegates all decisions that do not have broad cross-project implications to the Subproject maintainers. In the rare situation that a vote is called, the SSC will serve as the voting body and will consult closely with the Subproject maintainers. If one of these Subprojects grows or becomes more active, the SSC can, at any time, elect a standalone council for the Subproject, at which point, the Subproject will begin to have an SSC delegate of their own. In all other respects, these Subprojects are full and official Subprojects.

- nbdime (https://github.com/jupyter/nbdime)
- nbgrader (https://github.com/jupyter/nbgrader)
- nbviewer (https://github.com/jupyter/nbviewer)
- ipyparallel (https://github.com/ipython/ipyparallel)
- All other repos not listed above and that don't clearly fall into one of the official Subproject GitHub organizations above.

## Notes about Official Jupyter Subprojects

The Official Jupyter Subprojects document proposes a number of changes to how our repositories are organized into official Subprojects and GitHub organizations. This document describes the changes that are being proposed.

- Services
  - In general Jupyter services such as Binder, nbviewer, and the Jupyter website involve legal, financial, and operational matters. As such, we are proposing that the actual services are managed by working groups that report to the Executive Council, who can provide the needed support and oversight. For example, if we want to hire full or part time staff to maintain or operate these services, the Executive Council would be responsible for raising funds, hiring, and managing those staff.
  - The JupyterHub and Binder teams have a number of unique considerations. Currently all Binder repositories are under the Jupyterhub organizations, but there is a separate (but highly overlapping team) listed as the Binder team. These teams will need to work out if they would like to each have a formal Subproject Council with an SSC representative, or if they would like to have a single team. The Governance Working Group will be available to the JupyterHub and Binder teams to help working through these questions.
  - We propose that the Jupyter website and its repository will be governed by a working group that reports to the Executive Council.
  - We propose that the nbviewer service (only the actual live service) be governed by a working group that reports to the Executive Council. The reusable part of nbviewer contained (https://github.com/jupyter/nbviewer) will be an official Jupyter Subproject without SCC representation as described above.
- Jupyter Kernels
  - To consolidate the project’s work on first-party kernels, we propose to establish a new official Subproject called _Jupyter Kernels_ and create a Github organization named jupyter-kernels for the work of the Subproject. All Xeus repositories (https://github.com/jupyter-xeus) will be moved into this organization. This Subproject will also govern the IPython GitHub organization, which will be left in place (https://github.com/ipython).
  - A new Subproject Council for this organization will be established, and they will elect an SSC delegate.
- Jupyter Foundations and Standards
  - Ultimately, because Jupyter standards are cross-project in nature, they are owned by the SSC. The mechanics of day-to-day management of the JEP repo will be decided by the SSC.
  - There are a number of repositories that encode project-wide standards and protocols. To consolidate work on these repositories, we propose to establish a new official Subproject called Jupyter Standards and create a Github organization named jupyter-standards for the work of the Subproject. The following repositories will be moved into this organization:
    - Jupyter Client (https://github.com/jupyter/jupyter_client)
    - Jupyter Notebook Format (https://github.com/jupyter/nbformat)
    - Documentation for other specifications maintained by other Subprojects, such as the Jupyter Widgets message specification, or the Jupyter Server REST APIs.
    - JEPs repo (https://github.com/jupyter/enhancement-proposals).
  - Jupyter’s software has a number of components that serve as a foundation for many other Subprojects. To consolidate work on these repositories, we propose to establish a new official Subproject called _Jupyter Foundations_ and create a Github organization named jupyter-foundations for the work of the Subproject. The following repositories will be moved into this organization:
    - nbconvert (https://github.com/jupyter/nbconvert)
    - Jupyter Core (https://github.com/jupyter/jupyter_core)
    - Jupyter-packaging (https://github.com/jupyter/jupyter-packaging)
    - Terminado (https://github.com/jupyter/terminado)
    - nbclient (https://github.com/jupyter/nbclient)
    - Telemetry (https://github.com/jupyter/telemetry)
    - Traitlets (https://github.com/ipython/traitlets)
    - Jupyter Console (https://github.com/jupyter/jupyter_console)
    - Docker stacks (https://github.com/jupyter/docker-stacks)

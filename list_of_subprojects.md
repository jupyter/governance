# List of Official Jupyter Subprojects

At the highest level, any Github repository under any official Jupyter GitHub organization is either itself an Official Jupyter Subproject, or is part of an Official Jupyter Subproject. All such Subprojects have all of the privileges and responsibilities detailed in the Software Subprojects of Jupyter governance document. Within the Official Jupyter Subproject designation, there are two types of Subprojects: ones with a formal decision making body and SSC representation, and smaller, less active ones whose decision making body is the SSC itself. This document enumerates Subprojects of these two types.

### Official Subprojects with SSC representation

The following Jupyter Subprojects have their own formal decision making body that elects and maintains an SSC representative:

- JupyterLab (https://github.com/jupyterlab/jupyterlab)
- JupyterHub and Binder 
  - https://github.com/jupyterhub/jupyterhub
  - https://github.com/jupyterhub/binder
  - https://github.com/jupyterhub/binderhub
- Voilà (https://github.com/voila-dashboards/voila)
- Jupyter Server (https://github.com/jupyter-server/jupyter_server)
- Jupyter Widgets (https://github.com/jupyter-widgets)
- Jupyter Notebook (https://github.com/jupyter/notebook)
- Jupyter Kernels
  - jupyter-xeus (https://github.com/jupyter-xeus/)
  - IPykernel (https://github.com/ipython/ipykernel)
  - IPython (https://github.com/ipython/ipython)
- Jupyter Foundations
- Jupyter Standards
- Jupyter UX, Design and Branding
- Jupyter Enterprise

### Official Subprojects without SSC representation

The following official Jupyter Subprojects are smaller and less active. As such their formal decision making body will be the SSC and they will not have an independent SSC delegate. Our expectation is that these smaller teams will basically continue working as they do today, making decisions using the consensus seeking phase of the Jupyter Decision Making Guidelines. In the rare situation that a vote is called, the SSC will serve as the voting body and will consult closely with the team. If one of these Subprojects grows or becomes more active, the SSC can, at any time, elect a standalone decision making body for the Subproject, at which point, the Subproject will begin to have an SSC delegate of their own. In all other respects, these Subprojects are full and official Subprojects.

- nbdime (https://github.com/jupyter/nbdime)
- nbgrader (https://github.com/jupyter/nbgrader)
- ipyparallel (https://github.com/ipython/ipyparallel)
- QtConsole (https://github.com/jupyter/qtconsole). Note that QtConsole today is most actively maintained by the Spyder team; as part of this reorganization we will discuss with them whether it's more appropriate to move the project to be fully under their organization.
- All other repos not listed above and that don't clearly fall into one of the official Subproject GitHub organizations above.

## Notes about Official Jupyter Subprojects

The Official Jupyter Subprojects document proposes a number of changes to how our repositories are organized into official Subprojects and GitHub organizations. This document describes the changes that are being proposed.

- Services
  - In general Jupyter services such as Binder, nbviewer, and the Jupyter website involve legal, financial, and operational matters. As such, we are proposing that the actual services are managed by working groups that report to the Board of Directors, who can provide the needed support and oversight. For example, if we want to hire full or part time staff to maintain or operate these services, the Board of Directors would be responsible for raising funds, hiring, and managing those staff.
  - The JupyterHub and Binder teams have a number of unique considerations. Currently all Binder repositories are under the Jupyterhub organizations, but there is a separate (but highly overlapping team) listed as the Binder team. These teams will need to work out if they would like to each have a formal decision making body with an SSC representative, or if they would like to have a single team. The Governance Working Group will be available to the JupyterHub and Binder teams to help working through these questions.
  - We propose that the Jupyer website and its repository will be governed by a working group that reports to the Board of Directors.
  - We propose that the nbviewer service (only the actual live service) be governed by a working group that reports to the Board of Directors. The reusable part of nbviewer contained (https://github.com/jupyter/nbviewer) will be governed by the Jupyter Enterprise Subproject.
- Jupyter Kernels
  - To consolidate the project’s work on first-party kernels, we propose to establish a new official Subproject called _Jupyter Kernels_ and create a Github organization named jupyter-kernels for the work of the Subproject. All Xeus repositories (https://github.com/jupyter-xeus) will be moved into this organization. This Subproject will also govern the IPython GitHub organization, which will be left in place (https://github.com/ipython).
  - A new decision making body for this organization will be established, and they will elect an SSC delegate.
- Jupyter Standards
  - There are a number of repositories that encode project-wide standards and protocols. To consolidate work on these repositories, we propose to establish a new official Subproject called Jupyter Standards and create a Github organization named jupyter-standards for the work of the Subproject. The following repositories will be moved into this organization:
    - Jupyter Client (https://github.com/jupyter/jupyter_client)
    - Jupyter Notebook Format (https://github.com/jupyter/nbformat)
    - Documentation for other specifications maintained by other Subprojects, such as the Jupyter Widgets message specification, or the Jupyter Server REST APIs.
    - JEPs repo (https://github.com/jupyter/enhancement-proposals). The entire SSC votes on JEPs, but the standards group is the day-to-day steward of the repo.
- Jupyter Enterprise
  - A number of Jupyter repositories pertain to enterprise deployments. To consolidate work on these repositories, we propose to establish a new official Subproject called _Jupyter Enterprise_ and create a Github organization named jupyter-enterprise for the work of the Subproject. The following repositories will be moved into this organization:
  - Enterprise Gateway (https://github.com/jupyter/enterprise_gateway)
  - Kernel Gateway (https://github.com/jupyter/kernel_gateway)
  - Docker stacks (https://github.com/jupyter/docker-stacks)
  - Jupyter Notebook Viewer (https://github.com/jupyter/nbviewer)
- Jupyter Foundations
  - Jupyter’s software has a number of components that serve as a foundation for many other Subprojects. To consolidate work on these repositories, we propose to establish a new official Subproject called _Jupyter Foundations_ and create a Github organization named jupyter-foundations for the work of the Subproject. The following repositories will be moved into this organization:
    - nbconvert (https://github.com/jupyter/nbconvert)
    - Jupyter Core (https://github.com/jupyter/jupyter_core)
    - Jupyter-packaging (https://github.com/jupyter/jupyter-packaging)
    - Terminado (https://github.com/jupyter/terminado)
    - nbclient (https://github.com/jupyter/nbclient)
    - Telemetry (https://github.com/jupyter/telemetry)
    - Traitlets (https://github.com/ipython/traitlets)
    - Jupyter Console (https://github.com/jupyter/jupyter_console)

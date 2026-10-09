# Software Subprojects

Software design and development in Project Jupyter is organized into a set of Software Subprojects. The lifecycle of Software Subprojects is described in detail [here](newsubprojects.md). A list of Subprojects is [here](./list_of_subprojects.md).

## Responsibilities of Jupyter Subprojects

Unless the [Software Steering Council (SSC)](./software_steering_council.md) or the [Executive Council (EC)](./executive_council.md) says otherwise, Subprojects self-govern as autonomously as possible, while following the overall governance model and processes of Project Jupyter. Specifically, all Subprojects under Jupyter’s governance have the following responsibilities:

- Adhere to the [Jupyter Code of Conduct](./conduct/code_of_conduct.md).
- Adhere to the [Jupyter Decision-Making Guidelines and process](decision_making.md).
- Where applicable, nominate and maintain a single representative to the SSC.
- Follow the Jupyter [licensing guidelines and practices](./projectlicense.md).
- Follow the Jupyter [trademark, branding, and intellectual property guidelines](./trademarks.md).
- Conduct its activities in a manner that is open, transparent, and inclusive. This includes coordinating with the SSC and EC on mechanisms for information flow and updates to the broader community.
- Maintain Subproject source code on GitHub in the [Project Jupyter GitHub enterprise organization](https://github.com/enterprises/jupyter).
- Ensure that Python packages published on PyPI are under the [Jupyter PyPI
  organisation](https://pypi.org/org/jupyter/).
- Maintain a publicly visible Team Compass with a list of the Subproject Council members.

## Incubator Subprojects

Incubator Subprojects are experimental and early-stage efforts where ideas are being explored and developed in the open and under the principles of Jupyter’s governance.  Therefore, Subprojects under incubation have the same responsibilities listed above for official Jupyter projects.

The [Jupyter Incubator GitHub organization](https://github.com/jupyter-incubator) serves as a home for all Incubator Subprojects and has further details on the process to create and approve them. This organization serves as a neutral playing ground for people who can’t easily create their own repositories.

## SSC Representation

Official Jupyter Software Subprojects that have large and active enough teams to have a standalone, formal Subproject Council will elect and maintain a single representative to the SSC. The Subproject Council of each such Subproject is free to set term limits or rotate this responsibility as they see fit.

**Current SSC Representatives:**

```{team-members} software_steering_council
```

There exist two categories of Subprojects that, while operating under Jupyter’s governance, do not have a dedicated delegate to the SSC:

- There are a number of smaller and/or low-activity Subprojects that don’t have enough active participants to have a standalone Subproject Council. The SSC itself will be the formal Subproject Council for these Subprojects when necessary, while otherwise allowing the team to manage its day-to-day activities.
- Projects in the Jupyter Incubator will only acquire official SSC representation if/once they graduate to official Jupyter Subproject status.

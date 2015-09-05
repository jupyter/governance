# New subproject process

Project Jupyter is organized as a set of Subprojects that are each a GitHub repository with a
development team that follows the Jupyter governance and contribution model. Officially supported
and maintained subprojects are hosted on the `jupyter` GitHub orgnization. This document
describes the process by which new Subprojects are created in or moved to the `jupyter`
organization.

There are two ways that new Subprojects are created:

1. Direct subproject creation
2. Incorporation of an existing, external subproject

## Criteria for official subprojects

The following criteria will be used in evaluating Subprojects for incorporation into the official
Jupyter organization. These apply to any Subproject, regardless of who is developing the
subproject. Subprojects should:

* Have an active developer community that offers a sustainable model for future development.
* Active user community.
* Use solid software engineering with documentation and tests hosted with appropriate
  technologies (readthedoc, Travis are examples of technologies that can be used).
* Demonstrate continued growth and development.
* Integrate well with the rest of the project.
* Be developed according to the Jupyter governance and contribution model.
* Have a well-defined scope.
* Be well packaged using appropriate technologies such as pip, conda, npm, bower, docker, etc.
* Not canibalize or fork and existing official subproject.

The most important question in evaluating subprojects for incorporation as official Subprojects
is this: is there broad agreement in the community and Steering Council that we are going to
develop and maintain the Subproject in an official capacity?

## Direct subproject creation

In some cases, Steering Council members can immediately create new offcial Subprojects in the main Jupyter organization. This option will be used when the new Subproject is clearly part of the existing scope, activities and development of the project. The process for this direct Subproject is minimal and informal: Steering Council members should be in consensus about the Subproject's creation and notify the main Jupyter list of its creation.

## Incorporation of an existing, external subproject

In other cases, Subprojects proposed for incorporation will have existed for some time outside the Jupyter organization. This section describes the incorporation process for these existing, external subprojects. This process applies to Subprojects that have incubated under the `jupyter-incubatror` GitHub organization, Subprojects developed under other GitHub organizations or even Subprojects developed in other public version control systems.

When a Subproject is incorporated, it becomes an officialy supported and maintained part
of Project Jupter and is moved to the jupyter GitHub organization.

### Proposal for incorporation

For an existing, external Subproject to be incorporated into the main Jupyter organization, the
following proposal process will be used:

1. The Subproject team should submit a pull request against the
   [jupyter/enhancement-proposals](https://github.com/jupyter/enhancement-proposals) repository
   with an enhancement proposal for including the subproject in the main Jupyter organization.
2. The proposal for incorporation will be discussed by the community.
3. A recommendation will be made by the consensus of the Steering Council.

The possible recommendations of the Steering Council wil be:

* Integration into an existing official Suproject.
* Graduation into a new official Subproject.
* Further internal or external incubation (see below) with recommendations on steps the team can
  take to prepare for future incorporation.
* Rejection. This option will be used if the Steering Council thinks the proposed Subproject not
  progressing or will never be appropriate for graduation. If a rejected Subproject has been
  incubating under the `jupyter-incubator` GitHub organization, its repository will be removed
  from that organization after a transition period.

### Incorporation

When a subproject is incorporated as a new official Subproject, the following steps
will be taken:

1. The repository will be transfered over to the main `jupyter` GitHub organization.
2. A GitHub team will be created for the Subproject, with read/write permissions on the
   Subproject repository.
3. The team will send an Email the main Jupyter list with an announcement about the new
   Subproject.
4. The standard Jupyter LICENSE file will be added to the repository.

## Incubation of subprojects

If there are questions about whether the incubation process applies to a given Subproject,
interested parties should simply start a discussion on the main Jupyter list to get community
and Steering Council feedback.

### Incubation in the `jupyter-incubator` organization

In some cases it will make sense
The incubation process doesn't apply to all new Subprojects, only those with the following
characteristics:

* Significant unanswered technical questions or uncertainties that require exploration.
* Entirely new directions, scopes or ideas that haven't been vetted with the community.
* Significant, already existing code bases where it is not clear how the project will
  integrate with the rest of Jupyter.
 
The goals of the incubation process are:

* Contributors can quickly and easily get their code exposed to the Jupyter community while
  complying with individual and organizational contribution restrictions.
* Contributors can work with the community and gather feedback that will help them develop and
  refine a clear and concise integration proposal.
* The broader community can easily distinguish between stable, officially supported
  and maintained Subprojects in the main GitHub organization and new efforts that are
  emerging and being developed for future inclusion.
* Enables the core development team to assess the readiness and applicability of proposed
  technologies against a backdrop of the broader project design efforts.
* Allow the community and Steering Council to re-evaluate existing Subprojects in the main
  jupyter GitHub organizations to determine if any need to be moved to jupyter-incubator.
* Allow the community to make sure that Subprojects develop into something that is
  appropriate to become an officially supported and maintained part of the project.

### Proposal for incubation

A Subproject enters into incubation by submitting a proposal for incubation. This process is
designed to be lightweight and quick:

1. The proposers must fill out incubation application by sumitting a pull request to the
   [jupyter-incubator/proposals](https://github.com/jupyter-incubator/proposals) repository.
2. Proposers must announce their intent to the community with a post to the main Jupyter
   list.
2. The proposed Subproject must have an Advocate who is an active Steering Council member.
3. The proposal for incubation will be discussed by the community and approved or rejected by
   the consensus of the Steering Council.
4. If approved, the proposal pull request will be merged, if rejected, it will be closed.

### Incubation period

Once a project has become an incubation Subproject, the following steps will be taken:

1. A GitHub repo will be created under the jupyter-incubator organization
2. A GitHub team will be created with read/write access to the repo, including the
   Advocate.
3. The standard Jupyter LICENSE file will be added to the repository.
4. A member of the Steering Council will announce the newly incubated Subproject on the
   main Jupyter list.

The goal of the incubation period is to demonstrate that the Subproject is going to develop an
with an active developer and user community. There is no particular length of time required,
but most projects will be in incubation for at least 6 months to 1 year.

## External incubation









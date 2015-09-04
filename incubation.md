# Jupyter Incubation Process

Incubation is the process by which certain types of new Jupyter Subprojects are created and
evaluated for inclusion in the main Jupyter organization. In this context a Subproject is a
GitHub repository with a development team that follows the Jupyter governance and contribution
model.

The incubation process doesn't apply to all new Subprojects, only those with the following
characteristics:

* Significant unanswered technical questions that required exploration.
* Entirely new directions, scopes or ideas that haven't been vetted with the community.
* Significant, already existing code bases where it is not clear how the project will
  integrate with the rest of Jupyter.
 
Most importantly, the incubation process does not apply to new Subprojects that are
created in the natural development of existing officially supported Subproject in the
main jupyter GitHub organization.

If there are questions about whether the incubation process applies to a given Subproject,
interested parties should simply start a discussion on the main Jupyter list to get community
and Steering Council feedback. The most important question in making this determination is
this: is there broad agreement in the community and Steering Council that we are undertaking
this activity in an official capacity. If this agreement exists, Steering Council members can
immediately create new offcial subprojects in the main Jupyter organization.

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
* Allows the community and Steering Council to re-evaluate existing Subprojects in the main
  jupyter GitHub organizations to determine if any need to be moved to jupyter-incubator.
* Allow the community to make sure that Subprojects develop into something that is
  appropriate to become an officially supported and maintained part of the project.


## Proposal for incubation

A Subproject enters into incubation by submitting a proposal for incubation. This process is
designed to be lightweight and quick:

1. The proposers must fill out incubation application by sumitting a pull request to the
   jupyter-incubator/proposals repository.
2. Proposers must announce their intent to the community with a post to the main Jupyter
   list.
2. The proposed Subproject must have a mentor/sponsor/champion who is an active Steering
   Council member.
3. The proposal for incubation will be discussed by the community and approved or rejected by
   the consensus of the Steering Council.
4. If approved, the proposal pull request will be merged, if rejected, it will be closed.


## Incubation period

Once a project has become an incubation Subproject, the following steps will be taken:

1. A GitHub repo will be created under the jupyter-incubator organization
2. A GitHub team will be created with read/write access to the repo, including the
   mentor/sponsor/champion.
3. The standard Jupyter LICENSE file will be added to the repo.
4. A member of the Steering Council will announce the newly incubated Subproject on the
   main Jupyter list.

The goal of the incubation period is to demonstrate that the Subproject is going to develop an
with an active developer and user community. There is no particular length of time required,
but most projects will be in incubation for at least 6 months to 1 year.

## Proposal for graduation from incubation

When an incubating Subproject graduates, it becomes an officialy supported and maintained part
of Project Jupter and is moved to the jupyter GitHub organization. When it is moved over, it
also starts to be developed according to the Jupyter governance and contribution model that is
documented in this governance document.

To graduate from the incubation period, the following process will be used:

1. The Subproject team should submit a second pull request against the
   jupyter-incubator/proposals repository that completes the second half of the incubator
   proposal.
2. The proposal for graduation will be discussd by the community.
3. A recommendation will be made by the consensus of the Steering Council.

The possible recommendations of the Steering Council wil be:

* Further incubation with recommendations on steps the team can take to prepare for future
  graduation.
* Forced termination. In this case, incubating Subproject will be shut down and removed
  from the incubation repository. This option will be used if the Steering Council thinks
  the Subproject has stopped progressing or will never be appropriate for graduation.
* Integration into an existing official Suproject.
* Graduattion into a new official Subproject.

## Criteria for graduation

The following criteria will be used in evaluating Subprojects for graduation.

* Active developer community that offers a sustainable model for future development.
* Active user community.
* Solid software engineering with documentation and tests hosted with appropriate
  technologies (readthedoc, Travis are examples of technologies that can be used).
* Demonstrates continued growth and development.
* Integration with the rest of the project.
* Willingness to submit to the Jupyter governance and contribution model.
* Well-defined scope.
* Well packaged using appropriate technologies such as pip, conda, npm, bower, docker, etc.

## Graduation

When a project graduates from incubation into a new official Subproject, the following steps
will be taken:

1. Transfer the GitHub repo over to the main `jupyter` GitHub organization.
2. Make a new GitHub team for the Subproject.
3. Email the main Jupyter list with an announcement about the new Subproject.

## Questions

* Do we want to introduce the idea of a repository/Subproject maintainer?
* Which repo do we want to use for the incubator proposals?
* Mentor? Sponsor? Champion?




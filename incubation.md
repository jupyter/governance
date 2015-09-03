# Jupyter Incubation Process

Incubation is the process by which new Jupyter Subprojects are created and evaluated for inclusion in the main Jupyter organization. In this context a Subproject is a GitHub repository with a development team that follows the Jupyter governance and contribution model. The goals of the incubation process are:

* Contributors can quickly and easily get their code exposed to the Jupyter community while complying with corporate contribution restrictions.
* Contributors can work with the community and gather feedback that will help them develop and refine a clear and concise integration proposal.
* The broader user community can easily distinguish between stable core project feature functions and what is on the docket for potential future integration.
* Enables the core development team to assess the readiness an applicability of proposed technologies against a backdrop of the broader project design efforts. 
* Allows the core team to re-evaluate existing jupyter org repos to determine if any need to be moved to jupyter-incubator.

## Proposal for incubation

A subproject enter into incubation by submitting a proposal for incubation. This process is designed to be lightweight and quick:

1. The proposers should fill out incubation application by sumitting a pull request to the
   jupyter-incubator/proposals repository.
2. The proposed subproject must have a mentor/sponsor/champion who is an active Steering 
   Council member.
3. The proposal for incubation will be discussed by the community and approved or rejected
   by the consensus of the Steering Council.
4. If approved the proposal PR will be merged, if rejected, it will be closed.

## Incubation period

Once a project has become an incubation subproject, the following steps will be taken:

1. A GitHub repo will be created under the jupyter-incubator organization
2. A GitHub team will created with read/write accees to the repo, including the
   mentor/sponsor/champion.
3. Standard Jupyter LICENSE file will be added to the repo.

The goal of the incubation period is to demonstrate that the subproject is going to take off
with an active developer and user community. There is no particular length of time required,
but most projects will be in incubation for at least 6 months to 1 year.

## Proposal for graduation from incubation

When a incubating subproject graduates, it becomes an official part of Project Jupter and
is moved to the jupyter GitHub organization.

To graduate from the incubation period, a subproject should submit a second pull request
against the jupyter-incubator/proposals repo that completes the second half of the incubator
proposal.

* Initiated by a second PR against the proposals repo that finishes the rest of the application.
* Requires consensus of the Steering Council.
* Three outcomes
  - More incubation with recommendations
  - Voluntary retiremet.
  - Forced termination.
  - Gradution as a new core project.
  - Integration into existing core project.

## Criteria for graduation

The following criteria will be used in evaluating subprojects for graduation.

* Active developer community that offers a sustainable model for future development.
* Active user community.
* Solid software engineering with docs on readthedocs, tests, Travis.
* Demonstrates continuing growth and development.
* Integration with the rest of the project.
* Willingness to submit to the Jupyter governance model.
* Well defined scope
* Well packaged (pip, conda, npm, bower, docker)

## Graduation

* Transfer GitHub repo over to jupyter org.
* Make team for the project.


## Questions

* Do we want to introduce the idea of a repository/subproject maintainer?
* 




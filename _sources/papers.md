# Process for Authoring Jupyter Related Academic Papers

This document describes the processes used to author Jupyter related academic
papers, which are typically submitted to peer-reviewed journals. This does not
include talks and posters submitted to conferences unless the conference also
publishes written proceedings.

On one hand, the primary focus of Project Jupyter is on producing open-source
software. We are very much focused on writing code that delights our users. On
the other hand, Jupyter (and IPython) emerged out of an acadmic setting, where
research and peer-reviwed publications are a primary focus. To this day, many
of our core contributors have academic positions and active research programs.
This emphasis is also reflected in the usage of Jupyter across all areas of
scientific research. Thus, in spite of a focus on writing software for users,
Jupyter remains a tool that is by and for researchers.

Given this focus on research, the ongoing academic careers of many Jupyter
contributors, and our desire to have an impact on computing research, it is
important for us to author and publish peer-reviewed papers on Jupyter itself.
Authoring these papers in the context of a large, open-source community
presents a number of differences compared to many research collaborations.

## Principles

We have tried to create a process for authoring papers with the following
general principles in mind:

* **Inclusivity and generosity in authorship.** Hundreds of individuals have
  contributed to the different Jupyter subprojects. These contributions span
  code, design, documentation, discussions, giving talks/tutorials, etc. We
  want to be generous in extending authorship privileges and responsibilities
  to as many of these contributors as possible.
* **Clear, explicit criteria for authorship.** While being generous, we want
  have concrete, specific and auditable criteria for including individuals as
  authors.
* **Openness.** The process of authoring papers should be open in the same way
  as the rest of the project's work. Thus, all of our papers are written in the
  public on GitHub.
* **Accountability.** Being an author on a paper is a privilege, but also
  involves responsibilities. The concrete processes described below elucidate
  these responsibilities.

We expect to author and submit papers to different types of journals. Different
journals will have slightly different concrete processes that appropriately
embody these principles.

## Author ordering

In some academic fields, author ordering is used to implicitly communicate the level and significance of the individual's contributions. We strongly feel this
is misleading and misguided. Because of this, all Jupyter papers will use the
following author ordering policy:

* The first author will be listed as "Project Jupyter";
* Individual authors will follow in alphabetical order; and
* An explicit statement about the ordering will be included in the paper.

Listing the first author as "Project Jupyter" is important as it means that in
abbreviated citations, the author list will be "Project Jupyter, et al." rather
than artificially showing the first alphabetical author's name. This is common
practice in academic field such as high energy physics where there are large
numbers of authors on papers.

## Process for Journal of Open Source Software (JOSS)

The [Journal of Open Source Software](http://joss.theoj.org/) (JOSS) is a
peer-reviewed, developer-friendly journal for research related software. JOSS
is unique in that:

* Each paper is associated with a single GitHub repository;
* The primary research artifact in the software itself; and
* The paper itself is a relatively brief markdown file in the software's GitHub
  repository, deferring details of the software to its own documentation.

It is our intention to publish a JOSS paper for each of our main, user-focused
subprojects (Notebook, JupyterLab, JupyterHub, nbconvert, ipywidgets, etc.).
All such paper should use the process described herein.

### JOSS authorship criteria

Our authorship criteria for JOSS papers are derived from those of the
[ICMJE](http://www.icmje.org/recommendations/browse/roles-and-responsibilities/defining-the-role-of-authors-and-contributors.html#two):

* Substantial contributions to the conception, design, or implementation of
  software; this includes coding, visual design, documentation, testing,
  discussions and other such contributions; AND
* Final approval of the version to be published; AND
* Agreement to be accountable for all aspects of the work in ensuring that
  questions related to the accuracy or integrity of any part of the work are
  appropriately investigated and resolved.

Anyone who satisfies and is willing to accept these responsibilities and commitments is welcome to be an author on any of our JOSS publications.

### JOSS process

The following process should be used to author any Jupyter related JOSS paper:

#### 1. Someone agrees to be the Coordinator for a paper

A single JOSS paper will be associated with a single Jupyter repository. The
Coordinator will usually be a senior project contributor, Steering Council
member, or leader of that subproject.

The role of the Coordinator is to implement this process for that paper. They
do not have to write the JOSS paper themselves, but they will work with the
community to organize the writing of the paper.

#### 2. Open an issue and announce the writing of the paper

The Coordinator should open an issue to organize the writing of the paper on
that repository and then announce to the Jupyter Google Group that the paper is
being worked on and that anyone can contribute (with a link to the issue).

#### 3. Draft the paper in the repository

At this point, the Coordinator should organize the writing of the actual paper.

The [JOSS Author Guidelines](http://joss.theoj.org/about) detail the format and
requirements of a JOSS paper. In general this will involve creating a `paper`
subdirectory in the root of the repository with two files: `paper.md` and
`paper.bib`. The paper should be written using our standard processes for pull
requests and code review.

#### 3. Email potential authors

Once a final draft of the paper has been merged into the repository, the
Coordinator should email all potential authors of the paper, inviting them to
participate. Usually this will include at least two emails:

* Individually email all contributors listed in the Git log of the repository.
  This list can be generated using the Git command `git log --all --format='%cN
  <%cE>' | sort -u`.
* Email the main Jupyter Google Group to include folks not listed in the Git
  log.

In addition, the Coordinator should send personal emails to individuals, such
as students, who are new to writing academic publications, explaining why we
are writing a paper, and encouraging them to participate. These personal emails
should cc the individual's mentor or advisor if applicable.

Both of these emails should include:

* A verbatim copy of the above JOSS authorship criteria;
* A description the tasks each individual needs complete to be an author on the
  paper;
* A concrete deadline for completing those tasks (at least 2 weeks out); and
* A link to the paper's markdown file in the repository.

The tasks each individual needs to complete are as follows:

* Create an account on [ORCID](http://orcid.org/).
* Submit a PR to the repository adding their name, ORCID id, and affiliation to
  the paper;
* Provide any edits to the content of the paper;
* In the comment of the PR, briefly describe their contributions to the work;
  and
* In the comment of the PR, provide verification that they have read the paper
  and agree to its publication.

As the deadline approaches, the Coordinator should remind potential authors to
complete their tasks.

#### 4. Final submission

Once the deadline for authors to complete their tasks has passed, the
Coordinator should make sure authors are listed in alphabetical order. The
Coordinator can then submit the paper.

### Process for traditional academic papers

Papers submitted to other (non-JOSS) journals, will usually be longer and take
a more significant amount of time to author. They will also usually be authored
in dedicated repository (under the jupyter-resources GitHub organization).
Because of these factors, the process is slightly different.

### Authorship criteria

The authorship criteria for non-JOSS papers is slightly different than for JOSS
in that all authors are expected to actively participate in the writing and
editing of the paper.

Our authorship criteria for papers are derived from those of the
[ICMJE](http://www.icmje.org/recommendations/browse/roles-and-responsibilities/defining-the-role-of-authors-and-contributors.html#two):

* Substantial contributions to the conception, design, or implementation of
  software; this includes coding, visual design, documentation, testing,
  discussions and other such contributions; AND
* Drafting the work or revising it critically for important intellectual
  content; AND
* Final approval of the version to be published; AND
* Agreement to be accountable for all aspects of the work in ensuring that
  questions related to the accuracy or integrity of any part of the work are
  appropriately investigated and resolved.

Anyone who satisfies and is willing to accept these responsibilities and
commitments is welcome to be an author on any of our publications.

The second of these responsibilities implies that all authors will actively
participate in the writing of the manuscript. We recognize that not all
co-authors will contribute equally and in the same way to the writing of a
paper. Furthermore, for papers with large numbers of co-authors, we expect the
main writing will be done by a smaller group of co-authors, with other
co-authors contributing to editing work and discussions. However, in all cases active participation in some manner is still required.

### Process

Before creating the detailed process for authoring non-JOSS papers, we want to
try out the above process for JOSS papers and see how it should be modified for
longer form papers. In general, we expect to closely follow the process used in
the SymPy project to author [this paper](https://github.com/sympy/sympy-paper).

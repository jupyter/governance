# Leadership Data Files

This directory contains the source data for Jupyter governance and leadership.

## Files

- **contributors.yml** - People data in MyST authors format
- **organizations.yml** - Organization affiliations in MyST affiliations format
- **jupyter-teams.yml** - Jupyter governance team definitions

These files are used by the `{team-members}` MyST directive to render team membership lists.

## Generated Markdown Tables

When the documentation is built, the `{team-members}` directive automatically generates downloadable markdown tables for each team. These files are available in the built site at:

jupyter.org/governance/build/team-tables/<team-id>.md`

These markdown files can be downloaded and reused in other documentation projects.

## Editing

To update team membership:

1. Edit the appropriate YAML file (_data/contributors.yml, _data/organizations.yml, or _data/jupyter-teams.yml)
2. Rebuild the documentation: `nox -s docs`
3. New markdown tables will be automatically generated in `_build/html/build/team-tables/`

## Adding a new team member

1. If they're not in `_data/contributors.yml`, add them to the `authors` list
2. Add the team to their `teams` list with appropriate metadata (term, subproject, organization)
3. Rebuild docs

## Adding a new team

1. Add team definition to `_data/jupyter-teams.yml`
2. Add team memberships to contributors in `_data/contributors.yml`
3. Add `{team-members} <team-id>` directive to the appropriate page
4. Rebuild docs

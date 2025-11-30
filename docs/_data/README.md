# Leadership Data Files

This directory contains the source data for Jupyter governance and leadership.

## Files

### leadership.yml (Deprecated - kept for reference)

The original leadership data file. This is no longer used but kept for historical reference.

### Migration to MyST-native system

Leadership data has been migrated to MyST-compliant YAML files:

- **contributors.yml** - People data in MyST authors format (in _data/)
- **organizations.yml** - Organization affiliations in MyST format (in _data/)
- **jupyter-teams.yml** - Jupyter governance team definitions (in _data/)

These files are used by the `{team-members}` MyST directive to render team membership lists.

## Editing

To update team membership:

1. Edit the appropriate YAML file (_data/contributors.yml, _data/organizations.yml, or _data/jupyter-teams.yml)
2. Rebuild the documentation: `nox -s docs` or `cd docs && myst build --html`
3. Verify changes locally: `nox -s docs-live` or `cd docs && myst start`

## Adding a new team member

1. If they're not in _data/contributors.yml, add them to the `authors` list
2. Add the team to their `teams` list with appropriate metadata (term, subproject, organization)
3. Rebuild docs

## Adding a new team

1. Add team definition to `_data/jupyter-teams.yml`
2. Add team memberships to contributors in `_data/contributors.yml`
3. Add `{team-members} <team-id>` directive to the appropriate page
4. Rebuild docs

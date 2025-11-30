/**
 * MyST directive plugin for rendering Jupyter team member lists
 */
import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

/**
 * Load YAML file
 */
function loadYaml(filepath) {
  const content = fs.readFileSync(filepath, 'utf8');
  return yaml.load(content);
}

/**
 * Team members directive
 */
const teamMembersDirective = {
  name: 'team-members',
  arg: {
    type: String,
    required: true,
  },
  run(data) {
    const teamId = data.arg;

    // Load data files
    const contributors = loadYaml(path.join(process.cwd(), 'contributors.yml'));
    const organizations = loadYaml(path.join(process.cwd(), 'organizations.yml'));
    const teams = loadYaml(path.join(process.cwd(), 'jupyter-teams.yml'));

    // Filter authors for this team
    const teamMembers = getTeamMembers(contributors.authors, teamId, teams);

    // Generate table AST
    const tableAst = generateTableAst(teamMembers, organizations.affiliations, teamId);

    return [tableAst];
  },
};

/**
 * Get team members for a given team ID
 */
function getTeamMembers(authors, teamId, allTeams) {
  // Special case: union of councils
  if (teamId === 'union_of_councils') {
    return getUnionOfCouncilsMembers(authors, allTeams);
  }

  const members = [];

  for (const author of authors) {
    if (!author.teams) continue;

    for (const team of author.teams) {
      if (team.team === teamId) {
        members.push({
          ...author,
          teamData: team,
        });
        break;
      }
    }
  }

  // Sort alphabetically by first name
  members.sort((a, b) => {
    const firstNameA = a.name.split(' ')[0];
    const firstNameB = b.name.split(' ')[0];
    return firstNameA.localeCompare(firstNameB);
  });

  return members;
}

/**
 * Get Union of Councils members (SSC + all active committees/working groups)
 */
function getUnionOfCouncilsMembers(authors, allTeams) {
  // Find all team IDs that are NOT former teams
  const activeTeamIds = allTeams.teams
    .filter(team => !team.id.startsWith('former_'))
    .filter(team => team.id !== 'union_of_councils')
    .map(team => team.id);

  // Collect unique author IDs
  const uniqueAuthorIds = new Set();
  const authorMap = new Map();

  for (const author of authors) {
    if (!author.teams) continue;

    for (const team of author.teams) {
      if (activeTeamIds.includes(team.team)) {
        uniqueAuthorIds.add(author.id);
        authorMap.set(author.id, author);
        break;
      }
    }
  }

  // Convert to array and sort
  const members = Array.from(uniqueAuthorIds).map(id => ({
    ...authorMap.get(id),
    teamData: {}, // No specific team data for union
  }));

  members.sort((a, b) => {
    const firstNameA = a.name.split(' ')[0];
    const firstNameB = b.name.split(' ')[0];
    return firstNameA.localeCompare(firstNameB);
  });

  return members;
}

/**
 * Generate table AST
 */
function generateTableAst(members, affiliations, teamId) {
  // Detect which columns we need
  const columns = detectColumns(members);

  // Generate header row
  const headerRow = {
    type: 'tableRow',
    children: columns.map(col => ({
      type: 'tableCell',
      header: true,
      align: 'left',
      children: [{ type: 'text', value: col.header }],
    })),
  };

  // Generate data rows
  const dataRows = members.map(member => ({
    type: 'tableRow',
    children: columns.map(col => ({
      type: 'tableCell',
      align: 'left',
      children: col.render(member, affiliations),
    })),
  }));

  return {
    type: 'table',
    children: [headerRow, ...dataRows],
  };
}

/**
 * Detect which columns to display based on team data
 */
function detectColumns(members) {
  const columns = [
    {
      header: 'Name',
      render: (member) => [{ type: 'text', value: member.name }],
    },
  ];

  // Check if any member has subproject
  if (members.some(m => m.teamData.subproject)) {
    columns.push({
      header: 'Subproject',
      render: (member) => [
        { type: 'text', value: member.teamData.subproject || '' },
      ],
    });
  }

  // Check if any member has organization
  if (members.some(m => m.teamData.organization)) {
    columns.push({
      header: 'Organization',
      render: (member, affiliations) => {
        const org = member.teamData.organization;
        if (!org) return [{ type: 'text', value: '' }];

        // Check if this org has a URL in affiliations
        const affiliation = affiliations.find(a => a.name === org);
        if (affiliation && affiliation.url) {
          return [{
            type: 'link',
            url: affiliation.url,
            children: [{ type: 'text', value: org }],
          }];
        }

        return [{ type: 'text', value: org }];
      },
    });
  }

  // Always add GitHub column
  columns.push({
    header: 'GitHub',
    render: (member) => {
      if (!member.github) return [{ type: 'text', value: '' }];

      const username = member.github.replace('https://github.com/', '');
      return [{
        type: 'link',
        url: member.github,
        children: [{ type: 'inlineCode', value: `@${username}` }],
      }];
    },
  });

  // Check if any member has term
  if (members.some(m => m.teamData.term)) {
    columns.push({
      header: 'Term',
      render: (member) => [
        { type: 'text', value: member.teamData.term || '' },
      ],
    });
  }

  return columns;
}

/**
 * Plugin export
 */
const plugin = {
  name: 'jupyter-team-members',
  directives: [teamMembersDirective],
};

export default plugin;

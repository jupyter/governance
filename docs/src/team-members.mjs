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
  run(data, vfile, ctx) {
    const teamId = data.arg;

    // Load data files
    const contributors = loadYaml(path.join(process.cwd(), '_data/contributors.yml'));
    const organizations = loadYaml(path.join(process.cwd(), '_data/organizations.yml'));
    const teams = loadYaml(path.join(process.cwd(), '_data/jupyter-teams.yml'));

    // Filter authors for this team
    const teamMembers = getTeamMembers(contributors.authors, teamId, teams);

    // Generate markdown table
    const markdown = generateMarkdownTable(teamMembers, organizations.affiliations, teamId);

    // Write markdown table to file
    writeTableFile(teamId, markdown);

    // Parse markdown to AST and return
    const ast = ctx.parseMyst(markdown);
    return ast.children;
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
 * Write markdown table to file in build directory
 */
function writeTableFile(teamId, markdown) {
  try {
    const outputDir = path.join(process.cwd(), '_build/site/public/team-tables');
    const outputFile = path.join(outputDir, `${teamId}.md`);

    // Create directory if it doesn't exist
    fs.mkdirSync(outputDir, { recursive: true });

    // Write markdown file
    fs.writeFileSync(outputFile, markdown, 'utf8');
  } catch (error) {
    // Log warning but don't crash the build
    console.warn(`Warning: Failed to write team table file for ${teamId}:`, error.message);
  }
}

/**
 * Generate markdown table string
 */
function generateMarkdownTable(members, affiliations, teamId) {
  // Detect which columns we need
  const columns = detectColumns(members);

  // Generate header row
  const headers = columns.map(col => col.header).join(' | ');
  const separator = columns.map(() => '---').join(' | ');

  // Generate data rows
  const rows = members.map(member => {
    const cells = columns.map(col => col.render(member, affiliations));
    return cells.join(' | ');
  });

  // Combine into markdown table
  return `| ${headers} |\n| ${separator} |\n${rows.map(row => `| ${row} |`).join('\n')}`;
}

/**
 * Detect which columns to display based on team data
 */
function detectColumns(members) {
  const columns = [
    {
      header: 'Name',
      render: (member) => member.name,
    },
  ];

  // Check if any member has subproject
  if (members.some(m => m.teamData.subproject)) {
    columns.push({
      header: 'Subproject',
      render: (member) => member.teamData.subproject || '',
    });
  }

  // Check if any member has organization
  if (members.some(m => m.teamData.organization)) {
    columns.push({
      header: 'Organization',
      render: (member, affiliations) => {
        const org = member.teamData.organization;
        if (!org) return '';

        // Check if this org has a URL in affiliations
        const affiliation = affiliations.find(a => a.name === org);
        if (affiliation && affiliation.url) {
          return `[${org}](${affiliation.url})`;
        }

        return org;
      },
    });
  }

  // Always add GitHub column
  columns.push({
    header: 'GitHub',
    render: (member) => {
      if (!member.github) return '';

      const username = member.github.replace('https://github.com/', '');
      return `[\`@${username}\`](${member.github})`;
    },
  });

  // Check if any member has term
  if (members.some(m => m.teamData.term)) {
    columns.push({
      header: 'Term',
      render: (member) => member.teamData.term || '',
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

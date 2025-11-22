#!/usr/bin/env python3
"""Generate markdown sections from leadership.yml data file."""

from __future__ import annotations

import yaml
from pathlib import Path
from typing import Any

DATA_DIR = Path(__file__).parent.parent / "_data"
INCLUDES_DIR = Path(__file__).parent.parent / "_includes" / "generated"
DATA_FILE = DATA_DIR / "leadership.yml"


def resolve_person(
    people_registry: dict[str, str], github_username: str | None
) -> str | None:
    """Resolve GitHub username to person's full name.

    Returns None if github_username is None. Raises KeyError if username not found.
    """
    if github_username is None:
        return None

    if github_username not in people_registry:
        raise KeyError(
            f"GitHub username '{github_username}' not found in people registry. "
            f"Please add it to the 'people' section in leadership.yml"
        )

    return people_registry[github_username]


def github_link(github_username: str) -> str:
    """Generate GitHub link markdown."""
    return f"[`@{github_username}`](https://github.com/{github_username})"


def generate_table(
    members: list[dict[str, Any]],
    people_registry: dict[str, str],
    second_column_header: str,
    second_column_key: str,
) -> str:
    """Generate markdown table with Representative, second column, and GitHub username."""
    separator = "-" * len(second_column_header)
    lines = [
        f"| Representative | {second_column_header} | GitHub username |",
        f"| -------------- | {separator} | --------------- |",
    ]
    for member in members:
        github = member.get("github")
        name = resolve_person(people_registry, github) or ""
        second_value = member[second_column_key]
        lines.append(
            f"| {name} | {second_value} | {github_link(github) if github else ''} |"
        )
    return "\n".join(lines)


def generate_committee_list(
    data: list[dict[str, Any]],
    people_registry: dict[str, str],
) -> str:
    """Generate markdown list of committee members, sorted by first name.

    Members with 'term' field will include it in parentheses: (term).
    """
    members_with_names = []
    for member in data:
        github = member.get("github")
        name = resolve_person(people_registry, github)
        members_with_names.append(
            {
                "name": name,
                "github": github,
                "term": member.get("term"),
            }
        )

    lines: list[str] = []
    for member in sorted(members_with_names, key=lambda x: x["name"].split()[0]):
        term = member.get("term")
        term_suffix = f" ({term})" if term is not None else ""
        lines.append(
            f"- {member['name']}, {github_link(member['github'])}{term_suffix}"
        )
    return "\n".join(lines)


def generate_union_of_councils(
    data: dict[str, Any], people_registry: dict[str, str]
) -> str:
    """Generate Union of Councils list (SSC + all committees), sorted by first name."""
    all_members: set[str] = set()

    for member in data["software_steering_council"]:
        if member["github"] is None:
            continue
        all_members.add(member["github"])

    for committee in data["committees"].values():
        for member in committee:
            all_members.add(member["github"])
    members_with_names = [
        {"name": resolve_person(people_registry, github), "github": github}
        for github in all_members
    ]
    members_with_names.sort(key=lambda x: x["name"].split()[0])

    lines = [
        f"- {member['name']}, {github_link(member['github'])}"
        for member in members_with_names
    ]

    return "\n".join(lines)


def write_file(filename: str, content: str) -> None:
    """Write content to a file in the includes directory."""
    (INCLUDES_DIR / filename).write_text(content)


def main() -> None:
    """Generate all markdown include files from leadership.yml."""
    with open(DATA_FILE, "r") as f:
        data: dict[str, Any] = yaml.safe_load(f)

    people_registry = data["people"]
    INCLUDES_DIR.mkdir(parents=True, exist_ok=True)

    for data_key in [
        "executive_council",
        "former_executive_council",
        "former_steering_council",
    ]:
        write_file(
            f"{data_key}.md",
            generate_committee_list(data[data_key], people_registry),
        )

    write_file(
        "software_steering_council.md",
        generate_table(
            data["software_steering_council"],
            people_registry,
            "Subproject",
            "subproject",
        ),
    )
    write_file(
        "jupyter_foundation_board.md",
        generate_table(
            data["jupyter_foundation"],
            people_registry,
            "Organization",
            "organization",
        ),
    )
    write_file(
        "union_of_councils.md",
        generate_union_of_councils(data, people_registry),
    )

    for committee_key, committee_value in data["committees"].items():
        write_file(
            f"{committee_key}.md",
            generate_committee_list(committee_value, people_registry),
        )

    for committee_key, committee_value in data["former_committees"].items():
        write_file(
            f"former_{committee_key}.md",
            generate_committee_list(committee_value, people_registry),
        )
    print(f"Generated include files in {INCLUDES_DIR}")
    print("Use these files with: ```{include} _includes/generated/<filename>.md")


if __name__ == "__main__":
    main()

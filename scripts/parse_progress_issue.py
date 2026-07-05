#!/usr/bin/env python3
"""Parse a Weekly Research Progress issue into GitHub Actions outputs."""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path
from typing import Optional


FIELD_MAP = {
    "Week": "week",
    "Course repository URL": "repo_url",
    "Project issue URL": "project_issue",
    "Current commit SHA or compare URL": "commit_or_compare",
    "What I accomplished this week": "done",
    "Evidence links": "evidence",
    "Goals I set last week — met or not?": "goals_met",
    "Goals for next week": "next_goals",
    "Self-rating": "self_rating",
    "Blockers / where I need help": "blockers",
}


def parse_issue_form(body: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    current: Optional[str] = None
    chunks: list[str] = []

    for line in body.splitlines():
        if line.startswith("### "):
            if current:
                fields[current] = "\n".join(chunks).strip()
            current = line[4:].strip()
            chunks = []
        else:
            chunks.append(line)

    if current:
        fields[current] = "\n".join(chunks).strip()

    return {FIELD_MAP[k]: v for k, v in fields.items() if k in FIELD_MAP}


def normalize_repo(repo_url: str) -> str:
    match = re.search(r"github\.com[:/](?P<owner>[^/\s]+)/(?P<repo>[^/\s.]+)", repo_url)
    if not match:
        return ""
    return f"{match.group('owner')}/{match.group('repo')}"


def append_output(name: str, value: str) -> None:
    output_path = os.environ.get("GITHUB_OUTPUT")
    if not output_path:
        print(f"{name}={value}")
        return
    with open(output_path, "a", encoding="utf-8") as handle:
        if "\n" in value:
            handle.write(f"{name}<<EOF\n{value}\nEOF\n")
        else:
            handle.write(f"{name}={value}\n")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: parse_progress_issue.py <github-event-json>", file=sys.stderr)
        return 2

    event = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    issue = event.get("issue", {})
    parsed = parse_issue_form(issue.get("body") or "")

    append_output("issue_number", str(issue.get("number", "")))
    append_output("week", parsed.get("week", ""))
    append_output("repository", normalize_repo(parsed.get("repo_url", "")))
    append_output("repo_url", parsed.get("repo_url", ""))
    append_output("project_issue", parsed.get("project_issue", ""))
    append_output("commit_or_compare", parsed.get("commit_or_compare", ""))
    append_output("done", parsed.get("done", ""))
    append_output("evidence", parsed.get("evidence", ""))
    append_output("goals_met", parsed.get("goals_met", ""))
    append_output("next_goals", parsed.get("next_goals", ""))
    append_output("self_rating", parsed.get("self_rating", ""))
    append_output("blockers", parsed.get("blockers", ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

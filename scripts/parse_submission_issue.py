#!/usr/bin/env python3
"""Parse a GitHub Issue Form submission into GitHub Actions outputs."""

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
    "Commit SHA": "commit",
    "Submission manifest path": "manifest",
    "Rendered answer path": "rendered",
    "Rendered report path": "rendered",
    "Key output paths": "outputs",
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
        raise ValueError(f"Could not parse GitHub repository from: {repo_url}")
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
        print("usage: parse_submission_issue.py <github-event-json>", file=sys.stderr)
        return 2

    event = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    issue = event.get("issue", {})
    parsed = parse_issue_form(issue.get("body") or "")

    required = ["week", "repo_url", "commit", "manifest"]
    missing = [field for field in required if not parsed.get(field)]
    if missing:
        raise ValueError(f"Submission issue is missing required fields: {', '.join(missing)}")

    labels = [label.get("name", "") for label in issue.get("labels", [])]
    submission_type = "question-set" if "question-set" in labels else "assignment"

    append_output("week", parsed["week"])
    append_output("repository", normalize_repo(parsed["repo_url"]))
    append_output("commit", parsed["commit"].strip())
    append_output("manifest", parsed["manifest"].strip())
    append_output("rendered", parsed.get("rendered", "").strip())
    append_output("outputs", parsed.get("outputs", "").strip())
    append_output("submission_type", submission_type)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Assess a Weekly Research Progress issue and write a Markdown report."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


URL_RE = re.compile(r"https?://\S+")
GITHUB_RE = re.compile(r"https?://github\.com/[^/\s]+/[^/\s]+")
COMMIT_RE = re.compile(r"\b[0-9a-f]{7,40}\b", re.IGNORECASE)


def nonempty(value: str) -> bool:
    return bool(value and value.strip() and value.strip() != "_No response_")


def count_goal_lines(value: str) -> int:
    lines = [line.strip() for line in value.splitlines() if line.strip()]
    return len(lines)


def has_status_language(value: str) -> bool:
    lowered = value.lower()
    return any(term in lowered for term in ["met", "partial", "not met", "missed", "done", "blocked", "changed"])


def write_report(path: Path, status: str, triage: str, passed: list[str], warnings: list[str], failures: list[str]) -> None:
    lines = [
        f"## Weekly progress assessment: {status}",
        "",
        f"Suggested triage label: `{triage}`",
        "",
        "This check evaluates whether the progress record is complete and actionable. The instructor still reviews project quality and scientific judgment.",
        "",
    ]

    if passed:
        lines += ["### Passed", ""]
        lines += [f"- {item}" for item in passed]
        lines.append("")

    if warnings:
        lines += ["### Warnings", ""]
        lines += [f"- {item}" for item in warnings]
        lines.append("")

    if failures:
        lines += ["### Failed checks", ""]
        lines += [f"- {item}" for item in failures]
        lines.append("")

    lines += [
        "### Human review focus",
        "",
        "- Is the project making appropriate scientific progress?",
        "- Are blockers being addressed early enough?",
        "- Are next-week goals realistic and connected to the final compendium?",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--week", required=True)
    parser.add_argument("--repository", default="")
    parser.add_argument("--repo-url", default="")
    parser.add_argument("--project-issue", default="")
    parser.add_argument("--commit-or-compare", default="")
    parser.add_argument("--done", default="")
    parser.add_argument("--evidence", default="")
    parser.add_argument("--goals-met", default="")
    parser.add_argument("--next-goals", default="")
    parser.add_argument("--self-rating", default="")
    parser.add_argument("--blockers", default="")
    parser.add_argument("--report", required=True)
    parser.add_argument("--status-file", required=True)
    parser.add_argument("--triage-file", required=True)
    args = parser.parse_args()

    passed: list[str] = []
    warnings: list[str] = []
    failures: list[str] = []

    if args.week.zfill(2) in {f"{n:02d}" for n in range(1, 11)}:
        passed.append(f"Week `{args.week}` is valid.")
    else:
        failures.append("Week is missing or outside 01-10.")

    if args.repository and GITHUB_RE.search(args.repo_url):
        passed.append(f"Course repository parsed as `{args.repository}`.")
    else:
        failures.append("Course repository URL is missing or not a GitHub repository URL.")

    if "/issues/" in args.project_issue and GITHUB_RE.search(args.project_issue):
        passed.append("Project issue link found.")
    else:
        failures.append("Project issue URL is missing or does not look like a GitHub issue.")

    if URL_RE.search(args.commit_or_compare) or COMMIT_RE.search(args.commit_or_compare):
        passed.append("Current commit SHA or compare URL found.")
    else:
        failures.append("Current commit SHA or compare URL is missing.")

    if len(args.done.strip()) >= 80:
        passed.append("Accomplishments include enough detail for review.")
    elif nonempty(args.done):
        warnings.append("Accomplishments are present but very brief.")
    else:
        failures.append("Accomplishments are missing.")

    evidence_urls = URL_RE.findall(args.evidence)
    if len(evidence_urls) >= 2:
        passed.append(f"{len(evidence_urls)} evidence links found.")
    elif len(evidence_urls) == 1:
        warnings.append("Only one evidence link found; include commits, outputs, or reports where possible.")
    else:
        failures.append("Evidence links are missing.")

    if nonempty(args.goals_met) and has_status_language(args.goals_met):
        passed.append("Prior goals are accounted for.")
    elif nonempty(args.goals_met):
        warnings.append("Prior goals are described, but met/not-met status is unclear.")
    else:
        failures.append("Prior-goal accounting is missing.")

    next_goal_count = count_goal_lines(args.next_goals)
    if next_goal_count >= 2:
        passed.append(f"{next_goal_count} next-week goal lines found.")
    elif next_goal_count == 1:
        warnings.append("Only one next-week goal found; use 2-4 concrete goals.")
    else:
        failures.append("Next-week goals are missing.")

    rating = args.self_rating.strip().lower()
    if rating == "on track":
        passed.append("Self-rating is `On track`.")
    elif rating == "some risk":
        warnings.append("Student self-rated as `Some risk`.")
    elif rating == "blocked":
        warnings.append("Student self-rated as `Blocked`.")
    else:
        warnings.append("Self-rating is missing or unrecognized.")

    blockers = args.blockers.strip()
    if rating == "blocked":
        if "/issues/" in blockers and GITHUB_RE.search(blockers):
            passed.append("Blocked status includes a linked help/blocker issue.")
        else:
            warnings.append("Blocked status should include a linked Help Request or Blocker/Bug issue.")
    elif blockers and blockers != "_No response_":
        passed.append("Blockers/help needs were documented.")
    else:
        passed.append("No blockers reported.")

    if failures:
        status = "fail"
    elif warnings:
        status = "warn"
    else:
        status = "pass"

    if rating == "blocked":
        triage = "progress:blocked"
    elif status == "fail" or rating == "some risk":
        triage = "progress:watch"
    elif status == "warn":
        triage = "progress:watch"
    else:
        triage = "progress:on-track"

    write_report(Path(args.report), status, triage, passed, warnings, failures)
    Path(args.status_file).write_text(status + "\n", encoding="utf-8")
    Path(args.triage_file).write_text(triage + "\n", encoding="utf-8")
    print(status)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

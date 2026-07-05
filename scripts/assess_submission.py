#!/usr/bin/env python3
"""Assess a FISH 546 submission manifest and write a Markdown report."""

from __future__ import annotations

import argparse
import os
import subprocess
from pathlib import Path
from typing import Optional


def parse_simple_yaml(path: Path) -> dict[str, object]:
    data: dict[str, object] = {}
    current_list: Optional[str] = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if current_list and stripped.startswith("- "):
            data.setdefault(current_list, []).append(stripped[2:].strip().strip('"').strip("'"))
            continue
        current_list = None
        if ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value == "":
            data[key] = []
            current_list = key
        elif value.lower() in {"true", "false"}:
            data[key] = value.lower() == "true"
        else:
            data[key] = value.strip('"').strip("'")

    return data


def safe_path(root: Path, relative: str) -> Optional[Path]:
    if not relative or relative.startswith("/") or ".." in Path(relative).parts:
        return None
    return root / relative


def file_check(root: Path, relative: str, label: str, passed: list[str], warnings: list[str], failures: list[str]) -> None:
    path = safe_path(root, relative)
    if path is None:
        failures.append(f"{label} path is unsafe: `{relative}`.")
        return
    if not path.exists():
        failures.append(f"{label} is missing: `{relative}`.")
        return
    if path.is_file() and path.stat().st_size == 0:
        failures.append(f"{label} is empty: `{relative}`.")
        return
    passed.append(f"{label} found: `{relative}`.")


def tracked_raw_data(root: Path) -> list[str]:
    result = subprocess.run(
        ["git", "-C", str(root), "ls-files", "data/raw"],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return []
    return [line for line in result.stdout.splitlines() if line.strip()]


def write_report(path: Path, status: str, passed: list[str], warnings: list[str], failures: list[str]) -> None:
    lines = [
        f"## Automatic assessment: {status}",
        "",
        "This check verifies submission structure and evidence files. Scientific interpretation still needs human review.",
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
        "### Needs human review",
        "",
        "- Biological reasoning, interpretation, caveats, and writing quality.",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--student-root", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--week", required=True)
    parser.add_argument("--submission-type", required=True)
    parser.add_argument("--rendered", default="")
    parser.add_argument("--outputs", default="")
    parser.add_argument("--report", required=True)
    parser.add_argument("--status-file", required=True)
    args = parser.parse_args()

    root = Path(args.student_root)
    manifest_path = safe_path(root, args.manifest)
    passed: list[str] = []
    warnings: list[str] = []
    failures: list[str] = []

    manifest: dict[str, object] = {}
    if manifest_path is None:
        failures.append(f"Manifest path is unsafe: `{args.manifest}`.")
    elif not manifest_path.exists():
        failures.append(f"Manifest is missing: `{args.manifest}`.")
    else:
        passed.append(f"Manifest found: `{args.manifest}`.")
        manifest = parse_simple_yaml(manifest_path)

    expected_type = args.submission_type
    if manifest:
        if str(manifest.get("type", "")).strip() != expected_type:
            failures.append(f"Manifest `type` should be `{expected_type}`.")
        else:
            passed.append(f"Manifest type is `{expected_type}`.")

        if str(manifest.get("week", "")).zfill(2) != args.week.zfill(2):
            failures.append(f"Manifest week does not match issue week `{args.week}`.")
        else:
            passed.append(f"Manifest week matches issue week `{args.week}`.")

        source = str(manifest.get("source", ""))
        rendered = args.rendered or str(manifest.get("rendered", ""))
        file_check(root, source, "Source file", passed, warnings, failures)
        file_check(root, rendered, "Rendered file", passed, warnings, failures)

        manifest_outputs = manifest.get("outputs", [])
        issue_outputs = [line.strip() for line in args.outputs.splitlines() if line.strip()]
        outputs = issue_outputs or manifest_outputs
        if expected_type == "assignment" and not outputs:
            warnings.append("No output files were listed.")
        for output in outputs:
            file_check(root, str(output), "Output file", passed, warnings, failures)

        if expected_type == "question-set":
            answered = str(manifest.get("questions_answered", "")).strip()
            if not answered:
                warnings.append("Manifest does not include `questions_answered`.")
            elif answered.isdigit() and int(answered) >= 5:
                passed.append("Manifest reports at least five answered questions.")
            else:
                warnings.append("Manifest reports fewer than five answered questions.")

        if manifest.get("project_connection") is True:
            passed.append("Manifest includes a project connection.")
        else:
            warnings.append("Manifest does not confirm a project connection.")

        if manifest.get("raw_data_committed") is False:
            raw_files = tracked_raw_data(root)
            if raw_files:
                failures.append("Manifest says raw data are not committed, but `data/raw/` contains tracked files.")
            else:
                passed.append("No tracked files found under `data/raw/`.")

    status = "fail" if failures else "warn" if warnings else "pass"
    write_report(Path(args.report), status, passed, warnings, failures)
    Path(args.status_file).write_text(status + "\n", encoding="utf-8")
    print(status)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

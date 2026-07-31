#!/usr/bin/env python3
"""Audit FISH 546 course sources and the generated Quarto site.

The default audit is offline and deterministic. It checks local links in source
materials, local links and anchors in ``docs/``, copied tutorial resources, and
the render-source manifest. Use ``--external`` for the pre-course external-link
review and ``--write-manifest`` immediately after a successful Quarto render.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlparse
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
MANIFEST = ROOT / "maintenance" / "render-source-manifest.json"
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
AUTOLINK = re.compile(r"<((?:https?://)[^>]+)>")
RAW_URL = re.compile(r"https?://[^\s<>()\"']+")
HTML_ATTR = re.compile(r"(?:href|src)=[\"']([^\"']+)[\"']", re.IGNORECASE)
EXTERNAL_SCHEMES = {"http", "https", "mailto", "tel", "data", "javascript"}
URL_PLACEHOLDERS = ("github.com/...", "your-repo", "<", ">", "{", "}")


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.targets: list[tuple[str, str]] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"] or "")
        if tag == "a" and values.get("name"):
            self.ids.add(values["name"] or "")
        for attr in ("href", "src"):
            if values.get(attr):
                self.targets.append((attr, values[attr] or ""))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def source_files() -> list[Path]:
    files = [ROOT / "_quarto.yml", ROOT / "styles.css"]
    files.extend(sorted(ROOT.glob("*.qmd")))
    files.extend(sorted((ROOT / "lectures").glob("*.qmd")))
    for pattern in ("*.html", "*.css", "*.js"):
        files.extend(sorted((ROOT / "tutorials").glob(pattern)))
    return sorted({path for path in files if path.is_file()})


def source_documents() -> list[Path]:
    files: list[Path] = []
    files.extend(sorted(ROOT.glob("*.qmd")))
    files.extend(sorted((ROOT / "lectures").glob("*.qmd")))
    files.extend(sorted((ROOT / "tutorials").glob("*.html")))
    return files


def display(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def clean_target(raw: str) -> str:
    target = html.unescape(raw.strip())
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    if " " in target and not target.startswith(("http://", "https://")):
        target = target.split()[0]
    return target


def is_external(target: str) -> bool:
    return urlparse(target).scheme.lower() in EXTERNAL_SCHEMES or target.startswith("//")


def source_targets(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    targets = [match.group(1) for match in MARKDOWN_LINK.finditer(text)]
    targets.extend(match.group(1) for match in HTML_ATTR.finditer(text))
    return [clean_target(target) for target in targets]


def check_source_links() -> list[str]:
    errors: list[str] = []
    for source in source_documents():
        for target in source_targets(source):
            parsed = urlparse(target)
            if not target or target.startswith("#") or is_external(target):
                continue
            candidate = (source.parent / unquote(parsed.path)).resolve()
            if not parsed.path or candidate.exists():
                continue
            errors.append(f"{display(source)} -> missing {target}")
    return errors


def parse_generated_pages() -> dict[Path, PageParser]:
    pages: dict[Path, PageParser] = {}
    for path in sorted(DOCS.rglob("*.html")):
        parser = PageParser()
        parser.feed(path.read_text(encoding="utf-8", errors="replace"))
        pages[path.resolve()] = parser
    return pages


def check_generated_links() -> list[str]:
    errors: list[str] = []
    pages = parse_generated_pages()
    for source, parser in pages.items():
        for _, raw_target in parser.targets:
            target = clean_target(raw_target)
            parsed = urlparse(target)
            if not target or is_external(target):
                continue
            if target.startswith("#"):
                candidate = source
            elif parsed.path:
                candidate = (source.parent / unquote(parsed.path)).resolve()
            else:
                candidate = source
            if not candidate.exists():
                errors.append(f"{display(source)} -> missing {target}")
                continue
            if parsed.fragment and candidate.suffix.lower() in {".html", ".htm"}:
                destination = pages.get(candidate)
                if destination is not None and unquote(parsed.fragment) not in destination.ids:
                    errors.append(f"{display(source)} -> missing anchor {target}")
    return errors


def check_tutorial_copies() -> list[str]:
    errors: list[str] = []
    for source in sorted((ROOT / "tutorials").iterdir()):
        if source.suffix not in {".html", ".css", ".js"}:
            continue
        destination = DOCS / "tutorials" / source.name
        if not destination.exists():
            errors.append(f"{display(source)} -> not copied to {display(destination)}")
        elif sha256(source) != sha256(destination):
            errors.append(f"{display(destination)} does not match {display(source)}")
    return errors


def manifest_payload() -> dict[str, object]:
    return {
        "description": "Source hashes recorded after the last accepted course-site render.",
        "sources": {display(path): sha256(path) for path in source_files()},
    }


def write_manifest() -> None:
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(manifest_payload(), indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {display(MANIFEST)}")


def check_manifest() -> list[str]:
    if not MANIFEST.exists():
        return [f"missing {display(MANIFEST)}; run with --write-manifest after rendering"]
    try:
        expected = json.loads(MANIFEST.read_text(encoding="utf-8"))["sources"]
    except (KeyError, TypeError, json.JSONDecodeError) as exc:
        return [f"invalid {display(MANIFEST)}: {exc}"]
    current = manifest_payload()["sources"]
    errors: list[str] = []
    expected_names = set(expected)
    current_names = set(current)
    for name in sorted(expected_names - current_names):
        errors.append(f"render source removed since manifest: {name}")
    for name in sorted(current_names - expected_names):
        errors.append(f"render source added since manifest: {name}")
    for name in sorted(expected_names & current_names):
        if expected[name] != current[name]:
            errors.append(f"render source changed since manifest: {name}")
    return errors


def external_urls() -> list[str]:
    urls: set[str] = set()
    for path in source_documents() + sorted((ROOT / ".github").rglob("*.yml")):
        text = html.unescape(path.read_text(encoding="utf-8", errors="replace"))
        urls.update(match.group(1) for match in AUTOLINK.finditer(text))
        urls.update(match.group(0).rstrip(".,;:") for match in RAW_URL.finditer(text))
    return sorted(url for url in urls if not any(marker in url for marker in URL_PLACEHOLDERS))


def request_status(url: str, timeout: float) -> tuple[str, str]:
    headers = {"User-Agent": "FISH546-course-link-audit/1.0"}
    for method in ("HEAD", "GET"):
        request = Request(url, headers=headers, method=method)
        try:
            with urlopen(request, timeout=timeout) as response:
                return str(response.status), response.geturl()
        except HTTPError as exc:
            if method == "HEAD" and exc.code in {403, 405}:
                continue
            return str(exc.code), exc.geturl()
        except URLError as exc:
            return "ERROR", str(exc.reason)
        except TimeoutError:
            return "ERROR", "timeout"
    return "ERROR", "request failed"


def check_external_links(timeout: float) -> list[tuple[str, str, str]]:
    urls = external_urls()
    with ThreadPoolExecutor(max_workers=min(8, len(urls) or 1)) as executor:
        responses = executor.map(lambda url: request_status(url, timeout), urls)
        return [(status, url, destination) for url, (status, destination) in zip(urls, responses)]


def report_group(title: str, errors: list[str]) -> None:
    state = "PASS" if not errors else "FAIL"
    print(f"[{state}] {title}")
    for error in errors:
        print(f"  - {error}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write-manifest",
        action="store_true",
        help="record source hashes after a successful Quarto render",
    )
    parser.add_argument(
        "--external",
        action="store_true",
        help="also request every external URL found in student-facing sources",
    )
    parser.add_argument(
        "--strict-external",
        action="store_true",
        help="fail for external 4xx/5xx responses (implies --external)",
    )
    parser.add_argument("--timeout", type=float, default=10.0, help="seconds per external request")
    args = parser.parse_args()

    if args.write_manifest:
        write_manifest()

    groups = [
        ("source local links", check_source_links()),
        ("generated-site local links and anchors", check_generated_links()),
        ("tutorial resources copied to docs", check_tutorial_copies()),
        ("render-source manifest", check_manifest()),
    ]
    for title, errors in groups:
        report_group(title, errors)

    failed = any(errors for _, errors in groups)
    if args.external or args.strict_external:
        print("[INFO] external links")
        results = check_external_links(args.timeout)
        for status, url, destination in results:
            suffix = "" if destination == url else f" -> {destination}"
            print(f"  {status:>5} {url}{suffix}")
        if args.strict_external:
            failed = failed or any(
                (status.isdigit() and int(status) >= 400) or status == "ERROR"
                for status, _, _ in results
            )

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

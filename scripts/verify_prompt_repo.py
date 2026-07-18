#!/usr/bin/env python3
"""Portable baseline verifier for the public prompt repository."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent.parent
README_FILES = [
    "README.md",
    "README_es.md",
    "README_pt.md",
    "README_ja.md",
    "README_ko.md",
    "README_de.md",
    "README_fr.md",
    "README_tr.md",
    "README_zh-TW.md",
    "README_zh-CN.md",
    "README_ru.md",
]
REQUIRED_FILES = [
    "LICENSE",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    ".github/ISSUE_TEMPLATE/submit-prompt.yml",
    ".github/PULL_REQUEST_TEMPLATE.md",
    "docs/maintenance.md",
    "docs/update-log.md",
    "data/ingested_tweets.json",
]
CASE_RE = re.compile(r"^### Case \d+:", re.MULTILINE)
CASE_HEADING_RE = re.compile(
    r"^### Case (\d+): \[.+\]\(https?://[^)]+\) "
    r"\(by \[@[^]]+\]\(https?://[^)]+\)\)$"
)
CASE_COMMENT_RE = re.compile(r"^<!-- Case (\d+):")
STATUS_ID_RE = re.compile(
    r"https?://(?:x\.com|twitter\.com)/[^/\s)]+/status/(\d+)"
)
FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})(?:[^`]*)?$")
EXPECTED_CASE_COUNT = 462
REQUIRED_SECTION_ANCHORS = [
    "introduction",
    "quick-start",
    "model-overview",
    "news",
    "menu",
    "category-ecommerce",
    "category-ad-creative",
    "category-portrait",
    "category-poster",
    "category-character",
    "category-ui",
    "category-comparison",
    "contributing",
    "related-repositories",
    "acknowledge",
]
FORBIDDEN_API_FIRST_MARKERS = [
    'export EVOLINK_API_KEY=',
    "Authorization: Bearer",
    "npx evolink-gpt-image",
    "curl --request POST",
]
RELATED_REPOSITORY_URLS = [
    "https://github.com/Evolink-AI/gpt-image-2-gen-skill",
    "https://github.com/Evolink-AI/GPT-Image-2-Seedance2-Workflow",
]
HTML_MEDIA_RE = re.compile(
    r"<(?:img|source)\b[^>]*\b(?:src|poster)=[\"']([^\"']+)[\"']",
    re.IGNORECASE,
)
MARKDOWN_IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)(?:\s+[\"'][^\"']*[\"'])?\)")


def analyze_case_headings(text: str) -> tuple[int, int, bool]:
    """Count rendered case headings and detect headings swallowed by fences."""
    outside_count = 0
    inside_count = 0
    fence_char = ""
    fence_length = 0

    for line in text.splitlines():
        fence_match = FENCE_RE.match(line)
        if fence_match:
            marker = fence_match.group(1)
            if not fence_char:
                fence_char = marker[0]
                fence_length = len(marker)
            elif marker[0] == fence_char and len(marker) >= fence_length:
                fence_char = ""
                fence_length = 0
            continue

        if CASE_RE.match(line):
            if fence_char:
                inside_count += 1
            else:
                outside_count += 1

    return outside_count, inside_count, bool(fence_char)


def visible_lines(text: str) -> list[str]:
    """Return lines that GitHub renders outside fenced code blocks."""
    lines: list[str] = []
    fence_char = ""
    fence_length = 0
    for line in text.splitlines():
        fence_match = FENCE_RE.match(line)
        if fence_match:
            marker = fence_match.group(1)
            if not fence_char:
                fence_char = marker[0]
                fence_length = len(marker)
            elif marker[0] == fence_char and len(marker) >= fence_length:
                fence_char = ""
                fence_length = 0
            continue
        if not fence_char:
            lines.append(line)
    return lines


def local_target(raw: str, source: Path) -> Path | None:
    raw = raw.strip().strip("<>")
    parsed = urlsplit(raw)
    if parsed.scheme or raw.startswith("//") or raw.startswith("#"):
        return None
    path_text = unquote(parsed.path)
    if not path_text:
        return None
    return (source.parent / path_text).resolve()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="emit JSON")
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []
    details: dict[str, object] = {}

    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    if (ROOT / "README_en.md").exists():
        errors.append("README_en.md must not exist; README.md is the English source")

    english_count = 0
    readme_counts: dict[str, int] = {}
    readme_inside_fence_counts: dict[str, int] = {}
    readme_unclosed_fences: dict[str, bool] = {}
    checked_local_media: set[str] = set()
    english_source_order: list[str] = []

    for name in README_FILES:
        path = ROOT / name
        if not path.is_file():
            errors.append(f"missing required README: {name}")
            continue

        text = path.read_text(encoding="utf-8")
        count, inside_fence_count, has_unclosed_fence = analyze_case_headings(text)
        readme_counts[name] = count
        readme_inside_fence_counts[name] = inside_fence_count
        readme_unclosed_fences[name] = has_unclosed_fence
        if name == "README.md":
            english_count = count

        rendered_lines = visible_lines(text)
        rendered_text = "\n".join(rendered_lines)
        case_numbers = [
            int(match.group(1))
            for line in rendered_lines
            if (match := re.match(r"^### Case (\d+):", line))
        ]
        case_heading_lines = [line for line in rendered_lines if CASE_RE.match(line)]
        malformed_case_headings = [
            line for line in case_heading_lines if not CASE_HEADING_RE.match(line)
        ]
        if malformed_case_headings:
            errors.append(
                f"{name}: {len(malformed_case_headings)} Case headings do not match "
                "the linked title + linked author template"
            )
        case_comment_numbers = [
            int(match.group(1))
            for line in rendered_lines
            if (match := CASE_COMMENT_RE.match(line))
        ]
        if case_comment_numbers != case_numbers:
            errors.append(
                f"{name}: Case comment numbers do not match visible Case heading order"
            )
        source_order = []
        for line in case_heading_lines:
            match = STATUS_ID_RE.search(line)
            if not match:
                errors.append(f"{name}: Case heading has no X/Twitter status source: {line}")
                continue
            source_order.append(match.group(1))
        if len(source_order) != len(set(source_order)):
            errors.append(f"{name}: duplicate X/Twitter source ids in Case headings")
        if name == "README.md":
            english_source_order = source_order
        elif english_source_order and source_order != english_source_order:
            errors.append(f"{name}: Case source order differs from README.md")
        duplicate_case_numbers = sorted(
            number for number in set(case_numbers) if case_numbers.count(number) > 1
        )
        if duplicate_case_numbers:
            errors.append(
                f"{name}: duplicate Case numbers: {duplicate_case_numbers}"
            )
        expected_numbers = list(range(1, len(case_numbers) + 1))
        if sorted(case_numbers) != expected_numbers:
            missing_numbers = sorted(set(expected_numbers) - set(case_numbers))
            unexpected_numbers = sorted(set(case_numbers) - set(expected_numbers))
            errors.append(
                f"{name}: Case numbering is not contiguous 1..{len(case_numbers)}; "
                f"missing={missing_numbers}, unexpected={unexpected_numbers}"
            )
        anchors = re.findall(r'^<a id="([^"]+)"></a>$', rendered_text, re.MULTILINE)
        required_anchors = [anchor for anchor in anchors if anchor in REQUIRED_SECTION_ANCHORS]
        if required_anchors != REQUIRED_SECTION_ANCHORS:
            errors.append(
                f"{name}: required section anchor order differs: {required_anchors}"
            )

        visible_h2 = [line for line in rendered_lines if line.startswith("## ")]
        if len(visible_h2) != len(REQUIRED_SECTION_ANCHORS):
            errors.append(
                f"{name}: visible H2 count {len(visible_h2)}; expected {len(REQUIRED_SECTION_ANCHORS)}"
            )
        if not visible_h2 or "Acknowledge" not in visible_h2[-1] and name == "README.md":
            errors.append(f"{name}: final visible H2 must be the acknowledge section")

        menu_start = rendered_text.find('<a id="menu"></a>')
        first_category = rendered_text.find('<a id="category-ecommerce"></a>')
        if menu_start < 0 or first_category < 0 or menu_start >= first_category:
            errors.append(f"{name}: Menu must appear before the first prompt category")
        else:
            menu_text = rendered_text[menu_start:first_category]
            menu_targets = re.findall(r"\]\(#([^)]+)\)", menu_text)
            if menu_targets != REQUIRED_SECTION_ANCHORS:
                errors.append(f"{name}: Menu targets differ: {menu_targets}")

        for marker in FORBIDDEN_API_FIRST_MARKERS:
            if marker in rendered_text:
                errors.append(
                    f"{name}: API-first runtime marker remains in prompt repository: {marker}"
                )
        for url in RELATED_REPOSITORY_URLS:
            if url not in rendered_text:
                errors.append(f"{name}: missing related repository link: {url}")

        if '<a id="quick-start"></a>' not in "\n".join(rendered_lines[:120]):
            errors.append(f"{name}: Quick Start is not visible in the first 120 rendered lines")
        if not rendered_lines or not rendered_lines[0].startswith("# Awesome GPT Image 2 Prompts"):
            errors.append(f"{name}: first heading does not position the repository as prompt-first")

        if inside_fence_count:
            errors.append(
                f"{name}: {inside_fence_count} Case headings are inside fenced code blocks"
            )
        if has_unclosed_fence:
            errors.append(f"{name}: contains an unclosed fenced code block")

        for raw in HTML_MEDIA_RE.findall(text) + MARKDOWN_IMAGE_RE.findall(text):
            target = local_target(raw, path)
            if target is None:
                continue
            try:
                target.relative_to(ROOT)
            except ValueError:
                errors.append(f"{name}: local media escapes repository: {raw}")
                continue
            checked_local_media.add(str(target.relative_to(ROOT)))
            if not target.is_file():
                errors.append(f"{name}: missing local media: {raw}")

    if english_count == 0:
        errors.append("README.md contains no Case headings")
    for name, count in readme_counts.items():
        if name != "README.md" and count != english_count:
            errors.append(
                f"{name}: case count {count} does not match README.md {english_count}"
            )

    source_index = ROOT / "data/ingested_tweets.json"
    if source_index.is_file():
        try:
            source_data = json.loads(source_index.read_text(encoding="utf-8"))
            indexed_anchors: dict[str, set[str]] = {}
            for record in source_data.get("records", []):
                source_match = STATUS_ID_RE.search(record.get("tweet_url", ""))
                if not source_match or source_match.group(1) not in set(english_source_order):
                    continue
                indexed_anchors.setdefault(source_match.group(1), set()).add(
                    record.get("case_anchor", "")
                )
            if len(indexed_anchors) != len(english_source_order):
                errors.append(
                    "data/ingested_tweets.json does not cover every authoritative README source"
                )
            for number, source_id in enumerate(english_source_order, 1):
                anchors = indexed_anchors.get(source_id, set())
                if not anchors or any(
                    not anchor.startswith(f"#case-{number}-") for anchor in anchors
                ):
                    errors.append(
                        f"data/ingested_tweets.json: source {source_id} has a stale Case anchor"
                    )
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            errors.append(f"invalid data/ingested_tweets.json: {exc}")

    unexpected_system_files: list[str] = []
    for path in ROOT.rglob("*"):
        if ".git" in path.parts:
            continue
        if path.name == ".DS_Store" or path.name == "__pycache__" or path.suffix == ".pyc":
            unexpected_system_files.append(str(path.relative_to(ROOT)))
    if unexpected_system_files:
        errors.extend(
            f"unexpected system file: {relative}" for relative in unexpected_system_files
        )

    if english_count != EXPECTED_CASE_COUNT:
        warnings.append(
            f"rendered case count is {english_count}; expected {EXPECTED_CASE_COUNT}"
        )

    details.update(
        {
            "ok": not errors,
            "english_case_count": english_count,
            "readme_case_counts": readme_counts,
            "readme_inside_fence_case_counts": readme_inside_fence_counts,
            "readme_unclosed_fences": readme_unclosed_fences,
            "checked_local_media_count": len(checked_local_media),
            "errors": errors,
            "warnings": warnings,
        }
    )

    if args.json:
        print(json.dumps(details, ensure_ascii=False, indent=2))
    else:
        print(f"ok: {details['ok']}")
        print(f"english_case_count: {english_count}")
        print(f"checked_local_media_count: {len(checked_local_media)}")
        for warning in warnings:
            print(f"warning: {warning}")
        for error in errors:
            print(f"error: {error}")

    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())

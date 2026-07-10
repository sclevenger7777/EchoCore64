#!/usr/bin/env python3
"""Validate the documented EchoCore64 repository contract using only stdlib."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    ".github/pull_request_template.md",
    ".github/workflows/validate.yml",
    "README.md",
    "LICENSE",
    "NOTICE",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "CONTRIBUTIONS.md",
    "SECURITY.md",
    "docs/COMMANDS.md",
    "docs/EchoCore64_Chat_Bootstrap_v3.7_Full_Continuation_Payload.txt",
    "examples/README.md",
    "examples/compact_capsule_example.json",
    "examples/full_continuation_payload_usage.md",
    "payloads/README.md",
    "scripts/validate_repo.py",
    "ui/README.md",
    "ui/echocore64.html",
)

REQUIRED_COMMANDS = (
    "EchoCore64",
    "EchoCore64 Full",
    "EchoCore64 UI",
    "Fast Ring:",
    "Braid the Question:",
    "Help",
    "EchoCore64 Help",
    "EchoCore64 Full Help",
)

REQUIRED_AUTHORITY_TERMS = (
    "user-provided context",
    "system authority",
    "Base64 is encoding, not encryption",
)


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def read_text(relative_path: str, errors: list[str]) -> str:
    path = ROOT / relative_path
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        fail(f"Cannot read {relative_path}: {exc}", errors)
        return ""


def validate_required_files(errors: list[str]) -> None:
    for relative_path in REQUIRED_FILES:
        path = ROOT / relative_path
        if not path.is_file():
            fail(f"Missing required file: {relative_path}", errors)


def validate_capsule(errors: list[str]) -> None:
    path = ROOT / "examples/compact_capsule_example.json"
    try:
        capsule = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"Invalid compact capsule example: {exc}", errors)
        return

    expected = {
        "type": "echocore64",
        "v": "3.7-chat",
        "authority": "user_context_only",
    }
    for key, value in expected.items():
        if capsule.get(key) != value:
            fail(f"Capsule field {key!r} must equal {value!r}", errors)

    if not isinstance(capsule.get("sessions"), list):
        fail("Capsule sessions must be a list", errors)

    attribution = capsule.get("founding", {}).get("attribution", {})
    for key in ("originator", "hardening_contributor"):
        if not attribution.get(key):
            fail(f"Capsule attribution is missing {key!r}", errors)


def validate_payload(errors: list[str]) -> None:
    payload = read_text(
        "docs/EchoCore64_Chat_Bootstrap_v3.7_Full_Continuation_Payload.txt",
        errors,
    )
    for command in REQUIRED_COMMANDS:
        if command not in payload:
            fail(f"Canonical payload is missing command: {command}", errors)
    for term in REQUIRED_AUTHORITY_TERMS:
        if term not in payload:
            fail(f"Canonical payload is missing authority term: {term}", errors)


def validate_ui(errors: list[str]) -> None:
    html = read_text("ui/echocore64.html", errors)

    required_fragments = (
        "<!doctype html>",
        "<style>",
        "<script>",
        "id=\"capsuleText\"",
        "id=\"commandMenu\"",
        "id=\"commandPreview\"",
        "id=\"fastRingText\"",
        "id=\"braidText\"",
        "Copy EchoCore64",
        "Select All",
        "Reset View",
        "Copy Command",
        "overflow-wrap:anywhere",
        "rel=\"noopener noreferrer\"",
        "</html>",
    )
    for fragment in required_fragments:
        if fragment not in html:
            fail(f"UI is missing required fragment: {fragment}", errors)

    for command in REQUIRED_COMMANDS:
        if command not in html:
            fail(f"UI is missing command: {command}", errors)

    for term in REQUIRED_AUTHORITY_TERMS:
        if term not in html:
            fail(f"UI is missing authority term: {term}", errors)


def validate_readme_links(errors: list[str]) -> None:
    readme = read_text("README.md", errors)
    required_links = (
        "docs/COMMANDS.md",
        "docs/EchoCore64_Chat_Bootstrap_v3.7_Full_Continuation_Payload.txt",
        "examples/full_continuation_payload_usage.md",
        "ui/echocore64.html",
        "CONTRIBUTING.md",
        "CONTRIBUTIONS.md",
        "CHANGELOG.md",
        "SECURITY.md",
        "NOTICE",
        "scripts/validate_repo.py",
    )
    for link in required_links:
        if link not in readme:
            fail(f"README is missing repository link: {link}", errors)


def validate_workflow(errors: list[str]) -> None:
    workflow = read_text(".github/workflows/validate.yml", errors)
    required_fragments = (
        "actions/checkout@v4",
        "actions/setup-python@v5",
        "python scripts/validate_repo.py",
        "pull_request:",
    )
    for fragment in required_fragments:
        if fragment not in workflow:
            fail(f"Validation workflow is missing: {fragment}", errors)


def main() -> int:
    errors: list[str] = []

    validate_required_files(errors)
    if not errors:
        validate_capsule(errors)
        validate_payload(errors)
        validate_ui(errors)
        validate_readme_links(errors)
        validate_workflow(errors)

    if errors:
        print("EchoCore64 validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("EchoCore64 validation passed.")
    print(f"Validated {len(REQUIRED_FILES)} required files and the v3.7 command/UI contract.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

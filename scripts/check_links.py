#!/usr/bin/env python3
"""Repo self-checks: internal markdown links resolve, template JSON is valid.

Run from the repository root (CI does). External links are checked separately
by the scheduled lychee job, so this script stays deterministic and offline.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

MD_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
HTML_SRC = re.compile(r"""(?:src|href)=["']([^"']+)["']""")

SKIP_DIRS = {".git", "__pycache__"}


def iter_markdown_files() -> list[Path]:
    return [
        path
        for path in REPO_ROOT.rglob("*.md")
        if not any(part in SKIP_DIRS for part in path.parts)
    ]


def is_internal(target: str) -> bool:
    if target.startswith(("http://", "https://", "mailto:", "#", "data:")):
        return False
    if "{{" in target:  # template placeholder links are not real paths
        return False
    return True


def check_internal_links() -> list[str]:
    errors: list[str] = []
    for md_file in iter_markdown_files():
        text = md_file.read_text(encoding="utf-8")
        targets = MD_LINK.findall(text) + HTML_SRC.findall(text)
        for target in targets:
            if not is_internal(target):
                continue
            path_part = target.split("#", 1)[0].split("?", 1)[0]
            if not path_part:
                continue
            resolved = (md_file.parent / path_part).resolve()
            if not resolved.exists():
                rel = md_file.relative_to(REPO_ROOT)
                errors.append(f"{rel}: broken internal link -> {target}")
    return errors


def check_json_files() -> list[str]:
    errors: list[str] = []
    for json_file in REPO_ROOT.rglob("*.json"):
        if any(part in SKIP_DIRS for part in json_file.parts):
            continue
        try:
            json.loads(json_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{json_file.relative_to(REPO_ROOT)}: invalid JSON ({exc})")
    return errors


def check_json_templates() -> list[str]:
    errors: list[str] = []
    for template in (REPO_ROOT / "templates").glob("*.json.template"):
        text = template.read_text(encoding="utf-8")
        substituted = re.sub(r"\{\{[^}]*\}\}", "X", text)
        try:
            json.loads(substituted)
        except json.JSONDecodeError as exc:
            errors.append(
                f"{template.relative_to(REPO_ROOT)}: invalid after placeholder "
                f"substitution ({exc})"
            )
    return errors


def main() -> int:
    errors = check_internal_links() + check_json_files() + check_json_templates()
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        print(f"\n{len(errors)} problem(s) found")
        return 1
    print("All internal links resolve; all JSON files and templates are valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Validate benchmark case files against the repository conventions.

Checks performed:

- every case file has YAML front matter with the required fields,
- the ``id`` matches the filename prefix and is unique,
- every path listed under ``reference_data`` and ``figures`` exists,
- ``has_reference_data: true`` implies at least one existing data file,
- every key listed under ``references`` exists in ``references.bib``,
- every case file is listed in ``index.md``.

Exit code is non-zero if any check fails, so the script can gate CI.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FIELDS = [
    "id",
    "title",
    "status",
    "benchmark_class",
    "physics",
    "process",
    "dimension",
    "geometry",
    "interface_motion",
    "quantities_of_interest",
    "references",
]


def parse_frontmatter(text: str, path: Path) -> dict[str, object]:
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing YAML front matter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError(f"{path}: unclosed YAML front matter")
    block = text[4:end]

    # Minimal YAML subset parser (scalars and flat lists) to avoid a
    # dependency; the front matter in this repository only uses these.
    data: dict[str, object] = {}
    current_list: list[str] | None = None
    for raw_line in block.splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - ") and current_list is not None:
            current_list.append(line[4:].strip())
            continue
        match = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line)
        if not match:
            continue
        key, value = match.group(1), match.group(2).strip()
        if value == "":
            current_list = []
            data[key] = current_list
        else:
            current_list = None
            data[key] = value
    return data


def bib_keys() -> set[str]:
    text = (ROOT / "references.bib").read_text()
    return set(re.findall(r"^@\w+\{([^,]+),", text, flags=re.MULTILINE))


def main() -> int:
    errors: list[str] = []
    keys = bib_keys()
    index_text = (ROOT / "index.md").read_text()
    seen_ids: dict[str, str] = {}

    case_paths = sorted((ROOT / "cases").glob("*.md"))
    if not case_paths:
        errors.append("no case files found under cases/")

    for path in case_paths:
        rel = path.relative_to(ROOT)
        try:
            meta = parse_frontmatter(path.read_text(), path)
        except ValueError as exc:
            errors.append(str(exc))
            continue

        for field in REQUIRED_FIELDS:
            if field not in meta or meta[field] in ("", []):
                errors.append(f"{rel}: missing required field '{field}'")

        case_id = str(meta.get("id", ""))
        if case_id:
            if not path.name.startswith(case_id):
                errors.append(f"{rel}: id '{case_id}' does not prefix filename")
            if case_id in seen_ids:
                errors.append(
                    f"{rel}: duplicate id '{case_id}' (also in {seen_ids[case_id]})"
                )
            seen_ids[case_id] = path.name

        for field in ("reference_data", "figures"):
            entries = meta.get(field, [])
            if isinstance(entries, str):
                entries = [entries]
            for entry in entries:
                if not (ROOT / entry).is_file():
                    errors.append(f"{rel}: {field} path does not exist: {entry}")

        if str(meta.get("has_reference_data", "false")).lower() == "true":
            entries = meta.get("reference_data", [])
            if not entries:
                errors.append(
                    f"{rel}: has_reference_data is true but reference_data is empty"
                )

        refs = meta.get("references", [])
        if isinstance(refs, str):
            refs = [refs]
        for ref in refs:
            if ref not in keys:
                errors.append(f"{rel}: reference key not in references.bib: {ref}")

        if f"cases/{path.name}" not in index_text:
            errors.append(f"{rel}: not listed in index.md")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"{len(errors)} problem(s) found.", file=sys.stderr)
        return 1

    print(f"{len(case_paths)} case files validated, no problems found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

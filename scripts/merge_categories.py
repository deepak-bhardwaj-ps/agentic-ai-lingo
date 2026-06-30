#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore
except ModuleNotFoundError:  # pragma: no cover
    yaml = None


ROOT = Path(__file__).resolve().parents[1]
ITEMS_DIR = ROOT / "terms" / "items"
META_PATH = ROOT / "terms" / "meta.json"


def load_meta() -> dict[str, Any]:
    if not META_PATH.exists():
        return {}
    text = META_PATH.read_text(encoding="utf-8")
    if yaml is not None:
        try:
            data = yaml.safe_load(text) or {}
        except Exception:
            data = {}
    else:
        data = {}
    return data if isinstance(data, dict) else {}


def save_meta(meta: dict[str, Any]) -> None:
    if yaml is not None:
        text = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, default_flow_style=False)
    else:
        text = "\n".join(f"{k}: {v}" for k, v in meta.items()) + "\n"
    META_PATH.write_text(text, encoding="utf-8")


def parse_mapping(values: list[str]) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for item in values:
        if "=" not in item:
            raise SystemExit(f"Invalid mapping {item!r}; expected old=new")
        old, new = item.split("=", 1)
        old = old.strip()
        new = new.strip()
        if not old or not new:
            raise SystemExit(f"Invalid mapping {item!r}; both sides are required")
        mapping[old.lower()] = new
    return mapping


def merge_categories(mapping: dict[str, str], dry_run: bool) -> None:
    changed_files: list[Path] = []
    matched_categories: set[str] = set()
    seen_categories: set[str] = set()

    for path in sorted(ITEMS_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        match = re.search(r"(?ms)^---\n(.*?)\n---\n?(.*)$", text)
        if not match:
            continue
        raw_meta, body = match.groups()
        category_match = re.search(r"(?m)^category:\s*(.+?)\s*$", raw_meta)
        if not category_match:
            continue
        category = category_match.group(1).strip().strip('"')
        if category:
            seen_categories.add(category)
        replacement = mapping.get(category.lower())
        if not replacement or replacement == category:
            continue
        matched_categories.add(category)
        updated_meta = re.sub(
            r"(?m)^(category:\s*)(.+?)\s*$",
            rf"\1{replacement}",
            raw_meta,
            count=1,
        )
        changed_files.append(path)
        if not dry_run:
            path.write_text(f"---\n{updated_meta}\n---\n{body.lstrip()}", encoding="utf-8")

    meta = load_meta()
    categories = meta.get("categories") or []
    if not isinstance(categories, list):
        categories = []
    updated_categories: list[str] = []
    seen: set[str] = set()
    for category in categories:
        current = str(category).strip()
        if not current:
            continue
        replacement = mapping.get(current.lower(), current)
        key = replacement.lower()
        if key in seen:
            continue
        seen.add(key)
        updated_categories.append(replacement)
    if updated_categories != categories:
        meta["categories"] = updated_categories
        if not dry_run:
            save_meta(meta)

    print(f"Matched {len(changed_files)} files")
    missing = sorted(cat for cat in seen_categories if cat.lower() not in mapping)
    if missing:
        print("Unmapped categories:")
        for category in missing:
            print(f"  {category}")
    for path in changed_files[:20]:
        print(path.relative_to(ROOT))
    if len(changed_files) > 20:
        print(f"... and {len(changed_files) - 20} more")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--merge",
        action="append",
        default=[],
        help="Merge a category into another, in the form old=new. May be repeated.",
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    mapping = parse_mapping(args.merge)
    if not mapping:
        raise SystemExit("No merges supplied. Use --merge old=new at least once.")
    merge_categories(mapping, args.dry_run)


if __name__ == "__main__":
    main()

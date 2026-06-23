#!/usr/bin/env python3
from __future__ import annotations

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
README_PATH = ROOT / "README.md"

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.DOTALL)
WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
CODE_SPAN_RE = re.compile(r"```.*?```|`[^`\n]+`", re.DOTALL)
MARKDOWN_LINK_RE = re.compile(r"!? \[[^\]]+\]\([^)]+\)", re.VERBOSE)


def parse_markdown(text: str) -> tuple[dict[str, Any], str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    raw_meta, body = match.groups()
    if yaml is not None:
        meta = yaml.safe_load(raw_meta) or {}
    else:
        meta = parse_simple_frontmatter(raw_meta)
    if not isinstance(meta, dict):
        raise TypeError("Frontmatter must be a mapping.")
    return meta, body


def build_markdown(meta: dict[str, Any], body: str) -> str:
    if yaml is not None:
        raw_meta = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, default_flow_style=False).strip()
    else:
        raw_meta = dump_simple_frontmatter(meta)
    return f"---\n{raw_meta}\n---\n\n{body.lstrip()}"


def parse_simple_frontmatter(raw_meta: str) -> dict[str, Any]:
    meta: dict[str, Any] = {}
    current_key: str | None = None
    for line in raw_meta.splitlines():
        if line.startswith("- ") and current_key and isinstance(meta.get(current_key), list):
            item = line[2:].strip().strip('"')
            item = item.replace("https: //", "https://").replace("http: //", "http://")
            meta[current_key].append(item)
            continue
        if line.startswith(" ") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        current_key = key
        if value == "":
            meta[key] = []
        elif value.startswith("[") and value.endswith("]"):
            meta[key] = [item.strip().strip('"') for item in value[1:-1].split(",") if item.strip()]
        elif value.startswith('"') and value.endswith('"'):
            meta[key] = value[1:-1]
        else:
            meta[key] = value
    return meta


def dump_simple_frontmatter(meta: dict[str, Any]) -> str:
    lines: list[str] = []
    for key, value in meta.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"- {item}")
        else:
            lines.append(f"{key}: {value}")
    return "\n".join(lines).strip()


def split_protected(text: str, pattern: re.Pattern[str]) -> list[tuple[str, bool]]:
    chunks: list[tuple[str, bool]] = []
    cursor = 0
    for match in pattern.finditer(text):
        if match.start() > cursor:
            chunks.append((text[cursor:match.start()], False))
        chunks.append((match.group(0), True))
        cursor = match.end()
    if cursor < len(text):
        chunks.append((text[cursor:], False))
    return chunks


def normalise_existing_wikilinks(text: str, mapping: dict[str, str], stats: dict[str, int]) -> str:
    def replace(match: re.Match[str]) -> str:
        target = match.group(1).strip()
        label = match.group(2).strip() if match.group(2) else None
        canonical = mapping.get(target.lower())
        if not canonical or canonical == target:
            return match.group(0)
        stats["links_normalized"] += 1
        display = label or target
        return f"[[{canonical}]]" if display == canonical else f"[[{canonical}|{display}]]"

    return WIKILINK_RE.sub(replace, text)


def add_missing_wikilinks(text: str, candidates: list[dict[str, str]], stats: dict[str, int]) -> str:
    if not candidates:
        return text
    by_phrase = {item["phrase"].lower(): item["title"] for item in candidates}
    pattern = re.compile("|".join(re.escape(item["phrase"]) for item in candidates), re.IGNORECASE)

    def replace(match: re.Match[str]) -> str:
        before = text[match.start() - 1] if match.start() > 0 else ""
        after = text[match.end()] if match.end() < len(text) else ""
        if before and (before.isalnum() or before == "_"):
            return match.group(0)
        if after and (after.isalnum() or after == "_"):
            return match.group(0)
        display = match.group(0)
        title = by_phrase[display.lower()]
        stats["links_added"] += 1
        return f"[[{title}]]" if display == title else f"[[{title}|{display}]]"

    chunks: list[str] = []
    for chunk, protected in split_protected(text, re.compile(f"{WIKILINK_RE.pattern}|{MARKDOWN_LINK_RE.pattern}")):
        chunks.append(chunk if protected else pattern.sub(replace, chunk))
    return "".join(chunks)


def first_paragraph(body: str) -> str:
    for part in (segment.strip() for segment in body.split("\n\n")):
        if part:
            return re.sub(r"\s+", " ", part)
    return ""


def title_case_phrase(value: str) -> str:
    words = re.sub(r"[-_]+", " ", value).split()
    return " ".join(word if word.isupper() else word.capitalize() for word in words)


def section_lines(title: str, text: str) -> list[str]:
    return [f"## {title}", "", text, ""]


def load_meta() -> dict[str, Any]:
    if not META_PATH.exists():
        return {}
    text = META_PATH.read_text(encoding="utf-8")
    if yaml is not None:
        return yaml.safe_load(text) or {}
    return parse_simple_frontmatter(text)


def load_terms() -> list[dict[str, Any]]:
    terms = []
    for path in sorted(ITEMS_DIR.glob("*.md")):
        meta, body = parse_markdown(path.read_text(encoding="utf-8"))
        terms.append({"path": path, "meta": meta, "body": body})
    return terms


def validate_terms(terms: list[dict[str, Any]]) -> list[str]:
    errors = []
    for term in terms:
        meta = term["meta"]
        title = str(meta.get("title") or meta.get("name") or term["path"].stem).strip()
        if not str(meta.get("short_description") or "").strip():
            errors.append(f"{term['path'].relative_to(ROOT)}: missing short_description for {title}")
    return errors


def build_candidates(terms: list[dict[str, Any]]) -> list[dict[str, str]]:
    phrases: dict[str, dict[str, str] | None] = {}

    def add(phrase: str, title: str, note_id: str) -> None:
        key = phrase.lower()
        candidate = {"phrase": phrase, "title": title, "id": note_id}
        existing = phrases.get(key)
        if existing is None and key in phrases:
            return
        if existing and existing != candidate:
            phrases[key] = None
            return
        phrases[key] = candidate

    for term in terms:
        title = str(term["meta"].get("title") or term["meta"].get("name") or term["path"].stem).strip()
        add(title, title, term["path"].stem)
        for alias in term["meta"].get("aliases") or []:
            alias_text = str(alias).strip()
            if alias_text:
                add(alias_text, title, term["path"].stem)

    usable = [{"phrase": phrase, **target} for phrase, target in phrases.items() if target is not None]
    usable.sort(key=lambda item: len(item["phrase"]), reverse=True)
    return usable


def generate_readme(meta: dict[str, Any], terms: list[dict[str, Any]]) -> str:
    lines = [
        "# Agentic AI Buzzword Dictionary",
        "",
        "A living dictionary of agentic AI terminology, runtime language, governance terms, protocol vocabulary, and meme slang.",
        "",
    ]
    categories = meta.get("categories") or sorted({str(term["meta"].get("category") or "Uncategorised") for term in terms})
    by_category: dict[str, list[dict[str, Any]]] = {}
    for term in terms:
        category = str(term["meta"].get("category") or "Uncategorised")
        by_category.setdefault(category, []).append(term)
    for category in categories:
        group = sorted(by_category.get(category, []), key=lambda item: str(item["meta"].get("title") or item["path"].stem))
        if not group:
            continue
        lines.extend([f"## {category}", ""])
        for term in group:
            title = str(term["meta"].get("title") or term["meta"].get("name") or term["path"].stem)
            summary = str(term["meta"].get("short_description") or "").strip()
            rel = term["path"].as_posix().replace(str(ROOT.as_posix()) + "/", "")
            lines.append(f"- [{title}]({rel}): {summary}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    meta = load_meta()
    terms = load_terms()
    validation_errors = validate_terms(terms)
    if validation_errors:
        for error in validation_errors:
            print(error)
        raise SystemExit(1)
    candidates = build_candidates(terms)
    mapping = {item["phrase"].lower(): item["title"] for item in candidates}
    stats = {"links_added": 0, "links_normalized": 0}

    for term in terms:
        meta_doc = term["meta"]
        name = str(meta_doc.get("name") or "").strip()
        if name:
            meta_doc["title"] = name
        elif not str(meta_doc.get("title") or "").strip():
            meta_doc["title"] = term["path"].stem.replace("-", " ").title()
        body = term["body"]
        chunks: list[str] = []
        for chunk, protected in split_protected(body, CODE_SPAN_RE):
            if protected:
                chunks.append(chunk)
                continue
            filtered = [item for item in candidates if item["title"].lower() != str(meta_doc["title"]).lower()]
            normalized = normalise_existing_wikilinks(chunk, mapping, stats)
            chunks.append(add_missing_wikilinks(normalized, filtered, stats))
        term["body"] = "".join(chunks).strip() + "\n"
        term["path"].write_text(build_markdown(meta_doc, term["body"]), encoding="utf-8")

    README_PATH.write_text(generate_readme(meta, terms), encoding="utf-8")
    print(f"updated {len(terms)} terms, added {stats['links_added']} links, normalised {stats['links_normalized']} links")


if __name__ == "__main__":
    main()

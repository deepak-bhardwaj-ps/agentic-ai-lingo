#!/usr/bin/env python3
from __future__ import annotations

import re
from datetime import date
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
STATS_PATH = ROOT / "terms" / "stats.svg"

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
        try:
            meta = yaml.safe_load(raw_meta) or {}
        except Exception:
            meta = parse_simple_frontmatter(raw_meta)
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
                lines.append(f"- {dump_simple_scalar(item)}")
        else:
            lines.append(f"{key}: {dump_simple_scalar(value)}")
    return "\n".join(lines).strip()


def dump_simple_scalar(value: Any) -> str:
    text = str(value)
    if text == "":
        return '""'
    if re.fullmatch(r"[A-Za-z0-9_.:/@+-]+", text):
        return text
    escaped = text.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


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


def svg_escape(value: Any) -> str:
    return (
        str(value)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


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


def build_stats_svg(meta: dict[str, Any], terms: list[dict[str, Any]]) -> str:
    categories = [str(category).strip() for category in (meta.get("categories") or []) if str(category).strip()]
    if not categories:
        categories = sorted({str(term["meta"].get("category") or "Uncategorised") for term in terms})
    canonical_by_lower = {category.lower(): category for category in categories}
    counts = {category: 0 for category in categories}
    source_urls: set[str] = set()
    for term in terms:
        raw_category = str(term["meta"].get("category") or "Uncategorised").strip()
        category = canonical_by_lower.get(raw_category.lower(), raw_category)
        if category not in counts:
            continue
        counts[category] = counts.get(category, 0) + 1
        source_url = str(term["meta"].get("source_url") or "").strip()
        if source_url:
            source_urls.add(source_url)

    total_terms = len(terms)
    total_categories = len(categories)
    emerging_terms = sum(
        1
        for term in terms
        if str(term["meta"].get("status") or term["meta"].get("maturity") or "").lower() in {"emerging", "draft", "experimental"}
    )
    updated = date.today().strftime("%d %b %Y")

    cards = [
        ("Terms", str(total_terms), "#B3E6EC"),
        ("Categories", str(total_categories), "#F3A880"),
        ("Emerging", str(emerging_terms), "#9BB982"),
        ("Sources", str(len(source_urls)), "#FFA5A4"),
        ("Updated", updated.split()[0] + " " + updated.split()[1] + "\n" + updated.split()[2], "#4DC5D4"),
    ]

    widths = [165] * len(cards)
    gap = 22
    start_x = 44
    card_y = 51
    card_h = 108
    svg_width = 1000
    svg_height = 456
    parts = [
        f'<svg width="{svg_width}" height="{svg_height}" viewBox="0 0 {svg_width} {svg_height}" fill="none" xmlns="http://www.w3.org/2000/svg">',
        '<rect width="1000" height="456" fill="white"/>',
    ]
    x = start_x
    for idx, (label, value, fill) in enumerate(cards):
        parts.append(f'<rect x="{x + 1}" y="{card_y + 1}" width="{widths[idx] + 2}" height="{card_h}" rx="20" fill="{fill}"/>')
        parts.append(f'<rect x="{x}" y="{card_y}" width="{widths[idx]}" height="{card_h - 2}" rx="19" fill="#EFEFEF" opacity="0.0"/>')
        parts.append(f'<rect x="{x}" y="{card_y}" width="{widths[idx]}" height="{card_h - 2}" rx="19" fill="{fill}"/>')
        parts.append(f'<text fill="black" style="white-space: pre" xml:space="preserve" font-family="Arial" font-size="20"><tspan x="{x + 52}" y="78">{svg_escape(label)}</tspan></text>')
        if label == "Updated":
            parts.append(f'<text fill="black" style="white-space: pre" xml:space="preserve" font-family="Arial Black" font-size="24" font-weight="900"><tspan x="{x + 46}" y="114">{svg_escape(value.split()[0] + " " + value.split()[1])}</tspan></text>')
            parts.append(f'<text fill="black" style="white-space: pre" xml:space="preserve" font-family="Arial" font-size="20"><tspan x="{x + 62}" y="140">{svg_escape(value.split()[2])}</tspan></text>')
        else:
            font_size = 48 if len(value) < 3 else 40
            parts.append(f'<text fill="black" style="white-space: pre" xml:space="preserve" font-family="Arial Black" font-size="{font_size}" font-weight="900"><tspan x="{x + (49 if len(value) < 3 else 30)}" y="135">{svg_escape(value)}</tspan></text>')
        x += widths[idx] + gap

    parts.append('<text fill="black" style="white-space: pre" xml:space="preserve" font-family="Arial" font-size="32"><tspan x="43.5898" y="227.594">Number of terms by category</tspan></text>')
    parts.append('<g clip-path="url(#clip0)">')
    max_count = max(counts.values()) if counts else 1
    label_x = 43.5898
    label_font = 18
    label_w = max((len(category) for category in categories), default=0) * 10
    bar_x = min(350, label_x + label_w + 28)
    bar_y = 252
    row_h = 28
    chart_h = max(146, row_h * len(categories) + 8)
    svg_height = 456 + max(0, chart_h - 146)
    parts[0] = f'<svg width="{svg_width}" height="{svg_height}" viewBox="0 0 {svg_width} {svg_height}" fill="none" xmlns="http://www.w3.org/2000/svg">'
    parts[1] = f'<rect width="1000" height="{svg_height}" fill="white"/>'
    for index, category in enumerate(categories):
        count = counts.get(category, 0)
        y = bar_y + row_h * index
        bar_max = 1000 - bar_x - 110
        width = bar_max * (count / max_count) if max_count else 0
        text_y = y + 18
        parts.append(f'<text fill="black" style="white-space: pre" xml:space="preserve" font-family="Arial" font-size="{label_font}"><tspan x="{label_x}" y="{text_y:.3f}">{svg_escape(category)}</tspan></text>')
        if count:
            parts.append(f'<path d="M{bar_x} {y + 2}H{bar_x + width}C{bar_x + width + 5.8} {y + 2} {bar_x + width + 10.5} {y + 6.701} {bar_x + width + 10.5} {y + 12.5}V{y + 13.5}C{bar_x + width + 10.5} {y + 19.299} {bar_x + width + 5.8} {y + 24} {bar_x + width} {y + 24}H{bar_x}V{y + 2}Z" fill="#60A5FA"/>')
        else:
            parts.append(f'<path d="M{bar_x} {y + 2}H{bar_x + 10}V{y + 24}H{bar_x}V{y + 2}Z" fill="#E5E7EB"/>')
        parts.append(f'<text fill="black" style="white-space: pre" xml:space="preserve" font-family="Arial" font-size="18"><tspan x="914" y="{text_y:.3f}">{count}</tspan></text>')
    parts.append('</g>')
    parts.append(f'<defs><clipPath id="clip0"><rect width="915" height="{chart_h}" fill="white" transform="translate(43.5898 240)"/></clipPath></defs>')
    parts.append("</svg>")
    return "\n".join(parts)


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
        "![Dictionary stats](terms/stats.svg)",
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
            summary = str(term["meta"].get("short_description") or "")
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
    STATS_PATH.write_text(build_stats_svg(meta, terms), encoding="utf-8")
    README_PATH.write_text(generate_readme(meta, terms), encoding="utf-8")
    print(f"updated stats and README for {len(terms)} terms")


if __name__ == "__main__":
    main()

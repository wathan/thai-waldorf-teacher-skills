#!/usr/bin/env python3
"""Render one course markdown document to a print-ready A4 HTML copy beside it.

Standard library only. Usage:
    python3 render_html.py SOURCE.md [--force]
Prints a JSON report: the copy's path, whether it was written, the unsupported
markdown found (kept as plain text), and whether an existing copy was edited
since export (then kept, exit 3, unless --force). Exit 1: not a markdown file.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

PAGE = """<!doctype html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="export-digest" content="{digest}">
<title>{title}</title>
<style>
  @page {{ size: A4 portrait; margin: 20mm 18mm; }}
  body {{ margin: 0 auto; max-width: 174mm; padding: 16px; background: #fff; color: #111;
         font-family: "Sarabun", "TH Sarabun New", "Noto Sans Thai", sans-serif;
         font-size: 11pt; line-height: 1.5; }}
  h1 {{ font-size: 16pt; margin: 0 0 6pt; }}
  h2 {{ font-size: 13pt; margin: 12pt 0 4pt; border-bottom: 1px solid #999; }}
  h3, h4 {{ font-size: 11.5pt; margin: 10pt 0 4pt; }}
  p {{ margin: 0 0 6pt; }}
  table {{ width: 100%; border-collapse: collapse; margin: 0 0 8pt; font-size: 10pt; }}
  th, td {{ border: 1px solid #555; padding: 3pt 4pt; text-align: left; vertical-align: top; }}
  th {{ background: #eee; }}
  thead {{ display: table-header-group; }}
  tr {{ break-inside: avoid; }}
  ul, ol {{ margin: 0 0 6pt 18pt; padding: 0; }}
  ul.tasks {{ list-style: none; margin-left: 4pt; }}
  @media print {{ body {{ padding: 0; max-width: none; }} }}
</style>
</head>
<body>
{body}
</body>
</html>
"""

HEADING = re.compile(r"^(#{1,4})\s+(.*?)\s*#*\s*$")


@dataclass
class Result:
    out: Path
    written: bool = True
    edited_copy: bool = False
    unsupported: list = field(default_factory=list)


BOLD = re.compile(r"\*\*(?=\S)(.+?)(?<=\S)\*\*|__(?=\S)(.+?)(?<=\S)__")
ITALIC = re.compile(r"(?<![\w*])\*(?=\S)(.+?)(?<=\S)\*(?![\w*])|(?<![\w_])_(?=\S)(.+?)(?<=\S)_(?![\w_])")


def inline(text: str) -> str:
    text = html.escape(text, quote=False)
    text = BOLD.sub(lambda m: f"<strong>{m.group(1) or m.group(2)}</strong>", text)
    return ITALIC.sub(lambda m: f"<em>{m.group(1) or m.group(2)}</em>", text)


TASK = re.compile(r"^[-*+]\s+\[([ xX])\]\s+(.*)$")
BULLET = re.compile(r"^[-*+]\s+(.*)$")
NUMBERED = re.compile(r"^\d+[.)]\s+(.*)$")
TABLE_ROW = re.compile(r"^\|.*\|$")
TABLE_RULE = re.compile(r"^\|(\s*:?-+:?\s*\|)+$")
BR = re.compile(r"<br\s*/?>", re.I)


def cells(row: str) -> list:
    return [cell.strip() for cell in row.strip()[1:-1].split("|")]


def cell_html(text: str) -> str:
    return "<br>".join(inline(part) for part in BR.split(text))


class Blocks:
    """Collects block-level html, one open paragraph, list or table at a time."""

    def __init__(self):
        self.html, self.para, self.items, self.rows = [], [], [], []
        self.list_tag, self.list_open = "", ""

    def flush(self):
        if self.para:
            self.html.append(f"<p>{inline(' '.join(self.para))}</p>")
        if self.items:
            self.html.append("\n".join([self.list_open, *self.items, f"</{self.list_tag}>"]))
        if self.rows:
            head, *body = self.rows
            row = lambda tag, r: "<tr>" + "".join(f"<{tag}>{cell_html(c)}</{tag}>" for c in r) + "</tr>"
            self.html.append("\n".join(
                ["<table>", f"<thead>{row('th', head)}</thead>", "<tbody>",
                 *(row("td", r) for r in body), "</tbody>", "</table>"]))
        self.para, self.items, self.rows = [], [], []

    def item(self, tag, opening, text):
        if self.para or self.rows or (self.items and self.list_open != opening):
            self.flush()
        self.list_tag, self.list_open = tag, opening
        self.items.append(f"<li>{text}</li>")

    def raw(self, line):
        self.flush()
        self.html.append(f"<p>{html.escape(line, quote=False)}</p>")

    def row(self, line):
        if self.para or self.items:
            self.flush()
        if not TABLE_RULE.match(line):
            self.rows.append(cells(line))


FENCE = re.compile(r"^(```|~~~)")
QUOTE = re.compile(r"^>")
RULE = re.compile(r"^(-{3,}|\*{3,}|_{3,})$")
NESTED = re.compile(r"^(\s{2,}|\t)([-*+]|\d+[.)])\s+")
IMAGE = re.compile(r"!\[[^\]]*\]\([^)]*\)")
LINK = re.compile(r"(?<!!)\[[^\]]+\]\([^)]*\)")
CODE = re.compile(r"`[^`]+`")


def plain(text: str) -> str:
    """Text with emphasis markers removed, escaped: for the page title."""
    text = BOLD.sub(lambda m: m.group(1) or m.group(2), text)
    return html.escape(ITALIC.sub(lambda m: m.group(1) or m.group(2), text), quote=False)


def to_html(markdown: str) -> tuple[str, str, list]:
    """Return (title, body html, sorted names of unsupported markdown found)."""
    title, blocks, found, in_fence = "", Blocks(), set(), False
    for line in markdown.splitlines():
        stripped = line.strip()
        if FENCE.match(stripped):
            found.add("code block")
            blocks.flush()
            in_fence = not in_fence
            continue
        if in_fence:
            blocks.raw(line)
            continue
        for name, pattern in (("image", IMAGE), ("link", LINK), ("inline code", CODE)):
            if pattern.search(line):
                found.add(name)
        heading = HEADING.match(line)
        task = TASK.match(stripped)
        bullet = BULLET.match(stripped)
        numbered = NUMBERED.match(stripped)
        if heading:
            blocks.flush()
            level, text = len(heading.group(1)), heading.group(2)
            if level == 1 and not title:
                title = text
            blocks.html.append(f"<h{level}>{inline(text)}</h{level}>")
        elif TABLE_ROW.match(stripped):
            blocks.row(stripped)
        elif QUOTE.match(stripped):
            found.add("blockquote")
            blocks.raw(stripped)
        elif RULE.match(stripped):
            found.add("horizontal rule")
            blocks.raw(stripped)
        elif task or bullet or numbered:
            if NESTED.match(line):
                found.add("nested list")
            if task:
                box = "☐" if task.group(1) == " " else "☑"
                blocks.item("ul", '<ul class="tasks">', f"{box} {inline(task.group(2))}")
            elif bullet:
                blocks.item("ul", "<ul>", inline(bullet.group(1)))
            else:
                blocks.item("ol", "<ol>", inline(numbered.group(1)))
        elif not stripped:
            blocks.flush()
        else:
            if blocks.items or blocks.rows:
                blocks.flush()
            blocks.para.append(stripped)
    blocks.flush()
    return title, "\n".join(blocks.html), sorted(found)


DIGEST = re.compile(r'(<meta name="export-digest" content=")([0-9a-f]*)(">)')


def digest(page: str) -> str:
    """Hash of a page with its own digest left blank."""
    blank = DIGEST.sub(r"\g<1>\g<3>", page, count=1)
    return hashlib.sha256(blank.encode("utf-8")).hexdigest()


def edited_since_export(copy: Path) -> bool:
    """True when the copy no longer matches the digest it was exported with."""
    page = copy.read_text(encoding="utf-8", errors="replace")
    recorded = DIGEST.search(page)
    return not recorded or recorded.group(2) != digest(page)


def render(source: Path, force: bool = False) -> Result:
    """Write SOURCE's HTML copy beside it, unless the copy was edited and not forced."""
    source = Path(source)
    out = source.with_suffix(".html")
    title, body, unsupported = to_html(source.read_text(encoding="utf-8"))
    if out.exists() and not force and edited_since_export(out):
        return Result(out=out, written=False, edited_copy=True, unsupported=unsupported)
    page = PAGE.format(title=plain(title) or html.escape(source.stem), body=body, digest="")
    out.write_text(DIGEST.sub(rf"\g<1>{digest(page)}\g<3>", page, count=1), encoding="utf-8")
    return Result(out=out, unsupported=unsupported)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Render a course markdown document to an A4 HTML copy beside it.")
    parser.add_argument("source", type=Path)
    parser.add_argument("--force", action="store_true", help="overwrite a copy edited since export")
    args = parser.parse_args(argv)
    if args.source.suffix.lower() != ".md" or not args.source.is_file():
        print(json.dumps({"error": f"not a markdown file: {args.source}"}, ensure_ascii=False))
        return 1
    result = render(args.source, force=args.force)
    print(json.dumps({"out": str(result.out), "written": result.written,
                      "edited_copy": result.edited_copy, "unsupported": result.unsupported},
                     ensure_ascii=False))
    return 3 if result.edited_copy else 0


if __name__ == "__main__":
    sys.exit(main())

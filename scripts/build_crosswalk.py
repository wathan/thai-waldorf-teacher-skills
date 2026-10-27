#!/usr/bin/env python3
"""Generate the curriculum crosswalk from the plugin's reference corpus.

Usage:
  uv run --no-project python scripts/build_crosswalk.py           # rewrite it
  uv run --no-project python scripts/build_crosswalk.py --check   # exit 1 if stale

Reads four files in plugins/thai-waldorf-science/references/ and writes
references/curriculum-crosswalk.md next to them:

  thai-science-core-indicators-2560.md       Thai indicators ม.3–ม.6 (verbatim)
  thai-science-glossary-2560.md              official indicator verbs
  waldorf-upper-school-macro-curriculum.md   Waldorf grade modes G9–G12
  waldorf-pisa-competencies-g9-g12.md        PISA-adapted competencies G9–G12

Regenerate whenever one of those files changes, then commit both. The test
suite fails while the committed crosswalk differs from what this script
produces. Standard library only; output is deterministic.
"""

import re
import sys
from pathlib import Path

from plugin_paths import plugin_dir

REPO = Path(__file__).resolve().parents[1]
REFERENCES = plugin_dir(REPO) / "references"
OUTPUT_NAME = "curriculum-crosswalk.md"

INDICATORS_FILE = "thai-science-core-indicators-2560.md"
GLOSSARY_FILE = "thai-science-glossary-2560.md"
MACRO_FILE = "waldorf-upper-school-macro-curriculum.md"
PISA_FILE = "waldorf-pisa-competencies-g9-g12.md"

THAI_GRADES = ("ม.3", "ม.4", "ม.5", "ม.6")

INDICATOR_LINE = re.compile(r"^\d+\.\s+`(ว (\d+\.\d+) (ม\.\d)/(\d+))`\s+(.*\S)\s*$")


def read(references: Path, name: str) -> str:
    return (references / name).read_text(encoding="utf-8")


def parse_indicators(text: str) -> list:
    """Return dicts (code, standard, grade, text) for ม.3–ม.6, in source order."""
    found = []
    for line in text.split("\n"):
        match = INDICATOR_LINE.match(line)
        if match and match.group(3) in THAI_GRADES:
            code, standard, grade, _, wording = match.groups()
            found.append({"code": code, "standard": standard, "grade": grade, "text": wording})
    return found


STANDARD_HEADING = re.compile(r"^### มาตรฐาน (ว \d+\.\d+)\s*$")


def parse_standards(text: str) -> list:
    """Return (code, wording) per standard, wording being the paragraph under its heading."""
    standards, pending = [], None
    for line in text.split("\n"):
        heading = STANDARD_HEADING.match(line)
        if heading:
            pending = heading.group(1)
        elif pending and line.strip():
            standards.append((pending, line.strip()))
            pending = None
    return standards


def render_standards_matrix(standards: list, modes: dict, indicators: list) -> list:
    head = " | ".join(f"{g} ({modes[g]['waldorf']})" if g in modes else g for g in THAI_GRADES)
    lines = [
        "## 2. Thai standards × grade",
        "",
        "Number of core indicators (ตัวชี้วัด) per standard and grade. "
        "Standard wording verbatim.",
        "",
        f"| Standard | มาตรฐาน (verbatim) | {head} |",
        "|---|---|" + "---|" * len(THAI_GRADES),
    ]
    for code, wording in standards:
        nums = []
        for g in THAI_GRADES:
            n = sum(1 for i in indicators if i["grade"] == g and f"ว {i['standard']}" == code)
            nums.append(str(n) if n else "Gap")
        lines.append(f"| {code} | {cell(wording)} | {' | '.join(nums)} |")
    lines.append("")
    return lines


# Verbs whose kind of thinking the macro curriculum names as one grade's
# capacity (Observation G9, Comparison G10, Analysis and models G11), as the
# glossary's agent note does for สังเกต and สร้างแบบจำลอง. Only a verb from a
# later grade than the indicator's is noted: earlier modes stay valid.
VERB_MODES = {
    "สังเกต": 9, "บรรยาย": 9, "บันทึก": 9,
    "เปรียบเทียบ": 10,
    "วิเคราะห์": 11, "สร้างแบบจำลอง": 11,
}


def mode_notes(grade: str, modes: dict, verbs_used: list) -> list:
    waldorf = modes.get(grade, {}).get("waldorf")
    if not waldorf:
        return []
    level = int(waldorf[1:])
    return [
        f"{thai} → G{VERB_MODES[thai]}, above {waldorf}"
        for thai, _ in verbs_used
        if VERB_MODES.get(thai, 0) > level
    ]


GRADE_CARD = re.compile(r"^### Grade (\d+): \*(.+?)\* \((ม\.\d)\)\s*$")
CARD_FIELD = re.compile(r"^- \*\*(Question|Capacity|Motif):\*\* (.*\S)\s*$")


def parse_grade_modes(text: str) -> dict:
    """Return {thai grade: {waldorf, mode, Question, Capacity, Motif}} from the cards."""
    modes, current = {}, None
    for line in text.split("\n"):
        card = GRADE_CARD.match(line)
        if card:
            current = {"waldorf": f"G{card.group(1)}", "mode": card.group(2)}
            modes[card.group(3)] = current
        elif line.startswith(("## ", "---")):
            current = None
        elif current is not None:
            field = CARD_FIELD.match(line)
            if field:
                current[field.group(1)] = field.group(2)
    return modes


GLOSSARY_ROW = re.compile(r"^\|\s*\d+\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|")


def parse_glossary_verbs(text: str) -> list:
    """Return (thai, english) for the science indicator verbs (first table only).

    A slashed entry such as "เขียนแผนผัง/วาดภาพ" yields one verb per alternative.
    The technology table holds nouns (algorithm, technology...), not verbs.
    """
    verbs, in_science = [], False
    for line in text.split("\n"):
        if line.startswith("## "):
            in_science = "วิทยาศาสตร์" in line
            continue
        match = GLOSSARY_ROW.match(line) if in_science else None
        if match:
            for thai in match.group(1).split("/"):
                if thai.strip():
                    verbs.append((thai.strip(), match.group(2).strip()))
    return verbs


def verbs_in(text: str, verbs: list) -> list:
    """Glossary verbs occurring in text, in order of first use.

    An occurrence lying wholly inside an occurrence of a longer verb is not
    counted (ทดลอง inside ออกแบบการทดลอง).
    """
    spans = []
    for thai, english in verbs:
        start = text.find(thai)
        while start != -1:
            spans.append((start, start + len(thai), thai, english))
            start = text.find(thai, start + 1)
    kept = [
        s for s in spans
        if not any(o[0] <= s[0] and s[1] <= o[1] and (o[1] - o[0]) > (s[1] - s[0]) for o in spans)
    ]
    seen, ordered = set(), []
    for _, _, thai, english in sorted(kept):
        if thai not in seen:
            seen.add(thai)
            ordered.append((thai, english))
    return ordered


# Link rules: an indicator is linked to a PISA-adapted headline when it uses
# one of the headline's official verbs (S1-S3) or, for E1-E3, environment
# terms. They are documented in the crosswalk itself; change them here only.
HEADLINES = ("S1", "S2", "S3", "E1", "E2", "E3")
VERB_RULES = {
    "S1": ("อธิบาย", "บรรยาย", "สร้างแบบจำลอง", "คาดคะเน", "คำนวณ", "ยกตัวอย่าง",
           "เขียนแผนผัง", "วาดภาพ"),
    "S2": ("ตั้งคำถาม", "กำหนดปัญหา", "ออกแบบการทดลอง", "ทดลอง", "สังเกต", "วัด",
           "สำรวจ", "บันทึก", "แปลความหมาย", "วิเคราะห์"),
    "S3": ("สืบค้นข้อมูล", "อภิปราย", "นำเสนอ", "สื่อสาร"),
}
ENVIRONMENT_TERMS = ("สิ่งแวดล้อม", "ระบบนิเวศ", "ทรัพยากรธรรมชาติ", "ความหลากหลายทางชีวภาพ",
                     "ภูมิอากาศ", "พื้นที่เสี่ยงภัย")
ACTION_TERMS = ("แนวทาง", "แนวปฏิบัติ", "อนุรักษ์", "ดูแลรักษา")
AWARENESS_TERMS = ("ตระหนัก",)


def pisa_links(text: str, verbs_used: list) -> list:
    used = {thai for thai, _ in verbs_used}
    links = [h for h, rule in VERB_RULES.items() if used & set(rule)]
    if any(t in text for t in ENVIRONMENT_TERMS):
        links.append("E1")
        if any(t in text for t in ACTION_TERMS):
            links.append("E2")
        if any(t in text for t in AWARENESS_TERMS):
            links.append("E3")
    return links


def render_link_rules() -> list:
    lines = [
        "## 4. Link rules",
        "",
        "Links between a Thai indicator and a PISA-adapted headline are generated by the "
        "rules below. They are candidates for planning, not alignment judgements: confirm "
        "each against the full statements before claiming it. Neither framework's wording "
        "is changed by a link.",
        "",
        "| Headline | Linked when the indicator… |",
        "|---|---|",
    ]
    for headline, rule in VERB_RULES.items():
        lines.append(f"| {headline} | uses an official verb: {', '.join(rule)} |")
    env = ", ".join(ENVIRONMENT_TERMS)
    lines += [
        f"| E1 | names an environment term: {env} |",
        f"| E2 | is linked to E1 and names an action term: {', '.join(ACTION_TERMS)} |",
        f"| E3 | is linked to E1 and names an awareness term: {', '.join(AWARENESS_TERMS)} |",
        "",
        "Indicator verbs are found by their official wording in "
        "`thai-science-glossary-2560.md` (science table); a verb inside a longer official "
        "verb (ทดลอง in ออกแบบการทดลอง) counts once, as the longer verb.",
        "",
    ]
    return lines


PISA_GRADE = re.compile(r"^# Grade (\d+)\s*$")
PISA_HEADLINE = re.compile(r"^## ([SE]\d) — (.*\S)\s*$")
PISA_THAI = re.compile(r"^\*\*([^*]+)\*\*\s*$")
PISA_ITEM = re.compile(r"^\*\*([SE]\d\.\d+) — (.+?)\*\* · `(\w+)`")


def parse_pisa(text: str) -> tuple:
    """Return (headlines {code: (en, th)}, items {G9: [(code, title, tag)]})."""
    headlines, items, grade, last_headline = {}, {}, None, None
    for line in text.split("\n"):
        g = PISA_GRADE.match(line)
        if g:
            grade = f"G{g.group(1)}"
            items[grade] = []
            continue
        if line.startswith("# "):
            grade = None  # lineage table and anything after the grade sections
            continue
        if grade is None:
            continue
        h = PISA_HEADLINE.match(line)
        if h:
            last_headline = h.group(1)
            headlines.setdefault(last_headline, [h.group(2), ""])
            continue
        th = PISA_THAI.match(line)
        if th and last_headline and not headlines[last_headline][1]:
            headlines[last_headline][1] = th.group(1)
            last_headline = None
            continue
        item = PISA_ITEM.match(line)
        if item:
            items[grade].append(item.groups())
    return {k: tuple(v) for k, v in headlines.items()}, items


def render_pisa_matrix(headlines: dict, modes: dict, counts: dict) -> list:
    head = " | ".join(f"{g} ({modes[g]['waldorf']})" if g in modes else g for g in THAI_GRADES)
    lines = [
        "## 3. PISA-adapted competencies × grade",
        "",
        "Number of Thai indicators linked to each headline by the link rules (§4). "
        "Headlines are PISA 2025 verbatim (EN) and PISA TH verbatim (TH).",
        "",
        f"| Headline | PISA 2025 | PISA TH | {head} |",
        "|---|---|---|" + "---|" * len(THAI_GRADES),
    ]
    for code in HEADLINES:
        en, th = headlines.get(code, ("Gap: not in the competencies file", ""))
        nums = " | ".join(str(counts[(code, g)]) if counts[(code, g)] else "Gap" for g in THAI_GRADES)
        lines.append(f"| {code} | {cell(en)} | {cell(th)} | {nums} |")
    lines.append("")
    return lines


def cell(text: str) -> str:
    return text.replace("|", "\\|")


def render_grade_bands(modes: dict) -> list:
    lines = [
        "## 1. Grade bands",
        "",
        "Thai ม. grades serve as the bands; each is paired with its Waldorf grade "
        "(assumed mapping in the macro curriculum) and that grade mode's own words.",
        "",
        "| Thai grade | Waldorf grade mode | Question | Capacity | Motif (localise) |",
        "|---|---|---|---|---|",
    ]
    for grade in THAI_GRADES:
        m = modes.get(grade)
        if m is None:
            lines.append(f"| {grade} | Gap: no grade card | — | — | — |")
            continue
        lines.append(
            f"| {grade} | {m['waldorf']} *{m['mode']}* | {cell(m.get('Question', 'Gap'))} "
            f"| {cell(m.get('Capacity', 'Gap'))} | {cell(m.get('Motif', 'Gap'))} |"
        )
    lines += [
        "",
        "**Gap: Waldorf block placement.** The reference corpus holds no list of which "
        "main lesson blocks sit in which grade. Placement is by grade mode only: read a "
        "block's fit from the grade mode above and the placement diagnostic in "
        "`waldorf-upper-school-macro-curriculum.md` §5.",
        "",
    ]
    return lines


def grade_heading(grade: str, modes: dict) -> str:
    m = modes.get(grade)
    return f"## {grade} · {m['waldorf']} *{m['mode']}*" if m else f"## {grade} · Gap: no grade card"


def render_grade_section(grade: str, modes: dict, indicators: list, pisa_items: dict) -> list:
    lines = [grade_heading(grade, modes), ""]
    waldorf = modes.get(grade, {}).get("waldorf")
    items = pisa_items.get(waldorf, [])
    lines.append(f"**PISA-adapted sub-abilities ({waldorf or 'no Waldorf grade'}):** " + (
        "; ".join(f"{code} — {title} · {tag}" for code, title, tag in items)
        if items else "Gap: none in the competencies file."
    ))
    lines.append("")
    rows = [i for i in indicators if i["grade"] == grade]
    lines += [
        "| Code | ตัวชี้วัด (verbatim) | Indicator verbs (glossary) | PISA-adapted (link rules) "
        "| Grade-mode note |",
        "|---|---|---|---|---|",
    ]
    for ind in rows:
        verb_cell = ", ".join(f"{t} ({e})" for t, e in ind["verbs"]) or "Gap: no glossary verb"
        link_cell = ", ".join(ind["links"]) or "Gap: no link rule matches"
        note_cell = "; ".join(mode_notes(grade, modes, ind["verbs"])) or "—"
        lines.append(
            f"| `{ind['code']}` | {cell(ind['text'])} | {cell(verb_cell)} | {link_cell} "
            f"| {cell(note_cell)} |"
        )
    lines.append("")
    return lines


def render_header(modes: dict) -> list:
    sources = (INDICATORS_FILE, GLOSSARY_FILE, MACRO_FILE, PISA_FILE)
    grade_entries = [f"- {grade_heading(g, modes)[3:]}" for g in THAI_GRADES]
    return [
        "# Curriculum crosswalk (G9–G12 / ม.3–ม.6)",
        "",
        "> **Generated file. Do not edit by hand.** Built from "
        + ", ".join(f"`{s}`" for s in sources)
        + ". When any of them changes, regenerate in the source repository with "
        "`uv run --no-project python scripts/build_crosswalk.py` and commit the result; "
        "`--check` reports a stale crosswalk and the test suite fails on one.",
        ">",
        "> **Agent use:**",
        "> - **Role:** relates Thai core indicators, Waldorf grade modes and PISA-adapted "
        "competencies for upper-school science. Read it before matching indicators to a "
        "teaching sequence; do not match by hand.",
        "> - **Three frameworks side by side, never merged.** Each keeps its own wording and "
        "codes. Thai ม. grades are the bands; there is no KUD or band translation.",
        "> - **Gaps are explicit.** A cell reading *Gap* means the sources hold nothing there; "
        "report it, do not fill it.",
        "> - **Links are candidates** generated by the rules in §4, not alignment judgements.",
        "> - **Quote indicators from here or the indicators file**, code and Thai wording "
        "verbatim; read their verbs through `thai-science-glossary-2560.md`.",
        "",
        "## Contents",
        "",
        "- 1. Grade bands",
        "- 2. Thai standards × grade",
        "- 3. PISA-adapted competencies × grade",
        "- 4. Link rules",
        *grade_entries,
        "- Not in this crosswalk",
        "",
    ]


def render_out_of_scope() -> list:
    return [
        "## Not in this crosswalk",
        "",
        "- **Supplementary learning outcomes** (ผลการเรียนรู้ เพิ่มเติม, ม.4–6 science "
        "track): they are not indicators and their codes are not official. Read "
        "`thai-science-supplementary-learning-outcomes-2560.md` directly for elective "
        "courses.",
        "- **Indicators below ม.3**: outside the upper school.",
        "- **Full PISA-adapted statements**: only codes, titles and tags are listed; the "
        "statements are in `waldorf-pisa-competencies-g9-g12.md`.",
        "- **Core content** (สาระการเรียนรู้แกนกลาง): in the indicators file under each grade.",
        "",
    ]


def build_crosswalk(references: Path) -> str:
    indicators = parse_indicators(read(references, INDICATORS_FILE))
    modes = parse_grade_modes(read(references, MACRO_FILE))
    verbs = parse_glossary_verbs(read(references, GLOSSARY_FILE))
    headlines, pisa_items = parse_pisa(read(references, PISA_FILE))
    for ind in indicators:
        ind["verbs"] = verbs_in(ind["text"], verbs)
        ind["links"] = pisa_links(ind["text"], ind["verbs"])
    counts = {
        (h, g): sum(1 for i in indicators if i["grade"] == g and h in i["links"])
        for h in HEADLINES for g in THAI_GRADES
    }
    lines = render_header(modes)
    standards = parse_standards(read(references, INDICATORS_FILE))
    lines += render_grade_bands(modes)
    lines += render_standards_matrix(standards, modes, indicators)
    lines += render_pisa_matrix(headlines, modes, counts)
    lines += render_link_rules()
    for grade in THAI_GRADES:
        lines += render_grade_section(grade, modes, indicators, pisa_items)
    lines += render_out_of_scope()
    return "\n".join(lines).rstrip("\n") + "\n"


def main(argv) -> int:
    references = Path(argv[argv.index("--references") + 1]) if "--references" in argv else REFERENCES
    target = references / OUTPUT_NAME
    content = build_crosswalk(references)
    if "--check" in argv:
        current = target.read_text(encoding="utf-8") if target.is_file() else ""
        if current != content:
            print(f"{target.name} is stale; run scripts/build_crosswalk.py and commit it")
            return 1
        print(f"{target.name} is up to date")
        return 0
    target.write_text(content, encoding="utf-8")
    print(f"wrote {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

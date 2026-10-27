#!/usr/bin/env python3
"""Static structure validator for this repo's plugin marketplace (spec #1, seam 2).

Usage: uv run --no-project python scripts/validate.py [REPO_ROOT]

Standard library only, so it runs offline and in CI without installs.
Every plugin listed in .claude-plugin/marketplace.json is checked, and every
skill directory under a plugin's skills/ is discovered automatically, so new
skills need no change here. Repo-only maintainer skills in .claude/skills/
get the same SKILL.md and upstream-record checks.
"""

import json
import re
import sys
from pathlib import Path

KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MANIFEST_REQUIRED = ("version", "description", "author", "license")


class Report:
    def __init__(self, root: Path):
        self.root = root
        self.errors = []

    def error(self, path: Path, message: str) -> None:
        try:
            where = path.relative_to(self.root)
        except ValueError:
            where = path
        self.errors.append(f"{where}: {message}")


def load_json(report: Report, path: Path):
    if not path.is_file():
        report.error(path, "missing")
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        report.error(path, f"invalid JSON ({exc})")
        return None


def check_marketplace(report: Report) -> list:
    """Return (entry_name, plugin_dir) for each plugin entry that resolves."""
    path = report.root / ".claude-plugin/marketplace.json"
    market = load_json(report, path)
    if market is None:
        return []
    for key in ("name", "owner", "plugins"):
        if key not in market:
            report.error(path, f"missing '{key}'")
    plugins = []
    for i, entry in enumerate(market.get("plugins", [])):
        name, source = entry.get("name"), entry.get("source")
        if not name or not isinstance(source, str):
            report.error(path, f"plugins[{i}] needs 'name' and string 'source'")
            continue
        if not source.startswith("./"):
            report.error(path, f"plugins[{i}] source {source!r} must start with ./")
            continue
        plugin_dir = (report.root / source).resolve()
        if not plugin_dir.is_dir():
            report.error(path, f"plugins[{i}] source {source} does not exist")
            continue
        plugins.append((name, plugin_dir))
    return plugins


def check_manifest(report: Report, entry_name: str, plugin_dir: Path) -> None:
    path = plugin_dir / ".claude-plugin/plugin.json"
    manifest = load_json(report, path)
    if manifest is None:
        return
    name = manifest.get("name", "")
    if not KEBAB.match(name):
        report.error(path, f"name {name!r} must be kebab-case")
    if name != entry_name:
        report.error(path, f"name {name!r} does not match marketplace entry {entry_name!r}")
    for key in MANIFEST_REQUIRED:
        if not manifest.get(key):
            report.error(path, f"missing '{key}'")


class FrontmatterError(ValueError):
    pass


def _scalar(raw: str) -> str:
    raw = raw.strip()
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "'\"":
        return raw[1:-1]
    return raw


def parse_frontmatter(text: str) -> dict:
    """Parse the YAML subset used in SKILL.md frontmatter.

    Supports top-level `key: value`, quoted scalars, folded (>) and literal (|)
    block scalars, and indented nested blocks (kept as raw text). Enough for
    the portable skill keys without a YAML dependency.
    """
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        raise FrontmatterError("must start with a --- frontmatter block")
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        raise FrontmatterError("frontmatter block is not closed with ---")
    data, key, block, style = {}, None, [], None

    def flush():
        if key is not None and style is not None:
            parts = [b.strip() for b in block]
            data[key] = (" ".join(p for p in parts if p) if style == ">" else "\n".join(parts)).strip()

    for line in lines[1:end]:
        if line.startswith((" ", "\t")) or not line.strip():
            if key is None:
                if line.strip():
                    raise FrontmatterError(f"unexpected indented line: {line!r}")
                continue
            block.append(line)
            continue
        flush()
        match = re.match(r"^([A-Za-z0-9_-]+):(.*)$", line)
        if not match:
            raise FrontmatterError(f"cannot parse line: {line!r}")
        key, rest = match.group(1), match.group(2).strip()
        block = []
        if rest[:1] in (">", "|"):
            style = rest[0]
        elif rest == "":
            style = "|"  # nested mapping or list: keep raw
        else:
            style = None
            data[key] = _scalar(rest)
    flush()
    return data


SKILL_KEYS = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
SKILL_MAX_LINES = 500
DESCRIPTION_MAX = 1024
RESERVED_WORDS = ("anthropic", "claude")
FIRST_OR_SECOND_PERSON = re.compile(r"^\s*(I|I'm|We|You|Your)\b|\b(I can|you can|we can)\b", re.I)


def check_skill(report: Report, skill_dir: Path) -> None:
    path = skill_dir / "SKILL.md"
    if not path.is_file():
        report.error(path, "missing")
        return
    text = path.read_text(encoding="utf-8")
    if text.count("\n") + (0 if text.endswith("\n") else 1) > SKILL_MAX_LINES:
        report.error(path, f"longer than {SKILL_MAX_LINES} lines")
    try:
        fm = parse_frontmatter(text)
    except FrontmatterError as exc:
        report.error(path, f"frontmatter: {exc}")
        return
    for key in sorted(set(fm) - SKILL_KEYS):
        report.error(path, f"frontmatter key '{key}' not in portable set {sorted(SKILL_KEYS)}")
    name = fm.get("name", "")
    if not KEBAB.match(name) or len(name) > 64:
        report.error(path, f"name {name!r} must be kebab-case, at most 64 chars")
    if any(word in name for word in RESERVED_WORDS):
        report.error(path, f"name {name!r} contains a reserved word")
    if name != skill_dir.name:
        report.error(path, f"name {name!r} does not match directory {skill_dir.name!r}")
    desc = fm.get("description", "")
    if not desc:
        report.error(path, "description missing")
        return
    if len(desc) > DESCRIPTION_MAX:
        report.error(path, f"description longer than {DESCRIPTION_MAX} chars")
    if "<" in desc or ">" in desc:
        report.error(path, "description contains angle brackets")
    if FIRST_OR_SECOND_PERSON.search(desc):
        report.error(path, "description must be written in the third person")
    if "use when" not in desc.lower():
        report.error(path, "description must say when to use the skill ('Use when ...')")


PLUGIN_PATH = re.compile(r"\$\{CLAUDE_PLUGIN_ROOT\}/([^\s`)'\"]+)")
SKILL_PATH = re.compile(r"\$\{CLAUDE_SKILL_DIR\}/([^\s`)'\"]+)")


def check_skill_paths(report: Report, plugin_dir: Path, skill_dir: Path) -> None:
    """Every ${CLAUDE_PLUGIN_ROOT}/... or ${CLAUDE_SKILL_DIR}/... path must exist."""
    for md in sorted(skill_dir.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        for pattern, base in ((PLUGIN_PATH, plugin_dir), (SKILL_PATH, skill_dir)):
            for rel in pattern.findall(text):
                rel = rel.rstrip(".,:;")
                if not (base / rel).exists():
                    report.error(md, f"path {rel} does not resolve")


TOC_THRESHOLD = 100
TOC_HEADING = re.compile(r"^#{2,4}\s+(contents|table of contents)\s*$", re.I)
TOC_WINDOW = 50


def check_tocs(report: Report, plugin_dir: Path) -> None:
    for md in sorted(plugin_dir.rglob("*.md")):
        if md.name == "SKILL.md":
            continue
        lines = md.read_text(encoding="utf-8").splitlines()
        if len(lines) > TOC_THRESHOLD and not any(
            TOC_HEADING.match(line) for line in lines[:TOC_WINDOW]
        ):
            report.error(
                md,
                f"over {TOC_THRESHOLD} lines without a '## Contents' heading "
                f"in its first {TOC_WINDOW} lines",
            )


INDEX_ENTRY = re.compile(r"`([^`\s*]+\.(?:md|pdf|docx))`")


def check_references_index(report: Report, plugin_dir: Path) -> None:
    index = plugin_dir / "references/README.md"
    if not index.is_file():
        return
    for rel in INDEX_ENTRY.findall(index.read_text(encoding="utf-8")):
        target = (index.parent / rel).resolve()
        if not target.is_file() or plugin_dir.resolve() not in target.parents:
            report.error(index, f"lists {rel}, which does not resolve inside the plugin")


UPSTREAM_HEADING = re.compile(r"^##\s+`?([a-z0-9-]+)`?\s*$", re.M)


def check_upstream(report: Report, skills: list) -> None:
    path = report.root / "UPSTREAM.md"
    if not path.is_file():
        report.error(path, "missing")
        return
    entries = set(UPSTREAM_HEADING.findall(path.read_text(encoding="utf-8")))
    for skill_dir in skills:
        if skill_dir.name not in entries:
            report.error(path, f"no '## {skill_dir.name}' entry for skill {skill_dir.name}")


LICENSE_MARKER = "Attribution-ShareAlike 4.0"
NOTICE_ATTRIBUTIONS = (
    "anthropics/k12-teacher-skills",
    "GarethManning/education-agent-skills",
    "mattpocock/skills",
)


def check_licensing(report: Report, base: Path) -> None:
    license_path, notice_path = base / "LICENSE", base / "NOTICE"
    if not license_path.is_file():
        report.error(license_path, "missing")
    elif LICENSE_MARKER not in license_path.read_text(encoding="utf-8"):
        report.error(license_path, "must be the CC BY-SA 4.0 license text")
    if not notice_path.is_file():
        report.error(notice_path, "missing")
        return
    notice = notice_path.read_text(encoding="utf-8")
    for source in NOTICE_ATTRIBUTIONS:
        if source not in notice:
            report.error(notice_path, f"must attribute {source}")


REPO_ONLY_DIRS = {"archive", "sources", "evals", "check-upstream"}
REPO_ONLY_SUFFIXES = {".pdf", ".docx"}
REPO_ONLY_FILES = {"CLAUDE.md"}


def check_repo_only(report: Report, plugin_dir: Path) -> None:
    for path in sorted(plugin_dir.rglob("*")):
        rel = path.relative_to(plugin_dir)
        if (
            (path.is_dir() and path.name in REPO_ONLY_DIRS)
            or (path.is_file() and path.suffix.lower() in REPO_ONLY_SUFFIXES)
            or (path.is_file() and path.name in REPO_ONLY_FILES)
        ):
            if not any(parent.name in REPO_ONLY_DIRS for parent in rel.parents if parent.name):
                report.error(path, "repo-only material must not ship inside the plugin")


def skill_dirs(plugin_dir: Path) -> list:
    skills = plugin_dir / "skills"
    return sorted(p for p in skills.iterdir() if p.is_dir()) if skills.is_dir() else []


def repo_only_skill_dirs(root: Path) -> list:
    """Maintainer skills in .claude/skills (e.g. check-upstream): checked, never shipped."""
    return skill_dirs(root / ".claude")


def validate(repo_root) -> list:
    report = Report(Path(repo_root).resolve())
    check_licensing(report, report.root)
    all_skills = []
    for entry_name, plugin_dir in check_marketplace(report):
        check_manifest(report, entry_name, plugin_dir)
        check_licensing(report, plugin_dir)
        for name in ("LICENSE", "NOTICE"):
            copy, original = plugin_dir / name, report.root / name
            if copy.is_file() and original.is_file() and copy.read_bytes() != original.read_bytes():
                report.error(copy, f"differs from the repo-root {name}; copy it again")
        check_repo_only(report, plugin_dir)
        check_tocs(report, plugin_dir)
        check_references_index(report, plugin_dir)
        for skill_dir in skill_dirs(plugin_dir):
            check_skill(report, skill_dir)
            check_skill_paths(report, plugin_dir, skill_dir)
            all_skills.append(skill_dir)
    for skill_dir in repo_only_skill_dirs(report.root):
        check_skill(report, skill_dir)
        all_skills.append(skill_dir)
    check_upstream(report, all_skills)
    return report.errors


def main(argv) -> int:
    root = Path(argv[1]) if len(argv) > 1 else Path(__file__).resolve().parents[1]
    errors = validate(root)
    for error in errors:
        print(f"ERROR {error}")
    print("OK" if not errors else f"{len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

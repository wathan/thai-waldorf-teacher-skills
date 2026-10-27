#!/usr/bin/env python3
"""Report which skills have upstream changes worth reviewing (repo-only, issue #17).

Usage (from the repo root):
  uv run --no-project python .claude/skills/check-upstream/scripts/check_upstream.py \
      [--record UPSTREAM.md] [--state RECORDED-STATE.json]

Reads the upstream record (UPSTREAM.md: an "Upstream repositories" table of
key -> owner/repo, then one table per skill of repo key, path and commit last
reviewed) and compares each recorded commit with the current upstream state:

- With --state, a recorded upstream state (JSON, used by tests and evals):
    {"recorded_at": "...",
     "repos": {"owner/repo": {"branch": "main",
                              "commits": [{"sha": "...", "files": ["path", ...]}, ...]}}}
  `commits` is the branch history, newest first.
- Without --state, live GitHub through `gh api .../compare/<commit>...<branch>`.

Prints a Markdown report and never writes any file: merging stays manual
(ADR-0001). Exit status: 0 all up to date, 1 changes or commits that could not
be compared, 2 invalid record or state. Standard library only.
"""

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

SHA = re.compile(r"^[0-9a-f]{7,40}$")
NOT_SKILLS = {"contents", "format", "upstream repositories", "pending confirmation"}
LIVE_FILE_CAP = 300  # GitHub's compare API lists at most 300 files


class CheckError(ValueError):
    pass


@dataclass(frozen=True)
class Row:
    skill: str
    key: str
    repo: str
    path: str
    commit: str


@dataclass
class Record:
    repos: dict = field(default_factory=dict)  # key -> owner/repo
    rows: list = field(default_factory=list)
    no_sources: list = field(default_factory=list)


def _cells(line: str) -> list:
    return [c.strip().strip("`") for c in line.strip().strip("|").split("|")]


def parse_record(text: str) -> Record:
    """Parse UPSTREAM.md into repo keys, source rows and skills without sources."""
    record = Record()
    sections, title = [], None
    for line in text.splitlines():
        match = re.match(r"^##\s+(.+?)\s*$", line)
        if match:
            title = match.group(1).strip("`")
            sections.append((title, []))
        elif title is not None:
            sections[-1][1].append(line)
    pending = []
    for title, lines in sections:
        table = [_cells(l) for l in lines if l.strip().startswith("|")]
        header = [h.lower() for h in table[0]] if table else []
        body = [r for r in table[1:] if not all(set(c) <= set("-: ") for c in r)]
        if title.lower() == "upstream repositories":
            for r in body:
                record.repos[r[header.index("key")]] = r[header.index("repo")]
            continue
        if title.lower() in NOT_SKILLS:
            continue
        skill = "plugin-wide" if title.lower() == "plugin-wide" else title
        if not header or header[:3] != ["repo", "path", "commit last reviewed"]:
            record.no_sources.append(skill)
            continue
        if not body:
            record.no_sources.append(skill)
        for r in body:
            pending.append((skill, r[0], r[1], r[2]))
    for skill, key, path, commit in pending:
        if key not in record.repos:
            raise CheckError(f"{skill}: repo key {key!r} is not in the Upstream repositories table")
        if not SHA.match(commit):
            raise CheckError(f"{skill}: {key} {path}: {commit!r} is not a commit SHA")
        record.rows.append(Row(skill, key, record.repos[key], path.rstrip("/"), commit))
    return record


@dataclass
class Comparison:
    head: str = ""
    files: list = None  # files changed since the commit; None when it cannot be compared
    problem: str = ""
    truncated: bool = False


class RecordedUpstream:
    """Upstream as recorded in a JSON file: per repo, the branch history newest first."""

    def __init__(self, path: Path):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            self.repos = data["repos"]
        except (OSError, ValueError, KeyError, TypeError) as exc:
            raise CheckError(f"{path}: not a recorded upstream state ({exc})")
        self.label = f"recorded upstream state `{path.name}`" + (
            f", recorded {data['recorded_at']}" if data.get("recorded_at") else ""
        )

    def compare(self, repo: str, commit: str) -> Comparison:
        history = (self.repos.get(repo) or {}).get("commits")
        if not history:
            return Comparison(problem=f"{repo} is not in the recorded state")
        head = history[0]["sha"]
        for i, entry in enumerate(history):
            if entry["sha"].startswith(commit) or commit.startswith(entry["sha"]):
                files = []
                for newer in reversed(history[:i]):
                    files += [f for f in newer.get("files", []) if f not in files]
                return Comparison(head=head, files=files)
        return Comparison(head=head, problem="recorded commit is not in the upstream history")


class LiveUpstream:
    """Upstream on GitHub, read through the gh CLI (read-only API calls)."""

    label = "live GitHub"

    def __init__(self, gh: str = "gh"):
        self.gh = gh
        self.branches = {}

    def _api(self, endpoint: str):
        proc = subprocess.run([self.gh, "api", endpoint], capture_output=True, text=True)
        if proc.returncode != 0:
            raise CheckError(proc.stderr.strip() or f"gh api {endpoint} failed")
        return json.loads(proc.stdout)

    def compare(self, repo: str, commit: str) -> Comparison:
        if repo not in self.branches:
            try:
                self.branches[repo] = self._api(f"repos/{repo}")["default_branch"]
            except CheckError as exc:
                self.branches[repo] = CheckError(f"cannot read {repo}: {exc}")
        if isinstance(self.branches[repo], CheckError):
            return Comparison(problem=f"GitHub: {self.branches[repo]}")
        try:
            data =self._api(f"repos/{repo}/compare/{commit}...{self.branches[repo]}")
        except CheckError as exc:
            return Comparison(problem=f"GitHub: {exc}")
        commits = data.get("commits") or []
        head = commits[-1]["sha"] if commits else commit
        if data.get("status") not in ("ahead", "identical"):
            return Comparison(head=head, problem=f"recorded commit is {data.get('status')} the branch")
        files = [f["filename"] for f in data.get("files") or []]
        return Comparison(head=head, files=files, truncated=len(files) >= LIVE_FILE_CAP)


def under(path: str, filename: str) -> bool:
    return filename == path or filename.startswith(path + "/")


def check(record: Record, upstream) -> tuple:
    """Return (report markdown, exit code). Reads only; writes nothing."""
    cache, heads = {}, {}
    changed, current, problems = {}, {}, {}
    for row in record.rows:
        key = (row.repo, row.commit)
        if key not in cache:
            cache[key] = upstream.compare(row.repo, row.commit)
        result = cache[key]
        if result.head:
            heads[row.repo] = result.head
        if result.files is None:
            problems.setdefault(row.skill, []).append((row, result))
            continue
        files = [f for f in result.files if under(row.path, f)]
        if files or (result.truncated and not files):
            changed.setdefault(row.skill, []).append((row, result, files))
        else:
            current.setdefault(row.skill, []).append(row)

    short = lambda sha: sha[:7]  # noqa: E731
    out = ["# Upstream check", "", f"Compared against: {upstream.label}.", ""]
    if heads:
        out += ["Upstream heads: " + ", ".join(
            f"{repo} `{short(sha)}`" for repo, sha in sorted(heads.items())), ""]
    if changed:
        out += ["## Changes worth reviewing", ""]
        for skill, items in changed.items():
            out += [f"### {skill}", ""]
            for row, result, files in items:
                out.append(f"- {row.key} `{row.path}`: reviewed `{short(row.commit)}`, "
                           f"upstream now `{short(result.head)}`. Changed files:")
                out += [f"  - `{f}`" for f in files]
                if result.truncated:
                    out.append("  - (GitHub listed only the first 300 changed files; "
                               "open the compare view for the rest)")
            out.append("")
    if problems:
        out += ["## Could not compare", ""]
        for skill, items in problems.items():
            for row, result in items:
                out.append(f"- {skill}: {row.key} `{row.path}` at `{short(row.commit)}`: "
                           f"{result.problem}")
        out.append("")
    if current:
        out += ["## Up to date", ""]
        for skill, rows in current.items():
            paths = "; ".join(f"{r.key} `{r.path}` (`{short(r.commit)}`)" for r in rows)
            out.append(f"- {skill}: {paths}")
        out.append("")
    if record.no_sources:
        out += ["## No upstream sources", "", "- " + ", ".join(record.no_sources), ""]
    out.append("Nothing was changed. Merge by hand, then update the commit in UPSTREAM.md "
               "for each path you reviewed.")
    return "\n".join(out) + "\n", 1 if (changed or problems) else 0


def main(argv, out=sys.stdout) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--record", default="UPSTREAM.md", help="upstream record (UPSTREAM.md)")
    parser.add_argument("--state", help="recorded upstream state JSON; omit for live GitHub")
    parser.add_argument("--gh", default="gh", help="gh executable (live mode)")
    args = parser.parse_args(argv)
    try:
        record = parse_record(Path(args.record).read_text(encoding="utf-8"))
        upstream = RecordedUpstream(Path(args.state)) if args.state else LiveUpstream(args.gh)
        report, code = check(record, upstream)
    except (OSError, CheckError) as exc:
        print(f"ERROR {exc}", file=out)
        return 2
    out.write(report)
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

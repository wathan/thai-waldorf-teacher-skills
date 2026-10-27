"""Where the shipped plugin lives, read from .claude-plugin/marketplace.json.

The one place the repo scripts (run_evals.py, build_crosswalk.py) learn the
plugin folder, so moving the plugin means editing only the marketplace entry.
Standard library only.
"""

import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PLUGIN_NAME = "thai-waldorf-science"


def plugin_dir(repo: Path = REPO, name: str = PLUGIN_NAME) -> Path:
    """The folder of plugin `name`, from its marketplace entry's ./source."""
    market = json.loads((repo / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
    for entry in market.get("plugins", []):
        if entry.get("name") == name:
            return repo / entry["source"].removeprefix("./")
    raise LookupError(f"plugin {name!r} is not listed in {repo}/.claude-plugin/marketplace.json")

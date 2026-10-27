"""The scripts find the plugin through the marketplace, not a copied path."""

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from plugin_paths import plugin_dir  # noqa: E402


class PluginDirTest(unittest.TestCase):
    def test_plugin_folder_comes_from_the_marketplace_entry(self):
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp)
        (tmp / ".claude-plugin").mkdir()
        (tmp / ".claude-plugin/marketplace.json").write_text(json.dumps({
            "name": "m", "owner": {"name": "o"},
            "plugins": [{"name": "thai-waldorf-science", "source": "./elsewhere/tws"}]}))
        self.assertEqual(plugin_dir(tmp), tmp / "elsewhere/tws")

    def test_this_repo_plugin_folder(self):
        self.assertEqual(plugin_dir(), ROOT / "plugins/thai-waldorf-science")


if __name__ == "__main__":
    unittest.main()

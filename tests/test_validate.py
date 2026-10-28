"""Behaviour tests for the plugin structure validator (spec #1, seam 2).

Each test builds a small repo in a temp dir, breaks one rule, and checks that
`validate(repo_root)` reports it. Run: python3 -m unittest discover tests
"""

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate import validate  # noqa: E402

PLUGIN = "plugins/demo-plugin"

SKILL_MD = """---
name: doing-things
description: Does things for teachers. Use when the teacher asks to do things.
license: CC-BY-SA-4.0
---

# Doing things

Read ${CLAUDE_PLUGIN_ROOT}/references/README.md first.
"""

UPSTREAM_MD = """# Upstream record

## doing-things

| Repo | Path | Commit last reviewed | Status |
|---|---|---|---|
| — | — | — | none |
"""

LICENSE_TXT = "Attribution-ShareAlike 4.0 International\n"
NOTICE_TXT = (
    "Derived from anthropics/k12-teacher-skills, "
    "GarethManning/education-agent-skills and mattpocock/skills.\n"
)


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def make_valid_repo(root: Path) -> None:
    write(
        root / ".claude-plugin/marketplace.json",
        json.dumps(
            {
                "name": "demo-market",
                "description": "Demo",
                "owner": {"name": "someone"},
                "plugins": [
                    {"name": "demo-plugin", "source": "./" + PLUGIN, "description": "Demo"}
                ],
            }
        ),
    )
    plugin = root / PLUGIN
    write(
        plugin / ".claude-plugin/plugin.json",
        json.dumps(
            {
                "name": "demo-plugin",
                "version": "0.1.0",
                "description": "Demo",
                "author": {"name": "someone"},
                "license": "CC-BY-SA-4.0",
            }
        ),
    )
    write(plugin / "skills/doing-things/SKILL.md", SKILL_MD)
    write(plugin / "references/README.md", "# Index\n\n| `notes.md` | x |\n")
    write(plugin / "references/notes.md", "# Notes\n")
    for base in (root, plugin):
        write(base / "LICENSE", LICENSE_TXT)
        write(base / "NOTICE", NOTICE_TXT)
    write(root / "UPSTREAM.md", UPSTREAM_MD)


class ValidatorTest(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp())
        make_valid_repo(self.root)
        self.plugin = self.root / PLUGIN

    def tearDown(self):
        shutil.rmtree(self.root)

    def assertReports(self, fragment: str):
        errors = validate(self.root)
        self.assertTrue(
            any(fragment in e for e in errors),
            f"expected an error containing {fragment!r}, got {errors}",
        )

    def test_valid_repo_has_no_errors(self):
        self.assertEqual(validate(self.root), [])

    def test_missing_marketplace_is_reported(self):
        (self.root / ".claude-plugin/marketplace.json").unlink()
        self.assertReports("marketplace.json")

    def edit_json(self, path: Path, change) -> None:
        data = json.loads(path.read_text())
        change(data)
        path.write_text(json.dumps(data))

    def test_marketplace_source_must_exist(self):
        self.edit_json(
            self.root / ".claude-plugin/marketplace.json",
            lambda d: d["plugins"][0].update(source="./plugins/missing"),
        )
        self.assertReports("plugins/missing")

    def test_marketplace_source_must_be_relative_dot_slash(self):
        self.edit_json(
            self.root / ".claude-plugin/marketplace.json",
            lambda d: d["plugins"][0].update(source=PLUGIN),
        )
        self.assertReports("must start with ./")

    def test_marketplace_entry_name_must_match_manifest(self):
        self.edit_json(
            self.root / ".claude-plugin/marketplace.json",
            lambda d: d["plugins"][0].update(name="other-name"),
        )
        self.assertReports("does not match")

    def test_manifest_needs_author_version_description_license(self):
        for key in ("author", "version", "description", "license"):
            make_valid_repo(self.root)
            self.edit_json(
                self.plugin / ".claude-plugin/plugin.json", lambda d: d.pop(key)
            )
            self.assertReports(f"'{key}'")

    def test_manifest_name_must_be_kebab_case(self):
        self.edit_json(
            self.plugin / ".claude-plugin/plugin.json",
            lambda d: d.update(name="Demo_Plugin"),
        )
        self.assertReports("kebab-case")

    # --- SKILL.md -------------------------------------------------------

    @property
    def skill_md(self) -> Path:
        return self.plugin / "skills/doing-things/SKILL.md"

    def set_frontmatter(self, frontmatter: str, body: str = "# Body\n") -> None:
        write(self.skill_md, f"---\n{frontmatter.strip()}\n---\n\n{body}")

    def test_skill_dir_without_skill_md_is_reported(self):
        write(self.plugin / "skills/empty-skill/notes.md", "x\n")
        self.assertReports("empty-skill/SKILL.md: missing")

    def test_skill_without_frontmatter_is_reported(self):
        write(self.skill_md, "# No frontmatter\n")
        self.assertReports("frontmatter")

    def test_folded_multiline_description_is_accepted(self):
        self.set_frontmatter(
            "name: doing-things\n"
            "description: >\n"
            "  Does things for teachers.\n"
            "  Use when the teacher asks to do things.\n"
            "license: CC-BY-SA-4.0\n"
        )
        self.assertEqual(validate(self.root), [])

    def test_skill_name_must_match_directory(self):
        self.set_frontmatter("name: doing-other-things\ndescription: Does things. Use when asked.")
        self.assertReports("directory")

    def test_skill_name_rules(self):
        for bad in ("Doing_Things", "claude-helper", "x" * 65):
            self.set_frontmatter(f"name: {bad}\ndescription: Does things. Use when asked.")
            self.assertReports("name")

    def test_description_required(self):
        self.set_frontmatter("name: doing-things")
        self.assertReports("description")

    def test_description_length_limit(self):
        self.set_frontmatter("name: doing-things\ndescription: " + "Does things. " * 100)
        self.assertReports("1024")

    def test_description_rejects_angle_brackets(self):
        self.set_frontmatter("name: doing-things\ndescription: Does <things>. Use when asked.")
        self.assertReports("angle brackets")

    def test_description_must_be_third_person(self):
        for bad in ("I help teachers plan.", "You can use this to plan."):
            self.set_frontmatter(f"name: doing-things\ndescription: {bad} Use when asked.")
            self.assertReports("third person")

    def test_description_must_say_when(self):
        self.set_frontmatter("name: doing-things\ndescription: Does things for teachers.")
        self.assertReports("Use when")

    def test_unknown_frontmatter_key_is_reported(self):
        self.set_frontmatter(
            "name: doing-things\ndescription: Does things. Use when asked.\nskill_id: x/y"
        )
        self.assertReports("skill_id")

    def test_skill_md_line_limit(self):
        self.set_frontmatter(
            "name: doing-things\ndescription: Does things. Use when asked.",
            body="line\n" * 500,
        )
        self.assertReports("500")

    # --- references -----------------------------------------------------

    def test_long_reference_without_contents_is_reported(self):
        write(self.plugin / "references/long.md", "# Long\n\n" + "text\n" * 120)
        self.assertReports("references/long.md: over 100 lines")

    def test_long_skill_reference_without_contents_is_reported(self):
        write(self.plugin / "skills/doing-things/references/long.md", "# Long\n" + "x\n" * 120)
        self.assertReports("doing-things/references/long.md")

    def test_long_reference_with_contents_is_accepted(self):
        write(
            self.plugin / "references/long.md",
            "# Long\n\n## Contents\n\n- [Part](#part)\n\n## Part\n" + "text\n" * 120,
        )
        self.assertEqual(validate(self.root), [])

    def test_references_index_entry_must_resolve(self):
        write(self.plugin / "references/README.md", "| `notes.md` | x |\n| `gone.md` | y |\n")
        self.assertReports("gone.md")

    def test_plugin_root_path_in_skill_must_resolve(self):
        self.set_frontmatter(
            "name: doing-things\ndescription: Does things. Use when asked.",
            body="Read ${CLAUDE_PLUGIN_ROOT}/references/absent.md\n",
        )
        self.assertReports("absent.md")

    def test_skill_dir_path_in_skill_must_resolve(self):
        self.set_frontmatter(
            "name: doing-things\ndescription: Does things. Use when asked.",
            body="Read ${CLAUDE_SKILL_DIR}/references/local.md\n",
        )
        self.assertReports("local.md")
        write(self.plugin / "skills/doing-things/references/local.md", "# Local\n")
        self.assertEqual(validate(self.root), [])

    def test_skill_with_a_bundled_script_is_accepted(self):
        self.set_frontmatter(
            "name: doing-things\ndescription: Does things. Use when asked.",
            body='Run `python3 "${CLAUDE_SKILL_DIR}/scripts/do_it.py"`\n',
        )
        self.assertReports("scripts/do_it.py")
        write(self.plugin / "skills/doing-things/scripts/do_it.py", "print('done')\n")
        self.assertEqual(validate(self.root), [])

    # --- upstream record ------------------------------------------------

    def test_skill_without_upstream_entry_is_reported(self):
        write(self.root / "UPSTREAM.md", "# Upstream record\n")
        self.assertReports("doing-things")

    def test_missing_upstream_record_is_reported(self):
        (self.root / "UPSTREAM.md").unlink()
        self.assertReports("UPSTREAM.md")

    # --- licensing ------------------------------------------------------

    def test_license_and_notice_required_at_repo_and_plugin_root(self):
        for base in (self.root, self.plugin):
            for name in ("LICENSE", "NOTICE"):
                make_valid_repo(self.root)
                (base / name).unlink()
                self.assertReports(name)

    def test_license_must_be_cc_by_sa(self):
        write(self.plugin / "LICENSE", "MIT License\n")
        self.assertReports("CC BY-SA 4.0")

    def test_notice_must_attribute_each_upstream(self):
        write(self.root / "NOTICE", "Derived from anthropics/k12-teacher-skills.\n")
        self.assertReports("GarethManning/education-agent-skills")

    def test_plugin_notice_must_match_repo_notice(self):
        write(self.plugin / "NOTICE", NOTICE_TXT + "Extra line.\n")
        self.assertReports("differs from")

    # --- repo-only material ---------------------------------------------

    def test_repo_only_material_inside_plugin_is_reported(self):
        for rel in (
            "references/sources/original.pdf",
            "references/form.docx",
            "archive/old.md",
            "evals/doing-things/evals.json",
            "skills/check-upstream/SKILL.md",
            "CLAUDE.md",
        ):
            make_valid_repo(self.root)
            for leftover in ("references/sources", "archive", "evals", "skills/check-upstream"):
                shutil.rmtree(self.plugin / leftover, ignore_errors=True)
            for leftover in ("references/form.docx", "CLAUDE.md"):
                (self.plugin / leftover).unlink(missing_ok=True)
            write(self.plugin / rel, "x\n")
            self.assertReports("repo-only")

    # --- repo-only skills (.claude/skills, never shipped) ---------------

    def write_repo_only_skill(self, frontmatter_name="checking-stuff"):
        write(
            self.root / ".claude/skills/checking-stuff/SKILL.md",
            SKILL_MD.replace("doing-things", frontmatter_name).replace(
                "Read ${CLAUDE_PLUGIN_ROOT}/references/README.md first.", "Run the check."
            ),
        )

    def test_repo_only_skill_is_validated_like_a_plugin_skill(self):
        self.write_repo_only_skill(frontmatter_name="other-name")
        write(self.root / "UPSTREAM.md", UPSTREAM_MD + "\n## checking-stuff\n\nNone.\n")
        self.assertReports("does not match directory")

    def test_repo_only_skill_needs_an_upstream_entry(self):
        self.write_repo_only_skill()
        self.assertReports("no '## checking-stuff' entry")
        write(self.root / "UPSTREAM.md", UPSTREAM_MD + "\n## checking-stuff\n\nNone.\n")
        self.assertEqual(validate(self.root), [])

    # --- the real repo --------------------------------------------------

    def test_this_repo_passes(self):
        self.assertEqual(validate(ROOT), [])


if __name__ == "__main__":
    unittest.main()

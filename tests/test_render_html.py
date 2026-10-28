"""Behaviour tests for the HTML renderer shipped with exporting-documents (spec #18, issue #20).

Each test writes a markdown document to a temp course folder, renders it through
`render(source)`, and checks the HTML copy written beside it and the report.
"""

import io
import json
import os
import sys
import tempfile
import time
import unittest
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.dont_write_bytecode = True  # keep __pycache__ out of the shipped plugin
sys.path.insert(0, str(ROOT / "plugins/thai-waldorf-science/skills/exporting-documents/scripts"))

from render_html import main, render  # noqa: E402


class RenderTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def doc(self, text, name="session-1-prep.md"):
        path = self.dir / name
        path.write_text(text, encoding="utf-8")
        return path

    def html(self, text):
        result = render(self.doc(text))
        return result, result.out.read_text(encoding="utf-8")

    def test_copy_beside_source_is_a_thai_a4_page(self):
        result, html = self.html("# บันทึกเตรียมสอน: คาบที่ 1\n\nย่อหน้าแรก\n")
        self.assertEqual(result.out, self.dir / "session-1-prep.html")
        self.assertIn('<html lang="th">', html)
        self.assertIn("size: A4", html)
        self.assertIn("Sarabun", html)
        self.assertIn("<title>บันทึกเตรียมสอน: คาบที่ 1</title>", html)
        self.assertIn("<h1>บันทึกเตรียมสอน: คาบที่ 1</h1>", html)
        self.assertIn("<p>ย่อหน้าแรก</p>", html)

    def test_lists_and_checkboxes(self):
        _, html = self.html(
            "- ติด: เลือกสัตว์หนึ่งตัว\n- เสร็จเร็ว: ฤดูร้อน\n\n"
            "1. วัดอะไรได้บ้าง\n2. วัดด้วยเครื่องมืออะไร\n\n"
            "- [ ] ขวดรูปชมพู่\n- [x] ซ้อมอุ่นน้ำ\n"
        )
        self.assertIn("<ul>\n<li>ติด: เลือกสัตว์หนึ่งตัว</li>\n<li>เสร็จเร็ว: ฤดูร้อน</li>\n</ul>", html)
        self.assertIn("<ol>\n<li>วัดอะไรได้บ้าง</li>\n<li>วัดด้วยเครื่องมืออะไร</li>\n</ol>", html)
        self.assertIn('<ul class="tasks">\n<li>☐ ขวดรูปชมพู่</li>\n<li>☑ ซ้อมอุ่นน้ำ</li>\n</ul>', html)

    def test_table_repeats_its_header_row_on_every_printed_page(self):
        result, html = self.html(
            "| เวลา | ช่วง |\n|---|:---:|\n"
            "| 13:00–13:10 | นำเข้า |\n| 13:10 | 1. อ่าน<br>2. เขียน |\n"
        )
        self.assertIn(
            "<table>\n<thead><tr><th>เวลา</th><th>ช่วง</th></tr></thead>\n<tbody>\n"
            "<tr><td>13:00–13:10</td><td>นำเข้า</td></tr>\n"
            "<tr><td>13:10</td><td>1. อ่าน<br>2. เขียน</td></tr>\n"
            "</tbody>\n</table>",
            html,
        )
        self.assertIn("thead { display: table-header-group; }", html)
        self.assertEqual(result.unsupported, [])

    def test_bold_and_italic(self):
        _, html = self.html(
            "**ซ้อมก่อน:** คำถามเปิด _ไม่บอก_ และ *ดูเวลา*\n\n"
            "| สัญญาณ |\n|---|\n| **หยุดตรง 14:50** |\n"
        )
        self.assertIn("<p><strong>ซ้อมก่อน:</strong> คำถามเปิด <em>ไม่บอก</em> และ <em>ดูเวลา</em></p>", html)
        self.assertIn("<td><strong>หยุดตรง 14:50</strong></td>", html)

    def test_markdown_outside_the_subset_is_kept_as_plain_text_and_reported(self):
        result, html = self.html(
            "> คำพูดอ้างอิง\n\n"
            "ดู [แผนรายวัน](days/week-2-day-6.md) และ `ค่า`\n\n"
            "---\n\n"
            "```\nโค้ด <b>\n```\n\n"
            "- ข้อแรก\n  - ข้อย่อย\n\n"
            "![ภาพ](board.jpg)\n"
        )
        self.assertEqual(
            result.unsupported,
            ["blockquote", "code block", "horizontal rule", "image", "inline code", "link", "nested list"],
        )
        self.assertIn("&gt; คำพูดอ้างอิง", html)
        self.assertIn("[แผนรายวัน](days/week-2-day-6.md)", html)
        self.assertIn("`ค่า`", html)
        self.assertIn("โค้ด &lt;b&gt;", html)
        self.assertIn("<li>ข้อย่อย</li>", html)
        self.assertNotIn("<a ", html)
        self.assertNotIn("<img", html)

    def test_re_export_overwrites_an_older_copy(self):
        source = self.doc("# เดิม\n")
        render(source)
        old = time.time() - 60
        os.utime(source.with_suffix(".html"), (old, old))
        source.write_text("# ใหม่\n", encoding="utf-8")
        result = render(source)
        self.assertTrue(result.written)
        self.assertFalse(result.edited_copy)
        self.assertIn("<h1>ใหม่</h1>", result.out.read_text(encoding="utf-8"))

    def test_re_export_of_an_untouched_copy_needs_no_warning(self):
        source = self.doc("# แผน\n")
        render(source)
        old = time.time() - 60
        os.utime(source, (old, old))
        result = render(source)
        self.assertTrue(result.written)
        self.assertFalse(result.edited_copy)

    def test_copy_edited_since_export_is_reported_and_kept_unless_forced(self):
        source = self.doc("# แผน\n")
        copy = source.with_suffix(".html")
        copy.write_text("edited in the browser", encoding="utf-8")
        old = time.time() - 60
        os.utime(source, (old, old))
        result = render(source)
        self.assertTrue(result.edited_copy)
        self.assertFalse(result.written)
        self.assertEqual(copy.read_text(encoding="utf-8"), "edited in the browser")
        forced = render(source, force=True)
        self.assertTrue(forced.written)
        self.assertIn("<h1>แผน</h1>", copy.read_text(encoding="utf-8"))
        self.assertEqual(source.read_text(encoding="utf-8"), "# แผน\n")

    def test_title_is_plain_text(self):
        _, html = self.html("# **คาบที่ 1**\n")
        self.assertIn("<title>คาบที่ 1</title>", html)


    def cli(self, *args):
        out = io.StringIO()
        with redirect_stdout(out):
            code = main([str(a) for a in args])
        return code, json.loads(out.getvalue())

    def test_cli_reports_the_copy_as_json(self):
        code, report = self.cli(self.doc("> อ้างอิง\n"))
        self.assertEqual(code, 0)
        self.assertEqual(report["out"], str(self.dir / "session-1-prep.html"))
        self.assertTrue(report["written"])
        self.assertEqual(report["unsupported"], ["blockquote"])

    def test_cli_keeps_an_edited_copy_unless_forced(self):
        source = self.doc("# แผน\n")
        source.with_suffix(".html").write_text("edited", encoding="utf-8")
        code, report = self.cli(source)
        self.assertEqual(code, 3)
        self.assertTrue(report["edited_copy"])
        self.assertFalse(report["written"])
        code, report = self.cli(source, "--force")
        self.assertEqual(code, 0)
        self.assertTrue(report["written"])

    def test_cli_rejects_a_missing_or_non_markdown_source(self):
        self.assertEqual(self.cli(self.dir / "missing.md")[0], 1)
        self.assertEqual(self.cli(self.doc("x", name="plan.txt"))[0], 1)

if __name__ == "__main__":
    unittest.main()

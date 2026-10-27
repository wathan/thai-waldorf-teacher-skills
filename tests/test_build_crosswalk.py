"""Behaviour tests for the curriculum crosswalk generator (spec #1, issue #3).

Each test writes a small reference corpus in the real files' formats to a
temp dir and checks what `build_crosswalk(references_dir)` produces. The last
tests check the committed crosswalk against the real corpus and the CLI.
"""

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_crosswalk import build_crosswalk, main  # noqa: E402

INDICATORS = """# ตัวชี้วัด

## Contents

- สาระที่ 1

## สาระที่ 1 วิทยาศาสตร์ชีวภาพ

### มาตรฐาน ว 1.1

เข้าใจความหลากหลายของระบบนิเวศ

#### ว 1.1 · ม.2

**ตัวชี้วัด**

1. `ว 1.1 ม.2/1` บรรยายสิ่งที่ไม่ควรอยู่ในครอสวอล์ก

#### ว 1.1 · ม.3

**ตัวชี้วัด**

1. `ว 1.1 ม.3/1` อธิบายปฏิสัมพันธ์ขององค์ประกอบของระบบนิเวศที่ได้จากการสำรวจ
2. `ว 1.1 ม.3/3` สร้างแบบจำลองในการอธิบายการถ่ายทอดพลังงานในสายใยอาหาร
3. `ว 1.1 ม.3/6` ตระหนักถึงความสัมพันธ์ของสิ่งมีชีวิต และสิ่งแวดล้อมในระบบนิเวศ

**สาระการเรียนรู้แกนกลาง**

- เนื้อหาที่ไม่ใช่ตัวชี้วัด

## สาระที่ 3 วิทยาศาสตร์โลก และอวกาศ

### มาตรฐาน ว 3.2

เข้าใจองค์ประกอบและความสัมพันธ์ของระบบโลก

#### ว 3.2 · ม.6

**ตัวชี้วัด**

1. `ว 3.2 ม.6/10` อธิบายการหมุนเวียนของอากาศตามเขตละติจูด และผลที่มีต่อภูมิอากาศ
2. `ว 3.2 ม.6/14` แปลความหมายสัญลักษณ์ลมฟ้าอากาศที่สำคัญจากแผนที่อากาศ
3. `ว 3.2 ม.6/15` สืบค้นข้อมูลและนำเสนอ
"""

GLOSSARY = """# อภิธานศัพท์

## ศัพท์ที่เกี่ยวข้องกับตัวชี้วัดกลุ่มสาระการเรียนรู้วิทยาศาสตร์

| ที่ | ภาษาไทย | English | ความหมาย |
|---|---|---|---|
| 1 | แปลความหมาย | interpret | แสดงความหมายของข้อมูลจากหลักฐานที่ปรากฏเพื่อลงข้อสรุป |
| 2 | สร้างแบบจำลอง | construct model | นำเสนอแนวคิด หรือเหตุการณ์ในรูปของแผนภาพ |
| 3 | สำรวจ | explore | หาข้อมูลเกี่ยวกับสิ่งต่าง ๆ |
| 4 | สืบค้นข้อมูล | search | หาข้อมูล หรือข้อสนเทศที่มีผู้รวบรวมไว้แล้ว |
| 5 | อธิบาย | explain | กล่าวถึงเรื่องราวต่าง ๆ อย่างมีเหตุผล |
| 6 | นำเสนอ | present | แสดงข้อมูล เรื่องราว หรือความคิด |

## ศัพท์ที่เกี่ยวข้องกับตัวชี้วัดสาระเทคโนโลยี

| ที่ | ภาษาไทย | English | ความหมาย |
|---|---|---|---|
| 1 | อัลกอริทึม | algorithm | ขั้นตอนในการแก้ปัญหา |
"""

MACRO = """# Waldorf Upper-School Macro-Curriculum

## 2. Grade modes (lookup cards)

### Grade 9: *What?* (ม.3)
- **Question:** What is here? What happened?
- **Capacity:** Observation. Exact, theory-free description.
- **Motif:** Unresolved opposition, e.g. heat/cold.

### Grade 10: *How?* (ม.4)
- **Question:** How does this relate to that?
- **Capacity:** Comparison.
- **Motif:** Polarity and intensification.

### Grade 11: *Why?* (ม.5)
- **Question:** Why are things this way?
- **Capacity:** Analysis.
- **Motif:** The invisible and the individual element.

### Grade 12: *Who?* (ม.6)
- **Question:** Who is this being called human?
- **Capacity:** Synthesis.
- **Motif:** Comprehensive synthesis.

---

## 3. Potentiality-mode matrix
"""

PISA_GRADE = """# Grade {g}

- **Guiding question:** *X?*

## S1 — Explain phenomena scientifically

**การอธิบายปรากฏการณ์ในเชิงวิทยาศาสตร์**

**S1.1 — Recall and apply scientific knowledge** · `Keep`
Recall and apply.
ระลึก

## S2 — Construct and evaluate designs for scientific enquiry and interpret scientific data and evidence critically

**การออกแบบ**

**S2.1 — Identify the question** · `Keep`
Identify.
ระบุ

## S3 — Research, evaluate and use scientific information for decision making and action

**การสืบค้น**

**S3.1 — Search, evaluate and communicate** · `Keep`
Search.
สืบค้น

## E1 — Explain the impact of human interactions with Earth's systems

**ผลกระทบ**

**E1.1 — Explain systems** · `Keep`
Explain.
อธิบาย

## E2 — Make informed decisions to act

**การตัดสินใจ**

**E2.1 — Evidence** · `Keep`
Evidence.
หลักฐาน

## E3 — Demonstrate respect for diverse perspectives, and hope

**ความเคารพ**

**E3.1 — Ecocentric ethic** · `Shift`
Care.
ใส่ใจ

"""

PISA = (
    "# Waldorf-aligned PISA 2025 Science Competencies\n\n"
    + "".join(PISA_GRADE.format(g=g) for g in (9, 10, 11, 12))
    + "# Lineage table (G9 → G12)\n\n**S9.9 — Not a statement** · `Keep`\n"
)

FILES = {
    "thai-science-core-indicators-2560.md": INDICATORS,
    "thai-science-glossary-2560.md": GLOSSARY,
    "waldorf-upper-school-macro-curriculum.md": MACRO,
    "waldorf-pisa-competencies-g9-g12.md": PISA,
}


def make_corpus(root: Path, **overrides) -> Path:
    for name, text in FILES.items():
        (root / name).write_text(overrides.get(name, text), encoding="utf-8")
    return root


def section(text: str, heading_start: str) -> str:
    """The body of the first `## ` section whose heading starts with heading_start."""
    lines = text.split("\n")
    start = next(i for i, l in enumerate(lines) if l.startswith("## " + heading_start))
    end = next(
        (i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines)
    )
    return "\n".join(lines[start:end])


def row(text: str, first_cell: str) -> str:
    return next(l for l in text.split("\n") if l.startswith(f"| {first_cell} |"))


class CorpusTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp)

    def build(self, **overrides) -> str:
        return build_crosswalk(make_corpus(self.tmp, **overrides))


class ThaiIndicatorsTest(CorpusTest):
    def test_upper_school_indicators_appear_with_code_and_verbatim_wording(self):
        out = self.build()
        self.assertIn("`ว 1.1 ม.3/1`", out)
        self.assertIn("อธิบายปฏิสัมพันธ์ขององค์ประกอบของระบบนิเวศที่ได้จากการสำรวจ", out)
        self.assertIn("`ว 3.2 ม.6/10`", out)
        self.assertIn("อธิบายการหมุนเวียนของอากาศตามเขตละติจูด และผลที่มีต่อภูมิอากาศ", out)

    def test_lower_grade_indicators_and_core_content_are_left_out(self):
        out = self.build()
        self.assertNotIn("ม.2/1", out)
        self.assertNotIn("เนื้อหาที่ไม่ใช่ตัวชี้วัด", out)


class WaldorfGradeModesTest(CorpusTest):
    def test_each_thai_grade_is_paired_with_its_waldorf_grade_mode_in_its_own_words(self):
        bands = section(self.build(), "1. Grade bands")
        g9 = row(bands, "ม.3")
        self.assertIn("G9 *What?*", g9)
        self.assertIn("What is here? What happened?", g9)
        self.assertIn("Observation. Exact, theory-free description.", g9)
        self.assertIn("Unresolved opposition, e.g. heat/cold.", g9)
        self.assertIn("G12 *Who?*", row(bands, "ม.6"))

    def test_missing_block_placement_list_is_stated_as_a_gap(self):
        bands = section(self.build(), "1. Grade bands")
        self.assertIn("Gap", bands)
        self.assertIn("block", bands.lower())

    def test_indicators_sit_under_their_grade_with_the_waldorf_grade_named(self):
        out = self.build()
        g9 = section(out, "ม.3 · G9")
        self.assertIn("`ว 1.1 ม.3/1`", g9)
        self.assertNotIn("`ว 3.2 ม.6/10`", g9)
        self.assertIn("`ว 3.2 ม.6/10`", section(out, "ม.6 · G12"))


class GlossaryVerbsTest(CorpusTest):
    def test_each_indicator_lists_the_official_verbs_it_uses_with_their_glossary_gloss(self):
        out = self.build()
        r1 = row(out, "`ว 1.1 ม.3/1`")
        self.assertIn("อธิบาย (explain)", r1)
        self.assertIn("สำรวจ (explore)", r1)
        r15 = row(out, "`ว 3.2 ม.6/15`")
        self.assertIn("สืบค้นข้อมูล (search)", r15)
        self.assertIn("นำเสนอ (present)", r15)

    def test_a_verb_inside_a_longer_official_verb_is_not_listed_again(self):
        glossary = GLOSSARY.replace(
            "| 6 | นำเสนอ |",
            "| 7 | ทดลอง | conduct/experiment | ปฏิบัติการ |\n"
            "| 8 | ออกแบบการทดลอง | design experiment | กำหนด |\n| 6 | นำเสนอ |",
        )
        indicators = INDICATORS.replace(
            "สืบค้นข้อมูลและนำเสนอ", "ออกแบบการทดลองเรื่องลม"
        )
        r = row(
            self.build(**{
                "thai-science-glossary-2560.md": glossary,
                "thai-science-core-indicators-2560.md": indicators,
            }),
            "`ว 3.2 ม.6/15`",
        )
        self.assertIn("ออกแบบการทดลอง (design experiment)", r)
        self.assertNotIn("ทดลอง (conduct/experiment)", r)

    def test_technology_terms_are_not_read_as_indicator_verbs(self):
        indicators = INDICATORS.replace("สืบค้นข้อมูลและนำเสนอ", "เขียนอัลกอริทึม")
        r = row(self.build(**{"thai-science-core-indicators-2560.md": indicators}), "`ว 3.2 ม.6/15`")
        self.assertNotIn("algorithm", r)


class PisaLinksTest(CorpusTest):
    def test_indicator_verbs_and_environment_terms_link_to_pisa_headlines_by_rule(self):
        out = self.build()
        r1 = row(out, "`ว 1.1 ม.3/1`")
        for code in ("S1", "S2", "E1"):
            self.assertIn(code, r1)
        self.assertNotIn("S3", r1)
        r6 = row(out, "`ว 1.1 ม.3/6`")
        self.assertIn("E1", r6)
        self.assertIn("E3", r6)
        r15 = row(out, "`ว 3.2 ม.6/15`")
        self.assertIn("S3", r15)
        self.assertNotIn("S1", r15)

    def test_an_indicator_no_rule_matches_shows_an_explicit_gap(self):
        indicators = INDICATORS.replace("สืบค้นข้อมูลและนำเสนอ", "ใช้เครื่องมืออย่างปลอดภัย")
        out = self.build(**{"thai-science-core-indicators-2560.md": indicators})
        r = row(out, "`ว 3.2 ม.6/15`")
        self.assertIn("Gap: no link rule matches", r)
        self.assertIn("Gap: no glossary verb", r)

    def test_each_grade_lists_its_own_pisa_adapted_sub_abilities_verbatim(self):
        head, g12 = PISA.split("# Grade 12\n")
        pisa = head + "# Grade 12\n" + g12.replace(
            "**E3.1 — Ecocentric ethic** · `Shift`", "**E3.1 — Owned ecocentric position** · `Deepen`"
        )
        out = self.build(**{"waldorf-pisa-competencies-g9-g12.md": pisa})
        self.assertIn("E3.1 — Ecocentric ethic · Shift", section(out, "ม.3 · G9"))
        g12 = section(out, "ม.6 · G12")
        self.assertIn("E3.1 — Owned ecocentric position · Deepen", g12)
        self.assertNotIn("Ecocentric ethic · Shift", g12)
        self.assertNotIn("S9.9", out)

    def test_coverage_matrix_counts_linked_indicators_and_marks_empty_cells_as_gaps(self):
        matrix = section(self.build(), "3. PISA-adapted competencies")
        s1 = row(matrix, "S1")
        self.assertIn("Explain phenomena scientifically", s1)
        self.assertIn("การอธิบายปรากฏการณ์ในเชิงวิทยาศาสตร์", s1)
        cells = [c.strip() for c in s1.strip("|").split("|")]
        self.assertEqual(cells[-4:], ["2", "Gap", "Gap", "1"])  # ม.3/1, ม.3/3; ม.6/10
        e2 = [c.strip() for c in row(matrix, "E2").strip("|").split("|")]
        self.assertEqual(e2[-4:], ["Gap", "Gap", "Gap", "Gap"])


class StandardsMatrixTest(CorpusTest):
    def test_standards_matrix_counts_indicators_per_grade_and_marks_gaps(self):
        matrix = section(self.build(), "2. Thai standards")
        cells = [c.strip() for c in row(matrix, "ว 1.1").strip("|").split("|")]
        self.assertIn("เข้าใจความหลากหลายของระบบนิเวศ", cells[1])
        self.assertEqual(cells[-4:], ["3", "Gap", "Gap", "Gap"])
        cells = [c.strip() for c in row(matrix, "ว 3.2").strip("|").split("|")]
        self.assertEqual(cells[-4:], ["Gap", "Gap", "Gap", "3"])


class GradeModeNotesTest(CorpusTest):
    def test_a_verb_whose_mode_belongs_to_a_later_grade_is_flagged(self):
        out = self.build()
        self.assertIn("สร้างแบบจำลอง → G11, above G9", row(out, "`ว 1.1 ม.3/3`"))
        self.assertNotIn("above", row(out, "`ว 1.1 ม.3/1`"))

    def test_a_verb_from_an_earlier_mode_is_not_flagged(self):
        indicators = INDICATORS.replace("สืบค้นข้อมูลและนำเสนอ", "สร้างแบบจำลองลม")
        out = self.build(**{"thai-science-core-indicators-2560.md": indicators})
        self.assertNotIn("above", row(out, "`ว 3.2 ม.6/15`"))


class HeaderTest(CorpusTest):
    def test_header_marks_the_file_generated_and_says_how_to_regenerate_from_which_sources(self):
        out = self.build()
        head = "\n".join(out.split("\n")[:50])
        self.assertIn("scripts/build_crosswalk.py", head)
        for name in FILES:
            self.assertIn(name, head)
        self.assertRegex(head, r"(?m)^## Contents$")

    def test_out_of_scope_material_is_named_rather_than_silently_dropped(self):
        rest = section(self.build(), "Not in this crosswalk")
        self.assertIn("thai-science-supplementary-learning-outcomes-2560.md", rest)


class CommittedCrosswalkTest(unittest.TestCase):
    def test_committed_crosswalk_matches_the_reference_corpus(self):
        references = ROOT / "plugins/thai-waldorf-science/references"
        committed = (references / "curriculum-crosswalk.md").read_text(encoding="utf-8")
        self.assertEqual(
            committed, build_crosswalk(references),
            "curriculum-crosswalk.md is stale: run scripts/build_crosswalk.py",
        )


class CliTest(CorpusTest):
    def test_check_fails_while_stale_and_passes_after_regeneration(self):
        make_corpus(self.tmp)
        self.assertEqual(main(["--references", str(self.tmp), "--check"]), 1)
        self.assertEqual(main(["--references", str(self.tmp)]), 0)
        self.assertEqual(main(["--references", str(self.tmp), "--check"]), 0)
        self.assertIn("`ว 1.1 ม.3/1`", (self.tmp / "curriculum-crosswalk.md").read_text("utf-8"))


if __name__ == "__main__":
    unittest.main()

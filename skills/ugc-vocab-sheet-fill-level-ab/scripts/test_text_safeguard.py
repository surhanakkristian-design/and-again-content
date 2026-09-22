#!/usr/bin/env python3
"""Tests for the blank-language safeguard (owner decision 28, 22.9.2026; data-pass brief Part 5).

  python3 test_text_safeguard.py            # unit tests (+ the real-workbook tests when the Drive file exists)
"""
import io, os, subprocess, sys, unittest
from contextlib import redirect_stdout
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import validate_part as vp
import import_db as idb

HERE = os.path.dirname(os.path.abspath(__file__))
A2 = os.path.expanduser("~/Meine Ablage/And Again/Excels/Claude/6.9.2026-part1-translations/partsA/6.9.2026_A_part2.xlsx")


def rec(eid, L, intro=None, full=None, rid=None):
    return {"id": rid or eid * 10, "exercise_id": eid, "language_code": L, "intro_text": intro, "full_sentence": full,
            "correct_answer": "", "distractor_1": None, "distractor_2": None}


def full_set(eid, blank=()):
    return [rec(eid, L, None if L in blank else f"{L} ...", None if L in blank else f"{L} x.") for L in vp.LANGS]


class GapTests(unittest.TestCase):
    def by(self, records):
        out = {}
        for r in records:
            out.setdefault(r["exercise_id"], {})[r["language_code"]] = r
        return out

    def test_all_filled_no_gap(self):
        self.assertEqual(vp.blank_text_gaps(self.by(full_set(1))), [])

    def test_blank_new_languages_are_gaps(self):
        g = vp.blank_text_gaps(self.by(full_set(1, blank=("de", "ua", "es", "fr", "tr", "hu"))))
        self.assertEqual(sorted(L for _, L in g), sorted(["de", "ua", "es", "fr", "tr", "hu"]))

    def test_whitespace_is_blank(self):
        rs = full_set(1)
        for r in rs:
            if r["language_code"] == "hu":
                r["intro_text"], r["full_sentence"] = "  ", ""
        self.assertEqual(vp.blank_text_gaps(self.by(rs)), [(1, "hu")])

    def test_full_sentence_alone_counts_as_text(self):
        rs = full_set(1)
        rs[2]["intro_text"] = None            # de keeps full_sentence
        self.assertEqual(vp.blank_text_gaps(self.by(rs)), [])

    def test_missing_row_is_a_gap(self):
        rs = [r for r in full_set(1) if r["language_code"] != "tr"]
        self.assertEqual(vp.blank_text_gaps(self.by(rs)), [(1, "tr")])

    def test_no_source_text_no_gap(self):
        # a no-stem type (Label): no intro and no full_sentence in any language -> nothing to require
        rs = [rec(1, L) for L in vp.LANGS]
        self.assertEqual(vp.blank_text_gaps(self.by(rs)), [])

    def test_en_alone_triggers(self):
        rs = [rec(1, "en", "x ...", "x y.")] + [rec(1, L) for L in vp.LANGS if L != "en"]
        self.assertEqual(len(vp.blank_text_gaps(self.by(rs))), 8)

    def test_scope_does_not_exempt(self):
        # §0p would have scoped a grammar type to en/sk/cz; the safeguard still reports the other six
        rs = full_set(7, blank=("de", "fr"))
        self.assertEqual(sorted(L for _, L in vp.blank_text_gaps(self.by(rs))), ["de", "fr"])

    def test_filled_counts(self):
        rs = full_set(1) + full_set(2, blank=("de",))
        n = vp.filled_text_counts(rs)
        self.assertEqual(n["de"], 1)
        self.assertEqual(n["sk"], 2)
        self.assertEqual(set(n), set(vp.LANGS))


class ImportTests(unittest.TestCase):
    def test_import_refuses_blank(self):
        with redirect_stdout(io.StringIO()):
            with self.assertRaises(SystemExit) as cm:
                idb.text_safeguard(full_set(1, blank=("ua",)))
        self.assertIn("IMPORT REFUSED", str(cm.exception))
        self.assertIn("ua: 1 blank", str(cm.exception))

    def test_import_passes_and_counts(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            n = idb.text_safeguard(full_set(1) + full_set(2))
        self.assertEqual(n, {L: 2 for L in vp.LANGS})
        self.assertIn("filled text per language", buf.getvalue())

    def test_verification_sql_asserts_every_language(self):
        want = {L: i for i, L in enumerate(vp.LANGS)}
        sql = "\n".join(idb.lang_count_sql("id between 1 and 9", want))
        for i, L in enumerate(vp.LANGS):
            self.assertIn(f"language_code = '{L}'", sql)
            self.assertIn(f"if n <> {i} then raise exception 'TEXT {L}", sql)
        self.assertIn("coalesce(btrim(intro_text), '') <> ''", sql)
        self.assertIn("coalesce(btrim(full_sentence), '') <> ''", sql)


@unittest.skipUnless(os.path.exists(A2), "6.9.2026_A_part2.xlsx not on this machine")
class RealWorkbookTests(unittest.TestCase):
    """The workbook that caused the gap: its de/ua/es/fr/tr/hu grammar rows are blank (read-only runs)."""

    def test_validate_reports_E20(self):
        p = subprocess.run([sys.executable, os.path.join(HERE, "validate_part.py"), A2], capture_output=True, text=True)
        out = p.stdout + p.stderr
        self.assertIn("[E20]", out)
        for L in ("de", "ua", "es", "fr", "tr", "hu"):
            self.assertRegex(out, rf"\d+ exercises have blank {L} text")

    def test_import_dry_run_refuses(self):
        p = subprocess.run([sys.executable, os.path.join(HERE, "import_db.py"), "--workbook", A2],
                           capture_output=True, text=True, env={**os.environ, "SUPABASE_URL": "", "SUPABASE_KEY": ""})
        self.assertNotEqual(p.returncode, 0)
        self.assertIn("IMPORT REFUSED", p.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)

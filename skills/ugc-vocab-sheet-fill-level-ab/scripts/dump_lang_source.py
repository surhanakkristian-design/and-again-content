#!/usr/bin/env python3
"""
dump_lang_source.py — the SOURCE file a translator subagent reads for one batch.

    python3 dump_lang_source.py <workbook.xlsx> <out.txt> --media 5019-5031
                                [--styles styles_part1.csv] [--exceptions exception_rows.csv]

Written 15.9.2026. It replaces nothing: the batch-15 SOURCE file was produced by a script that was
never saved, so a production pass could not regenerate its own input (REPORT_2026-09-14_03 §3.2).
The block format below is that file's format, reproduced exactly.

BRIEF v29 §0f/§0: each MEDIA block now opens with the eight-line brief header of
`dump_media_briefs.py` — the word, its meaning, the irony flag, the category, the voiceover, the
explanation of the video, the props and the actions. Those eight lines are LIFTED UNCHANGED from
`dump_media_briefs.py` lines 50-57; there is one formatter for that block and this is not a second
one. Loaded once per word, they cost about 7 tokens per exercise on a 27-exercise video word.

What the translator does with them (the rule, stated in PROMPT_translations.md):
  * `meaning of the word` decides WHICH SENSE the exercise is about. Binding.
  * `explanation of the video`, `props`, `actions` decide WHICH READING of an ambiguous English
    sentence is the right one. Context only.
  * `irony: Yes` means the row is meant to be funny, and the translation must stay funny.
  * NEVER translate from the scene. The row being translated is the English sentence.

Output, per media:

    MEDIA <media_id> | concept <concept_id> | <media_type>
    <the eight-line brief header>
    W <concept_id>
    en word: <word> (<pos>) — meaning: <meaning>
    E <eid> | type <t> <title> | style <style> | exception: <why> | options <n>
    en|<intro_text>|<correct_answer>|<distractor_1>|<distractor_2>
    ...
"""
import csv, os, sys
import openpyxl


def s(v):
    return "" if v is None else str(v).strip()


def arg(name, default=None):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default


def main():
    wbp, outp = sys.argv[1], sys.argv[2]
    spec = arg("--media")
    if not spec:
        sys.exit("dump_lang_source.py: --media <lo-hi> is required")
    lo, hi = (int(x) for x in spec.split("-"))
    window = range(lo, hi + 1)

    styles, why = {}, {}
    if arg("--styles") and os.path.exists(arg("--styles")):
        with open(arg("--styles"), encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                styles[int(r["exercise_id"])] = r["style"]
    if arg("--exceptions") and os.path.exists(arg("--exceptions")):
        with open(arg("--exceptions"), encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                why[int(r["exercise_id"])] = r["why"]

    wb = openpyxl.load_workbook(wbp, read_only=True, data_only=True)

    def rows(name):
        for r in wb[name].iter_rows(min_row=2, values_only=True):
            if r[0] is not None and s(r[0]).isdigit():
                yield r

    aw = {int(r[0]): r for r in rows("All Words")}
    md = {int(r[0]): r for r in rows("media")}
    con = {int(r[0]): (s(r[1]), s(r[2])) for r in rows("word_concepts")}
    types = {int(r[0]): s(r[1]) for r in rows("ALIAS - exercise_types")}
    ex = {}
    for r in rows("exercises"):
        ex.setdefault(int(r[2]), []).append((int(r[0]), int(r[1]), int(r[3]), int(r[4])))
    en = {}
    for r in rows("sentence_translations"):
        if s(r[2]) == "en":
            en[int(r[1])] = (s(r[3]), s(r[4]), s(r[5]), s(r[6]))

    out = ["# SOURCE — for the translation pass. Read-only. Never edit this file.",
           "# One MEDIA header per clip, then its W block (the headword) and its E blocks (the exercises).",
           "# 'exception' names why a row takes the slang / flirt / idiom rule of PROMPT_translations.md.",
           ""]
    n_media = n_ex = 0
    for mid in sorted(aw):
        if mid not in window:
            continue
        exs = sorted(ex.get(mid, []))
        if not exs:
            continue
        a, m = aw[mid], md[mid]
        cid = exs[0][1]
        word, pos = con.get(cid, (s(a[1]), s(a[2])))
        if n_media:
            out.append("")                     # blank line between blocks, as SOURCE_batch_15.txt has
        out.append(f"MEDIA {mid} | concept {cid} | {s(m[5])}")
        # --- dump_media_briefs.py lines 50-57, lifted unchanged ---
        out.append(f"All Words word (as displayed): {s(a[1])}")
        out.append(f"meaning of the word: {s(a[5])}")
        out.append(f"irony: {s(a[4])} | category: {s(a[6])}")
        out.append(f"voiceover: {s(a[7]) or '(none)'}")
        out.append(f"explanation of the video: {s(a[8])}")
        out.append(f"props: {s(a[9])}")
        out.append(f"actions: {s(a[10])}")
        # ----------------------------------------------------------
        out.append(f"W {cid}")
        out.append(f"en word: {word} ({pos}) — meaning: {s(a[5])}")
        for eid, _, t, oc in exs:
            out.append(f"E {eid} | type {t} {types.get(t, '?')} | style {styles.get(eid, '?')} "
                       f"| exception: {why.get(eid, 'no')} | options {oc}")
            intro, ca, d1, d2 = en.get(eid, ("", "", "", ""))
            out.append(f"en|{intro}|{ca}|{d1}|{d2}")
            n_ex += 1
        n_media += 1
    with open(outp, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")
    print(f"wrote {outp} — {n_media} media, {n_ex} exercises, media {lo}-{hi}")


if __name__ == "__main__":
    main()

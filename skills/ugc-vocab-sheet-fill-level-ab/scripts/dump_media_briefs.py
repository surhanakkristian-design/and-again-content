#!/usr/bin/env python3
"""
dump_media_briefs.py — one brief per media item for the English content pass.

    python3 dump_media_briefs.py <workbook.xlsx> <out_dir> [--media 4001-4051]

Each brief holds everything a writer needs and nothing else: the word, part of
speech, level, meaning, irony flag, category, voiceover, the scene (explanation,
props, actions) and the list of exercise ids with their type id, title and level.
"""
import os, re, sys
import openpyxl


def s(v):
    return "" if v is None else str(v).strip()


def main():
    wbp, out = sys.argv[1], sys.argv[2]
    window = None
    if "--media" in sys.argv:
        spec = sys.argv[sys.argv.index("--media") + 1]
        lo, hi = spec.split("-")
        window = range(int(lo), int(hi) + 1)
    wb = openpyxl.load_workbook(wbp, read_only=True, data_only=True)

    def rows(name):
        for r in wb[name].iter_rows(min_row=2, values_only=True):
            if r[0] is not None and s(r[0]).isdigit():
                yield r

    aw = {int(r[0]): r for r in rows("All Words")}
    md = {int(r[0]): r for r in rows("media")}
    con = {int(r[0]): (s(r[1]), s(r[2])) for r in rows("word_concepts")}
    types = {int(r[0]): (s(r[1]), s(r[2])) for r in rows("ALIAS - exercise_types")}
    types.setdefault(74, ("Simple Explanation", "A"))
    types.setdefault(75, ("Simple Explanation", "B"))
    ex = {}
    for r in rows("exercises"):
        ex.setdefault(int(r[2]), []).append((int(r[0]), int(r[1]), int(r[3])))
    os.makedirs(out, exist_ok=True)
    n = 0
    for mid in sorted(aw):
        if window and mid not in window:
            continue
        a, m = aw[mid], md[mid]
        exs = sorted(ex.get(mid, []))
        cid = exs[0][1] if exs else None
        word, pos = con.get(cid, (s(a[1]), s(a[2])))
        lines = [f"MEDIA {mid} | concept {cid} | word: {word} | part of speech: {pos} | level: {s(a[3])} | {s(m[5])}",
                 f"All Words word (as displayed): {s(a[1])}",
                 f"meaning of the word: {s(a[5])}",
                 f"irony: {s(a[4])} | category: {s(a[6])}",
                 f"voiceover: {s(a[7]) or '(none)'}",
                 f"explanation of the video: {s(a[8])}",
                 f"props: {s(a[9])}",
                 f"actions: {s(a[10])}",
                 "", "EXERCISES (id | type id | type title | type level):"]
        for eid, _, t in exs:
            title, lv = types.get(t, ("?", "?"))
            lines.append(f"  {eid} | {t} | {title} | {lv}")
        with open(os.path.join(out, f"brief_{mid}.txt"), "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")
        n += 1
    print(f"wrote {n} briefs to {out}")


if __name__ == "__main__":
    main()

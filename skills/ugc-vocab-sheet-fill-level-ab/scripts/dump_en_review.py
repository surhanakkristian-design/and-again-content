#!/usr/bin/env python3
"""
dump_en_review.py — readable Markdown of the English rows, one section per media item.

    python3 dump_en_review.py <workbook.xlsx> <out.md>

For the human review of an English content pass: word, level, category, the scene, then
every exercise as `type title · intro · ✓ correct · ✗ distractor · ✗ distractor`.
Read-only.
"""
import sys
import openpyxl


def s(v):
    return "" if v is None else str(v).strip()


def main():
    wbp, out = sys.argv[1], sys.argv[2]
    wb = openpyxl.load_workbook(wbp, read_only=True, data_only=True)

    def rows(name):
        for r in wb[name].iter_rows(min_row=2, values_only=True):
            if r[0] is not None and s(r[0]).isdigit():
                yield r

    aw = {int(r[0]): r for r in rows("All Words")}
    con = {int(r[0]): (s(r[1]), s(r[2])) for r in rows("word_concepts")}
    types = {int(r[0]): (s(r[1]), s(r[2])) for r in rows("ALIAS - exercise_types")}
    ex_by_media = {}
    for r in rows("exercises"):
        ex_by_media.setdefault(int(r[2]), []).append((int(r[0]), int(r[1]), int(r[3])))
    en = {}
    for r in rows("sentence_translations"):
        if s(r[2]) == "en":
            en[int(r[1])] = (s(r[3]), s(r[4]), s(r[5]), s(r[6]))

    lines = ["# English exercises — review", ""]
    n_ex = n_filled = 0
    for mid in sorted(ex_by_media):
        a = aw[mid]
        exs = sorted(ex_by_media[mid])
        word, pos = con.get(exs[0][1], (s(a[1]), s(a[2])))
        lines += [f"## {mid} · {s(a[1])} ({pos}) · level {s(a[3])} · {s(a[6])} · concept {exs[0][1]}",
                  f"*Meaning:* {s(a[5])}  ",
                  f"*Scene:* {s(a[8])}", ""]
        if s(a[7]):
            lines.insert(len(lines) - 1, f"*Voiceover:* {s(a[7])}  ")
        lines.append("| # | type | intro | ✓ | ✗ | ✗ |")
        lines.append("|---|---|---|---|---|---|")
        for eid, cid, t in exs:
            title, lv = types.get(t, ("Simple Explanation", "?"))
            intro, ca, d1, d2 = en.get(eid, ("", "", "", ""))
            n_ex += 1
            n_filled += bool(ca)
            esc = lambda x: x.replace("|", "\\|")
            lines.append(f"| {eid} | {t} {esc(title)} ({lv}) | {esc(intro)} | {esc(ca)} | {esc(d1)} | {esc(d2)} |")
        lines.append("")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print(f"{out}: {len(ex_by_media)} media, {n_filled}/{n_ex} exercises with English content")


if __name__ == "__main__":
    main()

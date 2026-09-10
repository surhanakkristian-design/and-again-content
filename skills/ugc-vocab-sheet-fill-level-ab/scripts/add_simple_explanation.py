#!/usr/bin/env python3
"""
add_simple_explanation.py — add the Simple Explanation exercise to a finished part.

Simple Explanation (type 74 = A, 75 = B) is the shortest exercise there is: name the
asset in at most four words. It is derived from the Label exercise of the same media
(type 27 at A level, 68 at B), so this script only builds the scaffold — one exercises
row plus nine empty sentence_translations rows per media item — and copies the Label
exercise id into a side file so the language pass knows what to shorten.

  python3 add_simple_explanation.py --workbook part.xlsx                    # dry run
  ... --apply                                                              # writes
  ... --apply --exercise-id-start 120000                                   # explicit ids

Ids continue from the workbook's own maximum unless --exercise-id-start says otherwise;
sentence_translations ids follow the usual `(exercise_id - 1) * 9 + k` rule, so they
never collide with anything already in the file.
"""
import argparse, csv, os, shutil, sys
from collections import defaultdict
from datetime import datetime
import openpyxl

LANGS = ["sk", "en", "de", "cz", "fr", "es", "ua", "tr", "hu"]
LABEL = {"A": 27, "B": 68}          # the exercise each new one is derived from
SIMPLE = {"A": 74, "B": 75}         # the new type ids


def s(v):
    return "" if v is None else str(v).strip()


def rows_of(ws, skip=2):
    out = []
    for i, r in enumerate(ws.iter_rows(values_only=True), start=1):
        if i <= 1 or not any(c not in (None, "") for c in r):
            continue
        if any(s(v).lower() in ("example", "exemple") for v in r):
            continue
        try:
            int(s(r[0]))
        except ValueError:
            continue
        out.append(r)
    return out


def main(a):
    wb = openpyxl.load_workbook(a.workbook)
    words = rows_of(wb["All Words"])
    level_of = {s(r[0]): s(r[3]).upper() for r in words}
    bad = {v for v in level_of.values() if v not in LABEL}
    if bad:
        sys.exit(f"unknown level(s) in All Words: {bad}")
    levels = set(level_of.values())
    level = levels.pop() if len(levels) == 1 else "AB"   # mixed parts: per media row

    ex_ws, st_ws = wb["exercises"], wb["sentence_translations"]
    exes = rows_of(ex_ws)
    by_media_label, existing_new = {}, set()
    max_ex = 0
    for r in exes:
        eid, cid, mid, t = int(s(r[0])), s(r[1]), s(r[2]), int(s(r[3]))
        max_ex = max(max_ex, eid)
        lv = level_of.get(mid)
        if lv is None:
            sys.exit(f"exercise {eid}: media {mid} has no All Words row")
        if t == LABEL[lv]:
            by_media_label[mid] = (eid, cid)
        if t == SIMPLE[lv]:
            existing_new.add(mid)
    label_type = "/".join(str(LABEL[l]) for l in sorted(set(level_of.values())))
    new_type_desc = "/".join(str(SIMPLE[l]) for l in sorted(set(level_of.values())))

    concepts = {s(r[0]): s(r[1]) for r in rows_of(wb["word_concepts"])}   # id -> word
    todo = [(mid, eid, cid) for mid, (eid, cid) in sorted(by_media_label.items(), key=lambda x: int(x[0]))
            if mid not in existing_new]

    print(f"{os.path.basename(a.workbook)} — level {level}")
    print(f"  media with a Label exercise (type {label_type})   {len(by_media_label)}")
    print(f"  Simple Explanation (type {new_type_desc}) already there {len(existing_new)}")
    print(f"  to add                                            {len(todo)}")
    if not todo:
        print("nothing to do")
        return

    next_ex = a.exercise_id_start or max_ex + 1
    print(f"  new exercise ids                                  {next_ex}–{next_ex + len(todo) - 1}")
    if not a.apply:
        print("\ndry run — add --apply to write")
        return

    backup = f"{a.workbook}.bak_{datetime.now():%Y%m%d_%H%M%S}"
    shutil.copy(a.workbook, backup)

    ex_row = ex_ws.max_row + 1
    st_row = st_ws.max_row + 1
    pairs = []
    for mid, label_eid, cid in todo:
        eid = next_ex
        next_ex += 1
        for col, val in enumerate([eid, int(cid), int(mid), SIMPLE[level_of[mid]], 3], start=1):
            ex_ws.cell(ex_row, col, val)
        ex_row += 1
        for k, lang in enumerate(LANGS):
            st_ws.cell(st_row, 1, (eid - 1) * 9 + k + 1)
            st_ws.cell(st_row, 2, eid)
            st_ws.cell(st_row, 3, lang)
            st_row += 1
        pairs.append({"exercise_id": eid, "derived_from_exercise_id": label_eid,
                      "media_id": mid, "concept_id": cid,
                      "word": concepts.get(cid, "")})

    wb.save(a.workbook)

    side = os.path.splitext(a.workbook)[0] + " — simple_explanation.csv"
    with open(side, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(pairs[0].keys()))
        w.writeheader()
        w.writerows(pairs)

    print(f"\nadded {len(pairs)} exercises and {len(pairs) * 9} translation rows")
    print(f"backup:  {os.path.basename(backup)}")
    print(f"mapping: {os.path.basename(side)}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--workbook", required=True)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--exercise-id-start", type=int, default=0)
    main(ap.parse_args())

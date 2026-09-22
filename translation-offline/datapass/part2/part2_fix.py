"""Part 2: punctuation fixes from Wave 1 Part A (ua 138 no final period, ua/es 720, es 10819, de 3046)."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "lib"))
sys.path.insert(0, os.path.expanduser("~/Projects/and-again-content/skills/ugc-vocab-sheet-fill-level-ab/scripts"))
from validate_part import derive_full_sentence
import writer

rows = [json.loads(l) for l in open(os.path.join(ROOT, "snapshot/loc_rows.jsonl"))]
ex = {e["id"]: e for e in map(json.loads, open(os.path.join(ROOT, "snapshot/exercises.jsonl")))}
S = {r["exercise_id"] for r in json.load(open(os.path.join(ROOT, "snapshot/sets.json")))["selected"]}
by = {(r["exercise_id"], r["language_code"]): r for r in rows}
COLS = ["intro_text", "full_sentence"]
changes, why = [], {}

def add(r, intro, reason, expect_full):
    full = derive_full_sentence(intro, r["correct_answer"] or "", r["language_code"], ex[r["exercise_id"]]["exercise_type_id"])
    assert full == expect_full, (r["exercise_id"], full, expect_full)
    changes.append({"id": r["id"], "exercise_id": r["exercise_id"], "lang": r["language_code"],
                    "new": {"intro_text": intro, "full_sentence": full},
                    "old": {"intro_text": r["intro_text"], "full_sentence": r["full_sentence"]}})
    why[r["id"]] = reason

for (eid, L), r in sorted(by.items()):
    if eid in S and L == "ua" and r["full_sentence"] and eid != 720:
        fs = r["full_sentence"].rstrip()
        if not fs.endswith((".", "!", "?", "…", "»", '"', "“", "”", ")")):
            add(r, r["intro_text"], "ua: final period missing (intro ends on the gap; derive adds it)", r["full_sentence"] + ".")
add(by[(720, "ua")], by[(720, "ua")]["intro_text"], "ua: doubled '??'", "Ти вистелила деко пергаментом, правда ж?")
add(by[(720, "es")], "Forraste la bandeja con papel de horno, ...?", "es: double '¿' and doubled '??' (the tag carries its own ¿…?)",
    "Forraste la bandeja con papel de horno, ¿verdad?")
add(by[(10819, "es")], "Estaba pasadísimo de ácido, ...?", "es: double '¿' (the tag carries its own ¿…?)",
    "Estaba pasadísimo de ácido, ¿verdad?")
add(by[(3046, "de")], by[(3046, "de")]["intro_text"], "de: final period missing", by[(3046, "de")]["full_sentence"] + ".")

json.dump([{**c, "reason": why[c["id"]]} for c in changes], open(os.path.join(HERE, "part2_changes.json"), "w"), ensure_ascii=False, indent=0)
import collections
print(len(changes), collections.Counter(c["lang"] for c in changes))
dry = "--write" not in sys.argv
res = writer.run("part2", "part2_all", changes, COLS, dry=dry)
print(json.dumps({k: v for k, v in res.items()}, ensure_ascii=False)[:1500])

"""Machine check of the Part 1 proposals + the verifier input."""
import json, os, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.expanduser("~/Projects/and-again-content/skills/ugc-vocab-sheet-fill-level-ab/scripts"))
from validate_part import derive_full_sentence
rows = [json.loads(l) for l in open(os.path.join(ROOT, "snapshot/loc_rows.jsonl"))]
ex = {e["id"]: e for e in map(json.loads, open(os.path.join(ROOT, "snapshot/exercises.jsonl")))}
S = {r["exercise_id"] for r in json.load(open(os.path.join(ROOT, "snapshot/sets.json")))["selected"]}
by = {(r["exercise_id"], r["language_code"]): r for r in rows}
props, bad = [], []
for k in range(1, 9):
    for line in open(os.path.join(HERE, f"prop_{k:02d}.txt"), encoding="utf-8"):
        line = line.rstrip("\n")
        if not line.strip() or line.strip() == "NONE":
            continue
        p = line.split("|")
        if len(p) != 6:
            bad.append((line, "field count")); continue
        eid, L, ni, na, nf, why = p
        eid = int(eid)
        if eid not in S or L not in ("sk", "cz"):
            bad.append((line, "not a selected sk/cz row")); continue
        r = by[(eid, L)]
        old = (r["intro_text"] or "", r["correct_answer"] or "", r["full_sentence"] or "")
        issues = []
        if (ni, na, nf) == old:
            issues.append("no change")
        if ni.count("...") != old[0].count("..."):
            issues.append("gap count changed")
        d = derive_full_sentence(ni, na, L, ex[eid]["exercise_type_id"])
        if d != nf:
            issues.append(f"full_sentence != intro+answer ({d})")
        props.append({"id": r["id"], "exercise_id": eid, "lang": L, "old": old, "new": (ni, na, nf), "why": why, "issues": issues})
json.dump({"props": props, "bad": bad}, open(os.path.join(HERE, "props_checked.json"), "w"), ensure_ascii=False, indent=0)
c = collections.Counter((p["lang"], tuple(x.split(" (")[0] for x in p["issues"])) for p in props)
print(len(props), c, "bad", len(bad))
for p in props:
    if p["issues"]:
        print(p["exercise_id"], p["lang"], p["issues"], p["old"], p["new"])
# verifier input (ALL proposals, issues included)
with open(os.path.join(HERE, "verify_in.txt"), "w") as f:
    for n, p in enumerate(props, 1):
        en = by[(p["exercise_id"], "en")]["full_sentence"]
        f.write(f"P{n} | E {p['exercise_id']} {p['lang']} | en: {en}\n")
        f.write(f"OLD|{'|'.join(p['old'])}\nNEW|{'|'.join(p['new'])}\nREASON|{p['why']}\n")

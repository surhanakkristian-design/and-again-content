"""Part 1 input slices: the 4,064 selected exercises, sk + cz rows, English full_sentence for meaning."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.expanduser("~/Projects/and-again-content/skills/ugc-vocab-sheet-fill-level-ab/scripts"))
from validate_part import derive_full_sentence
rows = [json.loads(l) for l in open(os.path.join(ROOT, "snapshot/loc_rows.jsonl"))]
ex = {e["id"]: e for e in map(json.loads, open(os.path.join(ROOT, "snapshot/exercises.jsonl")))}
sel = json.load(open(os.path.join(ROOT, "snapshot/sets.json")))["selected"]
by = {(r["exercise_id"], r["language_code"]): r for r in rows}
N = 8
ids = [r["exercise_id"] for r in sel]; lev = {r["exercise_id"]: r["level"] for r in sel}
per = -(-len(ids) // N)
for k in range(N):
    part = ids[k * per:(k + 1) * per]
    with open(os.path.join(HERE, f"in_{k+1:02d}.txt"), "w") as f:
        for i in part:
            en = by[(i, "en")]["full_sentence"]
            f.write(f"E {i} {lev[i]} | en: {en}\n")
            for L in ("sk", "cz"):
                r = by[(i, L)]
                f.write(f"{L}|{r['intro_text'] or ''}|{r['correct_answer'] or ''}|{r['full_sentence'] or ''}\n")
                d = derive_full_sentence(r["intro_text"] or "", r["correct_answer"] or "", L, ex[i]["exercise_type_id"])
                if d != r["full_sentence"]:
                    f.write(f"NOTE {L}: full_sentence differs from intro_text+correct_answer; the mechanical fill gives: {d}\n")
    print(k + 1, len(part))

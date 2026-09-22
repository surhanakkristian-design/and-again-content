"""Write the Part 1 fixes that BOTH the proposer and the independent verifier agree on."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "lib"))
import writer
props = json.load(open(os.path.join(HERE, "props_checked.json")))["props"]
v = {}
for f in ("verdict_a.txt", "verdict_b.txt"):
    for l in open(os.path.join(HERE, f), encoding="utf-8"):
        p = l.strip().split("|")
        v[int(p[0][1:])] = p[1:]
assert len(v) == len(props)
COLS = ["intro_text", "correct_answer", "full_sentence"]
changes, rejected = [], []
for n, p in enumerate(props, 1):
    if v[n][0] == "AGREE" and not p["issues"]:
        changes.append({"id": p["id"], "exercise_id": p["exercise_id"], "lang": p["lang"],
                        "new": dict(zip(COLS, p["new"])), "old": dict(zip(COLS, p["old"]))})
    else:
        rejected.append({**p, "verdict": v[n]})
# the snapshot stores NULL/'' where old fields were empty; the proposals use '' -> map back to the exact stored value
snap = {(json.loads(l)["id"]): json.loads(l) for l in open(os.path.join(ROOT, "snapshot/loc_rows.jsonl"))}
for c in changes:
    r = snap[c["id"]]
    for k in COLS:
        if (r[k] or "") == c["old"][k]:
            c["old"][k] = r[k]
        if c["new"][k] == "" and r[k] is None:
            c["new"][k] = None
json.dump({"written": changes, "rejected": rejected}, open(os.path.join(HERE, "part1_final.json"), "w"), ensure_ascii=False, indent=0)
print("agreed", len(changes), "rejected", len(rejected))
dry = "--write" not in sys.argv
print(json.dumps(writer.run("part1", "part1_all", changes, COLS, dry=dry), ensure_ascii=False)[:800])

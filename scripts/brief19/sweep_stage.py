#!/usr/bin/env python3
"""Brief 20 Part 5: from the recall sweep to repair inputs.
  sweep_stage.py flagged  --lang de   -> runs/sweep_<lang>/precision/input_<k>.json (150 rows each) for judges 2 and 3
                                         (rows flagged by the sweep, minus rows already repaired)
  sweep_stage.py majority --lang de   -> rows failed by >=2 of 3 judges -> runs/sweep_<lang>/repair/input_<k>.json (25 rows each,
                                         full row from the DB + type_title + judge_issue/judge_fix) and repair/targets.json
Judges 2/3 write precision/judge2_<k>.json and judge3_<k>.json (PROMPT_grammar_check.md)."""
import json, os, sys, glob, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); APP = os.path.abspath(os.path.join(HERE, "..", ".."))
def dbq(sql):
    out = subprocess.run(["npx", "-y", "supabase@2.116.0", "db", "query", sql, "--linked", "-o", "json"], cwd=APP, capture_output=True, text=True).stdout
    i = out.find('{\n  "boundary"'); i = out.find('{') if i < 0 else i
    return json.JSONDecoder().raw_decode(out[i:])[0]["rows"]
def arg(n, d=None): return sys.argv[sys.argv.index(n)+1] if n in sys.argv else d
lang = arg("--lang", "de"); d = os.path.join(HERE, "runs", f"sweep_{lang}")
rows = {r["id"]: r for r in json.load(open(os.path.join(d, "rows.json")))}
def sweep_verdicts():
    v = {}
    for f in sorted(glob.glob(os.path.join(d, "judge_*.json"))):
        for x in json.load(open(f)): v[x["id"]] = x
    return v
already = set()
for f in (os.path.join(HERE, "runs", "repair_de", "fixes.json"), os.path.join(HERE, "runs", "grammar_de", "fixes.json")):
    if os.path.exists(f): already |= {x["id"] for x in json.load(open(f))}
if sys.argv[1] == "flagged":
    v = sweep_verdicts(); flagged = sorted(i for i, x in v.items() if not x.get("ok", True) and i in rows and i not in already)
    pd = os.path.join(d, "precision"); os.makedirs(pd, exist_ok=True); made = []
    for k, b in enumerate(range(0, len(flagged), 150), 1):
        part = flagged[b:b+150]
        json.dump([{"id": i, "sentence": rows[i]["sentence"]} for i in part], open(os.path.join(pd, f"input_{k}.json"), "w"), ensure_ascii=False, indent=0); made.append(k)
    json.dump(flagged, open(os.path.join(pd, "flagged_ids.json"), "w"))
    print(json.dumps({"judged": len(v), "flagged": len(flagged), "already_repaired_skipped": len(already & {i for i, x in v.items() if not x.get("ok", True)}), "parts": made}))
elif sys.argv[1] == "majority":
    v = sweep_verdicts(); pd = os.path.join(d, "precision")
    j2 = {}; j3 = {}
    for f in glob.glob(os.path.join(pd, "judge2_*.json")):
        for x in json.load(open(f)): j2[x["id"]] = x
    for f in glob.glob(os.path.join(pd, "judge3_*.json")):
        for x in json.load(open(f)): j3[x["id"]] = x
    flagged = json.load(open(os.path.join(pd, "flagged_ids.json")))
    missing = [i for i in flagged if i not in j2 or i not in j3]
    bad = []
    for i in flagged:
        votes = 1 + (0 if j2.get(i, {}).get("ok", True) else 1) + (0 if j3.get(i, {}).get("ok", True) else 1)
        if votes >= 2: bad.append(i)
    print(json.dumps({"flagged": len(flagged), "missing_precision_verdicts": len(missing), "majority_bad": len(bad), "precision": round(len(bad)/max(1,len(flagged)), 3)}))
    if missing: print("missing:", missing[:30]); sys.exit(1)
    types = {t["id"]: t["title"].get("en") for t in json.load(open(arg("--types", "/private/tmp/claude-501/-Users-kristiansurhanak-Meine-Ablage-And-Again/377e9bc3-6d06-4a36-9ba6-e6557ba618de/scratchpad/types.json")))}
    rd = os.path.join(d, "repair"); os.makedirs(rd, exist_ok=True)
    full = {}
    for b in range(0, len(bad), 500):
        ids = ",".join(map(str, bad[b:b+500]))
        for r in dbq(f"select el.id, e.exercise_type_id as type_id, el.intro_text, el.correct_answer, el.distractor_1, el.distractor_2, el.full_sentence from exercise_localizations el join exercises e on e.id=el.exercise_id where el.id in ({ids})"): full[r["id"]] = r
    items = []
    for i in bad:
        r = full[i]; vs = [x for x in (v.get(i), j2.get(i), j3.get(i)) if x and not x.get("ok", True)]
        items.append({**r, "type_title": types.get(r["type_id"]), "kind": "grammar", "judge_issue": " | ".join(x.get("issue", "") for x in vs), "judge_fix": vs[0].get("fix") if vs else None})
    json.dump(items, open(os.path.join(rd, "targets.json"), "w"), ensure_ascii=False, indent=1)
    made = []
    for k, b in enumerate(range(0, len(items), 25), 1):
        json.dump(items[b:b+25], open(os.path.join(rd, f"input_{k}.json"), "w"), ensure_ascii=False, indent=1); made.append(k)
    print(json.dumps({"repair_parts": made, "rows": len(items)}))

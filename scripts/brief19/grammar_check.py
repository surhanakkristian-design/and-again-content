#!/usr/bin/env python3
"""Reusable grammar audit of full_sentence per language.
  grammar_check.py sample --lang de [--n 200] [--salt grammar1]   -> runs/grammar_<lang>/sample.json (+ input for judges)
  grammar_check.py report --lang de                                -> aggregates judge_*.json by exercise type, agreement of judges
Judges are Claude subagents that read PROMPT_grammar_check.md + the sample and write judge_<k>.json."""
import json, os, sys, subprocess
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); APP = os.path.abspath(os.path.join(HERE, "..", ".."))
def dbq(sql):
    out = subprocess.run(["npx", "-y", "supabase@2.116.0", "db", "query", sql, "--linked", "-o", "json"], cwd=APP, capture_output=True, text=True).stdout
    i = out.find('{\n  "boundary"'); i = out.find('{') if i < 0 else i
    return json.JSONDecoder().raw_decode(out[i:])[0]["rows"]
def arg(n, d=None): return sys.argv[sys.argv.index(n)+1] if n in sys.argv else d
lang = arg("--lang"); d = arg("--dir") or os.path.join(HERE, "runs", f"grammar_{lang}"); os.makedirs(d, exist_ok=True)
if sys.argv[1] == "merge":  # judge_<k>_part<i>.json -> judge_<k>.json
    import glob, re
    for k in sorted({re.search(r"judge_(\d+)_part", f).group(1) for f in glob.glob(os.path.join(d, "judge_*_part*.json"))}):
        out = []
        for f in sorted(glob.glob(os.path.join(d, f"judge_{k}_part*.json"))): out += json.load(open(f))
        json.dump(out, open(os.path.join(d, f"judge_{k}.json"), "w"), ensure_ascii=False); print("judge", k, len(out), "verdicts")
    sys.exit(0)
if sys.argv[1] == "sample":
    n = int(arg("--n", 200)); salt = arg("--salt", "grammar1")
    rows = dbq(f"select el.id, e.exercise_type_id as type_id, el.full_sentence as sentence, el.correct_answer as answer from exercise_localizations el join exercises e on e.id=el.exercise_id where el.language_code='{lang}' and el.full_sentence is not null and e.exercise_type_id<>69 order by md5(el.id::text||'{salt}') limit {n}")
    json.dump(rows, open(os.path.join(d, "sample.json"), "w"), ensure_ascii=False, indent=1)
    json.dump([{"id": r["id"], "sentence": r["sentence"]} for r in rows], open(os.path.join(d, f"input_{lang}.json"), "w"), ensure_ascii=False, indent=0)
    print(json.dumps({"lang": lang, "n": len(rows), "types": len(set(r["type_id"] for r in rows)), "input": os.path.join(d, f"input_{lang}.json")}))
elif sys.argv[1] == "report":
    rows = {r["id"]: r for r in json.load(open(os.path.join(d, "sample.json")))}
    judges = sorted(f for f in os.listdir(d) if f.startswith("judge_") and f.endswith(".json"))
    verdicts = {}
    for f in judges:
        for v in json.load(open(os.path.join(d, f))): verdicts.setdefault(v["id"], {})[f] = v
    flagged_any = {i for i, vs in verdicts.items() if any(not v.get("ok", True) for v in vs.values())}
    flagged_all = {i for i, vs in verdicts.items() if len(vs) == len(judges) and all(not v.get("ok", True) for v in vs.values())}
    print(f"lang {lang}: sample {len(rows)}, judges {len(judges)}; flagged by ANY judge {len(flagged_any)} ({100*len(flagged_any)/len(rows):.1f}%), by ALL judges {len(flagged_all)} ({100*len(flagged_all)/len(rows):.1f}%)")
    by_type_all = Counter(rows[i]["type_id"] for i in flagged_all); by_type_any = Counter(rows[i]["type_id"] for i in flagged_any)
    sampled_by_type = Counter(r["type_id"] for r in rows.values())
    print("by exercise type (both judges / any judge / sampled):")
    for t, c in sorted(by_type_any.items(), key=lambda x: -x[1]): print(f"  type {t}: {by_type_all.get(t,0)} / {c} / {sampled_by_type[t]}")
    print("--- flagged by both judges ---")
    for i in sorted(flagged_all, key=lambda i: rows[i]["type_id"]):
        r = rows[i]; v = next(iter(verdicts[i].values()))
        print(f"  [{r['type_id']}] {r['sentence']}\n       -> {v.get('issue','')} | {v.get('fix','')}")
    print("--- flagged by one judge only ---")
    for i in sorted(flagged_any - flagged_all, key=lambda i: rows[i]["type_id"]):
        r = rows[i]; v = next(v for v in verdicts[i].values() if not v.get("ok", True))
        print(f"  [{r['type_id']}] {r['sentence']}\n       -> {v.get('issue','')} | {v.get('fix','')}")
    json.dump({"lang": lang, "sample": len(rows), "flagged_any": sorted(flagged_any), "flagged_all": sorted(flagged_all), "by_type_all": by_type_all, "by_type_any": by_type_any}, open(os.path.join(d, "report.json"), "w"), ensure_ascii=False, indent=1)

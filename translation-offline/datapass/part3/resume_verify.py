"""RESUME RUN verification: rowhash resume_before vs resume_after, changed rows must be rows written by s046-s069;
filled counts before/after; per-language/level cells; reviewer disagreement."""
import json, os, sys, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")); sys.path.insert(0, os.path.join(ROOT, "lib"))
import db
J = lambda p: json.load(open(os.path.join(ROOT, p)))
SL = [f"s{n:03d}" for n in range(46, 70)]
ex = {e["id"]: e for e in map(json.loads, open(os.path.join(ROOT, "snapshot/exercises.jsonl")))}
index = {x["slice"]: x for x in J("part3/slices/index.json")}; st = J("part3/state.json")
b = J("snapshot/rowhash_resume_before.json"); a = J("snapshot/rowhash_resume_after.json")
written = set(); cells = collections.Counter(); lvl = collections.Counter(); left = []; corr = emptied = 0; ncells = 0
for sl in SL:
    f = J(f"part3/final/{sl}.json"); ncells += len(index[sl]["ids"]) * 6
    corr += len(f["corrections"]); emptied += sum(1 for x in f["left_empty"] if x[2].startswith("reviewer"))
    left += f["left_empty"]
    for c in f["changes"]:
        cells[c["lang"]] += 1; lvl[(c["lang"], ex[c["exercise_id"]]["type_level"])] += 1
    for l in open(os.path.join(ROOT, "backups/part3", f"{sl}.jsonl")):
        if l.strip() and l.strip() != "null": written.add(json.loads(l)["id"])
out = {"slices_done": [s for s in SL if st.get(s, {}).get("done")], "exercises": sum(len(index[s]["ids"]) for s in SL),
       "cells_total": ncells, "cells": dict(cells), "lvl": {f"{k[0]}|{k[1]}": v for k, v in lvl.items()}, "left_empty": left,
       "reviewer_changed": corr, "reviewer_emptied": emptied, "per_lang": {}, "tables": {},
       "state": {s: st[s] for s in SL}}
for L in b["loc"]:
    ch = {int(i) for i, h in a["loc"][L].items() if b["loc"][L].get(i) != h}
    out["per_lang"][L] = {"rows": len(a["loc"][L]), "changed": len(ch), "changed_not_written": len(ch - written),
                          "written_not_changed": len({i for i in written if str(i) in a["loc"][L]} - ch) if L in cells else 0,
                          "added": len(set(a["loc"][L]) - set(b["loc"][L])), "removed": len(set(b["loc"][L]) - set(a["loc"][L]))}
for t in b["tables"]:
    out["tables"][t] = {"n": a["tables"][t]["n"], "same": a["tables"][t] == b["tables"][t]}
E = J("snapshot/sets.json")["empty_ids"]; nowE = collections.Counter()
for i in range(0, len(E), 3000):
    for r in db.rows(f"""select language_code l, count(*) n from exercise_localizations where exercise_id in ({','.join(map(str, E[i:i+3000]))})
        and (coalesce(btrim(intro_text),'')<>'' or coalesce(btrim(full_sentence),'')<>'') group by 1"""):
        nowE[r["l"]] += r["n"]
now = {r["l"]: r["n"] for r in db.rows("""select language_code l, count(*) n from exercise_localizations
        where coalesce(btrim(intro_text),'')<>'' or coalesce(btrim(full_sentence),'')<>'' group by 1""")}
fb = J("snapshot/filled_resume_before.json")
out["filled_10283"] = {L: [fb["filled_10283"].get(L, 0), nowE[L]] for L in b["loc"]}
out["filled_table"] = {L: [fb["filled_table"].get(L, 0), now.get(L, 0)] for L in b["loc"]}
json.dump(out, open(os.path.join(ROOT, "verify_db_resume.json"), "w"), indent=1, ensure_ascii=False)
print(json.dumps({k: v for k, v in out.items() if k not in ("state", "left_empty")}, indent=0, ensure_ascii=False))
print("left_empty", left)

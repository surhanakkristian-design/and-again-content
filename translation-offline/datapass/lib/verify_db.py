"""DB verification after the data pass: rowhash_after vs rowhash_before, touched ids per part, filled counts."""
import glob, json, os, sys, collections
sys.path.insert(0, os.path.dirname(__file__))
import db
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
b = json.load(open(os.path.join(ROOT, "snapshot/rowhash_before.json")))
a = json.load(open(os.path.join(ROOT, "snapshot/rowhash_after.json")))
touched = collections.defaultdict(set)      # part -> row ids written by this pass
for part in ("part1", "part2", "part3", "part4"):
    for l in open(os.path.join(ROOT, "backups", part, "write_log.jsonl")) if os.path.exists(os.path.join(ROOT, "backups", part, "write_log.jsonl")) else []:
        pass
    for p in glob.glob(os.path.join(ROOT, "backups", part, "*.jsonl")):
        if p.endswith("write_log.jsonl"):
            continue
        for l in open(p):
            if l.strip() and l.strip() != "null":
                touched[part].add(json.loads(l)["id"])
alltouched = set().union(*touched.values())
out = {"per_lang": {}, "tables": {}}
for L in b["loc"]:
    changed = {int(i) for i, h in b["loc"][L].items() if a["loc"][L].get(i) != h}
    added = set(map(int, a["loc"][L])) - set(map(int, b["loc"][L]))
    removed = set(map(int, b["loc"][L])) - set(map(int, a["loc"][L]))
    out["per_lang"][L] = {"rows": len(a["loc"][L]), "changed": len(changed), "changed_not_touched": sorted(changed - alltouched)[:20],
                          "n_changed_not_touched": len(changed - alltouched), "added": len(added), "removed": len(removed)}
for t in b["tables"]:
    out["tables"][t] = {"before": b["tables"][t], "after": a["tables"][t], "same": b["tables"][t] == a["tables"][t]}
out["touched_per_part"] = {k: len(v) for k, v in touched.items()}
# filled counts (intro_text or full_sentence non-blank), whole table and the 10,283 set, before (snapshot) vs now
sets = json.load(open(os.path.join(ROOT, "snapshot/sets.json")))
E = sets["empty_ids"]
now = collections.Counter(); nowE = collections.Counter()
for i in range(0, len(E), 3000):
    for r in db.rows(f"""select language_code l, count(*) n from exercise_localizations where exercise_id in ({','.join(map(str, E[i:i+3000]))})
        and (coalesce(btrim(intro_text),'')<>'' or coalesce(btrim(full_sentence),'')<>'') group by 1"""):
        nowE[r["l"]] += r["n"]
for r in db.rows("""select language_code l, count(*) n from exercise_localizations
        where coalesce(btrim(intro_text),'')<>'' or coalesce(btrim(full_sentence),'')<>'' group by 1"""):
    now[r["l"]] = r["n"]
snap = [json.loads(l) for l in open(os.path.join(ROOT, "snapshot/loc_rows.jsonl"))]
Es = set(E)
beforeE = collections.Counter(r["language_code"] for r in snap if r["exercise_id"] in Es and ((r["intro_text"] or "").strip() or (r["full_sentence"] or "").strip()))
out["filled_10283"] = {L: {"before": beforeE[L], "after": nowE[L]} for L in b["loc"]}
out["filled_table_now"] = dict(now)
json.dump(out, open(os.path.join(ROOT, "verify_db.json"), "w"), indent=1)
print(json.dumps(out, indent=1)[:3000])

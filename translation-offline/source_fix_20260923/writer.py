"""Guarded batched writes to exercise_localizations (copied from mismatch_fix_20260923 for the 5 source fixes, decision 59).

change = {"id", "exercise_id", "lang", "new": {col: val}, "old": {col: val}, ...}. Every change in one call writes the
same column set. A row is written only when every written column still holds the backed-up value (IS NOT DISTINCT
FROM); jsonb columns (chunks, correct_alternative) are only in the column set of the English Part 3 rows.
Batches <= 200 rows, each ONE UPDATE statement = one transaction. Rollback SQL is written, never run.
"""
import hashlib, json, os, sys, time
sys.path.insert(0, os.path.expanduser('~/Projects/and-again-content/translation-offline/datapass/lib'))
import db
H = os.path.dirname(os.path.abspath(__file__))
TEXT = ["intro_text", "correct_answer", "distractor_1", "distractor_2", "full_sentence"]
JSONB = ["chunks", "correct_alternative"]
ALL = TEXT + JSONB
SEL = "id, exercise_id, language_code, " + ", ".join(ALL)


def fetch(ids):
    ids = sorted(set(ids)); out = []
    for i in range(0, len(ids), 1000):
        out += db.rows(f"select {SEL} from exercise_localizations where id in ({','.join(map(str, ids[i:i+1000]))})")
    return {r["id"]: r for r in out}


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def lit(col, v):
    if col in JSONB:
        return "NULL::jsonb" if v is None else db.q(json.dumps(v, ensure_ascii=False)) + "::jsonb"
    return db.q(v) + "::text"


def update_sql(changes, cols):
    vn = ["id", "eid", "lang"] + [f"n_{k}" for k in cols] + [f"o_{k}" for k in cols]
    tup = []
    for c in changes:
        p = [str(int(c["id"])), str(int(c["exercise_id"])), db.q(c["lang"])]
        p += [lit(k, c["new"][k]) for k in cols] + [lit(k, c["old"][k]) for k in cols]
        tup.append("(" + ",".join(p) + ")")
    sets = ", ".join(f"{k} = v.n_{k}" for k in cols)
    guard = " and ".join(f"l.{k} is not distinct from v.o_{k}" for k in cols)
    return (f"update exercise_localizations l set {sets}\nfrom (values\n" + ",\n".join(tup) +
            f"\n) v({', '.join(vn)})\nwhere l.id = v.id and l.exercise_id = v.eid and l.language_code = v.lang and {guard}\nreturning l.id;")


def run(name, changes, cols, dry=False, B=200):
    assert set(cols) <= set(ALL)
    for c in changes:
        assert set(c["new"]) == set(cols) and set(c["old"]) == set(cols), c["id"]
    cur = fetch([c["id"] for c in changes])
    os.makedirs(f"{H}/backups", exist_ok=True); os.makedirs(f"{H}/rollback", exist_ok=True)
    bpath = f"{H}/backups/{name}.jsonl"
    if not os.path.exists(bpath):                      # first backup is kept forever
        with open(bpath, "w") as f:
            for c in changes:
                f.write(json.dumps(cur[c["id"]], ensure_ascii=False, sort_keys=True) + "\n")
        open(bpath + ".sha256", "w").write(sha(bpath) + "  " + os.path.basename(bpath) + "\n")
    backup = {json.loads(l)["id"]: json.loads(l) for l in open(bpath)}
    todo, already, skipped = [], [], []
    for c in changes:
        r = cur.get(c["id"])
        if r is None or r["exercise_id"] != c["exercise_id"] or r["language_code"] != c["lang"]:
            skipped.append((c["id"], "row missing / id mismatch")); continue
        if all(r[k] == c["new"][k] for k in cols):
            already.append(c["id"]); continue
        if all(r[k] == c["old"][k] for k in cols):
            todo.append(c); continue
        skipped.append((c["id"], "live value differs from old"))
    rpath = f"{H}/rollback/{name}_rollback.sql"
    with open(rpath, "w") as f:
        f.write(f"-- rollback for source_fix_20260923/{name}; NOT run. Restores the backed-up values where the row still holds\n"
                f"-- exactly what this pass wrote.\n")
        flip = [{**c, "new": c["old"], "old": c["new"]} for c in changes]
        for i in range(0, len(flip), B):
            f.write("begin;\n" + update_sql(flip[i:i+B], cols) + "\ncommit;\n")
    written = []
    if not dry:
        for i in range(0, len(todo), B):
            sql = update_sql(todo[i:i+B], cols)
            for a in range(6):
                try:
                    res = db.rows(sql); break
                except RuntimeError:
                    if a == 5: raise
                    time.sleep(10 * (a + 1))
            written += [x["id"] for x in res]
    after = fetch([c["id"] for c in changes]) if not dry else cur
    bad = []
    if not dry:
        sk = {s[0] for s in skipped}
        for c in changes:
            if c["id"] in sk: continue
            r, b = after[c["id"]], backup[c["id"]]
            for k in ALL:
                want = c["new"][k] if k in cols else b[k]
                if r[k] != want:
                    bad.append((c["id"], k))
    res = {"name": name, "n": len(changes), "todo": len(todo), "written": len(written), "already": len(already),
           "skipped": skipped, "verify_bad": bad, "backup": os.path.relpath(bpath, H), "backup_sha256": sha(bpath),
           "rollback": os.path.relpath(rpath, H), "dry": dry}
    with open(f"{H}/backups/write_log.jsonl", "a") as f:
        f.write(json.dumps(res, ensure_ascii=False) + "\n")
    return res

"""Guarded, batched, idempotent writes to exercise_localizations.

A change = {"id": row id, "exercise_id", "lang", "new": {col: value}, "old": {col: value}}.
Only the columns in "new" are written; the row is written only when EVERY column in "old" still
holds its backed-up value (IS NOT DISTINCT FROM) -- so a re-run is a no-op and a row that changed
in the meantime is skipped and listed. For Part 3 "old" is the empty state of the target fields.
"""
import hashlib, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import db

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
COLS = ["intro_text", "correct_answer", "distractor_1", "distractor_2", "full_sentence"]
SEL = "id, exercise_id, language_code, intro_text, correct_answer, distractor_1, distractor_2, full_sentence, chunks, correct_alternative"


def fetch(ids):
    out = []
    ids = sorted(set(ids))
    for i in range(0, len(ids), 2000):
        out += db.rows(f"select {SEL} from exercise_localizations where id in ({','.join(map(str, ids[i:i+2000]))}) order by id")
    return {r["id"]: r for r in out}


def _sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def _vals(changes, cols):
    tup = []
    for c in changes:
        parts = [str(int(c["id"])), str(int(c["exercise_id"])), db.q(c["lang"])]
        parts += [db.q(c["new"].get(k)) + "::text" for k in cols]
        parts += [db.q(c["old"].get(k)) + "::text" for k in cols]
        tup.append("(" + ",".join(parts) + ")")
    return ",\n".join(tup)


def update_sql(changes, cols):
    """One UPDATE statement (= one transaction) for a batch; guarded on the old values."""
    vnames = ["id", "eid", "lang"] + [f"n_{k}" for k in cols] + [f"o_{k}" for k in cols]
    sets = ", ".join(f"{k} = v.n_{k}" for k in cols)
    guard = " and ".join(f"l.{k} is not distinct from v.o_{k}" for k in cols)
    return (f"update exercise_localizations l set {sets}\nfrom (values\n{_vals(changes, cols)}\n) v({', '.join(vnames)})\n"
            f"where l.id = v.id and l.exercise_id = v.eid and l.language_code = v.lang and {guard}\nreturning l.id;")


def rollback_sql(changes, cols):
    """Restore the old values, only where the row still holds exactly what this pass wrote."""
    flip = [{"id": c["id"], "exercise_id": c["exercise_id"], "lang": c["lang"], "new": c["old"], "old": c["new"]} for c in changes]
    return update_sql(flip, cols)


def run(part, batch_name, changes, cols, dry=False):
    """Backup -> compare -> rollback file -> write in <=500 batches -> re-select verify. Returns a result dict."""
    assert set(cols) <= set(COLS), cols
    for c in changes:
        assert set(c["new"]) == set(cols) and set(c["old"]) == set(cols), c
    bdir = os.path.join(ROOT, "backups", part); os.makedirs(bdir, exist_ok=True)
    rdir = os.path.join(ROOT, "rollback", part); os.makedirs(rdir, exist_ok=True)
    cur = fetch([c["id"] for c in changes])
    bpath = os.path.join(bdir, f"{batch_name}.jsonl")
    if not os.path.exists(bpath):          # the FIRST backup is kept; a resumed run never overwrites it
        with open(bpath, "w") as f:
            for c in changes:
                f.write(json.dumps(cur.get(c["id"]), ensure_ascii=False, sort_keys=True) + "\n")
        with open(bpath + ".sha256", "w") as f:
            f.write(_sha(bpath) + "  " + os.path.basename(bpath) + "\n")
    todo, done_already, skipped = [], [], []
    for c in changes:
        r = cur.get(c["id"])
        if r is None or r["exercise_id"] != c["exercise_id"] or r["language_code"] != c["lang"]:
            skipped.append((c, "row missing / id mismatch")); continue
        if all(r[k] == c["new"][k] for k in cols):
            done_already.append(c); continue
        if all(r[k] == c["old"][k] for k in cols):
            todo.append(c); continue
        skipped.append((c, "changed since backup: " + json.dumps({k: r[k] for k in cols}, ensure_ascii=False)))
    rpath = os.path.join(rdir, f"{batch_name}_rollback.sql")
    if changes and not os.path.exists(rpath):
        with open(rpath, "w") as f:
            f.write(f"-- rollback for {part}/{batch_name}; NOT run. Restores the backed-up values where the row\n"
                    f"-- still holds exactly what the data pass wrote.\n")
            for i in range(0, len(changes), 500):
                f.write("begin;\n" + rollback_sql(changes[i:i+500], cols) + "\ncommit;\n")
    written = []
    if not dry:
        for i in range(0, len(todo), 500):
            res = db.rows(update_sql(todo[i:i+500], cols))
            written += [x["id"] for x in res]
    after = fetch([c["id"] for c in changes]) if not dry else cur
    verify_bad = []
    if not dry:
        for c in changes:
            if any(sk[0]["id"] == c["id"] for sk in skipped):
                continue
            r = after[c["id"]]
            if not all(r[k] == c["new"][k] for k in cols):
                verify_bad.append(c["id"])
            # untouched columns must equal the backup
            b = cur[c["id"]]
            for k in ("chunks", "correct_alternative") + tuple(x for x in COLS if x not in cols):
                if r[k] != b[k]:
                    verify_bad.append(c["id"])
    res = {"batch": batch_name, "n": len(changes), "todo": len(todo), "written": len(written),
           "already": len(done_already), "skipped": [(s[0]["id"], s[0]["exercise_id"], s[0]["lang"], s[1]) for s in skipped],
           "verify_bad": verify_bad, "backup": os.path.relpath(bpath, ROOT), "backup_sha256": _sha(bpath),
           "rollback": os.path.relpath(rpath, ROOT)}
    with open(os.path.join(ROOT, "backups", part, "write_log.jsonl"), "a") as f:
        f.write(json.dumps({**res, "dry": dry}, ensure_ascii=False) + "\n")
    return res

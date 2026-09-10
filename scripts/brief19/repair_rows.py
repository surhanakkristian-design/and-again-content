#!/usr/bin/env python3
"""Brief 20 Part 2/3: apply whole-row repairs to exercise_localizations.
  repair_rows.py check  fixes.json   -> builds full_sentence by interleaving intro/answer on '...', checks shapes, prints before/after
  repair_rows.py sql    fixes.json out.sql -> UPDATE statements (chunks/correct_alternative set NULL)
fixes.json: [{"id", "intro_text", "correct_answer", "distractor_1", "distractor_2", "note"}]"""
import json, sys, subprocess, os
APP = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
def interleave(intro, answer):
    ip = intro.split("..."); ap = [a.strip() for a in answer.split("...")]
    assert len(ip) == len(ap) + 1, f"blanks {len(ip)-1} vs answer parts {len(ap)}: {intro!r} / {answer!r}"
    out = ip[0]
    for a, i in zip(ap, ip[1:]): out += a + i
    return " ".join(out.split())  # normalise whitespace only (no double spaces)
def shape(s): return (s or "").count("...")
def dbq(sql):
    out = subprocess.run(["npx", "-y", "supabase@2.116.0", "db", "query", sql, "--linked", "-o", "json"], cwd=APP, capture_output=True, text=True).stdout
    i = out.find('{\n  "boundary"'); i = out.find('{') if i < 0 else i
    return json.JSONDecoder().raw_decode(out[i:])[0]["rows"]
def lit(v): return "NULL" if v is None else "'" + v.replace("'", "''") + "'"
cmd, path = sys.argv[1], sys.argv[2]; fixes = json.load(open(path))
ids = ",".join(str(f["id"]) for f in fixes)
before = {r["id"]: r for r in dbq(f"select el.id, e.exercise_type_id as type_id, el.intro_text, el.correct_answer, el.distractor_1, el.distractor_2, el.full_sentence from exercise_localizations el join exercises e on e.id=el.exercise_id where el.id in ({ids})")}
ok = True
for f in fixes:
    b = before[f["id"]]; f["full_sentence"] = interleave(f["intro_text"], f["correct_answer"])
    problems = []
    # Two-option types ("Past Simple or Continuous" etc.) legitimately have no distractor_2: keep it empty
    # when the source row had none; otherwise it must exist and match the answer's shape.
    d2_optional = not b.get("distractor_2")
    if shape(f["correct_answer"]) != shape(f["distractor_1"]): problems.append("distractor shape differs from answer")
    if f.get("distractor_2") and shape(f["correct_answer"]) != shape(f["distractor_2"]): problems.append("distractor shape differs from answer")
    if f["full_sentence"].count("...") : problems.append("'...' left in full_sentence")
    for k in ("distractor_1", "distractor_2"):
        if f.get(k) and f[k] == f["correct_answer"]: problems.append(f"{k} equals answer")
    for k in ("intro_text","correct_answer","distractor_1") + (() if d2_optional else ("distractor_2",)):
        if not f.get(k): problems.append(f"{k} empty")
    if d2_optional and not f.get("distractor_2"): f["distractor_2"] = None
    if problems: ok = False
    if cmd == "check":
        print(f"--- {f['id']} type {b['type_id']} {'OK' if not problems else 'PROBLEM ' + '; '.join(problems)}\n  note:   {f.get('note','')}")
        for k in ("intro_text", "correct_answer", "distractor_1", "distractor_2", "full_sentence"):
            print(f"  {k:15} BEFORE {b[k]!r}\n  {'':15} AFTER  {f[k]!r}")
if cmd == "sql":
    assert ok, "fix problems first"
    lines = []
    for f in fixes:
        lines.append(f"update public.exercise_localizations set intro_text={lit(f['intro_text'])}, correct_answer={lit(f['correct_answer'])}, distractor_1={lit(f['distractor_1'])}, distractor_2={lit(f['distractor_2'])}, full_sentence={lit(f['full_sentence'])}, chunks=NULL, correct_alternative=NULL where id={f['id']};")
    lines.append(f"select id, full_sentence, correct_answer from public.exercise_localizations where id in ({ids}) order by id;")
    open(sys.argv[3], "w").write("\n".join(lines) + "\n"); print("sql written:", sys.argv[3], len(fixes), "rows")
    json.dump([{"id": f["id"], "type_id": before[f["id"]]["type_id"], "before": {k: before[f["id"]][k] for k in ("intro_text","correct_answer","distractor_1","distractor_2","full_sentence")}, "after": {k: f[k] for k in ("intro_text","correct_answer","distractor_1","distractor_2","full_sentence")}, "note": f.get("note","")} for f in fixes],
              open(os.path.join(os.path.dirname(path), "fixes_before_after.json"), "w"), ensure_ascii=False, indent=1)

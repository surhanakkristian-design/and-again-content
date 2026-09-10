#!/usr/bin/env python3
"""usage: apply_chunks.py accepted.json out.sql  -> UPDATE statements for exercise_localizations (chunks + correct_alternative).
Only rows in accepted.json; chunks are written from the validated arrays, never re-derived."""
import json, sys
acc = json.load(open(sys.argv[1]))
def lit(v): return "'" + json.dumps(v, ensure_ascii=False).replace("'", "''") + "'::jsonb"
lines = ["update public.exercise_localizations as el set chunks = v.chunks, correct_alternative = v.alt from (values"]
vals = [f"  ({a['id']}, {lit(a['chunks'])}, {lit(a['alternatives'])})" for a in acc]
lines.append(",\n".join(vals))
lines.append(") as v(id, chunks, alt) where el.id = v.id and el.full_sentence = " + "array_to_string(array(select jsonb_array_elements_text(v.chunks)), ' ');")
lines.append("select count(*) as updated from public.exercise_localizations where id in (" + ",".join(str(a['id']) for a in acc) + ") and chunks is not null;")
open(sys.argv[2], "w").write("\n".join(lines) + "\n")
print("statements for", len(acc), "rows ->", sys.argv[2])

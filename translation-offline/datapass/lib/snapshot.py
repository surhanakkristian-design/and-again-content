"""Read-only snapshot of every row the data pass may touch (all 9 languages), plus context."""
import hashlib, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import db

OUT = os.path.join(os.path.dirname(__file__), "..", "snapshot")
LANGS6 = ["de", "ua", "es", "fr", "tr", "hu"]

def blank(c):
    return f"coalesce(btrim({c}),'')=''"

# The empty set: full_sentence filled in sk/cz/en, empty in all six new languages (the check report's definition).
empty = db.rows(f"""
select e.id from exercises e
where exists(select 1 from exercise_localizations l where l.exercise_id=e.id and l.language_code='sk' and not {blank('l.full_sentence')})
  and exists(select 1 from exercise_localizations l where l.exercise_id=e.id and l.language_code='cz' and not {blank('l.full_sentence')})
  and exists(select 1 from exercise_localizations l where l.exercise_id=e.id and l.language_code='en' and not {blank('l.full_sentence')})
  and not exists(select 1 from exercise_localizations l where l.exercise_id=e.id and l.language_code in ('de','ua','es','fr','tr','hu') and not {blank('l.full_sentence')})
order by e.id""")
empty_ids = [r["id"] for r in empty]
sel = db.rows("select exercise_id, level from translation_selected_exercises order by exercise_id")
sel_ids = [r["exercise_id"] for r in sel]
ids = sorted(set(empty_ids) | set(sel_ids))
print("empty", len(empty_ids), min(empty_ids), max(empty_ids), "selected", len(sel_ids), "union", len(ids))

rows = []
for i in range(0, len(ids), 1500):
    chunk = ids[i:i + 1500]
    rows += db.rows(f"""select l.id, l.exercise_id, l.language_code, l.intro_text, l.correct_answer, l.distractor_1,
      l.distractor_2, l.full_sentence, l.chunks, l.correct_alternative
      from exercise_localizations l where l.exercise_id in ({','.join(map(str, chunk))}) order by l.exercise_id, l.language_code""")
ex = []
for i in range(0, len(ids), 3000):
    chunk = ids[i:i + 3000]
    ex += db.rows(f"""select e.id, e.concept_id, e.media_id, e.exercise_type_id, t.level as type_level, t.title->>'en' as type_title from exercises e
      left join exercise_types t on t.id=e.exercise_type_id where e.id in ({','.join(map(str, chunk))}) order by e.id""")

def dump(name, obj):
    p = os.path.join(OUT, name)
    with open(p, "w") as f:
        for o in obj:
            f.write(json.dumps(o, ensure_ascii=False, sort_keys=True) + "\n")
    h = hashlib.sha256(open(p, "rb").read()).hexdigest()
    print(name, len(obj), h)
    return h

hs = {}
hs["loc_rows.jsonl"] = dump("loc_rows.jsonl", rows)
hs["exercises.jsonl"] = dump("exercises.jsonl", ex)
json.dump({"empty_ids": empty_ids, "selected": sel}, open(os.path.join(OUT, "sets.json"), "w"))
hs["sets.json"] = hashlib.sha256(open(os.path.join(OUT, "sets.json"), "rb").read()).hexdigest()
with open(os.path.join(OUT, "SHA256SUMS"), "w") as f:
    for k, v in hs.items():
        f.write(f"{v}  {k}\n")

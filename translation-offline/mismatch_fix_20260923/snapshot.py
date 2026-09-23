# Live snapshot of every exercise touched by this brief: all 9 langs of the 303 confirmed exercises + the 629 Part 4 es rows.
import json, sys, os
sys.path.insert(0, os.path.expanduser('~/Projects/and-again-content/translation-offline/datapass/lib'))
import db
H = os.path.dirname(os.path.abspath(__file__))
TO = os.path.dirname(H)
c = json.load(open(f'{TO}/mismatch_scan_20260923/confirmed.json'))
p4 = sorted({json.loads(l)['exercise_id'] for l in open(f'{TO}/datapass/backups/part4/part4_es.jsonl')})
ids = sorted({x['id'] for x in c} | set(p4))
out = []
for i in range(0, len(ids), 300):
    out += db.rows("select l.id, l.exercise_id, l.language_code, l.intro_text, l.correct_answer, l.distractor_1, l.distractor_2, l.full_sentence, l.chunks, l.correct_alternative, e.exercise_type_id "
                   f"from exercise_localizations l join exercises e on e.id=l.exercise_id where l.exercise_id in ({','.join(map(str, ids[i:i+300]))}) order by l.exercise_id, l.language_code")
name = sys.argv[1] if len(sys.argv) > 1 else 'before'
json.dump(out, open(f'{H}/work/snapshot_{name}.json', 'w'), ensure_ascii=False, indent=0)
print(len(ids), 'exercises', len(out), 'rows', name)

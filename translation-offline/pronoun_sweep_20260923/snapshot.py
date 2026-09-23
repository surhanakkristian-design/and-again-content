# SELECT only: every localization row (en + the six natives) of the 4,064 translation_selected_exercises.
import json, sys, os
sys.path.insert(0, os.path.expanduser('~/Projects/and-again-content/translation-offline/datapass/lib'))
import db
H = os.path.dirname(os.path.abspath(__file__))
ids = [r['exercise_id'] for r in db.rows("select exercise_id from translation_selected_exercises order by exercise_id")]
assert len(ids) == 4064, len(ids)
out = []
for i in range(0, len(ids), 500):
    out += db.rows("select l.id, l.exercise_id, l.language_code, l.intro_text, l.correct_answer, l.distractor_1, l.distractor_2, "
                   "l.full_sentence, e.exercise_type_id, t.level from exercise_localizations l join exercises e on e.id=l.exercise_id "
                   "join translation_selected_exercises t on t.exercise_id=l.exercise_id "
                   f"where l.exercise_id in ({','.join(map(str, ids[i:i+500]))}) and l.language_code in ('en','de','ua','es','fr','tr','hu') "
                   "order by l.exercise_id, l.language_code")
name = sys.argv[1] if len(sys.argv) > 1 else 'before'
json.dump(out, open(f'{H}/work/snapshot_{name}.json', 'w'), ensure_ascii=False, indent=0)
from collections import Counter
print(len(ids), 'exercises', len(out), 'rows', dict(Counter(r['language_code'] for r in out)))

# Live snapshot (read-only): every language row of every exercise that has at least one row whose full_sentence
# ends without . ! ? (after trimming). chunks are not read: this pass never touches them.
import json, sys, os, hashlib
sys.path.insert(0, os.path.expanduser('~/Projects/and-again-content/translation-offline/datapass/lib'))
import db
H = os.path.dirname(os.path.abspath(__file__))
name = sys.argv[1] if len(sys.argv) > 1 else 'before'
ids = [r['exercise_id'] for r in db.rows(
    "select distinct exercise_id from exercise_localizations where full_sentence is not null and full_sentence<>'' "
    "and right(rtrim(full_sentence),1) not in ('.','!','?') order by 1")]
out = []
for i in range(0, len(ids), 1500):
    out += db.rows("select l.id, l.exercise_id, l.language_code, l.intro_text, l.correct_answer, l.distractor_1, l.distractor_2, "
                   "l.full_sentence, e.exercise_type_id from exercise_localizations l join exercises e on e.id=l.exercise_id "
                   f"where l.exercise_id in ({','.join(map(str, ids[i:i+1500]))}) order by l.exercise_id, l.language_code")
p = f'{H}/work/snapshot_{name}.json'
json.dump(out, open(p, 'w'), ensure_ascii=False)
open(p + '.sha256', 'w').write(hashlib.sha256(open(p, 'rb').read()).hexdigest() + '  ' + os.path.basename(p) + '\n')
print(len(ids), 'exercises', len(out), 'rows', name)

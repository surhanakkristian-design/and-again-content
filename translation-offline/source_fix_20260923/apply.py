"""Decision 59: write the 5 agreed source fixes (proposer + independent verifier both AGREE). Guarded writer."""
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H); sys.path.insert(0, os.path.join(os.path.dirname(H), 'mismatch_fix_20260923'))
import writer, fixlib
COLS = ["intro_text", "correct_answer", "distractor_1", "distractor_2", "full_sentence"]
snap = {(r['exercise_id'], r['language_code']): r for r in json.load(open(f'{H}/work/snapshot_before.json'))}
ver = {(v['exercise_id'], v['lang']): v['verdict'] for v in json.load(open(f'{H}/work/verdicts.json'))}
changes = []
for p in json.load(open(f'{H}/work/proposals.json')):
    k = (p['exercise_id'], p['lang'])
    if ver.get(k) != 'AGREE':
        print('not agreed, skipped', k); continue
    old = snap[k]
    new = {c: p[c] for c in COLS}
    errs = fixlib.check_row({**new, 'exercise_type_id': old['exercise_type_id'], 'language_code': p['lang']})
    assert not errs, (k, errs)
    assert new['intro_text'].count('...') == 1, k
    changes.append({'id': old['id'], 'exercise_id': k[0], 'lang': k[1], 'new': new, 'old': {c: old[c] for c in COLS}})
print(len(changes), 'changes')
res = writer.run('source_fix_5', changes, COLS, dry='--dry' in sys.argv)
print(json.dumps(res, ensure_ascii=False))

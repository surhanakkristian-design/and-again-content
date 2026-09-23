# Part A fix: rows that BOTH the judge (A) and the independent verifier (B) call WRONG, with B accepting A's fix.
import csv, json, os, sys, collections
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(H), "mismatch_fix_20260923")); sys.path.insert(0, H)
import writer, fixlib
dry = '--dry' in sys.argv
A = {r['key']: r for r in csv.DictReader(open(f'{H}/agents/judge_A.tsv'), delimiter='\t')}
B = {r['key']: r for r in csv.DictReader(open(f'{H}/agents/verify_B.tsv'), delimiter='\t')}
flags = {f['key']: f for f in json.load(open(f'{H}/work/flags_keyed.json'))}
snap = {(r['exercise_id'], r['language_code']): r for r in json.load(open(f'{H}/work/snapshot_before.json'))}
changes, table = [], []
for k in sorted(flags):
    a, b, f = A[k], B[k], flags[k]
    both = a['verdict'] == 'WRONG' and b['my_verdict'] == 'WRONG' and b['fix_ok'] == 'YES'
    table.append({'key': k, 'exercise_id': f['exercise_id'], 'lang': f['lang'], 'A': a['verdict'], 'B': b['my_verdict'], 'fix_ok': b['fix_ok'], 'fixed': both})
    if not both:
        continue
    cur = snap[(f['exercise_id'], f['lang'])]
    new = dict(cur, intro_text=a['intro_text'], correct_answer=a['correct_answer'], distractor_1=a['distractor_1'], distractor_2=a['distractor_2'])
    new['full_sentence'] = fixlib.derive(new['intro_text'], new['correct_answer'], f['lang'], cur['exercise_type_id'])
    errs = fixlib.check_row(new)
    assert not errs, (k, errs)
    cols = [c for c in writer.TEXT if new[c] != cur[c]]
    changes.append({'id': cur['id'], 'exercise_id': cur['exercise_id'], 'lang': f['lang'], 'cols': cols,
                    'new': {c: new[c] for c in cols}, 'old': {c: cur[c] for c in cols}})
json.dump(table, open(f'{H}/work/decisions.json', 'w'), ensure_ascii=False, indent=1)
json.dump(changes, open(f'{H}/work/changes.json', 'w'), ensure_ascii=False, indent=1)
by = collections.defaultdict(list)
for c in changes: by[tuple(c['cols'])].append(c)
for cols, ch in by.items():
    print(json.dumps(writer.run('sweep_fix_' + '_'.join(cols), ch, list(cols), dry=dry), ensure_ascii=False))
for c in changes: print(c['exercise_id'], c['lang'], c['old'], '->', c['new'])

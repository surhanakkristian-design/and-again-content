# Round 2: writes the round-2 rows both passes agree on (fresh proposer + fresh verifier).
import csv, json, writer
props = json.load(open('work/proposals_r2.json'))
verd = {r['key']: r['verdict'] for r in csv.DictReader(open('agents/v_r2_verdict.tsv'), delimiter='\t', quoting=csv.QUOTE_NONE)}
COLS = ['intro_text', 'correct_answer', 'distractor_1', 'distractor_2', 'full_sentence']
ch = [{'id': p['id'], 'exercise_id': p['exercise_id'], 'lang': p['lang'], 'key': k, 'new': {c: p['new'][c] for c in COLS}, 'old': p['old']}
      for k, p in props.items() if verd.get(k) == 'AGREE' and not p['errs'] and p['changed']]
left = [k for k in props if k not in {c['key'] for c in ch}]
json.dump(left, open('work/unwritten_final.json', 'w'))
print('left', left)
r = writer.run('round2', ch, COLS)
print(json.dumps({k: r[k] for k in ('name', 'n', 'todo', 'written', 'skipped', 'verify_bad')}, ensure_ascii=False))

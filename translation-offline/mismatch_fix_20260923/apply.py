# Writes the rows BOTH passes agree on. Usage: python3 apply.py [--dry]
import csv, json, sys, writer
dry = '--dry' in sys.argv
props = json.load(open('work/proposals.json'))
p3 = json.load(open('work/p3_en_changes.json'))
verd = {}
for g in ('v1', 'v2a', 'v2b'):
    for r in csv.DictReader(open(f'agents/{g}_verdict.tsv'), delimiter='\t', quoting=csv.QUOTE_NONE):
        verd[r['key'].strip()] = (r['verdict'].strip(), r['reason'])
COLS = ['intro_text', 'correct_answer', 'distractor_1', 'distractor_2', 'full_sentence']
agreed = {'part1_es': [], 'part2_natives': []}; unwritten = []
for k, p in props.items():
    v = verd.get(k, ('MISSING', ''))
    if v[0] != 'AGREE' or p['errs'] or not p['changed']:
        unwritten.append({'key': k, 'exercise_id': p['exercise_id'], 'lang': p['lang'], 'verdict': v[0], 'reason': v[1], 'errs': p['errs'],
                          'old': p['old']['full_sentence'], 'proposed': p['new']['full_sentence']}); continue
    agreed['part1_es' if k.startswith('P1') else 'part2_natives'].append(
        {'id': p['id'], 'exercise_id': p['exercise_id'], 'lang': p['lang'], 'key': k, 'new': {c: p['new'][c] for c in COLS}, 'old': p['old']})
en = []
for c in p3:
    v = verd.get(c['key'], ('MISSING', ''))
    if v[0] == 'AGREE':
        en.append(c)
    else:
        unwritten.append({'key': c['key'], 'exercise_id': c['exercise_id'], 'lang': 'en', 'verdict': v[0], 'reason': v[1], 'errs': [],
                          'old': c['old']['full_sentence'], 'proposed': c['new']['full_sentence']})
json.dump(unwritten, open('work/unwritten.json', 'w'), ensure_ascii=False, indent=1)
print('unwritten', len(unwritten))
out = []
for name, ch in agreed.items():
    out.append(writer.run(name, ch, COLS, dry=dry))
if en:
    out.append(writer.run('part3_en', en, COLS + ['chunks', 'correct_alternative'], dry=dry))
for r in out:
    print(json.dumps({k: r[k] for k in ('name', 'n', 'todo', 'written', 'already', 'skipped', 'verify_bad', 'backup_sha256', 'dry')}, ensure_ascii=False))

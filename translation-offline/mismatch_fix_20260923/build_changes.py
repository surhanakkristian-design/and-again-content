# Reads the proposer TSVs, derives full_sentence, runs the invariants, writes work/proposals.json and the verifier inputs.
import csv, json, sys, fixlib, collections
R2 = '--r2' in sys.argv
by = fixlib.load('before')
keys = json.load(open('work/item_keys.json'))
types = {int(k): v for k, v in json.load(open('work/types.json')).items()}
items_txt = {}
for n in ('p1', 'p2a', 'p2b'):
    for b in open(f'agents/{n}_items.txt').read().split('\n@@ ')[0:]:
        b = b if b.startswith('@@ ') else '@@ ' + b
        items_txt[b.split()[1]] = b.strip()
props = {}
for n in (('p_r2',) if R2 else ('p1', 'p2a', 'p2b')):
    for r in csv.DictReader(open(f'agents/{n}_prop.tsv'), delimiter='\t', quoting=csv.QUOTE_NONE):
        props[r['key']] = r
missing = sorted(set(keys) - set(props)); extra = sorted(set(props) - set(keys))
COLS = ['intro_text', 'correct_answer', 'distractor_1', 'distractor_2', 'full_sentence']
res = {}; problems = []
if R2:
    keys = {k: v for k, v in keys.items() if k in props}
for key, (eid, lang) in keys.items():
    if key not in props:
        continue
    p = props[key]; old = by[eid][lang]
    new = {k: p[k] for k in ('intro_text', 'correct_answer', 'distractor_1', 'distractor_2')}
    for k in new:                          # an empty cell keeps its NULL-vs-'' form
        if new[k] == '' and old[k] in (None, ''):
            new[k] = old[k]
    new['full_sentence'] = fixlib.derive(new['intro_text'], new['correct_answer'], lang, old['exercise_type_id'])
    errs = fixlib.check_row({**old, **new}) if new['full_sentence'] is not None else ['derive failed']
    # a distractor collision the row did not already have
    oc = lambda r: sum(1 for d in ('distractor_1', 'distractor_2') if r[d] and (r['correct_answer'] or '').strip() and r[d].strip().lower() == r['correct_answer'].strip().lower())
    errs = [e for e in errs if 'equals correct_answer' not in e]
    if oc({**old, **new}) > oc(old):
        errs.append('new distractor collision')
    changed = any((new[k] or '') != (old[k] or '') for k in ('intro_text', 'correct_answer', 'distractor_1', 'distractor_2', 'full_sentence'))
    res[key] = {'key': key, 'exercise_id': eid, 'lang': lang, 'id': old['id'], 'mode': p['mode'], 'note': p['note'],
                'old': {k: old[k] for k in COLS},
                'new': new, 'changed': changed, 'errs': errs}
    if errs: problems.append((key, errs))
json.dump(res, open('work/proposals_r2.json' if R2 else 'work/proposals.json', 'w'), ensure_ascii=False, indent=1)
print('proposals', len(res), 'missing', missing, 'extra', extra)
print('modes', collections.Counter(r['mode'] for r in res.values()), 'unchanged-but-not-NOCHANGE',
      [k for k, r in res.items() if not r['changed'] and r['mode'] != 'NOCHANGE'])
for p in problems: print('PROBLEM', p)

def vblock(r):
    t = items_txt[r['key']].split('\n')
    head = [l for l in t if not l.startswith(f"{r['lang']} CURRENT")]
    o, n = r['old'], r['new']
    add = [f"{r['lang']} OLD full: {o['full_sentence']}  [gap: {o['correct_answer'] or ''}]  [distractors: {o['distractor_1'] or ''} | {o['distractor_2'] or ''}]",
           f"{r['lang']} PROPOSED NEW full: {n['full_sentence']}  [gap: {n['correct_answer'] or ''}]  [distractors: {n['distractor_1'] or ''} | {n['distractor_2'] or ''}]  [mode: {r['mode']}]  [proposer note: {r['note']}]"]
    return '\n'.join(head[:2] + add + head[2:])
if R2:
    open('agents/v_r2_items.txt', 'w').write('\n\n'.join(vblock(r) for r in res.values()) + '\n')
if '--verify-inputs' in sys.argv:
    p3 = json.load(open('work/p3_en_changes.json'))
    groups = {'v1': [], 'v2a': [], 'v2b': []}
    for k, r in res.items():
        g = 'v1' if k.startswith('P1') else ('v2a' if r['lang'] in ('de', 'es', 'fr', 'tr') else 'v2b')
        groups[g].append(vblock(r))
    for c in p3:
        eid = c['exercise_id']; e = by[eid]
        L = [f"@@ {c['key']} {eid} en level-type: {types[e['en']['exercise_type_id']]} (type {e['en']['exercise_type_id']})",
             f"en OLD full: {c['old']['full_sentence']}  [gap: {c['old']['correct_answer']}]  [distractors: {c['old']['distractor_1']} | {c['old']['distractor_2']}]  [chunks: {' / '.join(c['old']['chunks'])}]",
             f"en PROPOSED NEW full: {c['new']['full_sentence']}  [gap: {c['new']['correct_answer']}]  [distractors: {c['new']['distractor_1']} | {c['new']['distractor_2']}]  [chunks: {' / '.join(c['new']['chunks'])}]  [correct_alternative: {c['new']['correct_alternative']}]",
             "ISSUE: the English said something different from all 8 natives; the English is rewritten to what the natives say"]
        L += [f"  (native) {l}: {e[l]['full_sentence']}  [gap: {e[l]['correct_answer'] or ''}]" for l in fixlib.LANGS if l != 'en']
        groups['v2a'].append('\n'.join(L))
    for g, L in groups.items():
        open(f'agents/{g}_items.txt', 'w').write('\n\n'.join(L) + '\n')
        print(g, len(L))

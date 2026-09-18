#!/usr/bin/env python3
"""Compact indexes for annotators: synonyms/INDEX.txt and selection/batches/b<n>_lib.txt."""
import json, glob, os
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
groups = []
for f in sorted(glob.glob('synonyms/*.json')):
    if f.endswith('forms.json'): continue
    groups += json.load(open(f)).get('groups', [])
with open('synonyms/INDEX.txt', 'w') as o:
    o.write('# safe (automatic, never annotate): ' + '; '.join('/'.join(g['m']) for g in groups if g['kind'] == 'safe') + '\n')
    o.write('# contextual: id: members (pos)\n')
    for g in groups:
        if g['kind'] == 'contextual':
            o.write(f"{g['id']}: {', '.join(g['m'])} ({g.get('pos','x')})\n")
lib = {}
for f in glob.glob('mistakes/*.json'):
    d = json.load(open(f)); lib[int(d['type_id'])] = d
for bf in sorted(glob.glob('selection/batches/b*.jsonl')):
    ts = sorted({json.loads(l)['t'] for l in open(bf)})
    with open(bf.replace('.jsonl', '_lib.txt'), 'w') as o:
        for t in ts:
            d = lib.get(t)
            if not d: o.write(f'## {t} (library missing)\n'); continue
            o.write(f"## {t} {d.get('topic','')}\n")
            for it in d['items']:
                extra = [s for s in it.get('slots', []) if s not in ('right', 'wrong')]
                o.write(f"{it['id']} [{'tip' if it['verdict']=='correct_with_tip' else 'wrong'}] {it.get('pattern') or it.get('kind')}" + (f" slots:{','.join(extra)}" if extra else '') + '\n')
print('indexes:', len(groups), 'groups,', len(lib), 'topics')

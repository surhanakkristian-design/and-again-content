# A66 task 1: "ATV" -> "quad bike" in the English of item 7071 (lib/lab58.json). Articles change with it.
# Clears the recordings of every changed voiced text (phrases, nouns, rows, story) -> tts66.py records them.
import json, sys, os
APP = os.path.expanduser('~/Projects/and-again-a66/lib/lab58.json')
HERE = os.path.dirname(os.path.abspath(__file__))
lab = json.load(open(APP)); c = [x for x in lab if x['mediaId'] == 7071][0]
log = []
def sub(s):
    t = s.replace('an ATV', 'a quad bike').replace('the ATV', 'the quad bike').replace("ATV", 'quad bike')
    return t
def setp(where, obj, key):
    old = obj[key]; new = sub(old)
    if new != old: obj[key] = new; log.append({'field': where, 'before': old, 'after': new})
    return new != old
v = c['voices']
for i, t in enumerate(c['taps']):
    setp(f'taps[{i}].target', t, 'target')
    if setp(f'taps[{i}].phrase', t, 'phrase'): v['phrases'][i] = None
for i, n in enumerate(c['nouns']):
    if setp(f'nouns[{i}].word', n, 'word'): v['nouns'][i] = None
for i, r in enumerate(c['rows']):
    for j, p in enumerate(r):
        if setp(f'rows[{i}][{j}].text', p, 'text'): v['rows'][i] = None
for i in range(len(c['story'])):
    if setp(f'story[{i}]', c['story'], i): v['story'][i] = None
for i in range(len(c['storyModels'])): setp(f'storyModels[{i}]', c['storyModels'], i)
for i, s in enumerate(c['scenes']):
    setp(f'scenes[{i}].scene', s, 'scene')
    for j in range(len(s['models'])): setp(f'scenes[{i}].models[{j}]', s['models'], j)
for i in range(len(c['captions'])): setp(f'captions[{i}]', c['captions'], i)
for n in c['mindMap']['nodes']:
    for k in ('caption', 'partner'): setp(f'mindMap.{k}', n, k)
assert 'ATV' not in json.dumps({k: c[k] for k in c if k != 'tr'}), 'ATV left in English'
json.dump(lab, open(APP, 'w'), ensure_ascii=False, indent=1)
json.dump(log, open(f'{HERE}/content/quad_changes.json', 'w'), ensure_ascii=False, indent=1)
print(len(log), 'changes')

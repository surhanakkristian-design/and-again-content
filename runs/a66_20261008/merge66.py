# A66 merge: new 7071 recordings into voices (read back by upload66.sh), the verified help translations (tr/<lang>.json),
# and storyPhrases (verify/phrases_recheck.json final) into ~/Projects/and-again-a66/lib/lab58.json.
# labExtras / labExercises: only the 7071 Turkish/other recall texts if a verifier changed them (A66: none).
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
APP = os.path.expanduser('~/Projects/and-again-a66/lib/lab58.json')
PUB = 'https://abyrutykpvmzkfbesire.supabase.co/storage/v1/object/public/audio/'
lab = json.load(open(APP)); by = {c['mediaId']: c for c in lab}
log = []
# 1. voices
log_up = open(f'{HERE}/upload/upload.log').read()
for m in [f'{HERE}/audio/{d}/manifest.json' for d in os.listdir(f'{HERE}/audio')]:
    man = json.load(open(m)); c = by[man['mediaId']]; v = c['voices']
    for it in man['items']:
        assert (f"up audio/{it['object']}" in log_up) or (f"there audio/{it['object']}" in log_up), it
        key = {'phrase': 'phrases', 'noun': 'nouns', 'story': 'story', 'row': 'rows'}[it['kind']]
        assert v[key][it['i'] - 1] is None, (key, it)
        v[key][it['i'] - 1] = PUB + it['object']; log.append(f"voice {man['mediaId']} {key}[{it['i']-1}] {it['file']}")
for c in lab:
    if c['mediaId'] == 461: continue
    for k, arr in c['voices'].items():
        if isinstance(arr, list): assert None not in arr, (c['mediaId'], k)
# 2. translations (7071)
c = by[7071]
for L in ['de', 'es', 'fr', 'sk', 'cz', 'ua', 'hu', 'tr']:
    t = json.load(open(f'{HERE}/tr/{L}.json')); tr = c['tr'][L]
    new = {('phrases', 2): t['phrases']['to ride a quad bike'], ('nouns', 2): t['nouns']['a quad bike'],
           ('rows', 1): t['rows']['to ride a quad bike']}
    for i in range(3): new[('story', i)] = t['story'][i]
    for (k, i), val in new.items():
        if tr[k][i] != val: log.append(f'tr {L} {k}[{i}]: {tr[k][i]} -> {val}'); tr[k][i] = val
# 3. storyPhrases
fin = json.load(open(f'{HERE}/verify/phrases_recheck.json'))
for sid, ps in fin.items():
    assert len(ps['final']) == 4, sid
    sp = [{'text': p['text'], 'match': p['match']} for p in ps['final']]
    for p in sp:
        assert p['match'] and all(alt and all(w == w.lower() and ' ' not in w for w in alt) for alt in p['match']), p
    c = by[int(sid)]
    c['storyPhrases'] = sp; log.append(f'storyPhrases {sid}')
assert all('storyPhrases' in c for c in lab if c['mediaId'] != 461)
json.dump(lab, open(APP, 'w'), ensure_ascii=False, indent=1)
json.dump(log, open(f'{HERE}/content/merge_log.json', 'w'), ensure_ascii=False, indent=1)
print('\n'.join(log))

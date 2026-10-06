# A58: builds the lab's content file ~/Projects/and-again-a58/lib/lab58.json from content/<id>.json (verified), the live
# regions, data/themes.json, data/scenes.json, the recordings (audio/<id>/manifest.json) and the help texts (tr/<lang>.json).
#   python3 build58.py [--out <path>]
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else os.path.expanduser('~/Projects/and-again-a58/lib/lab58.json')
IDS = [8055, 236, 7071, 8056, 461, 62, 8039]   # the lab wall's order of the noun videos
LANGS = ['de', 'fr', 'es', 'sk', 'cz', 'ua', 'tr', 'hu']
BASE = 'https://abyrutykpvmzkfbesire.supabase.co/storage/v1/object/public/audio/'
LIVE = {r['media_id']: r for r in json.load(open(f'{HERE}/data/live_rows.json'))}
THEMES = json.load(open(f'{HERE}/data/themes.json')); SC = json.load(open(f'{HERE}/data/scenes.json'))
TR = {l: json.load(open(f'{HERE}/tr/{l}.json'))['videos'] for l in LANGS}
def parts_of(phrase, verb, noun, gap):
    rest = phrase[3:]  # after "to "
    vi = rest.index(verb); ni = rest.index(noun, vi + len(verb))
    segs = [('pre', rest[:vi]), ('verb', verb), ('mid', rest[vi + len(verb):ni]), ('noun', noun), ('post', rest[ni + len(noun):])]
    parts = [{'text': 'to', 'plain': True}]
    for kind, text in segs:
        text = text.strip()
        if not text: continue
        part = {'text': text}
        if kind == gap: part['gap'] = True
        parts.append(part)
    assert ' '.join(p['text'] for p in parts) == phrase, (phrase, parts)
    return parts
out = []
for vid in IDS:
    c = json.load(open(f'{HERE}/content/{vid}.json')); src = json.load(open(f'{HERE}/data/{vid}.json'))
    verdict = open(f'{HERE}/verify/{vid}/VERDICT.md').readline().strip()
    assert verdict in ('PASS', 'FIXED'), (vid, verdict)
    man = json.load(open(f'{HERE}/audio/{vid}/manifest.json'))
    url = {(x['kind'], x['i']): BASE + x['object'] for x in man['items']}
    taps = []
    for t in c['taps']:
        k = t['keys']; keys = LIVE[vid]['taps'][int(k.split(':')[1]) - 1]['keys'] if isinstance(k, str) else k
        taps.append({'phrase': t['phrase'], 'target': t['target'], 'keys': keys})
    targets = {t['target'] for t in c['taps']}
    cut = not c['cutVerdict'].startswith('no cut')
    tapsOn = len(targets) >= 2 and not cut
    skip = None if tapsOn else ('a scene cut (' + c['cutVerdict'] + ')' if cut else 'one actor only (' + ', '.join(sorted(targets)) + ')')
    captions = [x['caption'] for x in src['en']['carousel']]
    item = {
        'mediaId': vid, 'theme': THEMES[str(vid)]['theme'], 'whiteShare': THEMES[str(vid)]['whiteShare'],
        'tapsOn': tapsOn, 'tapsSkip': skip, 'taps': taps,
        'nouns': [{'word': n['word'], 'correct': True, 'x': n['x'], 'y': n['y']} for n in c['nouns']],
        'rows': [parts_of(t['phrase'], t['verb'], t['noun'], f['gap']) for t, f in zip(c['taps'], c['fill'])],
        'mindMap': {'centre': re.sub(r'^(a|an|the|to) ', '', src['keyWord']['en']), 'nodes': [{'caption': m['caption'], 'partner': m['partner']} for m in c['mindMap']]},
        'story': c['story'], 'captions': captions,
        'voices': {'phrases': [url[('phrase', i + 1)] for i in range(3)], 'nouns': [url[('noun', i + 1)] for i in range(3)],
                   'captions': {cap: url[('caption', i + 1)] for i, cap in enumerate(captions)}, 'story': [url[('story', i + 1)] for i in range(len(c['story']))]},
        'tr': {l: {k: TR[l][str(vid)][k] for k in ('phrases', 'nouns', 'story')} for l in LANGS},
    }
    out.append(item)
json.dump(out, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, [(x['mediaId'], x['theme'], x['tapsOn'], x['tapsSkip']) for x in out])

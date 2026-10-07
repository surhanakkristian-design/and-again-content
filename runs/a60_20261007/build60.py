# A60: builds lib/lab58.json from the A59 file: the 6 shown noun videos get the rule-6 stories (story, voices.story, tr.*.story,
# level, pos); 461 stays as it is (hidden in the app); the two lab-only pilots (to select 900001, classical 900002) are added with
# their still picture, static tap regions, carousel (pictures + voices + native captions), timeline / mind map, recordings, help texts.
#   python3 build60.py <path to lib/lab58.json>
import json, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
PUB = 'https://abyrutykpvmzkfbesire.supabase.co/storage/v1/object/public'
LANGS = ['sk', 'cz', 'de', 'es', 'fr', 'hu', 'tr', 'ua']
path = sys.argv[1]
lab = json.load(open(path))
st = json.load(open(f'{HERE}/content/stories.json'))
tr = {l: json.load(open(f'{HERE}/tr/{l}.json')) for l in LANGS}
def audio(vid):
    m = json.load(open(f'{HERE}/audio/{vid}/manifest.json'))
    return {(x['kind'], x['i']): f"{PUB}/audio/{x['object']}" for x in m['items']}
LEVEL = {}
for entry in lab:
    vid = entry['mediaId']; k = str(vid)
    if k not in st: continue
    a = audio(vid)
    entry['story'] = st[k]['new']
    entry['voices']['story'] = [a[('story', i + 1)] for i in range(3)]
    for l in LANGS: entry['tr'][l]['story'] = tr[l]['nouns'][k]['story']
    entry['level'] = st[k]['level']; entry['pos'] = 'noun'
themes = json.load(open(f'{HERE}/content/themes.json'))
stills = json.load(open(f'{HERE}/upload/stills.json'))
car = json.load(open(f'{HERE}/upload/carousel.json'))
for vid, name in [(900001, 'select'), (900002, 'classical')]:
    c = json.load(open(f'{HERE}/content/{name}.json')); a = audio(vid)
    caps = [n['caption'] for n in c['fill4']['nodes']]
    box = lambda b: [{'t': 0, **b}, {'t': 1, **b}]
    pil = {l: tr[l]['pilots'][name] for l in LANGS}
    entry = {
        'mediaId': vid, 'theme': themes[name]['theme'], 'whiteShare': themes[name]['whiteShare'], 'tapsOn': True, 'tapsSkip': None,
        'taps': [{'phrase': t['phrase'], 'target': t['target'], 'keys': box(t['box'])} for t in c['taps']],
        'nouns': [{'word': n['word'], 'correct': True, 'x': n['x'], 'y': n['y']} for n in c['nouns']],
        'rows': c['rows'],
        'mindMap': {'centre': c['centre'], 'nodes': [{'caption': n['caption'], 'partner': n['partner']} for n in c['fill4']['nodes']], 'kind': c['fill4']['kind']},
        'story': st[name]['new'], 'captions': caps,
        'voices': {'phrases': [a[('phrase', i + 1)] for i in range(3)], 'nouns': [a[('noun', i + 1)] for i in range(3)],
                   'captions': {cap: a[('caption', i + 1)] for i, cap in enumerate(caps)}, 'story': [a[('story', i + 1)] for i in range(3)]},
        'tr': {l: {'phrases': pil[l]['phrases'], 'nouns': pil[l]['nouns'], 'story': pil[l]['story']} for l in LANGS},
        'level': c['level'], 'pos': c['pos'],
        'item': {'keyWord': c['keyWord'], 'level': c['level'], 'pictureUrl': f"{PUB}/Thumbnails/lab/a60/{stills[name + '_pic']}",
                 'thumbnailUrl': f"{PUB}/Thumbnails/lab/a60/{stills[name + '_thumb']}", 'aspect': stills[name + '_aspect'],
                 'carousel': {'pictures': [{'caption': cap, 'url': f"{PUB}/Thumbnails/lab/a60/{car[cap]}", 'voice': a[('caption', i + 1)]} for i, cap in enumerate(caps)]},
                 'captionsTr': {l: {cap: pil[l]['captions'][cap] for cap in caps} for l in LANGS}},
    }
    lab = [e for e in lab if e['mediaId'] != vid] + [entry]
json.dump(lab, open(path, 'w'), ensure_ascii=False, indent=1)
print('built', len(lab), 'entries')

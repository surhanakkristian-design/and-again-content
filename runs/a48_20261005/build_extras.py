# A48: builds the app's lib/labExtras.json (carousel + recall + native texts + recordings) from the run:
#   content/<id>.json (verified), tr/<lang>.json (verified), audio/manifest.json, pilot/accepted.json (the accepted
#   pictures: caption -> local PNG), and writes the carousel WebPs into upload/Thumbnails/lab/carousel/ (new names).
#   python3 build_extras.py <app checkout>
import json, os, sys, hashlib
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
APP = sys.argv[1]
BASE = 'https://abyrutykpvmzkfbesire.supabase.co/storage/v1/object/public'
IDS = [8055, 236, 624, 7071, 8056, 4265, 461, 62, 8039, 432]
LANGS = ['de', 'fr', 'es', 'sk', 'cz', 'ua', 'tr', 'hu']
SIZE = (720, 1280)  # the carousel size: 9:16, WebP
accepted = json.load(open(f'{HERE}/pilot/accepted.json')) if os.path.exists(f'{HERE}/pilot/accepted.json') else {}
manifest = json.load(open(f'{HERE}/audio/manifest.json'))
voice = {(m['mediaId'], m['kind'], m['text']): f"{BASE}/audio/{m['object']}" for m in manifest}
tr = {l: json.load(open(f'{HERE}/tr/{l}.json')) for l in LANGS}
lab = {v['mediaId']: v for v in json.load(open(f'{APP}/lib/labExercises.json'))}
out = {}
up = f'{HERE}/upload/Thumbnails/lab/carousel'; os.makedirs(up, exist_ok=True)
def webp(vid, caption, src):
    im = Image.open(src).convert('RGB')
    # cover-crop to 9:16, then the carousel size
    w, h = im.size; t = SIZE[0] / SIZE[1]
    if w / h > t: nw = round(h * t); im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
    else: nh = round(w / t); im = im.crop((0, (h - nh) // 2, w, (h - nh) // 2 + nh))
    im = im.resize(SIZE, Image.LANCZOS)
    slug = ''.join(c if c.isalnum() else '_' for c in caption.lower()).strip('_')
    key = lab[vid]['keyWord'].split()[-1]
    tmp = f'{up}/tmp.webp'; im.save(tmp, 'WEBP', quality=82, method=6)
    h8 = hashlib.sha1(open(tmp, 'rb').read()).hexdigest()[:8]
    name = f'{key}_{vid}_{slug}_{h8}_a48.webp'; os.replace(tmp, f'{up}/{name}')
    return f'{BASE}/Thumbnails/lab/carousel/{name}'
for vid in IDS:
    c = json.load(open(f'{HERE}/content/{vid}.json'))
    car = c['carousel']; pics = accepted.get(str(vid))
    carousel = None
    if pics:
        def item(x):
            cap = x['caption']
            return {'caption': cap, 'url': webp(vid, cap, pics[cap]), 'voice': voice.get((vid, 'caption', cap)), **({'original': True} if x.get('original') else {})}
        vert = car['vertical']; hor = car['horizontal']
        if car['originalIn'] == 'vertical':
            o = next(i for i, x in enumerate(vert) if x.get('original'))
            col = [item(x) for x in vert]; orig = col[o]
            row = [orig] + [item(x) for x in hor]
        else:
            o_h = next(i for i, x in enumerate(hor) if x.get('original'))
            orig = item(hor[o_h]); row = [orig] + [item(x) for i, x in enumerate(hor) if i != o_h]
            half = len(vert) // 2
            col = [item(x) for x in vert[:half]] + [orig] + [item(x) for x in vert[half:]]; o = half
        carousel = {'row': row, 'column': col, 'origin': o}
    entry = {'carousel': carousel, 'recall': c['recall'], 'tr': {}}
    if c.get('answerChanged'):
        entry['answer'] = c['answer']
        entry['answerVoice'] = voice.get((vid, 'answer', ' '.join(c['answer'])))
    for l in LANGS:
        t = tr[l][str(vid)]
        entry['tr'][l] = {'captions': t['captions'], 'recall': t['recall'], **({'answer': t['answer']} if 'answer' in t else {})}
    out[str(vid)] = entry
json.dump(out, open(f'{APP}/lib/labExtras.json', 'w'), ensure_ascii=False, indent=1)
print('written', sum(1 for v in out.values() if v['carousel']), 'carousels,', sum(len(v['recall']) for v in out.values()), 'recall rows')

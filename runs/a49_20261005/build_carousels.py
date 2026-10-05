# A49: adds the finished words' carousels to the app's lib/labExtras.json: the accepted pictures (pics/accepted.json:
# id -> caption -> local PNG; the original = the still) as 720 x 1280 WebPs under new names (upload/carousel/), with
# A48's caption recordings (already in storage). A dropped variant is left out of the carousel and of the recall rows.
#   python3 build_carousels.py <app checkout>
import json, os, sys, hashlib
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); APP = sys.argv[1]
A48 = os.path.expanduser('~/Projects/and-again-content/runs/a48_20261005')
BASE = 'https://abyrutykpvmzkfbesire.supabase.co/storage/v1/object/public'
SIZE = (720, 1280)
acc = json.load(open(f'{H}/pics/accepted.json'))
voice = {(m['mediaId'], m['text']): f"{BASE}/audio/{m['object']}" for m in json.load(open(f'{A48}/audio/manifest.json')) if m['kind'] == 'caption'}
lab = {v['mediaId']: v for v in json.load(open(f'{APP}/lib/labExercises.json'))}
ex = json.load(open(f'{APP}/lib/labExtras.json'))
up = f'{H}/upload/carousel/Thumbnails/lab/carousel'; os.makedirs(up, exist_ok=True)
def webp(vid, caption, src):
    im = Image.open(src).convert('RGB'); w, h = im.size; t = SIZE[0] / SIZE[1]
    if w / h > t: nw = round(h * t); im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
    else: nh = round(w / t); im = im.crop((0, (h - nh) // 2, w, (h - nh) // 2 + nh))
    im = im.resize(SIZE, Image.LANCZOS)
    slug = ''.join(c if c.isalnum() else '_' for c in caption.lower()).strip('_')
    key = lab[vid]['keyWord'].split()[-1]; tmp = f'{up}/tmp.webp'; im.save(tmp, 'WEBP', quality=82, method=6)
    h8 = hashlib.sha1(open(tmp, 'rb').read()).hexdigest()[:8]; name = f'{key}_{vid}_{slug}_{h8}_a49.webp'
    os.replace(tmp, f'{up}/{name}'); return f'{BASE}/Thumbnails/lab/carousel/{name}'
done = []
for sid, pics in acc.items():
    vid = int(sid); c = json.load(open(f'{A48}/content/{vid}.json')); car = c['carousel']
    item = lambda x: {'caption': x['caption'], 'url': webp(vid, x['caption'], pics[x['caption']]), 'voice': voice[(vid, x['caption'])], **({'original': True} if x.get('original') else {})}
    keep = lambda xs: [x for x in xs if x['caption'] in pics]
    vert, hor = keep(car['vertical']), keep(car['horizontal'])
    if car['originalIn'] == 'vertical':
        col = [item(x) for x in vert]; o = next(i for i, x in enumerate(vert) if x.get('original'))
        row = [col[o]] + [item(x) for x in hor]
    else:
        oh = next(x for x in hor if x.get('original')); orig = item(oh)
        row = [orig] + [item(x) for x in hor if not x.get('original')]
        half = len(vert) // 2; col = [item(x) for x in vert[:half]] + [orig] + [item(x) for x in vert[half:]]; o = half
    e = ex[sid]; e['carousel'] = {'row': row, 'column': col, 'origin': o}
    # recall rows of dropped variants go too (rows "from": "carousel" whose caption has no picture), with their native texts
    shown = {x['caption'] for x in row + col}
    capt = lambda r: ' '.join(p['text'] for p in r['parts'])
    keepidx = [i for i, r in enumerate(e['recall']) if r['from'] != 'carousel' or capt(r) in shown or any(capt(r) in s or s in capt(r) for s in shown)]
    if len(keepidx) != len(e['recall']):
        e['recall'] = [e['recall'][i] for i in keepidx]
        for l in e['tr']: e['tr'][l]['recall'] = [e['tr'][l]['recall'][i] for i in keepidx]
    done.append((vid, len(row) + len(col) - 1))
json.dump(ex, open(f'{APP}/lib/labExtras.json', 'w'), ensure_ascii=False, indent=1)
print('carousels added:', done)

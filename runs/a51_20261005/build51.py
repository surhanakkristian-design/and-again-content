# A51: writes the 3-picture carousels (decision 373) into the app's lib/labExtras.json and fixes 4265's French answer.
#   python3 build51.py <app checkout>
# FINAL.json: id -> [{caption, type, picture (local PNG or "url:<existing https url>"), voice (storage object)}];
# a word without exactly 3 valid pictures gets carousel null and loses its carousel recall rows and caption texts.
# Native captions: verify/out2_<lang>.json (+ OVERRIDE below). Recall rows: ROWS below (one per caption).
import json, os, sys, hashlib
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); APP = sys.argv[1]
BASE = 'https://abyrutykpvmzkfbesire.supabase.co/storage/v1/object/public'
LANGS = ['de', 'fr', 'es', 'sk', 'cz', 'ua', 'tr', 'hu']
FINAL = json.load(open(f'{H}/FINAL.json'))
NAT = {l: json.load(open(f'{H}/verify/out2_{l}.json'))['captions'] for l in LANGS}
OVERRIDE = {('tr', '432', 'to lead a horse'): 'bir atı yularından çekmek'}  # natural Turkish; key word not kept (open point)
T = lambda text, **kw: {'text': text, **kw}
G = lambda text, *alt: {'text': text, 'gap': True, 'accept': [text, *alt]}
TO = {'text': 'to', 'plain': True}
ROWS = {
 'young king': [G('young', 'old'), T('king')], 'king and queen': [T('king and'), G('queen')], 'to bow to the king': [TO, G('bow'), T('to the king')],
 'beach bag': [G('beach', 'sports'), T('bag')], 'sports bag': [G('sports', 'sport', 'beach'), T('bag')], 'to drop a bag': [TO, G('drop', 'carry'), T('a bag')],
 'to block the way': [TO, G('block'), T('the way')], 'narrow way': [G('narrow'), T('way')], 'to look for a way through': [TO, G('look'), T('for a way through')],
 'weight bench': [G('weight', 'park', 'picnic'), T('bench')], 'to paint a bench': [TO, G('paint', 'share'), T('a bench')], 'to share a bench': [TO, G('share', 'paint', 'sit on'), T('a bench')],
 'was leading knights to a castle': [T('was'), G('leading'), T('knights'), T('to a castle')], 'will be leading robots on Mars': [T('will be leading'), T('robots'), T('on'), G('Mars')], 'to lead a horse': [TO, T('lead'), T('a'), G('horse')],
 'shop-window mannequin': [G('shop-window', 'shop window'), T('mannequin')], 'to dress a mannequin': [TO, G('dress', 'carry'), T('a mannequin')], 'to carry a mannequin': [TO, G('carry', 'dress'), T('a mannequin')],
 'pod of dolphins': [G('pod'), T('of dolphins')], 'to swim with a dolphin': [TO, G('swim'), T('with a dolphin')], 'to feed a dolphin': [TO, G('feed'), T('a dolphin')],
 'was calmed by a knight': [T('was'), T('calmed'), T('by a'), G('knight')], 'to calm a barking dog': [TO, T('calm'), T('a'), G('barking'), T('dog')], 'to calm a crying baby': [TO, T('calm'), T('a'), G('crying'), T('baby')],
}
FR_OLD = 'en le serrant dans ses bras'; FR_NEW = 'en lui faisant un câlin'
lab = {v['mediaId']: v for v in json.load(open(f'{APP}/lib/labExercises.json'))}
ex = json.load(open(f'{APP}/lib/labExtras.json'))
up = f'{H}/upload/carousel/Thumbnails/lab/carousel'; os.makedirs(up, exist_ok=True)
def webp(vid, caption, src):
    im = Image.open(src).convert('RGB'); w, h = im.size; t = 720 / 1280
    if w / h > t: nw = round(h * t); im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
    else: nh = round(w / t); im = im.crop((0, (h - nh) // 2, w, (h - nh) // 2 + nh))
    im = im.resize((720, 1280), Image.LANCZOS); tmp = f'{up}/tmp.webp'; im.save(tmp, 'WEBP', quality=82, method=6)
    slug = ''.join(c if c.isalnum() else '_' for c in caption.lower()).strip('_'); key = lab[vid]['keyWord'].split()[-1]
    name = f'{key}_{vid}_{slug}_{hashlib.sha1(open(tmp, "rb").read()).hexdigest()[:8]}_a51.webp'
    os.replace(tmp, f'{up}/{name}'); return f'{BASE}/Thumbnails/lab/carousel/{name}'
report = {}
for sid, e in ex.items():
    vid = int(sid); items = FINAL.get(sid, [])
    keep_rows = [i for i, r in enumerate(e['recall']) if r['from'] != 'carousel']
    e['recall'] = [e['recall'][i] for i in keep_rows]
    for l in LANGS: e['tr'][l]['recall'] = [e['tr'][l]['recall'][i] for i in keep_rows]
    if len(items) != 3:
        e['carousel'] = None
        for l in LANGS: e['tr'][l]['captions'] = {}
        report[sid] = f'no carousel ({len(items)} valid pictures)'; continue
    pics = []
    for it in items:
        c = it['caption']; p = it['picture']
        url = p[4:] if p.startswith('url:') else webp(vid, c, p)
        pics.append({'caption': c, 'url': url, 'voice': f"{BASE}/audio/{it['voice']}"})
        e['recall'].append({'from': 'carousel', 'parts': ROWS[c]})
        assert ' '.join(x['text'] for x in ROWS[c]) == c, c
    e['carousel'] = {'pictures': pics}
    for l in LANGS:
        caps = {it['caption']: OVERRIDE.get((l, sid, it['caption']), NAT[l][sid][it['caption']]['native']) for it in items}
        e['tr'][l]['captions'] = caps
        e['tr'][l]['recall'] += [caps[it['caption']] for it in items]
    report[sid] = [it['caption'] for it in items]
# 4265: the French answer (decision: a parrot has wings) in both lab files
fr = ex['4265']['tr']['fr']; assert FR_OLD in fr['answer'] or FR_NEW in fr['answer']; fr['answer'] = fr['answer'].replace(FR_OLD, FR_NEW)
fr['recall'] = [x.replace(FR_OLD, FR_NEW) for x in fr['recall']]
json.dump(ex, open(f'{APP}/lib/labExtras.json', 'w'), ensure_ascii=False, indent=1)
s = open(f"{APP}/lib/labExercises.json").read(); o = "Il calme le perroquet en colère " + FR_OLD; s = s.replace(o, "Il calme le perroquet en colère " + FR_NEW) if o in s else s; open(f"{APP}/lib/labExercises.json", "w").write(s)
print(json.dumps(report, ensure_ascii=False, indent=1))

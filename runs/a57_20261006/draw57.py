# A57 (copy of A55 draw55.py): draws a video's tap regions (the ENGLISH keys, reused unchanged) with the phrases + targets of one
# language on every frame (verify/<lang>/<id>/box_NN.jpg) and its noun pills at the English slots on the still frame
# (verify/<lang>/<id>/slots.jpg; the still = frames/<id>/still.jpg, else the frame at the English still moment).
#   python3 draw57.py <lang> <id> [...]      lang = en (the source) | de | es | fr (content/<lang>/<id>.json)
import json, os, sys, glob
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__))
COL = [(255, 40, 40), (40, 220, 60), (60, 120, 255)]
def font(s):
    try: return ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', s)
    except Exception: return ImageFont.load_default()
def key(keys, t):
    for k in keys:
        if abs(k['t'] - t) < 0.01: return None if k.get('off') else k
    return None
def en_row(vid):
    p = f'{HERE}/src/en_rows/{vid}.json'
    if os.path.exists(p): return json.load(open(p))
    rows = {r['media_id']: r for r in json.load(open(f'{HERE}/src/sets_en.json'))}
    os.makedirs(f'{HERE}/src/en_rows', exist_ok=True)
    json.dump(rows[vid], open(p, 'w'))
    return rows[vid]
lang = sys.argv[1]
for vid in map(int, sys.argv[2:]):
    src = json.load(open(f'{HERE}/src/{vid}.json')); row = en_row(vid)
    c = src['en'] if lang == 'en' else json.load(open(f'{HERE}/content/{lang}/{vid}.json'))
    info = json.load(open(f'{HERE}/frames/{vid}/info.json'))
    out = f'{HERE}/verify/{lang}/{vid}'; os.makedirs(out, exist_ok=True)
    for f in glob.glob(f'{out}/box_*.jpg'): os.remove(f)
    tiles = []
    for t in info['times']:
        im = Image.open(f'{HERE}/frames/{vid}/f_{t:05.2f}.jpg').convert('RGB'); W, H = im.size
        dr = ImageDraw.Draw(im, 'RGBA')
        for i, tap in enumerate(c['taps']):
            k = key(row['taps'][i]['keys'], t)
            dr.rectangle([0, 18 + i * 20, W, 38 + i * 20], fill=(0, 0, 0, 170))
            dr.text((4, 20 + i * 20), f'{i + 1} {tap["phrase"]} -> {tap["target"]}' + ('' if k else '  (OFF)'), fill=COL[i] + (255,), font=font(15))
            if k: dr.rectangle([k['x'] * W + i * 3, k['y'] * H + i * 3, (k['x'] + k['w']) * W - i * 3, (k['y'] + k['h']) * H - i * 3], outline=COL[i] + (255,), width=3)
        tiles.append(im)
    W, H = tiles[0].size; per = 4
    for n in range(0, len(tiles), per):
        chunk = tiles[n:n + per]; rows = (len(chunk) + 1) // 2
        sheet = Image.new('RGB', (W * 2 + 6, H * rows + 6 * (rows - 1)), (255, 255, 255))
        for k, im in enumerate(chunk): sheet.paste(im, ((k % 2) * (W + 6), (k // 2) * (H + 6)))
        sheet.save(f'{out}/box_{n // per + 1:02d}.jpg', quality=80)
    sp = f'{HERE}/frames/{vid}/still.jpg'
    if not os.path.exists(sp): sp = f'{HERE}/frames/{vid}/f_{row["still_s"]:05.2f}.jpg'
    im = Image.open(sp).convert('RGB'); W, H = im.size
    dr = ImageDraw.Draw(im, 'RGBA')
    for n, slot in zip(c['nouns'], row['nouns']):
        tw = dr.textlength(n['word'], font=font(17)); pw, ph = tw + 22, 30
        cx = min(max(slot['x'] * W, pw / 2 + 2), W - pw / 2 - 2); cy = slot['y'] * H
        dr.rounded_rectangle([cx - pw / 2, cy - ph / 2, cx + pw / 2, cy + ph / 2], radius=15, fill=(255, 255, 255, 235), outline=(0, 0, 0, 255), width=2)
        dr.text((cx - tw / 2, cy - 10), n['word'], fill=(0, 0, 0, 255), font=font(17))
    im.save(f'{out}/slots.jpg', quality=85)
    print(f'{lang} {vid} ok: {(len(tiles) + per - 1) // per} box pictures + slots.jpg in verify/{lang}/{vid}/')

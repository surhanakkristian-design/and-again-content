# A45: checks content/<id>.json and draws the tap regions on the frames (verify/<id>/box_NN.jpg) and the noun slots on the
# still frame (verify/<id>/slots.jpg).   python3 draw.py <id> [...]
import json, os, sys, glob
from PIL import Image, ImageDraw, ImageFont
from validate import check
HERE = os.path.dirname(os.path.abspath(__file__))
COL = [(255, 40, 40), (40, 220, 60), (60, 120, 255)]
def font(s):
    try: return ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', s)
    except Exception: return ImageFont.load_default()
def key(tap, t):
    for k in tap['keys']:
        if abs(k['t'] - t) < 0.01: return None if k.get('off') else k
    return None
rc = 0
for vid in sys.argv[1:]:
    errors = check(vid, need_tr=False, need_audio=False)
    info = json.load(open(f'{HERE}/frames/{vid}/info.json'))
    c = None
    try: c = json.load(open(f'{HERE}/content/{vid}.json'))
    except Exception: pass
    if c and not any(abs(c.get('stillS', -1) - t) < 0.01 for t in info['times']): errors.append(f'stillS {c.get("stillS")} is not one of the frame times')
    if errors:
        print(f'{vid} ERROR:\n  ' + '\n  '.join(errors[:30])); rc = 1; continue
    taps = c['taps']; out = f'{HERE}/verify/{vid}'; os.makedirs(out, exist_ok=True)
    for f in glob.glob(f'{out}/box_*.jpg'): os.remove(f)
    tiles = []
    for t in info['times']:
        im = Image.open(f'{HERE}/frames/{vid}/f_{t:05.2f}.jpg').convert('RGB'); W, H = im.size
        dr = ImageDraw.Draw(im, 'RGBA')
        for i, tap in enumerate(taps):
            k = key(tap, t)
            dr.rectangle([0, 18 + i * 20, W, 38 + i * 20], fill=(0, 0, 0, 170))
            dr.text((4, 20 + i * 20), f'{i + 1} {tap["phrase"]} -> {tap["target"]}' + ('' if k else '  (OFF)'), fill=COL[i] + (255,), font=font(15))
            if not k: continue
            dr.rectangle([k['x'] * W + i * 3, k['y'] * H + i * 3, (k['x'] + k['w']) * W - i * 3, (k['y'] + k['h']) * H - i * 3], outline=COL[i] + (255,), width=3)
        tiles.append(im)
    W, H = tiles[0].size; per = 4 if H > W else 6
    for n in range(0, len(tiles), per):
        chunk = tiles[n:n + per]; rows = (len(chunk) + 1) // 2
        sheet = Image.new('RGB', (W * 2 + 6, H * rows + 6 * (rows - 1)), (255, 255, 255))
        for k, im in enumerate(chunk): sheet.paste(im, ((k % 2) * (W + 6), (k // 2) * (H + 6)))
        sheet.save(f'{out}/box_{n // per + 1:02d}.jpg', quality=80)
    im = Image.open(f'{HERE}/frames/{vid}/f_{c["stillS"]:05.2f}.jpg').convert('RGB'); W, H = im.size
    dr = ImageDraw.Draw(im, 'RGBA')
    for n in c['nouns']:
        tw = dr.textlength(n['word'], font=font(17)); pw, ph = tw + 22, 30
        cx = min(max(n['x'] * W, pw / 2 + 2), W - pw / 2 - 2); cy = n['y'] * H
        dr.rounded_rectangle([cx - pw / 2, cy - ph / 2, cx + pw / 2, cy + ph / 2], radius=15, fill=(255, 255, 255, 235), outline=(0, 0, 0, 255), width=2)
        dr.text((cx - tw / 2, cy - 10), n['word'], fill=(0, 0, 0, 255), font=font(17))
    im.save(f'{out}/slots.jpg', quality=85)
    print(f'{vid} ok: {len(tiles)} frames -> {(len(tiles) + per - 1) // per} box pictures + slots.jpg in verify/{vid}/')
sys.exit(rc)

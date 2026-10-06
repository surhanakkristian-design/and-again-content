# A59 (A58 + the second doer's region, dashed look: thinner box with 'also'): draws content/<id>.json's tap regions + phrases on every frame (verify/<id>/box_NN.jpg) and its noun pills at their
# slots on the still (verify/<id>/slots.jpg). python3 draw58.py <id>...
import json, os, sys, glob, re
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); FR = os.path.expanduser('~/Projects/and-again-content/runs/a55_20261005/frames')
LIVE = {r['media_id']: r for r in json.load(open(f'{HERE}/data/live_rows.json'))}
COL = [(255, 40, 40), (40, 220, 60), (60, 120, 255)]
def font(s): return ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', s)
def keys_of(vid, k):
    if isinstance(k, str): return LIVE[vid]['taps'][int(k.split(':')[1]) - 1]['keys']
    return k
def region(keys, t):
    before, after = keys[0], None
    for k in keys:
        if k['t'] <= t + 1e-6: before = k
        else: after = k; break
    if before.get('off'): return None
    b = dict(x=before['x'], y=before['y'], w=before['w'], h=before['h'])
    if not after or after.get('off') or t <= before['t']: return b
    s = (t - before['t']) / (after['t'] - before['t'])
    return {q: b[q] + (after[q] - b[q]) * s for q in b}
for vid in map(int, sys.argv[1:]):
    c = json.load(open(f'{HERE}/content/{vid}.json')); info = json.load(open(f'{FR}/{vid}/info.json'))
    out = f'{HERE}/verify/{vid}'; os.makedirs(out, exist_ok=True)
    for f in glob.glob(f'{out}/box_*.jpg'): os.remove(f)
    tiles = []
    for t in info['times']:
        im = Image.open(f'{FR}/{vid}/f_{t:05.2f}.jpg').convert('RGB'); W, H = im.size; dr = ImageDraw.Draw(im, 'RGBA')
        for i, tap in enumerate(c['taps']):
            r = region(keys_of(vid, tap['keys']), t)
            dr.rectangle([0, 30 + i * 20, W, 50 + i * 20], fill=(0, 0, 0, 170))
            dr.text((4, 32 + i * 20), f'{i + 1} {tap["phrase"]} -> {tap["target"]}' + ('' if r else '  (OFF)'), fill=COL[i] + (255,), font=font(15))
            if r: dr.rectangle([r['x'] * W + i * 3, r['y'] * H + i * 3, (r['x'] + r['w']) * W - i * 3, (r['y'] + r['h']) * H - i * 3], outline=COL[i] + (255,), width=3)
            if 'alsoKeys' in tap:
                r2 = region(keys_of(vid, tap['alsoKeys']), t)
                if r2:
                    dr.rectangle([r2['x'] * W + i * 3, r2['y'] * H + i * 3, (r2['x'] + r2['w']) * W - i * 3, (r2['y'] + r2['h']) * H - i * 3], outline=COL[i] + (255,), width=1)
                    dr.text((r2['x'] * W + 4, r2['y'] * H + 4), f'{i + 1} also', fill=COL[i] + (255,), font=font(13))
        tiles.append(im)
    W, H = tiles[0].size; per = 4
    for n in range(0, len(tiles), per):
        chunk = tiles[n:n + per]; rows = (len(chunk) + 1) // 2
        sheet = Image.new('RGB', (W * 2 + 6, H * rows + 6 * (rows - 1)), (255, 255, 255))
        for k, im in enumerate(chunk): sheet.paste(im, ((k % 2) * (W + 6), (k // 2) * (H + 6)))
        sheet.save(f'{out}/box_{n // per + 1:02d}.jpg', quality=80)
    im = Image.open(f'{FR}/{vid}/still.jpg').convert('RGB'); W, H = im.size; dr = ImageDraw.Draw(im, 'RGBA')
    for n in c['nouns']:
        tw = dr.textlength(n['word'], font=font(17)); pw, ph = tw + 22, 30
        cx = min(max(n['x'] * W, pw / 2 + 2), W - pw / 2 - 2); cy = n['y'] * H
        dr.rounded_rectangle([cx - pw / 2, cy - ph / 2, cx + pw / 2, cy + ph / 2], radius=15, fill=(255, 255, 255, 235), outline=(0, 0, 0, 255), width=2)
        dr.text((cx - tw / 2, cy - 10), n['word'], fill=(0, 0, 0, 255), font=font(17))
    im.save(f'{out}/slots.jpg', quality=85)
    print(f'{vid} ok: {(len(tiles) + per - 1) // per} box pictures + slots.jpg in verify/{vid}/')

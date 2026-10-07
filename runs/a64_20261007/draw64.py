"""A64: exercise 2's still at 390x844 and 375x667 (cover-fit box as the lab draws it) with the protected zones (red),
the object points (yellow dots) and the slots (cyan boxes). python3 draw64.py zones/<file>.json <outdir>"""
import json, subprocess, sys, os, urllib.request
from PIL import Image, ImageDraw

LAB = os.path.expanduser('~/Projects/and-again-a64/lib')
videos = json.load(open(f'{LAB}/labExercises.json'))
videos = videos if isinstance(videos, list) else list(videos.values())
vid = {v['mediaId']: v for v in videos if isinstance(v, dict) and 'mediaId' in v}
items = {e['mediaId']: e for e in json.load(open(f'{LAB}/lab58.json'))}

def still(mid):
    path = f'stills/{mid}.png'
    if os.path.exists(path):
        return Image.open(path).convert('RGB')
    if items[mid].get('item'):
        raw = f'stills/{mid}.webp'
        urllib.request.urlretrieve(items[mid]['item']['pictureUrl'], raw)
        Image.open(raw).convert('RGB').save(path)
    else:
        v = vid[mid]
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(v.get('stillS') or 0), '-i', v['mediaUrl'], '-frames:v', '1', path], check=True, timeout=120)
    return Image.open(path).convert('RGB')

data = json.load(open(sys.argv[1]))
outdir = sys.argv[2]
os.makedirs(outdir, exist_ok=True)
for entry in data:
    mid = entry['mediaId']
    pic = still(mid)
    W, H = pic.size
    aspect = entry['aspect']
    panels = []
    for win in entry['windows']:
        box = win['box']
        bw, bh = box['width'], box['height']
        ba = bw / bh
        if ba >= aspect:
            share = aspect / ba; x0, x1, y0, y1 = 0, 1, (1 - share) / 2, (1 + share) / 2
        else:
            share = ba / aspect; x0, x1, y0, y1 = (1 - share) / 2, (1 + share) / 2, 0, 1
        crop = pic.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H))).resize((int(bw), int(bh)))
        # the title strip above the box (title zone reaches into the box's top)
        top = 61
        canvas = Image.new('RGB', (int(bw), int(bh) + top), (255, 255, 255))
        canvas.paste(crop, (0, top))
        d = ImageDraw.Draw(canvas, 'RGBA')
        for z in win['zones']:
            r = z['rect']
            d.rectangle([r['left'], r['top'] + top, r['left'] + r['width'], r['top'] + r['height'] + top], fill=(255, 0, 0, 70), outline=(255, 0, 0, 255), width=2)
            d.text((r['left'] + 4, r['top'] + top + 4), z['name'], fill=(255, 255, 255, 255))
        for i, (t, s) in enumerate(zip(win['targets'], win['rects'])):
            d.rectangle([s['left'], s['top'] + top, s['left'] + s['width'], s['top'] + s['height'] + top], outline=(0, 255, 255, 255), width=3)
            d.text((s['left'] + 6, s['top'] + top + 14), win['words'][i], fill=(0, 255, 255, 255))
            d.ellipse([t['x'] - 7, t['y'] + top - 7, t['x'] + 7, t['y'] + top + 7], fill=(255, 230, 0, 255), outline=(0, 0, 0, 255))
            d.text((t['x'] + 9, t['y'] + top - 6), str(i + 1), fill=(255, 230, 0, 255))
        panels.append(canvas)
    sheet = Image.new('RGB', (sum(p.width for p in panels) + 20, max(p.height for p in panels)), (40, 40, 40))
    x = 0
    for p in panels:
        sheet.paste(p, (x, 0)); x += p.width + 20
    sheet.save(f'{outdir}/{mid}.jpg', quality=85)
    print(mid, 'problems:', entry['problems'] or 'none')

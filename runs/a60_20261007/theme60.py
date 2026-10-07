# A60: the theme of a lab-only still picture, the same rule as A58 theme.py (one frame = the picture).
import json, sys
from PIL import Image
LIGHT, SPREAD, BAND, LIMIT = 225, 30, 0.06, 0.80
out = {}
for name in sys.argv[1:]:
    im = Image.open(f'pics/{name}.png').convert('RGB'); im = im.resize((180, round(180 * im.height / im.width))); w, h = im.size; px = im.load()
    bx, by = max(1, round(w * BAND)), max(1, round(h * BAND)); light = total = 0
    for y in range(h):
        for x in range(w):
            if bx <= x < w - bx and by <= y < h - by: continue
            r, g, b = px[x, y]; total += 1
            if 0.299 * r + 0.587 * g + 0.114 * b >= LIGHT and max(r, g, b) - min(r, g, b) <= SPREAD: light += 1
    share = light / total
    out[name] = {'whiteShare': round(share, 3), 'theme': 'white' if share >= LIMIT else 'dark'}
    print(name, out[name])
json.dump(out, open('content/themes.json', 'w'), indent=1)

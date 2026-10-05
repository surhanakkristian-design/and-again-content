# A49: one contact sheet per word (every kept picture, its caption, blind score x/3, UNSURE / owner notes).
#   python3 contact_sheets.py <out dir>   (reads final_sets.json, blind/<id>_f<r>_key.json, blind/final_f<r>_answer.md, notes.json)
import json, os, re, sys
from PIL import Image, ImageDraw, ImageFont
P = os.path.dirname(os.path.abspath(__file__)); OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
S = json.load(open(f'{P}/final_sets.json')); notes = json.load(open(f'{P}/notes.json')) if os.path.exists(f'{P}/notes.json') else {}
def picks(r):
    t = open(f'{P}/blind/final_{r}_answer.md').read(); out = {}; cur = None
    for line in t.split('\n'):
        m = re.search(r'\b(62|236|432|461|624|4265|7071|8039|8055|8056)\b', line) if not line.startswith('|') else None
        if m: cur = m.group(1)
        if line.startswith('|') and cur:
            cells = [c.strip().strip('"*') for c in line.strip('|').split('|')]
            n = re.search(r'\d+', cells[0] or '')
            if n and len(cells) > 1: out.setdefault(cur, {})[int(n.group())] = cells[1]
    return out
score = {}
for r in ('f1', 'f2', 'f3'):
    pk = picks(r)
    for vid in S:
        key = json.load(open(f'{P}/blind/{vid}_{r}_key.json'))
        for card, cap in key.items():
            got = pk.get(vid, {}).get(int(card), '')
            score.setdefault(vid, {}).setdefault(cap, 0)
            score[vid][cap] += int(got.lower() == cap.lower())
json.dump(score, open(f'{P}/blind_scores.json', 'w'), indent=1)
try: font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 22); small = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 17)
except Exception: font = small = ImageFont.load_default()
W, H = 300, 533
for vid, m in S.items():
    caps = list(m); sheet = Image.new('RGB', (W * len(caps) + 10 * (len(caps) + 1), H + 120), 'white'); d = ImageDraw.Draw(sheet)
    for i, cap in enumerate(caps):
        p = m[cap] if m[cap].startswith('/') else f'{P}/{m[cap]}'
        im = Image.open(p).convert('RGB'); im.thumbnail((W, H)); x = 10 + i * (W + 10)
        sheet.paste(im, (x, 10)); s = score[vid][cap]
        d.text((x, H + 18), cap, fill='black', font=font)
        mark = f'blind {s}/3' + ('' if s >= 2 else '  UNSURE')
        d.text((x, H + 48), mark, fill=('black' if s >= 2 else (200, 0, 0)), font=small)
        if cap in notes.get(vid, {}): d.text((x, H + 72), notes[vid][cap][:40], fill=(200, 0, 0), font=small)
    sheet.save(f'{OUT}/CONTACT_SHEET_{vid}.jpg', quality=85)
print(json.dumps(score))

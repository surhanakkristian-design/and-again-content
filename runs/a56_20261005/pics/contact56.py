# A56: one contact sheet per new word: the 3 kept pictures, caption, tense / collocation type, blind score x/3,
# UNSURE mark (decision 380) and where the picture comes from.   python3 contact56.py <out dir>
# Reads ../FINAL56.json and blind_scores.json (score.py).
import json, os, sys, urllib.request, io
from PIL import Image, ImageDraw, ImageFont
P = os.path.dirname(os.path.abspath(__file__)); OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
F = json.load(open(f'{P}/../FINAL56.json')); S = json.load(open(f'{P}/blind_scores.json'))
font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 21); small = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 17)
W, Hh = 300, 533
def load(p):
    if p.startswith('url:'): return Image.open(io.BytesIO(urllib.request.urlopen(p[4:], timeout=60).read())).convert('RGB')
    return Image.open(p).convert('RGB')
for vid in ['236', '62', '461', '4265', '624', '8055']:
    sheet = Image.new('RGB', (W * 3 + 40, Hh + 130), 'white'); d = ImageDraw.Draw(sheet)
    for i, it in enumerate(F[vid]):
        im = load(it['picture']); im.thumbnail((W, Hh)); x = 10 + i * (W + 10); sheet.paste(im, (x, 10))
        got, n = map(int, S.get(f"{vid}|{it['caption']}", '0/0').split('/'))
        unsure = n == 0 or got < 3
        d.text((x, Hh + 18), it['caption'], fill='black', font=font)
        d.text((x, Hh + 46), it['type'], fill=(90, 90, 90), font=small)
        d.text((x, Hh + 70), f'blind {got}/{n}' + ('  UNSURE' if unsure else ''), fill=((200, 0, 0) if unsure else 'black'), font=small)
        d.text((x, Hh + 94), 'new (A56, 1 paid attempt)' if it['from'].startswith('A56') else 'reused (A49)', fill=(90, 90, 90), font=small)
    sheet.save(f'{OUT}/CONTACT_SHEET_{vid}.jpg', quality=85)
print('ok')

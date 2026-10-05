# A51: one contact sheet per word: the 3 kept pictures, each with its caption, tense / collocation type, blind score
# x/3 and UNSURE mark (decision 380).   python3 contact51.py <out dir>
# Reads ../FINAL.json and every blind round blind/<round>_answer.md with its blind/<id>_<round>_key.json.
import json, os, re, sys, glob, urllib.request, io
from PIL import Image, ImageDraw, ImageFont
P = os.path.dirname(os.path.abspath(__file__)); OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
F = json.load(open(f'{P}/../FINAL.json'))
score = {}
for ans in glob.glob(f'{P}/blind/*_answer.md'):
    r = os.path.basename(ans)[:-len('_answer.md')]; cur = None
    for line in open(ans).read().split('\n'):
        m = re.match(r'##\s*word\s*(\d+)', line)
        if m: cur = m.group(1); key = json.load(open(f'{P}/blind/{cur}_{r}_key.json')); continue
        if line.startswith('|') and cur:
            c = [x.strip().strip('"*') for x in line.strip('|').split('|')]; n = re.search(r'\d+', c[0])
            if n and len(c) > 1 and n.group() in key:
                s = score.setdefault(cur, {}).setdefault(key[n.group()], [0, 0]); s[1] += 1; s[0] += int(c[1].lower() == key[n.group()].lower())
json.dump(score, open(f'{P}/blind_scores.json', 'w'), indent=1)
font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 21); small = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 17)
W, Hh = 300, 533
def load(p):
    if p.startswith('url:'): return Image.open(io.BytesIO(urllib.request.urlopen(p[4:], timeout=60).read())).convert('RGB')
    return Image.open(p).convert('RGB')
for vid, items in F.items():
    sheet = Image.new('RGB', (W * 3 + 40, Hh + 130), 'white'); d = ImageDraw.Draw(sheet)
    for i, it in enumerate(items):
        im = load(it['picture']); im.thumbnail((W, Hh)); x = 10 + i * (W + 10); sheet.paste(im, (x, 10))
        got, n = score.get(vid, {}).get(it['caption'], [0, 0])
        d.text((x, Hh + 18), it['caption'], fill='black', font=font)
        d.text((x, Hh + 46), it['type'], fill=(90, 90, 90), font=small)
        unsure = n == 0 or got < 2
        d.text((x, Hh + 70), f'blind {got}/{n}' + ('  UNSURE' if unsure else ''), fill=((200, 0, 0) if unsure else 'black'), font=small)
        if it.get('note'): d.text((x, Hh + 94), it['note'][:42], fill=(200, 0, 0), font=small)
    sheet.save(f'{OUT}/CONTACT_SHEET_{vid}.jpg', quality=85)
print(json.dumps(score))

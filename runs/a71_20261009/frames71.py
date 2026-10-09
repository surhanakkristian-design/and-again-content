# A71 (owner brief part 2): dense frames of every lab item for the writer and the separate video verifier.
#   python3 frames71.py            -> media/<id>.<ext>, frames/<id>/f_<t>.jpg (4 per second over the WHOLE clip),
#                                     sheets/<id>_<n>.jpg (12 frames each, time stamped, the CURRENT tap regions drawn:
#                                     P1 red, P2 blue, P3 yellow, a second doer dashed), sheets/<id>_nouns.jpg (the noun
#                                     points of exercise 2 on the still), carousel/<id>_<i>.jpg (each carousel picture)
#   python3 frames71.py --plain    -> the same sheets without regions (sheets_plain/)
import json, os, subprocess, sys, urllib.request
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__))
LAB = '/Users/kristiansurhanak/Projects/and-again/lib/lab58.json'
MEDIA = json.load(open(f'{HERE}/media.json'))
FPS = 4
PLAIN = '--plain' in sys.argv
lab = {c['mediaId']: c for c in json.load(open(LAB))}
try:
    FONT = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 22)
    SMALL = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 16)
except OSError:
    FONT = SMALL = ImageFont.load_default()
COL = ['#ff2d2d', '#2d8cff', '#ffd400']

def get(url, out):
    if not os.path.exists(out):
        urllib.request.urlretrieve(url, out)
    return out

def region_at(keys, t):
    before, after = keys[0], None
    for k in keys:
        if k['t'] <= t: before = k
        else: after = k; break
    if before.get('off'): return None
    if after is None or after.get('off') or t <= before['t']: return before
    s = (t - before['t']) / (after['t'] - before['t'])
    return {q: before[q] + (after[q] - before[q]) * s for q in 'xywh'}

def draw_regions(img, c, t):
    d = ImageDraw.Draw(img)
    W, H = img.size
    for i, tap in enumerate(c['taps']):
        for j, keys in enumerate([tap['keys']] + ([tap['alsoKeys']] if tap.get('alsoKeys') else [])):
            if isinstance(keys, str): continue
            r = region_at(keys, t)
            if not r: continue
            box = [r['x'] * W, r['y'] * H, (r['x'] + r['w']) * W, (r['y'] + r['h']) * H]
            d.rectangle(box, outline=COL[i], width=4 if j == 0 else 2)
            d.text((box[0] + 4, box[1] + 2), f'P{i + 1}' + ('b' if j else ''), fill=COL[i], font=SMALL)

def sheet(frames, out, cols=4):
    w = 300
    tiles = []
    for t, f in frames:
        im = Image.open(f).convert('RGB')
        h = round(im.height * w / im.width)
        im = im.resize((w, h))
        ImageDraw.Draw(im).text((6, 4), f'{t:.2f}s', fill='white', font=FONT, stroke_width=3, stroke_fill='black')
        tiles.append(im)
    th = max(t.height for t in tiles)
    rows = (len(tiles) + cols - 1) // cols
    S = Image.new('RGB', (cols * w + (cols - 1) * 6, rows * th + (rows - 1) * 6), 'white')
    for k, im in enumerate(tiles):
        S.paste(im, ((k % cols) * (w + 6), (k // cols) * (th + 6)))
    S.save(out, quality=85)

def one(vid):
    m = MEDIA[str(vid)]
    c = lab[vid]
    os.makedirs(f'{HERE}/media', exist_ok=True)
    fdir = f'{HERE}/frames/{vid}'; os.makedirs(fdir, exist_ok=True)
    sdir = f'{HERE}/{"sheets_plain" if PLAIN else "sheets"}'; os.makedirs(sdir, exist_ok=True)
    cdir = f'{HERE}/carousel'; os.makedirs(cdir, exist_ok=True)
    for i, u in enumerate(m['pics']):
        p = get(u, f'{HERE}/media/{vid}_car{i}.webp')
        Image.open(p).convert('RGB').save(f'{cdir}/{vid}_{i}.jpg', quality=88)
    if m.get('video'):
        src = get(m['video'], f'{HERE}/media/{vid}.mp4')
        dur = float(subprocess.run(['ffprobe', '-v', '0', '-show_entries', 'format=duration', '-of', 'csv=p=0', src], capture_output=True, text=True, timeout=30).stdout)
        if not os.listdir(fdir):
            subprocess.run(['ffmpeg', '-v', 'error', '-i', src, '-vf', f'fps={FPS}', '-q:v', '3', f'{fdir}/f_%04d.jpg'], check=True, timeout=300)
        files = sorted(os.listdir(fdir))
        frames = [((k + 0.5) / FPS, f'{fdir}/{f}') for k, f in enumerate(files)]
    else:
        src = get(m['picture'], f'{HERE}/media/{vid}.webp')
        Image.open(src).convert('RGB').save(f'{fdir}/f_0001.jpg', quality=90)
        frames, dur = [(0.0, f'{fdir}/f_0001.jpg')], 0
    drawn = []
    for t, f in frames:
        if PLAIN:
            drawn.append((t, f)); continue
        im = Image.open(f).convert('RGB')
        draw_regions(im, c, t if m.get('video') else 0)
        g = f.replace('/f_', '/r_')
        im.save(g, quality=85)
        drawn.append((t, g))
    n = 0
    for k in range(0, len(drawn), 12):
        n += 1
        sheet(drawn[k:k + 12], f'{sdir}/{vid}_{n}.jpg')
    # exercise 2's noun points on the still (the first frame for a video at stillS is close enough for a place check)
    if not PLAIN:
        # exercise 2 shows the video's still at stillS (lib/labExercises.json): the points are judged on that frame
        still_s = next((x.get('stillS') for x in json.load(open('/Users/kristiansurhanak/Projects/and-again/lib/labExercises.json')) if x['mediaId'] == vid), None)
        if m.get('video') and still_s is not None:
            sf = f'{HERE}/still/{vid}.jpg'
            if not os.path.exists(sf):
                os.makedirs(f'{HERE}/still', exist_ok=True)
                subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(still_s), '-i', src, '-frames:v', '1', '-q:v', '3', sf], check=True, timeout=60)
            still = Image.open(sf).convert('RGB')
        else:
            still = Image.open(frames[0][1]).convert('RGB')
        d = ImageDraw.Draw(still)
        for i, noun in enumerate(c['nouns']):
            x, y = noun['x'] * still.width, noun['y'] * still.height
            d.ellipse([x - 14, y - 14, x + 14, y + 14], outline=COL[i], width=5)
            d.ellipse([x - 3, y - 3, x + 3, y + 3], fill=COL[i])
            d.text((x + 16, y - 10), noun['word'], fill=COL[i], font=FONT, stroke_width=3, stroke_fill='black')
        still.save(f'{sdir}/{vid}_nouns.jpg', quality=85)
    return f'{vid}: {round(dur, 2)} s, {len(frames)} frames, {n} sheets'

for vid in [8055, 236, 7071, 8056, 62, 8039, 900001, 900002]:
    print(one(vid))

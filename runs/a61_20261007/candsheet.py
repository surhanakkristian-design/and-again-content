# A61: one picture per clip with every candidate as a row of 6 frames:
#   A = 0.5 s before, B, C = the two frames before the change, | D = the frame of the change, E = the next one, F = 0.5 s after.
#   python3 candsheet.py <id> <out.jpg> <t1> [t2 ...]
import glob, json, os, subprocess, sys, tempfile, shutil
from PIL import Image, ImageDraw
from frames import clip, label
R = os.path.dirname(os.path.abspath(__file__))
i, out, times = sys.argv[1], sys.argv[2], [float(x) for x in sys.argv[3:]]
sc = json.load(open(f'{R}/scores/{i}.json')); fps = sc['fps'] or 24; ts = [x[0] for x in sc['s']]
p = clip(i); d = tempfile.mkdtemp()
subprocess.run(['ffmpeg', '-v', 'error', '-nostdin', '-i', p, '-vf', 'scale=150:-2', '-vsync', '0', f'{d}/%06d.png'], timeout=180)
files = sorted(glob.glob(f'{d}/*.png'))
rows = []
for n, t in enumerate(times):
    k = min(range(len(ts)), key=lambda j: abs(ts[j] - t)); h = int(round(fps * 0.5)); L = len(files) - 1
    idx = [max(0, k - h), max(0, k - 2), max(0, k - 1), k, min(L, k + 1), min(L, k + h)]
    ims = []
    for m, j in enumerate(idx):
        im = Image.open(files[min(j, L)]).convert('RGB'); label(im, f'{n + 1}{"ABCDEF"[m]} {ts[min(j, len(ts) - 1)]:.2f}'); ims.append(im)
    rows.append(ims)
W, H = rows[0][0].size
sheet = Image.new('RGB', (W * 6 + 30, len(rows) * (H + 8)), (255, 255, 255))
for r, ims in enumerate(rows):
    x = 0
    for m, im in enumerate(ims):
        sheet.paste(im, (x, r * (H + 8))); x += W + (30 if m == 2 else 0)
    ImageDraw.Draw(sheet).rectangle([W * 3 + 8, r * (H + 8), W * 3 + 22, r * (H + 8) + H], fill=(255, 0, 0))
sheet.save(out, quality=82)
shutil.rmtree(d)

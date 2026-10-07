# A61: pictures for the verifiers.
#   python3 frames.py strip <id> <t> <out.jpg>   6 frames around a candidate: t-0.5, t-2f, t-1f, t (the frame after the change), t+1f, t+0.5
#   python3 frames.py sheet <id> <out.jpg>       the whole clip, one frame every 1/3 s, 6 per row, numbered with their time
import json, os, subprocess, sys, tempfile, glob
from PIL import Image, ImageDraw
R = os.path.dirname(os.path.abspath(__file__))
os.makedirs(f'{R}/clips', exist_ok=True)
def clip(i):
    p = f'{R}/clips/{i}.mp4'
    if not os.path.exists(p):
        url = json.load(open(f'{R}/scores/{i}.json'))['url']
        part = f'{p}.{os.getpid()}.part'
        for _ in range(3):
            if os.path.exists(p): break
            if subprocess.run(['curl', '-sf', '--max-time', '120', '-o', part, url]).returncode == 0:
                os.replace(part, p); break
    return p
def grab(p, w):
    d = tempfile.mkdtemp()
    return d
def label(im, text):
    dr = ImageDraw.Draw(im); dr.rectangle([0, 0, 8 * len(text) + 6, 16], fill=(0, 0, 0)); dr.text((3, 2), text, fill=(255, 255, 0))
def frames_between(p, a, b, w):
    d = tempfile.mkdtemp()
    subprocess.run(['ffmpeg', '-v', 'error', '-nostdin', '-ss', str(max(0, a)), '-i', p, '-t', str(b - max(0, a)), '-vf', f'scale={w}:-2', '-vsync', '0', '-frame_pts', '1', f'{d}/%08d.png'], timeout=120)
    return d
if sys.argv[1] == 'strip':
    i, t, out = sys.argv[2], float(sys.argv[3]), sys.argv[4]
    sc = json.load(open(f'{R}/scores/{i}.json')); fps = sc['fps'] or 24
    ts = [x[0] for x in sc['s']]
    k = min(range(len(ts)), key=lambda j: abs(ts[j] - t))
    want = [ts[max(0, k - int(fps * 0.5))], ts[max(0, k - 2)], ts[max(0, k - 1)], ts[k], ts[min(len(ts) - 1, k + 1)], ts[min(len(ts) - 1, k + int(fps * 0.5))]]
    p = clip(i)
    # decode the clip once at small size and index frames by order (scores were taken frame by frame in the same order)
    d = tempfile.mkdtemp()
    subprocess.run(['ffmpeg', '-v', 'error', '-nostdin', '-i', p, '-vf', 'scale=200:-2', '-vsync', '0', f'{d}/%06d.png'], timeout=180)
    files = sorted(glob.glob(f'{d}/*.png'))
    idx = [max(0, k - int(fps * 0.5)), max(0, k - 2), max(0, k - 1), k, min(len(ts) - 1, k + 1), min(len(ts) - 1, k + int(fps * 0.5))]
    ims = []
    for n, (j, tt) in enumerate(zip(idx, want)):
        im = Image.open(files[min(j, len(files) - 1)]).convert('RGB')
        label(im, f'{"ABCDEF"[n]} {tt:.2f}s'); ims.append(im)
    W, H = ims[0].size
    sheet = Image.new('RGB', (W * 6 + 25, H), (255, 255, 255))
    x = 0
    for n, im in enumerate(ims):
        sheet.paste(im, (x, 0)); x += W + (25 if n == 2 else 0)
    sheet.save(out, quality=85)
elif sys.argv[1] == 'sheet':
    i, out = sys.argv[2], sys.argv[3]
    p = clip(i)
    d = tempfile.mkdtemp()
    subprocess.run(['ffmpeg', '-v', 'error', '-nostdin', '-i', p, '-vf', 'fps=3,scale=120:-2', f'{d}/%04d.png'], timeout=180)
    files = sorted(glob.glob(f'{d}/*.png'))
    ims = []
    for n, f in enumerate(files):
        im = Image.open(f).convert('RGB'); label(im, f'{n / 3:.1f}'); ims.append(im)
    W, H = ims[0].size; cols = 6; rows = (len(ims) + cols - 1) // cols
    sheet = Image.new('RGB', (cols * (W + 4), rows * (H + 4)), (255, 255, 255))
    for n, im in enumerate(ims): sheet.paste(im, ((n % cols) * (W + 4), (n // cols) * (H + 4)))
    sheet.save(out, quality=85)
if sys.argv[1] == 'dense':
    # every frame between a and b (s), 8 per row, numbered with their time
    i, a, b, out = sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
    p = clip(i); d = tempfile.mkdtemp()
    subprocess.run(['ffmpeg', '-v', 'error', '-nostdin', '-i', p, '-vf', 'scale=120:-2', '-vsync', '0', '-frame_pts', '1', f'{d}/%08d.png'], timeout=180)
    sc = json.load(open(f'{R}/scores/{i}.json')); ts = [x[0] for x in sc['s']]
    files = sorted(glob.glob(f'{d}/*.png'))
    sel = [(ts[j], files[j]) for j in range(min(len(ts), len(files))) if a <= ts[j] <= b]
    ims = []
    for tt, f in sel:
        im = Image.open(f).convert('RGB'); label(im, f'{tt:.2f}'); ims.append(im)
    W, H = ims[0].size; cols = 8; rows = (len(ims) + cols - 1) // cols
    sheet = Image.new('RGB', (cols * (W + 4), rows * (H + 4)), (255, 255, 255))
    for n, im in enumerate(ims): sheet.paste(im, ((n % cols) * (W + 4), (n // cols) * (H + 4)))
    sheet.save(out, quality=85)

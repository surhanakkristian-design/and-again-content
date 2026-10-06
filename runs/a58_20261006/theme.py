# A58 (decision 3): the theme of a lab video from the picture's edges. Frames every 1 s; the edge band is the outer
# 6 % on all four sides; a pixel is "light" when its luminance >= 225 and its colour spread <= 30.
# whiteShare = the median over the frames of the band's light share. white theme when whiteShare >= 0.80 (plain light
# edges, content in the centre: SVG-style illustrations), else dark (content reaching the edges: photos, videos).
# The same rule is lib/lab58.ts themeOfEdges. python3 theme.py <id>... -> data/themes.json
import json, subprocess, sys, statistics
from PIL import Image
LIGHT, SPREAD, BAND, LIMIT = 225, 30, 0.06, 0.80
out = {}
for vid in sys.argv[1:]:
    p = f'video/{vid}.mp4'
    dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p], capture_output=True, text=True, timeout=60).stdout)
    shares = []
    t = 0.2
    while t < dur - 0.1 and len(shares) < 30:
        f = f'/tmp/a58_theme_{vid}.png'
        subprocess.run(['ffmpeg', '-v', '0', '-y', '-ss', str(t), '-i', p, '-frames:v', '1', '-vf', 'scale=180:-2', f], check=True, timeout=60)
        im = Image.open(f).convert('RGB'); w, h = im.size; px = im.load()
        bx, by = max(1, round(w * BAND)), max(1, round(h * BAND))
        light = total = 0
        for y in range(h):
            for x in range(w):
                if bx <= x < w - bx and by <= y < h - by: continue
                r, g, b = px[x, y]; total += 1
                if 0.299 * r + 0.587 * g + 0.114 * b >= LIGHT and max(r, g, b) - min(r, g, b) <= SPREAD: light += 1
        shares.append(light / total); t += 1.0
    share = statistics.median(shares)
    out[vid] = {'whiteShare': round(share, 3), 'frames': len(shares), 'theme': 'white' if share >= LIMIT else 'dark'}
    print(vid, out[vid])
json.dump(out, open('data/themes.json', 'w'), indent=1)

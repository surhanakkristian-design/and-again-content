# A45: frames of the given videos every 0.5 s with a 10 x 10 grid, 4 per sheet, + frames/<id>/info.json and packet.
#   python3 prep.py <id> [...]     (resumable: a video with info.json is skipped; the mp4 is deleted after the frames)
import json, subprocess, os, sys
from concurrent.futures import ThreadPoolExecutor
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__))
V = {int(x['id']): x for x in json.load(open(f'{HERE}/data/videos.json'))}
W = 450
def font(s):
    try: return ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', s)
    except Exception: return ImageFont.load_default()
def one(vid):
    d = f'{HERE}/frames/{vid}'
    if os.path.exists(f'{d}/info.json'): return f'{vid} skip'
    try:
        v = V[vid]; os.makedirs(d, exist_ok=True); path = f'{HERE}/video/{vid}.mp4'
        subprocess.run(['curl', '-s', '-f', '--max-time', '180', '-o', path, v['media_url']], check=True, timeout=200)
        p = subprocess.run(['ffprobe', '-v', '0', '-select_streams', 'v:0', '-show_entries', 'stream=width,height:format=duration', '-of', 'json', path], capture_output=True, text=True, timeout=60)
        j = json.loads(p.stdout); dur = float(j['format']['duration']); w = j['streams'][0]['width']; h = j['streams'][0]['height']
        H = round(W * h / w); start = float(v['start_s'] or 0)
        times = []; t = start
        while t < dur - 0.05 and len(times) < 40:
            times.append(round(t, 2)); t += 0.5
        tiles = []
        for t in times:
            out = f'{d}/f_{t:05.2f}.jpg'
            subprocess.run(['ffmpeg', '-v', '0', '-y', '-ss', str(t), '-i', path, '-frames:v', '1', '-vf', f'scale={W}:{H}', '-q:v', '3', out], check=True, timeout=60)
            im = Image.open(out).convert('RGB'); dr = ImageDraw.Draw(im, 'RGBA')
            for i in range(1, 10):
                x = W * i / 10; y = H * i / 10
                dr.line([(x, 0), (x, H)], fill=(255, 255, 0, 110), width=1); dr.line([(0, y), (W, y)], fill=(255, 255, 0, 110), width=1)
                dr.text((x + 2, 2), f'.{i}', fill=(255, 255, 0, 255), font=font(13)); dr.text((2, y + 1), f'.{i}', fill=(255, 255, 0, 255), font=font(13))
            dr.rectangle([0, H - 26, 110, H], fill=(0, 0, 0, 200)); dr.text((6, H - 23), f't = {t:.1f} s', fill=(255, 255, 255, 255), font=font(18))
            tiles.append(im)
        per = 4 if H > W else 6; cols = 2 if H > W else 2
        for n in range(0, len(tiles), per):
            chunk = tiles[n:n + per]; rows = (len(chunk) + cols - 1) // cols
            sheet = Image.new('RGB', (W * cols + 6 * (cols - 1), H * rows + 6 * (rows - 1)), (255, 255, 255))
            for k, im in enumerate(chunk): sheet.paste(im, ((k % cols) * (W + 6), (k // cols) * (H + 6)))
            sheet.save(f'{d}/sheet_{n // per + 1:02d}.jpg', quality=80)
        word = v['word']; pos = v['part_of_speech']
        packet = {'mediaId': vid, 'keyWord': word, 'partOfSpeech': pos, 'level': v['level'], 'description': v['asset_description'], 'transcript': v['transcript'],
                  'duration': round(dur, 2), 'times': times, 'sheets': (len(tiles) + per - 1) // per, 'evenId': vid % 2 == 0}
        json.dump(packet, open(f'{d}/packet.json', 'w'), ensure_ascii=False, indent=1)
        json.dump({'duration': dur, 'width': w, 'height': h, 'times': times}, open(f'{d}/info.json', 'w'))
        os.remove(path)
        return f'{vid} {dur:.1f}s {w}x{h} {len(times)} frames'
    except Exception as x:
        return f'{vid} FAILED {x}'
ids = [int(x) for x in sys.argv[1:]]
with ThreadPoolExecutor(6) as ex:
    res = list(ex.map(one, ids))
bad = [r for r in res if 'FAILED' in r]
print(len(res) - len(bad), 'ok;', len(bad), 'failed', bad[:10])

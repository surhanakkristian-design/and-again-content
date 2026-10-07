# A61 part 1: ffmpeg scene score of every frame of every live video (the file the app plays: media.media_url).
# python3 scan.py [workers]  -> scores/<id>.json  {id, url, dur, fps, s: [[t, score], ...]}  (resumable)
import json, os, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
R = os.path.dirname(os.path.abspath(__file__))
rows = json.load(open(f'{R}/sets_media.json'))
if os.environ.get('REV'): rows = rows[::-1]
if os.environ.get('MID'): rows = rows[len(rows)//2:] + rows[:len(rows)//2]
def scan(r):
    out = f"{R}/scores/{r['media_id']}.json"
    if os.path.exists(out): return 'skip'
    url = r['media_url']
    for attempt in range(3):
        try:
            p = subprocess.run(['ffmpeg', '-hide_banner', '-nostdin', '-i', url, '-an', '-vf',
                                "scale=240:-2,select='gte(scene,0)',metadata=print:key=lavfi.scene_score", '-f', 'null', '-'],
                               capture_output=True, text=True, timeout=240)
        except subprocess.TimeoutExpired:
            continue
        s, t = [], None
        fps = None
        for line in p.stderr.splitlines():
            m = re.search(r'pts_time:([0-9.]+)', line)
            if m: t = float(m.group(1))
            m = re.search(r'scene_score=([0-9.]+)', line)
            if m and t is not None: s.append([round(t, 3), round(float(m.group(1)), 4)])
            if fps is None:
                m = re.search(r'Video:.* ([0-9.]+) fps', line)
                if m: fps = float(m.group(1))
        dur = re.search(r'Duration: (\d+):(\d+):([0-9.]+)', p.stderr)
        if p.returncode == 0 and s:
            d = int(dur.group(1)) * 3600 + int(dur.group(2)) * 60 + float(dur.group(3)) if dur else None
            json.dump({'id': r['media_id'], 'url': url, 'dur': d, 'fps': fps, 's': s}, open(out, 'w'))
            return 'ok'
    open(f'{R}/scan_errors.txt', 'a').write(f"{r['media_id']} {url} rc={p.returncode if 'p' in dir() else 'timeout'}\n")
    return 'err'
n = int(sys.argv[1]) if len(sys.argv) > 1 else 12
done = 0
with ThreadPoolExecutor(n) as ex:
    for res in ex.map(scan, rows):
        done += 1
        if done % 200 == 0: print(done, flush=True)
print('finished', done, flush=True)

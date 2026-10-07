# A61 part 1, second signal: metric.series (frame difference d, its ratio r to the motion around it, histogram distance h)
# for every live video, streamed from media_url.  python3 scan2.py [workers] -> metric/<id>.json {d, r, h} (resumable)
import json, os, sys, numpy as np
from concurrent.futures import ThreadPoolExecutor
import metric
R = os.path.dirname(os.path.abspath(__file__))
rows = json.load(open(f'{R}/sets_media.json'))
if os.environ.get('REV'): rows = rows[::-1]
if os.environ.get('MID'): rows = rows[len(rows)//2:] + rows[:len(rows)//2]
def one(r):
    out = f"{R}/metric/{r['media_id']}.json"
    if os.path.exists(out): return
    src = f"{R}/clips/{r['media_id']}.mp4"
    if not os.path.exists(src): src = r['media_url']
    for _ in range(3):
        try:
            d, h, rr = metric.series(src)
            if len(d) > 10:
                json.dump({'d': [round(float(x), 2) for x in d], 'r': [round(float(x), 2) for x in rr], 'h': [round(float(x), 4) for x in h]}, open(out, 'w')); return
        except Exception as e:
            err = str(e)
    open(f'{R}/scan2_errors.txt', 'a').write(f"{r['media_id']}\n")
n = int(sys.argv[1]) if len(sys.argv) > 1 else 16
with ThreadPoolExecutor(n) as ex: list(ex.map(one, rows))
print('finished', flush=True)

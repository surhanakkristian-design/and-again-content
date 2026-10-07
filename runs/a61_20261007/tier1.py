# A61 round 1: per clip, every scene-score peak >= 0.15 (cands.peaks, +-0.4 s), 6 rows per picture.
#   -> verify/r1/<id>_<n>.jpg and verify/r1/rows.json {picture: [[row, t, score], ...]}
import json, glob, os, subprocess
from concurrent.futures import ThreadPoolExecutor
from cands import peaks
os.makedirs('verify/r1', exist_ok=True)
jobs = []
for f in glob.glob('scores/*.json'):
    d = json.load(open(f)); p = peaks(d['s'], 0.15)
    for n in range(0, len(p), 6): jobs.append((d['id'], n // 6, p[n:n + 6]))
rows = {f'{i}_{n}.jpg': [[k + 1, t, s] for k, (t, s) in enumerate(ch)] for i, n, ch in jobs}
json.dump(rows, open('verify/r1/rows.json', 'w'))
def make(j):
    i, n, ch = j; out = f'verify/r1/{i}_{n}.jpg'
    if not os.path.exists(out): subprocess.run(['python3', 'candsheet.py', str(i), out] + [str(t) for t, s in ch], timeout=400)
if os.environ.get('REV'): jobs = jobs[::-1]
with ThreadPoolExecutor(10) as ex: list(ex.map(make, jobs))
print(len(jobs), 'pictures,', sum(len(c) for _, _, c in jobs), 'rows')

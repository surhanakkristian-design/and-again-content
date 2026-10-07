# A61 round 2 (the second signal and the lower score band): for every clip WITHOUT a cut confirmed in round 1,
# each frame that is a local peak (+-0.4 s) of either signal and passes
#   scene score >= 0.10   or   (r >= 3.0 and d >= 8)        (and was not a round-1 row)
# -> verify/r2/<id>_<n>.jpg, verify/r2/rows.json.   python3 tier2.py [--count]
import json, glob, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
ver = json.load(open('verify/verdicts.json')) if os.path.exists('verify/verdicts.json') else {}
r1 = json.load(open('verify/r1/rows.json'))
r1t = {}
for k, rows in r1.items():
    for row, t, s in rows: r1t.setdefault(k.split('_')[0], set()).add(t)
def cands(i):
    s = json.load(open(f'scores/{i}.json'))['s']; m = json.load(open(f'metric/{i}.json'))
    n = min(len(s), len(m['d'])); out = []
    for k in range(1, n):
        t, sc = s[k]; r, d = m['r'][k], m['d'][k]
        hit = sc >= 0.10 or (r >= 3.0 and d >= 8)
        if not hit: continue
        # local peak of the signal that fired, within +-0.4 s
        win = [j for j in range(1, n) if abs(s[j][0] - t) <= 0.4 and j != k]
        peak = (sc >= 0.10 and all(sc >= s[j][1] for j in win)) or (r >= 3.0 and d >= 8 and all(r >= m['r'][j] for j in win))
        if peak and not any(abs(t - u) <= 0.4 for u in r1t.get(str(i), ())): out.append([t, round(sc, 3)])
    return out
jobs = []
for f in sorted(glob.glob('scores/*.json')):
    i = int(f.split('/')[-1][:-5])
    if any(v == 'CUT' for v in ver.get(str(i), {}).values()): continue
    c = cands(i)
    for n in range(0, len(c), 6): jobs.append((i, n // 6, c[n:n + 6]))
print(len(jobs), 'pictures,', sum(len(c) for _, _, c in jobs), 'rows,', len({j[0] for j in jobs}), 'clips')
if '--count' in sys.argv: sys.exit()
os.makedirs('verify/r2', exist_ok=True)
json.dump({f'{i}_{n}.jpg': [[k + 1, t, s] for k, (t, s) in enumerate(ch)] for i, n, ch in jobs}, open('verify/r2/rows.json', 'w'))
def make(j):
    i, n, ch = j; out = f'verify/r2/{i}_{n}.jpg'
    if not os.path.exists(out): subprocess.run(['python3', 'candsheet.py', str(i), out] + [str(t) for t, s in ch], timeout=400)
with ThreadPoolExecutor(10) as ex: list(ex.map(make, jobs))

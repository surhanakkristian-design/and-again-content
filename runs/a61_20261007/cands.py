# A61: candidates per clip = local peaks of the scene score (the highest within +-0.4 s) at or above T.
#   python3 cands.py <T>  -> candidates.json {id: [[t, score], ...]} (clips without a candidate left out)
import json, glob, sys
T = float(sys.argv[1]) if __name__ == "__main__" else None
def peaks(s, T, win=0.4):
    out = []
    for i, (t, v) in enumerate(s):
        if i == 0 or v < T: continue
        if all(v >= w for (u, w) in s if abs(u - t) <= win and u != t): out.append([t, v])
    return out
if __name__ == '__main__':
    res = {}
    for f in glob.glob('scores/*.json'):
        d = json.load(open(f)); p = peaks(d['s'], T)
        if p: res[d['id']] = p
    json.dump(res, open('candidates.json', 'w'))
    print(len(res), 'clips,', sum(len(v) for v in res.values()), 'candidates at', T)

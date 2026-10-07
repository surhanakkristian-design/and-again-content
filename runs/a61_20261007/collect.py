# A61: collect row verdicts -> verify/verdicts.json {id: {t: verdict}}
import json, glob, re, sys
out = {}; bad = []
for D in ['verify/r1', 'verify/r2', 'verify/r3']:
    try: rows = json.load(open(f'{D}/rows.json'))
    except FileNotFoundError: continue
    for f in glob.glob(f'{D}/v_*.jsonl'):
        for l in open(f):
            l = l.strip()
            if not l: continue
            try: d = json.loads(l)
            except Exception: bad.append(l[:80]); continue
            item = d['item'].split('/')[-1]
            if item not in rows: bad.append(item); continue
            i = item.split('_')[0]
            for row, t, s in rows[item]:
                v = d['rows'].get(str(row))
                out.setdefault(i, {})[str(t)] = v
json.dump(out, open('verify/verdicts.json', 'w'))
from collections import Counter
print(len(out), 'clips', Counter(v for c in out.values() for v in c.values()), 'bad', bad[:5])

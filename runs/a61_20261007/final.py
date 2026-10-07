# A61: the final decision per clip -> final.json {id: [cut times]} and decisions.json (evidence per clip)
import json, glob, re, collections
v = json.load(open('verify/verdicts.json'))
ids = [str(r['media_id']) for r in json.load(open('sets_media.json'))]
times = collections.defaultdict(set); ev = collections.defaultdict(list); overturned = set()
for i, rows in v.items():
    for t, x in rows.items():
        if x == 'CUT': times[i].add(round(float(t), 2)); ev[i].append(f'row CUT {t}')
# Opus audit of the best CUT row of every clip below 0.3 (+ 40 above) and of the strong-signal NO clips
aj = {j[0]: j for j in json.load(open('verify/audit/jobs.json'))}
for i, d in json.load(open('verify/audit/verdicts.json')).items():
    if d['verdict'] in ('HARD', 'SOFT'):
        for t in d['times'][:1]: times[i].add(round(float(t), 2))
        ev[i].append(f"opus {d['verdict']} {d['times']}")
    elif aj[i][2] != 'doubtNO':
        times[i] = {t for t in times[i] if abs(t - round(aj[i][1], 2)) > 0.05}; overturned.add(i); ev[i].append(f'opus NONE at {aj[i][1]}')
# Opus dense on doubtful clips (round-2 left-overs, FN-sample claims)
jobs = json.load(open('verify/doubt2/jobs.json'))
for f in glob.glob('verify/doubt2/v_*.jsonl'):
    for l in open(f):
        if not l.strip(): continue
        d = json.loads(l); m = re.search(r'd_(\d+)_(\d+)', d['item']); n, i = int(m.group(1)), m.group(2)
        ev[i].append(f"opus-doubt {jobs[n][2]} {d['verdict']} {d['times']}")
        if d['verdict'] in ('HARD', 'SOFT'): times[i].add(round(float(d['times'][0]), 2))
# Opus dense of the tuning sample
for f in glob.glob('tune/dense2/verdicts_*.jsonl') + ['tune/dense_verdicts.jsonl']:
    for l in open(f):
        if not l.strip(): continue
        d = json.loads(l); m = re.search(r'dense_(\d+)', d['item']); i = m.group(1)
        if d['verdict'] in ('HARD', 'SOFT'): times[i].add(round(float(d['times'][0]), 2)); ev[i].append(f"opus-tune {d['verdict']} {d['times']}")
# Opus dense on the sweep claims (rounds d3: the first claim per clip, d4: the other claims)
for D in ['verify/d3', 'verify/d4']:
    try: jobs = json.load(open(f'{D}/jobs.json'))
    except FileNotFoundError: continue
    for f in glob.glob(f'{D}/v_*.jsonl'):
        for l in open(f):
            if not l.strip(): continue
            d = json.loads(l); m = re.search(r'd_(\d+)_(\d+)', d['item']); n, i = int(m.group(1)), m.group(2)
            ev[i].append(f"opus-sweep {d['verdict']} {d['times']}")
            if d['verdict'] in ('HARD', 'SOFT') and d['times']: times[i].add(round(float(d['times'][0]), 2))
for l in (open('verify/d4/sheets_extra.jsonl') if __import__('os').path.exists('verify/d4/sheets_extra.jsonl') else []):
    if l.strip():
        d = json.loads(l); i = re.search(r'sheet_(\d+)', d['item']).group(1); ev[i].append(f"opus-sheet {d['verdict']} {d.get('times')}")
        if d['verdict'] == 'CUT' and d.get('times'): times[i].add(round(float(d['times'][0]), 2))
final = {i: sorted(times[i]) for i in ids if times[i]}
# merge times closer than 0.15 s
for i, ts in final.items():
    out = []
    for t in ts:
        if not out or t - out[-1] > 0.15: out.append(t)
    final[i] = out
json.dump(final, open('final.json', 'w'), indent=0)
json.dump({i: ev[i] for i in ids if ev[i]}, open('decisions.json', 'w'), indent=0)
print('clips with a cut', len(final), 'of', len(ids), '| overturned best rows', len(overturned), '| overturned clips now clean', sorted(i for i in overturned if i not in final))

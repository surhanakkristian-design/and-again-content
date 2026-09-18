#!/usr/bin/env python3
"""Sum measured token usage (input, cache creation, cache read, output) from Claude Code transcripts.
usage: token_usage.py <session-dir-or-jsonl>... [--since ISO] [--until ISO] [--json out.json]
Each assistant message is counted once (deduped by message id). Subagent transcripts live in <session>/subagents/."""
import json, sys, glob, os, argparse
ap = argparse.ArgumentParser(); ap.add_argument('paths', nargs='+'); ap.add_argument('--since'); ap.add_argument('--until'); ap.add_argument('--json')
a = ap.parse_args()
files = []
for p in a.paths:
    if p.endswith('.jsonl'): files.append(p)
    else:
        files += glob.glob(os.path.join(p, '**', '*.jsonl'), recursive=True)
rows = []
for f in files:
    seen = set(); s = dict(file=os.path.relpath(f, os.path.dirname(a.paths[0].rstrip('/'))), model=set(), n=0, inp=0, cc=0, cr=0, out=0, first=None, last=None, desc=None)
    meta = f[:-6] + '.meta.json'
    if os.path.exists(meta):
        try: m = json.load(open(meta)); s['desc'] = m.get('description') or m.get('agentType')
        except Exception: pass
    for line in open(f, errors='replace'):
        try: e = json.loads(line)
        except Exception: continue
        if e.get('type') != 'assistant': continue
        msg = e.get('message') or {}; u = msg.get('usage'); ts = e.get('timestamp')
        if not u or not ts: continue
        if a.since and ts < a.since: continue
        if a.until and ts >= a.until: continue
        k = msg.get('id') or e.get('requestId') or e.get('uuid')
        if k in seen: continue
        seen.add(k)
        s['n'] += 1; s['model'].add(msg.get('model', '?'))
        s['inp'] += u.get('input_tokens', 0) or 0; s['cc'] += u.get('cache_creation_input_tokens', 0) or 0
        s['cr'] += u.get('cache_read_input_tokens', 0) or 0; s['out'] += u.get('output_tokens', 0) or 0
        s['first'] = min(filter(None, [s['first'], ts])); s['last'] = max(filter(None, [s['last'], ts]))
    if s['n']:
        s['model'] = ','.join(sorted(s['model'])); s['total'] = s['inp'] + s['cc'] + s['cr'] + s['out']; rows.append(s)
rows.sort(key=lambda r: r['first'])
T = {k: sum(r[k] for r in rows) for k in ('inp', 'cc', 'cr', 'out', 'total')}
for r in rows:
    print(f"{r['first'][11:19]}-{r['last'][11:19]} {r['model'][:22]:22} n={r['n']:4} in={r['inp']:>8} cc={r['cc']:>9} cr={r['cr']:>10} out={r['out']:>8} total={r['total']:>10} {r['desc'] or r['file']}")
print(f"TOTAL in={T['inp']} cc={T['cc']} cr={T['cr']} out={T['out']} total={T['total']}")
if a.json: json.dump(dict(rows=rows, total=T), open(a.json, 'w'), indent=1)

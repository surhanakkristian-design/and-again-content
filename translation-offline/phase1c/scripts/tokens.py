#!/usr/bin/env python3
"""Phase 1c §7 token accounting → phase1c/tokens.json. Same unit/method as phase1b/scripts/token_usage.py:
unit = input + cache creation + cache read + output, from Claude Code transcripts; assistant records deduped by message id
(fallback requestId, uuid). METHOD NOTE: a streamed message is written as several records with the same id; input/cache fields
are identical but output_tokens is only final in the LAST record (e.g. 7 → 11,204). Phase 1b kept the FIRST record, so its output
(and totals) are understated. Default here = max per field per message id ('corrected'); --method first reproduces Phase 1b.
Subagents are attributed by the [STEP: ...] tag at the start of their first user prompt.
  python3 phase1c/scripts/tokens.py [--session ID] [--out phase1c/tokens.json]
Re-run at the end (report agent) to finalise the partial measure/report transcripts."""
import json, glob, os, re, sys
from collections import defaultdict
args = sys.argv[1:]; opt = lambda n, d: args[args.index(n) + 1] if n in args else d
SID = opt('--session', 'd4aa7f1b-a2b6-4747-a41a-9af6aa32ab47')
BASE = os.path.expanduser('~/.claude/projects/-Users-kristiansurhanak-Meine-Ablage-And-Again')
OUT = opt('--out', 'phase1c/tokens.json')
METHOD = opt('--method', 'corrected')
C = ('input', 'cache_creation', 'cache_read', 'output')

def usage(path):
    seen, calls = {}, []
    for line in open(path, errors='replace'):
        try: e = json.loads(line)
        except Exception: continue
        if e.get('type') != 'assistant': continue
        m = e.get('message') or {}; u = m.get('usage')
        if not u: continue
        k = m.get('id') or e.get('requestId') or e.get('uuid')
        rec = {'ts': e.get('timestamp'), 'model': m.get('model'), 'input': u.get('input_tokens', 0) or 0,
               'cache_creation': u.get('cache_creation_input_tokens', 0) or 0, 'cache_read': u.get('cache_read_input_tokens', 0) or 0,
               'output': u.get('output_tokens', 0) or 0}
        if k in seen:
            if METHOD == 'corrected':
                for c in C: seen[k][c] = max(seen[k][c], rec[c])
            continue
        seen[k] = rec; calls.append(rec)
    return calls

def summarise(calls):
    s = {c: sum(x[c] for x in calls) for c in C}; s['total'] = sum(s.values()); s['calls'] = len(calls)
    s['startup_context'] = (calls[0]['input'] + calls[0]['cache_creation'] + calls[0]['cache_read']) if calls else 0
    s['models'] = sorted({x['model'] for x in calls if x['model']}); s['first'] = calls[0]['ts'] if calls else None; s['last'] = calls[-1]['ts'] if calls else None
    s['share_pct'] = {c: round(100 * s[c] / s['total'], 1) if s['total'] else 0 for c in C}
    return s

def step_of(path):
    for line in open(path, errors='replace'):
        try: e = json.loads(line)
        except Exception: continue
        if e.get('type') == 'user':
            c = e['message']['content']; t = c if isinstance(c, str) else ' '.join(x.get('text', '') for x in c if isinstance(x, dict))
            m = re.search(r'\[STEP:\s*([^\]]+)\]', t); return m.group(1).strip() if m else 'untagged'
    return 'untagged'

steps = defaultdict(list); files = defaultdict(list)
for f in sorted(glob.glob(os.path.join(BASE, SID, '**', '*.jsonl'), recursive=True)):
    st = step_of(f); cl = usage(f)
    steps[st].append(summarise(cl)); files[st].append(os.path.basename(f))
def merge(ss):
    if len(ss) == 1: return ss[0]
    m = {c: sum(s[c] for s in ss) for c in C + ('total', 'calls')}; m['agents'] = len(ss)
    m['startup_context'] = [s['startup_context'] for s in ss]; m['models'] = sorted({x for s in ss for x in s['models']})
    m['share_pct'] = {c: round(100 * m[c] / m['total'], 1) for c in C}; return m
per_step = {k: {**merge(v), 'transcripts': files[k]} for k, v in steps.items()}
main = summarise(usage(os.path.join(BASE, SID + '.jsonl')))
S, L = per_step.get('batchS'), per_step.get('batchL')
fv = None
if S and L:
    fv = {'arithmetic': 'v = (L - S) / 40 ; F = S - 20 v   (S = 20 sentences, L = 60 sentences)'}
    for c in C + ('total',):
        v = (L[c] - S[c]) / 40; F = S[c] - 20 * v
        fv[c] = {'S': S[c], 'L': L[c], 'v': round(v, 1), 'F': round(F, 1), 'show': f"v=({L[c]}-{S[c]})/40={v:.1f}; F={S[c]}-20*{v:.1f}={F:.1f}"}
    fv['compare_marginal_per_sentence'] = {'phase1c_v': round(fv['total']['v'], 1), 'phase1b': 11590, 'phase1': 21299}
units = {'review-syn': ('group', 164), 'review-lib': ('topic', 48), 'review-sample': ('sentence', 8)}
per_unit = {}
for st, (u, n) in units.items():
    if st in per_step: per_unit[f'{st} per {u}'] = {c: round(per_step[st][c] / n, 1) for c in C + ('total',)}
if 'review-lib' in per_step: per_unit['review-lib per item'] = {c: round(per_step['review-lib'][c] / 953, 1) for c in C + ('total',)}
if 'supp' in per_step:
    per_unit['supp per rejection (65)'] = {c: round(per_step['supp'][c] / 65, 1) for c in C + ('total',)}
    per_unit['supp per fix (52 really correct)'] = {c: round(per_step['supp'][c] / 52, 1) for c in C + ('total',)}
    per_unit['supp per effective fix (41 now accepted, in-sample)'] = {c: round(per_step['supp'][c] / 41, 1) for c in C + ('total',)}
tot = {c: main[c] + sum(s[c] for s in per_step.values()) for c in C + ('total', 'calls')}
tot['share_pct'] = {c: round(100 * tot[c] / tot['total'], 1) for c in C}
res = {'method': METHOD, 'note': 'Unit = input + cache_creation + cache_read + output from transcripts, deduped by message id (Phase 1b method). '
               'Transcripts still running when this was computed (measure, main) are partial — re-run at the end.',
       'session': SID, 'main_session': main, 'steps': per_step, 'F_v': fv, 'per_unit': per_unit, 'total_so_far': tot}
json.dump(res, open(OUT, 'w'), indent=1)
for k, s in sorted(per_step.items(), key=lambda x: str(x[1].get('first') or '')):
    print(f"{k:14} calls={s['calls']:4} in={s['input']:>7} cc={s['cache_creation']:>9} cr={s['cache_read']:>10} out={s['output']:>7} total={s['total']:>10} start={s['startup_context']}")
print(f"{'main':14} calls={main['calls']:4} in={main['input']:>7} cc={main['cache_creation']:>9} cr={main['cache_read']:>10} out={main['output']:>7} total={main['total']:>10} start={main['startup_context']}")
print('TOTAL', tot)
if fv: print('F/v total:', fv['total']['show'])

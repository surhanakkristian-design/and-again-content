#!/usr/bin/env python3
"""Task D — the D3 'empty reply' failure.

Part 1 (0 calls): timeline proof from the frozen phase1h ledger (aggregates only).
Part 2 (<=30 counted calls): one-variable-at-a-time prompt experiment on DEV items that
returned empty under P-C in 1h.  Model gemini-3.1-flash-lite, thinking off.
Only HTTP 200 counts toward the cap; 0/429/5xx are retried (max 5) and logged counted:false.
The API key is read inside this process and never printed or written.
"""
import json, os, re, sys, time, urllib.request, urllib.error, collections

ROOT = os.path.expanduser('~/Projects/and-again-content/translation-offline')
P1I = os.path.join(ROOT, 'phase1i')
TD = os.path.join(P1I, 'taskD')
sys.path.insert(0, P1I)
LEDGER = os.path.join(TD, 'calls.jsonl')
API = 'https://generativelanguage.googleapis.com/v1beta'
MODEL = 'gemini-3.1-flash-lite'
CAP = 30

# ---------------------------------------------------------------- part 1: timeline
rows = [json.loads(l) for l in open(os.path.join(ROOT, 'phase1h', 'calls.jsonl'))]
rows.sort(key=lambda r: r['ts'])
zero = [r for r in rows if r['http'] == 0]
first = min(r['ts'] for r in zero)
after = [r for r in rows if r['ts'] >= first]
before = [r for r in rows if r['ts'] < first]
tl = {
    'total_rows': len(rows),
    'http0_rows': len(zero),
    'http0_by_variant': dict(collections.Counter(r['variant'] for r in zero)),
    'raw_error_strings': dict(collections.Counter((r.get('raw') or '')[:120] for r in zero)),
    'rows_before_first_http0': len(before),
    'http0_before': sum(1 for r in before if r['http'] == 0),
    'rows_from_first_http0_on': len(after),
    'http0_from_first_on': sum(1 for r in after if r['http'] == 0),
    'non_http0_from_first_on': sum(1 for r in after if r['http'] != 0),
    'variants_from_first_on': dict(collections.Counter(r['variant'] for r in after)),
    'first_http0_ts': first,
    'last_ts': max(r['ts'] for r in rows),
    'outage_seconds': round(max(r['ts'] for r in rows) - first, 1),
    'pb_ts_range': [min(r['ts'] for r in rows if r['variant'] == 'P-B'),
                    max(r['ts'] for r in rows if r['variant'] == 'P-B')],
    'pc_ts_range': [min(r['ts'] for r in rows if r['variant'] == 'P-C'),
                    max(r['ts'] for r in rows if r['variant'] == 'P-C')],
    'pb_last_success_ts': max(r['ts'] for r in rows if r['variant'] == 'P-B' and r['http'] == 200),
    'pc_last_success_ts': max(r['ts'] for r in rows if r['variant'] == 'P-C' and r['http'] == 200),
}
json.dump(tl, open(os.path.join(TD, 'timeline.json'), 'w'), indent=1)
print('TIMELINE', json.dumps(tl, indent=1))

if '--calls' not in sys.argv:
    sys.exit(0)

# ---------------------------------------------------------------- key (never printed)
def load_key():
    p = os.path.expanduser('~/Projects/and-again/.env.local')
    for ln in open(p):
        m = re.match(r'\s*(?:export\s+)?GEMINI_API_KEY\s*=\s*["\']?([^"\'\s]+)', ln)
        if m:
            return m.group(1)
    print('STOP: GEMINI_API_KEY not found in ~/Projects/and-again/.env.local')
    sys.exit(3)

KEY = load_key()
def redact(s):
    return (s or '').replace(KEY, '<KEY>')

# ---------------------------------------------------------------- prompts
SYS = ("You judge English translations. Reply with exactly one word: SAME, TIP or DIFF. "
       "SAME = the learner sentence means the same as the reference and is correct English. "
       "TIP = same meaning and acceptable, but with a small slip. "
       "DIFF = different meaning, or not correct English. No explanation.")
GRAM = 'Practised grammar: %s — ALREADY VERIFIED as correct in this answer; judge meaning and vocabulary only.'
PC_LINE = ("The SLOVAK sentence is the ground truth and the English reference is only one valid rendering of "
           "it; judge the learner against the Slovak, not against the reference wording.")
PAD = ("Note for the grader: this task is part of a routine batch review of short school translation "
       "exercises; the sentences vary in length and topic and no other context is provided.")

def build(cond, it):
    """Returns (prompt_text, max_output).  One variable changed per condition off B."""
    sk = 'Slovak: ' + it['sk']
    ref = 'Reference English: ' + it['reference']
    lrn = 'Learner: ' + it['answer']
    gram = GRAM % it['topic']
    q = 'SAME, TIP or DIFF?'
    if cond == 'B':            # P-B exactly (baseline)
        return '\n'.join([sk, ref, lrn, gram, q]), 24
    if cond == 'C':            # P-C exactly (the shape blamed in 1h)
        return '\n'.join([sk, ref, lrn, gram, PC_LINE, q]), 24
    if cond == 'C_end':        # ordering: the extra line after the question
        return '\n'.join([sk, ref, lrn, gram, q, PC_LINE]), 24
    if cond == 'B_pad':        # length only: neutral padding instead of PC_LINE
        return '\n'.join([sk, ref, lrn, gram, PAD, q]), 24
    if cond == 'C_noSK':       # Slovak absent
        return '\n'.join([ref, lrn, gram, PC_LINE, q]), 24
    if cond == 'C_mo8':        # maxOutputTokens 8 instead of 24
        return '\n'.join([sk, ref, lrn, gram, PC_LINE, q]), 8
    raise ValueError(cond)

CONDS = ['B', 'C', 'C_end', 'B_pad', 'C_noSK', 'C_mo8']

# ---------------------------------------------------------------- items: DEV only
from loader import load_items
empty_ids = {r['item_id'] for r in rows
             if r['variant'] == 'P-C' and (r.get('reply') or '').strip() == ''}
dev = [r for r in load_items('dev') if r['item_id'] in empty_ids]
dev.sort(key=lambda r: r['item_id'])
# 4 items, spread over kind C / kind W
done = set()
if os.path.exists(LEDGER):
    done = {json.loads(l)['item_id'] for l in open(LEDGER)}
CAP = int(os.environ.get('TASKD_CAP', CAP))
nit = int(os.environ.get('TASKD_ITEMS', '4'))
pool = [r for r in dev if r['item_id'] not in done]
items = [r for r in pool if r['kind'] == 'C'][:nit] + [r for r in pool if r['kind'] == 'W'][:nit]
items = items[:nit]
print('DEV items empty under P-C: %d (C=%d W=%d); already done %d; using %d'
      % (len(dev), sum(1 for r in dev if r['kind'] == 'C'), sum(1 for r in dev if r['kind'] == 'W'),
         len(done), len(items)))

# ---------------------------------------------------------------- call
def http(body):
    data = json.dumps(body).encode()
    req = urllib.request.Request('%s/models/%s:generateContent' % (API, MODEL), data=data, method='POST')
    req.add_header('x-goog-api-key', KEY)
    req.add_header('Content-Type', 'application/json')
    t0 = time.monotonic()
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            raw = r.read().decode('utf-8', 'replace')
            st = r.status
    except urllib.error.HTTPError as e:
        raw, st = (e.read().decode('utf-8', 'replace') if e.fp else ''), e.code
    except Exception as e:
        return 0, None, redact('%s: %s' % (type(e).__name__, e)), int((time.monotonic() - t0) * 1000)
    ms = int((time.monotonic() - t0) * 1000)
    try:
        js = json.loads(raw)
    except Exception:
        js = None
    if st in (401, 403) or 'API_KEY_INVALID' in raw or 'API key not valid' in raw:
        print('STOP: auth failed (HTTP %s)' % st)
        sys.exit(4)
    return st, js, redact(raw), ms

def reply_of(js):
    """The empty-reply detector, exactly as a run script should implement it."""
    cands = (js or {}).get('candidates') or []
    txt = ''
    for c in cands:
        for p in ((c.get('content') or {}).get('parts') or []):
            txt += p.get('text', '') or ''
    fin = cands[0].get('finishReason') if cands else None
    empty = (not cands) or txt.strip() == ''
    m = re.search(r'\b(SAME|TIP|DIFF)\b', txt.upper())
    return txt.strip(), (m.group(1) if m else 'PARSE_FAIL'), fin, empty

used = 0
fh = open(LEDGER, 'a')
for it in items:
    for cond in CONDS:
        if used >= CAP:
            print('CAP reached, aborting'); break
        p, mo = build(cond, it)
        body = {'systemInstruction': {'parts': [{'text': SYS}]},
                'contents': [{'role': 'user', 'parts': [{'text': p}]}],
                'generationConfig': {'temperature': 0, 'maxOutputTokens': mo,
                                     'thinkingConfig': {'thinkingBudget': 0}}}
        for tryno in range(1, 6):
            st, js, raw, ms = http(body)
            counted = (st == 200)
            txt, verdict, fin, empty = reply_of(js) if counted else ('', 'NO_REPLY', None, None)
            u = (js or {}).get('usageMetadata') or {}
            rec = {'ts': time.time(), 'task': 'D', 'model': MODEL, 'condition': cond,
                   'item_id': it['item_id'], 'try': tryno, 'http': st, 'counted': counted,
                   'transport_error': (raw if st == 0 else None),
                   'verdict': verdict, 'reply': txt, 'empty_reply': empty, 'finish': fin,
                   'latency_ms': ms, 'max_output': mo, 'prompt_chars': len(p),
                   'thinking': {'thinkingBudget': 0},
                   'prompt_tokens': u.get('promptTokenCount'),
                   'candidates_tokens': u.get('candidatesTokenCount'),
                   'thoughts_tokens': u.get('thoughtsTokenCount'),
                   'raw_json': js if counted else None,
                   'raw_error': (raw[:400] if not counted else None)}
            fh.write(json.dumps(rec, ensure_ascii=False) + '\n'); fh.flush()
            if counted:
                used += 1
                print('%-7s %-22s http200 empty=%s finish=%s verdict=%s ptok=%s' %
                      (cond, it['item_id'], empty, fin, verdict, u.get('promptTokenCount')))
                break
            print('%-7s %-22s http=%s try %d/5 -> backoff (NOT counted)' % (cond, it['item_id'], st, tryno))
            time.sleep(min(2 ** tryno, 16))
        time.sleep(0.15)
fh.close()
print('COUNTED MODEL CALLS USED: %d of %d' % (used, CAP))

# ---------------------------------------------------------------- summary table
recs = [json.loads(l) for l in open(LEDGER) if '"task": "D"' in l]
ok = [r for r in recs if r['counted']]
tab = {}
for c in CONDS:
    g = [r for r in ok if r['condition'] == c]
    tab[c] = {'n': len(g), 'empty': sum(1 for r in g if r['empty_reply']),
              'finish': dict(collections.Counter(r['finish'] for r in g)),
              'verdicts': dict(collections.Counter(r['verdict'] for r in g)),
              'prompt_tokens': sorted({r['prompt_tokens'] for r in g})}
tab['_transport_retries_not_counted'] = sum(1 for r in recs if not r['counted'])
tab['_items'] = [r['item_id'] for r in items]
json.dump(tab, open(os.path.join(TD, 'conditions.json'), 'w'), indent=1)
print('CONDITIONS', json.dumps(tab, indent=1))

#!/usr/bin/env python3
"""Phase 2J S2 - A3 final: CLOSED-SET RE-SCORE of the 2I set with the A2 fix (run_S2 = 2I stored replies by request
hash + only the new L3 calls).  Writes partA/A3_FINAL.json + A3_FINAL.md."""
import json, math, os
P2J = '/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2j'; P2I = os.path.dirname(P2J) + '/phase2i'
def cp(x, n):
    def cdf(k, p): return sum(math.exp(math.lgamma(n+1)-math.lgamma(i+1)-math.lgamma(n-i+1)+i*math.log(p)+(n-i)*math.log(1-p)) for i in range(0, k+1))
    def bis(f):
        lo, hi = 0.0, 1.0
        for _ in range(60):
            m = (lo+hi)/2
            if f(m): lo = m
            else: hi = m
        return (lo+hi)/2
    lo = 0.0 if x == 0 else bis(lambda p: 1-cdf(x-1, p) < 0.025)
    hi = 1.0 if x == n else bis(lambda p: cdf(x, p) > 0.025)
    return [round(100*lo, 2), round(100*hi, 2)]
def rate(x, n): return {'x': x, 'n': n, 'pct': round(100.0*x/n, 2), 'cp95': cp(x, n)}
def fmt(r): return '%d/%d = %.2f %% [%.2f, %.2f]' % (r['x'], r['n'], r['pct'], r['cp95'][0], r['cp95'][1])
jl = lambda p: [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]
IT = {i['jid']: i for i in jl(P2I + '/set/items.jsonl')}
lab = {j: IT[j]['judge_label'] for j in IT}
R2I = {r['jid']: r for r in jl(P2I + '/run/results.jsonl') if r['stack'] == 'tonly'}
NEW = {r['jid']: r for r in jl(P2J + '/run_S2c/results.jsonl')}
N44 = {j for j, r in R2I.items() if r['layer'] == 'F4v2'}
st = json.load(open(P2J + '/run_S2c/RUN_STATUS.json'))
assert len(NEW) == len(R2I) == 900, (len(NEW), len(R2I))
def score(d):
    c = [j for j in lab if lab[j] == 'correct']; w = [j for j in lab if lab[j] == 'wrong']
    return rate(sum(bool(d[j]['accept']) for j in c), len(c)), rate(sum(bool(d[j]['accept']) for j in w), len(w))
b, a = score(R2I), score(NEW)
ch = []
for j in sorted(R2I):
    if (bool(R2I[j]['accept']), R2I[j]['layer']) != (bool(NEW[j]['accept']), NEW[j]['layer']):
        ch.append({'jid': j, 'judge': lab[j], 'type': IT[j].get('judge_type') or IT[j].get('type'), 'answer': IT[j]['answer'],
                   'before': [R2I[j]['layer'], bool(R2I[j]['accept'])], 'after': [NEW[j]['layer'], bool(NEW[j]['accept'])],
                   'l3_reply': NEW[j].get('l3_reply'), 'seeded_reply': NEW[j].get('seeded_reply'), 'in_44': j in N44})
un44 = [j for j in N44 if NEW[j]['layer'] == 'F4v2']
res = {'label': 'CLOSED-SET RE-SCORE (2I set, 900 items; 2I stored L3 replies by request hash + the new S2 calls)',
       'before_2I': {'coverage': b[0], 'fa': b[1]}, 'after_fix': {'coverage': a[0], 'fa': a[1]},
       'run_status': {k: st.get(k) for k in ('status', 'requests', 'needed', 'seeded_used', 'calls_made', 'counted_total', 'spend_usd', 'uncounted_attempts')},
       'changed': ch, 'changed_outside_44': [c for c in ch if not c['in_44']], 'still_F4v2_in_44': un44,
       'catches_correct_now_accepted': sum(1 for c in ch if c['judge'] == 'correct' and c['after'][1]),
       'correct_now_L3_rejected': sum(1 for c in ch if c['judge'] == 'correct' and not c['after'][1]),
       'cost_wrong_now_accepted': sum(1 for c in ch if c['judge'] == 'wrong' and c['after'][1]),
       'wrong_still_rejected_by_L3': sum(1 for j in N44 if lab[j] == 'wrong' and not NEW[j]['accept'])}
json.dump(res, open(P2J + '/partA/A3_FINAL_S2c.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
L = ['## A3 FINAL (stage S2c, F4v2+F4v3 fix) — %s' % res['label'], '',
     'Run: phase2j/run_S2c via run_2j.py (fixed TRANSLATION-ONLY stack, S2 hook fix + S2c F4v3 fix; seed = 2I ledger + run_S2 ledger): %(requests)s L3 requests, %(seeded_used)s answered by stored 2I replies (0 cost), %(needed)s new, %(calls_made)s calls made (counted %(counted_total)s, uncounted %(uncounted_attempts)s), $%(spend_usd)s.' % res['run_status'], '',
     '| | coverage | FA |', '|---|---|---|',
     '| 2I (before) | %s | %s |' % (fmt(b[0]), fmt(b[1])), '| A2 fix F4v2+F4v3 (after) | %s | %s |' % (fmt(a[0]), fmt(a[1])), '',
     'Catches (judge-correct, F4v2 before, now accepted): %d; judge-correct now rejected by L3: %d. Cost (judge-wrong, F4v2 before, now accepted): %d; judge-wrong still rejected (by L3): %d. Items changed outside the 44: %d. Of the 44, still F4v2: %d.'
     % (res['catches_correct_now_accepted'], res['correct_now_L3_rejected'], res['cost_wrong_now_accepted'], res['wrong_still_rejected_by_L3'], len(res['changed_outside_44']), len(un44)), '',
     'Every item whose verdict changed (layer or accept):', '', '| jid | judge | type | before | after | L3 | answer |', '|---|---|---|---|---|---|---|']
for c in ch:
    L.append('| %s | %s | %s | %s %s | %s %s | %s%s | %s |' % (c['jid'], c['judge'], c['type'] or '', c['before'][0], 'acc' if c['before'][1] else 'rej',
             c['after'][0], 'acc' if c['after'][1] else 'rej', c['l3_reply'] or '', ' (stored)' if c['seeded_reply'] else '', c['answer'].replace('|', '/')))
open(P2J + '/partA/A3_FINAL_S2c.md', 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('A3FINAL before', fmt(b[0]), fmt(b[1]), 'after', fmt(a[0]), fmt(a[1]), 'changed', len(ch), 'outside44', len(res['changed_outside_44']),
      'catch', res['catches_correct_now_accepted'], 'cost', res['cost_wrong_now_accepted'])

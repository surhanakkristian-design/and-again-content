"""S8 post-run: FINAL_RUN_DONE, ACCESS_LOG_VERBATIM.md, HEADLINE_QUICK.json (exact 95 % Clopper-Pearson), 0 calls."""
import json, math, os, sys
from collections import Counter
P2J = '/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2j'
D = P2J + '/partD'; RUN = D + '/run'
def jl(p): return [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]
def cdf(k, n, p):
    if p <= 0: return 1.0
    if p >= 1: return 0.0 if k < n else 1.0
    return sum(math.comb(n, i) * p**i * (1-p)**(n-i) for i in range(k+1))
def cp(x, n, a=0.05):
    def bis(f):
        lo, hi = 0.0, 1.0
        for _ in range(200):
            m = (lo+hi)/2
            if f(m): hi = m
            else: lo = m
        return (lo+hi)/2
    lo = 0.0 if x == 0 else bis(lambda p: 1 - cdf(x-1, n, p) >= a/2)
    hi = 1.0 if x == n else bis(lambda p: cdf(x, n, p) <= a/2)
    return [round(100*lo, 2), round(100*hi, 2)]
def rate(x, n): return {'x': x, 'n': n, 'pct': round(100*x/n, 2), 'cp95': cp(x, n)}
items = {it['jid']: it for it in jl(D + '/set/items.jsonl')}
res = {r['jid']: r for r in jl(RUN + '/results.jsonl')}
assert set(res) == set(items) and len(res) == 900, (len(res), len(items))
st = json.load(open(RUN + '/RUN_STATUS.json'))
led = jl(RUN + '/ledger.jsonl')
acc = jl(RUN + '/access_log.jsonl')
def block(sel):
    c = [j for j in sel if items[j]['judge_label'] == 'correct']; w = [j for j in sel if items[j]['judge_label'] == 'wrong']
    cov = rate(sum(bool(res[j]['accept']) for j in c), len(c)); fa = rate(sum(bool(res[j]['accept']) for j in w), len(w))
    return {'coverage': cov, 'fa': fa,
            'coverage_target_90': {'point': cov['pct'] >= 90, 'interval': cov['cp95'][0] >= 90},
            'fa_target_5': {'point': fa['pct'] <= 5, 'interval': fa['cp95'][1] <= 5}}
H = {'label': 'Part D FRESH set, opened once, fixed TRANSLATION-ONLY stack (A2 F4v2+F4v3 fix, corrected sk refs), L3 gemini-3.1-flash-lite t0 tb0 TIP-as-rejection',
     'truth': 'judge_label (partD/judge/labels.jsonl)', 'pooled': block(list(items)),
     'per_level': {lv: block([j for j in items if items[j]['level'] == lv]) for lv in ('A1', 'A2', 'B1', 'B2')},
     '2I': {'coverage': {'pct': 89.13, 'x': 443, 'n': 497, 'cp95': [86.06, 91.73]}, 'fa': {'pct': 4.71, 'x': 19, 'n': 403, 'cp95': [2.86, 7.26]}},
     'layers': dict(Counter(r['layer'] for r in res.values())),
     'false_rejections': sorted(j for j in items if items[j]['judge_label'] == 'correct' and not res[j]['accept']),
     'false_acceptances': sorted(j for j in items if items[j]['judge_label'] == 'wrong' and res[j]['accept']),
     'fr_by_layer': dict(Counter(res[j]['layer'] for j in items if items[j]['judge_label'] == 'correct' and not res[j]['accept'])),
     'fa_by_layer': dict(Counter(res[j]['layer'] for j in items if items[j]['judge_label'] == 'wrong' and res[j]['accept'])),
     'call_failed_items': sum(1 for r in res.values() if r.get('call_failed')),
     'run_status': {k: st.get(k) for k in ('status', 'requests', 'needed', 'seeded_used', 'calls_made', 'counted_total', 'spend_usd', 'uncounted_attempts', 'results_missing', 'stop')},
     'ledger_rows': len(led), 'ledger_http200': sum(1 for r in led if r.get('http') == 200),
     'ledger_http': dict(Counter(str(r.get('http')) for r in led)), 'opens': len(acc)}
json.dump(H, open(RUN + '/HEADLINE_QUICK.json', 'w'), indent=1, sort_keys=True)
raw = open(RUN + '/access_log.jsonl', encoding='utf-8').read()
open(RUN + '/ACCESS_LOG_VERBATIM.md', 'w').write('# Part D access log (verbatim copy of partD/run/access_log.jsonl)\n\n'
    'Opens recorded: %d. The pre-flight dry count (partD/S8_dry_count.json) ran the stack prepare step only in partD/dry '
    '(labels stripped by clean_item, no L3 call, no verdict); it did not go through open_set.\n\n```\n%s```\n' % (len(acc), raw))
open(RUN + '/FINAL_RUN_DONE', 'w').write('Part D run finished %s; status %s; counted %d; spend $%.6f; results %d; opens %d; RUN_COMMIT %s\n'
    % (st.get('ts'), st.get('status'), st.get('counted_total'), st.get('spend_usd'), len(res), len(acc), open(D + '/RUN_COMMIT.txt').read().strip()))
p, L = H['pooled'], H['per_level']
print('POOLED cov %(x)d/%(n)d = %(pct).2f %% %(cp95)s' % p['coverage'], '| FA %(x)d/%(n)d = %(pct).2f %% %(cp95)s' % p['fa'], p['coverage_target_90'], p['fa_target_5'])
for lv in L: print(lv, 'cov %(x)d/%(n)d %(pct).2f %(cp95)s' % L[lv]['coverage'], 'FA %(x)d/%(n)d %(pct).2f %(cp95)s' % L[lv]['fa'])
print('FR by layer', H['fr_by_layer'], 'FA by layer', H['fa_by_layer'], 'failed', H['call_failed_items'], 'ledger', H['ledger_http'], 'opens', len(acc))

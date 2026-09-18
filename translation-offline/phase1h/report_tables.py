#!/usr/bin/env python3
"""Phase 1h — report tables (SEPARATE from the frozen checker; aggregation only, no rule, no verdict).

Reads the newest phase1h/results_1h_*.json plus the fresh inputs and judgements and writes
phase1h/tables_1h.md: in-sample vs out-of-sample, the OLD-sentence vs NEW-sentence split of the fresh set,
FA by type/layer, routing, latency, cost, and the false rejections grouped by cause with an asserted sum.

usage: python3 phase1h/report_tables.py
"""
import glob
import json
import os
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FRESH = os.path.join(HERE, 'fresh')


# ---------------------------------------------------------------- Clopper-Pearson (reuse the frozen one)
def _own_cp(k, n, alpha=0.05):
    """exact Clopper-Pearson, bisection on the regularised incomplete beta."""
    import math

    def betacf(a, b, x):
        tiny, eps = 1e-300, 3e-16
        qab, qap, qam = a + b, a + 1.0, a - 1.0
        c, d = 1.0, 1.0 - qab * x / qap
        if abs(d) < tiny:
            d = tiny
        d, h = 1.0 / d, 1.0 / d
        for m in range(1, 300):
            m2 = 2 * m
            aa = m * (b - m) * x / ((qam + m2) * (a + m2))
            d = 1.0 + aa * d
            c = 1.0 + aa / c
            if abs(d) < tiny:
                d = tiny
            if abs(c) < tiny:
                c = tiny
            d = 1.0 / d
            h *= d * c
            aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
            d = 1.0 + aa * d
            c = 1.0 + aa / c
            if abs(d) < tiny:
                d = tiny
            if abs(c) < tiny:
                c = tiny
            d = 1.0 / d
            de = d * c
            h *= de
            if abs(de - 1.0) < eps:
                break
        return h

    def ibeta(a, b, x):
        if x <= 0:
            return 0.0
        if x >= 1:
            return 1.0
        lbeta = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log(1 - x)
        if x < (a + 1) / (a + b + 2):
            return math.exp(lbeta) * betacf(a, b, x) / a
        return 1.0 - math.exp(lbeta) * betacf(b, a, 1 - x) / b

    def inv(a, b, p):
        lo, hi = 0.0, 1.0
        for _ in range(200):
            mid = (lo + hi) / 2
            if ibeta(a, b, mid) < p:
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2

    if n == 0:
        return (0.0, 100.0)
    lo = 0.0 if k == 0 else 100 * inv(k, n - k + 1, alpha / 2)
    hi = 100.0 if k == n else 100 * inv(k + 1, n - k, 1 - alpha / 2)
    return (round(lo, 4), round(hi, 4))


CP = _own_cp
try:                                                   # prefer the frozen implementation if it exposes one
    sys.path.insert(0, HERE)
    import checker_1h as _C                            # noqa: E402  (import-safe, no side effects)
    for _n in ('cp', 'clopper_pearson', 'cp95', 'ci'):
        _f = getattr(_C, _n, None) or getattr(getattr(_C, 'base', None), _n, None)
        if callable(_f):
            try:
                _t = _f(2, 105)
                if isinstance(_t, (tuple, list)) and len(_t) == 2:
                    CP = (lambda f: (lambda k, n: tuple(round(100 * x, 4) if x <= 1 else round(x, 4) for x in f(k, n))))(_f)
                    break
            except Exception:
                pass
except Exception:
    pass


def pc(k, n):
    lo, hi = CP(k, n)
    return '%d/%d = %.1f %% (95 %% CP %.1f–%.1f)' % (k, n, (100.0 * k / n) if n else 0.0, lo, hi)


def cell(k, n):
    lo, hi = CP(k, n)
    return '%d/%d %.1f %% [%.1f–%.1f]' % (k, n, (100.0 * k / n) if n else 0.0, lo, hi)


# ---------------------------------------------------------------- inputs
def jl(p):
    return [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]


res_path = sorted(glob.glob(os.path.join(HERE, 'results_1h_*.json')))[-1]
R = json.load(open(res_path, encoding='utf-8'))

new_sids = {int(r['sid']) for r in jl(os.path.join(FRESH, 'new_sentences_60.jsonl'))}
sent = {}
for r in jl(os.path.join(FRESH, 'writer_input_140.jsonl')):
    sent[int(r['sid'])] = r


def band(sk):
    n = len((sk or '').split())
    return '1-6' if n <= 6 else '7-9' if n <= 9 else '10-12' if n <= 12 else '13-16' if n <= 16 else '17+'


def iid(kind, sid, en):
    import hashlib
    return '%s:%d:%d' % (kind, int(sid), int(hashlib.md5(en.encode()).hexdigest()[:8], 16))


items = {}
for kind, pat in (('C', 'correct_part*.jsonl'), ('W', 'wrong_part*.jsonl')):
    for p in sorted(glob.glob(os.path.join(FRESH, pat))):
        for r in jl(p):
            sid = int(r['sid'])
            i = iid(kind, sid, r['en'])
            items[i] = {'item_id': i, 'kind': kind, 'sid': sid, 'n': int(r['n']), 'en': r['en'],
                        'type': r.get('type'), 'half': 'NEW-sentences' if sid in new_sids else 'OLD-sentences',
                        'level': sent.get(sid, {}).get('level'), 'band': band(sent.get(sid, {}).get('sk', ''))}

jmap = {}
idx = {}
for kind, pat in (('C', 'correct_part*.jsonl'), ('W', 'wrong_part*.jsonl')):
    for p in sorted(glob.glob(os.path.join(FRESH, pat))):
        for r in jl(p):
            idx[(kind, int(r['sid']), int(r['n']))] = iid(kind, int(r['sid']), r['en'])
for r in jl(os.path.join(FRESH, 'judgements.jsonl')):
    k = (r['set'], int(r['sid']), int(r['n']))
    if k in idx:
        jmap[idx[k]] = r['real']

old105 = {r['id']: r['real'] for r in jl(os.path.join(FRESH, 'judgements_old105.jsonl'))}

out = []
w = out.append
w('# Phase 1h — measurement tables (generated by phase1h/report_tables.py)\n')
w('source: `%s`\n' % os.path.basename(res_path))

for row in ('row7', 'row8'):
    lab = 'row 7 (P-B)' if row == 'row7' else 'row 8 (P-C)'
    OLD = R['rows'][row]['OLD']
    NEW = R['rows'][row].get('NEW') or R['rows'][row].get('FRESH')
    w('\n## %s\n' % lab)

    # --- 1 in-sample vs out-of-sample
    w('### In-sample (frozen 235/105) vs out-of-sample (fresh 420/550)\n')
    w('| figure | in-sample OLD | out-of-sample FRESH | delta (pp) |')
    w('|---|---|---|---|')
    oc, nc = OLD['judged_coverage'], NEW['judged_coverage']
    of, nf = OLD['judged_fa'], NEW['judged_fa']
    w('| coverage (judged really correct) | %s | %s | %+.1f |' % (
        cell(oc['k'], oc['n']), cell(nc['k'], nc['n']), 100.0 * nc['k'] / nc['n'] - 100.0 * oc['k'] / oc['n']))
    w('| real false acceptance | %s | %s | %+.1f |' % (
        cell(of['k'], of['n']), cell(nf['k'], nf['n']), 100.0 * nf['k'] / nf['n'] - 100.0 * of['k'] / of['n']))
    orf, nrf = OLD['raw_fa'], NEW['raw_fa']
    w('| raw accepted wrong-set items | %s | %s | %+.1f |' % (
        cell(orf['k'], orf['n']), cell(nrf['k'], nrf['n']),
        100.0 * nrf['k'] / nrf['n'] - 100.0 * orf['k'] / orf['n']))
    w('| items without a model verdict (not measured) | %d | %d |  |' % (OLD['not_measured'], NEW['not_measured']))

    # --- 2 fresh coverage splits
    fr_ids = {x['item_id'] for x in NEW['false_rejections']}
    acc_c = {i: (i not in fr_ids) for i, it in items.items() if it['kind'] == 'C'}

    def split(keyf, title):
        g = defaultdict(lambda: [0, 0])
        for i, ok in acc_c.items():
            k = keyf(items[i])
            g[k][1] += 1
            g[k][0] += int(ok)
        w('\n**fresh correct set — coverage by %s**\n' % title)
        w('| %s | coverage |' % title)
        w('|---|---|')
        for k in sorted(g):
            w('| %s | %s |' % (k, cell(g[k][0], g[k][1])))
        return g

    w('\n### Coverage on the fresh correct set (denominator = 420 judged really correct)\n')
    w('headline: %s\n' % pc(nc['k'], nc['n']))
    split(lambda it: it['level'] or '?', 'level')
    split(lambda it: it['band'], 'Slovak length band')
    gh = split(lambda it: it['half'], 'sentence half (OLD 80 / NEW 60)')

    # --- 3 FA splits
    w('\n### Real false acceptance on the fresh wrong set\n')
    w('headline (judged really wrong denominator): %s\n' % pc(nf['k'], nf['n']))
    w('raw accepted / all written wrong answers: %s\n' % pc(nrf['k'], nrf['n']))
    fa = NEW['fa_ids']
    hh = Counter(items[x['item_id']]['half'] for x in fa if x['item_id'] in items)
    denom = Counter(items[i]['half'] for i, it in items.items() if it['kind'] == 'W' and jmap.get(i) == 'wrong')
    w('| sentence half | real FA |')
    w('|---|---|')
    for k in sorted(denom):
        w('| %s | %s |' % (k, cell(hh.get(k, 0), denom[k])))
    w('')
    w('| wrong type | real FA (of judged really wrong of that type) |')
    w('|---|---|')
    tden = Counter(items[i]['type'] for i, it in items.items() if it['kind'] == 'W' and jmap.get(i) == 'wrong')
    tnum = Counter(x.get('type') for x in fa)
    for t in ('T', 'W', 'M', 'S'):
        w('| %s | %s |' % (t, cell(tnum.get(t, 0), tden.get(t, 0))))
    w('')
    w('| layer | real FA |')
    w('|---|---|')
    for k, v in sorted(Counter(x.get('layer') for x in fa).items()):
        w('| %s | %d |' % (k, v))

    # --- 4 every real FA, itemised
    w('\n### Every real false acceptance, itemised\n')
    for src, tag, jd in ((OLD['fa_ids'], 'OLD in-sample', old105), (fa, 'FRESH out-of-sample', jmap)):
        for x in src:
            w('- **%s** [%s] %s · level %s · type %s · layer %s' % (
                x['item_id'], tag, x.get('why', ''), x.get('level'), x.get('type'), x.get('layer')))
            w('  - sk: %s' % x.get('sk', ''))
            w('  - reference: %s' % x.get('reference', ''))
            w('  - answer: %s' % x.get('answer', ''))
    w('\nOLD accepted-but-unjudged resolved against `fresh/judgements_old105.jsonl`:\n')
    abu = OLD.get('accepted_but_unjudged') or []
    res_abu = [(i, old105.get(i, 'NO JUDGEMENT')) for i in (abu if isinstance(abu, list) else [])]
    for i, v in res_abu:
        w('- `%s` -> judged **really %s**' % (i if isinstance(i, str) else i.get('item_id'), v))
    extra = sum(1 for i, v in res_abu if v == 'wrong')
    w('\nOLD strict (Phase 1g list) real FA: %s; OLD real FA under the NEW blind judgement '
      '(strict + newly judged really wrong): %s\n'
      % (cell(of['k'], of['n']), cell(of['k'] + extra, 105 - sum(1 for v in old105.values() if v == 'correct'))))

    # --- 5 routing / latency / cost
    rt = NEW['routing']
    tot = sum(rt.values())
    w('\n### Routing, latency, cost\n')
    w('| layer | fresh items | share |')
    w('|---|---|---|')
    for k, v in sorted(rt.items(), key=lambda x: -x[1]):
        w('| %s | %d | %.1f %% |' % (k, v, 100.0 * v / tot))
    w('| **total** | %d | 100 %% |' % tot)
    w('')
    w('OLD routing: %s' % json.dumps(OLD['routing']))

    # --- 6 false rejections by cause
    w('\n### False rejections by cause (fresh set)\n')
    cz = Counter(x.get('cause') or x.get('why') for x in NEW['false_rejections'])
    w('| cause | n | ids |')
    w('|---|---|---|')
    for k, v in cz.most_common():
        ids = [x['item_id'] for x in NEW['false_rejections'] if (x.get('cause') or x.get('why')) == k]
        w('| %s | %d | %s |' % (k, v, ', '.join('`%s`' % i for i in ids)))
    w('| **sum** | **%d** | asserted == total false rejections **%d** -> %s |'
      % (sum(cz.values()), len(NEW['false_rejections']),
         'OK' if sum(cz.values()) == len(NEW['false_rejections']) else 'MISMATCH'))
    assert sum(cz.values()) == len(NEW['false_rejections'])
    w('\nfr_by_cause as recorded by the frozen runner: `%s`\n' % json.dumps(NEW.get('fr_by_cause')))
    czo = Counter(x.get('cause') or x.get('why') for x in OLD['false_rejections'])
    w('OLD false rejections by cause: `%s` (sum %d == %d)\n'
      % (json.dumps(dict(czo)), sum(czo.values()), len(OLD['false_rejections'])))

# ---------------------------------------------------------------- global: latency, tokens, cost
lat, tok = R.get('latency_ms', {}), R.get('tokens', {})
PRICE_IN, PRICE_OUT = 0.25, 1.50                        # lib_prev.PRICE['lite'], $ per 1M tokens
n = max(1, lat.get('n') or 1)
cost_call = (tok.get('in', 0) / 1e6 * PRICE_IN + tok.get('out', 0) / 1e6 * PRICE_OUT) / n
l3 = 0
tot_all = 0
for row in ('row7', 'row8'):
    NEW = R['rows'][row].get('NEW') or {}
    if row == 'row7':
        l3 = NEW.get('routing', {}).get('L3', 0)
        tot_all = sum(NEW.get('routing', {}).values()) or 1
share = l3 / tot_all
out.append('\n## Cost and latency (whole run)\n')
out.append('- model calls latency: n %s, median %s ms, p95 %s ms' % (lat.get('n'), lat.get('median'), lat.get('p95')))
out.append('- tokens: in %s, out %s' % (tok.get('in'), tok.get('out')))
out.append('- price used: `lib_prev.PRICE["lite"]` $%.2f in / $%.2f out per 1M tokens (no cached rate: the '
           'prompt is below the implicit-caching minimum, Phase 1e §cost)' % (PRICE_IN, PRICE_OUT))
out.append('- **cost per L3 call: $%.6f**' % cost_call)
out.append('- usage assumption (Phase 1e/1f formula, restated by hand): 20 exercises/day x 30 days = 600 '
           'exercises per active user per month, times the L3 share')
out.append('- fresh L3 share (row 7): %.1f %% -> %.0f L3 calls/user/month -> **$%.4f per active user per '
           'month**' % (100 * share, 600 * share, 600 * share * cost_call))

txt = '\n'.join(out) + '\n'
open(os.path.join(HERE, 'tables_1h.md'), 'w', encoding='utf-8').write(txt)
print(txt)

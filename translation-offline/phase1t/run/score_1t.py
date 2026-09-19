#!/usr/bin/env python3
"""Phase 1T scoring — runs AFTER the run, from the rows, with 0 model calls and 0 network.

    PYTHONDONTWRITEBYTECODE=1 python3 phase1t/run/score_1t.py [--results results_1t.json]
    PYTHONDONTWRITEBYTECODE=1 python3 phase1t/run/score_1t.py --selftest

Every figure is produced TWICE: on the primary judge labels and on S2 (every item the judge
flagged borderline=true with a non-empty "dropped" field and judged wrong is scored as correct).
Intervals are exact Clopper-Pearson 95 %; P1 vs P2 is Fisher's exact test.
"""
import argparse
import collections
import json
import math
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
P1T = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(os.path.dirname(P1T), 'phase1s'))
from safe_json import safe_dump                                                # noqa: E402

AGENTDROP = ('agentdrop-main', 'agentdrop-embedded')
BYPASSIVE = ('by-passive', 'by-passive-embedded')
TYPES = ('T', 'W', 'M', 'S')


# ------------------------------------------------------------------ statistics
def _betacf(a, b, x):
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


def betainc(a, b, x):
    """Regularised incomplete beta I_x(a, b)."""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    lb = (math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
          + a * math.log(x) + b * math.log1p(-x))
    if x < (a + 1.0) / (a + b + 2.0):
        return math.exp(lb) * _betacf(a, b, x) / a
    return 1.0 - math.exp(lb) * _betacf(b, a, 1.0 - x) / b


def _betaq(p, a, b):
    lo, hi = 0.0, 1.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if betainc(a, b, mid) < p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def cp(k, n, alpha=0.05):
    """Exact Clopper-Pearson 95 % interval, in per cent."""
    if not n:
        return [0.0, 0.0]
    lo = 0.0 if k == 0 else _betaq(alpha / 2.0, k, n - k + 1)
    hi = 1.0 if k == n else _betaq(1.0 - alpha / 2.0, k + 1, n - k)
    return [round(100.0 * lo, 2), round(100.0 * hi, 2)]


def kn(k, n):
    return {'k': k, 'n': n, 'pct': round(100.0 * k / n, 2) if n else None, 'ci': cp(k, n)}


def _lhyp(a, b, c, d):
    r1, r2, c1, c2, tot = a + b, c + d, a + c, b + d, a + b + c + d
    return (math.lgamma(r1 + 1) + math.lgamma(r2 + 1) + math.lgamma(c1 + 1) + math.lgamma(c2 + 1)
            - math.lgamma(tot + 1) - math.lgamma(a + 1) - math.lgamma(b + 1)
            - math.lgamma(c + 1) - math.lgamma(d + 1))


def fisher_exact(a, b, c, d):
    """Two-sided Fisher exact p for [[a, b], [c, d]]."""
    tot = a + b + c + d
    if not tot:
        return 1.0
    r1, c1 = a + b, a + c
    obs = _lhyp(a, b, c, d)
    p = 0.0
    for x in range(max(0, c1 - (tot - r1)), min(r1, c1) + 1):
        l = _lhyp(x, r1 - x, c1 - x, tot - r1 - c1 + x)
        if l <= obs + 1e-9:
            p += math.exp(l)
    return min(1.0, p)


# ------------------------------------------------------------------ label sets
def label_of(row, s2):
    """(judged, type) under the primary labels or under S2."""
    j, t = row.get('judged'), row.get('judged_type')
    if s2 and j == 'wrong' and row.get('borderline') and (row.get('dropped') not in (None, '', [])):
        return 'correct', None
    return j, t


def moved_by_s2(rows):
    return [r['item_id'] for r in rows if label_of(r, False)[0] != label_of(r, True)[0]]


# ------------------------------------------------------------------ cells
def pack(rows, s2):
    cor = [r for r in rows if label_of(r, s2)[0] == 'correct']
    wro = [r for r in rows if label_of(r, s2)[0] == 'wrong']
    return {'coverage': kn(sum(1 for r in cor if r['final_accept']), len(cor)),
            'fa': kn(sum(1 for r in wro if r['final_accept']), len(wro))}


def tagged(rows, tags):
    return [r for r in rows if set(r.get('tags') or []) & set(tags)]


def block(rows, s2):
    d = {'pooled': pack(rows, s2),
         'P1': pack([r for r in rows if r['half'] == 'P1'], s2),
         'P2': pack([r for r in rows if r['half'] == 'P2'], s2)}
    for m in ('coverage', 'fa'):
        a, b = d['P1'][m], d['P2'][m]
        d.setdefault('fisher_P1_vs_P2', {})[m] = round(
            fisher_exact(a['k'], a['n'] - a['k'], b['k'], b['n'] - b['k']), 4)
    d['by_level'] = {lv: pack([r for r in rows if r['level'] == lv], s2)
                     for lv in sorted({r['level'] for r in rows if r['level']})}
    d['fa_by_judged_type'] = {}
    for t in TYPES:
        sub = [r for r in rows if label_of(r, s2) == ('wrong', t)]
        d['fa_by_judged_type'][t] = kn(sum(1 for r in sub if r['final_accept']), len(sub))

    # ---- the pre-declared cells
    cells = {}
    for name, tags in (('agent_drop_all', AGENTDROP), ('agent_drop_main', ('agentdrop-main',)),
                       ('agent_drop_embedded', ('agentdrop-embedded',))):
        sub = [r for r in tagged(rows, tags) if label_of(r, s2)[0] == 'wrong']
        k = sum(1 for r in sub if r['final_accept'])
        cells[name] = {'writer_tag_and_judged_wrong': len(sub), 'false_accepts': kn(k, len(sub)),
                       'caught': kn(len(sub) - k, len(sub)),
                       'ag_fired': sum(1 for r in sub if r['ag']['fired'])}
    bp = [r for r in tagged(rows, BYPASSIVE) if label_of(r, s2)[0] == 'correct']
    cells['by_passive_coverage'] = dict(kn(sum(1 for r in bp if r['final_accept']), len(bp)),
                                        expectation='100 %',
                                        rejected=[r['item_id'] for r in bp if not r['final_accept']])
    skp = [r for r in tagged(rows, ('skp-passive',)) if label_of(r, s2)[0] == 'correct']
    cells['skp_coverage'] = dict(kn(sum(1 for r in skp if r['final_accept']), len(skp)),
                                 ag_abstains=sum(1 for r in skp if not r['ag']['fired']),
                                 ag_fired=[r['item_id'] for r in skp if r['ag']['fired']])
    tf = [r for r in tagged(rows, ('timeframe',)) if label_of(r, s2)[0] == 'wrong']
    cells['time_frame_fa'] = kn(sum(1 for r in tf if r['final_accept']), len(tf))
    d['cells'] = cells

    d['false_rejections_by_layer'] = dict(collections.Counter(
        r['final_layer'] for r in rows if label_of(r, s2)[0] == 'correct' and not r['final_accept']))
    d['false_accepts_by_layer'] = dict(collections.Counter(
        r['final_layer'] for r in rows if label_of(r, s2)[0] == 'wrong' and r['final_accept']))
    d['true_rejections_by_layer'] = dict(collections.Counter(
        r['final_layer'] for r in rows if label_of(r, s2)[0] == 'wrong' and not r['final_accept']))

    # ---- AG v3: catches, measured cost, and the v2 / single-flag shadows
    fired = [r for r in rows if r['ag']['fired']]
    cost = [r for r in fired if label_of(r, s2)[0] == 'correct']
    d['ag_v3'] = {
        'fired': len(fired),
        'catches_judged_wrong': sum(1 for r in fired if label_of(r, s2)[0] == 'wrong'),
        'measured_cost_judged_correct': len(cost),
        'measured_cost_items': [{'item_id': r['item_id'], 'sid': r['sid'], 'tags': r['tags'],
                                 'level': r['level'], 'half': r['half'],
                                 'reason': r['ag']['reason']} for r in cost],
        'fired_on_unlabelled': sum(1 for r in fired if label_of(r, s2)[0] not in
                                   ('correct', 'wrong'))}
    sh = {}
    for name in sorted(set(k for r in rows for k in (r.get('ag_shadow') or {}))):
        f = [r for r in rows if (r['ag_shadow'][name] or {}).get('fired')]
        sh[name] = {'fired': len(f),
                    'catches_judged_wrong': sum(1 for r in f if label_of(r, s2)[0] == 'wrong'),
                    'cost_judged_correct': sum(1 for r in f if label_of(r, s2)[0] == 'correct'),
                    'fired_where_v3_did_not': sum(1 for r in f if not r['ag']['fired']),
                    'v3_fires_where_it_did_not': sum(
                        1 for r in rows if r['ag']['fired']
                        and not (r['ag_shadow'][name] or {}).get('fired'))}
    d['ag_shadows'] = sh
    return d


def run(results_path):
    out_dir = os.path.dirname(os.path.abspath(results_path))
    res = json.load(open(results_path, encoding='utf-8'))
    rows = res['rows']
    labelled = [r for r in rows if r.get('judged') in ('correct', 'wrong')]
    out = {'phase': '1T', 'results': os.path.basename(results_path),
           'freeze_commit': res.get('freeze_commit'), 'stub_model': res.get('stub_model'),
           'n_rows': len(rows), 'n_labelled': len(labelled),
           'preflight': res.get('preflight'), 'calls': res.get('calls'),
           'primary': block(labelled, False), 'S2': block(labelled, True),
           's2_moved_items': moved_by_s2(labelled),
           'judge_noise': (res.get('label_meta') or {}).get('label_join'),
           'selftest': selftest()}
    safe_dump(out, os.path.join(out_dir, 'SCORE_1T.json'))
    write_md(out, out_dir)
    print(json.dumps({'coverage': out['primary']['pooled']['coverage'],
                      'fa': out['primary']['pooled']['fa'],
                      'S2_coverage': out['S2']['pooled']['coverage'],
                      'S2_fa': out['S2']['pooled']['fa']}, indent=1))
    return out


def c(d):
    return '-' if not d or not d['n'] else '%d/%d = %.2f %% [%.2f, %.2f]' % (
        d['k'], d['n'], d['pct'], d['ci'][0], d['ci'][1])


def write_md(out, out_dir):
    L = ['# SCORE_1T — the fresh set (primary labels and S2), 0 model calls', '',
         '| figure | primary | S2 |', '| --- | --- | --- |']
    for nm, path in (('coverage (pooled)', ('pooled', 'coverage')), ('FA (pooled)', ('pooled', 'fa')),
                     ('coverage P1', ('P1', 'coverage')), ('coverage P2', ('P2', 'coverage')),
                     ('FA P1', ('P1', 'fa')), ('FA P2', ('P2', 'fa'))):
        a, b = out['primary'], out['S2']
        for k in path:
            a, b = a[k], b[k]
        L.append('| %s | %s | %s |' % (nm, c(a), c(b)))
    L += ['| Fisher P1 vs P2 (coverage) | %s | %s |'
          % (out['primary']['fisher_P1_vs_P2']['coverage'], out['S2']['fisher_P1_vs_P2']['coverage']),
          '| Fisher P1 vs P2 (FA) | %s | %s |'
          % (out['primary']['fisher_P1_vs_P2']['fa'], out['S2']['fisher_P1_vs_P2']['fa']), '',
          '## cells (primary / S2)', '', '| cell | primary | S2 |', '| --- | --- | --- |']
    for nm in ('agent_drop_all', 'agent_drop_main', 'agent_drop_embedded'):
        L.append('| %s — false accepts | %s | %s |'
                 % (nm, c(out['primary']['cells'][nm]['false_accepts']),
                    c(out['S2']['cells'][nm]['false_accepts'])))
    L += ['| by-passive coverage | %s | %s |' % (c(out['primary']['cells']['by_passive_coverage']),
                                                 c(out['S2']['cells']['by_passive_coverage'])),
          '| SKP-sentence coverage | %s | %s |' % (c(out['primary']['cells']['skp_coverage']),
                                                   c(out['S2']['cells']['skp_coverage'])),
          '| time-frame FA | %s | %s |' % (c(out['primary']['cells']['time_frame_fa']),
                                           c(out['S2']['cells']['time_frame_fa'])), '',
          '## per level (coverage / FA, primary)', '', '| level | coverage | FA |',
          '| --- | --- | --- |']
    for lv, d in sorted(out['primary']['by_level'].items()):
        L.append('| %s | %s | %s |' % (lv, c(d['coverage']), c(d['fa'])))
    L += ['', '## FA by judged type (primary)', '', '| type | FA |', '| --- | --- |']
    for t in TYPES:
        L.append('| %s | %s |' % (t, c(out['primary']['fa_by_judged_type'][t])))
    L += ['', '## AG v3', '', '```', json.dumps(out['primary']['ag_v3'], indent=1)[:4000], '```', '',
          '## AG shadows (v2 and each v3 flag alone)', '', '```',
          json.dumps(out['primary']['ag_shadows'], indent=1), '```', '',
          '## layers', '', '```',
          json.dumps({k: out['primary'][k] for k in ('false_rejections_by_layer',
                                                     'false_accepts_by_layer',
                                                     'true_rejections_by_layer')}, indent=1),
          '```', '', '## judge noise (the 80 duplicate controls)', '', '```',
          json.dumps(out['judge_noise'], indent=1)[:2000], '```', '']
    open(os.path.join(out_dir, 'SCORE_1T.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')


def selftest():
    ck = [('cp(8,481)', cp(8, 481), [0.72, 3.25]), ('cp(348,385)', cp(348, 385), [87.00, 93.14]),
          ('cp(0,10)', cp(0, 10), [0.0, 30.85]), ('cp(10,10)', cp(10, 10), [69.15, 100.0])]
    out = [{'check': n, 'got': g, 'want': w, 'ok': g == w} for n, g, w in ck]
    f = fisher_exact(1, 9, 11, 3)
    out.append({'check': 'fisher_exact(1,9,11,3)', 'got': round(f, 6), 'want': 0.0027,
                'ok': abs(f - 0.0027) < 5e-4})
    f2 = fisher_exact(5, 5, 5, 5)
    out.append({'check': 'fisher_exact(5,5,5,5)', 'got': round(f2, 4), 'want': 1.0,
                'ok': abs(f2 - 1.0) < 1e-9})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--results', default=os.path.join(HERE, 'results_1t.json'))
    ap.add_argument('--selftest', action='store_true')
    a = ap.parse_args()
    st = selftest()
    bad = [x for x in st if not x['ok']]
    print(json.dumps({'selftest': st}, indent=1))
    if bad:
        raise SystemExit('REFUSED: the statistics self-test failed: %s' % json.dumps(bad))
    if a.selftest:
        return st
    if not os.path.exists(a.results):
        raise SystemExit('REFUSED: %s does not exist — the run has not written its rows yet.'
                         % a.results)
    return run(a.results)


if __name__ == '__main__':
    main()

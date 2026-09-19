#!/usr/bin/env python3
"""Phase 1V Track A3 bounded loop on CLOSED sets (1T, 1U).  0 model calls."""
import os, sys, json, math, collections
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__)); TO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import stack_1v as S                                                          # noqa: E402
sys.path.insert(0, os.path.join(TO, 'phase1u', 'taskA'))
import gate_v4 as G                                                           # noqa: E402


def lbeta_tail(k, n, p, upper):
    # P(X>=k) if upper else P(X<=k)
    rng = range(k, n + 1) if upper else range(0, k + 1)
    s = 0.0
    for i in rng:
        if p in (0, 1):
            s += 1.0 if (p == 0 and i == 0) or (p == 1 and i == n) else 0.0
            continue
        s += math.exp(math.lgamma(n + 1) - math.lgamma(i + 1) - math.lgamma(n - i + 1)
                      + i * math.log(p) + (n - i) * math.log(1 - p))
    return s


def cp(k, n, a=0.05):
    if n == 0:
        return (0.0, 100.0)
    def bis(f, lo, hi):
        for _ in range(60):
            m = (lo + hi) / 2
            if f(m):
                hi = m
            else:
                lo = m
        return (lo + hi) / 2
    lo = 0.0 if k == 0 else bis(lambda p: lbeta_tail(k, n, p, True) >= a / 2, 0.0, 1.0)
    hi = 1.0 if k == n else bis(lambda p: lbeta_tail(k, n, p, False) <= a / 2, 0.0, 1.0)
    return (round(100 * lo, 2), round(100 * hi, 2))


def fig(k, n):
    return {'k': k, 'n': n, 'pct': round(100.0 * k / n, 2) if n else None, 'ci': cp(k, n)}


def metrics(rows):
    """rows: dicts judged, jtype, tags, acc"""
    cor = [r for r in rows if r['judged'] == 'correct']; wro = [r for r in rows if r['judged'] == 'wrong']
    out = {'coverage': fig(sum(r['acc'] for r in cor), len(cor)),
           'FA': fig(sum(r['acc'] for r in wro), len(wro)), 'FA_by_type': {}, 'cells': {}}
    for t in sorted({r['jtype'] for r in wro if r['jtype']}):
        w = [r for r in wro if r['jtype'] == t]
        out['FA_by_type'][t] = fig(sum(r['acc'] for r in w), len(w))
    tags = sorted({t for r in rows for t in r['tags']})
    for t in tags:
        c = [r for r in cor if t in r['tags']]; w = [r for r in wro if t in r['tags']]
        if c:
            out['cells']['cov:' + t] = fig(sum(r['acc'] for r in c), len(c))
        if w:
            out['cells']['FA:' + t] = fig(sum(r['acc'] for r in w), len(w))
    return out


def worse(new, old):
    """list of cells that got worse (coverage down / FA up), by point."""
    bad = []
    if new['coverage']['k'] * old['coverage']['n'] < old['coverage']['k'] * new['coverage']['n']:
        bad.append('coverage')
    if new['FA']['k'] > old['FA']['k']:
        bad.append('FA')
    for t, v in new['FA_by_type'].items():
        if v['k'] > old['FA_by_type'][t]['k']:
            bad.append('FA_type_' + t)
    for c, v in new['cells'].items():
        o = old['cells'].get(c)
        if o is None:
            continue
        if c.startswith('cov:') and v['k'] < o['k']:
            bad.append(c)
        if c.startswith('FA:') and v['k'] > o['k']:
            bad.append(c)
    return bad


# ------------------------------------------------------------------ closed sets
def load_1u():
    rows = json.load(open(os.path.join(TO, 'phase1u', 'run', 'results_1u.json')))['rows']
    return [{'id': r['item_id'], 'sk': r['sk'], 'answer': r['answer'], 'reference': r['reference'],
             'judged': r.get('judged'), 'jtype': r.get('judged_type'), 'tags': r.get('tags') or [],
             'acc0': bool(r['final_accept']), 'layer0': r.get('final_layer'),
             'v4': bool((r.get('ag') or {}).get('fired')), 'ann': None, 'wt': None}
            for r in rows if r.get('judged') in ('correct', 'wrong')]


def load_1t():
    rows, items, sents, ann = G.load_1t()
    out, notes = [], collections.Counter()
    for r in rows:
        if r.get('judged') not in ('correct', 'wrong'):
            continue
        it, s = items[r['item_id']], sents[r['sid']]
        a = (ann.get(str(r['sid'])) or ann.get(r['sid']) or {}) if ann else {}
        wt = (s.get('tags') or {}).get('writer_tags') or {}
        ref = G.ref_of(a, s)
        v4 = S.ORIG_V4_DECIDE(s['slovak'], a, wt, it['answer'], ref)['fired']
        acc0 = bool(r.get('final_accept'))
        layer0 = r.get('final_layer') or (r.get('layers') or {}).get('main_layer')
        if acc0 and v4:
            acc0, layer0 = False, 'AG'; notes['v4_rejects_stored_accept'] += 1
        if (not r.get('final_accept')) and layer0 == 'AG' and not v4:
            notes['stored_AG_reject_v4_silent_kept_rejected'] += 1
        out.append({'id': r['item_id'], 'sk': s['slovak'], 'answer': it['answer'], 'reference': ref,
                    'judged': r['judged'], 'jtype': r.get('judged_type') or r.get('type'),
                    'tags': r.get('tags') or [], 'acc0': acc0, 'layer0': layer0, 'v4': v4,
                    'ann': a, 'wt': wt})
    return out, dict(notes), sorted(rows[0].keys())


def apply(rows, extra, tip):
    res, ag_new, tip_new = [], [], []
    for r in rows:
        acc, lay = r['acc0'], r['layer0']
        if acc and extra and not r['v4'] and S.refsubj(r['sk'], r['answer'], r['reference'], extra):
            acc, lay = False, 'AGv5'; ag_new.append(r)
        if (not acc) and tip and S.tip_det_rule(r['sk'], r['answer'], r['reference'], lay):
            acc, lay = True, 'TIPdet'; tip_new.append(r)
        res.append(dict(r, acc=acc, layer=lay))
    return res, ag_new, tip_new


def ag_fires(rows, extra):
    """v5-only fires (v4 silent) regardless of the stored accept - the guard's own cost."""
    f = [r for r in rows if not r['v4'] and S.refsubj(r['sk'], r['answer'], r['reference'], extra)]
    return {'fires': len(f), 'catches': sum(r['judged'] == 'wrong' for r in f),
            'cost': [r['id'] for r in f if r['judged'] == 'correct'],
            'cost_detail': [(r['id'], r['answer']) for r in f if r['judged'] == 'correct']}


def packet(extra):
    orig = G.V4.decide
    def W(sk, ann, wtags, answer, reference, variant='primary', flags=G.V4.ALL_FLAGS):
        return S.decide(sk, ann, wtags, answer, reference, variant, flags, extra)
    G.V4.decide = W
    try:
        b = G.packet_gate([(G.CHOSEN, dict(G.CONFIGS)[G.CHOSEN])])[G.CHOSEN]
        ok = G.gate_ok(b)
    finally:
        G.V4.decide = orig
    return ok, {k: {kk: vv for kk, vv in v.items() if kk in ('fired', 'n')} for k, v in b.items()
                if isinstance(v, dict)}


def main():
    u = load_1u(); t, tnotes, tkeys = load_1t()
    log = {'model_calls': 0, 'sets': {'1U': len(u), '1T': len(t)}, 't_notes': tnotes,
           't_row_keys': tkeys}
    sets = {'1U': u, '1T': t}
    # A1 candidates (selected on measured cost, then 1S packet catches)
    cands = {}
    for ex in (('rs_pass',), ('rs_nom',), ('rs_pass', 'rs_nom')):
        ok, pk = packet(ex)
        cands['+'.join(ex)] = {'gate_pass': ok, 'packet': pk,
                               'closed': {k: ag_fires(v, ex) for k, v in sets.items()}}
    log['A1_candidates'] = cands
    def keyf(n):
        c = cands[n]
        return (sum(len(c['closed'][k]['cost']) for k in c['closed']),
                -sum(c['closed'][k]['fires'] for k in c['closed']))
    elig = [n for n in cands if cands[n]['gate_pass'] and all(len(cands[n]['closed'][k]['cost']) == 0
                                                             for k in sets)]
    chosen = min(elig, key=keyf) if elig else None
    log['A1_chosen'] = chosen
    # A2(b) TIP rule measured alone
    tipm = {}
    for k, v in sets.items():
        _, _, tn = apply(v, (), True)
        tipm[k] = {'overturned': len(tn), 'gain_correct': [r['id'] for r in tn if r['judged'] == 'correct'],
                   'cost_wrong': [r['id'] for r in tn if r['judged'] == 'wrong'],
                   'TIPrej_total': sum(1 for r in v if r['layer0'] == 'L3:TIPrej'),
                   'TIPrej_correct_det': sum(1 for r in v if r['layer0'] == 'L3:TIPrej'
                                             and r['judged'] == 'correct' and 'determiner' in r['tags'])}
    log['A2b_tip_rule'] = tipm
    # A3 loop
    rounds, prev = [], {k: metrics(apply(v, (), False)[0]) for k, v in sets.items()}
    rounds.append({'round': 0, 'fix': 'baseline (1U stored stack; 1T stored + AG v4)', 'metrics': prev,
                   'calls': 0})
    plan = [('AG v5 ' + (chosen or 'NONE ELIGIBLE'), (tuple(chosen.split('+')) if chosen else ()), False),
            ('TIP determiner rule', (tuple(chosen.split('+')) if chosen else ()), True)]
    stop, attacked, gains = None, ['FA', 'coverage'], []
    for i, (name, ex, tip) in enumerate(plan, 1):
        cur = {k: metrics(apply(v, ex, tip)[0]) for k, v in sets.items()}
        bad = {k: worse(cur[k], prev[k]) for k in sets}
        costs = {k: (len(ag_fires(sets[k], ex)['cost']) if ex else 0) for k in sets}
        tipcost = {k: len(tipm[k]['cost_wrong']) if tip else 0 for k in sets}
        m = attacked[i - 1]
        gain = {k: round((cur[k][m]['pct'] - prev[k][m]['pct']) * (-1 if m == 'FA' else 1), 2) for k in sets}
        gains.append(max(gain.values()))
        rec = {'round': i, 'fix': name, 'metric_attacked': m, 'gain_points': gain, 'metrics': cur,
               'worse_cells': bad, 'ag_v5_cost_vs_v4': costs, 'tip_cost_wrong_accepted': tipcost,
               'calls': 0, 'status': 'kept'}
        reasons = []
        if any(bad.values()):
            reasons.append('a headline metric or named cell got worse: %s' % bad)
        if any(c > 2 for c in costs.values()) or any(c > 2 for c in tipcost.values()):
            reasons.append('guard measured cost > 2')
        if len(gains) >= 2 and all(g < 1 for g in gains[-2:]):
            reasons.append('two consecutive rounds gained < 1 point on the attacked metric')
        if reasons:
            rec['status'] = 'REVERTED + STOP'; rec['stop_reasons'] = reasons
            rounds.append(rec); stop = reasons; break
        rounds.append(rec); prev = cur
    if not stop:
        rounds.append({'round': 3, 'fix': 'A2(a) L3 determiner PROMPT line', 'status': 'NOT RUN',
                       'calls': 0, 'why': 'not run in this track (0 of 200 loop calls spent)'})
    log['rounds'] = rounds; log['stop'] = stop
    json.dump(log, open(os.path.join(HERE, 'rounds.json'), 'w'), indent=1, ensure_ascii=False)
    L = ['| round | fix | set | coverage | FA | FA T | FA W | FA M | FA S | status |', '|' + '---|' * 10]
    for r in rounds:
        for k in ('1U', '1T'):
            if 'metrics' not in r:
                L.append('| %s | %s | - | - | - | - | - | - | - | %s |' % (r['round'], r['fix'], r['status'])); break
            mm = r['metrics'][k]; f = lambda d: '%d/%d = %.2f %% [%.2f, %.2f]' % (d['k'], d['n'], d['pct'], *d['ci'])
            ty = lambda t: ('%d/%d' % (mm['FA_by_type'][t]['k'], mm['FA_by_type'][t]['n'])) if t in mm['FA_by_type'] else '-'
            L.append('| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (r['round'], r['fix'], k, f(mm['coverage']),
                     f(mm['FA']), ty('T'), ty('W'), ty('M'), ty('S'), r.get('status', 'baseline')))
    open(os.path.join(HERE, 'ROUNDS.md'), 'w').write('# Phase 1V Track A3 rounds (closed sets, 0 calls)\n\n' + '\n'.join(L) + '\n')
    print(json.dumps({k: log[k] for k in ('sets', 't_notes', 't_row_keys', 'A1_chosen', 'stop')}, ensure_ascii=False))
    for n, c in cands.items():
        print('CAND', n, 'gate', c['gate_pass'], json.dumps(c['packet']), {k: (v['fires'], v['catches'], v['cost_detail']) for k, v in c['closed'].items()})
    print('TIP', json.dumps(tipm))
    print('\n'.join(L))
    for r in rounds:
        print('R', r['round'], r.get('status'), r.get('gain_points'), r.get('worse_cells'), r.get('stop_reasons'))


if __name__ == '__main__':
    main()

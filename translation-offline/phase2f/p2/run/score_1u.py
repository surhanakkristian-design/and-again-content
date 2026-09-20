#!/usr/bin/env python3
"""Phase 1U scoring - 0 model calls, 0 network.  Reads the stored rows (results_1u.json, which the
runner writes from the stored verdicts) and the judge labels; also usable for crash recovery.

    PYTHONDONTWRITEBYTECODE=1 python3 phase1u/run/score_1u.py
    PYTHONDONTWRITEBYTECODE=1 python3 phase1u/run/score_1u.py --recover   # rebuild rows, 0 calls
    PYTHONDONTWRITEBYTECODE=1 python3 phase1u/run/score_1u.py --selftest

Coverage = judged-correct accepted / judged-correct.  FA = judged-wrong accepted / judged-wrong.
Every figure k/n with an exact 95 % Clopper-Pearson interval; P1 = odd sid, P2 = even sid; Fisher
exact P1 vs P2; both targets stated on the POINT and on the INTERVAL, pooled / P1 / P2, never
averaged.  The statistics come from phase1t/run/score_1t.py (cp, kn, fisher_exact), unchanged.
"""
import argparse
import collections
import json
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
P1U = os.path.dirname(HERE)
TOFF = os.path.expanduser('~/Projects/and-again-content/translation-offline')
for _p in (HERE, os.path.join(TOFF, 'phase1t', 'run'), os.path.join(TOFF, 'phase1s')):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import score_1t as S                                                          # noqa: E402
from safe_json import safe_dump                                               # noqa: E402

cp, kn, fisher = S.cp, S.kn, S.fisher_exact
TYPES = ('T', 'W', 'M', 'S')
DROP = collections.OrderedDict([('drop-main', 'main'), ('drop-fronted', 'fronted'),
                                ('drop-misaligned', 'misaligned'), ('drop-other', 'other')])
SHADOWS = ('v2', 'v3', 'guarded_union', 'v4_full')
COV_TARGET, FA_TARGET = 90.0, 5.0
PRICE_IN_USD_PER_M, PRICE_OUT_USD_PER_M = 0.10, 0.40       # published flash-lite list price


# ------------------------------------------------------------------ labels
def base_label(r):
    return r.get('judged') if r.get('judged') in ('correct', 'wrong') else None


def writer_label(r):
    return {'C': 'correct', 'W': 'wrong'}.get(r.get('kind'))


def topup(rows, want, n_min=20):
    """S2/S3 top-up: lowest confidence first, ties by packet position, earliest first."""
    return sorted(rows, key=lambda r: ((r.get('confidence') if r.get('confidence') is not None
                                        else 99),
                                       (r.get('packet_position') if r.get('packet_position')
                                        is not None else 10 ** 9), r['item_id']))[:max(0, n_min
                                                                                       - want)]


def s_sets(rows):
    """The two pre-declared borderline sets, with their top-ups (n >= 20 by construction)."""
    wro = [r for r in rows if base_label(r) == 'wrong']
    cor = [r for r in rows if base_label(r) == 'correct']
    s2 = [r for r in wro if r.get('borderline')]
    s2 += topup([r for r in wro if not r.get('borderline')], len(s2))
    s3 = [r for r in cor if r.get('borderline')]
    s3 += topup([r for r in cor if not r.get('borderline')], len(s3))
    return {r['item_id'] for r in s2}, {r['item_id'] for r in s3}


def labellers(rows):
    """name -> (label function, row filter, description).  All six are non-empty by construction."""
    S2, S3 = s_sets(rows)
    art = {r['item_id'] for r in rows
           if 'missing-article' in (r.get('tags') or []) and base_label(r) == 'wrong'}
    lv = sorted({r['level'] for r in rows if r.get('level')})
    out = collections.OrderedDict()
    out['headline'] = (base_label, lambda r: True, 'the judge labels on every labelled item')
    out['S1_writer_intent'] = (writer_label, lambda r: True,
                               'scored by the writer kind C/W instead of the judge label')
    out['S2_wrong_borderline_correct'] = (
        lambda r: 'correct' if r['item_id'] in S2 else base_label(r), lambda r: True,
        'judged-wrong borderline (topped up to n>=20 by lowest confidence, ties by packet '
        'position) scored correct')
    out['S3_correct_borderline_wrong'] = (
        lambda r: 'wrong' if r['item_id'] in S3 else base_label(r), lambda r: True,
        'judged-correct borderline (same top-up) scored wrong')
    out['S4_exclude_S2_S3'] = (base_label, lambda r: r['item_id'] not in (S2 | S3),
                               'the S2 and S3 item sets excluded from the denominator')
    out['S5_article_pre_ruling'] = (
        lambda r: 'correct' if r['item_id'] in art else base_label(r), lambda r: True,
        'every missing-article item the judge called wrong scored correct (the 1T M1 reading)')
    for x in lv:
        out['S6_leave_out_%s' % x] = (base_label, (lambda r, x=x: r['level'] != x),
                                      'leave-one-level-out: %s dropped' % x)
    moved = {'S2_wrong_borderline_correct': sorted(S2), 'S3_correct_borderline_wrong': sorted(S3),
             'S4_exclude_S2_S3': sorted(S2 | S3), 'S5_article_pre_ruling': sorted(art),
             'S1_writer_intent': sorted(r['item_id'] for r in rows
                                        if base_label(r) != writer_label(r))}
    for x in lv:
        moved['S6_leave_out_%s' % x] = sorted(r['item_id'] for r in rows if r['level'] == x)
    return out, moved


# ------------------------------------------------------------------ blocks
def targets(d, kind):
    if not d['n']:
        return {'point': None, 'interval': None}
    if kind == 'coverage':
        return {'point': 'MET' if d['pct'] >= COV_TARGET else 'MISSED',
                'interval': 'MET' if d['ci'][0] >= COV_TARGET else 'MISSED',
                'rule': 'coverage >= 90 %'}
    return {'point': 'MET' if d['pct'] < FA_TARGET else 'MISSED',
            'interval': 'MET' if d['ci'][1] < FA_TARGET else 'MISSED', 'rule': 'FA < 5 %'}


def pack(rows, lf):
    cor = [r for r in rows if lf(r) == 'correct']
    wro = [r for r in rows if lf(r) == 'wrong']
    cov = kn(sum(1 for r in cor if r['final_accept']), len(cor))
    fa = kn(sum(1 for r in wro if r['final_accept']), len(wro))
    cov['target'], fa['target'] = targets(cov, 'coverage'), targets(fa, 'fa')
    return {'coverage': cov, 'fa': fa}


def halves(rows, lf):
    d = {'pooled': pack(rows, lf),
         'P1': pack([r for r in rows if int(r['sid']) % 2 == 1], lf),
         'P2': pack([r for r in rows if int(r['sid']) % 2 == 0], lf)}
    for m in ('coverage', 'fa'):
        a, b = d['P1'][m], d['P2'][m]
        d.setdefault('fisher_P1_vs_P2', {})[m] = round(
            fisher(a['k'], a['n'] - a['k'], b['k'], b['n'] - b['k']), 4)
    d['n_rows'] = len(rows)
    return d


def tagged(rows, tags):
    return [r for r in rows if set(r.get('tags') or []) & set(tags)]


def cells(rows, lf):
    out = collections.OrderedDict()
    art = tagged(rows, ('missing-article',))
    aw = [r for r in art if lf(r) == 'wrong']
    ac = [r for r in art if lf(r) == 'correct']
    out['missing_article'] = {
        'judged_wrong_n': len(aw),
        'fa': kn(sum(1 for r in aw if r['final_accept']), len(aw)),
        'rejected_by_layer': dict(collections.Counter(r['final_layer'] for r in aw
                                                      if not r['final_accept'])),
        'judged_correct_n': len(ac),
        'coverage': kn(sum(1 for r in ac if r['final_accept']), len(ac))}
    ad = collections.OrderedDict()
    allw = [r for r in rows if lf(r) == 'wrong' and set(r.get('tags') or []) & set(DROP)]
    ad['all'] = dict(kn(sum(1 for r in allw if r['final_accept']), len(allw)),
                     ag_fired=sum(1 for r in allw if r['ag']['fired']))
    for tag, name in DROP.items():
        sub = [r for r in rows if lf(r) == 'wrong' and tag in (r.get('tags') or [])]
        ad[name] = dict(kn(sum(1 for r in sub if r['final_accept']), len(sub)),
                        ag_fired=sum(1 for r in sub if r['ag']['fired']))
    out['agent_drop_fa'] = ad
    bp = [r for r in tagged(rows, ('by-passive', 'by-passive-embedded')) if lf(r) == 'correct']
    out['by_passive_coverage'] = dict(kn(sum(1 for r in bp if r['final_accept']), len(bp)),
                                      expectation='100 %',
                                      rejected=[r['item_id'] for r in bp if not r['final_accept']])
    skp = [r for r in tagged(rows, ('skp-passive',)) if lf(r) == 'correct']
    out['skp_coverage'] = dict(kn(sum(1 for r in skp if r['final_accept']), len(skp)),
                               ag_fired=[r['item_id'] for r in skp if r['ag']['fired']])
    tf = [r for r in tagged(rows, ('time-frame', 'timeframe')) if lf(r) == 'wrong']
    out['time_frame_fa'] = kn(sum(1 for r in tf if r['final_accept']), len(tf))
    return out


def ag_block(rows, lf):
    fired = [r for r in rows if r['ag']['fired']]
    cost = [r for r in fired if lf(r) == 'correct']
    d = {'primary_v4': {
        'fired': len(fired),
        'catches_judged_wrong': sum(1 for r in fired if lf(r) == 'wrong'),
        'measured_cost_judged_correct': len(cost),
        'cost_items': [{'item_id': r['item_id'], 'sid': r['sid'], 'tags': r['tags'],
                        'level': r['level'], 'answer': r['answer'],
                        'reason': r['ag']['reason']} for r in cost]}}
    sh = {}
    for name in SHADOWS:
        f = [r for r in rows if (r.get('ag_shadow') or {}).get(name, {}).get('fired')]
        sh[name] = {'fired': len(f),
                    'catches_judged_wrong': sum(1 for r in f if lf(r) == 'wrong'),
                    'cost_judged_correct': sum(1 for r in f if lf(r) == 'correct'),
                    'fired_where_v4_did_not': sum(1 for r in f if not r['ag']['fired']),
                    'v4_fires_where_it_did_not': sum(
                        1 for r in rows if r['ag']['fired']
                        and not (r.get('ag_shadow') or {}).get(name, {}).get('fired'))}
    d['shadows_offline'] = sh
    return d


def detail(rows, lf):
    d = {'by_level': {x: pack([r for r in rows if r['level'] == x], lf)
                      for x in sorted({r['level'] for r in rows if r.get('level')})},
         'fa_by_judged_type': {t: kn(sum(1 for r in rows if lf(r) == 'wrong'
                                         and r.get('judged_type') == t and r['final_accept']),
                                     sum(1 for r in rows if lf(r) == 'wrong'
                                         and r.get('judged_type') == t)) for t in TYPES},
         'false_accepts_by_layer': dict(collections.Counter(
             r['final_layer'] for r in rows if lf(r) == 'wrong' and r['final_accept'])),
         'false_rejections_by_layer': dict(collections.Counter(
             r['final_layer'] for r in rows if lf(r) == 'correct' and not r['final_accept'])),
         'true_rejections_by_layer': dict(collections.Counter(
             r['final_layer'] for r in rows if lf(r) == 'wrong' and not r['final_accept'])),
         'false_accepts': [_li(r) for r in rows if lf(r) == 'wrong' and r['final_accept']],
         'false_rejections': [_li(r) for r in rows if lf(r) == 'correct' and not r['final_accept']],
         'failed_calls': [_li(r) for r in rows if r.get('call_failed')]}
    return d


def _li(r):
    return {'item_id': r['item_id'], 'sid': r['sid'], 'slovak': r.get('sk'),
            'answer': r.get('answer'), 'layer': r['final_layer'], 'tags': r.get('tags'),
            'judged': r.get('judged'), 'type': r.get('judged_type'), 'level': r.get('level'),
            'model': (r.get('layers') or {}).get('model'), 'ag_fired': r['ag']['fired'],
            'call_failed': bool(r.get('call_failed'))}


def model_block(res):
    rows = res.get('rows') or []
    m = collections.Counter((r.get('layers') or {}).get('model') for r in rows
                            if (r.get('layers') or {}).get('model'))
    c = res.get('calls') or {}
    ti, to = c.get('tokens_in') or 0, c.get('tokens_out') or 0
    spend = ti / 1e6 * PRICE_IN_USD_PER_M + to / 1e6 * PRICE_OUT_USD_PER_M
    return {'model_replies': dict(m), 'failed_calls': sum(1 for r in rows if r.get('call_failed')),
            'counted_calls': c.get('counted_calls'), 'tokens_in': ti, 'tokens_out': to,
            'latency_ms_total': c.get('latency_ms_total'),
            'latency_ms_mean': c.get('latency_ms_mean'),
            'spend_usd_upper_bound': round(spend, 4),
            'price_note': 'UPPER BOUND at the published flash-lite list price '
                          '($%.2f/1M in, $%.2f/1M out); free-tier calls cost 0'
                          % (PRICE_IN_USD_PER_M, PRICE_OUT_USD_PER_M)}


# ------------------------------------------------------------------ scoring
def score(res):
    rows = [r for r in (res.get('rows') or []) if base_label(r) or writer_label(r)]
    lab = [r for r in rows if base_label(r)]
    lfs, moved = labellers(lab)
    out = collections.OrderedDict()
    out['phase'] = '1U'
    out['prompt'] = res.get('prompt')
    out['freeze_commit'] = res.get('freeze_commit')
    out['stub_model'] = res.get('stub_model')
    out['n_rows'] = len(res.get('rows') or [])
    out['n_labelled'] = len(lab)
    out['preflight'] = res.get('preflight')
    out['floors'] = res.get('floors')
    out['prompt_assertion'] = res.get('prompt_assertion')
    out['model'] = model_block(res)
    out['failed_call_rule'] = ('an empty or unparsable HTTP 200 reply is a FAILED call: it is '
                               'counted against the cap, never guessed and never silently '
                               'retried; the item keeps the stack decision it gets without a '
                               'model verdict (a rejection), stays in its own denominator and is '
                               'listed under detail.failed_calls')
    empty = []
    for name, (lf, flt, desc) in lfs.items():
        sub = [r for r in (lab if name != 'S1_writer_intent' else rows) if flt(r)]
        blk = halves(sub, lf)
        blk['definition'] = desc
        blk['n_moved'] = len(moved.get(name, [])) if name != 'headline' else 0
        blk['moved_items'] = moved.get(name, [])[:50] if name != 'headline' else []
        out[name] = blk
        if name != 'headline' and not moved.get(name):
            empty.append(name)
    if empty:
        out['SENSITIVITY_EMPTY'] = empty
    hl = [r for r in lab]
    out['cells'] = cells(hl, base_label)
    out['ag'] = ag_block(hl, base_label)
    out['detail'] = detail(hl, base_label)
    out['judge_noise_duplicates'] = (res.get('label_meta') or {}).get('label_join')
    out['selftest_statistics'] = S.selftest()
    return out, empty


def f(d):
    return '-' if not d or not d['n'] else '%d/%d = %.2f %% [%.2f, %.2f]' % (
        d['k'], d['n'], d['pct'], d['ci'][0], d['ci'][1])


def t(d):
    return '-' if not d or not d.get('target') else '%s on the point, %s on the interval' % (
        d['target']['point'], d['target']['interval'])


def write_md(out, path):
    L = ['# SCORE_1U - the fresh 1U set (AG v4, P-FROZEN-1U), 0 model calls', '',
         'Coverage = judged-correct accepted / judged-correct.  FA = judged-wrong accepted / '
         'judged-wrong.  Exact 95 % Clopper-Pearson; P1 = odd sid, P2 = even sid; never averaged.',
         '', '## headline (the judge labels)', '',
         '| figure | k/n, point, 95 % CI | target |', '| --- | --- | --- |']
    h = out['headline']
    for nm, a, b in (('coverage pooled', 'pooled', 'coverage'), ('FA pooled', 'pooled', 'fa'),
                     ('coverage P1', 'P1', 'coverage'), ('FA P1', 'P1', 'fa'),
                     ('coverage P2', 'P2', 'coverage'), ('FA P2', 'P2', 'fa')):
        L.append('| %s | %s | %s |' % (nm, f(h[a][b]), t(h[a][b])))
    L += ['| Fisher P1 vs P2 (coverage) | p = %s | |' % h['fisher_P1_vs_P2']['coverage'],
          '| Fisher P1 vs P2 (FA) | p = %s | |' % h['fisher_P1_vs_P2']['fa'], '',
          '## cells, one per line', '']
    c = out['cells']
    L += ['* missing-article, judged wrong: FA %s, rejected by layer %s'
          % (f(c['missing_article']['fa']), json.dumps(c['missing_article']['rejected_by_layer'],
                                                       sort_keys=True)),
          '* missing-article, judged correct: n = %d, coverage %s'
          % (c['missing_article']['judged_correct_n'], f(c['missing_article']['coverage']))]
    for k in ('all', 'main', 'fronted', 'misaligned', 'other'):
        L.append('* agent-drop FA (%s, writer tag among judged-wrong): %s (AG fired %d)'
                 % (k, f(c['agent_drop_fa'][k]), c['agent_drop_fa'][k]['ag_fired']))
    L += ['* by-passive coverage: %s' % f(c['by_passive_coverage']),
          '* SKP coverage: %s' % f(c['skp_coverage']),
          '* time-frame FA: %s' % f(c['time_frame_fa']),
          '* AG v4: fired %d, catches %d, measured cost (judged-correct rejected) %d'
          % (out['ag']['primary_v4']['fired'], out['ag']['primary_v4']['catches_judged_wrong'],
             out['ag']['primary_v4']['measured_cost_judged_correct'])]
    for n in SHADOWS:
        s = out['ag']['shadows_offline'][n]
        L.append('* AG shadow %s (offline, same items): fired %d, catches %d, cost %d'
                 % (n, s['fired'], s['catches_judged_wrong'], s['cost_judged_correct']))
    d = out['detail']
    L += ['* false accepts by layer: %s' % json.dumps(d['false_accepts_by_layer'], sort_keys=True),
          '* false rejections by layer: %s' % json.dumps(d['false_rejections_by_layer'],
                                                         sort_keys=True),
          '* true rejections by layer: %s' % json.dumps(d['true_rejections_by_layer'],
                                                        sort_keys=True)]
    for ty in TYPES:
        L.append('* FA, judged type %s: %s' % (ty, f(d['fa_by_judged_type'][ty])))
    for lv, v in sorted(d['by_level'].items()):
        L.append('* level %s: coverage %s, FA %s' % (lv, f(v['coverage']), f(v['fa'])))
    m = out['model']
    L += ['* model replies: %s; failed calls %s' % (json.dumps(m['model_replies'], sort_keys=True),
                                                    m['failed_calls']),
          '* tokens in/out %s/%s, latency mean %s ms, spend <= $%s (%s)'
          % (m['tokens_in'], m['tokens_out'], m['latency_ms_mean'], m['spend_usd_upper_bound'],
             m['price_note']),
          '* judge noise on the 80 duplicate controls: %s'
          % json.dumps(out['judge_noise_duplicates'])[:400], '',
          '## pre-declared sensitivities (SPLIT_1U.md S1-S6)', '',
          '| sensitivity | n moved | coverage pooled | FA pooled | coverage P1 / P2 | FA P1 / P2 |',
          '| --- | --- | --- | --- | --- | --- |']
    for k in out:
        if not k.startswith('S1_') and not k.startswith('S2_') and not k.startswith('S3_') \
                and not k.startswith('S4_') and not k.startswith('S5_') and not k.startswith('S6_'):
            continue
        b = out[k]
        L.append('| %s | %d | %s | %s | %s / %s | %s / %s |'
                 % (k, b['n_moved'], f(b['pooled']['coverage']), f(b['pooled']['fa']),
                    f(b['P1']['coverage']), f(b['P2']['coverage']), f(b['P1']['fa']),
                    f(b['P2']['fa'])))
    L += ['', '### targets under each sensitivity (point / interval)', '']
    for k in out:
        if k[:2] in ('S1', 'S2', 'S3', 'S4', 'S5', 'S6') and isinstance(out[k], dict) \
                and 'pooled' in out[k]:
            L.append('* %s: coverage %s; FA %s' % (k, t(out[k]['pooled']['coverage']),
                                                   t(out[k]['pooled']['fa'])))
    L += ['', '## every false accept', '', '| item | sid | layer | tags | Slovak | answer |',
          '| --- | --- | --- | --- | --- | --- |']
    for r in d['false_accepts']:
        L.append('| %s | %s | %s | %s | %s | %s |' % (r['item_id'], r['sid'], r['layer'],
                                                      ','.join(r['tags'] or []), r['slovak'],
                                                      r['answer']))
    L += ['', '## every false rejection', '', '| item | sid | layer | tags | Slovak | answer |',
          '| --- | --- | --- | --- | --- | --- |']
    for r in d['false_rejections']:
        L.append('| %s | %s | %s | %s | %s | %s |' % (r['item_id'], r['sid'], r['layer'],
                                                      ','.join(r['tags'] or []), r['slovak'],
                                                      r['answer']))
    L += ['', '## failed calls (counted, never guessed, never silently retried)', '',
          '```', json.dumps(d['failed_calls'], indent=1)[:2000], '```',
          '', out['failed_call_rule'], '']
    open(path, 'w', encoding='utf-8').write('\n'.join(L) + '\n')


def run(results_path, out_dir=None):
    out_dir = out_dir or os.path.dirname(os.path.abspath(results_path))
    res = json.load(open(results_path, encoding='utf-8'))
    out, empty = score(res)
    safe_dump(out, os.path.join(out_dir, 'score_1u.json'))
    write_md(out, os.path.join(out_dir, 'SCORE_1U.md'))
    print(json.dumps({'coverage': out['headline']['pooled']['coverage'],
                      'fa': out['headline']['pooled']['fa'],
                      'empty_sensitivities': empty}, indent=1))
    if empty:
        raise SystemExit('REFUSED: a pre-declared sensitivity moved 0 items: %s' % empty)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--results', default=os.path.join(HERE, 'results_1u.json'))
    ap.add_argument('--recover', action='store_true')
    ap.add_argument('--data-dir', default=None)
    ap.add_argument('--selftest', action='store_true')
    a = ap.parse_args()
    bad = [x for x in S.selftest() if not x['ok']]
    if bad:
        raise SystemExit('REFUSED: the statistics self-test failed: %s' % json.dumps(bad))
    if a.selftest:
        import selftest_1u_run as T
        return T.scorer_selftest()
    if a.recover:
        import runner_1u as RU
        RU.final_core(HERE, a.data_dir, offline=True)
    if not os.path.exists(a.results):
        raise SystemExit('REFUSED: %s does not exist - the run has not written its rows yet.'
                         % a.results)
    return run(a.results)



# Phase 2F Part 2 - S7, as 1W declared it: determiner-difference items judged CORRECT rescored
# as WRONG.
_labellers_1u = labellers


def labellers(rows):
    out, moved = _labellers_1u(rows)
    det = {r['item_id'] for r in rows
           if 'determiner' in (r.get('tags') or []) and base_label(r) == 'correct'}
    out['S7_determiner_correct_as_wrong'] = (
        lambda r: 'wrong' if r['item_id'] in det else base_label(r), lambda r: True,
        'determiner-difference items (writer tag determiner) judged CORRECT rescored as WRONG')
    moved['S7_determiner_correct_as_wrong'] = sorted(det)
    return out, moved


if __name__ == '__main__':
    main()

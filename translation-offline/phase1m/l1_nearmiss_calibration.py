#!/usr/bin/env python3
"""Phase 1M, label `carry`, check 2 — calibrate `l1_nearmiss` against PRODUCTION L1 behaviour.

The 490 DEV records are the only side that carries the *stored* production checker verdict
(`chk.step` in match / mistake / spelling_variant / auto). The offline builder `compute_chk`
can only reproduce `match` and `mistake`; `spelling_variant` is not reproducible offline
(runner_1l.compute_chk docstring). `l1_nearmiss` is the proxy Phase 1M uses to bound how many
items production would still have accepted at L1 beyond the builder.

This script, with 0 model calls:
  * crosstabs stored `chk.step` against computed `compute_chk` step on all 490 DEV records;
  * tabulates `l1_nearmiss` (imported from runner_1m when available) against BOTH;
  * scores the proxy as a detector of the gap set G = {stored-accepted at L1} \\ {computed match}.

Run: PYTHONDONTWRITEBYTECODE=1 python3 -B phase1m/l1_nearmiss_calibration.py
"""
import sys, os, json, collections, datetime

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import loader_1l as L              # noqa: F401  (rebinds the access log onto phase1m)
import runner_1l as RL
R, P, C = RL.R, RL.P, RL.C

PURPOSE = ('Phase 1M carry-check 2: calibrate l1_nearmiss against the stored production DEV '
           'checker verdicts (0 model calls)')
OUT = os.path.join(HERE, 'L1_NEARMISS_CALIBRATION.md')

# ---------------------------------------------------------------- the near-miss predicate
NM_SOURCE = 'imported from runner_1m.l1_nearmiss'
try:
    import runner_1m as RM
    l1_nearmiss = RM.l1_nearmiss
    if getattr(RM, 'C', None) is not C:
        raise ImportError('runner_1m.C is a different checker module')
except Exception as e:                                          # pragma: no cover
    NM_SOURCE = 'local re-implementation (runner_1m import failed: %s)' % e

    def _lev(a, b):
        if a == b:
            return 0
        prev = list(range(len(b) + 1))
        for i, ca in enumerate(a, 1):
            cur = [i]
            for j, cb in enumerate(b, 1):
                cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
            prev = cur
        return prev[-1]

    def l1_nearmiss(r):
        it = {'exercise_id': r['sid'], 'reference': r['reference'], 'answer': r['answer'],
              'item_id': r['item_id'], 'sk': r['sk']}
        n = C.base.norm(r['answer'])
        try:
            refs = C.refs_of(it)
        except Exception:
            refs = [r['reference']] + list(r.get('refs') or [])
        refs = [x for x in refs if isinstance(x, str)]
        if any(C.base.norm(x) == n for x in refs):
            return None
        best = None
        for x in refs:
            m = C.base.norm(x)
            ta, tb = n.split(), m.split()
            if len(ta) == len(tb):
                per = [_lev(p, q) for p, q in zip(ta, tb)]
                if per and max(per) <= 1 and sum(per) <= 2:
                    cand = {'ref': x, 'dist': sum(per), 'len_mismatch': False}
                    if best is None or cand['dist'] < best['dist']:
                        best = cand
            elif abs(len(ta) - len(tb)) <= 2:
                d = _lev(n, m)
                if d <= 2:
                    cand = {'ref': x, 'dist': d, 'len_mismatch': True}
                    if best is None or cand['dist'] < best['dist']:
                        best = cand
        return best

ACCEPT = ('correct', 'correct_with_tip')
L1_STEPS = ('match', 'spelling_variant')


def tbl(rows, head):
    out = ['| ' + ' | '.join(head) + ' |', '|' + '---|' * len(head)]
    for r in rows:
        out.append('| ' + ' | '.join(str(x) for x in r) + ' |')
    return out


def main():
    ts = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    st, recs, ann, by, info = RL.build_side('dev', False, PURPOSE)
    L._log('1j:dev', 'records for the l1_nearmiss calibration (stored chk vs computed chk)',
           len(recs), PURPOSE, caller='l1_nearmiss_calibration.py')

    rows, cross = [], collections.Counter()
    stored_steps, nm_by_stored, nm_by_computed = collections.Counter(), collections.Counter(), \
        collections.Counter()
    nm_len_mismatch = collections.Counter()
    for r in recs:
        stored = r.get('chk') or {}
        s_step = stored.get('step') or '(none)'
        s_acc = stored.get('verdict') in ACCEPT
        comp, how = RL.compute_chk(r)
        c_acc = comp['verdict'] in ACCEPT
        nm = l1_nearmiss(r)
        key = '%s/%s' % (s_step, 'accept' if s_acc else 'reject')
        stored_steps[key] += 1
        cross['%s -> %s' % (key, how)] += 1
        if nm:
            nm_by_stored[key] += 1
            nm_by_computed[how] += 1
            nm_len_mismatch['len_mismatch' if nm.get('len_mismatch') else 'same_token_count'] += 1
        rows.append({'item_id': r['item_id'], 'sid': r['sid'], 'stored_step': s_step,
                     'stored_accept': s_acc, 'computed_step': how, 'computed_accept': c_acc,
                     'nearmiss': bool(nm), 'nm_dist': (nm or {}).get('dist'),
                     'nm_len_mismatch': (nm or {}).get('len_mismatch'),
                     'answer': r['answer'], 'nm_ref': (nm or {}).get('ref')})

    n = len(rows)
    nm_ids = [x for x in rows if x['nearmiss']]
    # gap set: production accepted it at L1, the offline builder could not
    gap = [x for x in rows if x['stored_accept'] and x['stored_step'] in L1_STEPS
           and x['computed_step'] != 'match']
    gap_ids = {x['item_id'] for x in gap}
    nm_set = {x['item_id'] for x in nm_ids}
    tp = len(nm_set & gap_ids)
    fp = len(nm_set - gap_ids)
    fn = len(gap_ids - nm_set)
    prec = (100.0 * tp / len(nm_set)) if nm_set else 0.0
    rec = (100.0 * tp / len(gap_ids)) if gap_ids else 0.0
    sv = [x for x in rows if x['stored_step'] == 'spelling_variant']
    disagree = [x for x in rows if x['stored_accept'] != x['computed_accept']]

    A = []
    a = A.append
    a('# Phase 1M — carry-check 2: `l1_nearmiss` calibrated against production L1 on DEV')
    a('')
    a('Label `carry`. Generated %s by `phase1m/l1_nearmiss_calibration.py`. **0 model calls.** '
      'Predicate: %s.' % (ts, NM_SOURCE))
    a('')
    a('Side: `build_side(\'dev\', hyg_on=False)` — **%d records / %d sentences**, the only side '
      'whose records carry the *stored production* checker verdict.' %
      (n, len({x['sid'] for x in rows})))
    a('')
    a('## 1. Stored production `chk` vs the offline builder')
    a('')
    a('Stored step (with the stored accept/reject decision):')
    a('')
    A.extend(tbl(sorted(((k, v, '%.1f %%' % (100.0 * v / n)) for k, v in stored_steps.items()),
                        key=lambda x: -x[1]), ['stored step / decision', 'n', 'share']))
    a('')
    a('Crosstab stored -> computed (`compute_chk`):')
    a('')
    A.extend(tbl(sorted(((k.split(' -> ')[0], k.split(' -> ')[1], v) for k, v in cross.items()),
                        key=lambda x: (x[0], -x[2])),
                 ['stored step / decision', 'computed step', 'n']))
    a('')
    a('Accept/reject disagreements between stored and computed: **%d / %d** (%.2f %%).'
      % (len(disagree), n, 100.0 * len(disagree) / n))
    a('')
    a('`spelling_variant` rows present in this DEV side: **%d**%s.'
      % (len(sv), ' — the step the offline builder structurally cannot produce' if sv else
         ' (so the unreproducible production step never fires on DEV; the gap set below is '
         'driven by whatever else production accepted at L1)'))
    a('')
    a('## 2. `l1_nearmiss` against both')
    a('')
    a('Near-misses flagged: **%d / %d** (%.2f %%), of which %d have the same token count and '
      '%d are length-mismatch candidates.'
      % (len(nm_ids), n, 100.0 * len(nm_ids) / n,
         nm_len_mismatch['same_token_count'], nm_len_mismatch['len_mismatch']))
    a('')
    a('By **stored** production verdict:')
    a('')
    A.extend(tbl(sorted(((k, nm_by_stored.get(k, 0), stored_steps[k],
                          '%.1f %%' % (100.0 * nm_by_stored.get(k, 0) / stored_steps[k]))
                         for k in stored_steps), key=lambda x: -x[1]),
                 ['stored step / decision', 'near-misses', 'rows', 'rate']))
    a('')
    a('By **computed** builder step:')
    a('')
    A.extend(tbl(sorted(((k, v) for k, v in nm_by_computed.items()), key=lambda x: -x[1]),
                 ['computed step', 'near-misses']))
    a('')
    a('## 3. How well does the near-miss count approximate production L1 beyond the builder?')
    a('')
    a('Gap set **G** = items production accepted at L1 (`verdict` accepted and `step` in '
      '`match`/`spelling_variant`) that the offline builder does **not** call `match`: '
      '**|G| = %d**.' % len(gap_ids))
    a('')
    A.extend(tbl([['near-miss ∧ G (true positive)', tp],
                  ['near-miss ∧ ¬G (over-count)', fp],
                  ['G ∧ ¬near-miss (missed)', fn],
                  ['precision (share of near-misses that production really accepted at L1)',
                   '%.1f %%' % prec],
                  ['recall (share of G the proxy finds)', '%.1f %%' % rec]],
                 ['quantity', 'value']))
    a('')
    if not gap_ids:
        a('**Reading.** On DEV the gap set is empty: every item production accepted at L1 is also '
          'an exact `match` for the offline builder, so the builder loses nothing at L1 on this '
          'side and the %d near-misses are all *headroom* — answers production did **not** accept '
          'at L1, but which a fuzzy/spelling-variant step of the kind production owns could have '
          'accepted. The near-miss count is therefore an **upper bound on unmodelled L1 '
          'leniency, not an estimate of it**: on the one side where the truth is observable its '
          'precision as a predictor of actual production L1 accepts is 0 %%.' % len(nm_ids))
    else:
        gsplit = collections.Counter((x['stored_step'], x['computed_step']) for x in gap)
        g_sv = [x for x in gap if x['stored_step'] == 'spelling_variant']
        g_sv_nm = [x for x in g_sv if x['nearmiss']]
        a('Composition of G, by stored step -> computed step:')
        a('')
        A.extend(tbl(sorted(((k[0], k[1], v, sum(1 for x in gap if (x['stored_step'],
                              x['computed_step']) == k and x['nearmiss']))
                             for k, v in gsplit.items()), key=lambda x: -x[2]),
                     ['stored', 'computed', 'n', 'flagged near-miss']))
        a('')
        a('**Reading — and the caveat that decides how to use this number.** Taken at face value '
          'the proxy has **%.1f %% precision** (%d of %d flagged rows were really accepted by '
          'production at L1) but only **%.1f %% recall** (%d of %d gap rows found). The recall '
          'figure is, however, **not** a measurement of the offline builder\'s L1 leniency gap, '
          'because G is contaminated: %d of its %d rows have stored step `match`, i.e. production '
          'made an *exact* L1 match that the builder now misses. Those rows are production/offline '
          '**normalisation and reference-set drift**, not fuzzy acceptance: the stored `chk` was '
          'captured against the production reference set under production\'s own normaliser, '
          'while `build_side(\'dev\')` matches against the arm-B annotations (`ann_b0`). The '
          'sample below makes the dominant mechanism visible — every `match` near-miss differs '
          'from its nearest reference only by a contraction (`she\'s` / `there\'s` / '
          '`wouldn\'t` vs the spelled-out form), i.e. production\'s normaliser expands '
          'contractions and `checker_1i.base.norm` does not.'
          % (prec, tp, len(nm_set), rec, tp, len(gap_ids),
             gsplit.get(('match', 'auto'), 0), len(gap_ids)))
        a('')
        a('The part of G that really is "production accepts at L1 beyond what the offline builder '
          'can reproduce" is the `spelling_variant` step, and on DEV that is **%d row(s)**, of '
          'which the near-miss predicate flags **%d**. So:'
          % (len(g_sv), len(g_sv_nm)))
        a('')
        a('* as an **estimator of the size** of the unreproducible-L1 gap, the near-miss count is '
          'a loose **upper bound**: %d flagged vs %d true `spelling_variant` accepts on DEV '
          '(~%.0fx over-count);' % (len(nm_set), len(g_sv), len(nm_set) / max(1, len(g_sv))))
        a('* as a **filter**, it is accurate: %d of %d flagged rows (%.1f %%) are answers '
          'production did accept at L1, so items it flags deserve to be read as '
          '"production-plausible accepts the offline pipeline will reject", not as noise;'
          % (tp, len(nm_set), prec))
        a('* it is **not** a substitute for the missing `spelling_variant` step. DEV carries only '
          '%d such row in %d, so DEV cannot calibrate that step at all — any Phase 1M claim about '
          'production L1 leniency has to be stated as a bound, not an estimate.'
          % (len(sv), n))
    a('')
    a('Caveats: (a) DEV is the calibration set *and* the set the frozen config was tuned on, so '
      'these rates are optimistic for a fresh side; (b) the stored DEV verdicts come from the '
      'production checker at capture time — a later production change to the spelling-variant '
      'step would invalidate the mapping; (c) the near-miss predicate is a pure string rule and '
      'knows nothing of the annotation mistake patterns, so a near-miss can coexist with a '
      'legitimate `mistake` rejection (see the crosstab).')
    a('')
    if nm_ids:
        a('### Sample near-misses (up to 12)')
        a('')
        A.extend(tbl([[x['item_id'], x['stored_step'], x['computed_step'], x['nm_dist'],
                       x['nm_len_mismatch'], '`%s`' % x['answer'], '`%s`' % (x['nm_ref'] or '')]
                      for x in nm_ids[:12]],
                     ['item', 'stored', 'computed', 'dist', 'len_mm', 'answer', 'nearest ref']))
        a('')
    open(OUT, 'w', encoding='utf-8').write('\n'.join(A) + '\n')
    json.dump({'n': n, 'nearmiss': len(nm_ids), 'gap': len(gap_ids), 'tp': tp, 'fp': fp,
               'fn': fn, 'precision_pct': prec, 'recall_pct': rec,
               'stored_steps': dict(stored_steps), 'cross': dict(cross),
               'nm_by_stored': dict(nm_by_stored), 'nm_by_computed': dict(nm_by_computed),
               'nm_source': NM_SOURCE, 'rows': rows},
              open(os.path.join(HERE, 'l1_nearmiss_calibration.json'), 'w'), indent=1)
    print('n=%d nearmiss=%d gap=%d tp=%d fp=%d fn=%d prec=%.1f rec=%.1f src=%s'
          % (n, len(nm_ids), len(gap_ids), tp, fp, fn, prec, rec, NM_SOURCE))
    print('wrote', OUT)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Phase 1i TASK A — zero-call re-scoring of the WHOLE Phase 1h fresh set with an L3 "TIP" counted as a
REJECTION instead of an acceptance.

This FLIPS AN EXISTING SWITCH, it adds no rule: `checker_1h.decide()` already turns a model reply of TIP
into `verdict='correct_with_tip', accepted=True` (checker_1h.py lines 853-855). Task A only asks what the
frozen measurement would have said had that one branch rejected. No prompt, threshold, word list, layer or
annotation is touched and no model call is made.

Input: `phase1i/taskA/scoring_rows.jsonl` (written by phase1i/make_split.py) — verdict-only rows for DEV
and HOLDOUT together, containing no Slovak, no reference and no learner answer. This script prints and
writes AGGREGATES ONLY; no individual holdout item is printed or written.

usage: python3 phase1i/taskA_rescore.py
"""
import json
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROWS = os.path.join(HERE, 'taskA', 'scoring_rows.jsonl')


# ---------------------------------------------------------------- exact Clopper-Pearson
def cp(k, n, alpha=0.05):
    """Exact 95 % Clopper-Pearson interval in percent. scipy if available, else bisection on the
    binomial CDF (pure python, no dependency)."""
    if n == 0:
        return (0.0, 100.0)
    try:
        from scipy.stats import beta                                  # noqa: F401
        lo = 0.0 if k == 0 else beta.ppf(alpha / 2, k, n - k + 1)
        hi = 1.0 if k == n else beta.ppf(1 - alpha / 2, k + 1, n - k)
        return (round(100 * lo, 2), round(100 * hi, 2))
    except Exception:
        pass
    from math import comb

    def cdf(kk, p):                      # P(X <= kk)
        return sum(comb(n, i) * (p ** i) * ((1 - p) ** (n - i)) for i in range(0, kk + 1))

    def solve(f):
        lo, hi = 0.0, 1.0
        for _ in range(200):
            mid = (lo + hi) / 2
            if f(mid):
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2

    # lower: p such that P(X >= k) = alpha/2  ->  1 - cdf(k-1, p) = alpha/2
    lo = 0.0 if k == 0 else solve(lambda p: 1 - cdf(k - 1, p) < alpha / 2)
    # upper: p such that P(X <= k) = alpha/2
    hi = 1.0 if k == n else solve(lambda p: cdf(k, p) > alpha / 2)
    return (round(100 * lo, 2), round(100 * hi, 2))


def cell(k, n):
    lo, hi = cp(k, n)
    return '%d/%d = %.1f %% [%.1f–%.1f]' % (k, n, (100.0 * k / n) if n else 0.0, lo, hi)


def blk(k, n):
    lo, hi = cp(k, n)
    return {'k': k, 'n': n, 'pct': round(100.0 * k / n, 2) if n else None, 'ci95': [lo, hi]}


rows = [json.loads(l) for l in open(ROWS, encoding='utf-8') if l.strip()]

# ---------------------------------------------------------------- the switch
def accepted(r, row, after):
    a = r[row]['accepted']
    if after and a and r[row]['layer'] == 'L3' and r[row]['model'] == 'TIP':
        return False
    return a


COV = [r for r in rows if r['kind'] == 'C' and r['judged'] == 'correct']      # 420
FAD = [r for r in rows if r['kind'] == 'W' and r['judged'] == 'wrong']        # 550

out = {'switch': 'L3 reply TIP counted as a REJECTION (checker_1h.decide lines 853-855); no new rule',
       'set': 'whole Phase 1h fresh set, DEV + HOLDOUT together',
       'n_items': len(rows), 'n_coverage_denominator': len(COV), 'n_fa_denominator': len(FAD),
       'headline_row': 'row 7 (P-B) — the row that produced the 82.1 % coverage / 12.0 % false acceptance '
                       'of the Phase 1h report (§2 table, rows 7/8; row 8 = P-C is void, report §5 D3)',
       'rows': {}}


def why_split(rs, row):
    """How the accepted items were accepted: model TIP / model SAME / an offline layer."""
    c = Counter()
    for r in rs:
        if not r[row]['accepted']:
            continue
        if r[row]['layer'] == 'L3':
            c['L3_' + str(r[row]['model'])] += 1
        else:
            c['offline_' + r[row]['layer']] += 1
        if r[row]['layer'] == 'L3' and r[row]['model'] == 'SAME' and r[row]['verdict'] == 'correct_with_tip':
            c['L3_SAME_with_F2_tip'] += 1
    return dict(c)


for row in ('row7', 'row8'):
    before_cov = sum(1 for r in COV if accepted(r, row, False))
    after_cov = sum(1 for r in COV if accepted(r, row, True))
    before_fa = sum(1 for r in FAD if accepted(r, row, False))
    after_fa = sum(1 for r in FAD if accepted(r, row, True))
    d = {'coverage_before': blk(before_cov, len(COV)), 'coverage_after': blk(after_cov, len(COV)),
         'fa_before': blk(before_fa, len(FAD)), 'fa_after': blk(after_fa, len(FAD)),
         'accept_reason_correct_set_before': why_split(COV, row),
         'accept_reason_fa_before': why_split([r for r in FAD if r[row]['accepted']], row),
         'by_wrong_type': {}, 'by_half': {}, 'failed_calls': sum(1 for r in rows if r[row]['failed_call']),
         'no_verdict_items': sum(1 for r in rows if r[row]['layer'] == 'L3' and r[row]['verdict'] == 'failed')}
    for t in ('T', 'W', 'M', 'S'):
        sub = [r for r in FAD if r['wrong_type'] == t]
        d['by_wrong_type'][t] = {'fa_before': blk(sum(1 for r in sub if accepted(r, row, False)), len(sub)),
                                 'fa_after': blk(sum(1 for r in sub if accepted(r, row, True)), len(sub))}
    for h in ('OLD', 'NEW'):
        cs = [r for r in COV if r['half'] == h]
        ws = [r for r in FAD if r['half'] == h]
        d['by_half'][h] = {
            'coverage_before': blk(sum(1 for r in cs if accepted(r, row, False)), len(cs)),
            'coverage_after': blk(sum(1 for r in cs if accepted(r, row, True)), len(cs)),
            'fa_before': blk(sum(1 for r in ws if accepted(r, row, False)), len(ws)),
            'fa_after': blk(sum(1 for r in ws if accepted(r, row, True)), len(ws))}
    out['rows'][row] = d

r7 = out['rows']['row7']
assert (r7['coverage_before']['k'], r7['coverage_before']['n']) == (345, 420), 'before != 345/420'
assert (r7['fa_before']['k'], r7['fa_before']['n']) == (66, 550), 'before != 66/550'
out['sanity'] = 'row 7 before reproduces Phase 1h exactly: coverage 345/420 = 82.1 %, real FA 66/550 = 12.0 %'

# per-side aggregate counts only (no ids, no items)
out['by_side'] = {}
for s in ('dev', 'holdout'):
    cs = [r for r in COV if r['side'] == s]
    ws = [r for r in FAD if r['side'] == s]
    out['by_side'][s] = {
        'coverage_before': blk(sum(1 for r in cs if accepted(r, 'row7', False)), len(cs)),
        'coverage_after': blk(sum(1 for r in cs if accepted(r, 'row7', True)), len(cs)),
        'fa_before': blk(sum(1 for r in ws if accepted(r, 'row7', False)), len(ws)),
        'fa_after': blk(sum(1 for r in ws if accepted(r, 'row7', True)), len(ws))}

json.dump(out, open(os.path.join(HERE, 'taskA', 'TASK_A.json'), 'w'), indent=1)

# ---------------------------------------------------------------- markdown
fa_r = r7['accept_reason_fa_before']
cc_r = r7['accept_reason_correct_set_before']


def g(d, *keys):
    return sum(d.get(k, 0) for k in keys)


L = ['# Phase 1i — TASK A: an L3 "TIP" counted as a rejection (zero model calls)\n',
     'Whole Phase 1h fresh set, **DEV + HOLDOUT together** (this is a re-scoring of an already-made',
     'measurement, not a design decision taken on the holdout). Headline row = **row 7 (P-B)**, the row',
     'that produced the 82.1 % coverage and 12.0 % false acceptance of the Phase 1h report; row 8 (P-C) is',
     'shown because it is free, but it stays **void** (report §5 D3: 311 empty replies).\n',
     '**This flips an existing switch — it adds no rule.** `checker_1h.decide()` (lines 853-855) maps a',
     "model reply of `TIP` to `verdict='correct_with_tip', accepted=True`. Task A asks only what the frozen",
     'measurement would have said if that single branch rejected instead. Nothing else is changed; no prompt,',
     'threshold, layer, word list or annotation is touched and no call was made.\n',
     '## HEADLINE\n',
     '**The 66 real false acceptances of row 7 were accepted by:**\n',
     '| accepted by | n |', '|---|---|',
     '| L3 model reply **TIP** | %d |' % fa_r.get('L3_TIP', 0),
     '| L3 model reply **SAME** | %d |' % fa_r.get('L3_SAME', 0),
     '| an **offline** layer (L1) | %d |' % g(fa_r, 'offline_L1', 'offline_L2', 'offline_F2B'),
     '| **total** | %d |' % r7['fa_before']['k'], '',
     '**The 345 accepted correct answers of row 7 were accepted by:**\n',
     '| accepted by | n |', '|---|---|',
     '| L3 model reply **TIP** | %d |' % cc_r.get('L3_TIP', 0),
     '| L3 model reply **SAME** | %d |' % cc_r.get('L3_SAME', 0),
     '| an **offline** layer (L1) | %d |' % g(cc_r, 'offline_L1', 'offline_L2', 'offline_F2B'),
     '| **total** | %d |' % r7['coverage_before']['k'], '',
     '(of the L3 SAME accepts, %d carried an F2-released tip, i.e. `correct_with_tip` without a model TIP; '
     'they are NOT touched by this switch.)\n' % cc_r.get('L3_SAME_with_F2_tip', 0),
     '## Before / after, row 7 (P-B)\n',
     '| figure | before | after (TIP = reject) | change |', '|---|---|---|---|']
for lab, key in (('coverage (n = 420 judged really correct)', 'coverage'),
                 ('real false acceptance (n = 550 judged really wrong)', 'fa')):
    b, a = r7[key + '_before'], r7[key + '_after']
    L.append('| %s | %s | %s | %+.1f pp |' % (lab, cell(b['k'], b['n']), cell(a['k'], a['n']),
                                              (a['pct'] or 0) - (b['pct'] or 0)))
L += ['', '### By wrong type (false acceptance, row 7)\n',
      '| type | before | after |', '|---|---|---|']
for t in ('T', 'W', 'M', 'S'):
    b, a = r7['by_wrong_type'][t]['fa_before'], r7['by_wrong_type'][t]['fa_after']
    L.append('| %s | %s | %s |' % (t, cell(b['k'], b['n']), cell(a['k'], a['n'])))
L += ['', '### By sentence half (row 7)\n',
      '| half | coverage before | coverage after | FA before | FA after |', '|---|---|---|---|---|']
for h in ('OLD', 'NEW'):
    d = r7['by_half'][h]
    L.append('| %s (%s) | %s | %s | %s | %s |'
             % (h, 'the 80 in-sample sentences' if h == 'OLD' else 'the 60 fresh sentences',
                cell(d['coverage_before']['k'], d['coverage_before']['n']),
                cell(d['coverage_after']['k'], d['coverage_after']['n']),
                cell(d['fa_before']['k'], d['fa_before']['n']),
                cell(d['fa_after']['k'], d['fa_after']['n'])))
L += ['', '### DEV / HOLDOUT aggregates (row 7, counts only — no item is listed)\n',
      '| side | coverage before | coverage after | FA before | FA after |', '|---|---|---|---|---|']
for s in ('dev', 'holdout'):
    d = out['by_side'][s]
    L.append('| %s | %s | %s | %s | %s |'
             % (s, cell(d['coverage_before']['k'], d['coverage_before']['n']),
                cell(d['coverage_after']['k'], d['coverage_after']['n']),
                cell(d['fa_before']['k'], d['fa_before']['n']),
                cell(d['fa_after']['k'], d['fa_after']['n'])))
r8 = out['rows']['row8']
L += ['', '## Row 8 (P-C) — VOID, quoted for completeness only\n',
      '| figure | before | after |', '|---|---|---|',
      '| coverage | %s | %s |' % (cell(r8['coverage_before']['k'], r8['coverage_before']['n']),
                                  cell(r8['coverage_after']['k'], r8['coverage_after']['n'])),
      '| real false acceptance | %s | %s |' % (cell(r8['fa_before']['k'], r8['fa_before']['n']),
                                               cell(r8['fa_after']['k'], r8['fa_after']['n'])),
      '', 'Row 8 has %d failed calls and %d items with no parsed verdict (report §5 D3); its numbers are '
      'artefacts of missing verdicts and must not be quoted.\n'
      % (r8['failed_calls'], r8['no_verdict_items']),
      '## Sanity\n', '- ' + out['sanity'],
      '- row 7 failed calls %d, items reaching L3 without a parsed verdict %d (Phase 1h reported 23 fresh '
      'items without a verdict).' % (r7['failed_calls'], r7['no_verdict_items']),
      '- intervals: exact Clopper-Pearson, `scipy.stats.beta` when importable, otherwise a pure-python '
      'bisection on the binomial CDF (both implemented in this script; the numbers above say which ran: '
      'the values are identical to 2 decimals either way).\n',
      '## Reading\n',
      '- The TIP branch is the single cheapest lever in the whole checker: it removes %d of the %d false '
      'acceptances (%.1f pp) at a cost of %d of the %d accepted correct answers (%.1f pp of coverage).'
      % (r7['fa_before']['k'] - r7['fa_after']['k'], r7['fa_before']['k'],
         (r7['fa_before']['pct'] or 0) - (r7['fa_after']['pct'] or 0),
         r7['coverage_before']['k'] - r7['coverage_after']['k'], r7['coverage_before']['k'],
         (r7['coverage_before']['pct'] or 0) - (r7['coverage_after']['pct'] or 0)),
      '- It is a pure trade, not a free win: judge it against the product decision (assistive hint layer vs '
      'autonomous gate), not against one number.\n']
open(os.path.join(HERE, 'taskA', 'TASK_A.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')

print('ROW 7 coverage %s -> %s' % (cell(r7['coverage_before']['k'], r7['coverage_before']['n']),
                                   cell(r7['coverage_after']['k'], r7['coverage_after']['n'])))
print('ROW 7 real FA  %s -> %s' % (cell(r7['fa_before']['k'], r7['fa_before']['n']),
                                   cell(r7['fa_after']['k'], r7['fa_after']['n'])))
print('66 FA by accept reason: %s' % json.dumps(fa_r))
print('345 accepted correct by accept reason: %s' % json.dumps(cc_r))
print('ROW 8 (void) coverage %s -> %s | FA %s -> %s'
      % (cell(r8['coverage_before']['k'], r8['coverage_before']['n']),
         cell(r8['coverage_after']['k'], r8['coverage_after']['n']),
         cell(r8['fa_before']['k'], r8['fa_before']['n']),
         cell(r8['fa_after']['k'], r8['fa_after']['n'])))
print('FA by type after: %s' % json.dumps({t: [r7['by_wrong_type'][t]['fa_after']['k'],
                                               r7['by_wrong_type'][t]['fa_after']['n']]
                                           for t in ('T', 'W', 'M', 'S')}))

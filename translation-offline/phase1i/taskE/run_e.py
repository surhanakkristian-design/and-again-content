#!/usr/bin/env python3
"""Task E — prompt variants at L3, measured on DEV on top of Task B + Task C.

    python3 run_e.py --diag                          # 0 model calls: apparatus, reconciliation, causes
    python3 run_e.py --run --variants P-E2,P-E3      # model calls (resumable, interleaved, 4 threads)
    python3 run_e.py --score                         # writes taskE/results.json + phase1i/FROZEN_CONFIG.json

DEV only. The holdout is never touched here.
"""
import argparse
import collections
import difflib
import json
import os
import random
import re
import sys
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
P1I = os.path.dirname(HERE)
sys.path.insert(0, P1I)
import pipeline_1i as P                                                    # noqa: E402

LEDGER = os.path.join(HERE, 'calls.jsonl')
CAP = 1300
GUARD_SETS = {'F4v3': ('F4v3',), 'F4v3+F5t+F6': ('F5t', 'F6', 'F4v3')}
WORD = re.compile(r"[a-z0-9']+")


def toks(s):
    return WORD.findall((s or '').lower())


# ---------------------------------------------------------------- stored P-B verdicts
def stored_pb(st):
    """P-B verdicts whose prompt text is byte-identical to ours: row-7 + taskB ledger + our own ledger."""
    out, src = {}, {}
    for r in st['recs']:
        m = (r.get('rows', {}).get('row7') or {}).get('model')
        if m in ('SAME', 'TIP', 'DIFF'):
            out[r['item_id']] = m
            src[r['item_id']] = 'row7'
    for p in (os.path.join(P1I, 'taskB', 'calls.jsonl'), LEDGER):
        if not os.path.exists(p):
            continue
        for ln in open(p, encoding='utf-8'):
            try:
                row = json.loads(ln)
            except Exception:
                continue
            if row.get('http') == 200 and row.get('variant') == 'P-B' \
                    and row.get('verdict') in ('SAME', 'TIP', 'DIFF'):
                out[row['item_id']] = row['verdict']
                src[row['item_id']] = os.path.basename(os.path.dirname(p)) or 'taskE'
    return out, src


def l3_ids(st):
    res = P.run_pipeline(st, {})
    return [i for i in res if res[i]['reached_l3']]


# ---------------------------------------------------------------- diag
def diag():
    st = P.configure(b_fix=False, guards=(), side='dev')
    recs = {r['item_id']: r for r in st['recs']}
    pb, _src = stored_pb(st)
    base = P.run_pipeline(st, pb)
    mism = []
    for i, r in recs.items():
        w = r['rows']['row7']
        if (w['layer'], bool(w['accepted']), w['verdict']) != \
           (base[i]['layer'], base[i]['accepted'], base[i]['verdict']):
            mism.append({'id': i, 'stored': [w['layer'], w['accepted'], w['verdict']],
                         'got': [base[i]['layer'], base[i]['accepted'], base[i]['verdict']]})
    m_acc = P.metrics(st, base)
    print('APPARATUS flags-off replay of row 7: %d/%d items match (mismatches %d)'
          % (len(recs) - len(mism), len(recs), len(mism)))
    for x in mism[:5]:
        print('   ', x)
    print('  coverage %s  fa %s' % (m_acc['coverage'], m_acc['fa']))

    # --- the 145 vs 149 reconciliation -------------------------------------------------
    tip_any = [i for i in base if base[i]['accepted'] and base[i]['verdict'] == 'correct_with_tip']
    tip_l3 = [i for i in tip_any if base[i]['model'] == 'TIP']
    tip_not_l3 = [i for i in tip_any if base[i]['model'] != 'TIP']
    corr = [i for i, r in recs.items() if r['kind'] == 'C' and r['judged'] == 'correct']
    cov_l3rej = sum(1 for i in corr if base[i]['accepted'] and base[i]['model'] != 'TIP')
    cov_anytiprej = sum(1 for i in corr if base[i]['accepted'] and base[i]['verdict'] != 'correct_with_tip')
    print('\nRECONCILIATION  accepted-with-tip %d  (model TIP %d, tip from L2/F2 %d)'
          % (len(tip_any), len(tip_l3), len(tip_not_l3)))
    print('  coverage if ONLY an L3 model TIP is a rejection  : %d/%d' % (cov_l3rej, len(corr)))
    print('  coverage if ANY correct_with_tip is a rejection  : %d/%d' % (cov_anytiprej, len(corr)))
    print('  non-L3 tipped correct answers:',
          [(i, base[i]['layer'], base[i]['model']) for i in tip_not_l3 if i in corr][:10])
    ta = os.path.join(P1I, 'taskA', 'scoring_rows.jsonl')
    if os.path.exists(ta):
        rows = [json.loads(l) for l in open(ta, encoding='utf-8') if l.strip()]
        print('  taskA/scoring_rows.jsonl keys:', sorted(rows[0].keys()))
        dev = [r for r in rows if r.get('side') == 'dev']
        print('  taskA dev rows: %d' % len(dev))

    # --- L3 sets ------------------------------------------------------------------------
    st = P.configure(b_fix=True, guards=('F4v3',), side='dev')
    l3 = l3_ids(st)
    n_g = sum(1 for i in l3 if P.gender_chain(st, recs[i]['sid']))
    print('\nL3 items with B+C applied: %d   with a g chain: %d   without: %d'
          % (len(l3), n_g, len(l3) - n_g))
    print('B reports:', json.dumps(st['reports'].get('lock_fix', {}).get('releases', {}))[:200])
    chains = {}
    for i in l3:
        g = P.gender_chain(st, recs[i]['sid'])
        if g:
            chains[tuple(g)] = chains.get(tuple(g), 0) + 1
    print('g chain shapes (top 8):', sorted(chains.items(), key=lambda kv: -kv[1])[:8])

    # --- DIFF-on-correct causes ---------------------------------------------------------
    bad = [i for i in l3 if recs[i]['kind'] == 'C' and recs[i]['judged'] == 'correct'
           and pb.get(i) == 'DIFF']
    print('\nFALSE REJECTIONS by the model (correct answers, L3, P-B says DIFF): %d' % len(bad))
    cause = collections.Counter()
    ex = collections.defaultdict(list)
    for i in bad:
        r = recs[i]
        it = P.to_item(r)
        refs = [r['reference']] + [x for x in (r.get('refs') or []) if isinstance(x, str)]
        a = toks(r['answer'])
        best, bops = None, None
        for ref in refs:
            ops = [o for o in difflib.SequenceMatcher(a=toks(ref), b=a).get_opcodes() if o[0] != 'equal']
            if bops is None or len(ops) < len(bops):
                best, bops = ref, ops
        kinds = {o[0] for o in bops}
        has_g = bool(P.gender_chain(st, r['sid']))
        if not bops:
            c = 'exact match to an accepted rendering'
        elif kinds == {'replace'}:
            c = 'word choice only (paraphrase/synonym)'
        elif 'insert' in kinds and 'delete' in kinds:
            c = 'rewrite (insert+delete)'
        elif 'insert' in kinds:
            c = 'added words only'
        else:
            c = 'dropped words only'
        if has_g:
            gw = set()
            for w in ('he', 'she', 'him', 'her', 'his', 'hers', 'himself', 'herself'):
                gw.add(w)
            if (set(toks(best)) ^ set(a)) & gw:
                c = 'gender choice (g chain) + ' + c
        cause[c] += 1
        if len(ex[c]) < 3:
            ex[c].append({'id': i, 'sk': r['sk'], 'ref': best, 'answer': r['answer']})
    for c, n in cause.most_common():
        print('  %3d  %s' % (n, c))
        for e in ex[c]:
            print('        %s\n          SK  %s\n          REF %s\n          ANS %s'
                  % (e['id'], e['sk'], e['ref'], e['answer']))

    # --- rendered prompts ----------------------------------------------------------------
    print('\nSYS (frozen):', repr(P.sys_text(st, 'P-B')))
    print('SYS (P-E2)  :', repr(P.sys_text(st, 'P-E2')))
    sample = next(i for i in l3 if P.gender_chain(st, recs[i]['sid']))
    plain = next(i for i in l3 if not P.gender_chain(st, recs[i]['sid']))
    for i in (sample, plain):
        print('\n===== item %s (g chain: %s)' % (i, P.gender_chain(st, recs[i]['sid'])))
        for v in P.VARIANTS:
            u, hg, eq = P.build_prompt(st, recs[i], v)
            print('--- %s  (== P-B: %s)\n%s' % (v, eq, u))
    json.dump({'mismatches': mism, 'l3': sorted(l3), 'n_g': n_g, 'causes': dict(cause),
               'reconciliation': {'accepted_with_tip': len(tip_any), 'model_tip': len(tip_l3),
                                  'tip_from_l2_f2': len(tip_not_l3),
                                  'coverage_l3_tip_reject': cov_l3rej,
                                  'coverage_any_tip_reject': cov_anytiprej,
                                  'n_correct': len(corr)}},
              open(os.path.join(HERE, 'diag.json'), 'w'), indent=1)


# ---------------------------------------------------------------- run
def run(variants, cap):
    st = P.configure(b_fix=True, guards=('F4v3',), side='dev')
    recs = {r['item_id']: r for r in st['recs']}
    l3 = sorted(l3_ids(st))
    have, fails, _ret = P.ledger_verdicts(LEDGER)
    done200 = len(set(have) | set(fails))
    pb, _ = stored_pb(st)
    tasks, reused = [], collections.Counter()
    order = list(l3)
    random.Random(1618).shuffle(order)
    for i in order:
        for v in variants:
            if (v, i) in have or (v, i) in fails:
                continue
            _u, has_g, eq_pb = P.build_prompt(st, recs[i], v)
            if eq_pb and i in pb:
                reused[v] += 1
                continue
            tasks.append((i, v))
    print('L3 %d  variants %s  already in ledger %d  reused-as-P-B %s  to call %d  (cap %d)'
          % (len(l3), variants, done200, dict(reused), len(tasks), cap))
    if done200 + len(tasks) > cap:
        print('ABORT: would exceed the budget cap (%d + %d > %d)' % (done200, len(tasks), cap))
        return
    key = P.load_key()
    n = {'ok': 0, 'fail': 0}

    def work(t):
        i, v = t
        verdict, row = P.call_variant(st, recs[i], v, LEDGER, key)
        if row.get('http') == 200 and verdict:
            n['ok'] += 1
        else:
            n['fail'] += 1
        if (n['ok'] + n['fail']) % 50 == 0:
            print('   %d/%d ok=%d fail=%d' % (n['ok'] + n['fail'], len(tasks), n['ok'], n['fail']),
                  flush=True)
        return verdict

    with ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(work, tasks))
    print('done: ok %d  not-ok %d' % (n['ok'], n['fail']))
    have, fails, ret = P.ledger_verdicts(LEDGER)
    hist = collections.Counter()
    for ln in open(LEDGER, encoding='utf-8'):
        hist[json.loads(ln).get('http')] += 1
    print('ledger http histogram:', dict(hist), ' failed(200 but unparsable):', len(fails),
          ' transport rows:', ret)


# ---------------------------------------------------------------- score
def variant_map(st, variant, have, pb, l3):
    """verdict map for one variant + accounting."""
    vm, reused, missing = {}, [], []
    for i in l3:
        _u, _g, eq = P.build_prompt(st, st_recs(st)[i], variant)
        if (variant, i) in have:
            vm[i] = have[(variant, i)]
        elif eq and i in pb:
            vm[i] = pb[i]
            reused.append(i)
        else:
            missing.append(i)
    return vm, reused, missing


_RC = {}


def st_recs(st):
    if id(st) not in _RC:
        _RC[id(st)] = {r['item_id']: r for r in st['recs']}
    return _RC[id(st)]


def score():
    out = {'dev': {}, 'apparatus': {}, 'configs': []}
    st = P.configure(b_fix=False, guards=(), side='dev')
    recs = st_recs(st)
    pb, _src = stored_pb(st)
    base = P.run_pipeline(st, pb)
    mism = sum(1 for i, r in recs.items()
               if (r['rows']['row7']['layer'], bool(r['rows']['row7']['accepted']),
                   r['rows']['row7']['verdict']) != (base[i]['layer'], base[i]['accepted'],
                                                     base[i]['verdict']))
    out['apparatus'] = {'row7_replay_match': len(recs) - mism, 'row7_replay_n': len(recs),
                        'row7_coverage': P.metrics(st, base)['coverage'],
                        'row7_fa': P.metrics(st, base)['fa']}
    assert mism == 0, 'apparatus check failed: %d mismatches' % mism
    corr0 = [i for i, r in recs.items() if r['kind'] == 'C' and r['judged'] == 'correct']
    tipc = [i for i in corr0 if base[i]['accepted'] and base[i]['verdict'] == 'correct_with_tip']
    out['reconciliation'] = {
        'n_correct': len(corr0),
        'accepted_correct_row7': sum(1 for i in corr0 if base[i]['accepted']),
        'accepted_correct_with_tip': len(tipc),
        'of_those_model_TIP_at_L3': sum(1 for i in tipc if base[i]['model'] == 'TIP'),
        'of_those_tip_from_L2_F2': sum(1 for i in tipc if base[i]['model'] != 'TIP'),
        'tip_from_L2_F2_ids': sorted(i for i in tipc if base[i]['model'] != 'TIP'),
        'coverage_taskA_switch_L3_model_TIP_only':
            sum(1 for i in corr0 if base[i]['accepted'] and base[i]['model'] != 'TIP'),
        'coverage_any_correct_with_tip_rejected':
            sum(1 for i in corr0 if base[i]['accepted'] and base[i]['verdict'] != 'correct_with_tip')}
    print('RECONCILIATION', json.dumps(out['reconciliation']))

    have, fails, retries = P.ledger_verdicts(LEDGER)
    st = P.configure(b_fix=True, guards=('F4v3',), side='dev')
    l3 = sorted(l3_ids(st))
    out['l3_n'] = len(l3)
    out['transport_retry_rows'] = retries
    per_var = collections.Counter()
    per_fail = collections.Counter()
    for (v, i) in have:
        per_var[v] += 1
    for (v, i) in fails:
        per_fail[v] += 1

    variants = ['P-B'] + [v for v in P.VARIANTS if v != 'P-B' and per_var.get(v)]
    for v in variants:
        nc = per_var.get(v, 0) + per_fail.get(v, 0)
        out['dev'].setdefault('calls', {})[v] = {
            'counted_calls': nc, 'parsed': per_var.get(v, 0), 'failed': per_fail.get(v, 0),
            'failed_rate_pct': round(100.0 * per_fail.get(v, 0) / nc, 2) if nc else 0.0}

    for v in variants:
        for gname, guards in GUARD_SETS.items():
            stg = P.configure(b_fix=True, guards=guards, side='dev')
            vm, reused, missing = variant_map(stg, v, have, pb, l3)
            scorings = ['tip_accept'] if v == 'P-E2' else ['tip_accept', 'tip_reject']
            for sc in scorings:
                res = P.run_pipeline(stg, vm, tip_reject=(sc == 'tip_reject'))
                m = P.metrics(stg, res)
                nc = per_var.get(v, 0) + per_fail.get(v, 0)
                out['configs'].append({
                    'variant': v, 'scoring': sc, 'guards': gname, 'b_fix': True,
                    'coverage': m['coverage'], 'fa': m['fa'], 'fa_by_type': m['fa_by_type'],
                    'fa_by_layer': m['fa_by_layer'], 'fa_by_half': m['fa_by_half'],
                    'fa_items': m['fa_items'], 'false_rejections': m['false_rejections'],
                    'fr_by_layer': m['fr_by_layer'], 'tip_accepts': m['tip_accepts'],
                    'reused_pb': len(reused), 'no_verdict': len(missing),
                    'failed_calls': per_fail.get(v, 0), 'counted_calls': nc,
                    'failed_rate_pct': round(100.0 * per_fail.get(v, 0) / nc, 2) if nc else 0.0})

    # ---- selection rule, mechanically
    T_BASE = 1.49                       # baseline type-T FA, TIP = accept, 1/67
    elig = [c for c in out['configs'] if c['failed_rate_pct'] <= 2.0]
    out['disqualified'] = [{'variant': c['variant'], 'scoring': c['scoring'], 'guards': c['guards'],
                            'failed_rate_pct': c['failed_rate_pct']}
                           for c in out['configs'] if c['failed_rate_pct'] > 2.0]
    step1 = [c for c in elig if c['coverage']['pct'] >= 90.0 and c['fa']['pct'] < 5.0]
    step2 = [c for c in elig if c['fa']['pct'] < 5.0 and (c['fa_by_type']['T']['pct'] or 0) <= T_BASE]
    if step1:
        rule, ranked = 1, sorted(step1, key=lambda c: -c['coverage']['pct'])
    elif step2:
        rule, ranked = 2, sorted(step2, key=lambda c: (-c['coverage']['pct'], c['fa']['pct']))
    else:
        rule, ranked = 3, sorted(elig, key=lambda c: (c['fa']['pct'], -c['coverage']['pct']))
    win = ranked[0]
    out['selection'] = {'rule_step': rule, 'n_step1': len(step1), 'n_step2': len(step2),
                        'winner': {k: win[k] for k in ('variant', 'scoring', 'guards', 'coverage', 'fa')},
                        'runner_up': ({k: ranked[1][k] for k in ('variant', 'scoring', 'guards',
                                                                 'coverage', 'fa')}
                                      if len(ranked) > 1 else None),
                        'ranking': [{'variant': c['variant'], 'scoring': c['scoring'],
                                     'guards': c['guards'], 'coverage': c['coverage']['pct'],
                                     'fa': c['fa']['pct']} for c in ranked[:8]]}

    stw = P.configure(b_fix=True, guards=GUARD_SETS[win['guards']], side='dev')
    sample = st_recs(stw)[l3[0]]
    frozen = {
        'phase': '1i', 'decided_on': 'DEV (467 items; 203 correct / 260 really-wrong)',
        'selection_rule_step': rule,
        'prompt_variant': win['variant'],
        'tip_scoring': win['scoring'],
        'b_flags': {'backfill_s_ids': True, 'lock_fix': {'syn': True, 'gender': True,
                                                         'contraction': True}},
        'c_guards': list(GUARD_SETS[win['guards']]),
        'model': P.MODEL, 'generationConfig': P.GEN_CFG,
        'system_instruction': P.sys_text(stw, win['variant']),
        'prompt_template': {
            'base': 'lib_prev.prompt(it, "P-B") — Slovak / Reference English / Learner / '
                    'Practised grammar … / question line',
            'inserted_before_the_question_line': {
                'gender_line_when_the_annotation_has_g': P.GENDER_TMPL,
                'information_line': P.INFO_LINE if win['variant'] == 'P-E3' else None,
                'ground_truth_line': (P.GROUND_LINE if win['variant'] in ('P-E4a', 'P-E4b') else None),
                'alt_refs_line': (P.ALT_TMPL if win['variant'] == 'P-E4a' else None),
                'wording_line': (P.WORDING_LINE if win['variant'] == 'P-E4b' else None)},
            'question_line': 'SAME or DIFF?' if win['variant'] == 'P-E2' else 'SAME, TIP or DIFF?',
            'rendered_example': P.build_prompt(stw, sample, win['variant'])[0]},
        'dev_numbers': {'coverage': win['coverage'], 'fa': win['fa'],
                        'fa_by_type': win['fa_by_type'], 'failed_rate_pct': win['failed_rate_pct']},
        'runner_up': out['selection']['runner_up'],
    }
    json.dump(frozen, open(os.path.join(P1I, 'FROZEN_CONFIG.json'), 'w'), indent=1, ensure_ascii=False)
    json.dump(out, open(os.path.join(HERE, 'results.json'), 'w'), indent=1, ensure_ascii=False)

    print('apparatus: %d/%d row-7 replay' % (out['apparatus']['row7_replay_match'],
                                             out['apparatus']['row7_replay_n']))
    print('\n%-7s %-11s %-12s %-22s %-22s %s' % ('variant', 'scoring', 'guards', 'coverage', 'FA',
                                                 'failed%'))
    for c in out['configs']:
        print('%-7s %-11s %-12s %-22s %-22s %s' % (
            c['variant'], c['scoring'], c['guards'],
            '%d/%d=%.1f%% [%.1f-%.1f]' % (c['coverage']['k'], c['coverage']['n'], c['coverage']['pct'],
                                          c['coverage']['ci'][0], c['coverage']['ci'][1]),
            '%d/%d=%.1f%% [%.1f-%.1f]' % (c['fa']['k'], c['fa']['n'], c['fa']['pct'],
                                          c['fa']['ci'][0], c['fa']['ci'][1]),
            c['failed_rate_pct']))
    print('\nT-rate by config:', [(c['variant'], c['scoring'], c['guards'], c['fa_by_type']['T']['k'])
                                  for c in out['configs']])
    print('\nSELECTION rule step %d\n  winner   : %s' % (rule, out['selection']['winner']))
    print('  runner-up: %s' % out['selection']['runner_up'])
    print('  ranking  :', json.dumps(out['selection']['ranking'], indent=1))
    print('\ncalls:', json.dumps(out['dev']['calls'], indent=1), 'transport rows:', retries)
    fr = collections.Counter()
    for c in out['configs']:
        if c['variant'] == win['variant'] and c['scoring'] == win['scoring'] \
                and c['guards'] == win['guards']:
            for x in c['false_rejections']:
                fr[x['layer']] += 1
    print('winner false rejections by layer:', dict(fr))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--diag', action='store_true')
    ap.add_argument('--run', action='store_true')
    ap.add_argument('--score', action='store_true')
    ap.add_argument('--variants', default='P-E1,P-E2,P-E3')
    ap.add_argument('--cap', type=int, default=CAP)
    a = ap.parse_args()
    if a.diag:
        diag()
    if a.run:
        run(tuple(v.strip() for v in a.variants.split(',') if v.strip()), a.cap)
    if a.score:
        score()

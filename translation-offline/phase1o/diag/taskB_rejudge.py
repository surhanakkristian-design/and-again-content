#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phase 1O Task B - blind re-judge of the closed 1N set (topic restored) against the original 1N labels.
0 model calls, no network. Reads: phase1o/judge/out_*.json (new), phase1n/judge/out_*.json (old),
phase1n/judge/blind_map.json, phase1n/judge/controls_map.json, phase1n/results_1n.json (fr_ids / fa_ids = stack verdict
per item, stored), phase1o/diag/ce_dump.json (layer of judged-correct items), phase1o/taskCE_items.json (E buckets).
Writes: phase1o/TASK_B.md, phase1o/taskB_results.json; appends phase1o/access_log.jsonl. Writes nothing under phase1n/."""
import json, os, math, random, collections, datetime
DIAG = os.path.dirname(os.path.abspath(__file__)); O = os.path.dirname(DIAG); TOFF = os.path.dirname(O)
N = os.path.join(TOFF, 'phase1n'); ME = 'phase1o/diag/taskB_rejudge.py'; LOG = os.path.join(O, 'access_log.jsonl')
PURPOSE = 'Phase 1O Task B: blind re-judge vs 1N labels (0 calls)'
C = collections.Counter

def log(side, what, n, purpose=PURPOSE, caller=ME):
    with open(LOG, 'a') as f:
        f.write(json.dumps({'ts': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'), 'side': side, 'what': what,
                            'caller': caller, 'n': n, 'purpose': purpose}) + '\n')

def lbinom(n, i, p):
    return math.lgamma(n + 1) - math.lgamma(i + 1) - math.lgamma(n - i + 1) + i * math.log(p) + (n - i) * math.log(1 - p)
def cdf(k, n, p):
    if p <= 0: return 1.0
    if p >= 1: return 1.0 if k >= n else 0.0
    return min(1.0, sum(math.exp(lbinom(n, i, p)) for i in range(0, k + 1)))
def cp(k, n, a=0.05):
    if n == 0: return [None, None]
    def solve(f):
        lo, hi = 0.0, 1.0
        for _ in range(60):
            mid = (lo + hi) / 2
            if f(mid): lo = mid
            else: hi = mid
        return (lo + hi) / 2
    low = 0.0 if k == 0 else solve(lambda p: 1 - cdf(k - 1, n, p) < a / 2)
    up = 1.0 if k == n else solve(lambda p: cdf(k, n, p) > a / 2)
    return [round(100 * low, 2), round(100 * up, 2)]
def rate(k, n):
    return {'k': k, 'n': n, 'pct': round(100.0 * k / n, 2) if n else None, 'ci': cp(k, n)}
def fr(r):
    return '%d/%d = %.2f %% [%.2f, %.2f]' % (r['k'], r['n'], r['pct'], r['ci'][0], r['ci'][1]) if r['n'] else '0/0'
def sign_p(a, b):
    n = a + b
    if n == 0: return 1.0
    k = min(a, b)
    return min(1.0, 2 * sum(math.comb(n, i) for i in range(0, k + 1)) / 2.0 ** n)

def rows_of(p):
    d = json.load(open(p))
    return d if isinstance(d, list) else d.get('rows', d)
def load(base, side):
    lab, part = {}, {}
    for i in range(1, 6):
        fn = 'out_part%d.json' % i; rows = rows_of(os.path.join(base, 'judge', fn)); log(side, 'judge/' + fn, len(rows))
        for r in rows: lab[r['jid']] = r; part[r['jid']] = i
    rows = rows_of(os.path.join(base, 'judge', 'out_controls.json')); log(side, 'judge/out_controls.json', len(rows))
    return lab, part, {r['jid']: r for r in rows}

def find_lists(d, path=''):
    if isinstance(d, dict):
        for k, v in d.items():
            for x in find_lists(v, path + '/' + str(k)): yield x
    elif isinstance(d, list) and d and all(isinstance(x, str) for x in d):
        yield path, d

def main():
    assert cp(350, 426) == [78.19, 85.68], cp(350, 426)
    assert cp(14, 474) == [1.62, 4.91], cp(14, 474)
    new, npart, newK = load(O, '1o:judge'); old, opart, oldK = load(N, '1n:judge')
    bm = json.load(open(os.path.join(N, 'judge', 'blind_map.json'))); log('1n:judge', 'judge/blind_map.json', len(bm))
    assert set(new) == set(old) == set(bm) and len(bm) == 900, (len(new), len(old), len(bm))
    inv = {v: k for k, v in bm.items()}
    R = json.load(open(os.path.join(N, 'results_1n.json'))); log('1n:results', 'results_1n.json (fr_ids, fa_ids, judge_noise)', 900)
    lists = dict(find_lists(R.get('metrics', {}), 'metrics'))
    frp = [p for p in lists if p.endswith('/fr_ids')]; fap = [p for p in lists if p.endswith('/fa_ids')]
    print('id-list paths in metrics:', {p: len(v) for p, v in lists.items()})
    fr_ids = set(lists[frp[0]]); fa_ids = set(lists[fap[0]])
    oc = lambda j: old[j]['judged'] == 'correct'
    ncq = lambda j: new[j]['judged'] == 'correct'
    acc = {j: ((bm[j] not in fr_ids) if oc(j) else (bm[j] in fa_ids)) for j in bm}
    # pre-flight of the apparatus: must reproduce 1N exactly
    k_cov = sum(acc[j] for j in bm if oc(j)); n_cov = sum(oc(j) for j in bm)
    k_fa = sum(acc[j] for j in bm if not oc(j)); n_fa = 900 - n_cov
    assert (k_cov, n_cov, k_fa, n_fa) == (350, 426, 14, 474), (k_cov, n_cov, k_fa, n_fa)
    dump = json.load(open(os.path.join(DIAG, 'ce_dump.json'))); log('1o:derived', 'diag/ce_dump.json (layer of judged-correct items)', len(dump))
    drec = {r['id']: r for r in dump if r['id'] in inv}
    assert len(drec) == 426 and sum(bool(r['accepted']) for r in drec.values()) == 350
    assert all(bool(drec[bm[j]]['accepted']) == acc[j] for j in bm if oc(j))
    layer = lambda j: (drec[bm[j]].get('layer') if bm[j] in drec else 'not stored per item (judged wrong in 1N)')
    intent = lambda j: bm[j].split(':')[0]
    sid = lambda j: bm[j].split(':')[1]
    c2w = [j for j in bm if oc(j) and not ncq(j)]; w2c = [j for j in bm if not oc(j) and ncq(j)]
    both_c = [j for j in bm if oc(j) and ncq(j)]; both_w = [j for j in bm if not oc(j) and not ncq(j)]
    res = {'phase': '1O', 'task': 'B', 'model_calls': 0,
           'preflight': {'cp_350_426': cp(350, 426), 'cp_14_474': cp(14, 474), 'old_labels_reproduce': [k_cov, n_cov, k_fa, n_fa]},
           'totals': {'old_correct': n_cov, 'new_correct': sum(ncq(j) for j in bm), 'both_correct': len(both_c), 'both_wrong': len(both_w)}}
    def mv(ids, typ_side):
        return {'n': len(ids), 'stack_accepted': sum(acc[j] for j in ids), 'stack_rejected': sum(not acc[j] for j in ids),
                'by_writer_intent': dict(C(intent(j) for j in ids)),
                'by_type_' + typ_side: dict(C(str((new if typ_side == 'new' else old)[j].get('type')) for j in ids)),
                'by_passive_old>new': dict(C('%s>%s' % (old[j].get('passive'), new[j].get('passive')) for j in ids)),
                'by_part': dict(C(npart[j] for j in ids)),
                'by_layer_1n': dict(C(str(layer(j)) for j in ids)),
                'ids': sorted(bm[j] for j in ids)}
    res['movement'] = {'correct_to_wrong': mv(c2w, 'new'), 'wrong_to_correct': mv(w2c, 'old'),
                       'moved_total': rate(len(c2w) + len(w2c), 900), 'sign_test_p_two_sided': round(sign_p(len(c2w), len(w2c)), 4),
                       'moved_by_session': {'parts1-3': rate(sum(npart[j] <= 3 for j in c2w + w2c), 540), 'parts4-5': rate(sum(npart[j] >= 4 for j in c2w + w2c), 360)},
                       'net_by_session': {'parts1-3': [sum(npart[j] <= 3 for j in c2w), sum(npart[j] <= 3 for j in w2c)], 'parts4-5': [sum(npart[j] >= 4 for j in c2w), sum(npart[j] >= 4 for j in w2c)]}}
    base_rej = rate(76, 426)
    res['concentration'] = {'c2w_stack_rejected': rate(sum(not acc[j] for j in c2w), len(c2w)), 'base_rate_rejected_among_old_correct': base_rate if False else base_rej,
                            'w2c_stack_accepted': rate(sum(acc[j] for j in w2c), len(w2c)), 'base_rate_accepted_among_old_wrong': rate(14, 474),
                            'share_of_76_FR_flipped_to_wrong': rate(sum(not acc[j] for j in c2w), 76), 'share_of_350_accepted_flipped_to_wrong': rate(sum(acc[j] for j in c2w), 350),
                            'share_of_14_FA_flipped_to_correct': rate(sum(acc[j] for j in w2c), 14), 'share_of_460_true_rej_flipped_to_correct': rate(sum(not acc[j] for j in w2c), 460)}
    nc = [j for j in bm if ncq(j)]; nw = [j for j in bm if not ncq(j)]
    cov_new = rate(sum(acc[j] for j in nc), len(nc)); fa_new = rate(sum(acc[j] for j in nw), len(nw))
    res['under_new_labels'] = {'coverage': cov_new, 'fa': fa_new, 'coverage_1n': rate(350, 426), 'fa_1n': rate(14, 474),
                               'coverage_both_correct': rate(sum(acc[j] for j in both_c), len(both_c)), 'fa_both_wrong': rate(sum(acc[j] for j in both_w), len(both_w)),
                               'coverage_nonpassive_new': rate(sum(acc[j] for j in nc if not new[j].get('passive')), sum(1 for j in nc if not new[j].get('passive'))),
                               'label_points_of_6.93': round(cov_new['pct'] - 82.16, 2)}
    def bytype(lab, ids):
        t = C(str(lab[j].get('type')) for j in ids); return {k: rate(sum(acc[j] for j in ids if str(lab[j].get('type')) == k), v) for k, v in sorted(t.items())}
    res['fa_by_type'] = {'new_labels': bytype(new, nw), 'old_labels_1n': bytype(old, [j for j in bm if not oc(j)])}
    # paired cluster bootstrap (sentences) of coverage(new) - coverage(old)
    sids = sorted(set(sid(j) for j in bm)); bys = collections.defaultdict(list)
    for j in bm: bys[sid(j)].append(j)
    rnd = random.Random(1015); diffs = []
    for _ in range(2000):
        a = b = c = d = 0
        for s in (rnd.choice(sids) for _ in sids):
            for j in bys[s]:
                if oc(j): b += 1; a += acc[j]
                if ncq(j): d += 1; c += acc[j]
        diffs.append(100.0 * c / d - 100.0 * a / b)
    diffs.sort(); res['under_new_labels']['label_points_bootstrap95'] = [round(diffs[49], 2), round(diffs[1949], 2)]; res['n_sentences'] = len(sids)
    # noise yardsticks
    cm = json.load(open(os.path.join(N, 'judge', 'controls_map.json'))); log('1n:judge', 'judge/controls_map.json', len(cm))
    def strs(x):
        if isinstance(x, str): yield x
        elif isinstance(x, dict):
            for k, v in x.items():
                for y in strs(k): yield y
                for y in strs(v): yield y
        elif isinstance(x, list):
            for v in x:
                for y in strs(v): yield y
    twin = {}
    for ent in (cm.items() if isinstance(cm, dict) else cm):
        ss = list(strs(list(ent) if isinstance(ent, tuple) else ent))
        ks = [s for s in ss if s in newK]; js = [s for s in ss if s in bm] or [inv[s] for s in ss if s in inv]
        if ks and js: twin[ks[0]] = js[0]
    print('controls resolved:', len(twin), 'sample', list(twin.items())[:2])
    dis = lambda A, B, pairs: sum(A[a]['judged'] != B[b]['judged'] for a, b in pairs)
    pairs = sorted(twin.items()); same = [(k, j) for k, j in pairs if npart[j] >= 4]; cross = [(k, j) for k, j in pairs if npart[j] <= 3]
    res['noise'] = {'controls_resolved': len(twin),
                    'preflight_old_K_vs_old_J (1N reported 3/80)': rate(dis(oldK, old, pairs), len(pairs)),
                    'new_K_vs_new_J_all': rate(dis(newK, new, pairs), len(pairs)),
                    'new_K_vs_new_J_same_session(parts4-5)': rate(dis(newK, new, same), len(same)),
                    'new_K_vs_new_J_cross_session(parts1-3)': rate(dis(newK, new, cross), len(cross)),
                    'new_K_vs_old_K': rate(sum(newK[k]['judged'] != oldK[k]['judged'] for k, _ in pairs), len(pairs)),
                    'new_J_vs_old_J_on_the_80_twins': rate(sum(new[j]['judged'] != old[j]['judged'] for _, j in pairs), len(pairs)),
                    'direction_new_K_vs_old_K (c2w, w2c)': [sum(oldK[k]['judged'] == 'correct' and newK[k]['judged'] != 'correct' for k, _ in pairs), sum(oldK[k]['judged'] != 'correct' and newK[k]['judged'] == 'correct' for k, _ in pairs)],
                    'judge_noise_1n_verbatim': R.get('judge_noise')}
    tb = [j for j in both_w]; res['noise']['type_disagreement_both_wrong'] = rate(sum(str(new[j].get('type')) != str(old[j].get('type')) for j in tb), len(tb))
    # Task E cross-check
    ce = json.load(open(os.path.join(O, 'taskCE_items.json'))); log('1o:derived', 'taskCE_items.json (E buckets of false rejections)', len(ce))
    ce1n = [r for r in ce if r['id'] in inv]; eb = collections.defaultdict(lambda: [0, 0])
    for r in ce1n:
        e = str(r['E']); eb[e][1] += 1; eb[e][0] += (not ncq(inv[r['id']]))
    res['taskE_crosscheck'] = {'n_fr_1n_in_taskCE': len(ce1n), 'flipped_to_wrong_by_E': {k: {'flipped': v[0], 'n': v[1]} for k, v in sorted(eb.items())},
                               'E4_ids_flipped': sorted(r['id'] for r in ce1n if '4' in str(r['E']) and not ncq(inv[r['id']])),
                               'E4_ids_kept_correct': sorted(r['id'] for r in ce1n if '4' in str(r['E']) and ncq(inv[r['id']]))}
    log('1o:judge', 'recon by the closing worker: judged-counts per out_*.json, aggregates only (12:3x local)', 980, 'shape/count recon before Task B', 'closing worker inline python')
    log('1n:judge', 'recon by the closing worker: judged-counts per out_*.json, aggregates only (12:3x local)', 980, 'shape/count recon before Task B', 'closing worker inline python')
    json.dump(res, open(os.path.join(O, 'taskB_results.json'), 'w'), indent=1, ensure_ascii=False)
    # ---------- TASK_B.md
    m = res['movement']; a, b = m['correct_to_wrong'], m['wrong_to_correct']; u = res['under_new_labels']; cn = res['concentration']; nz = res['noise']
    pts = u['label_points_of_6.93']; lo, hi = u['label_points_bootstrap95']
    predominant = a['n'] > b['n'] and m['sign_test_p_two_sided'] < 0.05
    concentrated = cn['c2w_stack_rejected']['ci'][0] > base_rej['pct']
    e4 = res['taskE_crosscheck']['flipped_to_wrong_by_E']; e4k = [k for k in e4 if '4' in k]; e4f = sum(e4[k]['flipped'] for k in e4k); e4n = sum(e4[k]['n'] for k in e4k)
    L = []
    L.append('# Phase 1O - Task B: blind re-judge of the closed 1N set with `topic` restored\n')
    L.append('0 model calls, no network. Script `phase1o/diag/taskB_rejudge.py`, numbers `phase1o/taskB_results.json`. Intervals: exact Clopper-Pearson 95 %%. The apparatus was pre-flighted: with the ORIGINAL labels it reproduces 350/426 and 14/474 and both published intervals exactly; old K-vs-J control disagreement reproduces %s (1N reported 3/80).\n' % fr(nz['preflight_old_K_vs_old_J (1N reported 3/80)']))
    L.append('## 0. The bad news first\n')
    L.append('1. **The labels explain %+.2f of the 6.93 points** (coverage under the re-judged labels %s against 1N %s; paired sentence bootstrap of the difference [%+.2f, %+.2f], 2000 draws, %d sentences). %s' % (pts, fr(u['coverage']), fr(u['coverage_1n']), lo, hi, res['n_sentences'], 'The bootstrap interval includes 0: the label effect on coverage is not distinguishable from nothing.' if lo <= 0 <= hi else 'The bootstrap interval excludes 0.'))
    L.append('2. **The hypothesis (a topic-less judge passed marginal answers, depressing coverage and flattering FA together) is %s.** It needs movement that is predominantly correct->wrong AND concentrated on stack-rejected items. Movement: correct->wrong %d, wrong->correct %d (two-sided sign test p = %.4f) - predominance %s. Concentration: %s of the correct->wrong items were stack-rejected, against a base rate of %s among all 1N judged-correct items - concentration %s.' % (
        'SUPPORTED by this data' if predominant and concentrated else ('PARTLY supported' if predominant or concentrated else 'NOT supported by this data'),
        a['n'], b['n'], m['sign_test_p_two_sided'], 'holds' if predominant else 'does NOT hold at the 5 % level', fr(cn['c2w_stack_rejected']), fr(base_rej),
        'holds (lower bound above the base rate)' if concentrated else 'is NOT established (the interval reaches the base rate)'))
    L.append('3. **FA is worse under the new labels, which is what the hypothesis predicts: %s against 1N %s.** %d of the %d correct->wrong items were stack-ACCEPTED and become new false accepts; %d of the %d wrong->correct items were stack-rejected (new false rejections), %d were stack-accepted.' % (fr(u['fa']), fr(u['fa_1n']), a['stack_accepted'], a['n'], b['stack_rejected'], b['n'], b['stack_accepted']))
    L.append('4. **The AMOUNT of movement (%s of items) is no larger than the noise yardsticks; only its DIRECTION (item 2) stands out, and its effect on coverage is small (item 1).** New controls K vs their J twins under the new labels %s (same session, twins in parts 4-5: %s; across the two sessions, twins in parts 1-3: %s); new K vs old K %s; 1N baselines 3/80 = 3.75 %% (same-session verdict disagreement) and 2/80 = 2.5 %% (cross-session filler drift). A single re-judge cannot separate "topic" from ordinary re-judging noise except through asymmetry and these yardsticks.' % (fr(m['moved_total']), fr(nz['new_K_vs_new_J_all']), fr(nz['new_K_vs_new_J_same_session(parts4-5)']), fr(nz['new_K_vs_new_J_cross_session(parts1-3)']), fr(nz['new_K_vs_old_K'])))
    L.append('5. **Task E cross-check: of the %d 1N false rejections Task E called E4 ("answer really wrong, judge generous"), the blind re-judge flipped %d to wrong.**\n' % (e4n, e4f))
    L.append('## 1. Movement\n')
    L.append('| direction | n | stack-accepted | stack-rejected | by writer intent (id prefix) | by type | judge passive tag old>new | by packet |')
    L.append('|---|---|---|---|---|---|---|---|')
    L.append('| correct -> wrong | %d | %d | %d | %s | new type: %s | %s | %s |' % (a['n'], a['stack_accepted'], a['stack_rejected'], a['by_writer_intent'], a['by_type_new'], a['by_passive_old>new'], a['by_part']))
    L.append('| wrong -> correct | %d | %d | %d | %s | old type: %s | %s | %s |' % (b['n'], b['stack_accepted'], b['stack_rejected'], b['by_writer_intent'], b['by_type_old'], b['by_passive_old>new'], b['by_part']))
    L.append('\nTotals: old correct %d, new correct %d, correct under both %d, wrong under both %d. 1N layer of the correct->wrong items: %s. The layer of 1N judged-wrong items is not stored per item in the files this task used. Moved by session: parts 1-3 %s (c2w, w2c = %s), parts 4-5 %s (c2w, w2c = %s). Type disagreement on items wrong under both: %s.\n' % (
        n_cov, res['totals']['new_correct'], len(both_c), len(both_w), a['by_layer_1n'], fr(m['moved_by_session']['parts1-3']), m['net_by_session']['parts1-3'], fr(m['moved_by_session']['parts4-5']), m['net_by_session']['parts4-5'], fr(nz['type_disagreement_both_wrong'])))
    L.append('Concentration: of the 76 false rejections %s flipped to wrong; of the 350 accepted-correct %s flipped to wrong; of the 14 false accepts %s flipped to correct; of the 460 true rejections %s flipped to correct.\n' % (fr(cn['share_of_76_FR_flipped_to_wrong']), fr(cn['share_of_350_accepted_flipped_to_wrong']), fr(cn['share_of_14_FA_flipped_to_correct']), fr(cn['share_of_460_true_rej_flipped_to_correct'])))
    L.append('## 2. Coverage and FA against the new labels\n')
    L.append('| metric | 1N labels | re-judged labels |')
    L.append('|---|---|---|')
    L.append('| coverage | %s | %s |' % (fr(u['coverage_1n']), fr(u['coverage'])))
    L.append('| FA | %s | %s |' % (fr(u['fa_1n']), fr(u['fa'])))
    L.append('| coverage, items correct under BOTH labelings | - | %s |' % fr(u['coverage_both_correct']))
    L.append('| FA, items wrong under BOTH labelings | - | %s |' % fr(u['fa_both_wrong']))
    L.append('| coverage, new-correct items without a new-judge passive tag | - | %s |' % fr(u['coverage_nonpassive_new']))
    tl = sorted(set(res['fa_by_type']['new_labels']) | set(res['fa_by_type']['old_labels_1n']))
    L.append('\n| FA by type | 1N labels (old type) | re-judged labels (new type) |')
    L.append('|---|---|---|')
    for t in tl:
        L.append('| %s | %s | %s |' % (t, fr(res['fa_by_type']['old_labels_1n'][t]) if t in res['fa_by_type']['old_labels_1n'] else '-', fr(res['fa_by_type']['new_labels'][t]) if t in res['fa_by_type']['new_labels'] else '-'))
    L.append('\n## 3. Noise yardsticks\n')
    for k, v in nz.items():
        if isinstance(v, dict) and 'k' in v: L.append('* %s: %s' % (k, fr(v)))
    L.append('* direction new K vs old K (correct->wrong, wrong->correct): %s' % nz['direction_new_K_vs_old_K (c2w, w2c)'])
    L.append('* 1N `judge_noise` block verbatim: `%s`\n' % json.dumps(nz['judge_noise_1n_verbatim'], ensure_ascii=False))
    L.append('## 4. Task E cross-check\n')
    L.append('Flipped to wrong by the blind re-judge, per Task E bucket of the %d 1N false rejections: %s. E4 ids flipped: %s. E4 ids kept correct: %s.\n' % (res['taskE_crosscheck']['n_fr_1n_in_taskCE'], json.dumps(e4), res['taskE_crosscheck']['E4_ids_flipped'], res['taskE_crosscheck']['E4_ids_kept_correct']))
    L.append('## 5. Caveats\n')
    L.append('* The judge agent/model of 1N and of 1M is recorded nowhere we could find; judge identity is an uncontrolled difference between the labelings.\n* 2 judge sessions here (parts 1-3; parts 4-5 + controls) against 5 packets in 1N; the controls sat in the second session, so K-vs-J is within-session only for twins in parts 4-5.\n* One judge revised part 1 once (J0081 and J0152 re-levelled, both now correct).\n* A single re-judge cannot separate "topic" from ordinary re-judging noise except through the asymmetry of the movement and the yardsticks above.\n* Stack verdicts are the STORED 1N verdicts (results_1n.json `fr_ids` / `fa_ids`); nothing was re-run. Writer intent is the id prefix. The passive tag shown is the judge tag (old>new); the writer passive key was not read.\n* The sign test and Clopper-Pearson intervals treat items as independent; items cluster in 100 sentences (the bootstrap line resamples sentences).')
    open(os.path.join(O, 'TASK_B.md'), 'w').write('\n'.join(L) + '\n')
    print(open(os.path.join(O, 'TASK_B.md')).read())

if __name__ == '__main__':
    main()

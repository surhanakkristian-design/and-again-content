#!/usr/bin/env python3
"""Phase 1O Task F support numbers. 0 model calls: re-scores STORED verdicts only (1N ledger + phase1o/calls.jsonl)
through the Task A module (build / verdicts / score) and the Task B loaders. Writes phase1o/taskF_numbers.json."""
import sys, os, json, collections, traceback
DIAG = os.path.dirname(os.path.abspath(__file__)); O = os.path.dirname(DIAG); sys.path.insert(0, DIAG)
import taskA_oldprompt as T
import taskB_rejudge as B
C = collections.Counter; out = {}
def block(name):
    def deco(f):
        try: out[name] = f()
        except Exception: out[name] = {'ERROR': traceback.format_exc()[-900:]}
        print('##', name, json.dumps(out[name], ensure_ascii=False)[:1500])
    return deco
pids = sorted(set(v for v in vars(T).values() if isinstance(v, str) and v.startswith('P-FROZEN')))
print('prompt ids in module:', pids, 'OLD =', getattr(T, 'OLD', None))
ctx = T.build('Phase 1O Task F: re-score stored verdicts, 0 calls')
B.log('1o:judge', 'Task F reuses the Task B loaders for new and old labels', 980, 'Phase 1O Task F support numbers (0 calls)', 'phase1o/diag/taskF_numbers.py')
new, npart, newK = B.load(O, '1o:judge'); old, opart, oldK = B.load(B.N, '1n:judge')
bm = json.load(open(os.path.join(B.N, 'judge', 'blind_map.json'))); inv = {v: k for k, v in bm.items()}
P1N = [p for p in pids if p != getattr(T, 'OLD', None)]; P1N = P1N[0] if P1N else 'P-FROZEN-1N'
def recs(res):
    if isinstance(res, dict):
        v = list(res.values())
        if v and isinstance(v[0], dict) and 'accepted' in v[0]: return res
        for k, x in res.items():
            r = recs(x)
            if r: return r
    if isinstance(res, (list, tuple)) and res:
        if isinstance(res[0], dict) and 'accepted' in res[0]: return {r.get('item_id', r.get('id')): r for r in res}
        for x in res:
            r = recs(x)
            if r: return r
    return None
def scored(pid, tip_reject=True):
    vm = T.verdicts(ctx, pid)[1]
    if tip_reject: res = T.score(ctx, vm)[0]
    else:
        sel = ctx['sel']; res = T.R1K.configure_row(ctx['st'], ctx['recs'], vm, True, ctx['guards'], False, sel['f9'], False)
    r = recs(res)
    if r is None: print('res type', type(res), (list(res.keys())[:10] if isinstance(res, dict) else str(res)[:300]))
    return r
oc = lambda i: old[inv[i]]['judged'] == 'correct'; nc = lambda i: new[inv[i]]['judged'] == 'correct'
ids = list(inv)
def cov(r, lab, sub=None): 
    s = [i for i in ids if lab(i) and (sub is None or sub(i))]; return B.rate(sum(bool(r[i]['accepted']) for i in s), len(s))
def fa(r, lab):
    s = [i for i in ids if not lab(i)]; return B.rate(sum(bool(r[i]['accepted']) for i in s), len(s))
R1 = scored(P1N); print('sample rec', json.dumps(next(iter(R1.values())))[:400])
@block('sanity_1n_prompt')
def _(): return {'prompt': P1N, 'coverage_old_labels': cov(R1, oc), 'fa_old_labels': fa(R1, oc), 'coverage_new_labels': cov(R1, nc), 'fa_new_labels': fa(R1, nc)}
@block('judged_wrong_1n_by_layer')
def _(): return {'old_labels': dict(C(('ACCEPTED' if R1[i]['accepted'] else str(R1[i]['layer'])) for i in ids if not oc(i))), 'new_labels': dict(C(('ACCEPTED' if R1[i]['accepted'] else str(R1[i]['layer'])) for i in ids if not nc(i)))}
@block('judged_wrong_by_judge_passive_tag')
def _():
    d = {}
    for tag in ('agentless', 'by'):
        s = [i for i in ids if not oc(i) and old[inv[i]].get('passive') == tag]
        d[tag] = {'n_judged_wrong': len(s), 'accepted': sum(bool(R1[i]['accepted']) for i in s), 'layers': dict(C(str(R1[i]['layer']) for i in s if not R1[i]['accepted'])), 'types': dict(C(str(old[inv[i]].get('type')) for i in s))}
        s2 = [i for i in ids if oc(i) and old[inv[i]].get('passive') == tag]
        d[tag]['n_judged_correct'] = len(s2); d[tag]['correct_accepted'] = sum(bool(R1[i]['accepted']) for i in s2)
    return d
@block('tip_off_1n_prompt')
def _():
    r = scored(P1N, False)
    tip_ids_wrong = [i for i in ids if not oc(i) and r[i]['accepted'] and not R1[i]['accepted']]
    return {'coverage_old_labels (1N report: 366/426)': cov(r, oc), 'fa_old_labels (1N report: 81/474)': fa(r, oc), 'coverage_new_labels': cov(r, nc), 'fa_new_labels': fa(r, nc),
            'rescued_correct': sum(1 for i in ids if oc(i) and r[i]['accepted'] and not R1[i]['accepted']), 'rescued_correct_with_agentless_tag': sum(1 for i in ids if oc(i) and r[i]['accepted'] and not R1[i]['accepted'] and old[inv[i]].get('passive') == 'agentless'),
            'new_false_accepts': len(tip_ids_wrong), 'new_false_accepts_by_type': dict(C(str(old[inv[i]].get('type')) for i in tip_ids_wrong))}
RO = scored(T.OLD)
@block('old_prompt')
def _():
    both = lambda i: oc(i) and nc(i)
    have = sum(1 for i in ids if nc(i) and not oc(i))
    return {'coverage_old_labels': cov(RO, oc), 'coverage_both_correct': cov(RO, both), 'coverage_new_labels_(the %d wrong->correct item(s) had no old-prompt call: counted as the stack left them)' % have: cov(RO, nc),
            'coverage_nonpassive_old_labels': cov(RO, oc, lambda i: not old[inv[i]].get('passive')),
            'flips_vs_1n_prompt (reject->accept, accept->reject)': [sum(1 for i in ids if oc(i) and RO[i]['accepted'] and not R1[i]['accepted']), sum(1 for i in ids if oc(i) and not RO[i]['accepted'] and R1[i]['accepted'])],
            'flips_nonpassive': [sum(1 for i in ids if oc(i) and not old[inv[i]].get('passive') and RO[i]['accepted'] and not R1[i]['accepted']), sum(1 for i in ids if oc(i) and not old[inv[i]].get('passive') and not RO[i]['accepted'] and R1[i]['accepted'])]}
@block('old_prompt_tip_off_coverage_only')
def _():
    r = scored(T.OLD, False); return {'coverage_old_labels': cov(r, oc), 'coverage_new_labels': cov(r, nc)}
@block('false_rejections_by_taskC_cause')
def _():
    ce = [r for r in json.load(open(os.path.join(O, 'taskCE_items.json'))) if r['id'] in inv]; d = {}
    for r in ce:
        for key in ('cause:' + str(r['cause']), 'layer:' + str(r['layer']), 'E:' + str(r['E'])):
            x = d.setdefault(key, {'n': 0, 'rejudged_wrong': 0, 'accepted_by_old_prompt': 0, 'writer_prefix': C()})
            x['n'] += 1; x['rejudged_wrong'] += (not nc(r['id'])); x['accepted_by_old_prompt'] += bool(RO[r['id']]['accepted']); x['writer_prefix'][r['id'].split(':')[0]] += 1
    for x in d.values(): x['writer_prefix'] = dict(x['writer_prefix'])
    return d
@block('pooled')
def _():
    return {'1M+1N headline (547+350)/(614+426)': B.rate(897, 1040), '1M + 1N re-judged labels (547+347)/(614+415)': B.rate(894, 1029),
            'non-passive non-cleft 1M 536/571': B.rate(536, 571), 'non-passive non-cleft 1N 266/320': B.rate(266, 320), 'non-passive non-cleft pooled': B.rate(802, 891),
            '1M': B.rate(547, 614), '1N': B.rate(350, 426), 'E_b_central 361/426': B.rate(361, 426), 'E_union_opt 378/426': B.rate(378, 426), 'E_union_cons 361/426': B.rate(361, 426),
            'plus16 366/426': B.rate(366, 426), 'plus13 363/426': B.rate(363, 426), 'plus11 361/426': B.rate(361, 426), 'plus14 364/426': B.rate(364, 426)}
json.dump(out, open(os.path.join(O, 'taskF_numbers.json'), 'w'), indent=1, ensure_ascii=False)

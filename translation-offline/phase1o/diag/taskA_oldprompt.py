#!/usr/bin/env python3
"""Phase 1O Task A + Task D — DIAGNOSTIC re-run on the CLOSED 1N set. Not a new measurement.

Imports the phase1n machinery in-process and re-scores the 1N items through the identical frozen
stack (LOCKTIP + TIP-as-rejection ON + F8 none + F9 off, arm B, gemini-3.1-flash-lite, T 0,
thinkingBudget 0) with ONE difference: prompt 'P-FROZEN' instead of 'P-FROZEN-1N'.

Nothing inside phase1n/ (or any earlier phase dir) is written: every write path the imported
modules hold is redirected IN MEMORY to phase1o/ before any work happens
  RL.CALLS            -> phase1o/calls.jsonl        (the ONLY write ledger)
  LM.LOG / L.LOG / RL.ACCESS -> phase1o/access_log.jsonl (append)
  N.RUNLOG            -> phase1o/diag/run_taskA.log
  STOP_* / PAUSED     -> phase1o/diag/
phase1n/calls.jsonl joins RL.LEDGERS_RO (read-only, reuse by request hash).

Modes
  --preflight   0 calls. P-FROZEN-1N from stored verdicts must reproduce 350/426 and 14/474.
  --plan        0 calls. Requests under P-FROZEN that are not stored; hard cap 600 (exit 4 if over).
  --run         transport (needs phase1o/RUN_COMMIT pointing at a commit holding THIS file).
  --report      0 calls. Writes taskA_results.json, TASK_A.md, TASK_D.md, DEPENDENCY_READS.md.
  --inspect     0 calls. Prints the source of the routing functions (for the Task D write-up).
  --scope all|correct   which L3-eligible items to call (default all; 'correct' = judged-correct
                only = coverage-only diagnosis, FA then NOT measured).
"""
import argparse, collections, hashlib, inspect, json, os, subprocess, sys, time

sys.dont_write_bytecode = True
DIAG = os.path.dirname(os.path.abspath(__file__))
O = os.path.dirname(DIAG)
TOFF = os.path.dirname(O)
NDIR = os.path.join(TOFF, 'phase1n')
REPO = os.path.dirname(TOFF)
ME = 'phase1o/diag/taskA_oldprompt.py'
CALLS_O = os.path.join(O, 'calls.jsonl')
CALLS_N = os.path.join(NDIR, 'calls.jsonl')
ACCESS_O = os.path.join(O, 'access_log.jsonl')
RUN_COMMIT = os.path.join(O, 'RUN_COMMIT')
RUN_EXIT = os.path.join(DIAG, 'RUN_EXIT.json')
CAP = 600
OLD, NEW = 'P-FROZEN', 'P-FROZEN-1N'
EXP_COV, EXP_FA = (350, 426), (14, 474)
COV_1M = (547, 614)
TITLE = 'diagnostic re-run on a closed set, not a new measurement'

sys.path.insert(0, NDIR)
import loader_1l as L                                                          # noqa: E402
import loader_1n as LM                                                         # noqa: E402
import runner_1l as RL                                                         # noqa: E402

# ---- redirect every write path BEFORE runner_1n copies them at import
RL.CALLS = CALLS_O
RL.ACCESS = ACCESS_O
LM.LOG = ACCESS_O
L.LOG = ACCESS_O
RL.STOP_PRE = os.path.join(DIAG, 'STOP_PREFLIGHT.txt')
RL.STOP_PLAN = os.path.join(DIAG, 'STOP_PLAN.txt')
RL.DONE = os.path.join(DIAG, 'UNUSED_DONE')
import runner_1n as N                                                          # noqa: E402
N.RUNLOG = os.path.join(DIAG, 'run_taskA.log')
N.STOP_CHK = os.path.join(DIAG, 'STOP_CHK.txt')
N.PAUSED = os.path.join(DIAG, 'RUN_PAUSED.txt')
N.CALLS = CALLS_O
RL.LEDGERS_RO = list(RL.LEDGERS_RO) + [CALLS_N]          # 1N verdicts: read-only, reuse by hash
R1K, R, P = N.R1K, N.R, N.P
assert os.path.dirname(RL.CALLS) == O and os.path.dirname(N.CALLS) == O
for _p in (LM.LOG, L.LOG, RL.ACCESS, N.RUNLOG, N.STOP_CHK, N.PAUSED, RL.STOP_PRE, RL.STOP_PLAN):
    assert _p.startswith(O + os.sep), _p

_orig_log = LM._log


def _log(side, what, n, purpose, caller=None):
    return _orig_log(side, what, n, purpose, caller='%s (via %s)' % (ME, caller or 'direct'))


LM._log = _log
if hasattr(L, '_log'):
    L._log = _log


def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        for b in iter(lambda: fh.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def counted_o():
    return sum(1 for r in R.ledger_rows(CALLS_O) if r.get('http') == 200)


def fmt(d):
    return RL._r(d) if d and d.get('n') else '—'


# ================================================================== build / score
def build(purpose, with_labels=True):
    cfg, sel = N.load_cfg()
    N.select_f8('f8')
    st, recs, ann, by, info = N.build_side_1n(purpose)
    lock_rej, l3 = N.preflight_1n(st, recs, 'FRESH1N / 1O diagnostic')
    ctx = dict(sel=sel, st=st, recs=recs, ann=ann, by=by, info=info, lock_rej=lock_rej, l3=l3)
    if with_labels:
        labels, controls, lmeta = LM.load_labels(purpose, caller='taskA_oldprompt.py')
        for r in recs:
            if r['item_id'] in labels:
                r['judged'], r['wrong_type'] = labels[r['item_id']]
        ctx.update(labels=labels, lmeta=lmeta)
        N.select_f8('f8')
        g1 = R1K.guard_readouts(recs, ann, sel['f9_strict'])
        N.select_f8('f8v2')
        g2 = R1K.guard_readouts(recs, ann, sel['f9_strict'])
        N.select_f8('f8')
        ctx.update(g1=g1, g2=g2, guards={i: {'f8': None, 'f9': g1[i]['f9']} for i in g1})
    return ctx


def verdicts(ctx, prompt_id):
    hmap = RL.hashes_for(ctx['st'], ctx['recs'], ctx['l3'], prompt_id)
    rep, ver, failed, _c = RL.ledger_state()
    vm = {i: ver[h] for i, h in hmap.items() if h in ver}
    return hmap, vm, rep, ver, failed


def score(ctx, vm):
    sel = ctx['sel']
    res = R1K.configure_row(ctx['st'], ctx['recs'], vm, True, ctx['guards'], False, sel['f9'],
                            sel['tip_reject'])
    return res, RL.col_metrics(ctx['recs'], res, ctx['labels'])


def plan(ctx, scope):
    ids = list(ctx['l3'])
    if scope == 'correct':
        ids = [i for i in ids if ctx['labels'][i][0] == 'correct']
    req = RL.plan_requests(ctx['st'], ctx['recs'], ids, OLD, 'x')
    req = {h: (s, u, g, hh, 'L-1O:taskA-oldprompt', i) for h, (s, u, g, hh, _t, i) in req.items()}
    rep, ver, failed, _c = RL.ledger_state()
    need = [h for h in req if h not in ver and h not in failed]
    return ids, req, need


# ================================================================== modes
def cmd_preflight():
    purpose = 'Phase 1O Task A FIDELITY PRE-FLIGHT: re-score 1N under P-FROZEN-1N from stored verdicts (0 calls)'
    ctx = build(purpose)
    hmap, vm, rep, ver, failed = verdicts(ctx, NEW)
    miss = [i for i in hmap if i not in vm]
    res, m = score(ctx, vm)
    got = ((m['coverage']['k'], m['coverage']['n']), (m['fa']['k'], m['fa']['n']))
    stored = json.load(open(os.path.join(NDIR, 'results_1n.json'), encoding='utf-8'))
    LM._log('1n', 'results_1n.json (metrics, fa_ids, fr_ids)', 1, purpose)
    same_ids = (sorted(m['fa_ids']) == sorted(stored['metrics']['fa_ids'])
                and sorted(m['fr_ids']) == sorted(stored['metrics']['fr_ids']))
    ok = (not miss) and got == (EXP_COV, EXP_FA) and same_ids
    out = {'l3_eligible': len(ctx['l3']), 'lock_rejections_BASE': len(ctx['lock_rej']),
           'verdicts_found': len(vm), 'missing': len(miss), 'coverage': m['coverage'], 'fa': m['fa'],
           'fa_ids_and_fr_ids_identical_to_results_1n': same_ids, 'MATCH': ok, 'model_calls': 0}
    json.dump(out, open(os.path.join(DIAG, 'preflight.json'), 'w'), indent=1)
    print('[PREFLIGHT] L3-eligible %d, stored verdicts %d, missing %d' % (len(ctx['l3']), len(vm), len(miss)))
    print('[PREFLIGHT] coverage %s   FA %s   ids identical %s  -> %s'
          % (fmt(m['coverage']), fmt(m['fa']), same_ids, 'MATCH' if ok else 'MISMATCH'))
    print('[PREFLIGHT] res keys: %s' % sorted(next(iter(res.values())).keys()))
    print('[PREFLIGHT] price in/out per token: %r %r' % (RL.PRICE_IN, RL.PRICE_OUT))
    if not ok:
        raise SystemExit(2)
    return ctx


def cmd_plan(scope):
    purpose = 'Phase 1O Task A PLAN under P-FROZEN (0 calls); labels read only to size the judged-correct subset'
    ctx = build(purpose)
    out = {'cap': CAP, 'already_counted_phase1o': counted_o(), 'scopes': {}}
    for sc in ('all', 'correct'):
        ids, req, need = plan(ctx, sc)
        out['scopes'][sc] = {'l3_items': len(ids), 'unique_requests': len(req), 'new_calls': len(need),
                             'reused': len(req) - len(need)}
        print('[PLAN scope=%s] L3 items %d, unique %d, stored %d, NEW %d (cap %d, counted so far %d)'
              % (sc, len(ids), len(req), len(req) - len(need), len(need), CAP, out['already_counted_phase1o']))
    out['chosen_scope'] = scope
    n = out['scopes'][scope]['new_calls']
    out['over_cap'] = out['already_counted_phase1o'] + n > CAP
    json.dump(out, open(os.path.join(DIAG, 'plan.json'), 'w'), indent=1)
    if out['over_cap']:
        open(os.path.join(DIAG, 'STOP_PLAN.txt'), 'w').write(json.dumps(
            {'why': 'the plan exceeds the 600-call phase cap; nothing trimmed, 0 calls made',
             'plan': out}, indent=1) + '\n')
        print('[PLAN] STOP: %d + %d > %d — 0 calls made' % (out['already_counted_phase1o'], n, CAP))
        raise SystemExit(4)
    return out


def cmd_run(scope):
    if not os.path.exists(RUN_COMMIT):
        raise SystemExit('REFUSED: phase1o/RUN_COMMIT missing — commit the module first')
    rc = open(RUN_COMMIT).read().split()[0]
    cur = subprocess.check_output(['git', 'hash-object', os.path.abspath(__file__)], cwd=REPO).decode().strip()
    was = subprocess.check_output(['git', 'rev-parse', '%s:translation-offline/%s' % (rc, ME)],
                                  cwd=REPO).decode().strip()
    if cur != was:
        raise SystemExit('REFUSED: the module differs from RUN_COMMIT %s' % rc)
    before = sha(CALLS_N)
    info = {'run_commit': rc, 'scope': scope, 'sha256_phase1n_calls_before': before, 'started': time.time()}
    try:
        purpose = 'Phase 1O Task A RUN under P-FROZEN (scope %s)' % scope
        ctx = build(purpose, with_labels=(scope == 'correct'))
        ids, req, need = plan(ctx, scope)
        done = counted_o()
        if done + len(need) > CAP:
            info['stopped'] = 'over cap: %d + %d > %d' % (done, len(need), CAP)
            raise SystemExit(4)
        made = {'ok': 0, 'bad': 0, 'empty': 0, 'skipped': 0, 'wall': False}
        if need:
            made = N.make_calls(req, need)
        rep, ver, failed, _c = RL.ledger_state()
        still = [h for h in req if h not in ver and h not in failed]
        info.update(made=made, planned_new=len(need), unique=len(req), still_without_verdict=len(still),
                    counted_failures=len([h for h in req if h in failed]))
    finally:
        info['sha256_phase1n_calls_after'] = sha(CALLS_N)
        info['phase1n_calls_unchanged'] = info['sha256_phase1n_calls_after'] == before
        info['counted_phase1o'] = counted_o()
        info['ended'] = time.time()
        json.dump(info, open(RUN_EXIT, 'w'), indent=1)


def cmd_inspect():
    fs = [(P.run_pipeline, 90), (R1K.apply_guards, 25), (R1K.locktip_decide, 30), (P.ledger_append, 8)]
    for f, cap in fs:
        src = [l for l in inspect.getsource(f).split('\n') if l.strip() and not l.strip().startswith('#')]
        print('=====', f.__module__, f.__name__, len(src))
        print('\n'.join(l[:200] for l in src[:cap]))


def passive_split(ctx, res):
    by, lab = ctx['by'], ctx['labels']
    out = {}
    for tag in (None, 'by', 'agentless'):
        ids = [i for i in by if lab[i][0] == 'correct' and by[i].get('passive') == tag]
        acc = [i for i in ids if res[i]['accepted']]
        out[str(tag)] = {'coverage': P.rate(len(acc), len(ids)),
                         'rejected_by_layer': dict(collections.Counter(
                             str(res[i]['layer']) for i in ids if not res[i]['accepted']))}
    return out


def jsonable(x):
    return json.loads(json.dumps(x, default=str, ensure_ascii=False))


def cmd_report():
    purpose = 'Phase 1O Task A/D REPORT: score 1N items under P-FROZEN-1N (stored) and P-FROZEN with the ORIGINAL 1N judge labels'
    ctx = build(purpose)
    by, lab, l3 = ctx['by'], ctx['labels'], ctx['l3']
    hA, vmA, rep, ver, failed = verdicts(ctx, NEW)
    hB, vmB, _r, _v, _f = verdicts(ctx, OLD)
    LM._log('1n', 'calls.jsonl (stored verdicts + raw replies, read-only)', len(vmA), purpose)
    resA, mA = score(ctx, vmA)
    l3c = [i for i in l3 if lab[i][0] == 'correct']
    l3w = [i for i in l3 if lab[i][0] == 'wrong']
    have_c = all(i in vmB for i in l3c)
    have_w = all(i in vmB for i in l3w)
    noverd = sorted(i for i in l3 if i not in vmB)
    failedB = sorted(i for i in l3 if hB[i] in failed)
    resB = mB = None
    if have_c:
        resB, mB = score(ctx, vmB)
    spend = dict(RL.token_spend())
    spend.pop('phase_budget_remaining_estimate', None)
    rc = open(RUN_COMMIT).read().split()[0] if os.path.exists(RUN_COMMIT) else None
    run_exit = json.load(open(RUN_EXIT)) if os.path.exists(RUN_EXIT) else None
    planj = json.load(open(os.path.join(DIAG, 'plan.json'))) if os.path.exists(os.path.join(DIAG, 'plan.json')) else None
    pre = json.load(open(os.path.join(DIAG, 'preflight.json'))) if os.path.exists(os.path.join(DIAG, 'preflight.json')) else None
    status = ('COMPLETE' if have_c and have_w else 'COVERAGE-ONLY (judged-wrong items not called; FA not measured)'
              if have_c else 'NOT RUN — old-prompt verdicts missing for %d of %d L3-eligible items' % (len(noverd), len(l3)))

    out = {'title': TITLE, 'status': status, 'run_commit': rc, 'prompt_1N': NEW, 'prompt_old': OLD,
           'frozen_config': ctx['sel'], 'fidelity_preflight': pre, 'plan': planj, 'run_exit': run_exit,
           'calls_phase1o': spend, 'price': {'in_per_1M': 0.25, 'out_per_1M': 1.50},
           'l3_eligible': len(l3), 'l3_judged_correct': len(l3c), 'l3_judged_wrong': len(l3w),
           'items_without_old_prompt_verdict': noverd, 'of_which_counted_failures_empty_or_parse': failedB,
           'no_verdict_scoring': 'never guessed: the pipeline gets no verdict for the item and does not accept it at L3',
           'metrics_1N': {k: mA[k] for k in ('coverage', 'fa', 'fa_by_type', 'fa_by_layer', 'fr_by_layer')},
           'passive_split_1N': passive_split(ctx, resA)}
    if mB:
        out['metrics_old_prompt'] = {k: mB[k] for k in ('coverage', 'fa', 'fa_by_type', 'fa_by_layer', 'fr_by_layer')}
        out['passive_split_old_prompt'] = passive_split(ctx, resB)
        tm = {'correct': collections.Counter(), 'wrong': collections.Counter()}
        for i in l3:
            if i in vmB:
                tm[lab[i][0]]['%s->%s' % (vmA.get(i, 'NONE'), vmB.get(i, 'NONE'))] += 1
        flips = []
        for i in by:
            if i in l3 and i not in vmB:
                continue
            if resA[i]['accepted'] != resB[i]['accepted']:
                flips.append({'id': i, 'judged': lab[i][0], 'type': lab[i][1], 'passive': by[i].get('passive'),
                              'direction': 'reject->accept' if resB[i]['accepted'] else 'accept->reject',
                              'L3_1N': vmA.get(i), 'L3_old': vmB.get(i),
                              'layer_1N': str(resA[i]['layer']), 'layer_old': str(resB[i]['layer'])})
        out['l3_transitions_1N_to_old'] = {k: dict(v) for k, v in tm.items()}
        out['accept_reject_flips'] = flips
        covB = mB['coverage']['pct']
        pts = round(covB - 82.16, 2)
        out['gap'] = {'gap_1M_to_1N_points': 6.93, 'coverage_old_prompt_pct': covB,
                      'points_explained_by_prompt': pts,
                      'verdict': 'all' if pts >= 6.93 else 'none' if pts <= 0 else 'some'}

    # ---------------- Task D rows
    rowsD = []
    agl = [i for i in by if lab[i][0] == 'correct' and by[i].get('passive') == 'agentless']
    for i in sorted(agl):
        if resA[i]['accepted']:
            continue
        r = by[i]
        rowsD.append({'id': i, 'sid': r['sid'], 'slovak': r['sk'], 'answer': r['answer'], 'references': r['refs'],
                      'rejecting_layer_1N': str(resA[i]['layer']), 'l3_eligible': i in l3,
                      'L3_verdict_1N': vmA.get(i), 'raw_reply_1N': rep.get(hA[i]) if i in hA else None,
                      'L3_verdict_old_prompt': vmB.get(i), 'raw_reply_old_prompt': rep.get(hB[i]) if i in hB and i in vmB else None,
                      'accepted_under_old_prompt': (resB[i]['accepted'] if resB and (i not in l3 or i in vmB) else None),
                      'layer_old_prompt': (str(resB[i]['layer']) if resB and (i not in l3 or i in vmB) else None),
                      'chk': r['chk'], 'lock_ok': r.get('lock_ok'), 'intent': r.get('intent'), 'form': r.get('form'),
                      'pipeline_row_1N': jsonable(resA[i]),
                      'f8v1_readout': jsonable(ctx['g1'][i].get('f8')), 'f8v2_readout': jsonable(ctx['g2'][i].get('f8')),
                      'f9_readout': jsonable(ctx['g1'][i].get('f9'))})
    nD = collections.Counter()
    for x in rowsD:
        lay = x['rejecting_layer_1N']
        nD['TIP-turned-rejection' if lay == 'L3:TIPrej' else 'L3 DIFF' if lay == 'L3' else 'guard ' + lay] += 1
    out['taskD'] = {'agentless_judged_correct': len(agl), 'accepted': len(agl) - len(rowsD), 'rejected': len(rowsD),
                    'rejection_kind': dict(nD), 'rows': rowsD}
    json.dump(out, open(os.path.join(O, 'taskA_results.json'), 'w'), indent=1, ensure_ascii=False)

    # ---------------- TASK_A.md
    t = ['# Phase 1O Task A — %s' % TITLE, '',
         'Closed Phase 1N set (900 items, 100 sentences), ORIGINAL 1N judge labels, identical frozen stack '
         '(%s, arm B, `%s`, temperature 0, thinkingBudget 0). The ONLY difference between the two columns is the '
         'prompt: `%s` (the 1N run, stored verdicts) versus `%s` (the 1M prompt, no voice line).'
         % (ctx['sel']['name'], ctx['sel']['model'], NEW, OLD), '',
         '**Status: %s.** Run commit `%s`.' % (status, rc), '',
         '## Fidelity pre-flight (0 calls)', '',
         '* `%s` re-scored by this module from stored verdicts: coverage %s, FA %s — expected 350/426 and 14/474: **%s** '
         '(FA and FR id lists identical to `results_1n.json`: %s).'
         % (NEW, fmt(mA['coverage']), fmt(mA['fa']),
            'MATCH' if (mA['coverage']['k'], mA['coverage']['n'], mA['fa']['k'], mA['fa']['n']) == EXP_COV + EXP_FA else 'MISMATCH',
            (pre or {}).get('fa_ids_and_fr_ids_identical_to_results_1n')), '']
    if planj:
        t += ['## Plan (0 calls)', '', '| scope | L3 items | unique requests | already stored | NEW calls |', '|---|---|---|---|---|']
        for sc, d in planj['scopes'].items():
            t.append('| %s | %d | %d | %d | %d |' % (sc, d['l3_items'], d['unique_requests'], d['reused'], d['new_calls']))
        t += ['', '* hard cap for the whole phase: %d counted calls; counted in `phase1o/calls.jsonl` when planned: %d.'
              % (planj['cap'], planj['already_counted_phase1o']), '']
    if mB:
        t += ['## Side by side', '', '| metric | 1N run (`%s`) | old prompt (`%s`) |' % (NEW, OLD), '|---|---|---|',
              '| coverage | %s | %s |' % (fmt(mA['coverage']), fmt(mB['coverage'])),
              '| FA overall | %s | %s |' % (fmt(mA['fa']), fmt(mB['fa']) if have_w else 'not measured')]
        for ty in N.TYPES:
            t.append('| FA type %s | %s | %s |' % (ty, fmt(mA['fa_by_type'][ty]), fmt(mB['fa_by_type'][ty]) if have_w else 'not measured'))
        for lay in sorted(set(mA['fr_by_layer']) | set(mB['fr_by_layer'])):
            t.append('| FR at %s | %s | %s |' % (lay, fmt(mA['fr_by_layer'].get(lay)), fmt(mB['fr_by_layer'].get(lay))))
        for lay in sorted(set(mA['fa_by_layer']) | set(mB['fa_by_layer'])):
            t.append('| FA at %s | %s | %s |' % (lay, fmt(mA['fa_by_layer'].get(lay)), fmt(mB['fa_by_layer'].get(lay)) if have_w else 'not measured'))
        pa, pb = out['passive_split_1N'], out['passive_split_old_prompt']
        for tag in ('None', 'by', 'agentless'):
            t.append('| coverage, passive tag %s | %s | %s |' % (tag, fmt(pa[tag]['coverage']), fmt(pb[tag]['coverage'])))
        t += ['', 'All intervals are exact 95 % Clopper-Pearson. Same items, same labels in both columns: the intervals '
              'describe each column, the paired flips below describe the difference.', '',
              '## L3 verdict transitions, `%s` -> `%s`' % (NEW, OLD), '']
        for j in ('correct', 'wrong'):
            t += ['**judged %s**: `%s`' % (j, json.dumps(out['l3_transitions_1N_to_old'][j], sort_keys=True)), '']
        t += ['### Items whose final accept/reject flipped', '', '| id | judged | type | passive | direction | L3 1N -> old | layer 1N -> old |', '|---|---|---|---|---|---|---|']
        for f in out['accept_reject_flips']:
            t.append('| %s | %s | %s | %s | %s | %s -> %s | %s -> %s |' % (f['id'], f['judged'], f['type'], f['passive'],
                     f['direction'], f['L3_1N'], f['L3_old'], f['layer_1N'], f['layer_old']))
        g = out['gap']
        t += ['', '## How much of the gap is the prompt', '',
              'The 1M -> 1N coverage gap is 89.09 - 82.16 = **6.93 points**. Under the old prompt the same 1N items score '
              '**%s**, i.e. %+.2f points against 82.16: the prompt explains **%s** of the gap (%+.2f of 6.93 points); '
              'the remaining %.2f points are NOT the prompt (the set, the items, the labels).'
              % (fmt(mB['coverage']), g['points_explained_by_prompt'], g['verdict'].upper(),
                 g['points_explained_by_prompt'], 6.93 - g['points_explained_by_prompt']), '']
    else:
        t += ['## Result', '', '**No old-prompt figure exists.** %s. No model call was made for a plan above the cap; '
              'nothing was trimmed and nothing was guessed.' % status, '']
    notesA = os.path.join(DIAG, 'taskA_notes.md')
    if os.path.exists(notesA):
        t += [open(notesA, encoding='utf-8').read().rstrip(), '']
    t += ['## Calls', '',
          '* counted calls (HTTP 200) in `phase1o/calls.jsonl`: **%d**; uncounted retries (http 0/429/5xx): %d; '
          'empty-200 / parse failures (counted, never retried, never guessed): %d.'
          % (spend['counted_calls_http200'], spend['non200_attempts'], spend['failed_empty_200']),
          '* items without an old-prompt verdict: %d (%d of them counted failures). %s.'
          % (len(noverd), len(failedB), out['no_verdict_scoring']),
          '* tokens in %d, out %d; list-price spend at $0.25 in / $1.50 out per 1M tokens: **$%.5f**.'
          % (spend['tokens_in'], spend['tokens_out'], spend['tokens_in'] * 0.25e-6 + spend['tokens_out'] * 1.5e-6),
          '* `phase1n/calls.jsonl` byte-unchanged: %s.' % ((run_exit or {}).get('phase1n_calls_unchanged', 'no run — not touched')), '']
    open(os.path.join(O, 'TASK_A.md'), 'w', encoding='utf-8').write('\n'.join(t))

    # ---------------- TASK_D.md
    d = ['# Phase 1O Task D — the agentless passive (0 extra model calls)', '',
         '%d judged-correct 1N items carry passive tag `agentless`: %d accepted, **%d rejected**. '
         'How the %d were rejected under `%s`: `%s`.'
         % (len(agl), len(agl) - len(rowsD), len(rowsD), len(rowsD), NEW, json.dumps(dict(nD), sort_keys=True)), '']
    notes = os.path.join(DIAG, 'taskD_notes.md')
    if os.path.exists(notes):
        d += [open(notes, encoding='utf-8').read().rstrip(), '']
    d += ['## The %d rejected items' % len(rowsD), '']
    for x in rowsD:
        d += ['### %s' % x['id'], '',
              '* Slovak: %s' % x['slovak'], '* answer: %s' % x['answer'],
              '* reference(s): %s' % ' | '.join(x['references']),
              '* rejecting layer (1N): **%s**; L3-eligible: %s; chk `%s`; lock_ok %s'
              % (x['rejecting_layer_1N'], x['l3_eligible'], json.dumps(x['chk'], ensure_ascii=False), x['lock_ok']),
              '* model reply under `%s`: verdict %s, raw `%s`' % (NEW, x['L3_verdict_1N'], x['raw_reply_1N']),
              '* model reply under `%s`: %s' % (OLD, ('verdict %s, raw `%s` -> %s at %s' % (
                  x['L3_verdict_old_prompt'], x['raw_reply_old_prompt'],
                  'ACCEPTED' if x['accepted_under_old_prompt'] else 'rejected', x['layer_old_prompt']))
                  if x['L3_verdict_old_prompt'] or x['accepted_under_old_prompt'] is not None else 'not run'),
              '* pipeline row (1N): `%s`' % json.dumps(x['pipeline_row_1N'], ensure_ascii=False)[:600],
              '* readouts (decide nothing): F8v1 `%s`, F8v2 `%s`, F9 `%s`'
              % (json.dumps(x['f8v1_readout'], ensure_ascii=False)[:160], json.dumps(x['f8v2_readout'], ensure_ascii=False)[:160],
                 json.dumps(x['f9_readout'], ensure_ascii=False)[:160]), '']
    open(os.path.join(O, 'TASK_D.md'), 'w', encoding='utf-8').write('\n'.join(d))

    # ---------------- DEPENDENCY_READS.md
    mods = sorted(os.path.relpath(m.__file__, TOFF) for m in list(sys.modules.values())
                  if getattr(m, '__file__', None) and m.__file__.startswith(TOFF + os.sep))
    dep = ['# Phase 1O Task A/D — dependency reads', '',
           'Imported in-process (forced by the chain `taskA_oldprompt -> runner_1n -> runner_1l -> runner_1k -> ...`); '
           'nothing was written into any of these directories:', ''] + ['* `%s`' % m for m in mods]
    dep += ['', 'Read by hand (source text): `phase1n/runner_1n.py` (whole), `phase1n/HANDOFF_RUNNER_1N.md`, '
            '`phase1n/FROZEN_CONFIG_1N.json`, `phase1n/DEPENDENCY_READS.md` (tail); via `inspect.getsource` only the '
            'functions the module calls: `runner_1l.call_one / ledger_state / token_spend / load_keys / plan_requests / '
            'hashes_for / col_metrics / _r`, `pipeline_1i.rate / run_pipeline / ledger_append`, '
            '`runner_1k.configure_row / apply_guards / locktip_decide`, `runner_1j.ledger_rows`, '
            '`loader_1n._log / load_labels`.', '']
    open(os.path.join(O, 'DEPENDENCY_READS.md'), 'w', encoding='utf-8').write('\n'.join(dep))
    print('[REPORT] status: %s' % status)
    print('[REPORT] 1N   coverage %s  FA %s' % (fmt(mA['coverage']), fmt(mA['fa'])))
    if mB:
        print('[REPORT] OLD  coverage %s  FA %s  gap explained %+.2f' % (fmt(mB['coverage']), fmt(mB['fa']) if have_w else 'n/a',
                                                                      out['gap']['points_explained_by_prompt']))
    print('[REPORT] Task D: %s' % json.dumps(out['taskD']['rejection_kind'], sort_keys=True))
    for x in rowsD:
        print('  D %s | %s | L3 %s raw %r | old %s | %s' % (x['id'], x['rejecting_layer_1N'], x['L3_verdict_1N'],
                                                           x['raw_reply_1N'], x['L3_verdict_old_prompt'],
                                                           json.dumps(x['pipeline_row_1N'], ensure_ascii=False)[:260]))


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    for k in ('preflight', 'plan', 'run', 'report', 'inspect'):
        g.add_argument('--' + k, action='store_true')
    ap.add_argument('--scope', choices=('all', 'correct'), default='all')
    a = ap.parse_args()
    if a.preflight:
        cmd_preflight()
    elif a.plan:
        cmd_plan(a.scope)
    elif a.run:
        cmd_run(a.scope)
    elif a.inspect:
        cmd_inspect()
    else:
        cmd_report()


if __name__ == '__main__':
    main()

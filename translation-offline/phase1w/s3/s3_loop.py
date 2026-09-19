#!/usr/bin/env python3
"""Phase 1W §3 loop round 3: A2(a) L3 determiner prompt line on the CLOSED 1U + 1T sets.
Re-calls only reached-L3 items whose prompt changes; everything else replays stored verdicts."""
import os, sys, json, collections, datetime
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__)); W = os.path.dirname(HERE); TO = os.path.dirname(W)
RUN = os.path.join(HERE, 'run')
for p in (os.path.join(TO, 'phase1u', 'run'), os.path.join(TO, 'phase1v', 'trackA_loop'), HERE):
    if p not in sys.path:
        sys.path.insert(0, p)
import runner_1u as RU                                                         # noqa: E402
RU.set_run_dir(RUN)
import loop_1v as LP                                                           # noqa: E402
import s3_detline as DL                                                        # noqa: E402
R1P, R1K, RL = RU.R1P, RU.R1K, RU.RL
BUDGET, EXTRA = 200, ('rs_nom',)
TARGETS = ['C:1900%s:c2' % x for x in ('09', '28', '39', '59', '84', '94')]
WANT = {'1U': (390, 402, 13, 498), '1T': (394, 421, 9, 479)}
out = {'phase': '1W', 'section': 3, 'model': 'gemini-3.1-flash-lite', 'temperature': 0, 'thinkingBudget': 0,
       'det_line': DL.DET_LINE, 'ts': datetime.datetime.now().isoformat(timespec='seconds')}


def kn(m):
    return (m['coverage']['k'], m['coverage']['n'], m['FA']['k'], m['FA']['n'])


def m2a(v):
    return {'SAME': (True, 'L3'), 'TIP': (False, 'L3:TIPrej'), 'DIFF': (False, 'L3')}[v]


u = LP.load_1u(); t, tnotes, _ = LP.load_1t()
sets = {'1U': u, '1T': t}
base = {k: LP.apply(v, EXTRA, True)[0] for k, v in sets.items()}
bm = {k: LP.metrics(v) for k, v in base.items()}
out['baseline_check'] = {k: {'got': kn(bm[k]), 'want': WANT[k], 'ok': kn(bm[k]) == WANT[k]} for k in sets}
assert all(v['ok'] for v in out['baseline_check'].values()), out['baseline_check']
st1u = {r['item_id']: (r.get('layers') or {}) for r in
        json.load(open(os.path.join(TO, 'phase1u', 'run', 'results_1u.json')))['rows']}
st1t = {r['item_id']: (r.get('layers') or {}) for r in
        json.load(open(os.path.join(TO, 'phase1t', 'run', 'results_1t.json')))['rows']}
sides = {'1U': (os.path.join(TO, 'phase1u', 'data'), RU.PROMPT_1U, st1u),
         '1T': (os.path.join(TO, 'phase1u', 'taskR', 'data_restored'), R1P.PROMPT_1P, st1t)}
req_all, plan = {}, {}
for k, (dd, pid, stored) in sides.items():
    cfg, sel, st, recs, ann, by, info, ag = RU.build(dd, 'w1w_s3_' + k, 'Phase 1W s3 closed %s loop round 3' % k)
    rows = {r['id']: r for r in sets[k]}
    reached = [i for i, r in rows.items() if r['layer0'] in ('L3', 'L3:TIPrej') and not r['v4']]
    missing = [i for i in reached if i not in by]
    trig = sorted(i for i in reached if i in by and DL.det_diff(by[i]['answer'], by[i]['reference']))
    # replay apparatus: stored model verdict -> (acc0, layer0) mapping on every reached row
    mm = collections.Counter()
    for i in reached:
        v = (stored.get(i) or {}).get('model')
        mm['ok' if v in ('SAME', 'TIP', 'DIFF') and m2a(v) == (rows[i]['acc0'], rows[i]['layer0']) else 'mismatch:%s' % v] += 1
    req0, h0 = R1P.plan(st, recs, trig, pid)
    hrep = collections.Counter('match' if (stored.get(i) or {}).get('req_hash') == h0[i] else
                               ('no_stored_hash' if not (stored.get(i) or {}).get('req_hash') else 'MISMATCH')
                               for i in trig)
    orig = DL.install(RU, ids=set(trig))
    try:
        req1, h1 = R1P.plan(st, recs, trig, pid)
    finally:
        R1K.build_req = orig
    bad = []
    for i in trig:
        a, b = req0[h0[i]][1].split('\n'), req1[h1[i]][1].split('\n')
        if len(b) != len(a) + 1 or b.count(DL.DET_LINE) != 1 or [x for x in b if x != DL.DET_LINE] != a \
                or req0[h0[i]][0] != req1[h1[i]][0] or h0[i] == h1[i]:
            bad.append(i)
    assert not bad, ('prompt assertion failed', bad[:5])
    req_all.update(req1)
    plan[k] = {'reached_l3': len(reached), 'not_in_build': len(missing), 'triggered': len(trig), 'ids': trig,
               'h_new': {i: h1[i] for i in trig}, 'stored_model': {i: (stored.get(i) or {}).get('model') for i in trig},
               'replay_map_check': dict(mm), 'old_hash_reproduction': dict(hrep), 'prompt_assertion': 'ok (+1 line, sys same)',
               'targets_triggered': [x for x in TARGETS if x in trig] if k == '1U' else None}
ver, failed, counted = RU.ledger_state_1u()
need = sorted({h for k in plan for h in plan[k]['h_new'].values()} - set(ver) - set(failed))
out['plan'] = {k: {kk: vv for kk, vv in v.items() if kk != 'h_new'} for k, v in plan.items()}
out['planned_new_calls'] = len(need)
stop = []
if counted + len(need) > BUDGET:
    stop.append('budget: %d counted + %d planned > %d; 0 calls made, round NOT RUN' % (counted, len(need), BUDGET))
tier_of, switched = {}, None
if not stop:
    keys = RL.load_keys(); key = keys[0]; tier = 'free' if len(keys) > 1 else 'single-key(default)'
    for h in need:
        if RU.ledger_state_1u()[2] >= BUDGET:
            stop.append('budget reached mid-round'); break
        row = RL.call_one(req_all[h], key)
        if row.get('http') != 200 and len(keys) > 1 and key == keys[0]:
            key, tier, switched = keys[-1], 'paid', h
            row = RL.call_one(req_all[h], key)
        tier_of[h] = tier
ver, failed, counted = RU.ledger_state_1u()
calls = RU.rows_of(RU.CALLS)
c200 = [r for r in calls if r.get('http') == 200]
tin = sum(r.get('prompt_tokens') or 0 for r in c200); tout = sum((r.get('candidates_tokens') or 0) + (r.get('thoughts_tokens') or 0) for r in c200)
pin, pout = getattr(RL, 'PRICE_IN', 0.10e-6), getattr(RL, 'PRICE_OUT', 0.40e-6)
out['calls'] = {'counted_http200': len(c200), 'uncounted_non200': sum(1 for r in calls if r.get('http') != 200),
                'failed_200_unparsable': len(failed), 'failed_items': failed, 'tokens_in': tin, 'tokens_out': tout,
                'spend_usd_list_price': round(tin * pin + tout * pout, 5), 'price_in_per_tok': pin, 'price_out_per_tok': pout,
                'key_tiers': dict(collections.Counter(tier_of.values())), 'switched_to_paid_at': switched,
                'log': os.path.relpath(RU.CALLS, TO)}
after, flips = {}, {}
for k in sets:
    nv = {}
    for i, h in plan[k]['h_new'].items():
        if h in ver:
            nv[i] = m2a(ver[h])
        elif h in failed:
            nv[i] = (False, 'L3:FAILED')
    new = [dict(r, acc0=nv[r['id']][0], layer0=nv[r['id']][1]) if r['id'] in nv else r for r in sets[k]]
    after[k] = LP.apply(new, EXTRA, True)[0]
    b = {r['id']: r for r in base[k]}; f = collections.defaultdict(list)
    for r in after[k]:
        o = b[r['id']]
        if o['acc'] != r['acc']:
            f[('gain_correct' if r['acc'] else 'loss_correct') if r['judged'] == 'correct' else
              ('COST_wrong_accepted' if r['acc'] else 'catch_wrong_rejected')].append(r['id'])
    flips[k] = dict(f)
am = {k: LP.metrics(v) for k, v in after.items()}
worse = {k: LP.worse(am[k], bm[k]) for k in sets}
cost = {k: len(flips[k].get('COST_wrong_accepted', [])) for k in sets}
gain = {k: round(am[k]['coverage']['pct'] - bm[k]['coverage']['pct'], 2) for k in sets}
if any(worse.values()):
    stop.append('a worse cell: %s' % {k: v for k, v in worse.items() if v})
if any(c > 2 for c in cost.values()):
    stop.append('guard cost > 2: %s' % cost)
if max(gain.values()) < 1 and 1.99 < 1:
    stop.append('two consecutive rounds < 1 point')
if not need and not stop:
    stop.append('nothing to call')
tf = []
for i in TARGETS:
    a = next(r for r in after['1U'] if r['id'] == i); h = plan['1U']['h_new'].get(i)
    tf.append({'id': i, 'triggered': h is not None, 'old': plan['1U']['stored_model'].get(i), 'new': ver.get(h) if h else None,
               'accepted_after': a['acc'], 'layer_after': a['layer']})
decision = 'REVERT' if stop and not (stop == [] ) else 'KEEP'
if stop and all(s.startswith('budget') is False for s in stop) and False:
    pass
if not stop:
    decision = 'KEEP'
out.update({'before': bm, 'after': am, 'worse_cells': worse, 'flips': flips, 'guard_cost': cost, 'coverage_gain_pt': gain,
            'targets': tf, 'stop_rules_triggered': stop, 'decision': decision,
            'stack_entry_for_s4': ('translation-offline/phase1w/stack_1w_s3.py: install_prompt(RU) before plan(), then '
                                   'decide(...)/final_accept(row, extra=("rs_nom",), tip=True)') if decision == 'KEEP' else
                                  'translation-offline/phase1w/stack_1w.py (1V round 2 + s2), unchanged prompt; s3 REVERTED',
            't_notes': tnotes})
if decision != 'KEEP' and os.path.exists(os.path.join(W, 'stack_1w_s3.py')):
    os.remove(os.path.join(W, 'stack_1w_s3.py'))
json.dump(out, open(os.path.join(W, 's3_result.json'), 'w'), indent=1, ensure_ascii=False, default=str)


def f(d):
    return '%d/%d = %.2f %% [%.2f, %.2f]' % (d['k'], d['n'], d['pct'], *d['ci'])


L = ['# Phase 1W §3 result: A2(a) L3 determiner prompt line, loop round 3 on closed 1U + 1T (IN-SAMPLE, not a result)', '',
     '- Decision: **%s**' % decision,
     '- Stop rules triggered: %s' % (stop or 'none'),
     '- Stack entry for §4: %s' % out['stack_entry_for_s4'],
     '- Model calls counted (http 200): %d' % out['calls']['counted_http200'],
     '- Model calls uncounted (http 0/429/5xx retries): %d' % out['calls']['uncounted_non200'],
     '- Model calls FAILED (empty/unparsable 200): %d' % out['calls']['failed_200_unparsable'],
     '- Loop budget: %d of %d' % (out['calls']['counted_http200'], BUDGET),
     '- Spend (list price, tokens in %d / out %d): $%.5f; key tiers %s; switched to paid at %s' % (
         tin, tout, out['calls']['spend_usd_list_price'], out['calls']['key_tiers'], switched),
     '- Call log: translation-offline/%s' % out['calls']['log'],
     '- Prompt line (inserted per record only where answer vs reference differ in determiner tokens alone, after the last inserted line, before the tail): "%s"' % DL.DET_LINE]
for k in sets:
    p = plan[k]
    L += ['- %s reached L3 (non-AG): %d; triggered/re-called: %d; not in build: %d' % (k, p['reached_l3'], p['triggered'], p['not_in_build']),
          '- %s replay check (stored model verdict reproduces stored layer): %s' % (k, p['replay_map_check']),
          '- %s old-prompt hash reproduction on triggered items: %s' % (k, p['old_hash_reproduction'])]
L += ['', '## Per set, per cell (before = 1V round 2 + §2; after = + §3 line)']
for k in sets:
    L += ['- %s coverage before: %s' % (k, f(bm[k]['coverage'])), '- %s coverage after: %s' % (k, f(am[k]['coverage'])),
          '- %s FA before: %s' % (k, f(bm[k]['FA'])), '- %s FA after: %s' % (k, f(am[k]['FA']))]
    for t_ in sorted(set(bm[k]['FA_by_type']) | set(am[k]['FA_by_type'])):
        o, n = bm[k]['FA_by_type'].get(t_), am[k]['FA_by_type'].get(t_)
        L.append('- %s FA type %s: %s -> %s' % (k, t_, '%d/%d' % (o['k'], o['n']) if o else '-', '%d/%d' % (n['k'], n['n']) if n else '-'))
    for c in sorted(k2 for k2 in bm[k] if k2 not in ('coverage', 'FA', 'FA_by_type')):
        L.append('- %s cell %s: %s -> %s' % (k, c, json.dumps(bm[k][c], default=str)[:160], json.dumps(am[k][c], default=str)[:160]))
    L += ['- %s worse cells: %s' % (k, worse[k] or 'none'),
          '- %s guard cost (judged-wrong newly accepted): %d %s' % (k, cost[k], flips[k].get('COST_wrong_accepted', [])),
          '- %s flips: %s' % (k, json.dumps(flips[k])),
          '- %s coverage gain: %+.2f pt' % (k, gain[k])]
L += ['', '## The 6 target items (1U plain-L3 determiner false rejections)']
L += ['- %s: triggered %s, L3 %s -> %s, final %s (%s)' % (x['id'], x['triggered'], x['old'], x['new'],
                                                         'ACCEPT' if x['accepted_after'] else 'reject', x['layer_after']) for x in tf]
L += ['', '## Caveats', '- Closed sets, IN-SAMPLE: the line was written looking at the 6 1U targets.',
      '- 1T is re-called under ITS OWN prompt (P-FROZEN-1P) + the line; 1U under P-FROZEN-1U + the line: each is a one-line change from the stored stack.',
      '- The possessive sentence of the line goes beyond the owner wording (article + demonstrative); 2 of the 6 targets are possessive (028 my, 059 our).',
      '- A FAILED call is scored as a rejection (never guessed).']
open(os.path.join(W, 'S3_RESULT.md'), 'w').write('\n'.join(L) + '\n')
print('\n'.join(L))

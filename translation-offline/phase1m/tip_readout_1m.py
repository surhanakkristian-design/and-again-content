#!/usr/bin/env python3
"""Phase 1M label `readout` — ZERO-CALL readout of already-stored verdicts.

Scores the three CLOSED sides (dev, replay1j, fresh1l) under the candidate stack
F8v2 + F9-off, with TIP-as-rejection ON and OFF, using only verdicts that are
already in the ledgers.  Makes NO model call and opens nothing under data/ or judge/.

NOTE ON ORDERING: phase1i/checker_1i keeps ONE module-global annotation/SK map, which
`R.make_state` overwrites per side.  A side must therefore be scored immediately after
it is built (this is exactly what runner_1l.run_dev does); building all three sides and
scoring afterwards makes the checker re-hygienise a stale side and crash.
"""
import os, sys, json, datetime

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import runner_1m as RM                      # noqa: E402  (does the whole RL/R1K wiring)
RL, R1K, P = RM.RL, RM.R1K, RM.P
P1L = RM.P1L

os.environ['PHASE1J_FINAL'] = '1'
os.environ['PHASE1K_OPEN_FRESH'] = '1'

LABEL = 'readout'
ACCESS = os.path.join(HERE, 'access_log.jsonl')


def alog(side, what, n, purpose):
    row = {'ts': datetime.datetime.now(datetime.timezone.utc).isoformat(),
           'side': side, 'what': what, 'caller': 'tip_readout_1m.py[%s]' % LABEL,
           'n': n, 'purpose': purpose}
    with open(ACCESS, 'a', encoding='utf-8') as fh:
        fh.write(json.dumps(row, ensure_ascii=False) + '\n')


PURPOSE = ('Phase 1M brief 1.3 zero-call readout: re-score the CLOSED sides under '
           'F8v2/F9-off with TIP-as-rejection on vs off, stored verdicts only')

COMBOS = [('base_1l', 'f8', True, True),
          ('f8v2_only', 'f8v2', True, True),
          ('f9off_only', 'f8', False, True),
          ('new_tip_reject', 'f8v2', False, True),
          ('new_tip_accept', 'f8v2', False, False)]

OUT = {'generated': datetime.datetime.now(datetime.timezone.utc).isoformat(),
       'zero_calls': True, 'model_calls_made': 0, 'sides': {}}

hyg0 = RL.HYG
for side in ('dev', 'replay1j', 'fresh1l'):
    if side == 'fresh1l':
        RL.HYG = os.path.join(P1L, 'hygiene')
        st, recs, ann, by, info = RL.build_side('fresh', True, PURPOSE)
        labels, _k, _v = R1K.judge_labels('fresh', PURPOSE)
    else:
        RL.HYG = hyg0
        st, recs, ann, by, info = RL.build_side(side, False, PURPOSE)
        labels, _k, _v = R1K.judge_labels({'dev': 'dev', 'replay1j': 'holdout1j'}[side], PURPOSE)
    RL.HYG = hyg0
    alog(side, 'records+judge labels (closed side, re-scored offline)', len(recs), PURPOSE)
    for r in recs:
        if r['item_id'] in labels:
            r['judged'], r['wrong_type'] = labels[r['item_id']]
    lock_rej, l3 = RL.lock_counts(st, recs)
    hmap = RL.hashes_for(st, recs, l3, 'P-FROZEN')
    rep, ver, failed, _cl = RL.ledger_state()
    vm = {i: ver[h] for i, h in hmap.items() if h in ver}
    need = sorted(i for i, h in hmap.items() if h not in ver)
    print('[%s] items %d  L3-eligible %d  stored verdicts %d  WOULD-NEED-A-CALL %d'
          % (side.upper(), len(recs), len(l3), len(vm), len(need)))

    gcache = {}

    def score(f8name, f9_on, tip_reject, vm_use):
        RM.select_f8(f8name)
        if f8name not in gcache:
            gcache[f8name] = R1K.guard_readouts(recs, ann, False)
        res = R1K.configure_row(st, recs, vm_use, True, gcache[f8name], True, f9_on, tip_reject)
        return RL.col_metrics(recs, res, labels)

    row = {'n_items': len(recs), 'l3_eligible': len(l3), 'stored_verdicts': len(vm),
           'need_call': len(need), 'need_call_ids': need,
           'lock_rejections_BASE': len(lock_rej), 'combos': {}}
    for name, f8n, f9on, tipr in COMBOS:
        m = score(f8n, f9on, tipr, vm)
        row['combos'][name] = {
            'f8': f8n, 'f9': 'on' if f9on else 'off',
            'tip': 'reject' if tipr else 'accept',
            'coverage': m['coverage'], 'fa': m['fa'],
            'fa_by_type': {t: m['fa_by_type'][t] for t in RL.TYPES},
            'fa_ids': sorted(m['fa_ids'])}
    if need:                       # bounds only if some L3 item has no stored verdict
        for name, f8n, f9on, tipr in COMBOS[3:]:
            for bound, forced in (('lo_rejected', 'DIFF'), ('hi_accepted', 'SAME')):
                vmx = dict(vm)
                for i in need:
                    vmx[i] = forced
                m = score(f8n, f9on, tipr, vmx)
                row['combos'][name]['bound_' + bound] = {
                    'coverage': m['coverage'], 'fa': m['fa'], 'faT': m['fa_by_type']['T']}

    if side == 'fresh1l':
        f = row['combos']
        base = set(f['base_1l']['fa_ids'])
        byid = {r['item_id']: r for r in recs}

        def det(ids):
            out = []
            for i in ids:
                r = byid.get(i, {})
                out.append({'item_id': i, 'type': r.get('wrong_type'), 'sid': r.get('sid'),
                            'sk': r.get('sk'), 'answer': r.get('answer'),
                            'reference': r.get('reference')})
            return out

        fixed8 = sorted(base - set(f['f8v2_only']['fa_ids']))
        OUT['fresh1l_diag'] = {
            'f8v2_alone': {'fa_before': [f['base_1l']['fa']['k'], f['base_1l']['fa']['n']],
                           'fa_after': [f['f8v2_only']['fa']['k'], f['f8v2_only']['fa']['n']],
                           'cov_before': [f['base_1l']['coverage']['k'],
                                          f['base_1l']['coverage']['n']],
                           'cov_after': [f['f8v2_only']['coverage']['k'],
                                         f['f8v2_only']['coverage']['n']],
                           'fixed_ids': fixed8,
                           'new_fa_ids': sorted(set(f['f8v2_only']['fa_ids']) - base),
                           'fixed_detail': det(fixed8)},
            'f9off_alone': {'fa_before': [f['base_1l']['fa']['k'], f['base_1l']['fa']['n']],
                            'fa_after': [f['f9off_only']['fa']['k'], f['f9off_only']['fa']['n']],
                            'cov_before': [f['base_1l']['coverage']['k'],
                                           f['base_1l']['coverage']['n']],
                            'cov_after': [f['f9off_only']['coverage']['k'],
                                          f['f9off_only']['coverage']['n']],
                            'new_fa_ids': sorted(set(f['f9off_only']['fa_ids']) - base),
                            'new_fa_detail': det(sorted(set(f['f9off_only']['fa_ids']) - base)),
                            'fixed_ids': sorted(base - set(f['f9off_only']['fa_ids']))}}
    OUT['sides'][side] = row

json.dump(OUT, open(os.path.join(HERE, 'tip_readout_1m.json'), 'w'), indent=1, ensure_ascii=False)

for side in ('dev', 'replay1j', 'fresh1l'):
    r = OUT['sides'][side]
    print('\n== %s  (need_call %d)' % (side.upper(), r['need_call']))
    for name in ('base_1l', 'f8v2_only', 'f9off_only', 'new_tip_reject', 'new_tip_accept'):
        c = r['combos'][name]
        print('  %-16s cov %s | FA %s' % (name, RL._r(c['coverage']), RL._r(c['fa'])))
        print('      by type ' + '  '.join('%s %d/%d' % (t, c['fa_by_type'][t]['k'],
                                                         c['fa_by_type'][t]['n'])
                                           for t in RL.TYPES))
d = OUT['fresh1l_diag']
print('\nfresh1l F8v2 alone: FA %s -> %s ; fixed %s ; new %s'
      % (d['f8v2_alone']['fa_before'], d['f8v2_alone']['fa_after'],
         d['f8v2_alone']['fixed_ids'], d['f8v2_alone']['new_fa_ids']))
for x in d['f8v2_alone']['fixed_detail']:
    print('   FIX %s type=%s sid=%s | %s | ANS %s' % (x['item_id'], x['type'], x['sid'],
                                                      x['sk'], x['answer']))
print('fresh1l F9-off alone: FA %s -> %s ; new %s ; fixed %s'
      % (d['f9off_alone']['fa_before'], d['f9off_alone']['fa_after'],
         d['f9off_alone']['new_fa_ids'], d['f9off_alone']['fixed_ids']))
print('-- written phase1m/tip_readout_1m.json (0 model calls)')

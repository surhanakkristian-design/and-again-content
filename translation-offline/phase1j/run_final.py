#!/usr/bin/env python3
"""Phase 1j — the ONE final run (agent F) and the zero-call DEV reproduction of the selected row.

    PYTHONDONTWRITEBYTECODE=1 python3 phase1j/run_final.py --side dev        # 0 new calls, reproduces DEV
    PHASE1J_FINAL=1 PYTHONDONTWRITEBYTECODE=1 python3 phase1j/run_final.py --side holdout

Everything comes from phase1j/FROZEN_CONFIG_1J.json; the logic is the shared library
phase1j/taskC/runner_1j.py, so the holdout requests are built by exactly the code that built the DEV
requests. The holdout is read ONLY through loader_1j. The API key is read only inside
pipeline_1i.load_key(). Counted calls (HTTP 200) go to the ONE shared ledger phase1j/ledger.jsonl and
are also mirrored into taskD/final_calls.jsonl.
"""
import argparse, collections, json, os, random, sys
from concurrent.futures import ThreadPoolExecutor

P1J = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(P1J, 'taskC'))
import runner_1j as R                                                       # noqa: E402
import pipeline_1i as P                                                     # noqa: E402

CFG = json.load(open(os.path.join(P1J, 'FROZEN_CONFIG_1J.json'), encoding='utf-8'))
DONE = os.path.join(P1J, 'FINAL_RUN_DONE')
TASKD = os.path.join(P1J, 'taskD')
ARM, SWITCH = CFG['arm'], CFG['switch'] == 'on'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--side', required=True, choices=('dev', 'holdout'))
    a = ap.parse_args()
    if a.side == 'holdout':
        if os.environ.get('PHASE1J_FINAL') != '1':
            raise SystemExit('REFUSED: the holdout run needs PHASE1J_FINAL=1.')
        if os.path.exists(DONE):
            raise SystemExit('REFUSED: %s exists — the holdout is measured once.' % DONE)
    os.makedirs(TASKD, exist_ok=True)
    purpose = 'Phase 1j FINAL run of the frozen 1j config' if a.side == 'holdout' \
        else 'Phase 1j: zero-call reproduction of the selected DEV row'
    data = R.load_side(a.side, purpose)
    recs0 = data[0]
    prim, sens, rel = R.label_sets(recs0, a.side)
    ALL = R.build_all(a.side, data, purpose)
    reuse_1i = ALL['_reuse']
    rep, ver, counted, failed_h, retries = R.ledger_state()
    ver = dict(ver); ver.update({h: v for h, v in reuse_1i.items() if h not in ver})

    need = [h for h in ALL[ARM]['req'] if h not in ver and h not in rep and h not in failed_h]
    print('side=%s arm=%s switch=%s  L3=%d  unique prompts=%d  reused=%d  NEW calls needed=%d'
          % (a.side, ARM, CFG['switch'], len(ALL[ARM]['l3']), len(ALL[ARM]['req']),
             len(ALL[ARM]['req']) - len(need), len(need)))
    if a.side == 'dev':
        if need:
            raise SystemExit('FAIL: --side dev must need ZERO new calls, needs %d' % len(need))
    else:
        if counted + len(need) > R.CAP_TOTAL:
            raise SystemExit('REFUSED: %d + %d > hard cap %d' % (counted, len(need), R.CAP_TOTAL))
        if need:
            todo = [ALL[ARM]['req'][h] for h in need]
            random.Random(1).shuffle(todo)
            key = P.load_key()
            with ThreadPoolExecutor(max_workers=6) as pool:
                for _ in pool.map(lambda q: R.call_one(q, key), todo):
                    pass
            rep, ver, counted, failed_h, retries = R.ledger_state()
            ver = dict(ver); ver.update({h: v for h, v in reuse_1i.items() if h not in ver})

    out = {'side': a.side, 'frozen': CFG, 'relabel': rel, 'rows': {}}
    A = ALL[ARM]
    for lname, lab in (('primary', prim), ('sensitivity', sens)):
        use = lab if R.ARMS[ARM]['labels'] == 'b' else \
            {r['item_id']: (r['judged'], r['wrong_type']) for r in recs0}
        vm, tags = R.arm_verdict_map(ARM, A['hashes'], rep, ver, SWITCH)
        res = P.run_pipeline(A['st'], vm,
                             tip_reject=(False if R.ARMS[ARM]['contract'] else SWITCH))
        m = R.score(R.relabel(A['recs'], use), res)
        fa_full = []
        for f in m['fa_items']:
            r = A['by_id'][f['id']]
            fa_full.append(dict(f, model_reply=rep.get(A['hashes'].get(f['id']), ''),
                                slovak_used=r['sk'], reference=r['reference'], answer=r['answer']))
        out['rows'][lname] = {'coverage': m['coverage'], 'fa': m['fa'],
                              'fa_by_type': m['fa_by_type'], 'fa_by_layer': m['fa_by_layer'],
                              'fr_by_layer': m['fr_by_layer'],
                              'false_rejections': m['false_rejections'],
                              'false_acceptances': fa_full,
                              'no_verdict_items': [i for i in A['l3'] if i not in vm]}
        if lname == 'primary':
            with open(os.path.join(TASKD, 'final_verdicts.jsonl'), 'w', encoding='utf-8') as fh:
                for i in sorted(res):
                    fh.write(json.dumps(dict(res[i], model_reply=rep.get(A['hashes'].get(i), '')),
                                        ensure_ascii=False) + '\n')
    # zero-call BASE replay (the frozen Phase 1i config) on the same items
    vmb, _ = R.arm_verdict_map('BASE', ALL['BASE']['hashes'], rep, ver, True)
    resb = P.run_pipeline(ALL['BASE']['st'], vmb, tip_reject=True)
    mb = R.score(R.relabel(ALL['BASE']['recs'],
                           {r['item_id']: (r['judged'], r['wrong_type']) for r in recs0}), resb)
    out['base_1i_replay_same_items'] = {'coverage': mb['coverage'], 'fa': mb['fa'],
                                        'fa_by_type': mb['fa_by_type'],
                                        'fa_by_layer': mb['fa_by_layer'],
                                        'fr_by_layer': mb['fr_by_layer'],
                                        'new_calls': 0}
    out['calls'] = R.token_spend()
    out['calls']['transport_retries'] = retries
    out['calls']['reused_prompts'] = len(A['req']) - len(need)
    out['calls']['new_this_run'] = len(need)
    if a.side == 'holdout':
        rows = [r for r in R.ledger_rows() if r.get('http') == 200]
        with open(os.path.join(TASKD, 'final_calls.jsonl'), 'w', encoding='utf-8') as fh:
            for r in rows:
                fh.write(json.dumps(r, ensure_ascii=False) + '\n')
        json.dump(out, open(os.path.join(TASKD, 'final_summary.json'), 'w'), indent=1,
                  ensure_ascii=False)
        open(DONE, 'w').write(json.dumps({'coverage': out['rows']['primary']['coverage'],
                                          'fa': out['rows']['primary']['fa']}) + '\n')
    else:
        json.dump(out, open(os.path.join(TASKD, 'dev_reproduction.json'), 'w'), indent=1,
                  ensure_ascii=False)
    pr = out['rows']['primary']
    print('coverage %s' % R._r(pr['coverage']))
    print('FA       %s' % R._r(pr['fa']))
    for t in ('T', 'W', 'M', 'S'):
        print('  FA %s  %s' % (t, R._r(pr['fa_by_type'][t])))
    print('FA by layer %s   FR by layer %s' % (pr['fa_by_layer'], pr['fr_by_layer']))
    print('sensitivity: coverage %s  FA %s'
          % (R._r(out['rows']['sensitivity']['coverage']), R._r(out['rows']['sensitivity']['fa'])))
    print('BASE 1i replay (0 calls): coverage %s  FA %s'
          % (R._r(out['base_1i_replay_same_items']['coverage']),
             R._r(out['base_1i_replay_same_items']['fa'])))
    print('calls %s' % json.dumps(out['calls']))
    if a.side == 'holdout':
        print('false acceptances, itemised:')
        for f in pr['false_acceptances']:
            print(json.dumps(f, ensure_ascii=False))
        print('FINAL_RUN_DONE written — the holdout is closed.')
    if a.side == 'dev':
        exp = CFG['selected_dev_numbers']
        ok = (pr['coverage']['k'] == exp['coverage']['k'] and pr['fa']['k'] == exp['fa']['k']
              and len(need) == 0)
        print('DEV reproduction with ZERO new calls: %s' % ('OK' if ok else 'MISMATCH'))


if __name__ == '__main__':
    main()

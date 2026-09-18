#!/usr/bin/env python3
"""Phase 1i — run the FROZEN configuration end to end on one side.

    python3 run_config.py --side dev                    # reproduces the Task E DEV numbers, 0 new calls
    PHASE1I_TASK_F=1 python3 run_config.py --side holdout   # the ONE holdout measurement (Task F)

Reads `FROZEN_CONFIG.json`. Goes through `loader.py` only, so the holdout guard and the access log own the
access. Applies Task B (`backfill_s_ids` + `lock_fix`) to *that side's* annotations by script, then Task C's
frozen guard set, then the frozen prompt variant at L3. Resumable (ledger `taskF/<side>_calls.jsonl`,
HTTP-200 rows are never re-called), hard cap 600 model calls, reuses a stored verdict only when the prompt
text is byte-identical to the one it would send. Writes `taskF/<side>_verdicts.jsonl` and
`taskF/<side>_summary.json`. On `--side holdout` it creates `HOLDOUT_RUN_DONE` when finished and refuses to
start if that file already exists. The API key is read only inside `pipeline_1i.load_key()`.
"""
import argparse
import collections
import json
import os
import random
import sys
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pipeline_1i as P                                                     # noqa: E402

TASKF = os.path.join(HERE, 'taskF')
DONE = os.path.join(HERE, 'HOLDOUT_RUN_DONE')
CAP = 600


def prompt_key(st, rec, variant):
    """The identity under which a stored verdict may be reused: variant + the exact prompt text."""
    user, _g, _eq = P.build_prompt(st, rec, variant)
    return user


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--side', required=True, choices=('dev', 'holdout'))
    ap.add_argument('--cap', type=int, default=CAP)
    ap.add_argument('--dry', action='store_true', help='score from the ledger only, make no call')
    a = ap.parse_args()
    if a.side == 'holdout' and os.path.exists(DONE):
        raise SystemExit('REFUSED: %s exists — the holdout is measured once.' % DONE)
    cfg = json.load(open(os.path.join(HERE, 'FROZEN_CONFIG.json'), encoding='utf-8'))
    variant, scoring = cfg['prompt_variant'], cfg['tip_scoring']
    guards = tuple(cfg['c_guards'])
    os.makedirs(TASKF, exist_ok=True)
    ledger = os.path.join(TASKF, '%s_calls.jsonl' % a.side)

    st = P.configure(b_fix=True, guards=guards, side=a.side)          # backfill + lock_fix + guards
    recs = {r['item_id']: r for r in st['recs']}
    l3 = sorted(i for i, v in P.run_pipeline(st, {}).items() if v['reached_l3'])

    # ---- stored verdicts that may be reused: same variant AND byte-identical prompt text
    have, fails, retries = P.ledger_verdicts(ledger)
    reuse, reuse_src = {}, collections.Counter()
    for src in (os.path.join(HERE, 'taskE', 'calls.jsonl'),):
        if not os.path.exists(src):
            continue
        for ln in open(src, encoding='utf-8'):
            try:
                row = json.loads(ln)
            except Exception:
                continue
            if row.get('http') == 200 and row.get('variant') == variant \
                    and row.get('verdict') in ('SAME', 'TIP', 'DIFF') and row['item_id'] in recs:
                reuse[row['item_id']] = row['verdict']
    if variant == 'P-B':                          # the frozen prompt: row-7 verdicts are reusable as well
        for i, r in recs.items():
            m = (r.get('rows', {}).get('row7') or {}).get('model')
            if m in ('SAME', 'TIP', 'DIFF'):
                reuse.setdefault(i, m)

    vm, todo = {}, []
    for i in l3:
        if (variant, i) in have:
            vm[i] = have[(variant, i)]
        elif (variant, i) in fails:
            pass                                   # a failed call is never retried, never guessed
        elif i in reuse:
            vm[i] = reuse[i]
            reuse_src['stored_byte_identical_prompt'] += 1
        else:
            todo.append(i)
    print('side=%s  L3=%d  in ledger=%d  reused=%d  to call=%d  cap=%d'
          % (a.side, len(l3), len(have), sum(reuse_src.values()), len(todo), a.cap))
    if len(todo) > a.cap:
        raise SystemExit('REFUSED: %d calls needed > cap %d' % (len(todo), a.cap))

    n = {'ok': 0, 'bad': 0}
    if todo and not a.dry:
        key = P.load_key()
        random.Random(1618).shuffle(todo)

        def work(i):
            v, row = P.call_variant(st, recs[i], variant, ledger, key)
            if row.get('http') == 200 and v:
                n['ok'] += 1
            else:
                n['bad'] += 1
            return i, v

        with ThreadPoolExecutor(max_workers=4) as pool:
            for i, v in pool.map(work, todo):
                if v:
                    vm[i] = v
        have, fails, retries = P.ledger_verdicts(ledger)
        for (vv, i), val in have.items():
            if vv == variant:
                vm[i] = val

    res = P.run_pipeline(st, vm, tip_reject=(scoring == 'tip_reject'))
    m = P.metrics(st, res)
    with open(os.path.join(TASKF, '%s_verdicts.jsonl' % a.side), 'w', encoding='utf-8') as fh:
        for i in sorted(res):
            row = dict(res[i])
            row['model_verdict'] = vm.get(i)
            fh.write(json.dumps(row, ensure_ascii=False) + '\n')
    split = collections.Counter(vm.get(i) or 'none' for i in l3)
    acc_split = collections.Counter((vm.get(i) or 'none') for i in l3 if res[i]['accepted'])
    hist = collections.Counter()
    if os.path.exists(ledger):
        for ln in open(ledger, encoding='utf-8'):
            hist[json.loads(ln).get('http')] += 1
    n_calls = sum(v for k, v in hist.items() if k == 200)
    summary = {
        'side': a.side, 'frozen_config': {k: cfg[k] for k in ('prompt_variant', 'tip_scoring',
                                                              'c_guards', 'model', 'generationConfig')},
        'n_items': len(recs), 'l3_items': len(l3),
        'coverage': m['coverage'], 'fa': m['fa'], 'fa_by_type': m['fa_by_type'],
        'fa_by_layer': m['fa_by_layer'], 'fa_by_half': m['fa_by_half'],
        'model_verdict_split': dict(split), 'accepted_by_model_verdict': dict(acc_split),
        'tip_accepts': m['tip_accepts'],
        'calls': {'http_200': n_calls, 'made_this_run': n['ok'] + n['bad'],
                  'failed_calls_200_unparsable': len({k for k in fails if k[0] == variant}),
                  'transport_rows_not_counted': sum(v for k, v in hist.items() if k != 200),
                  'reused': dict(reuse_src)},
        'failed_items_no_verdict': m['failed_items'],
        'false_acceptances': m['fa_items'], 'false_rejections': m['false_rejections'],
        'fr_by_layer': m['fr_by_layer'],
    }
    json.dump(summary, open(os.path.join(TASKF, '%s_summary.json' % a.side), 'w'), indent=1,
              ensure_ascii=False)
    print('coverage %s\nFA       %s\nT %s  by layer %s  by half %s'
          % (m['coverage'], m['fa'], m['fa_by_type']['T'], m['fa_by_layer'],
             {k: (v['k'], v['n']) for k, v in m['fa_by_half'].items()}))
    print('calls:', json.dumps(summary['calls']))
    if a.side == 'holdout':
        open(DONE, 'w').write(json.dumps({'summary': os.path.join('taskF', 'holdout_summary.json'),
                                          'coverage': m['coverage'], 'fa': m['fa']}) + '\n')
        print('HOLDOUT_RUN_DONE written — the holdout is now closed.')


if __name__ == '__main__':
    main()

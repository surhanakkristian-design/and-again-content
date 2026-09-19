#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phase 1M - F8v1 vs F8v2 on DEV / replay1j / 1L-fresh with the STORED judge labels.

ZERO model calls, zero network, zero DB.  Writes phase1m/F8V2_DEV_EVAL.md.
Run:  PYTHONDONTWRITEBYTECODE=1 python3 -B phase1m/eval_f8v2.py
"""
import datetime
import json
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import loader_1l as L          # noqa: E402  (logs into phase1m/access_log.jsonl)
import runner_1l as RL         # noqa: E402  (wires R1K / f8 / f9)
import f8                      # noqa: E402
import f8v2                    # noqa: E402

CALLER = 'f8v2-build'
PURPOSE = 'F8v2 agent-demotion guard: offline replay of the stored judge labels (0 model calls)'
ACC = os.path.join(HERE, 'access_log.jsonl')
OUT = os.path.join(HERE, 'F8V2_DEV_EVAL.md')
EIGHT = [140006, 140014, 140024, 140037, 140041, 140058, 140060, 140064]


def alog(side, what, n):
    with open(ACC, 'a') as f:
        f.write(json.dumps({'ts': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
                            'side': side, 'what': what, 'caller': CALLER, 'n': n,
                            'purpose': PURPOSE}, ensure_ascii=False) + '\n')


def get_ann(ann, sid):
    return ann.get(str(sid)) or ann.get(sid) or None


def build(side, label_src, hyg):
    st, recs, ann, by, info = RL.build_side(side, hyg, PURPOSE)
    alog(side, 'records+annotations (build_side)', len(recs))
    labels, _k, _v = RL.R1K.judge_labels(label_src, PURPOSE)
    alog(side, 'judge labels (%s)' % label_src, len(labels))
    rows = []
    for r in recs:
        jd = labels.get(r['item_id'])
        judged, wt = (jd if jd else (r.get('judged'), r.get('wrong_type')))
        a = get_ann(ann, r['sid'])
        rows.append({'item_id': r['item_id'], 'sid': r['sid'], 'sk': r['sk'], 'answer': r['answer'],
                     'intent': r.get('intent'), 'judged': judged, 'type': wt, 'labeled': bool(jd),
                     'v1': f8.check(r['sk'], a, r['answer'])['verdict'],
                     'v2r': f8v2.check(r['sk'], a, r['answer'])})
    for row in rows:
        row['v2'] = row['v2r']['verdict']
    return rows


def main():
    os.environ['PHASE1J_FINAL'] = '1'
    st_pass = f8v2.selftest()
    sides = {}
    sides['dev'] = build('dev', 'dev', False)
    sides['replay1j'] = build('replay1j', 'holdout1j', False)
    os.environ['PHASE1K_OPEN_FRESH'] = '1'
    RL.HYG = os.path.join(RL.TOFF, 'phase1l', 'hygiene')
    sides['fresh1l'] = build('fresh', 'fresh', True)

    tot = {'wrong_v1': 0, 'wrong_v2': 0, 'wrongV_v1': 0, 'wrongV_v2': 0,
           'cost_v1': 0, 'cost_v2': 0}
    lines = ['# Phase 1M - F8v2 (agent demotion) vs F8v1, offline replay',
             '',
             'Label `f8v2-build`. 0 model calls, 0 network, 0 DB. Judge labels are the stored ones',
             '(`dev` / `holdout1j` / `fresh`); `intent` is writer intent, never truth.',
             '',
             'F8v2 rule: a Slovak clause with a nominative agent must keep that agent as the subject',
             'of the aligned English clause. Reject on (1) passive clause, (2) it-/wh-cleft,',
             '(3) perspective recast, (4) generic/expletive subject. Everything else abstains.',
             '',
             '| side | items | labeled | judged wrong | v1 fired/wrong | v2 fired/wrong |'
             ' v1 fired/wrong intent V | v2 fired/wrong intent V | v1 COST | v2 COST |',
             '|---|---|---|---|---|---|---|---|---|---|']
    cost_rows = []
    for side, rows in sides.items():
        w = [r for r in rows if r['judged'] == 'wrong']
        c = [r for r in rows if r['judged'] == 'correct']
        wv = [r for r in w if r['intent'] == 'V']
        f = lambda rs, k: sum(1 for r in rs if r[k] == 'reject')
        tot['wrong_v1'] += f(w, 'v1'); tot['wrong_v2'] += f(w, 'v2')
        tot['wrongV_v1'] += f(wv, 'v1'); tot['wrongV_v2'] += f(wv, 'v2')
        tot['cost_v1'] += f(c, 'v1'); tot['cost_v2'] += f(c, 'v2')
        lines.append('| %s | %d | %d | %d | %d | %d | %d/%d | %d/%d | %d | %d |'
                     % (side, len(rows), sum(1 for r in rows if r['labeled']), len(w),
                        f(w, 'v1'), f(w, 'v2'), f(wv, 'v1'), len(wv), f(wv, 'v2'), len(wv),
                        f(c, 'v1'), f(c, 'v2')))
        for r in c:
            if r['v1'] == 'reject' or r['v2'] == 'reject':
                cost_rows.append((side, r))
    lines += ['| **total** | | | | %d | %d | %d | %d | **%d** | **%d** |'
              % (tot['wrong_v1'], tot['wrong_v2'], tot['wrongV_v1'], tot['wrongV_v2'],
                 tot['cost_v1'], tot['cost_v2']), '']

    lines += ['## Cost: guards firing on judged-CORRECT items', '']
    if not cost_rows:
        lines.append('None. Neither F8v1 nor F8v2 rejects any judged-correct item on the three sides.')
    for side, r in cost_rows:
        lines += ['* **%s %s** (v1=%s, v2=%s)' % (side, r['item_id'], r['v1'], r['v2']),
                  '  * SK: `%s`' % r['sk'],
                  '  * EN: `%s`' % r['answer'],
                  '  * reason: %s' % r['v2r'].get('reason', '')]
    lines.append('')

    lines += ['## The 8 Phase 1L voice false acceptances', '',
              '| sid | item | intent | type | v1 | v2 | answer |', '|---|---|---|---|---|---|---|']
    caught = 0
    for sid in EIGHT:
        rs = [r for r in sides['fresh1l'] if r['sid'] == sid and r['judged'] == 'wrong']
        hit = False
        for r in rs:
            lines.append('| %d | %s | %s | %s | %s | %s | %s |'
                         % (sid, r['item_id'].split(':')[-1], r['intent'], r['type'], r['v1'],
                            r['v2'], r['answer'].replace('|', '/')))
            if r['v2'] == 'reject' and r['v1'] != 'reject':
                hit = True
        if not rs:
            lines.append('| %d | (no judged-wrong item) | | | | | |' % sid)
        if hit:
            caught += 1
    lines += ['', 'Newly caught (v2 rejects, v1 did not): **%d / 8** sids.' % caught, '']

    lines += ['## Slovak clause readout on the 8 sids (`sk_clauses`)', '']
    for sid in EIGHT:
        rs = [r for r in sides['fresh1l'] if r['sid'] == sid]
        if not rs:
            continue
        lines.append('* **%d** `%s`' % (sid, rs[0]['sk']))
        for c in f8v2.sk_clauses(rs[0]['sk']):
            ag = c['agent']
            lines.append('  * [%d/%s] agent=%s - %s'
                         % (c['i'], c['role'], (ag['en'] or ag['tok']) if ag else 'None', c['reason']))
    lines += ['', 'selftest: %s (%d cases)' % ('PASS' if st_pass == 0 else 'FAIL', len(f8v2.CASES)), '']
    open(OUT, 'w').write('\n'.join(lines) + '\n')

    res = {'ok': True, 'selftest_pass': st_pass == 0, 'caught_of_8': caught,
           'cost_correct_v1': tot['cost_v1'], 'cost_correct_v2': tot['cost_v2'],
           'wrong_fired_v1': tot['wrong_v1'], 'wrong_fired_v2': tot['wrong_v2'],
           'wrongV_v1': tot['wrongV_v1'], 'wrongV_v2': tot['wrongV_v2']}
    print(json.dumps(res))
    json.dump(res, open(os.path.join(HERE, 'f8v2_eval.json'), 'w'), indent=1)


if __name__ == '__main__':
    main()

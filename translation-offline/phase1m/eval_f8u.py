#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phase 1M - F8v1 vs F8v2 vs F8u (union) on DEV / replay1j / fresh1l with the STORED judge
labels.  Same method as eval_f8v2.py.  ZERO model calls, zero network, zero DB."""
import datetime, json, os, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import loader_1l as L          # noqa: E402
import runner_1l as RL         # noqa: E402
import f8, f8v2, f8u           # noqa: E402

CALLER = 'f8-union'
PURPOSE = 'F8u union guard: offline replay of the stored judge labels (0 model calls)'
ACC = os.path.join(HERE, 'access_log.jsonl')
EIGHT = [140006, 140014, 140024, 140037, 140041, 140058, 140060, 140064]
FOUR = [140001, 140003, 140012, 140021]


def alog(side, what, n):
    with open(ACC, 'a') as f:
        f.write(json.dumps({'ts': datetime.datetime.now(datetime.timezone.utc)
                            .strftime('%Y-%m-%dT%H:%M:%SZ'), 'side': side, 'what': what,
                            'caller': CALLER, 'n': n, 'purpose': PURPOSE}, ensure_ascii=False) + '\n')


def build(side, label_src, hyg):
    st, recs, ann, by, info = RL.build_side(side, hyg, PURPOSE)
    alog(side, 'records+annotations (build_side)', len(recs))
    labels, _k, _v = RL.R1K.judge_labels(label_src, PURPOSE)
    alog(side, 'judge labels (%s)' % label_src, len(labels))
    rows = []
    for r in recs:
        jd = labels.get(r['item_id'])
        judged, wt = (jd if jd else (r.get('judged'), r.get('wrong_type')))
        a = ann.get(str(r['sid'])) or ann.get(r['sid']) or None
        rows.append({'item_id': r['item_id'], 'sid': r['sid'], 'sk': r['sk'], 'answer': r['answer'],
                     'intent': r.get('intent'), 'judged': judged, 'type': wt,
                     'v1': f8.check(r['sk'], a, r['answer'])['verdict'],
                     'v2': f8v2.check(r['sk'], a, r['answer'])['verdict'],
                     'ur': f8u.check(r['sk'], a, r['answer'])})
    for row in rows:
        row['u'] = row['ur']['verdict']
        row['src'] = row['ur'].get('f8_source')
    return rows


def main():
    os.environ['PHASE1J_FINAL'] = '1'
    st = f8u.selftest()
    sides = {}
    sides['dev'] = build('dev', 'dev', False)
    sides['replay1j'] = build('replay1j', 'holdout1j', False)
    os.environ['PHASE1K_OPEN_FRESH'] = '1'
    RL.HYG = os.path.join(RL.TOFF, 'phase1l', 'hygiene')
    sides['fresh1l'] = build('fresh', 'fresh', True)

    print('\n| side | items | judged wrong | v1 fired | v2 fired | u fired | v1 COST | v2 COST | u COST |')
    print('|---|---|---|---|---|---|---|---|---|')
    tot = {k: 0 for k in ('w1', 'w2', 'wu', 'c1', 'c2', 'cu')}
    cost = []
    for side, rows in sides.items():
        w = [r for r in rows if r['judged'] == 'wrong']
        c = [r for r in rows if r['judged'] == 'correct']
        f = lambda rs, k: sum(1 for r in rs if r[k] == 'reject')
        tot['w1'] += f(w, 'v1'); tot['w2'] += f(w, 'v2'); tot['wu'] += f(w, 'u')
        tot['c1'] += f(c, 'v1'); tot['c2'] += f(c, 'v2'); tot['cu'] += f(c, 'u')
        print('| %s | %d | %d | %d | %d | %d | %d | %d | %d |'
              % (side, len(rows), len(w), f(w, 'v1'), f(w, 'v2'), f(w, 'u'),
                 f(c, 'v1'), f(c, 'v2'), f(c, 'u')))
        for r in c:
            if 'reject' in (r['v1'], r['v2'], r['u']):
                cost.append((side, r))
    print('| **total** | | | %d | %d | %d | **%d** | **%d** | **%d** |'
          % (tot['w1'], tot['w2'], tot['wu'], tot['c1'], tot['c2'], tot['cu']))

    print('\n## Cost: guards firing on judged-CORRECT items')
    if not cost:
        print('None on any of the three sides.')
    for side, r in cost:
        print('* **%s %s** (v1=%s, v2=%s, u=%s via %s)' % (side, r['item_id'], r['v1'], r['v2'],
                                                           r['u'], r['src']))
        print('  * SK: `%s`' % r['sk'])
        print('  * EN: `%s`' % r['answer'])
        print('  * reason: %s' % r['ur'].get('reason', ''))

    for name, ids in (('The 8 named FRESH1L voice false acceptances', EIGHT),
                      ('The 4 items F8v2 alone lost', FOUR)):
        print('\n## %s' % name)
        print('| sid | item | intent | type | judged | v1 | v2 | u | u source | answer |')
        print('|---|---|---|---|---|---|---|---|---|---|')
        for sid in ids:
            rs = [r for r in sides['fresh1l'] if r['sid'] == sid and r['judged'] == 'wrong']
            if not rs:
                print('| %d | (no judged-wrong item) | | | | | | | | |' % sid)
            for r in rs:
                print('| %d | %s | %s | %s | %s | %s | %s | %s | %s | %s |'
                      % (sid, r['item_id'].split(':')[-1], r['intent'], r['type'], r['judged'],
                         r['v1'], r['v2'], r['u'], r['src'], r['answer'].replace('|', '/')))
        print('caught by u: %d / %d sids'
              % (sum(1 for sid in ids if any(r['u'] == 'reject' for r in sides['fresh1l']
                                             if r['sid'] == sid and r['judged'] == 'wrong')), len(ids)))
    res = {'selftest_pass': st == 0, 'cost_v1': tot['c1'], 'cost_v2': tot['c2'], 'cost_u': tot['cu'],
           'wrong_v1': tot['w1'], 'wrong_v2': tot['w2'], 'wrong_u': tot['wu']}
    json.dump(res, open(os.path.join(HERE, 'f8u_eval.json'), 'w'), indent=1)
    print('\nJSON: ' + json.dumps(res))


if __name__ == '__main__':
    main()

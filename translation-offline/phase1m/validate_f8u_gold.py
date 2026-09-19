#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phase 1M - the F8v1 Slovak side (f8.sk_agent) and the F8u UNION validated against the SAME
blind hand gold as F8v2 (phase1m/f8gold), with the SAME AGREE / CONSERVATIVE / ERROR definitions
and the same harness (validate_f8v2.py is imported, not re-implemented).

0 model calls, 0 network, 0 DB, no annotation read.  Reads only existing_210.json (Slovak) and
f8gold/gold_part{1,2}.json; both reads are logged in access_log.jsonl.

f8.sk_agent() is SENTENCE-level: it returns at most ONE agent for the whole sentence.  It is
therefore scored as a ONE-clause readout.  When the gold has one clause the equal-length branch
of validate_f8v2.py applies verbatim; when the gold has several clauses the clause split differs
and validate_f8v2.py's split-mismatch branch applies verbatim (an asserted agent must match SOME
gold agent of the sentence, otherwise ERROR; matching one makes the row CONSERVATIVE).
`agent_nom` False ("passive"/"impersonal") asserts no agent and can never make f8.check() reject,
so it is scored as an abstention, exactly like an F8v2 clause with agent None.

UNION: ERROR if either readout errs; else AGREE if either readout agrees; else CONSERVATIVE.
"""
import datetime, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.dont_write_bytecode = True
import f8, f8v2                      # noqa: E402
import validate_f8v2 as V            # noqa: E402  (cp / same / g_val / s_val / show_g / show_s)

ACCESS = os.path.join(HERE, 'access_log.jsonl')


def alog(side, what, n, purpose):
    with open(ACCESS, 'a', encoding='utf-8') as fh:
        fh.write(json.dumps({'ts': datetime.datetime.now(datetime.timezone.utc)
                             .strftime('%Y-%m-%dT%H:%M:%SZ'), 'side': side, 'what': what,
                             'caller': 'f8-union', 'n': n, 'purpose': purpose},
                            ensure_ascii=False) + '\n')


def v1_assert(sk):
    r = f8.sk_agent(sk, None)
    if not r.get('agent_nom'):
        return None, r
    ag = (r.get('agent') or '')
    if ag in f8.PRON:
        return ('P', f8.PRON[ag][0]), r
    return ('N', ag.lower()), r


def classify(sv, gv, gc, show):
    errs, cons = [], False
    if len(sv) == len(gv):
        for k, (a, b) in enumerate(zip(sv, gv)):
            if a is None and b is None:
                continue
            if a is None:
                cons = True; continue
            if b is None:
                errs.append('clause %d: asserts %s, gold has NO agent (%s)'
                            % (k, show(k), gc[k].get('no_agent_reason')))
            elif not V.same(a, b):
                errs.append('clause %d: asserts %s vs gold %s'
                            % (k, show(k), V.show_g(gc[k].get('agent'))))
    else:
        pool = [x for x in gv if x is not None]
        for k, a in enumerate(sv):
            if a is None:
                continue
            hit = next((j for j, b in enumerate(pool) if V.same(a, b)), None)
            if hit is None:
                errs.append('clause %d (split mismatch): asserts %s, no gold clause of the '
                            'sentence has it' % (k, show(k)))
            else:
                pool.pop(hit)
        cons = True
    cls = 'ERROR' if errs else ('AGREE' if not cons else 'CONSERVATIVE')
    return cls, errs


def main():
    sents = json.load(open(os.path.join(HERE, 'existing_210.json'), encoding='utf-8'))
    alog('dev+holdout1j+fresh1k', 'existing_210.json (Slovak/side only)', len(sents),
         'F8v1 sk_agent + F8u union validation against the blind hand gold')
    gold = []
    for p in ('gold_part1.json', 'gold_part2.json'):
        g = json.load(open(os.path.join(HERE, 'f8gold', p), encoding='utf-8'))
        alog('dev+holdout1j+fresh1k', 'f8gold/' + p, len(g),
             'blind hand gold: Slovak clause agents, F8v1/F8u validation')
        gold += g
    G = {g['sid']: g for g in gold}
    assert set(G) == {s['sid'] for s in sents}

    rows = []
    for s in sents:
        sid, sk, g = s['sid'], s['slovak'], G[s['sid']]
        gc = g['clauses']
        gv = [V.g_val(c.get('agent')) for c in gc]
        a1, r1 = v1_assert(sk)
        sv1 = [a1]
        sc2 = f8v2.sk_clauses(sk, None)
        sv2 = [V.s_val(c['agent']) for c in sc2]
        show1 = lambda k: ('ABSTAIN' if a1 is None else '%s=%s' % ('pron' if a1[0] == 'P' else 'noun', a1[1]))
        show2 = lambda k: V.show_s(sc2[k]['agent'])
        c1, e1 = classify(sv1, gv, gc, show1)
        c2, e2 = classify(sv2, gv, gc, show2)
        cu = 'ERROR' if (e1 or e2) else ('AGREE' if 'AGREE' in (c1, c2) else 'CONSERVATIVE')
        rows.append({'sid': sid, 'side': s['side'], 'sk': sk, 'v1': c1, 'v2': c2, 'union': cu,
                     'e1': e1, 'e2': e2, 'v1_reason': r1.get('reason'),
                     'v1_voice': r1.get('voice_sk'), 'v1_agent': r1.get('agent'),
                     'gold': ['[%d/%s] %s%s' % (c['i'], c.get('role'), V.show_g(c.get('agent')),
                                                '' if c.get('agent') else
                                                ' (%s)' % c.get('no_agent_reason')) for c in gc]})

    tbl = {}
    for key in ('v1', 'v2', 'union'):
        print('\n### %s' % {'v1': 'F8v1 (f8.sk_agent, sentence-level)',
                            'v2': 'F8v2 (sk_clauses, re-measured here)',
                            'union': 'F8u UNION'}[key])
        print('| side | n | agree | conservative | error | error rate | CP 95 % |')
        print('|---|---|---|---|---|---|---|')
        for name, sk_ in (('DEV', 'dev'), ('HOLDOUT', 'holdout'), ('FRESH1K', 'fresh1k'), ('ALL', None)):
            rs = rows if sk_ is None else [r for r in rows if r['side'] == sk_]
            n = len(rs)
            a = sum(1 for r in rs if r[key] == 'AGREE')
            c = sum(1 for r in rs if r[key] == 'CONSERVATIVE')
            e = sum(1 for r in rs if r[key] == 'ERROR')
            lo, hi = V.cp(e, n)
            tbl['%s/%s' % (key, name)] = {'n': n, 'agree': a, 'cons': c, 'err': e,
                                          'rate': round(100.0 * e / n, 2) if n else 0.0,
                                          'ci': [lo, hi]}
            print('| %s | %d | %d | %d | %d | %.2f %% | [%.2f, %.2f] |'
                  % (name, n, a, c, e, 100.0 * e / n if n else 0.0, lo, hi))

    print('\n## Every UNION error (%d)' % sum(1 for r in rows if r['union'] == 'ERROR'))
    for r in rows:
        if r['union'] != 'ERROR':
            continue
        print('\n- **%s** (%s) `%s`' % (r['sid'], r['side'], r['sk']))
        for e in r['e1']:
            print('    ! F8v1 %s' % e)
        for e in r['e2']:
            print('    ! F8v2 %s' % e)
        print('    v1 readout: agent=%s voice=%s - %s' % (r['v1_agent'], r['v1_voice'], r['v1_reason']))
        for x in r['gold']:
            print('    gold   ' + x)
    json.dump({'table': tbl, 'rows': rows}, open(os.path.join(HERE, 'f8u_validation.json'), 'w'),
              ensure_ascii=False, indent=1)
    print('\nJSON: {"v1_gold_errors": %d, "v2_gold_errors": %d, "union_gold_errors": %d, "n": %d}'
          % (sum(1 for r in rows if r['v1'] == 'ERROR'), sum(1 for r in rows if r['v2'] == 'ERROR'),
             sum(1 for r in rows if r['union'] == 'ERROR'), len(rows)))


if __name__ == '__main__':
    main()

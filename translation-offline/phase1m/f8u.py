#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""F8u - the UNION guard: F8v2 (agent demotion) OR F8v1 (plain be+PP+by passive).

100% OFFLINE: no model, no API, no network, no DB.  Same public interface as f8 / f8v2, so the
runner can swap the module by name:

    check(slovak, annotation, answer) -> {"verdict": reject|accept|abstain, "sk":…, "en":…, "reason":…}
    sk_agent(slovak, annotation=None)      (re-exported from f8)
    en_passive(answer)                     (re-exported from f8)
    sk_clauses(slovak, annotation=None)    (re-exported from f8v2)
    en_clauses(answer)                     (re-exported from f8v2)

WHY.  The zero-call TIP readout (phase1m/TIP_READOUT.md, finding a) showed that F8v2 is NOT a
superset of F8v1 on the closed 1L fresh set: it catches the 8 known agent-demotion false
acceptances, but it LOSES four plain `be + PP + by`-passives that F8v1 rejected
(W:140001…, W:140003…, W:140012…, W:140021…), because the gold-validation fixes made
`f8v2.sk_clauses()` abstain on their Slovak side (clause-initial common-noun subjects are no
longer asserted, only mid-clause proper names).  The brief defines F8v2 as agent demotion
INCLUDING the passive, so the plain passive must not fall out of the guard.

RULE (the whole module):

    reject  if F8v2 rejects            -> the F8v2 rejection is returned unchanged
    else reject if F8v1 rejects        -> the F8v1 rejection is returned, marked source "f8v1"
    else                               -> the F8v2 pass/abstain result, unchanged

Nothing is loosened: F8u rejects a strict superset of what F8v2 rejects, and of what F8v1
rejects.  The cost of the union is therefore exactly the union of the two costs; it is measured
in F8_UNION_DECISION.md before the module is allowed anywhere near the new set.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import f8    # noqa: E402
import f8v2  # noqa: E402

# re-exports (identical objects, so callers that reach past check() behave as before)
sk_agent = f8.sk_agent
en_passive = f8.en_passive
sk_clauses = f8v2.sk_clauses
en_clauses = f8v2.en_clauses


def check(slovak, annotation, answer):
    r2 = f8v2.check(slovak, annotation, answer)
    if r2.get('verdict') == 'reject':
        r2['f8_source'] = 'f8v2'
        return r2
    r1 = f8.check(slovak, annotation, answer)
    if r1.get('verdict') == 'reject':
        out = dict(r2)
        out['f8_source'] = 'f8v1'
        out['v1'] = r1
        out['v2_verdict'] = r2.get('verdict')
        out['v2_reason'] = r2.get('reason')
        out.update(verdict='reject', reason='F8v1: ' + (r1.get('reason') or ''))
        return out
    r2['f8_source'] = 'f8v2'
    r2['v1_verdict'] = r1.get('verdict')
    return r2


# --------------------------------------------------------------------------- selftest
# every F8v2 case must still hold (the union may only turn accept/abstain into reject, and no
# F8v2 case may do so), plus plain by-passives of the kind F8v2 alone loses.
EXTRA = [
    # the four FRESH1L items F8v2 alone stopped rejecting (plain be + PP + by, explicit agent)
    ("Ona každé ráno pije zelený čaj s medom.",
     "Green tea with honey is drunk by her every morning.", {'reject'}),
    ("Moja sestra nosí okuliare iba pri čítaní.",
     "Glasses are worn by my sister only when she reads.", {'reject'}),
    ("Sused, ktorý býva nad nami, opravuje bicykle v garáži.",
     "Bicycles are repaired in the garage by the neighbour who lives above us.", {'reject'}),
    ("Moja babka nám každú nedeľu piekla jablkový koláč.",
     "An apple cake was baked for us every Sunday by my grandma.", {'reject'}),
    # a textbook by-passive with a pronoun agent
    ("Peter napísal ten list.", "That letter was written by Peter.", {'reject'}),
    # and the faithful actives of the same sentences must still pass
    ("Ona každé ráno pije zelený čaj s medom.",
     "She drinks green tea with honey every morning.", {'accept', 'abstain'}),
    ("Moja babka nám každú nedeľu piekla jablkový koláč.",
     "My grandma baked us an apple cake every Sunday.", {'accept', 'abstain'}),
]
CASES = list(f8v2.CASES) + EXTRA


def selftest(verbose=True):
    bad = []
    for sk, en, ok in CASES:
        r = check(sk, None, en)
        if r['verdict'] not in ok:
            bad.append((sk, en, r['verdict'], sorted(ok), r['reason']))
    print('F8u selftest: %d cases (%d inherited from F8v2, %d new), %d failures'
          % (len(CASES), len(f8v2.CASES), len(EXTRA), len(bad)))
    if verbose:
        for b in bad:
            print('  FAIL %-46s | %-46s -> %-8s want %s\n        %s'
                  % (b[0][:46], b[1][:46], b[2], b[3], b[4]))
    return 1 if bad else 0


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        sys.exit(selftest())
    for s in sys.argv[1:]:
        print(s, sk_agent(s))

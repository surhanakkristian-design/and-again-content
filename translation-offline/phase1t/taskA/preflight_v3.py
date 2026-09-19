#!/usr/bin/env python3
"""Phase 1T Task A - pre-flight for AG v3.  Synthetic rows only, 0 model calls.
v2's 13 rows (they must still pass, unchanged) + 8 new rows for the three v3 fixes."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import agent_drop_v3 as V3                                                     # noqa: E402
from agent_drop_v3 import V2                                                   # noqa: E402

ACT = {'voice_sk': 'active_agent', 'agent_nom': True}

NEW = [
    # name, sk, ann, wtags, answer, reference, expect_primary, expect_noun
    ('NEW embedded-clause agent drop', 'Šéf povedal, že tím pripravil tú správu.',
     ACT, {'nom_agent': True, 'agent': 'tím'},
     'The boss said that the report had been prepared.',
     'The boss said that the team had prepared the report.', True, True),
    ('NEW embedded clause, agent kept with by', 'Šéf povedal, že tím pripravil tú správu.',
     ACT, {'nom_agent': True, 'agent': 'tím'},
     'The boss said that the report had been prepared by the team.',
     'The boss said that the team had prepared the report.', False, False),
    ('NEW passive over a subjectless SK clause (agent lives in the other clause)',
     'Odkedy zaviedli nový systém, zamestnanci hlásia oveľa menej chýb.',
     {'voice_sk': 'active_agent', 'agent_nom': True}, {'nom_agent': True, 'agent': 'zamestnanci'},
     'Since the new system was introduced, employees report far fewer errors.',
     'Since they introduced the new system, the employees report far fewer errors.', False, False),
    ('NEW "by bike" is no by-agent', 'Ja zajtra odveziem tie knihy do knižnice na bicykli.',
     ACT, {'nom_agent': True, 'agent': 'ja'},
     'Tomorrow those books will be taken to the library by bike.',
     'Tomorrow I will take those books to the library by bike.', True, False),
    ('NEW proper-name agent', 'Jana vypila celý pohár mlieka.',
     ACT, {'nom_agent': True, 'agent': 'Jana'},
     'A whole glass of milk was drunk.', 'Jana drank a whole glass of milk.', True, True),
    ('NEW pronoun agent in a ze-clause', 'Otec mi povedal, že on zamkol garáž ešte pred obedom.',
     ACT, {'nom_agent': True, 'agent': 'on (otec)'},
     'My father told me that the garage had been locked before lunch.',
     'Father told me that he had locked the garage before lunch.', True, False),
    ('NEW by-passive control (proper name)', 'Jana vypila celý pohár mlieka.',
     ACT, {'nom_agent': True, 'agent': 'Jana'},
     'A whole glass of milk was drunk by Jana.', 'Jana drank a whole glass of milk.', False, False),
    ('NEW plain active control', 'Marek každý večer zamyká bránu do záhrady.',
     ACT, {'nom_agent': True, 'agent': 'Marek'},
     'Marek locks the garden gate every evening.',
     'Marek locks the garden gate every evening.', False, False),
]

ROWS = list(V2.SYN) + NEW


def main(verbose=True):
    lines, ok = [], True
    for name, sk, ann, wt, ans, ref, ep, en in ROWS:
        p = V3.decide(sk, ann, wt, ans, ref, 'primary')['fired']
        n = V3.decide(sk, ann, wt, ans, ref, 'noun')['fired']
        good = (p == ep and n == en)
        ok = ok and good
        lines.append('%-4s %-62s primary=%-5s (want %-5s)  noun=%-5s (want %-5s)'
                     % ('PASS' if good else 'FAIL', name, p, ep, n, en))
    # flags OFF must reproduce v2 bit for bit on every row
    same = all(V3.decide(r[1], r[2], r[3], r[4], r[5], v, flags=())['fired']
               == V2.decide(r[1], r[2], r[3], r[4], r[5], v)['fired']
               for r in ROWS for v in ('primary', 'noun'))
    lines.append('%-4s flags=() reproduces AG v2 on all %d rows' % ('PASS' if same else 'FAIL', len(ROWS)))
    ok = ok and same
    if verbose:
        print('\n'.join(lines))
        print('PRE-FLIGHT %s: %d/%d rows' % ('PASS' if ok else 'FAIL',
                                             sum(1 for x in lines if x.startswith('PASS')), len(lines)))
    return ok, lines


if __name__ == '__main__':
    sys.exit(0 if main()[0] else 1)

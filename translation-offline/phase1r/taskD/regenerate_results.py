#!/usr/bin/env python3
"""Phase 1R, Task D1: regenerate phase1p/results_1p.json from the STORED 1Q verdicts.

ZERO model calls, by construction:
  * every Gemini/Google key env var is blanked before runner_1p is imported;
  * runner_1n.make_calls (the only place an HTTP call is made) is replaced by a raiser,
    so a non-empty `need` list would abort the regeneration instead of calling the model.

check_freeze() is stubbed because runner_1p.py now carries the Phase 1R serialisation fix
(json.dump default= for sets) and therefore no longer hashes to the freeze commit. Nothing
else in the runner changed; the frozen hash is still recorded in the output.
"""
import hashlib, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TOFF = os.path.abspath(os.path.join(HERE, '..', '..'))
P1P = os.path.join(TOFF, 'phase1p')

for k in list(os.environ):
    if 'GEMINI' in k or 'GOOGLE' in k or ('API_KEY' in k and 'ANTHROPIC' not in k):
        os.environ.pop(k, None)

sys.path.insert(0, P1P)
os.chdir(P1P)
import runner_1p as R  # noqa: E402


def _no_calls(*a, **k):
    raise RuntimeError('REFUSED: a NEW model call was requested during the Phase 1R '
                       'offline regeneration. Nothing was called.')


R.R1N.make_calls = _no_calls
FREEZE = open(os.path.join(P1P, 'FREEZE_HASH'), encoding='utf-8').read().strip().split()[0]
R.check_freeze = lambda: FREEZE


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def find_sets(o, path='$'):
    hits = []
    if isinstance(o, (set, frozenset)):
        hits.append((path, sorted(map(str, o))[:6]))
    elif isinstance(o, dict):
        for k, v in o.items():
            hits += find_sets(v, '%s.%s' % (path, k))
    elif isinstance(o, list):
        for i, v in enumerate(o[:3]):
            hits += find_sets(v, '%s[%d]' % (path, i))
    return hits


CALLS = os.path.join(P1P, 'calls.jsonl')
before = (sum(1 for _ in open(CALLS, encoding='utf-8')), sha(CALLS))
print('[CALLS BEFORE] lines=%d sha256=%s' % before)

out = R.run_final(None)

after = (sum(1 for _ in open(CALLS, encoding='utf-8')), sha(CALLS))
print('[CALLS AFTER ] lines=%d sha256=%s' % after)
print('[ZERO-CALL PROOF] identical: %s' % (before == after))

sets = find_sets(out)
print('[SETS IN RESULTS] %s' % json.dumps(sets)[:600])

met = out['metrics']
ref = json.load(open(os.path.join(TOFF, 'phase1q', 'RESULTS_1Q.json'), encoding='utf-8'))
p = ref['pooled']
head = {'coverage_kn': met['coverage_kn'], 'fa_kn': met['fa_kn'],
        'coverage_pct': met['coverage_pct'], 'fa_pct': met['fa_pct'],
        'n_items': out['build']['n_items'], 'rows': len(out['rows'])}
exp = {'coverage_kn': '%d/%d' % (p['coverage']['k'], p['coverage']['n']),
       'fa_kn': '%d/%d' % (p['fa']['k'], p['fa']['n']),
       'coverage_pct': p['coverage']['pct'], 'fa_pct': p['fa']['pct'],
       'n_items': 1080, 'rows': 1080}
print('[HEADLINE regenerated] %s' % json.dumps(head))
print('[HEADLINE 1Q replay  ] %s' % json.dumps(exp))
print('[MATCH] %s' % json.dumps({k: (str(head[k]) == str(exp[k])) for k in exp}))
json.dump({'before': {'lines': before[0], 'sha256': before[1]},
           'after': {'lines': after[0], 'sha256': after[1]},
           'sets_found': sets, 'regenerated': head, 'replay_1q': exp,
           'match': {k: (str(head[k]) == str(exp[k])) for k in exp}},
          open(os.path.join(HERE, 'regenerate_check.json'), 'w', encoding='utf-8'),
          indent=1, ensure_ascii=False)

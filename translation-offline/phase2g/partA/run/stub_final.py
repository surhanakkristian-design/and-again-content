#!/usr/bin/env python3
"""Phase 2F PART 3.1 - 0-call stub of the final run, for the preflight selftest ONLY.
Same code path as --final (final_core), with a stub L3 in place of the transport and checks off:
it proves the set, the loader, the layers, the stack patch, the rows and the scorer all work
before a single model call is made.  Never used by --run."""
import json, os, random, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import runner_1u as RU                                                         # noqa: E402

DATA = sys.argv[sys.argv.index('--data-dir') + 1]


def stub(req, need):
    rng = random.Random(4242)
    with open(RU.CALLS, 'a', encoding='utf-8') as fh:
        for h in need:
            v = rng.choice(['SAME', 'SAME', 'SAME', 'DIFF', 'TIP'])
            fh.write(json.dumps({'ts': 'stub', 'http': 200, 'req_hash': h, 'verdict': v,
                                 'item_id': None, 'reply': v, 'prompt_tokens': 11,
                                 'candidates_tokens': 2, 'latency_ms': 1}) + chr(10))
    return {'ok': len(need), 'bad': 0, 'empty': 0, 'skipped': 0, 'wall': False}


fl = RU.check_floors_1u()
print('[STUB] floors gate exercised:', json.dumps(fl, sort_keys=True))
out = RU.final_core(HERE, DATA, call_fn=stub, checks=False)
print('[STUB] status', out.get('status'), 'headline', json.dumps(out.get('headline')))

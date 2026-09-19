#!/usr/bin/env python3
"""Phase 1L loader = the Phase 1k loader with its log redirected to phase1l/access_log.jsonl.

phase1k/ is read-only in Phase 1L, so loader_1k._log is neutered exactly the way loader_1k
neutered loader_1j._log. Every read of DEV or FRESH data made through this module is logged
here instead (same {ts, side, what, caller, n, purpose} format). Nothing in phase1k is edited.
"""
import datetime, json, os, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
K = os.path.join(os.path.dirname(HERE), 'phase1k')
if K not in sys.path:
    sys.path.insert(0, K)
import loader_1k as _K                                                     # noqa: E402
LOG = os.path.join(HERE, 'access_log.jsonl')


def _log(side, what, n, purpose, caller=None):
    rec = {'ts': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
           'side': side, 'what': what,
           'caller': caller or os.path.basename(sys.argv[0] or 'interactive'),
           'n': n, 'purpose': purpose or ''}
    with open(LOG, 'a', encoding='utf-8') as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + '\n')
    return rec


_K._log = _log
for _n in dir(_K):
    if _n.startswith('load_'):
        globals()[_n] = getattr(_K, _n)

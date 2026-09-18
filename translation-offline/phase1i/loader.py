#!/usr/bin/env python3
"""Phase 1i — the ONLY sanctioned way to read the split data. Every load is logged.

    from loader import load_items
    items = load_items("dev")          # always allowed
    items = load_items("holdout")      # raises unless PHASE1I_TASK_F=1 and no phase1i/HOLDOUT_RUN_DONE

`load_items(side)` returns a list of dicts, one per item, exactly the lines of
`phase1i/<side>/items.jsonl` (schema: phase1i/CONTEXT.md §2). Never read those files directly, and never
read `phase1i/holdout/` by any other means: the holdout is measured ONCE, by Task F, and the access log is
the evidence. `phase1i/holdout/` is chmod a-w (readable, not writable).
"""
import datetime
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, 'access_log.jsonl')
DONE = os.path.join(HERE, 'HOLDOUT_RUN_DONE')


def _caller():
    for f in sys._current_frames().values():
        pass
    try:
        import inspect
        for fr in inspect.stack()[1:]:
            fn = os.path.basename(fr.filename)
            if fn not in ('loader.py', '<stdin>'):
                return fn
    except Exception:
        pass
    return os.path.basename(sys.argv[0] or 'interactive')


def _log(side, n):
    rec = {'ts': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
           'side': side, 'caller': _caller(), 'n_items': n}
    with open(LOG, 'a', encoding='utf-8') as fh:
        fh.write(json.dumps(rec) + '\n')


def load_items(side):
    side = str(side).lower()
    if side not in ('dev', 'holdout'):
        raise ValueError('side must be "dev" or "holdout"')
    if side == 'holdout':
        if os.environ.get('PHASE1I_TASK_F') != '1':
            raise PermissionError('HOLDOUT is locked: set PHASE1I_TASK_F=1 only in the single Task F run')
        if os.path.exists(DONE):
            raise PermissionError('HOLDOUT already measured once (phase1i/HOLDOUT_RUN_DONE exists); '
                                  'a second measurement is not a holdout measurement')
    p = os.path.join(HERE, side, 'items.jsonl')
    out = [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]
    _log(side, len(out))
    return out


def load_annotations(side):
    """The sid -> {hygienised, raw} annotation map of one side. Same guard, same log."""
    side = str(side).lower()
    if side == 'holdout':
        load_items('holdout')          # runs the guard and logs; cheap enough
    p = os.path.join(HERE, side, 'annotations.json')
    a = json.load(open(p, encoding='utf-8'))
    _log(side + ':annotations', len(a))
    return a


if __name__ == '__main__':
    print(len(load_items(sys.argv[1] if len(sys.argv) > 1 else 'dev')))

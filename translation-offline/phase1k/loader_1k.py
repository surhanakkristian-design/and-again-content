#!/usr/bin/env python3
"""Phase 1k — the ONLY sanctioned way to read data in this phase. Every read is logged.

    import sys, os
    sys.path.insert(0, os.path.expanduser(
        '~/Projects/and-again-content/translation-offline/phase1k'))
    from loader_1k import load_dev_items, load_fresh_sentences

Sides
-----
`1j:dev`      the 490 Phase 1j DEV items / 70 sentences / annotations — always readable.
`1j:holdout`  the 490 Phase 1j HOLDOUT items (Phase 1j is CLOSED, `FINAL_RUN_DONE` exists;
              in Phase 1k they are a *labelled replay* set) — always readable here.
`1k:fresh`    the 70 NEW sentences of Phase 1k.
              * sentences / writer input (answer-free) — always readable.
              * writer output, items, judge key, judge labels (they contain or reveal answers)
                raise PermissionError unless `PHASE1K_OPEN_FRESH=1`.

Arm B
-----
Phase 1j arm B rewrote the Slovak with an explicit subject pronoun and dropped the `g` chain.
`load_dev_items(arm_b=True)` (the default) replaces `sk`, `reference` and `refs` with the arm-B
values from `phase1j/taskB/rewrites.jsonl`; `load_dev_annotations()` returns
`taskB/annotations_b_<side>.json` (g removed on rewritten sids).

$J is read-only (chmod a-w). Therefore this loader NEVER writes there: it delegates to
`loader_1j` with its `_log` neutered and records the read in `phase1k/access_log.jsonl`
instead — one JSON line per read: {ts, side, what, caller, n, purpose} (1j format).
"""
import datetime
import json
import os
import sys

sys.dont_write_bytecode = True  # $J is read-only: never try to drop a __pycache__ there

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
P1J = os.path.join(ROOT, 'phase1j')
LOG = os.path.join(HERE, 'access_log.jsonl')
FRESH = os.path.join(HERE, 'fresh')
JUDGE = os.path.join(HERE, 'judge')

if P1J not in sys.path:
    sys.path.insert(0, P1J)
import loader_1j as _L1J  # noqa: E402

_L1J._log = lambda *a, **k: None  # $J/access_log.jsonl is read-only; we log into $K


def _caller():
    try:
        import inspect
        for fr in inspect.stack()[1:]:
            fn = os.path.basename(fr.filename)
            if fn not in ('loader_1k.py', 'loader_1j.py', '<stdin>', '<string>'):
                return fn
    except Exception:
        pass
    return os.path.basename(sys.argv[0] or 'interactive')


def _log(side, what, n, purpose, caller=None):
    rec = {'ts': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
           'side': side, 'what': what, 'caller': caller or _caller(), 'n': n,
           'purpose': purpose or ''}
    with open(LOG, 'a', encoding='utf-8') as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + '\n')
    return rec


def _jsonl(path):
    return [json.loads(l) for l in open(path, encoding='utf-8') if l.strip()]


def _fresh_guard(what):
    if os.environ.get('PHASE1K_OPEN_FRESH') != '1':
        raise PermissionError(
            'FRESH %s is locked: it contains (or reveals) learner answers. Set '
            'PHASE1K_OPEN_FRESH=1 only for the judge-input build and the ONE final run, and say '
            'so in `purpose`.' % what)


# ---------------------------------------------------------------- arm B (Phase 1j)
_RW = None


def _rewrites():
    """sid -> {'sk': arm-B Slovak, 'refs': arm-B references, 'rewritten': bool}"""
    global _RW
    if _RW is None:
        _RW = {}
        for r in _jsonl(os.path.join(P1J, 'taskB', 'rewrites.jsonl')):
            _RW[int(r['sid'])] = {'sk': r['new_sk'], 'refs': list(r['refs_new']),
                                  'rewritten': r['status'] == 'rewritten'}
    return dict(_RW)


def _apply_arm_b(recs):
    rw = _rewrites()
    out = []
    for r in recs:
        r = dict(r)
        b = rw.get(int(r['sid']))
        if b:
            r['sk'] = b['sk']
            r['refs'] = list(b['refs'])
            if 'reference' in r:
                r['reference'] = b['refs'][0]
            r['arm_b_rewritten'] = b['rewritten']
        out.append(r)
    return out


def _items(side, purpose, arm_b):
    if side == 'holdout':
        # Phase 1j is closed (FINAL_RUN_DONE); its holdout is a labelled replay set in 1k.
        old = os.environ.get('PHASE1J_FINAL')
        os.environ['PHASE1J_FINAL'] = '1'
        try:
            recs = _L1J.load_items('holdout')
        finally:
            if old is None:
                os.environ.pop('PHASE1J_FINAL', None)
            else:
                os.environ['PHASE1J_FINAL'] = old
    else:
        recs = _L1J.load_items('dev')
    if arm_b:
        recs = _apply_arm_b(recs)
    _log('1j:%s' % side, 'items', len(recs), purpose)
    return recs


def _annotations(side, purpose, arm_b):
    p = os.path.join(P1J, 'taskB', 'annotations_b_%s.json' % side) if arm_b else \
        os.path.join(P1J, side, 'annotations.json')
    a = json.load(open(p, encoding='utf-8'))
    _log('1j:%s' % side, 'annotations', len(a), purpose)
    return a


def _sentences(side, purpose, arm_b):
    recs = [r for r in _jsonl(os.path.join(P1J, 'sentences_all.jsonl')) if r['side'] == side]
    if arm_b:
        recs = _apply_arm_b(recs)
        for r in recs:
            r['annotation_v'] = list(r['refs'])
            if r.get('arm_b_rewritten'):
                r['g'] = None
                r['g_raw'] = None
    _log('1j:%s' % side, 'sentences', len(recs), purpose)
    return recs


def load_dev_items(purpose='', arm_b=True):
    """The 490 Phase 1j DEV items (schema: phase1j/CONTEXT_1J.md §2), arm-B Slovak by default."""
    return _items('dev', purpose, arm_b)


def load_dev_annotations(purpose='', arm_b=True):
    return _annotations('dev', purpose, arm_b)


def load_dev_sentences(purpose='', arm_b=True):
    return _sentences('dev', purpose, arm_b)


def load_holdout1j_items(purpose='', arm_b=True):
    """The 490 Phase 1j HOLDOUT items — labelled replay set for Phase 1k."""
    return _items('holdout', purpose, arm_b)


def load_holdout1j_annotations(purpose='', arm_b=True):
    return _annotations('holdout', purpose, arm_b)


def load_holdout1j_sentences(purpose='', arm_b=True):
    return _sentences('holdout', purpose, arm_b)


def load_armb_map(purpose=''):
    rw = _rewrites()
    _log('1j:both', 'armb_map', len(rw), purpose)
    return rw


# ---------------------------------------------------------------- Phase 1k fresh
def load_fresh_sentences(purpose='', path=None):
    """The 70 NEW Slovak sentences + references + annotations. Answer-free: always readable."""
    recs = _jsonl(path or os.path.join(FRESH, 'sentences_fresh.jsonl'))
    _log('1k:fresh', 'sentences', len(recs), purpose)
    return recs


def load_fresh_annotations(purpose='', path=None):
    a = json.load(open(path or os.path.join(FRESH, 'annotations_fresh.json'), encoding='utf-8'))
    _log('1k:fresh', 'annotations', len(a), purpose)
    return a


def load_fresh_writer_input(purpose='', path=None):
    """{wid, slovak, level, topic} only — what the answer writer is allowed to see."""
    recs = _jsonl(path or os.path.join(FRESH, 'writer_input.jsonl'))
    _log('1k:fresh', 'writer_input', len(recs), purpose)
    return recs


def load_fresh_writer_output(purpose='', path=None):
    """The raw learner answers with their intents — GATED."""
    _fresh_guard('writer_output')
    recs = _jsonl(path or os.path.join(FRESH, 'writer_output.jsonl'))
    _log('1k:fresh', 'writer_output', len(recs), purpose)
    return recs


def load_fresh_items(purpose='', path=None):
    """{id, sid, text, intent} — GATED (contains answers)."""
    _fresh_guard('items')
    recs = _jsonl(path or os.path.join(FRESH, 'items_fresh.jsonl'))
    _log('1k:fresh', 'items', len(recs), purpose)
    return recs


def load_judge_key(purpose='', path=None):
    """j -> {id, sid, source, dup_of} — GATED (de-anonymises the judge input)."""
    _fresh_guard('judge key')
    recs = _jsonl(path or os.path.join(JUDGE, 'key.jsonl'))
    _log('1k:fresh', 'judge_key', len(recs), purpose)
    return recs


def load_judge_labels(purpose='', path=None):
    """The blind judge's verdicts — GATED."""
    _fresh_guard('judge labels')
    p = path or os.path.join(JUDGE, 'labels.jsonl')
    recs = _jsonl(p)
    _log('1k:fresh', 'judge_labels', len(recs), purpose)
    return recs


if __name__ == '__main__':
    print('dev items', len(load_dev_items(purpose='cli smoke')))
    print('dev annotations', len(load_dev_annotations(purpose='cli smoke')))
    print('holdout1j items', len(load_holdout1j_items(purpose='cli smoke')))

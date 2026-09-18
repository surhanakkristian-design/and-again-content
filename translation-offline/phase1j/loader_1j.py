#!/usr/bin/env python3
"""Phase 1j — the ONLY sanctioned way to read the Phase 1j split data. Every read is logged.

    from loader_1j import load_items, load_annotations, load_sentences
    items = load_items('dev', purpose='DEV run row 3')          # always allowed
    items = load_items('holdout', purpose='final run')          # needs PHASE1J_FINAL=1

Holdout reads raise PermissionError unless exactly one of

    PHASE1J_FINAL=1        the ONE final run (Task F)
    PHASE1J_LABEL_PREP=1   Task B data preparation: rewriting the Slovak sentences and re-labelling the
                           answers. It produces no checker output and no measurement.

is set. Every call appends one JSON line to `phase1j/access_log.jsonl`:
{ts, side, what (items|annotations|sentences), caller, n, purpose}. The log is the evidence that the
holdout was read only for the sanctioned reasons.
"""
import datetime
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, 'access_log.jsonl')


def _caller():
    try:
        import inspect
        for fr in inspect.stack()[1:]:
            fn = os.path.basename(fr.filename)
            if fn not in ('loader_1j.py', '<stdin>', '<string>'):
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


def _guard(side):
    if side not in ('dev', 'holdout'):
        raise ValueError('side must be "dev" or "holdout"')
    if side == 'holdout':
        final = os.environ.get('PHASE1J_FINAL') == '1'
        prep = os.environ.get('PHASE1J_LABEL_PREP') == '1'
        if not (final or prep):
            raise PermissionError(
                'HOLDOUT is locked: set PHASE1J_FINAL=1 (the one final run) or PHASE1J_LABEL_PREP=1 '
                '(Task B sentence rewrite / re-labelling, no checker output) — and say so in `purpose`.')


def load_items(side, purpose=''):
    """The list of item dicts of one side (schema: phase1j/CONTEXT_1J.md §2)."""
    side = str(side).lower()
    _guard(side)
    p = os.path.join(HERE, side, 'items.jsonl')
    out = [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]
    _log(side, 'items', len(out), purpose)
    return out


def load_annotations(side, purpose=''):
    """sid(str) -> {'hygienised': {...}, 'raw': {...}} for the sentences of one side."""
    side = str(side).lower()
    _guard(side)
    p = os.path.join(HERE, side, 'annotations.json')
    a = json.load(open(p, encoding='utf-8'))
    _log(side, 'annotations', len(a), purpose)
    return a


def load_sentences(side, purpose=''):
    """Answer-free sentence export (DEV only on disk; 'all' reads sentences_all.jsonl)."""
    side = str(side).lower()
    if side == 'all':
        p = os.path.join(HERE, 'sentences_all.jsonl')
    else:
        _guard(side)
        p = os.path.join(HERE, side, 'sentences.jsonl')
    out = [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]
    _log(side, 'sentences', len(out), purpose)
    return out


if __name__ == '__main__':
    print(len(load_items(sys.argv[1] if len(sys.argv) > 1 else 'dev', purpose='cli smoke')))

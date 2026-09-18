#!/usr/bin/env python3
"""Phase 1h measuring-agent I/O wrapper — NOT a checker.

It changes no rule, threshold, word-class table, prompt or hygiene step. It imports the FROZEN
`checker_1h.py` unmodified and only replaces the BYTES the frozen loader reads, to work around two
pure I/O defects found after the freeze (recorded in the report, deliberately not fixed):

  D1  `load_fresh()` builds its sentence map from `fresh/new_sentences_60.jsonl` only, but the blind
      writers answered all 140 sentences of `fresh/writer_input_140.jsonl` -> KeyError on every OLD sid.
  D2  no fresh answer line carries the `chk` block that `FRESH_SCHEMA.md` declares REQUIRED; it is
      produced here by the app's own offline checker (`checker/v2` via `phase1h/chk_fresh.ts`, the same
      checker Phase 1c used) and attached at read time.

usage: python3 phase1h/fresh_io_fix.py --plan | --calls | --tabulate | --selftest
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import checker_1h as C                      # frozen, imported byte-for-byte

FRESH = C.FRESH
_orig_jl = C.jl
_orig_glob = C._jl_glob


def _rows_140():
    """sentence records for all 140 answered sentences (80 old + 60 new)."""
    rows = {}
    for r in _orig_jl(os.path.join(FRESH, 'writer_input_140.jsonl')):
        rows[int(r['sid'])] = dict(r)
    for r in _orig_jl(os.path.join(FRESH, 'new_sentences_60.jsonl')):
        rows[int(r['sid'])] = dict(r)       # the new 60 keep their richer record
    return list(rows.values())


def _jl_patched(p):
    if os.path.basename(p) == 'new_sentences_60.jsonl':
        return _rows_140()
    return _orig_jl(p)


def _chk_map():
    p = os.path.join(FRESH, 'chk_1h.jsonl')
    m = {}
    if os.path.exists(p):
        for r in _orig_jl(p):
            if r.get('chk'):
                m[(int(r['sid']), r['en'])] = r['chk']
    return m


def _glob_patched(pat):
    rows = _orig_glob(pat)
    m = _chk_map()
    for r in rows:
        k = (int(r['sid']), r['en'])
        if not r.get('chk') and k in m:
            r['chk'] = m[k]
    return rows


C.jl = _jl_patched
C._jl_glob = _glob_patched

if __name__ == '__main__':
    sys.argv = [os.path.join(HERE, 'checker_1h.py')] + sys.argv[1:]
    C.main_1h()

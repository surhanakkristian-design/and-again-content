#!/usr/bin/env python3
"""Shared helper: build the EXACT prompt run_2f_cz.py would send for a given v session id.
Importing run_2f_cz executes its module body, so sys.argv is set first.  0 model calls."""
import os, sys
P2F = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def load(batch_ids, cap=2_000_000):
    sys.path.insert(0, P2F)
    argv = ["run_2f_cz.py"]
    for b in batch_ids: argv += ["--batch", b]
    argv += ["--cap", str(cap)]
    sys.argv = argv
    import run_2f_cz as m
    m.alt_build()
    return m
def chunk_task(m, bid, sid):
    """-> (lang, batch_rows, chunk_rows, header, row_lines) for one v session id."""
    bid_, lang, rows = [b for b in m.BATCHES if b[0] == bid][0]
    drv = m.derive_batch(rows)
    tasks = m.batch_tasks(bid, lang, rows, drv)
    t = [x for x in tasks if x[0] == sid][0]
    header = m.VPROMPT(lang)
    assert t[2].startswith(header)
    body = t[2][len(header):]
    lines = body.split("\n")
    assert len(lines) == len(t[3]), (len(lines), len(t[3]))
    return lang, rows, t[3], header, lines

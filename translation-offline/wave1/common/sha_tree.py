#!/usr/bin/env python3
"""Wave 1: SHA-256 of every file under translation-offline/ EXCEPT wave1/ (sorted, relative paths).
Usage: python3 -B sha_tree.py /abs/OUT.txt ; diff two outputs to prove earlier phases are byte-identical."""
import hashlib, os, sys
ROOT = '/Users/kristiansurhanak/Projects/and-again-content/translation-offline'
rows = []
for dp, dn, fn in os.walk(ROOT):
    dn[:] = sorted(d for d in dn if not (dp == ROOT and d == 'wave1') and d != '.git')
    for f in fn:
        p = os.path.join(dp, f)
        if os.path.islink(p) or not os.path.isfile(p):
            continue
        h = hashlib.sha256()
        with open(p, 'rb') as fh:
            for b in iter(lambda: fh.read(1 << 20), b''):
                h.update(b)
        rows.append('%s  %s' % (h.hexdigest(), os.path.relpath(p, ROOT)))
rows.sort(key=lambda r: r.split('  ', 1)[1])
out = sys.argv[1]
assert os.path.isabs(out), 'absolute path required'
open(out, 'w', encoding='utf-8').write('\n'.join(rows) + '\n')
print(len(rows), 'files ->', out)

"""Overnight deploy Stage E (owner decision 39): the last 2 empty Part 3 cells, 39286 hu and 40497 tr.
Same pipeline as the data pass (run_slice.py), on a two-exercise slice s070 that is NOT in slices/index.json;
only the two target cells are ever written.  fix_last2.py review_input | apply [--write]"""
import sys
import run_slice
TARGETS = {(39286, 'hu'), (40497, 'tr')}
run_slice.INDEX['s070'] = {'slice': 's070', 'ids': [39286, 40497], 'levels': ['B1'], 'selected': 0}
_run = run_slice.writer.run
run_slice.writer.run = lambda part, sl, changes, cols, **kw: _run(
    part, sl, [c for c in changes if (c['exercise_id'], c['lang']) in TARGETS], cols, **kw)
if sys.argv[1] == 'review_input':
    run_slice.review_input('s070')
else:
    run_slice.apply('s070', '--write' in sys.argv)

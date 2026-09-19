# Phase 1Q — tooling edits (data content untouched)

Rule: the frozen stack (runner_1p.py, lever1/2/3.py, loader_1p.py, F5 and the other guards,
prompts, FROZEN_CONFIG_1P.json) is NOT changed. Only a key-format mismatch in the normaliser
was fixed. No annotation content, label, threshold, lever or prompt was touched.

## 1. normalise_1p.py — annotation key lookup

`normalise_1p.py` looked the annotation up under the writer-style key `1P001..1P120`, while the
blind annotation agent delivered `data/annotations_src.json` keyed by the numeric sid
`170001..170120` (commit 6021fac, provenance phase1q/taskC/ANNOTATION_PROVENANCE.md). The
normaliser therefore reported
`REFUSED: annotations_src.json has no usable "v" for 120 sentences: [170001, ...]` and exited 2
without writing `data/annotations.json`. Pure format problem, no content problem.

```diff
-            a = src.get('1P%03d' % (s['sid'] - 170000))
+            a = src.get('1P%03d' % (s['sid'] - 170000)) or src.get(str(s['sid'])) or src.get(s['sid'])
```

Both spellings are accepted now; the `1P###` spelling keeps priority, so the behaviour on a
writer-style delivery is unchanged. `normalise_1p.py` is in FREEZE_FILES but is NOT executed by
`--final`; the edit was made BEFORE FREEZE_HASH was computed, so the freeze covers the edited file.

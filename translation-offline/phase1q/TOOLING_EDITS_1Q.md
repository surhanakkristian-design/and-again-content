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

## 2. FREEZE_FILES — two additions (no code changed)

* `build_B.py` was present in `phase1p/` but absent from `FREEZE_FILES`, so `check_freeze()`
  refused the run with `REFUSED: .py files in phase1p not in FREEZE_FILES: build_B.py`. It is a
  writer-side helper, not executed by `--final`; it is now listed, i.e. hash-frozen like the rest.
* `data/annotations.json` (the normalised blind annotation) was added to the list so the freeze
  covers the data the stack reads, not only the code. `check_freeze()` resolves entries relative
  to `phase1p/`, on disk and as `<hash>:translation-offline/phase1p/<entry>`, so a relative data
  path works unchanged.
* `phase1q/f6.py` could NOT be listed: `git rev-parse` does not accept `..` inside a `rev:path`
  (verified: `HEAD:translation-offline/phase1p/../phase1q/f6.py` fails). F6 is offline and is not
  wired into the runner, so instead its committed blob sha is recorded in `phase1q/FREEZE_COMMIT`
  and the file is committed; that pins it just as hard for a post-hoc application.

No runner, lever, loader, guard, prompt or config file was touched; F5 is unchanged.

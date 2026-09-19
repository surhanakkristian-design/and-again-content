# Phase 1P — tooling edits by the runner agent

**None.**  The reconciliations named in the brief (`TF` -> `T`, positional `aid`, the split
`_key_A.json` / `_key_B.json`, dropping the 40 hidden duplicates per writer, the verdict schema)
were never applied, because `data/writer_A.json` does not exist and the A side cannot be
assembled at all — see `FLOOR_CHECK_1P.md`.  `assemble_1p.py`, `floor_check_1p.py`, `runner_1p.py`,
`loader_1p.py` and `lever{1,2,3}.py` are byte-identical to commit 0e0961b; no `normalise_1p.py`
was added, so `FREEZE_FILES` is unchanged.

Inspection of the delivered files was done with throw-away scripts in the session scratchpad,
outside `phase1p/`; no module in `phase1p/` was executed, so `access_log.jsonl` is unchanged too.

# STOP - Phase 2I stage 2 (build / test / freeze) - 21.9.2026, 0 model calls

**Blocker: the frozen 1W stack cannot read production annotations as stored.** The 1W chain expects the 1W
annotation shape `{voice_sk, agent_nom, tf_gold, tense_open, perfective_present, hygienised{..., alt: {tok:
[groups]}, lk, v ...}, raw}`. Production rows (phase2d/out/annotations_sk_final.jsonl) are flat and `alt` is a
LIST of `{tok, class, groups_or_candidates}` (4,064/4,064). First failure, both side tags:
`phase1i/taskB/backfill_s_ids.py:44 backfill_annotation: for k, vs in (a.get('alt') or {}).items()` ->
`AttributeError: 'list' object has no attribute 'items'` (via runner_1j.make_state -> pipeline_1i.configure).

2F solved this with an adapter: phase2f/p3/probe/data/annotations.json holds production sentences in the 1W shape
(e.g. alt `{'cleans': ['clean_pure', ...]}`, `tf_gold`, `voice_sk`, `hygienised`, `raw`). That adapter was not
located within this stage's 12-call budget, and writing a new one would be an unreviewed change to how the
annotation reaches the checker (the brief: "annotation used exactly as stored"). Not guessed.

## What exists (committed, NOT frozen)
- make_tonly.py -> tonly/{lib_prev,pipeline_1i,runner_1p}.py, tonly.diff (123 lines), TONLY_CHANGES.md: 11 edits
  (lib_prev route lock veto; lib_prev prompt 'Practised grammar ... ALREADY VERIFIED' line; pipeline_1i to_item
  locks/lock_ok; ROW7 F2B 1->0; runner_1p build_side lk->locks + lock_ok; decide guard_readouts + LOCKTIP False;
  l3_eligible without LOCKTIP) + __file__ path pins.
- stack_frozen.py (runner_1u in place, MemLoader, say/STOP_CHK redirected), stack_tonly.py (copies preloaded,
  lk/lk_* stripped, poison mode), run_2i.py (transport per section 3, cap 2,000, $1.00, resume, access log),
  test_2i.py (a-i + z), DEFECTS.md.
- test_2i_output.txt = the crash above (the suite stopped at the first stack call; no check ran to completion).

## To unblock (next stage)
1. Locate the 2F production->1W annotation adapter (the code that wrote phase2f/p3/probe/data/annotations.json)
   and call it in stack_frozen.from_2i (both stacks share it; stack_tonly strips lk after it).
2. Re-run `PYTHONDONTWRITEBYTECODE=1 python3 -B phase2i/test_2i.py` until green, then freeze (FROZEN_SHA.txt +
   FREEZE_COMMIT.txt). Test (g) (1W reproduction) does not depend on the adapter and is ready.

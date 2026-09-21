# Phase 2I - defects recorded, NOT fixed (stage 2)

1. **F2B x tip_det_rule interaction** (CONTEXT 1.4). Under LOCKTIP + TIP-as-rejection F2B only relabels an
   `L3:TIPrej` item as `F2B`; but `stack_1v.tip_det_rule` overturns only layer `L3:TIPrej`. With F2B removed, an
   item that F2B labelled can become TIPdet-accepted. Any such verdict flip is caused by the F2B removal.
2. **System text vs ground line.** `lib_prev.SYS` says "SAME = the learner sentence means the same as the
   reference", while GROUND_LINE says judge against the Slovak, not the reference. Kept unchanged in both stacks.
3. **1W chain writes into earlier phases when run in place.** `runner_1p.say` appends to phase1p/run_1p.log,
   `build_side` writes `STOP_CHK` into phase1p/ on a degenerate chk, loaders append to their phase's
   access_log.jsonl. Probably the source of the pre-2I dirty phase1p/run_1p.log + access_log.jsonl. 2I redirects
   say() to stderr and STOP_CHK to the 2I run dir, and feeds data from memory (MemLoader).
4. **Degenerate-chk guard is batch-level.** `runner_1p.build_side` STOPs if every record has the same accepting
   chk; a batch of only exact-reference answers would stop the stack. Harmless for the 900-item set (mixed).
5. **F1 / F2 flags stay on in TONLY** (ROW7_FLAGS) though unreachable: they only run in the L2 lock branch.
   `phase1i/taskB/lock_fix.py` still patches C.f1_lock_ok / C.lock_equivalent_ok at state build (no read).
6. **Production sentences carry no writer tags.** 1W sentences had `tags.writer_tags` (agent, subordinator,
   tf_gold...) feeding `ag_map_1u` (`wt`); production rows have none, so AG runs with `wt = {}` in both stacks.
7. **Reply parsing.** run_2i parses a reply strictly: the bare token SAME / TIP / DIFF, optionally wrapped in
   whitespace or punctuation; anything else is a FAILED call. The 1W chain's own `P.parse_reply` is not used by
   the runner (the stacks receive the parsed token).
8. **Two differing prompt families in one code base.** runner_1k.NEW_RULES (P-1K) says an agent-dropping passive
   is DIFF, VOICE_SAME_LINE (used) says SAME; only the latter is on the 1W/2I path (AG rejects agent drops first).
9. **Production annotation shape != 1W annotation shape** (the stage-2 STOP). Production `alt` is a list of
   `{tok, class, groups_or_candidates}`; 1W code (backfill_s_ids.py:44 and others) needs `alt` as a dict and
   the `hygienised` / `tf_gold` / `voice_sk` wrapper. 2F converted with an adapter; see STOP_stage2.md.

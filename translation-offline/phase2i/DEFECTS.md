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
6. **(superseded in 2b)** Production sentences carry no writer tags. 1W sentences had `tags.writer_tags` (agent, subordinator,
   tf_gold...) feeding `ag_map_1u` (`wt`); production rows have none, so AG runs with `wt = {}` in both stacks.
7. **Reply parsing.** run_2i parses a reply strictly: the bare token SAME / TIP / DIFF, optionally wrapped in
   whitespace or punctuation; anything else is a FAILED call. The 1W chain's own `P.parse_reply` is not used by
   the runner (the stacks receive the parsed token).
8. **Two differing prompt families in one code base.** runner_1k.NEW_RULES (P-1K) says an agent-dropping passive
   is DIFF, VOICE_SAME_LINE (used) says SAME; only the latter is on the 1W/2I path (AG rejects agent drops first).
9. **Production annotation shape != 1W annotation shape** (the stage-2 STOP). Production `alt` is a list of
   `{tok, class, groups_or_candidates}`; 1W code (backfill_s_ids.py:44 and others) needs `alt` as a dict and
   the `hygienised` / `tf_gold` / `voice_sk` wrapper. 2F converted with an adapter; see STOP_stage2.md.

## Stage 2b
9. -> resolved in 2b by the verbatim 2F adapter (adapter_2f.py); the defect itself (shape mismatch) stays true of the 1W code.
6. -> with the adapter, sentences carry 2F's synthetic writer_tags (agent = `subject`, impersonal_or_passive = voice != 'active_agent', agent_clause always 'main', subordinator None): AG sees what it saw in the 2F probe, not true writer tags.
10. **Adapter pid/lid labels.** The verbatim adapter formats `pid = 'P31%03d' % (sid - 220001 + 1)`; for production sids (n 1..4064) that yields labels like 'P31-219998'. Label only (not in the verdict path as far as the suite shows); not changed.
11. **Adapter reads `d.get('lk')`.** Verbatim 2F code; on TRANSLATION-ONLY the row is lk-stripped first, so the read returns nothing (poison test passes).
12. **Fixture observation:** in test (a) item jx0429 ('Honestly, ...') FROZEN returns layer 'L3', accept False, l3_reply None (no L3 request planned) while TONLY sends it to L3 and accepts. Likely the LOCKTIP/lock path labelling; check in the 4.2 analysis, not investigated here.
13. **3 dirty paths outside phase2i predate 2I and stay as-is:** phase1p/access_log.jsonl, phase1p/run_1p.log (in SHA_before) and untracked phase2d/run_2d_cz.stdout.txt.

## Stage 3
14. **Writer validator bug (stage 3, fixed).** run_writers.validate compared `sorted(types)` with the unsorted list ['T','W','M','S'], so all 4 valid writer outputs were rejected and each session was retried once (4 wasted sessions, ~195k tokens). Fixed to `sorted(TYPES)`; the stored attempt-1 outputs were re-validated offline at 0 cost and used. The spurious STOP_stage3.md (uncommitted) was deleted.

## Stage 5
15. **run_2i.py relative-path crash (recorded, not fixed).** With relative `--set`/`--run-dir`, stack_call writes run/_io/*.json relative to the caller's cwd but runs the stack subprocess with cwd=phase2i, so `prepare` hit FileNotFoundError. First open of the set (pid 20166) died before any model call (0 calls, empty ledger/results); re-launched with absolute paths (pid 20343), which ran the whole set. The access log shows both opens. test_2i.py passes absolute paths, so the suite could not catch it.
16. **Observation, not analysed:** TRANSLATION-ONLY pooled coverage 443/497 is BELOW FROZEN 447/497 on the same items, so removing the structure check lost 4 net correct acceptances. For the 4.2 analysis.

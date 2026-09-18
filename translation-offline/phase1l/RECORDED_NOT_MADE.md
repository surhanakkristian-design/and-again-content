# Phase 1L — changes RECORDED, NOT MADE

The rule set is frozen (arm B, Slovak-anchored acceptance, LOCKTIP, F8, F9, P-FROZEN,
TIP-as-rejection ON, `f9.REPORTED_STRICT` False). Only the three permitted changes were made
(2.1 builder — NOT yet built, see HANDOFF_A.md; 2.2 F9 negated-present fix — made; 2.3 hygiene
plumbing — made). Everything below is recorded and deliberately NOT changed.

1. **The four unpatched guard bugs of Phase 1k report §5.4** (F8 only fires on an English passive
   main clause; F9 inert on DEV so `REPORTED_STRICT` untested; F2B not applied to lock-released
   items; an L2 `step == "mistake"` rejection is not released) stay unpatched, as instructed. The
   runner must only COUNT whether each still fires on fresh.
2. **Phase 1k report §5.4 item 5 / §8** — five DEV false acceptances are L1 exact matches of an
   accepted reference; no layer above L1 can see them. This is exactly what the 2.3 reference
   hygiene pass is for; the references are not edited by this agent, only exported.
3. **F8 `sk_agent` was NOT re-validated or changed.** `f8.py` is a byte-for-byte copy of
   `phase1k/taskB/f8.py`. The brief asks only for F9's hand-check validation.
4. **`_pres_la` also excludes the shapes `-iel` / `-ieľ`** (e.g. the noun "diel"), not just the
   `-iela` of "neposiela". This is inside the same ending-detection family named in 2.2 and can
   only make F9 more conservative on those tokens; it is recorded here because it is slightly
   wider than the single reported sentence.
5. **Fresh hand-check labels exist** — `phase1k/fresh/sentences_fresh.jsonl` carries `tf_gold`
   (70/70) plus `voice_sk` / `agent_nom`, written by agent P before any answer existed. The fresh
   F9 validation therefore has gold to run against; it must run only inside the final run.
   No new gold was invented.
6. **No re-selection, re-tuning, re-weighting or re-tie-breaking** of any configuration was done,
   and no new sentence, answer or judge label was created. The Phase 1k blind-judge labels stand.

7. **The 2.1 builder reproduces only the OFFLINE-decidable part of `chk`.** `compute_chk()` is the
   checker's own L1 test (`checker_1i.refs_of` = `[reference] + annotation v` + the 2.3 gender
   variants, compared under `lib_prev.norm`) plus the annotation mistake patterns. The production
   checker's `spelling_variant` step (1 DEV item) and its fuzzy tolerances are NOT reproducible
   offline and are therefore never produced. Calibration on the 490 DEV records (printed by
   `runner_1l.py dev`): 25 stored `match` reproduce as `match`, 42 stored `match` come out `auto`,
   7 `mistake` and 1 `spelling_variant` come out `auto`, all 415 `auto` agree — 46 accept-level
   disagreements. The 42 are an artefact of arm B: the stored DEV `chk` was produced by the live
   checker against the ORIGINAL Slovak/reference pair, while arm B measures against the rewritten
   Slovak and its realigned references. The direction of the difference is CONSERVATIVE: the
   computed `chk` accepts strictly fewer items at L1, so more fresh items reach L2/L3 and are
   judged by the frozen stack rather than waved through. **DEV `chk` is NOT recomputed** — the DEV
   and replay1j regressions reproduce Phase 1k exactly (182/189, 12/301; 90.82 / 5.10 / 3.39).
   No attempt was made to "improve" the agreement.
8. **Reference-hygiene removal of the DISPLAYED reference.** A patch may remove the string that is
   also `r['reference']`, which the prompt has to show. The deterministic rule applied is: promote
   the first surviving `v` entry to reference; if nothing survives, keep the original reference and
   report the sid under `reference_kept_because_nothing_survived`. No reference is invented.
9. **F9's fix is inert on DEV and on the 1j replay** (0 readouts move, guard bug 2 of §5.4 again).
   Nothing was tuned to make it fire; its effect, if any, will show only on the fresh side.
10. **Free-tier versus billed is not detectable from the response body.** The spend figures are
   list-price figures for the tokens the API reported; no attempt was made to infer the tier.


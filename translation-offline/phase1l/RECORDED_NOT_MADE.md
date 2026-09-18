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

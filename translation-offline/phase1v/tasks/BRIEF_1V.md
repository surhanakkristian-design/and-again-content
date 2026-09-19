# Brief: offline translation checking – Phase 1V (three tracks in parallel, bounded loop, one fresh run)

Repos: ~/Projects/and-again and ~/Projects/and-again-content.
Read ONLY: docs/features/reports/TRANSLATION_OFFLINE_PHASE1U_REPORT.md, phase1u/, phase1t/taskB/.
Model: gemini-3.1-flash-lite, temperature 0, thinkingBudget 0.

## 0. State after 1U (fresh set, opened once, 700 calls, 0 failures)
coverage 382/402 = 95.02 % [92.42, 96.93] — target MET on the interval, the first time.
FA 16/498 = 3.21 % [1.85, 5.17] — met on the point, upper bound 5.17, two items short of settled.
- 9 of the 16 false accepts are agent drops AG v4 misses. Type M 9/159 = 5.66 % is the only cell above 5.
- 12 of the 20 false rejections carry the `determiner` tag — the stack is over-strict on a determiner
  choice the owner's rule declares FREE.
by-passive 98.75 %, SKP 93.65 %, time-frame FA 3.33 %, judge noise 0/80, halves agree (p = 0.49 / 0.80).

## TRACK A — finish Slovak (the only track that opens a fresh set)
A1 AG: fix the misses behind the 9 type-M false accepts. Classify them first (fronted 3, main 3,
   misaligned 3 by writer tag) and fix only what is deterministic. AG v4 costs 1 judged-correct item
   (`W:190081:w2`); do not make that worse. Regression gate: on the 1S packet keep ≥ 96/97 catches,
   0/42 by-passive and 0/39 plain controls rejected. Select on MEASURED COST, never on gold accuracy.
A2 DETERMINER: 12 of the 20 false rejections are a determiner difference. The owner's rule makes the
   determiner free where the Slovak has no demonstrative (ten/tá/tie/tieto). 8 come through
   L3:TIPrej, 4 through a plain L3 DIFF, so this is a PROMPT line plus a TIP-path rule, not an offline
   guard. Build both, measure them separately, and report the cost of each.
A3 BOUNDED LOOP — runs on CLOSED sets only. Repeat, at most 3 rounds:
     (i) apply the next fix from A1/A2 · (ii) re-score the closed 1T and 1U sets (0 or few calls) ·
     (iii) record coverage, FA, FA by type, and the measured cost of each guard.
   STOP the loop immediately and report if ANY of these is true:
     - any headline metric or any named cell gets worse than the round before;
     - a fix would need a change to an owner rule, a target, or the definition of a correct answer;
     - two consecutive rounds gain less than 1 point on the metric being attacked;
     - the model-call budget for the loop (200 calls) is reached;
     - a guard's measured cost rises above 2 judged-correct items on either closed set.
   Never tune against the fresh set of A4. Report every round's numbers, including reverted rounds.
A4 ONE fresh set, opened once: 100 new sentences, arm-B, 25 per level, no overlap with the 770
   existing ones; 4 correct + 5 wrong per sentence. Same build as 1U — blind writers one per level,
   ONE blind judge for all packets, shuffled across levels, 80 hidden duplicates, floors checked on
   JUDGED counts BEFORE the run, sensitivities pre-declared and none able to come out empty.
   Floors: agent drops judged wrong ≥ 120 (fronted ≥ 40, misaligned ≥ 30) · determiner-difference
   answers judged CORRECT ≥ 60 · missing-article judged wrong ≥ 40 · time-frame ≥ 100 ·
   by-passive correct ≥ 60 · SKP correct ≥ 40.
   Report pooled / P1 / P2 with exact Clopper-Pearson intervals and Fisher, both targets on the POINT
   and the INTERVAL, every figure under every sensitivity.

## TRACK B — annotation cost of production sentences (0 fresh data, measurement only)
B1 60 REAL Slovak sentences from the DB (read-only, stratified by level). Rewrite to arm-B (explicit
   subject pronoun where Slovak drops it) and annotate with the unchanged 1N/1M pipeline. Report
   SEPARATELY: tokens/sentence for rewrite, tokens/sentence for annotation, how many of 60 needed a
   rewrite (1J needed 91 of 140).
B2 Deterministic guards' gold validation on those 60 BEFORE and AFTER rewrite+annotation; error rate of
   each guard in both states. 1T measured 47 agent-reader errors on 120 raw production sentences.
B3 Extrapolate to 5,895 (saturation if data supports, else linear): token total, wall-clock, Gemini
   calls (0). State assumptions.

## TRACK C — Czech, three named bugs (0 model calls)
Fix in a Czech-specific reader (Slovak reader untouched): instrumental -em read as 1sg (8/120, 6 false
readings); `se` missing from reflexive regex (23 sentences, both gold reflexive passives lost); `jestli`
read as l-participle (29); Czech aspect lexicon gap (15). Re-run the 1T Czech gold validation unchanged;
agree / conservative / ERROR per guard, before and after, Slovak control beside it. No Czech probe, no
Czech test set.

## Constraints
Gemini spend pre-approved up to $1.00; free tier first, paid fallback allowed; report actual spend.
HARD CAP 1,200 model calls whole phase: loop ≤ 200, A4 run ~600, B and C 0. Plan the count, print it,
STOP rather than narrowing scope. Preflight with L3-eligible 0 or degenerate all-accepting `chk` STOPS
with 0 calls; counted = (http 200) only; retry http 0/429/5xx logged counted:false; empty/unparsable
200 = FAILED call, counted, never guessed, never retried; if the run crashes, recompute from stored
verdicts and say so in the title; no code change after the run starts. Freeze and commit before
opening the fresh set; record freeze hash AND RUN commit; write FINAL_RUN_DONE; publish access log
verbatim; chmod a-w earlier phase dirs BEFORE the run. Each agent at most 12 own tool calls; at 12,
stop and report. No DB writes (read-only SELECT ok), no app code changes, nothing deployed, no
migration applied. Every lettered item appears in the report with result or "not done".

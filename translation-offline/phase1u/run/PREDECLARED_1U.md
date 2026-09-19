# Phase 1U - PRE-DECLARED scoring plan and sensitivities (written BEFORE the set is judged)

Written by the RUN-TOOLING agent before any 1U verdict exists.  It restates, in the form the
scorer implements, what `phase1u/set/SPLIT_1U.md` declared.  Nothing here may change after
`--final` starts.

## Headline
* **Coverage** = judged-correct items the stack accepts / judged-correct items.
* **False accepts (FA)** = judged-wrong items the stack accepts / judged-wrong items.
* Everything is reported **k/n** with an exact **95 % Clopper-Pearson** interval.
* **P1 = odd sid, P2 = even sid** (sid 190001-190100).  Pooled is the headline; P1 and P2 are
  reported separately and compared with **Fisher's exact test** (coverage and FA separately).
  No figure is ever averaged across halves or levels; every rate is recomputed from raw counts.
* Both targets (**coverage >= 90 %**, **FA < 5 %**) are stated **on the point and on the
  interval**, for pooled, P1 and P2.  A target is MET only if the whole interval clears it;
  otherwise it is reported as MET-on-the-point-only or MISSED, in those words.

## Cells, each on its own line in SCORE_1U.md
missing-article (judged wrong: FA and the layer that rejected; judged correct: n and coverage) *
agent-drop FA split main / fronted / misaligned / other by the WRITER tag among judged-wrong items *
by-passive coverage * SKP coverage * time-frame FA * AG v4 firings, catches and measured cost
(judged-correct answers it rejected) with the offline shadows **v2 / v3 (= v4 flags=()) / guarded
union / full v4** on the same items * FA and false rejections by layer * true rejections by layer *
FA by judged type T/W/M/S * per level * judge noise on the 80 duplicate controls * model replies
SAME/DIFF/TIP, failed calls, tokens, latency and a spend **upper bound** at the published
flash-lite list price.  Every false accept and every false rejection is listed with sid, Slovak,
answer, layer and tags.

## The six pre-declared sensitivities (non-empty by construction; asserted in code)
* **S1 - writer intent.** Score all items by the writer's `kind` (C/W) instead of the judge label.
* **S2 - judged-WRONG borderline scored correct.** `borderline: true` among judged-wrong; if fewer
  than 20 qualify, topped up to 20 with the lowest-`confidence` judged-wrong items (ascending;
  ties by packet position, earliest first).
* **S3 - the mirror.** Judged-CORRECT borderline scored wrong, topped up the same way.
* **S4 - S2 and S3 excluded** from the denominator ("only the confident items").
* **S5 - the pre-ruling reading of articles.** Every `missing-article` item judged wrong is scored
  correct instead (the 1T M1 reading).  The gap headline - S5 is what the owner's ruling costs or
  buys.
* **S6 - leave-one-level-out x 4** (A1, A2, B1, B2 dropped in turn).

Each sensitivity carries pooled / P1 / P2 coverage and FA with intervals and the **n of items
moved**; the scorer REFUSES to finish if any of them moved 0 items.  Sensitivities are reported
**beside** the headline, never instead of it.

## Failed calls
An empty or unparsable HTTP 200 reply is a **failed call**: counted against the cap, never guessed,
never silently retried.  The item keeps the decision the stack reaches without a model verdict (a
rejection), stays in its own judged denominator, is flagged `call_failed` on its row and listed in
`SCORE_1U.md`.  HTTP 0 / 429 / 5xx are retried with backoff and logged `counted:false`.

## Stop rules (in code, before any call)
L3-eligible 0, or a degenerate all-accepting `chk`, STOPS with 0 calls * floors `all_pass` false
STOPS * counted HTTP-200 lines in `phase1u/ledger_dev.jsonl` + planned calls > **900** STOPS and
prints the numbers - the scope is never narrowed to fit the cap * `labels.json` is read LAST, after
every verdict exists * `--final` refuses a second run.

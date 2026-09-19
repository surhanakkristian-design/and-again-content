# Phase 1U — SPLIT, SIDs, floors and pre-declared sensitivities
**Declared 19 Sept 2026, BEFORE any 1U sentence exists.** Nothing in this file may be revised after
the first writer has written a sentence. Any later change is a new phase, not a 1U result.

## Set and ids
- 4 blind writers, one per level (A1, A2, B1, B2). Each writes 29 sentences with local ids
  `s01`–`s29`; the assembler keeps **25 per level**: 8 FR + 6 MC + 6 MN + 5 SKP.
- Public ids `1U001`–`1U100`; numeric `sid = 190000 + n`, i.e. **190001–190100**.
  A1 = 1U001–1U025, A2 = 1U026–1U050, B1 = 1U051–1U075, B2 = 1U076–1U100.
- 9 answers per sentence (4 correct c1–c4, 5 wrong w1–w5) → **900 items**.

## Split
- **Odd sid → half P1, even sid → half P2.** 50 sentences each, 12/13 per level, 450 items each.
- Both halves are reported separately and pooled. The **pooled** figure is the headline; P1 and P2
  are compared with **Fisher's exact test** (coverage and FA separately).
- Figures are never averaged across halves or levels: every rate is recomputed from raw counts.

## Targets and how they are reported
- **Coverage ≥ 90 %** — of the items the judge labelled `correct`, the share the stack accepts.
- **False accepts < 5 %** — of the items the judge labelled `wrong`, the share the stack accepts.
- Each reported **on the point AND on the exact 95 % Clopper–Pearson interval**, for pooled, P1 and
  P2. A target counts as MET only if the whole interval clears it; MET-on-the-point-only is reported
  as such, in those words, and is not a met target.

## Floors — checked on JUDGED counts, BEFORE the run
The run does not start until all six hold. The floor check writes `phase1u/set/FLOOR_CHECK_1U.json`
with each count, and the runner refuses to start if any key is missing or below its floor.

| id | floor | definition |
|---|---|---|
| F1 | ≥ 120 | agent drops judged **wrong** (writer tag `drop-fronted`, `drop-misaligned`, `drop-main` or `drop-other`) |
| F1a | ≥ 40 | of F1, tagged `drop-fronted` |
| F1b | ≥ 30 | of F1, tagged `drop-misaligned` |
| F2 | ≥ 100 | time-frame shifts judged **wrong** (tag `time-frame`) |
| F3 | ≥ 60 | by-passives judged **correct** (tag `by-passive`) |
| F4 | ≥ 40 | answers to SKP sentences judged **correct** (tag `skp-passive`) |
| F5 | ≥ 40 | `missing-article` answers judged **wrong** |

Alongside F5 the floor check also **reports how many `missing-article` answers the judge called
correct** (no floor on it; it is the direct read-out of whether the ruling took, and it feeds S5).

By construction the set delivers, per level: 20 FR/MC/MN sentences × 2 agent drops = 40 (F1 ≈ 160),
8 FR × 2 = 16 fronted (F1a ≈ 64), 6 MC × 2 = 12 misaligned (F1b ≈ 48), 20 + 5×2 = 30 time-frame
(F2 ≈ 120), 20 by-passives (F3 ≈ 80), 5 SKP × ≥3 = 15 skp-passive correct (F4 ≈ 60), and ≥ 17 + 5
missing-article (F5 ≈ 88) — every floor has ≥ 25 % headroom against judge disagreement.

## Cell definitions (fixed now)
- **Agent-drop cell**: items whose writer tag is one of the four `drop-*` tags **and** which the
  judge labelled `wrong`. Split into **main / fronted / misaligned / other** by the writer tag —
  the writer tag, not the judge's `agent_drop` field, defines the cell; the judge's field is
  reported beside it as agreement.
- **Article cell**: items whose writer tag is `missing-article` (both labels reported).
- **Time-frame cell**: tag `time-frame`. **By-passive cell**: tag `by-passive`. **SKP cell**: tag
  `skp-passive`.
- Every cell is reported pooled, P1, P2 and per level, with Clopper–Pearson intervals.

## Judging and controls
- One blind judge brief (`phase1u/set/judge/JUDGE_BRIEF_1U.md`) for the whole set; items shuffled
  across packets irrespective of level and of sentence, **shuffle seed 20260920**, so no judge
  instance is confounded with a level.
- **80 hidden duplicate controls** (80 items repeated in a different packet position under a
  different opaque id). Judge self-agreement on them is reported; the duplicate's second verdict is
  excluded from all headline counts.
- Packets `packet_partK.jsonl`, K = 1..N, N ≤ 5; verdicts `verdicts_partK.json`.

## PRE-DECLARED SENSITIVITIES
Every one of the six is **non-empty by construction** — no sensitivity can silently disappear.
Every headline figure (coverage and FA; pooled, P1 and P2; point and 95 % Clopper–Pearson interval)
is carried through all six and reported in the same table shape as the headline.

- **S1 — writer intent instead of judge labels.** Score all **900** items by the WRITER's
  `kind` (C / W) rather than by the judge's label. *Non-empty:* the set has 900 items by
  construction, whatever the judge does.
- **S2 — judged-WRONG borderline items scored correct.** Take the items the judge labelled `wrong`
  with `borderline: true` and score them as correct. *Non-empty:* if fewer than 20 qualify, top up
  to 20 with the lowest-`confidence` judged-wrong items (confidence ascending; ties broken by packet
  position, earliest first), so **n ≥ 20 always**. `confidence` is mandatory on every verdict, so
  the top-up can always be filled.
- **S3 — the mirror on the judged-CORRECT side.** Judged-`correct` borderline items scored wrong,
  topped up the same way from the lowest-confidence judged-correct items; **n ≥ 20 always**.
- **S4 — the S2 and S3 item sets excluded** from the denominator altogether (the "only the confident
  items" reading). *Non-empty:* S2 ∪ S3 has ≥ 40 items by the two rules above.
- **S5 — the pre-ruling reading of articles.** Every `missing-article` item that the judge labelled
  `wrong` is scored **correct** instead (i.e. the Phase 1T M1 reading in which a dropped article was
  a function-word omission). *Non-empty:* ≥ 40 items by floor F5. This is the sensitivity that
  prices the owner's ruling: the gap between the headline and S5 is exactly what the ruling costs or
  buys.
- **S6 — leave-one-level-out × 4.** Four re-computations, each dropping one level's 25 sentences
  (225 items). *Non-empty:* each leaves 675 items.

Reporting rule for all six: report them beside the headline, never instead of it; the headline is
the judge's labels on the full 900 minus duplicates.

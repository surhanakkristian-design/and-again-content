# Phase 1P — floor check: STOP before the run (0 model calls)

Runner agent, 19 Sept 2026.  The final run was **not** started: the phase cannot be assembled,
so the four floors cannot be certified.  0 counted model calls were made in this session
(`calls.jsonl` still holds the 225 dev calls only).

## Blocker: `data/writer_A.json` does not exist

`assemble_1p.py` reads `data/writer_A.json` (SIDs 1P001-1P060) and `data/writer_B.json`
(1P061-1P120).  Only the B file was delivered:

    data/  writer_B.json  writer_B_part1.json  writer_B_part2.json  writer_B_part3.json

A machine-wide search (`~/Projects`, the Drive folder, `/tmp`, the session scratchpad) finds
`writer_A.json` **only** as the synthetic fixture `selftest/fx/data/writer_A.json`.  It is in no
commit (`git log --all -- '*writer_A*'` returns only 0e0961b, the fixture), in no stash.
The A-side writer agent published its judge packets and key but never left the writer file behind.

What survives of the A side, and what does not:

| A-side artefact | state |
|---|---|
| 60 Slovak sentences, level, topic | recoverable from `judge/packets_A{1,2}.json` |
| 540 answer texts, addressed by sid + aid | recoverable from packets + `judge/_key_A.json` |
| judged labels (judged / type / passive / tip) | **complete**, `judge/verdicts_A{1,2}.json` |
| sentence annotations (`tf_gold`, `nom_agent`, `agent`, `passivizable`, `voice_sk` …) | **lost** |
| per-answer writer tags (`agentless` / `by-passive` / `determiner` / `timeframe` / `aspect`) | **lost** |
| per-answer writer intent (T/TF, W, M, S) | **lost** |

The lost columns are exactly the ones the stack consumes: `loader_1p.load_annotations()` refuses
without `data/annotations.json`, lever 1 needs `agent_nom`, lever 3 needs the determiner/tense
annotation, and two of the four floors are defined on the writers' tags.

Reconstruction by this agent was rejected on purpose.  Re-deriving the `agentless` tag from the
answer text means running lever 1's own detector over the data: floors 2 and 3 would then be
circular and the required read-out "lever-1 detector agreement with the tag" would be vacuous.
Re-deriving `tf_gold` / intents means authoring the blind writer's data from inside the runner.
Neither is a tooling reconciliation, so neither was done.  **No tooling was edited** — see
`TOOLING_EDITS_1P.md`.

## What was measurable, with 0 calls

Verdict coverage is complete: 1,160 verdicts for 1,160 jids (580 + 580), no jid judged twice,
no jid unjudged.  Per side 540 test items + 40 hidden duplicates.
Two judge agents were used: agent 1 did A1 + A2 and stalled, agent 2 did B1 + B2.

### Judge noise (the 80 hidden duplicate pairs)

| side | pairs scored | label disagreements | type-only disagreements |
|---|---|---|---|
| A | 40 | 0 | 0 |
| B | 40 | 0 | 0 |

80/80 pairs identical in judged label **and** type.  Perfect duplicate agreement is not a
measurement of judge reliability here — the duplicate carries the identical answer string, so this
bounds only within-answer self-consistency.  It should be read as "no evidence of noise", not as
"noise = 0".

### Judged labels (test items only)

| side | judged correct | judged wrong | wrong T | wrong W | wrong M | wrong S |
|---|---|---|---|---|---|---|
| A | 300 | 240 | 104 | 67 | 9 | 60 |
| B | 299 | 241 | 120 | 60 | 1 | 60 |
| both | 599 | 481 | **224** | 127 | 10 | 120 |

Judge's own passive tag: judged-correct agentless A 66 / B 51 (= 117), by-passive A 17 / B 25;
judged-wrong agentless A 78 / B 79.  Tips: A 137, B 115.

The owner rule landed as predicted on the B side, where writer intent survives:
writer-intended **M** (dropped meaning) 59/60 judged **correct**, 1 judged wrong; C 240/240
correct; TF 120/120, W 60/60, S 60/60 wrong.  So on B the judged set is 299 correct vs the 240
writer-intended correct.

### Floors — 2 of 4 cannot be evaluated at all

| floor | target | B side (measurable) | A side | verdict |
|---|---|---|---|---|
| judged-wrong, time frame (type T) | >= 120 | 120 | 104 | 224 — would hold |
| judged-wrong with the writers' `agentless` tag | >= 60 | 76 | tag lost | **not evaluable** |
| judged-correct agentless passives (writers' tag) | >= 60 | 50 | tag lost | **not evaluable**, B alone under |
| judged-correct determiner variants (writers' tag) | >= 80 | 60 | tag lost | **not evaluable**, B alone under |

B-side writer tags, for the record: judged-correct plain 92, determiner 60, agentless 50,
by-passive 25, aspect 13; judged-wrong timeframe 120, plain 114, agentless 76, number 12,
determiner 7.

Even if the A side had been tagged in the same proportion, floors 3 and 4 clear only through A:
B alone supplies 50 of the 60 agentless-correct and 60 of the 80 determiner-correct.  Running the
B half alone would therefore both miss two floors and silently halve the pre-declared split
(SPLIT_1P.md fixes 120 sentences, 60 per half, 15 per level per half) — an unannounced narrowing of
scope, which the brief forbids.  It was not done.

## Not done, and why

* no freeze (`FREEZE_HASH`, `RUN_COMMIT`), no `chmod -R a-w` on the earlier phase dirs — freezing a
  set that is missing half its data would only make the defect permanent;
* no `--preflight`, no `--dry-run`, no `--final`, no `--ablation`;
* no `HEADLINE_1P.json/.md` — nothing was opened, so there is nothing to report;
* the 1P set is still **unopened**: no 1P sentence or answer was shown to a model in this session.

## Remedy (cheapest first)

1. A fresh, blind A-side writer agent re-derives, for the **existing** 60 A sentences and 540
   answer texts (both fully recoverable from `judge/packets_A{1,2}.json` + `judge/_key_A.json`),
   the sentence annotations and the per-answer tags and intents, and writes `data/writer_A.json`
   in the B file's schema.  The answer strings must be reproduced verbatim so the judged labels
   stay valid — no re-judging, 0 judge calls.  Note the aid convention differs per writer
   (A: `c0..c3` / `w0..w4`, B: `c1..c4` / `w1..w5`) and A codes the time frame `T` where B codes
   `TF`; that part is a genuine tooling reconciliation and is still open.
2. Failing that, a new A side is written from scratch and judged (~580 judge items).
3. Running 1P on the B half alone is possible but changes the declared design and misses two
   floors; it needs the owner's explicit decision, not the runner's.

The phase-cap ledger is untouched: 225 of 1,400 counted calls used, 1,175 left.

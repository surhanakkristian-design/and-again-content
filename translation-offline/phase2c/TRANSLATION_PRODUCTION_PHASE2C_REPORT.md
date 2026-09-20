# Translation production Phase 2C: Slovak is annotated and fit to upload, Czech was stopped by rate limiting

20 September 2026. Files: `and-again-content/translation-offline/phase2c/`. 0 Gemini calls, DB SELECT only, no migration,
no deploy, no push, no checker rule changed. Nothing was written to the database. The run was **stopped by the owner at
07:37** while Czech batch 1 was in flight; nothing was retried, restarted or deleted.

**Headline:**
- **Slovak is COMPLETE: 4,064 sentences in 5 batches, all five GATE 3 checks passed**, written, committed and left
  byte-identical (`out/annotations_sk_0001..0005.jsonl`, `out/DONE_sk_0001..0005`).
- The Slovak count is **4,064, not 4,109**. The brief's 4,109 is 2B's slot count before this phase's exclusion union;
  45 (concept, level) slots lost every candidate to the excluded ids, so the rule yields 4,064 per language (§3.1 of the
  selection work, `selection_2c_summary.json`). 4,109 was never attainable either.
- **Czech did not complete.** Batch `cz_0001` reached **13 of its 20 sessions** (7 rewrite-fallback + 6 v, 600 v-rows),
  then the run hit sustained throttling. No `annotations_cz_*.jsonl` exists: a batch is written only when all 20 sessions
  finish. The 13 session files are on disk, valid, and reusable by a resume.
- **The throughput collapse is rate limiting, not a code fault.** Czech sessions went from 66,091 tokens / 277 s
  (238 tok/s) before 02:22 to 313,773 tokens / 12,554 s (25 tok/s) after the five-hour gap — **tokens ×4.75, wall ×45** on
  identical prompts, with a literal `429` three times inside `cz_0001_s04_v.json`.
- **Cost: 1,356.5 tokens per Slovak sentence against 2B's 1,033.4 (+31.3 %).** GATE 1 sent five more fields to the model
  than 2B assumed, which is where the increase went.
- **GATE 1 largely failed.** After the three reader fixes only **person, number and perfective_present** clear the 10 %
  bar. voice, agent_nom, gender, tf and tense_open are model-authored.
- **GATE 2 passed:** v_cz measured at **510.1 tok/sent** incl. cache reads against Slovak's 476.7.
- Harness spend **≈ 8.6 M of 14.0 M** (7,908,962 measured headless + 292,093 subagent + main session, estimated).

---

## 1. Slovak: what was annotated, and at what cost

| batch | rows | tokens | tok/sent | batch wall | finished |
|---|---|---|---|---|---|
| sk_0001 | 1,000 | 1,364,193 | 1,364.2 | ~27 min (includes the pre-run smoke session) | 00:47:04 |
| sk_0002 | 1,000 | 1,339,641 | 1,339.6 | 25.3 min | 01:13:53 |
| sk_0003 | 1,000 | 1,356,943 | 1,356.9 | 25.4 min | 01:40:50 |
| sk_0004 | 1,000 | 1,344,287 | 1,344.3 | 26.2 min | 02:07:01 |
| sk_0005 | 64 | 107,610 | 1,681.4 | 4.7 min | 02:11:42 |
| **total** | **4,064** | **5,512,674** | **1,356.5** | **≈ 1 h 52 min** | |

- 82 sessions (41 v + 41 rewrite-fallback), 4 in parallel, N = 100 per v session. Mean v session: 87,439 tokens / 426.0 s.
- **1,356.5 vs 2B's 1,033.4 = +31.3 %.** 2B's figure assumed voice / agent_nom / gender / tf / tense_open would be
  script-derived; GATE 1 refused all five, so they ride in the v session, and the lk correction was folded into the same
  session (saving 2B's separate 245.6 tok/sent judge pass). Net effect: +323 tok/sent.
- Wall clock: the Slovak side ran at **0.93 s/sentence at 4 parallel**, comfortably inside the 5 h projection in `PLAN.md`
  (2.85 h for both languages).
- Field completeness over 4,064 rows: 2 real gaps (1 `number`, 1 `perfective_present` null). `subject` is null on 1,576
  rows and `gender` on 1,094 — both legitimate absences (pro-drop, gender not applicable), not omissions.
  `script_reader_agent` is null on 3,110 rows by design: it is the diagnostic column that records where the fixed
  `reader_nom` abstained.

### GATE 3 (random 50 per batch, scored against that batch's own model annotation), bar 12 %

| batch | AG v4 ERROR-of-decided | reader_nom ERROR-of-decided | g4 (diagnostic only) | lk adjust rate | verdict |
|---|---|---|---|---|---|
| sk_0001 | 6.00 % [1.25, 16.55] (3/50) | 0.00 % [0.00, 10.28] (0/34 decided, 16 abstain) | 32.0 % | 13.0 % | PASS |
| sk_0002 | 10.00 % [3.33, 21.81] (5/50) | 7.69 % [0.95, 25.13] (2/26) | 36.0 % | 11.0 % | PASS |
| sk_0003 | 10.00 % [3.33, 21.81] (5/50) | 6.45 % [0.79, 21.42] (2/31) | 14.0 % | 18.4 % | PASS |
| sk_0004 | 6.00 % [1.25, 16.55] (3/50) | 0.00 % [0.00, 14.25] (0/24) | 24.0 % | 9.0 % | PASS |
| sk_0005 | 4.00 % [0.49, 13.71] (2/50) | 0.00 % [0.00, 13.72] (0/25) | 12.0 % | 53.1 % | PASS |
| **pooled** | **7.20 % [4.32, 11.14]** (18/250) | **2.86 % [0.78, 7.15]** (4/140) | 23.60 % [18.48, 29.36] | — | |

AG v4 pooled 7.20 % sits exactly on 2B's 7.0 % [3.88, 11.47]. The fixed `reader_nom` is better than 2B's post-rewrite
11.0 %, but it buys that by abstaining on 44 % of the scored rows (110 of 250 decided). **g4 is a diagnostic only** and
was never gated on: 2B settled it as the harness guard built over AG v2/v3, with 20 of its 23–28 raw errors the one
reflexive `si`/`sa`/`se` pattern that the arm-B rewrite amplifies by construction; 23.6 % pooled here is consistent with
that and says nothing new.

## 2. The lk_adjust_rate jump: not noise, but not batch size either

Per batch: **13.0 %** [10.98, 15.24] · **11.0 %** [9.13, 13.11] · **18.4 %** [16.04, 20.94] · **9.0 %** [7.30, 10.95] ·
**53.1 %** [40.23, 65.72] (34 of 64).

sk_0005's interval does not come close to touching the first four (pooled 12.85 % [11.83, 13.93]), so on 64 rows this is
**not small-sample noise** — a 9 % process does not produce 34/64 by chance. But the batch's size is not the explanation
either, and the obvious "the tail of the md5 ordering is different material" story does not survive one check:
**the builder's smoke session — the first 100 rows of sk_0001, run alone before the full run — adjusted 48/100 = 48.0 %
[37.90, 58.22].** Those same 100 rows sat inside sk_0001, whose full-batch rate is 13.0 %.

So the pattern is by session, not by slice: the **two sessions that ran alone scored 50.0 % [42.10, 57.90] (82/164)**,
and the **45 sessions that ran four-up inside a batch scored 12.85 % [11.83, 13.93] (514/4,000)**. sk_0005 was a lone
session too (64 rows, one chunk). That is a 4× difference with no linguistic cause, and it is a defect, not a finding:
either the loaded sessions under-adjust or the lone sessions over-adjust. 2B's dedicated judge pass measured 20.5 %
[15.4, 26.4] on the 200-row sample — between the two, closer to the loaded rate.

**Consequence for the owner: `lk` is the one field in the Slovak output I would not trust as delivered.** Everything else
passed a gate; `lk` passed no gate, and its own diagnostic is unstable by a factor of four. Fixing it costs a separate
lk pass at 2B's measured 245.6 tok/sent — about 1.0 M tokens for the 4,064 Slovak rows — and does not require redoing
anything else.

## 3. GATE 1: the three reader fixes, before and after

The three named defects were fixed in `phase2c/derive_2c.py` (frozen code untouched; `mode="before"` reproduces 2B
byte-for-byte — 0/1600 field mismatches against `derived_2b.json`). Fix 1: the f9 Czech tokenizer's character class now
covers ř/ů and the rest of the Czech+Slovak alphabet. Fix 2: `_verbish` no longer takes nouns (`ceste`, `Kámoš`) for
finite verbs. Fix 3: `reader_nom` no longer returns adverbs, particles, subordinators, obliques, bare adjectives or the
demonstrative `ty` as agents, and abstains when no nominative candidate remains. `tense_open` was left alone by
instruction: 2B showed it is a definition mismatch and the gold itself flips on 13/100 Slovak rows.

ERROR-of-decided, exact 95 % Clopper–Pearson, sk | cz:

| field | before sk | after sk | before cz | after cz | gate (10 %, both languages) |
|---|---|---|---|---|---|
| person | 5.63 % [1.56, 13.80] | **4.29 % [0.89, 12.02]** | 11.76 % [5.22, 21.87] | **8.82 % [3.31, 18.22]** | **PASS** |
| number | 2.70 % [0.33, 9.42] | **1.37 % [0.03, 7.40]** | 4.41 % [0.92, 12.36] | **2.94 % [0.36, 10.22]** | **PASS** |
| perfective_present | 7.41 % [2.77, 15.43] | **7.41 % [2.77, 15.43]** | 3.77 % [0.46, 12.98] | **5.45 % [1.14, 15.12]** | **PASS** |
| voice_sk | 17.65 % [8.40, 30.87] | 14.29 % [5.94, 27.24] | 16.67 % [7.48, 30.22] | 11.36 % [3.79, 24.56] | FAIL |
| agent_nom | 17.78 % [8.00, 32.05] | 11.63 % [3.89, 25.08] | 34.88 % [21.01, 50.93] | 21.05 % [9.55, 37.32] | FAIL |
| gender | 11.63 % [3.89, 25.08] | 11.63 % [3.89, 25.08] | 20.83 % [7.13, 42.15] | 19.23 % [6.55, 39.35] | FAIL |
| tf | 12.00 % [5.64, 21.56] | 12.00 % [5.64, 21.56] | 17.39 % [7.82, 31.42] | 14.89 % [6.20, 28.31] | FAIL |
| tense_open | 22.83 % [14.72, 32.75] | 22.83 % (untouched) | 42.53 % [31.99, 53.59] | 43.96 % (untouched) | FAIL (not fixed by instruction) |

The fixes worked — Czech `agent_nom` fell from 34.88 % to 21.05 %, Czech `person` from 11.76 % to 8.82 % — but **none of
the three target fields crossed the bar**, so voice, agent_nom, gender, tf and tense_open went to the model in §3, which
is the whole of the +31.3 % token cost. Two caveats stay on the record: the fixes were designed from defect examples
drawn from this same frozen 200-row sample, so the AFTER column is an optimistic in-sample number; and several cells
have 19–75 decided rows, so the intervals are wide (Czech person's upper bound is 18.22 %). The out-of-sample check is
GATE 3, where the fixed `reader_nom` ran at 2.86 % [0.78, 7.15] on 4,064 fresh Slovak rows — but at the price of a 44 %
abstention rate.

**GATE 2:** v_cz measured once, N = 100, one session: 51,010 tokens = **510.1 tok/sent incl. cache reads, 302.3 excl.**,
108.0 output tokens/sent, 98.7 s, against Slovak's 476.7 / 252.1 / 71.4 / 53.6. Czech is 7.0 % dearer incl. cache reads
and 19.9 % excl. Under the 700 bar, so the §4 extrapolation stood: mean 1,050.1 tok/sent → 8.54 M for 8,128 sentences.
The run came in at 1,356.5 for Slovak, 29 % above that, because of GATE 1, not because of Czech.

## 4. Czech: what exists, and why it stopped

Completed and on disk (`out/sessions/`), all valid, nothing deleted:

| session | kind | tokens | wall | rows | finished |
|---|---|---|---|---|---|
| cz_0001_s01_rw | rewrite fallback | 47,110 | 115.7 s | 53 | 02:13:38 |
| cz_0001_s02_rw | rewrite fallback | 44,622 | 137.6 s | 44 | 02:14:00 |
| cz_0001_s03_rw | rewrite fallback | 46,434 | 125.9 s | 44 | 02:16:05 |
| cz_0001_s01_v | v + fields + lk | 89,130 | 423.3 s | 100 | 02:18:45 |
| cz_0001_s02_v | v + fields + lk | 91,262 | 479.0 s | 100 | 02:19:41 |
| cz_0001_s04_rw | rewrite fallback | 48,646 | 148.3 s | 46 | 02:21:14 |
| cz_0001_s03_v | v + fields + lk | 95,434 | 510.7 s | 100 | 02:22:08 |
| — | — | — | **four-hour, forty-three-minute gap, four sessions in flight, none completing** | — | — |
| cz_0001_s05_rw | rewrite fallback | 341,748 | 17,032.5 s | 48 | 07:05:06 |
| cz_0001_s04_v | v + fields + lk | 436,644 | 18,839.1 s | 100 | 07:30:05 |
| cz_0001_s05_v | v + fields + lk | 433,946 | 18,634.1 s | 100 | 07:30:15 |
| cz_0001_s06_v | v + fields + lk | 437,473 | 18,510.3 s | 100 | 07:30:39 |
| cz_0001_s07_rw | rewrite fallback | 79,701 | 383.1 s | 40 | 07:36:38 |
| cz_0001_s06_rw | rewrite fallback | 153,128 | 1,924.2 s | 51 | 07:37:10 |

Not done: `cz_0001` v sessions s07–s10, rw sessions s08–s10 (7 of 20), and batches `cz_0002`–`cz_0005` entirely.
Czech spend so far: 2,345,278 tokens for 600 annotated rows. **No `annotations_cz_*.jsonl` was written** — by design the
runner writes a batch's annotations only when all 20 of its sessions are complete, so the 13 finished sessions are
banked, not harvested. They are reusable: a resume skips them (`SKIP-DONE`, 0 tokens).

The brief's premise said 11 of 20 sessions; the disk says **13** (7 rw + 6 v). Recorded, not corrected.

**Measured throughput, before and after:**

| window | sessions | mean tokens | mean wall | throughput |
|---|---|---|---|---|
| 02:13 – 02:22 | 7 | 66,091 | 277 s | **238.4 tok/s** |
| 07:05 – 07:37 | 6 | 313,773 | 12,554 s | **25.0 tok/s** |

**This is rate limiting.** Plainly, on four independent grounds:
1. The **429** response code appears literally in `cz_0001_s04_v.json`, three times.
2. Tokens per session inflated **×4.75** on prompts that are the same size and shape as the ones that cost 89–95 k an
   hour earlier — the signature of the CLI re-sending a request after a refusal and re-billing the input and cache reads,
   not of longer work.
3. Wall inflated **×45** while output stayed at 100 rows a session: the sessions were waiting, not computing.
4. It is not Czech, not the prompts and not the code path: `cz_0001_s01..s03` ran at Slovak speed on the same code
   twenty minutes earlier, and the last two sessions after 07:30 partially recovered (383 s / 79,701 tokens), which a
   code fault would not do.

It began when batch `cz_0001` opened its 20-session queue at 02:11, immediately after four Slovak batches had run
82 sessions in under two hours — i.e. after roughly 5.5 M tokens in 110 minutes. The account hit a window limit.

## 5. Upload format: A (.xlsx)

- **A — `out/upload_candidate_A_sk_0001.xlsx`**: 6 columns (`exercise_id`, `language_code`, `level`, `src`, `en`,
  `structure_json`), 1,000 rows, the whole annotation as JSON in one cell. **Lossless — all 34 fields survive.** Largest
  cell measured over the sheet: **2,854 characters against Excel's 32,767 limit**, so ~11× headroom; nothing is at risk
  of truncation.
- **B — `out/upload_candidate_B_sk_0001.csv`**: 30 flat columns keyed by `exercise_id` + `language_code`. Easier to read,
  but **lossy**: it drops `correct_answer_src`, `lk_supplied`, `main_sentence_index`, `field_sources` and
  `script_voice_paths`, and it hard-caps the variable-length fields — `v1`/`v2` only (a third variant would be silently
  lost), `lk1`/`lk2` only, and `alt` reduced to a group-name list.

**Recommended: A for the upload, B alongside it for eyeballing.** `out/annotations_sk_*.jsonl` remains the canonical
artefact; A is a faithful container for it, B is a view. If the import path can read JSONL directly, use the JSONL and
skip both.

## 6. Budget and what Czech would now cost

| item | tokens |
|---|---|
| production run, headless (ledger `spent`) | 7,857,952 — Slovak 5,512,674 + Czech 2,345,278 |
| v_cz measurement session | 51,010 |
| subagents (GATE 1 / selection / runner build) | 292,093 |
| main session | not separately metered; ≈ 0.4 M estimated |
| **total** | **≈ 8.6 M of 14.0 M (61 %)** |

The run's own 10.5 M headless cap was never approached (7.86 M spent, 75 %). The phase budget was not breached — unlike
2B's.

**To finish Czech**, 3,464 sentences remain unannotated (4,064 − the 600 banked v-rows):
- At the healthy Czech rate measured before the throttle (1,379 tok/sent: 918.8 v + 460.6 amortised rewrite fallback):
  **≈ 4.8 M tokens and ≈ 1.6 h** at 4 parallel. That fits the remaining ≈ 5.4 M, with about 0.6 M of headroom and no room
  at all for a retry.
- At the throttled rate: **≈ 23 M tokens and 40–55 h**. Impossible inside this budget.

So Czech is a decision, not a continuation: resume only once the limit window has cleared and only with a fresh budget
allocation, or accept a two-session-per-batch pace. The resume itself is free and safe — the runner is idempotent,
`nohup python3 run_2c.py --all` from `phase2c/` skips every finished batch and session and picks up at `cz_0001_s07`.

## 7. Defects found (recorded, not fixed)

1. **The runner has no circuit breaker for a throttled session.** Its in-flight budget check compares the projected cost
   against a *running mean*, so a session that cost 4.75× the mean sailed through, burned 436,644 tokens and 5.2 h, and
   dragged three siblings with it. A per-session wall ceiling (say 3× mean) and a token ceiling would have stopped the
   Czech side after one bad session instead of six, saving ~1.3 M tokens of retry waste.
2. **`lk_verdict` is unstable by session: 50.0 % adjusted in lone sessions vs 12.85 % in loaded ones** (§2). The lk field
   passed no gate and should not be trusted as delivered.
3. **A partially finished batch harvests nothing.** 13 completed Czech sessions and 2.35 M tokens produce no output file
   because the 20th session never ran. Correct by design (no half-batches on disk), but a `--harvest-partial` flag would
   have turned tonight's Czech spend into 600 usable rows.
4. Two Slovak rows still carry a null after the model pass (1 `number` in sk_0002, 1 `perfective_present` in sk_0004).
5. **g4 pooled at 23.60 % [18.48, 29.36]** across the five Slovak batches — consistent with 2B's reading, diagnostic only.
6. The brief's premises differ from the disk on two counts: Slovak is **4,064** sentences, not 4,109 (45 slots lost every
   candidate to the exclusion union), and Czech reached **13** of 20 sessions, not 11.
7. **GATE 1's after-numbers are in-sample.** The three fixes were designed from defect examples in the same frozen 200-row
   sample they were then scored on.
8. 56 selected rows per language carry an empty `correct_answer` in the source data; they were annotated anyway and are
   flagged per row in `selection_2c.jsonl` (`field_gaps`).
9. The fixed `reader_nom` buys its 2.86 % error with a **44 % abstention rate** — it is now conservative rather than
   accurate, which is the right trade for a gate but means it derives little.

## 8. Judgement

1. **The Slovak annotation is fit to upload**, with one reservation: every field except `lk` passed a gate (AG v4 7.20 %
   [4.32, 11.14], reader_nom 2.86 % [0.78, 7.15], both well inside the 12 % bar), and `lk` should be re-judged in its own
   pass before the column is trusted.
2. **It cost 5.51 M tokens, 1 h 52 min and 1,356.5 tok/sent** — 31 % above 2B's 1,033.4, entirely because GATE 1 refused
   five of the eight derived fields and sent them to the model.
3. **Czech is half a batch in and stopped by the account's rate limit**, with 2.35 M tokens banked in 13 valid sessions
   and nothing written; resuming is free and idempotent, but needs ≈ 4.8 M tokens, ≈ 1.6 h and a cleared limit window.
4. **The 771 concepts with no grammar sentence** (`MISSING_CONCEPTS.txt`) need sentences authored before they can be
   annotated at all — that is a content task, not a pipeline one, and nothing here invented anything for them.
5. **Before the six other languages**: fix the lk instability, add the per-session circuit breaker, and decide whether a
   44 %-abstaining reader is worth keeping or whether voice/agent_nom should simply be model-authored everywhere.
6. **Throughput, not quality, is now the binding constraint** — the pipeline produces good rows at 0.93 s/sentence when
   the API lets it, and 45× slower when it does not; the next phase should be scheduled against the rate limit, not
   against the token budget.

---

### Files

`phase2c/`: `PLAN.md` · `GATE1.md`, `gate1_2c.json`, `gate1_2c.py`, `derive_2c.py`, `derived_2c.json`,
`DEFECTS_gate1.md` · `selection_2c.sql`, `selection_2c.jsonl`, `selection_2c_summary.json`, `MISSING_CONCEPTS.txt`,
`data_2c.py` · `vcz_2c.py`, `vcz_2c.json`, `sessions/v_cz_measure.json` · `run_2c.py`, `run_2c.log`, `ledger_2c.json`,
`gates_2c.json` · `out/annotations_sk_0001..0005.jsonl`, `out/DONE_sk_0001..0005`,
`out/upload_candidate_A_sk_0001.xlsx`, `out/upload_candidate_B_sk_0001.csv`, `out/sessions/*.json` (95 sessions).
Every file was committed as it was produced. Nothing was pushed.

# Translation production Phase 2D: the lk defect was in the measurement, not in the concurrency — and Czech was defeated by 429s

20 September 2026. Files: `and-again-content/translation-offline/phase2d/`. **0 Gemini calls. DB SELECT only —
nothing was written to the database.** No deploy, no migration, no push, no checker rule changed. The Slovak
annotations in `phase2c/out/` are INPUT and were verified byte-identical before and after every step
(`SHA_phase2c_out_before.txt`, 12/12 files, 0 mismatches, twice).

**Headline:**
- **2C's lk diagnosis was wrong, and wrong in an instructive way.** There is no lone-vs-four-up effect. 2C's
  "smoke session" *is* `sk_0001_s01_v`, which the full run reused rather than re-ran; its 48/100 was compared
  against a batch mean that already contains it. The same rows were never judged twice.
- The 41 Slovak v-session prompts share **one byte-identical fixed prefix** (sha256[:16] `63abade8fac1971a`,
  3,122 chars); the lone session's prefix equals the four-up session's exactly; the runner sets no temperature
  and passes no concurrency-dependent flag. **Nothing varies with concurrency.**
- **The dedicated pass settles it the other way round.** At a fixed PAR = 2, all 41 sessions, 4,064 rows:
  **51.13 % non-exact [49.58, 52.68]**, unimodal, 40 of 41 sessions between 35 % and 74 %. 2C's *low* band —
  37 sessions at 2–19 % — is the defect; its 4 high sessions were right.
- **2,076 of 4,064 Slovak `lk` values (51.1 %) differ from the stored answer; 1,699 (41.8 %) differ from what
  2C wrote.** Written to `out/lk_corrected_sk.jsonl` and merged into `out/annotations_sk_final.jsonl`.
- **GATE 3 on the merged output holds:** AG v4 10.00 % [6.58, 14.41] PASS on the point, reader_nom
  3.85 % [1.42, 8.18] PASS. The lk change broke nothing.
- **Czech produced nothing.** 4.91 M tokens, 3.16 h, 58 sessions run, 3,200 rows annotated — and **zero batches
  written**, because a 429 storm killed exactly one session in each of the first three batches and two in the
  fourth, and a batch is written only when all 20 of its sessions are complete.
- **Spend ≈ 7.31 M of the 8.00 M budget.** Finishing Czech needs ≈ 1.08 M more; the phase has ≈ 0.69 M. It
  stops here.

---

## 1. Task A1 — what actually differs between a lone session and a four-up session

**Nothing.** In plain words:

2C's argument had three parts: the lone sessions adjusted 50 % of rows, the four-up sessions adjusted 12.85 %,
and the clincher was that "the builder's smoke session took the FIRST 100 ROWS OF sk_0001 alone and adjusted
48/100, while those same rows inside the full batch came out at 13.0 %".

The clincher is an artefact. `phase2c/PLAN.md` §7 records the smoke session as **`sk_0001_s01_v`** and states
"That session's output stays on disk and is reused by the full run" — and the runner's `session()` does exactly
that, printing `SKIP-DONE` and spending 0 tokens when a complete session file exists. So the file on disk *is*
the smoke session. Its rate is 48/100. The batch rate of 13.0 % is the mean of ten sessions, **one of which is
that very session**. 2C compared one session against an average that contains it and read the gap as a rerun
difference. Those 100 rows were judged once, not twice.

The rest of 2C's split dissolves the same way. The per-session rates are:

```
48 13  2 14  8 14 12  7  4  8 | 12  8 15  6 16 10 10  4 18 11 | 50 18 12  9  7  8 19  7  7 47 | 10 10 11  4  6  7  9 10 15  8 | 53
```

Four sessions sit at 47–53 % and thirty-seven at 2–19 %. **Three of the four high sessions — `sk_0001_s01`,
`sk_0003_s01`, `sk_0003_s10` — ran four-up.** The population is bimodal by session, and concurrency does not
predict which mode a session lands in.

**And the prompts are identical.** Over all 41 Slovak v sessions the fixed prefix (everything up to and
including `Rows:\n`) hashes to a single value, `63abade8fac1971a`, 3,122 characters — one distinct value, 41
sessions. `sk_0005_s01_v`, the lone 64-row session, has a prefix byte-identical to four-up `sk_0004_s01_v`.
The runner invokes `claude -p <prompt> --output-format json --max-turns 12 --model opus` with no temperature,
no seed, no sampling parameter and no flag that depends on `PAR`; `PAR` is a thread-pool size and nothing else.
There is no shared state between the four child processes.

So, as the brief put it: **the prompts are identical, therefore the cause is non-determinism.** Specifically it
is a *session-level* non-determinism, not a per-row one: within each session the verdicts are independent
(observed 0→1 switch counts 46, 53, 50, 31, 22, 27, 18 against binomial expectations 49.4, 49.5, 49.3, 31.4,
22.4, 29.2, 17.8 — no local herding), but the *rate* the session settles on is drawn once and then applied
consistently to all 100 rows. Both modes use the same reason vocabulary; the low mode just spends it on
cosmetics ("dropped trailing period", "trailing period removed") while the high mode applies it to substance
("modal needs its verb", "wh-word is not verb phrase").

The mechanism is visible in the 2C v prompt itself. It hands the model `lk_supplied` and asks it, among
seventeen other fields, to judge it — with the warning "DO NOT COPY lk_supplied BY DEFAULT" that was added
precisely because 2B's v session had copied it 100/100 times. A default that has to be argued against in the
prompt is a default the model sometimes falls back to, and it falls back for a whole session at a time. 2B saw
the extreme of this (0 % adjusted); 2C saw it 37 times out of 41.

**Conclusion recorded in `PLAN.md` before any tokens were spent: the lone/four-up statistic is not real, the
fix is not a concurrency setting, and the fix that matters is taking `lk` out of the seventeen-field v session
and giving it a dedicated pass — which is what the brief asked for anyway, for the wrong reason.**

## 2. Task A2/A3 — the dedicated lk pass

`phase2d/run_2d_lk.py`, 2B's judge method: the model sees **only** `en` and `correct_answer_en`. 2B's `LK`
prompt string is reused verbatim, asserted in code, with exactly two additions — one schema field `lk_fixed`
(the correct span, verbatim from `en`) and one sentence telling the model to fill it — because 2B's judge
returned only a class and this phase needs the corrected value. Prompt sha16 `5fa910459c078539`.

**Fixed concurrency: PAR = 2 for every one of the 41 sessions, recorded in `ledger_2d_lk.json`.** N = 100 rows
per session (64 for the last). No session ran alone, none ran four-up.

### Rates, exact 95 % Clopper–Pearson

| batch | n | exact | adjust | unusable | non-exact | 95 % CP |
|---|---|---|---|---|---|---|
| sk_0001 | 1,000 | 521 (52.10 %) | 289 (28.90 %) | 190 (19.00 %) | **47.90 %** | [44.76, 51.05] |
| sk_0002 | 1,000 | 484 (48.40 %) | 239 (23.90 %) | 277 (27.70 %) | **51.60 %** | [48.45, 54.74] |
| sk_0003 | 1,000 | 485 (48.50 %) | 236 (23.60 %) | 279 (27.90 %) | **51.50 %** | [48.35, 54.64] |
| sk_0004 | 1,000 | 467 (46.70 %) | 228 (22.80 %) | 305 (30.50 %) | **53.30 %** | [50.15, 56.43] |
| sk_0005 | 64 | 29 (45.31 %) | 14 (21.88 %) | 21 (32.81 %) | **54.69 %** | [41.75, 67.18] |
| **pooled** | **4,064** | **1,986 (48.87 %)** | **1,006 (24.75 %)** | **1,072 (26.38 %)** | **51.13 %** | **[49.58, 52.68]** |

All five batch intervals overlap; the material is homogeneous. The mild drift from 47.9 % to 54.7 % tracks a
rising `unusable` share, not a rising `adjust` share.

**Against the three reference points.** 12.85 % (2C four-up) and 20.5 % (2B) are excluded outright — the pooled
lower bound is 49.58 %. 50.0 % (2C lone) sits **just** outside the interval, so the true rate is marginally but
significantly above one row in two. On the face of it 2C's lone sessions were almost exactly right.

**But 51.13 % must not be set against 2B's 20.5 % as if they measured the same thing.** 2B's 20.5 % is an
`adjust` rate with an empty `unusable` class (0/200). Here `unusable` is 26.38 %. The like-for-like slice is
**adjust-only = 24.75 % [23.43, 26.11]** — modestly and significantly above 2B's 20.5 %, not double it.

**What the `unusable` rows are.** Of the 1,072, **1,071 (99.9 %) have `correct_answer_en` as a verbatim span of
`en`, and 1,071 received a valid replacement span from the same sentence.** Not one is a row where no key
phrase exists. The pattern is uniform — the stored answer is a numeral, conjunction, relative pronoun or
interrogative:

| en | stored `correct_answer_en` | `lk_fixed` | reason |
|---|---|---|---|
| He tastes one olive sample, then buys ten oranges. | `ten` | `buys` | numeral, not verb phrase |
| A lagoon is water that is next to a beach, so this beach has a lagoon. | `that` | `is water` | relative pronoun, not verb |
| She has got one ticket for the plane. | `one` | `has got` | number, not verb phrase |
| The plate is clean, so the food looks perfect. | `so` | `is` | conjunction, not verb phrase |
| He goes to the bathroom because he wants to be there. | `because` | `goes` | conjunction, not verb phrase |

This is the second clause of 2B's own definition of `unusable` ("…or does not identify the practised phrase"),
so the label is used correctly — but it exercises a failure mode 2B's 200-row sample happened not to contain.
**The open question, which is the owner's and not this phase's:** if the pipeline's rule is "the practised
phrase must be a verb phrase", these 1,072 stored answers are real data defects; if exercises may legitimately
practise a conjunction or a numeral, then the judge's scope is too narrow and those rows should be left alone.
This is flagged in the upload README and nothing was overwritten in the database either way.

### The bimodality does not reproduce

Per-session non-exact rate, all 41, at fixed PAR = 2:

```
48 47 49 54 54 42 53 58 17 57 | 47 61 58 57 51 49 48 37 61 47 | 50 65 53 35 50 59 53 49 43 58 | 53 51 43 53 50 74 56 55 47 51 | 55
```

Min 17, max 74, mean 51.1. **Forty of 41 sessions lie between 35 % and 74 %. Exactly one (`sk_0001_s09`, 17 %)
falls anywhere near 2C's low band.** The distribution is unimodal around 2C's *minority* mode. That inverts the
diagnosis: 2C's 37 low sessions were the broken ones, and the failure still fires sporadically — about 1 session
in 41 under a dedicated single-purpose prompt, against 37 in 41 under the seventeen-field v prompt.

### Changes written

- **1,699 of 4,064 rows (41.8 %) got a different `lk[0]` than 2C wrote**; 2,076 (51.1 %) differ from the stored
  `lk_supplied`.
- **`unusable_span` = 1.** Row `n = 3661` ("Where is he sitting? At an empty school table.", stored `Where`):
  the model returned `is sitting`, which is not contiguous in `en` ("is **he** sitting"), so validation rejected
  it and the row kept its 2C value. Every other returned span was a verbatim, case-sensitive substring of `en`.
- `lk_supplied` agreed with `correct_answer_en` in `selection_2c.jsonl` on all 4,064 rows — 0 source
  disagreements.
- `out/annotations_sk_final.jsonl` is `phase2c/out/annotations_sk_0001..0005.jsonl` concatenated in batch order
  with **only** `lk[0]`, `lk_verdict` and `lk_reason` replaced. A round-trip assert passed on all 4,064 rows:
  `lk[1:]`, key order and every other field are byte-identical to 2C.

### Cost

1,924,126 tokens, **473.5 tok/sentence**, 2,214 s combined wall, 869 tok/s, 41/41 sessions exit 0.
**Zero 429s, zero back-offs, zero retries.** The pass cost 93 % more than 2B's measured 245.6 tok/sent, which
is why the first attempt hit its 1.4 M cap at 29 sessions and had to be resumed (idempotently, `SKIP-DONE` on
all 29, 0 tokens) with a 750 k continuation.

## 3. Task A4 — GATE 3 on the merged output

Random 250 rows of `annotations_sk_final.jsonl`, seed 20260920, scored by the frozen AG v4 path and the fixed
`reader_nom`, bar 12 %, **0 model calls**.

| check | result | 95 % CP | bar 12 % | 2C pooled |
|---|---|---|---|---|
| AG v4, ERROR-of-decided | 25/250 = **10.00 %** | [6.58, 14.41] | **PASS on the point** (upper bound crosses) | 7.20 % [4.32, 11.14] |
| reader_nom, ERROR-of-decided | 6/156 decided = **3.85 %** (94 conservative) | [1.42, 8.18] | **PASS** | 2.86 % |

The intervals overlap 2C's throughout. Both checks read `voice` / `subject` / `embedded_agents` /
`script_voice_paths`, none of which this pass touches, so the movement against 2C is sampling, not the lk edit.
**The lk change broke nothing.** The same gate computed on the 29-session partial output gave identical
numbers, which is the expected consequence of an unchanged draw.

## 4. Task B — Czech

`phase2d/run_2d_cz.py`: 2C's runner restricted to Czech, with **PAR = 2**, exponential 429 back-off from 60 s
with jitter and at most 3 retries then `GIVEUP`, a per-session circuit breaker (3× the running mean wall or
tokens, floors 900 s / 200,000 tok), a 60-second monitor thread that aborts the run if measured throughput
stays under 60 tok/s for 20 continuous minutes, and a per-batch projection gate that stops over 4 h or over the
cap. A `--dry-run` self-test exercised all 29 checks at 0 model tokens before launch, including a synthetic
runaway session — against 2C's own healthy mean, 2C's 436,644-token / 18,839-second session is killed at 900 s.
The Czech v prompt is 2C's `VPROMPT("cz")` byte-identical, sha `4f9d486477084793`.

### Sessions reused

**13, exactly as the disk showed, every one logged `SKIP-DONE … 0 tokens`:** `cz_0001_s01_v`…`s06_v` (6 v) and
`cz_0001_s01_rw`…`s07_rw` (7 rw). They were **copied** from `phase2c/out/sessions/`, never moved; `git status`
on `phase2c/` is empty. These were the only SKIP-DONE lines in the run.

### Sessions run, and the outcome

58 spawned: 54 completed (27 v, 27 rw), 4 gave up.

| batch | complete sessions | rows with a v annotation | new tokens | wall | throughput |
|---|---|---|---|---|---|
| cz_0001 | 19/20 | 900/1,000 | 509,365 | 1,061 s | **480.1 tok/s** |
| cz_0002 | 19/20 | 900/1,000 | 1,599,214 | 3,514 s | **455.1 tok/s** |
| cz_0003 | 19/20 | 900/1,000 | 1,618,532 | 4,058 s | **398.8 tok/s** |
| cz_0004 | 9 | 500/1,000 | 1,184,532 | 2,672 s | **443.3 tok/s** |
| cz_0005 | 0 | 0/64 | 0 | — | — |

**Batches completed: zero.** `annotations_cz_NNNN.jsonl`: none. `DONE_cz_NNNN`: none. GATE 3 per batch: no data,
because the gate runs on a completed batch. 3,200 of 4,064 rows have a v annotation sitting in
`phase2d/out/sessions/` (committed) and none of it is assembled.

The cause is arithmetic, not bad luck: four batches each lost one v session to a 429 give-up, and the rule —
carried over from 2C and re-affirmed in the brief — is that a batch is written only when **all 20** of its
sessions are complete. One missing session out of twenty voids a thousand rows.

### Every 429 and back-off

- **19 retries, every one a literal `429`.** Delays behaved exactly as specified — e.g. `cz_0004_s04_v` backed
  off 74.7 s, then 120.8 s, then 258.7 s (60·2ⁿ plus jitter < 30 s), each logged `counted:false`.
- **4 GIVEUPs, all `retries_exhausted (429)`:** `cz_0002_s04_v` (364,431 tok, 2,272 s), `cz_0003_s04_v`
  (279,472 tok, 2,639 s), `cz_0004_s04_rw` (191,397 tok, 983 s), `cz_0004_s04_v` (343,231 tok, 2,072 s). A
  fifth session, `cz_0001_s07_v`, returned an unparsable result on exit 0 (81,602 tok) and is logged as a defect.
- **Those five sessions cost 1,260,133 tokens — 25.7 % of the entire Czech spend — for zero rows.** Each retry
  re-pays the full 100-row prompt and the session is abandoned after the third anyway.
- **Circuit breaker: never tripped.** The longest session ran 2,639 s against a 3×-mean ceiling that the retries
  themselves had pushed up. The guard is sound against 2C's failure but not against this one.
- **Throughput guard: never fired, correctly.** Measured 399–480 tok/s per batch against the 60 tok/s floor —
  16 to 19× 2C's throttled 25 tok/s. The peak low-streak reached 13 of the 20 minutes required. This run was not
  slow; it was refused.
- **Projection gate: never evaluated**, because it only runs after a completed batch.
- **Token cap: fired.** The in-flight pre-check refused `cz_0004_s06_rw` at 4,766,199 spent + 95,000 in flight +
  46,606 projected > 4,900,000; `STOP_token_cap.md` written, exit 3. The final ledger reads **4,911,643** — an
  11,643 overshoot, because sessions already in flight when the pre-check refused the next spawn still landed.
  The cap was not raised.

### What remains

- **864 rows unannotated, in 9 v sessions** — `cz_0001_s07_v`, `cz_0002_s04_v`, `cz_0003_s04_v`,
  `cz_0004_s04/07/08/09/10_v`, `cz_0005_s01_v` — plus about 7 rw sessions.
- At the measured means (v 83,422 tok, rw 46,606 tok): **≈ 1.08 M tokens and ≈ 0.7 h at 440 tok/s.**
  **Nine sessions would close four batches at once**, since cz_0001–cz_0003 are each one session from done.
- Effective cost so far: **1,535 tok/sentence** over the 3,200 annotated rows, against the 1,379 planning
  figure. The difference is the 429 waste.

### lk for Czech

The Czech v sessions wrote `lk` with 2C's unchanged prompt, and each batch carries a
`lk_needs_dedicated_pass: true` sidecar — though since no batch was written, no sidecar exists on disk yet.
Given §1 and §2, **Czech `lk` from the v session must not be presented as final**; it needs the same dedicated
pass Slovak got, at roughly 473 tok/sentence.

## 5. Task C — the upload package

`out/upload_sk_final.xlsx` — format A as 2C recommended: sheet `sk`, 4,064 rows, 6 columns (`exercise_id`,
`language_code`, `level`, `src`, `en`, `structure_json`), the whole 34-field annotation as JSON in one cell.
Lossless. Largest `structure_json` cell over the sheet: **2,937 characters against Excel's 32,767 limit**, 11×
headroom.

`out/UPLOAD_README.md` gives the column-to-database map, states that each line updates exactly one row —
`exercise_localizations WHERE exercise_id = <exercise_id> AND language_code = 'sk'` — and lists ten checks for
the first ten rows. It also flags the one thing this phase could not settle: `lk` / `lk_supplied` belong to the
**English** localization row (`correct_answer` for `language_code = 'en'`), while the rest of the structure
describes the Slovak row, so the upload touches two rows per exercise or needs a separate English correction
list. That is a schema decision and was left to the owner.

**No Czech .xlsx**, because Czech completed no batch. **Nothing was uploaded.**

## 6. Budget

| item | tokens |
|---|---|
| Task A, headless (`ledger_2d_lk.json` `spent`) | 1,924,126 |
| Task B, headless (`ledger_2d_cz.json` `spent`) | 4,911,643 |
| subagents (harness-reported) | ≈ 332,400 |
| main session | ≈ 146,300 |
| **total** | **≈ 7,314,500 of 8,000,000 (91 %)** |

Under budget, with ≈ 685,500 unspent. Finishing Czech needs ≈ 1.08 M, so it is about 0.4 M short and the phase
stops here rather than exceed, as instructed. Gemini calls: **0**. DB writes: **0**.

## 7. Defects recorded, not fixed

1. **`cz_0001_s07_v` returned an unparsable result on exit 0** after 81,602 tokens. Not diagnosed. It is one of
   the nine sessions still owed.
2. **The 429 retry policy is economically wrong.** Three retries at 100 rows each re-pay the full prompt and
   then the session is abandoned regardless: 1,260,133 tokens for zero rows, a quarter of the Czech spend. A
   retry should resume a smaller slice, or the session should be split before the first retry, or a 429 should
   pause the whole pool instead of one session.
3. **The circuit breaker does not catch a retry storm.** It compares against a running mean that the storm
   itself inflates, so the 2,639-second session passed. It needs an absolute ceiling, not a relative one.
4. **The all-sessions-complete rule turned a 95 %-finished run into nothing.** Four batches were one session
   short. 2C recorded this as defect 3 and recommended `--harvest-partial`; the brief re-affirmed the strict
   rule, so 3,200 annotated Czech rows are banked in `out/sessions/` and unusable. It should be revisited.
5. **Row `n = 3661` keeps a wrong Slovak `lk`** (`Where`) because the model's correction was non-contiguous.
   One row; needs a manual span.
6. **The 1,072 `unusable` Slovak rows are an unsettled content question** — stored answers that are numerals,
   conjunctions or pronouns rather than verb phrases (§2). Either the data is wrong on 26 % of rows or the
   judge's scope is.
7. **`lk` non-determinism still fires**, at about 1 session in 41 even under a dedicated single-field prompt
   (`sk_0001_s09`, 17 % against a 51 % mean). A second independent judgement on disagreeing rows would settle it.
8. **`REPORT_2d_lk.json`'s `tok_per_s`** divides the cumulative ledger spend by the current process's wall —
   meaningless on a resumed run. The correct rates are in §2.
9. **`run_2d_lk.py --selftest` commits `GATE3_2d.{json,md}` before deleting them**, leaving one historical
   commit with a gate computed on pure-2C data. Both files are correct at HEAD.
10. **The Czech token cap overshot by 11,643** — in-flight sessions land after the pre-check refuses the next
    spawn. Harmless here, but the cap is a soft ceiling, not a hard one.

## 8. Judgement

1. **The Slovak output is fit to upload.** Every field now carries a gate: AG v4 10.00 % [6.58, 14.41] and
   reader_nom 3.85 % [1.42, 8.18] on the merged file, both inside the 12 % bar, and `lk` has been re-judged in
   a dedicated pass at a fixed concurrency over all 4,064 rows.
2. **`lk` is settled as a measurement and open as a content question.** The rate is 51.13 % [49.58, 52.68]
   non-exact, the concurrency story was an artefact of comparing a session against an average containing it, and
   the real cause is a session-level default in the seventeen-field v prompt — which the dedicated pass removes.
   What is not settled is whether the 26 % of stored answers that are conjunctions and numerals are defects.
3. **2C's `lk` column was wrong on 1,699 of 4,064 rows**, and its lone-vs-four-up finding should be struck from
   the record rather than carried into the other six languages.
4. **Czech is 864 rows and about 1.08 M tokens from done** — nine v sessions, of which closing just three would
   release 2,700 already-paid-for rows in cz_0001–cz_0003. It is the cheapest work in the project and it needs
   a fresh budget, not a redesign.
5. **The binding constraint is the 429, and it is not throughput.** This run measured 399–480 tok/s, 16–19×
   2C's throttled rate; the guards built for 2C's failure all held and none of them caught this one. The next
   run needs a pool-wide pause on 429 and a resume that does not re-pay the prompt.
6. **Do not start the other six languages until defect 4 is fixed.** A pipeline that discards 3,200 finished
   rows because four sessions out of eighty-seven were refused will do it again, and at six languages it will
   do it six times.

---

### Files

`phase2d/`: `PLAN.md` · `SHA_phase2c_out_before.txt` · `run_2d_lk.py`, `ledger_2d_lk.json`, `run_2d_lk.log` ·
`run_2d_cz.py`, `ledger_2d_cz.json`, `run_2d_cz.log`, `STOP_token_cap.md` ·
`out/lk_corrected_sk.jsonl`, `out/annotations_sk_final.jsonl`, `out/GATE3_2d.json`, `out/GATE3_2d.md`,
`out/REPORT_2d_lk.json`, `out/upload_sk_final.xlsx`, `out/UPLOAD_README.md`, `out/sessions/*.json` (41 sk lk +
67 cz). Every file was committed as it was produced. Nothing was pushed.

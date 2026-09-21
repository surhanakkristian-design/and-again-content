# Translation production Phase 2F: Czech coverage was NOT measured — and the probe that did run says production sentences cost Slovak 13 points of coverage

21 September 2026. Files: `and-again-content/translation-offline/phase2f/`.
**0 database writes — SELECT only.** No deploy, no migration, no push, no checker rule change, no rebase.
`phase2c/out/`, `phase2d/out/`, `phase2e/out/` were verified byte-identical before and after: **337 files,
0 mismatches.** Nothing was uploaded. Gemini: **312 counted calls of the 900 cap, 0 failed, $0.0163.**
Claude: **≈ 5,526,000 of the 6,500,000 budget.**

---

## 1. Part 2's headline — first, as asked

**Czech coverage and false acceptance were not measured. The set was never opened. 0 Gemini calls were
spent on it.**

| | Czech (2F Part 2) | Slovak blind test (1W) |
|---|---|---|
| coverage | **not measured** | 392/401 = 97.76 % [95.78, 98.97] |
| false acceptance | **not measured** | 16/499 = 3.21 % [1.84, 5.15] |

Both targets — coverage ≥ 90 %, FA < 5 % — are therefore **unanswered for Czech, on the point and on the
interval.** Nothing in this report should be read as a Czech coverage figure.

**What does exist, and what it cost.** The measurement was built, not run:

* The set is **selected, annotated and packeted**. 100 Czech production sentences, **25 per level**,
  sids 210001–210100, seed 20260921, drawn from the full **39,498**-sentence Czech production corpus read
  SELECT-only (A1 9,999 / A2 13,591 / B1 8,906 / B2 7,002); 4,552 ids and 10,595 normalised sentence texts
  excluded for having been used by 2C/2D/2E/2F-Part-1 or any `phase1*` Slovak set; 34,966 candidates
  remained. **Overlap 0, violations 0, both asserted.**
* The 100 were annotated by the driver itself with the frozen 2E pipeline (v prompt sha16
  `4f9d486477084793`, arm-B rewrite, dedicated `lk` pass sha16 **`5fa910459c078539` asserted in code**),
  PAR 2, MAX_RETRY 3: **12 sessions, 310,134 tokens, 100/100 rows**, lk corrected 52 / exact 48, **no chunk
  refused and no reserve sentence used**.
* 4 blind writers (one per level, seeing only the Czech sentence, its level and its topic) produced
  **900 items**; packets carry `jid / czech / level / answer / topic` with **80 hidden duplicate controls**,
  980 qids, shuffled across levels.
* **It died at the judge.** `judge_s1` ran 13 turns, returned exit 1, and consumed **1,547,186 tokens on its
  own** (cache-read 1,266,632). Cumulative Part 2 headless spend reached **2,265,574** against the
  1,800,000 cap this phase set for it, the cap fired, and the driver wrote its result and stopped:
  *"the judge did not deliver all verdict files; 0 Gemini calls"*.
* **FREEZE hash: none. RUN commit: none. `FINAL_RUN_DONE`: absent. The set remains openable exactly once.**
  Selection, annotations and packets are cached, so a resumed run re-enters at the judge at ≈ 0 tokens for
  everything upstream.

**Two things recorded before anyone resumes it.**

1. The `Label join`, `Floors` and `judge_noise_pct: 5.0` blocks in `p2/PART2_RESULT.md` are **stale
   selftest artefacts, not measurements** — `selftest()` shares the driver's global result object and the
   real stages never overwrote them. Read nothing from those sections.
2. **Production Czech is 52/100 SKP** (no named doer), against MN 23 / MC 19 / FR 6. The assembler therefore
   produced **0 fronted and 0 misaligned** agent drops (drop-main 164, time-frame 136). The floor
   **F1 ≥ 120 agent drops judged wrong is probably unreachable on an unselected production sample.** That is
   a property of the corpus, not of the driver, and it has to be re-declared — as F1a/F1b already were — or
   the strata re-drawn against `kind`, **before** a resumed run is worth its tokens. This is the same class
   of problem as 1T's pre-declared S2, which had 0 qualifying items and tested nothing.

### 1.1 Part 2's cells

**None exist.** No pooled, P1 or P2 coverage or FA; no Fisher; no sensitivity; no agent-drop, by-passive,
time-frame, missing-article, T/W/M/S or by-layer cell; no judge-noise rate. They are not estimated here and
they are not guessed. The Slovak figures they were to be set beside are in §2 and §5 of `phase2f/STATUS.md`.

---

## 2. Part 3.1 — the Slovak PRODUCTION probe, beside 1W

This is the measurement nobody had made, and it is the only new headline this phase produced. **It is a
PROBE**: at n ≈ 180 correct items the interval is about ±5 points — enough to locate the region, not enough
to settle it. Set opened **once**, 60 Slovak sentences from `phase2d/out/annotations_sk_final.jsonl` (the
real uploaded material), 15 per level, sids 220001–220060, seed 20260921, one blind writer, 3 correct + 3
wrong each = **360 items**, one blind judge, frozen 1W stack, L3 `gemini-3.1-flash-lite` / temperature 0 /
thinkingBudget 0.

| | production (2F §3.1) | blind test (1W) | difference |
|---|---|---|---|
| coverage | **154/182 = 84.62 % [78.54, 89.53]** | 392/401 = 97.76 % [95.78, 98.97] | **−13.14 points; intervals DISJOINT by 3.0 points** |
| false acceptance | **11/178 = 6.18 % [3.12, 10.79]** | 16/499 = 3.21 % [1.84, 5.15] | +2.97 points; intervals OVERLAP |

**Both targets MISSED on the point and on the interval.** On coverage, production does **not** behave like
the test sets and the separation is real at this n. On FA the difference is not separable at this n.

**The confound, stated rather than buried.** Production rows carry far thinner reference material: mean
**1.1** accepted English references per sentence with **90 % having only one**, against **2.0** and **0 %**
on the constructed 1U/1W set (`alt` 3.38 vs 4.19). A blind writer's correct-but-differently-worded answer
simply has less to match. The −13-point gap is consistent with thinner annotation, with harder sentences, or
both; reading it as a property of production *sentences* over-reads it.

**Against 2B.** Consistent in direction, not in magnitude. 2B measured the reader's derived field (50 % error
on raw production against 1.67 % on blind-test Slovak); this probe measures the whole stack's verdict. The
deterministic agent path **fired only 13 times in 360 items, every one of them on a judged-wrong answer** —
it cost coverage nothing. Whatever the reader gets wrong is largely absorbed before the final verdict.

Cells, one per line (thin ones left as `n`):
* missing-article FA: 3/27 = 11.11 %  ·  1W 3/97 = 3.09 %
* agent-drop FA: 2/22 = 9.09 % (n = 22, thin)  ·  1W all 10/160 = 6.25 %
* time-frame FA: 1/52 = 1.92 %  ·  1W 2/119 = 1.68 %
* by-passive coverage: 20/24 = 83.33 % (thin)  ·  1W 79/80 = 98.75 %
* by-passive FA: n = 0
* FA by type: M 6/55 = 10.91 % · S 3/31 = 9.68 % · T 1/52 = 1.92 % · W 1/40 = 2.50 %
* FA by layer: **all 11 false accepts land at L3** — no deterministic layer let one through
* L3 replies: SAME 151 / DIFF 131 / TIP 30  ·  1W DIFF 311 / SAME 252 / TIP 37
* coverage by level: A2 97.78 % · B2 84.78 % · A1 82.22 % · **B1 73.91 %**; B2 carries the FA at 13.64 %
* judge noise: **0/36 duplicate-control pairs disagreed = 0.0 % [0, 9.74]**, 0 type-only disagreements

FREEZE hash `36a00a53723b05a87ee0636ca6328bb0b121cc14`, RUN commit
`e99e6b9f084bd312a31527ae997f6d92ef827f54`, `FINAL_RUN_DONE` 2026-09-20T22:37:22Z, result commit `3c63368`.
**312 counted HTTP-200 calls, 0 uncounted retries, 0 failed (0.0 %)**, 162,085 tokens in / 312 out,
**$0.0163** at list price. Access log published verbatim in
`phase2f/p3/probe/PROBE_SLOVAK_PRODUCTION.md`.

---

## 3. Part 1 — finishing Czech

**Rows: 2,850 of 4,064 (70.1 %). Part 1 added 50 rows and cost 1,466,116 tokens.**

| batch | rows | present (`n`) | missing (`n`) |
|---|---|---|---|
| cz_0001 | 1,000 | 4065-5064 | — |
| cz_0002 | **950** (+50) | 5065-5414, 5465-6064 | 5415-5464 |
| cz_0003 | 900 | 6065-6364, 6465-7064 | 6365-6464 |
| cz_0004 | **0** | — | 7065-8064, never annotated |
| cz_0005 | **0** | — | 8065-8128, never reached |
| **total** | **2,850** | | **1,214 missing** |

### 3.1 §1.2's diagnosis, stated plainly

`cz_0002_s04_v` had been refused with 429 on **nine consecutive attempts across two phases, 919,962 tokens,
zero rows**, and 2D's other give-ups were also `s04` of cz_0002, cz_0003 and cz_0004.

* **The byte comparison found nothing.** The instruction header is byte-identical across chunks. s04 is
  **smaller** than three chunks that succeeded (30,839 bytes against 31,690 / 30,903 / 31,871), its longest
  row is shorter (358 against 386 chars), it has fewer non-ASCII characters (613 against 621), and the set of
  codepoints present in s04 and in **no** successful chunk is **empty**. Zero control characters beyond
  newline, zero lone surrogates, zero Cf / bidi / NBSP / zero-width, no markup, nothing that reads as an
  injection or policy trigger.
* **`s04` is always chunk 4 of 10, batch offsets 300-399.** The three s04 chunks share **0** sentences with
  each other and contain 0 internal duplicates. They share nothing but the ordinal position.
* **The halves, run once at MAX_RETRY 3: h1 (n 5365-5414) succeeded on the first attempt, zero 429s, 50/50
  rows, 66,724 tokens. h2 (n 5415-5464) was refused on all four attempts, 218,588 tokens, 0 rows.**
* **The conclusion, plainly: exactly one half succeeded, and that localises the cause to the other half's
  content.** Fifty of the hundred rows that had been refused nine times as one request were answered first
  try, so the chunk is not refused for a reason that applies to all of it — **size alone is not the
  explanation either**, because the identically sized second half was refused four more times. The brief's
  test ("if a 50-row half succeeds, the cause is size or content, not throttling") comes back as
  **content, not size and not throttling — but the content that causes it is not identified.** The byte
  comparison, which is the only instrument available, finds nothing in it.
* Caveat recorded: h2's attempts 1–2 overlapped two duplicate chains of our own (defect 1 below); attempts
  3 and 4 ran clean and were still refused.
* **Ruling applied:** halves did not both succeed, so `cz_0003_s04_v` got one whole-chunk attempt under
  MAX_RETRY 3 (refused, 305,827 tokens) and `cz_0002_s04_v` was not attempted a tenth time.
* **The 50 rows h1 bought were recovered.** The assembler now accepts a half-chunk session over a contiguous
  sub-range (2F change 4); the 2,800 rows already assembled were verified byte-identical afterwards —
  0 vanished, 0 changed.

### 3.2 The guard, twice

**2F change 1** (as briefed): every `counted:false` back-off sleep is recorded as an interval and subtracted
from elapsed time before tok/s is computed, intervals merged so PAR 2 cannot drive the clock negative; the
floor returned to 60 tok/s over 20 minutes on that corrected clock. **2F change 2**: MAX_RETRY 5 → 3.
Self-test 37/37 PASS, 0 model calls.

**It stopped the run anyway, at 00:13:25, with 285,312 tokens and zero new rows.** `STATE["tok"]` is only
incremented when a session *returns*, so a single long-running in-flight session reads as 0.0 tok/s: the
guard counted 20 minutes of legitimate work as 20 minutes of nothing. The brief's fix removed the **sleep**
from the clock; it did not remove **in-flight work that has not returned yet**. **2F change 3** was written
in response: a window in which `tok` has not moved while `inflight > 0` is **unmeasurable** — the streak
neither advances nor resets and the guard cannot fire; a genuinely stuck pool is the circuit breaker's job.
Self-test 41/41 PASS, including that 2C's case (25 tok/s *with* sessions returning) still fires at exactly
20 minutes.

**This is the third phase in a row in which the throughput guard, not the work, ended the run.** 2E raised
the floor and was stopped twice; 2F excluded sleep and was stopped again on a different mechanism.

### 3.3 Every 429 and give-up

**12 HTTP 429s across the phase.** Give-ups: `cz_0002_s04_v` h2 (4 attempts, 218,588 tok),
`cz_0003_s04_v` (305,827 tok), `cz_0004_s04_rw` (195,916 tok), `cz_0004_s04_v` (349,712 tok).
The second Part 1 run stopped on its **token cap** — 1,410,428 spent + 95,000 in flight + 79,155 projected
against a cap of 1,408,861 — at `cz_0004_s09_v`, before cz_0004 reached assembly. **cz_0004 cost 875,000
tokens and produced 0 rows: 29,322 tokens per new row against the healthy 1,379.** The 2,000,000 tripwire
was not reached.

### 3.4 GATE 3 and the new rows' `lk`

**GATE 3: no gate fired and no `STOP_gate3_*` file was written.** Only the three already-assembled batches
were re-assembled; cz_0004 never reached assembly, so it has no GATE 3.

**The `lk` pass did not run on the new rows.** The chain downgrades to `--merge-only` whenever any `STOP_*`
file exists, and this run wrote one. **The 50 recovered rows therefore have no dedicated `lk` judgement and
there is no new-rows non-exact rate to report.** The comparison file was written and says so in writing,
quoting Czech's pooled **52.44 % [50.54, 54.34]** and Slovak's **51.13 %** unchanged — after a first run in
which the same stage died on a `FileNotFoundError`, now fixed.

---

## 4. Part 3.2 — pricing the other six languages (0 model calls)

`phase2f/p3/PRICING_SIX_LANGUAGES.md`.

| language | annotation | `lk` | GATE 3 | engineering (phases) | total |
|---|---|---|---|---|---|
| **ua** | 1,800,000 | 470,000 | 20,000 | 1,600,000 (4.0) | **3,890,000** |
| es | 1,800,000 | 470,000 | 20,000 | 2,000,000 (5.0) | 4,290,000 |
| fr | 1,800,000 | 470,000 | 20,000 | 2,200,000 (5.5) | 4,490,000 |
| de | 1,800,000 | 470,000 | 20,000 | 2,400,000 (6.0) | 4,690,000 |
| tr | 1,800,000 | 470,000 | 20,000 | 3,200,000 (8.0) | 5,490,000 |
| hu | 1,800,000 | 470,000 | 20,000 | 3,200,000 (8.0) | 5,490,000 |
| **total** | | | | | **28,340,000** (52 % engineering; low bracket 24,818,000) |

The three findings that drive it:

1. **`tip_det_rule` (`phase1v/trackA_loop/stack_1v.py:130-134`) fires on 100 % of `L3:TIPrej` rows in all
   six.** Its veto is `SK_DEM.search(sk)`, a Latin list of Slovak demonstratives (`stack_1v.py:107-109`)
   that cannot match German, French, Spanish, Turkish or Hungarian words, or Cyrillic at all. The rule exists
   *because Slovak has no articles*; de/fr/es/hu have them, so the premise is false **and** the safety veto is
   permanently off. Silent, confident, wrong — 1T's four Czech bugs behaved the same way.
2. **`sk_clause_is_passive` (`phase1t/taskA/agent_drop_v3.py:279-287`) returns `False` on every clause of all
   six.** It needs a `SK_BYT` token followed by a `SK_PPART` ending (`ný|ná|né|ní|tý…`). German
   `wird…gebaut`, Turkish's passive **infix** `-ıl-` and Ukrainian's `-но/-то` impersonal (no copula at all)
   produce neither, so AG charges correct agentless English as a dropped agent and the abstain never fires.
3. **Ukrainian's Cyrillic break splits both ways, and that is why it wins.** `checker_1i.py:469`,
   `checker_1i.py:533` and `f9.py:99` are Latin-only character classes returning `[]`, so
   `sk_features → _feats → reader_nom` abstains on 100 % of Ukrainian — **loud and safe**. The three vetoes
   above bypass that tokenizer and run on raw strings, so they stay **silently** off. There is no
   `unicodedata` or `isascii()` anywhere in the stack; ~35 literal tables get rewritten, not patched.

Also recorded: **arm B's explicit-subject rewrite and F4v2's whole purpose go moot for de and fr**
(non-pro-drop), forfeiting 1J's measured 6.55 % → 5.05 % FA gain, replaced by German V2 object-fronting and
case syncretism (no noun suffix for `OBLEND` at `reader_nom.py:199` to test) and French clitics `la`/`les`
homographic with the articles inside the pre-verbal scan window. And `agent_drop_v3.py:370`
("capitalised = proper name") is wrong on **every German common noun** — a one-line, high-frequency,
1T-class silent bug.

**Cheapest next: Ukrainian, 3,890,000 tokens.** Not because Cyrillic is easy but because it fails loudly:
the reader abstains rather than inventing, which is the failure mode this project has paid for repeatedly.
Runner-up: Spanish. What would change the answer: if the three raw-string vetoes were made to abstain on an
unrecognised script, Ukrainian's advantage would collapse to ordinary morphology work and Spanish would win.

**One correction the pricing agent recorded rather than hid.** The briefed anchor of 1,800 tok/sentence does
not reconcile with its own source: 6.84 M / 4,064 = **1,683**, and 2D states that figure covers *both*
passes, so it already contains `lk` (473.5/sentence). Annotation alone is ≈ 1,210. Pricing at 1,800 **plus** a
separate `lk` line double-counts by ≈ 35 %. The briefed figure is headlined above as instructed; the
reconciled low bracket is given beside it.

---

## 5. The upload package

`phase2f/out/upload_cz_final.xlsx` — sheet **`cz`**, **2,850 rows**, six columns (`exercise_id`,
`language_code`, `level`, `src`, `en`, `structure_json`), the whole annotation as JSON in one cell, 2D's
Slovak format exactly. **Largest `structure_json` cell 2,936 characters against Excel's 32,767 — 11.2×
headroom.** `phase2f/out/annotations_cz_final.jsonl`, 2,850 lines. **Nothing was uploaded and nothing was
written to the database.** The 50 rows added this phase carry a v-session `lk`, not a dedicated-pass one;
that is recorded in the meta and in §3.4.

`phase2f/STATUS.md` is the one-page consolidated status (§3.3 of the brief): every measured headline with
its interval and phase, per-guard rates sk vs cz, `lk` rates, rows per language, per-sentence costs, what is
ready to upload, and the three open decisions. Numbers and sources only.

---

## 6. Budget

| item | tokens |
|---|---|
| Part 1 headless (`ledger_2f_cz.json`) | 1,466,116 |
| Part 2 headless (annotation 310,134 · writers ≈ 408,000 · `judge_s1` 1,547,186) | 2,265,574 |
| Part 3.1 headless (8 sessions) | 547,613 |
| agents (6) | ≈ 1,057,000 |
| main session | ≈ 190,000 |
| **total** | **≈ 5,526,000 of 6,500,000 (85 %)** |

**Gemini: 312 counted calls of the 900 hard cap, 0 uncounted retries, 0 failed calls (0.0 %),
$0.0163 at list price** against the $1.00 approval — all of it Part 3.1; Part 2 spent none.
**Database writes: 0.**

---

## 7. Defects recorded, not fixed

1. **`ps` without `ax` lists only the calling session's processes.** Reading its empty output as "the
   launch was reaped" started three annotation chains against one account at once and contaminated two of
   h2's four attempts. Duplicates killed; the lesson is the seventh instance of *suspect the measuring
   apparatus first*.
2. **A session killed from outside spends tokens no ledger sees** — `session()` charges tokens only when the
   CLI returns, so the tripwire under-reads real spend by that amount.
3. **The throughput guard has now ended three consecutive phases' runs.** Change 3 is written and self-tested
   but has not yet been proved on a run that finishes.
4. **cz_0004 is 429-limited at ~21× the healthy cost** (29,322 tok/row against 1,379) and needs a decision —
   lower PAR, smaller chunks, or a different window — before another attempt. It has now consumed
   875,000 tokens for zero rows in 2F, on top of 2D's and 2E's losses.
5. **Any `STOP_*` file silently downgrades the paid `lk` stage to merge-only**, which is why the 50 recovered
   rows have no dedicated `lk` judgement.
6. **`s04` is still not explained.** Content and encoding are ruled out by measurement; the halves rule out
   "the whole chunk"; what is left is a property of 50 specific rows that no instrument here can see.
7. **`reader_nom` spells Czech `'cz'` and never `'cs'`**; `'cs'` raises `KeyError` inside a bare `except` and
   abstains silently on every row, producing a plausible-looking 100 % abstention.
8. **The AG decision layer below the reader is still Slovak for Czech**: `SK_REFLEX (sa|si)` not `(se|si)`,
   `SK_DEM` Slovak-only (so the TIP determiner rule cannot fire on Czech `tenhle/tahle/tohle`), `SK_PPART`
   and `SK_CONN` Slovak. `cz_reader`'s V2/V3 patches are not in the decision path.
9. **P-FROZEN-1U tells the model "Slovak has no articles" while judging Czech.** Left unchanged deliberately:
   editing it is a stack change.
10. **1W's own cross-phase overlap check was inert.** `assemble_1v.py` derives its root relatively; copied
    into `phase1w/a4/set/` it resolved one level short, and `assemble_1v.json` records
    `earlier_sentences_checked_against: 0`. **The Slovak 1W set was never checked against earlier phases.**
11. **`phase2e/out/GATE3_2e.json|md` are headed "phase 2D … merged `sk` rows" although the data is Czech.**
    Anyone citing the 10.40 % [6.91, 14.87] figure must say so.
12. **Part 3.1's Clopper–Pearson helper was wrong** — an increasing-function bisection on a decreasing
    function, returning degenerate `[0,0]`/`[100,100]` bounds. Found after the run, fixed in the reporting
    layer at 0 calls; the fixed helper reproduces the frozen scorer digit-for-digit on this run and on 1W,
    k/n were never affected, and the published headline is the frozen scorer's. Eighth occurrence.
13. **Part 3.1 spent 312 calls against a declared ~250** — flagged rather than hidden; the hard constraint
    (900 phase-wide) was never at risk.
14. **The seven 1U construction floors cannot hold on production material**; the gate was kept structurally
    with minima at 0 and the real counts reported — a stated deviation, not a tuned gate.
15. **Production rows carry no `topic`;** the probe's packet topic is `type_title`, stated so that 1N's
    dropped-`topic` defect cannot recur silently.
16. **`score_1u.py`'s markdown writer hard-codes S1–S6**, so S7 never renders; the JSON carries it.
17. **8 of 36 duplicate controls landed in the same packet**, so the probe's 0.0 % judge noise is a lower
    bound.

---

## 8. Judgement

1. **Czech does not meet 90 % coverage or 5 % FA, because Czech was not measured.** The set is built,
   annotated and packeted with 0 Gemini calls spent and one opening still available; it died on a judge
   session that read 1.27 M tokens of its own cache.
2. **Where Czech is worse than Slovak is still only known from the older diagnostics**: `agent_nom` 21.05 %
   against 11.63 % and `gender` 19.23 % against 11.63 % (2C) — roughly **1.8× and 1.7×** — and AG v4
   10.40 % [6.91, 14.87] against 10.00 % on a 12 % bar (2E), a gap of 0.4 points that neither interval
   separates.
3. **Production sentences do not behave like test sentences.** Slovak lost **13.14 points of coverage** on
   production material — 84.62 % [78.54, 89.53] against 97.76 % [95.78, 98.97], **disjoint intervals** —
   while FA rose 2.97 points inside overlapping ones. The confound is real and named: production rows carry
   1.1 accepted references against 2.0.
4. **The refused chunk is half diagnosed.** Content and encoding are excluded by measurement, throttling is
   excluded by h1 succeeding first try, and size is excluded by h2 failing at the same size. Fifty specific
   rows are the cause and nothing available here can say why.
5. **Czech finished at 2,850 of 4,064 rows (70.1 %)**, 50 more than 2E, for 1,466,116 tokens — 875,000 of
   which bought nothing on cz_0004.
6. **Ukrainian is cheapest next at 3,890,000 tokens**, because its script makes the reader abstain loudly
   rather than answer wrongly; Spanish is the runner-up and would take the lead if the three raw-string
   vetoes were taught to abstain on an unrecognised script.

---

### Files

`phase2f/`: `PLAN.md` · `STATUS.md` · `SHA_inputs_before.txt` · `CHANGES_2F.md` · `DEFECTS_run_2f_cz.md` ·
`run_2f_cz.py`, `run_2f_lk.py`, `run_part1.py`, `ledger_2f_cz.json`, `run_2f_cz.log`, `run_part1.log` ·
`diag/DIAGNOSIS_s04.md`, `diag/s04_facts.json` · `out/annotations_cz_NNNN.jsonl` + `.meta.json`,
`out/annotations_cz_final.jsonl`, `out/upload_cz_final.xlsx`, `out/REPORT_2f_lk_compare.md`,
`out/sessions/` · `p2/p2_driver.py`, `p2/PART2_RESULT.md`, `p2/set/`, `p2/run/` ·
`p3/PRICING_SIX_LANGUAGES.md` · `p3/probe/PROBE_SLOVAK_PRODUCTION.md`, `probe_result.json`,
`SHA_inputs_p31.txt`. Every file was committed as it was produced. Nothing was pushed.

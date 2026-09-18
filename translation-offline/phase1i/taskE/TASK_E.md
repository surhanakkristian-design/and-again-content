# Task E — prompt variants at L3, and the frozen Phase 1i configuration (DEV only, 18 Sept 2026)

Agent E. Everything below is measured on **DEV** (467 items: 203 correct all judged really correct,
260 judged really wrong) through `phase1i/loader.py`. **The holdout was never opened** — `run_config.py`
exists for it but was run only with `--side dev`.

Files: `pipeline_1i.py` (the pipeline as a wrapper module — `checker_1i.py` was **not** edited),
`taskE/run_e.py` (`--diag` / `--run` / `--score`), `taskE/calls.jsonl` (881 rows, one per call),
`taskE/results.json`, `taskE/diag.json`, `FROZEN_CONFIG.json`, `run_config.py`,
`taskF/dev_verdicts.jsonl` + `taskF/dev_summary.json` (the frozen config re-run end to end).

## 0 Apparatus check first

With **all Phase 1i flags off** (no Task B, no Task C guards, TIP = accept) and the frozen row-7 verdict map
replayed, `pipeline_1i.run_pipeline` reproduces the stored `rows.row7` triple (layer, accepted, verdict) for
**467/467 DEV items**, coverage 160/203 = 78.8 %, FA 30/260 = 11.5 % — byte-identical to the frozen headline.
`run_e.py --score` asserts this before it prints anything.

One bug of my own, found by that check's neighbour: `C.decide()` does **not** return the model label, so my
first TIP-scoring read `d['model']` and got `None` everywhere, which silently made "TIP = reject" identical
to "TIP = accept". The model label is now taken from the verdict map for items that actually reached L3
(`VM` is a dict subclass that records every lookup, which is also how "reaches L3" is decided — 270 items).

## 1 The 145 vs 149 reconciliation — **149 is right**

Row 7 accepts 160 correct answers. **15** of them are accepted `correct_with_tip`, and they split:

| source of the tip | n | ids |
|---|---|---|
| the model said `TIP` at L3 (what Task A's switch re-scores) | **11** | — |
| the tip came from **L2 `f2_equivalent`** (or survived F2B) — no model call decided it | **4** | `C:10734:1211638808`, `C:26084:1366855423`, `C:27097:1143309800`, `C:2783:808267455` |

- rejecting **only an L3 model `TIP`** → 160 − 11 = **149/203** (agent C, and this is what Task A defines:
  "counting an L3 `TIP` as a rejection … a flip of an existing switch");
- rejecting **any `correct_with_tip` verdict** → 160 − 15 = **145/203** (agent B).

Agent B's 145 therefore also throws away four lock-releases that the L3 switch does not touch. Both numbers
are arithmetically right about different rules; the Task A rule gives **149/203 = 73.4 %**, and the FA figure
(8/260 without guards, 6/260 with F4v3) is the same either way, because all four extra rejections are correct
answers. Everything below scores `tip_reject` as **L3 model TIP only**.

## 2 What causes the remaining false rejections at L3 (diagnosis before designing)

Of the 270 DEV items that reach L3 with B+C applied, P-B calls **17 correct answers DIFF**:

| n | cause | example |
|---|---|---|
| **10** | the answer picks the **other gender** than the reference (the annotation has a `g` chain) — usually together with a synonym | `He drops his guidebook…` vs `She'll let her guide…` |
| 5 | **word choice only** — a synonym or a register change (`children/kids`, `beam/ray`, `awake/wake up`) | `The children awake at seven` vs `The kids will wake up at seven a.m.` |
| 1 | a full paraphrase (insert+delete: fronted adjunct) | `At seven in the morning, the children will wake up` |
| 1 | a dropped-word reading of an inversion (`Were the beam weaker…`) | |

So the dominant cause is exactly the one Phase 1h named: `g` reaches F3/F5/F2B but never the prompt. The
second is that the model treats the **reference wording** as the target instead of the Slovak. That fixed the
design of the fourth variant.

## 3 The variants

All inside the frozen call shape: `gemini-3.1-flash-lite`, system instruction `lib_prev.SYS`, one user part,
`temperature 0`, `maxOutputTokens 24`, `thinkingConfig {thinkingBudget: 0}`, one-word answer. Each extra line
is inserted immediately **before** the final question line of the frozen P-B text.

- **P-E1** = P-B + the gender chain, when the annotation has one:
  `Gender: the Slovak does not fix the gender here — the reference's "He", "his" may equally be the other
  gender (he/she, him/her, his/her, himself/herself). An answer that keeps the meaning but picks the other
  gender is SAME on that point.`
  62 of the 270 L3 items have a `g` chain → **199 items got the plain P-B text and their stored Phase 1h
  P-B verdict was reused** (no call); 71 calls were made = the 62 with a `g` chain + 9 L3 items that have no stored P-B verdict at all.
- **P-E2** = binary: question line `SAME or DIFF?` and the system instruction with the TIP sentence removed
  (`Reply with exactly one word: SAME or DIFF. …`). No TIP, so it has one scoring only.
- **P-E3** = P-E1 + `Information: any information in the learner sentence that is not in the Slovak, or in
  the Slovak but not in the learner sentence, makes it DIFF — including a single adverb, particle, place word
  or time word.`
- **P-E4b** (my own design, aimed at cause 2 above, since coverage is the target that is furthest away) =
  P-E1 + the P-C ground-truth line + a boundary: `The SLOVAK sentence is the ground truth and the English
  reference is only one valid rendering of it; judge the learner against the Slovak, not against the
  reference wording.` + `A synonym, a different word order or a different phrasing that keeps the Slovak
  meaning is SAME; a word that changes which thing, person, place, time or quantity the Slovak names is DIFF.`
  The second half is deliberate: Task C showed that 14 of the 21 residual false acceptances are lexical
  substitutions (`stag→elk`, `path→road`, `penalty→foul`), i.e. precisely a change of *which thing* is named,
  so the licence for paraphrase is paid for with an explicit boundary instead of a blanket permission.
  A designed-but-unrun variant `P-E4a` (ground-truth line + the sanctioned alternative renderings) is left in
  `pipeline_1i.py`; the budget went to P-E4b because the false rejections are paraphrases that are *not* in
  the annotation's list, which is what P-E4a would have supplied.

## 4 Results — DEV, full pipeline (Task B always on, Task C guard set varied)

Coverage = accepted of the 203 correct; FA = accepted of the 260 really-wrong; exact 95 % Clopper-Pearson.
**0 failed calls and 0 transport retries in all 881 calls**, so no variant is disqualified by the >2 % rule.

| variant | scoring | guards | coverage | false acceptance | type T |
|---|---|---|---|---|---|
| P-B | TIP=accept | F4v3 | 160/203 = 78.8 % [72.5–84.2] | 28/260 = 10.8 % [7.3–15.2] | 1/67 |
| P-B | TIP=reject | F4v3 | 149/203 = 73.4 % [66.8–79.3] | 6/260 = 2.3 % [0.8–5.0] | 0/67 |
| P-B | TIP=accept | F4v3+F5t+F6 | 157/203 = 77.3 % [71.0–82.9] | 21/260 = 8.1 % [5.1–12.1] | 1/67 |
| P-B | TIP=reject | F4v3+F5t+F6 | 147/203 = 72.4 % [65.7–78.4] | 6/260 = 2.3 % [0.8–5.0] | 0/67 |
| **P-E1** | TIP=accept | F4v3 | 178/203 = 87.7 % [82.4–91.9] | 26/260 = 10.0 % [6.6–14.3] | 1/67 |
| **P-E1** | **TIP=reject** | **F4v3** | **167/203 = 82.3 % [76.3–87.3]** | **5/260 = 1.9 % [0.6–4.4]** | 0/67 |
| P-E1 | TIP=accept | F4v3+F5t+F6 | 175/203 = 86.2 % [80.7–90.6] | 20/260 = 7.7 % [4.8–11.6] | 1/67 |
| P-E1 | TIP=reject | F4v3+F5t+F6 | 165/203 = 81.3 % [75.2–86.4] | 5/260 = 1.9 % [0.6–4.4] | 0/67 |
| P-E2 | (binary) | F4v3 | 168/203 = 82.8 % [76.8–87.7] | 12/260 = 4.6 % [2.4–7.9] | 1/67 |
| P-E2 | (binary) | F4v3+F5t+F6 | 165/203 = 81.3 % [75.2–86.4] | 9/260 = 3.5 % [1.6–6.5] | 1/67 |
| P-E3 | TIP=accept | F4v3 | 150/203 = 73.9 % [67.3–79.8] | 4/260 = 1.5 % [0.4–3.9] | 0/67 |
| P-E3 | TIP=reject | F4v3 | 138/203 = 68.0 % [61.1–74.3] | 4/260 = 1.5 % [0.4–3.9] | 0/67 |
| P-E3 | TIP=accept | F4v3+F5t+F6 | 148/203 = 72.9 % [66.2–78.9] | 4/260 = 1.5 % [0.4–3.9] | 0/67 |
| P-E3 | TIP=reject | F4v3+F5t+F6 | 137/203 = 67.5 % [60.6–73.9] | 4/260 = 1.5 % [0.4–3.9] | 0/67 |
| **P-E4b** | **TIP=reject** | **F4v3** | **175/203 = 86.2 % [80.7–90.6]** | **10/260 = 3.9 % [1.9–7.0]** | **0/67** |
| P-E4b | TIP=accept | F4v3 | 180/203 = 88.7 % [83.5–92.7] | 22/260 = 8.5 % [5.4–12.5] | 1/67 |
| P-E4b | TIP=reject | F4v3+F5t+F6 | 172/203 = 84.7 % [79.0–89.4] | 9/260 = 3.5 % [1.6–6.5] | 0/67 |
| P-E4b | TIP=accept | F4v3+F5t+F6 | 177/203 = 87.2 % [81.8–91.5] | 17/260 = 6.5 % [3.9–10.3] | 1/67 |

Readings:

- **Passing `g` into the prompt is free coverage**: +18 accepted correct answers under TIP=accept
  (160→178) and +18 under TIP=reject (149→167), while FA *falls* (30→26 / 6→5). It is the single best lever
  measured in Phase 1i and it confirms the Phase 1h hypothesis exactly.
- **P-E4b** adds another +8 correct answers on top of P-E1 under TIP=reject (167→175) for +5 FA (5→10).
- **P-E3's information rule is a trap**: it is the lowest FA of all (4/260 = 1.5 %) but it costs 28 correct
  answers against P-E1 (167→138 under TIP=reject) — the model starts calling every re-realisation of an
  adjunct a DIFF. Strictness is available cheaply; coverage is not.
- **P-E2 (binary)** lands between: 168/203 with FA 12/260. Dropping TIP is not as good as keeping TIP and
  rejecting it, because a TIP is informative (it separates "small slip" from "wrong meaning").
- Task C's finding survives the prompt change: **F5t+F6 on top of the TIP switch still buy ~1 FA for 3
  correct answers** (P-E4b: 10→9 FA, 175→172 coverage). F4v3 remains free.
- Type-T FA is **0/67 in every TIP=reject row** and unchanged (1/67) in every TIP=accept row. No prompt
  variant weakened the grammar veto; the veto is offline and none of these lines touches it.

## 5 The frozen configuration (selection rule applied mechanically)

Targets: coverage ≥ 90 %, real FA < 5 %, type-T FA not above the 1.5 % baseline.

1. **Step 1** — configs meeting *both* targets: **0** (the maximum coverage reachable at L3 is
   160 + 17 = 177/203 = 87.2 % under TIP=accept; 43 of the 203 correct answers are lost, and 14 of those are
   lost *before* the model — 12 at the L2 lock, one at F4v2, one at F5 — so no prompt can reach 90 %).
2. **Step 2** — configs with DEV FA < 5 % **and** type-T FA ≤ 1.49 %: **12** of the 18 rows. Highest
   coverage wins: **P-E4b, TIP = reject, guards {F4v3}** — coverage **175/203 = 86.2 % [80.69–90.63]**,
   FA **10/260 = 3.85 % [1.86–6.96]**, T **0/67**.
3. Step 3 was not needed.

**Runner-up: P-E4b, TIP = reject, guards {F4v3, F5t, F6}** — 172/203 = 84.7 %, FA 9/260 = 3.46 %. It loses
step 2 on coverage by 3 answers (84.73 < 86.21). Third was P-E2 (82.8 %, FA 4.6 %), fourth P-E1
(82.3 %, FA 1.9 %) — P-E1 is the pick for anyone who wants margin under the 5 % ceiling rather than coverage,
since its FA point estimate is half the winner's and its upper CI bound (4.4 %) is the only one below 5 %.

Written to `FROZEN_CONFIG.json` (variant, full prompt template with every inserted line, the rendered
example, system instruction, TIP scoring, B flags, C guards, model, generationConfig) and executed by
`run_config.py`.

**`run_config.py --side dev` reproduces it with 0 new model calls** (270 verdicts reused from
`taskE/calls.jsonl`, same variant = byte-identical prompt text): coverage 175/203, FA 10/260, T 0/67 —
see `taskF/dev_summary.json`.

### The winner's residue

False acceptances, 10 — **9 at L3 (all `SAME`)** + 1 at L1: `W:10013:1594646351` (W), `W:14697:2532470414`
(S), `W:14697:567072060` (M), `W:2121:4138132892` (M), `W:2389:1402963517` (S), `W:28006:2654956435` (W),
`W:5959:2145732155` (S), `W:7444:2683969038` (M), `W:7998:52962874` (M), `W:9907:1778280655` (S, L1, the
known writer artefact that is byte-identical to the reference). By type: T 0/67, W 2/69, M 4/56, S 4/68.
By half: OLD 4/138, NEW 6/122. Note that two of them (`W:2121:4138132892`, `W:2389:1402963517`) were
previously `TIP` items — under P-E4b the model upgraded them to `SAME`, which is the price of the
paraphrase licence.

**What is left — the 28 DEV false rejections, by cause:**

| n | layer | cause |
|---|---|---|
| **12** | L2 | the grammar lock fires on a genuine paraphrase of the practised grammar (9 of the 15 are genuine per the phase brief and are to be left alone; the other three are sid 103's data defect). Task B's fix released 4 items but L3 then rejected 3 of them, and 2 of those 3 are *still* rejected here |
| **5** | L3 (TIP re-scored as reject) | the price of the Task A switch: real paraphrases the model flags as a small slip (`There's a long bandage…`, `the seller is dropping…`, `that green overall`, `the whole chair rocks`, `running full speed ahead`) |
| **4** | L3 DIFF | **gender**: the answer swaps he↔she *and* re-words (`C:16261:937570043`, `C:29691:1286045143/2119858295/2714964500`). The gender line moved 18 other items but not these: the sid-29691 answers also change aspect (`drops`→`will let`) and the model reads the pair as a different event |
| 3 | L3 DIFF | **person recast**: the Slovak drops the subject and the answer chooses `you` where the reference has `she` (`C:9907:2336650878/3590124615`), or `it` for `he` (`C:7928:2593205770`) — the same class of problem as `g`, but for *person*, which no annotation field carries |
| 2 | L3 DIFF | synonym + register (`beam→ray`, `blink→flicker`; `awake at seven`→`will wake up at seven`, fronted adjunct) |
| 1 | F4v2 | offline subject mismatch on a correct answer (`C:10116:2497170629`) |
| 1 | F5 | offline adjunct-deletion on a correct answer (`C:14779:188731256`) |

The honest summary of "what is left": **14 of the 28 are not the model's fault at all** (12 L2 + 2 offline
guards), and the single tractable model-side class that remains is the *person/gender recast of a
subjectless Slovak sentence* (7 items) — the natural next step is a `p`-style **person** chain in the
annotation, or an F-layer that tells the prompt which person the Slovak underdetermines.

## 6 Model calls, honesty and cost

**881 counted calls** (P-E1 71, P-E2 270, P-E3 270, P-E4b 270), all **HTTP 200**, all parsed:
**0 failed calls, 0 empty replies, 0 transport retries, http histogram `{200: 881}`**, 4 threads,
`(item, variant)` pairs interleaved and shuffled with a fixed seed exactly as Task D requires, so no
variant or kind could be hit selectively by an outage. Budget 1,300 → 881 used, **419 left** and the
holdout needs ~290. Phase total spent after Task E: 34 + 881 = 915 of 2,500. 199 P-E1 verdicts were
**reused** from the frozen Phase 1h P-B ledger because their P-E1 prompt text is byte-identical to P-B
(no `g` chain). The ledger `taskE/calls.jsonl` carries one row per call with item id, variant, http,
counted, the raw reply, `finishReason`, latency and usage. No key was printed, logged or put on a command
line.

## 7 Overfitting disclosure and what the holdout can still measure

The gender line is driven by the annotation's own `g` field, the ground-truth and boundary lines contain **no
content word from any DEV item**, and nothing is keyed to a sid — so all of it is measurable on the holdout
despite the leakage caveat (138 of 140 sids have items on both sides). What *was* chosen on DEV is the
selection among four variants and two guard sets, i.e. **one choice out of 18 rows**; the winner's DEV
coverage (86.2 %) and FA (3.9 %) are therefore mildly optimistic, and the two sides are already 6.5 pp apart
on row-7 coverage by chance alone. The holdout number is the one to quote.

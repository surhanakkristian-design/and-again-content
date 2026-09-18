# Translation offline — Phase 1f report

Date: 18 September 2026. Model: `gemini-3.1-flash-lite`. Sample: 235 correct answers + 105 wrong
answers (the frozen Phase 1e set). Four offline fixes (F1 verb-lock loosening, F2 structure-avoidance
veto drop, F3 deletion guard, F4 subject guard) crossed with the two prompt variants P-B and P-C —
32 combinations, all tabulated. Data files: `translation-offline/phase1f/`.

---

## 1. The exact recount of the 48 L2 vetoes

Phase 1e §2.2 estimated the composition of the 48 correct items that were routed to L2
(~17 different-verb / ~10 string artefacts / 4 article-quantifier / ~18 different grammar = 49, i.e.
the estimate over-counted by one). The exact recount (`veto_recount.json`, `totals`) sums to 48:

| category | n |
|---|---|
| different_verb (a different but equivalent verb inside the locked span) | 16 |
| avoids_structure (the practised structure replaced by an equivalent one) | 15 |
| string_artefact (the structure is present, the lock string is not matched literally) | 10 |
| article_quantifier (determiner / quantifier alternative) | 4 |
| other | 3 |
| **total** | **48** |

Sub-split of the 10 string artefacts:

| sub-type | n |
|---|---|
| contraction (`she'd taken`, `it's said`, `she's dancing`, `he'd turned`) | 4 |
| gap lock (`had the kitchen filmed` vs the lock `had .. filmed`) | 2 |
| adverb inserted inside the locked span (`has finally stamped`, `has completely gone out`) | 2 |
| pronoun inside the locked span (`has he been tapping`, `Had he set off`) | 2 |

The 3 "other", named:

- `C:7558:2926388663` — vetoed by the mistake library (step = mistake, auxiliary tense), not by a lock;
  F1/F2 never see it.
- `C:23669:2842578131` — non-verb lexical lock: `over` for the preposition lock `above`.
- `C:10107:4080641578` — non-verb lexical lock: `nevertheless` for the linker lock `even so`.

---

## 2. The ablation table

Two baselines must not be confused. The brief's **76.6 %** figure is Phase 1e's **P-A** row
(180/235). The baseline this phase reproduces exactly is **P-B with no flags: 177/235 = 75.3 %,
FA raw 22 / real 13**. All rows below are measured against that P-B row.

Rule from the brief, applied literally: **a configuration above 2 % real false acceptance (more than
2 of 105) is not a candidate, however high its coverage.**

| row | variant | flags | coverage /235 | by level (A1/A2/B1/B2) | accepted correct / with tip | FA real /105 | FA by type real (raw) | L1/L2/L3 correct (F3/F4 kills) | regressions vs P-B |
|---|---|---|---|---|---|---|---|---|---|
| Phase 1e baseline | P-B | — | 177 (75.3 %) | 25/36 69.4 % · 41/48 85.4 % · 62/82 75.6 % · 49/69 71.0 % | 169 / 8 | 13 (12.4 %) | M 11, S 2 (raw M 13, T 6, S 3) | 100/48/87 (0/0) | — |
| +F1 | P-B | F1 | 203 (86.4 %) | 28/36 77.8 % · 43/48 89.6 % · 69/82 84.1 % · 63/69 91.3 % | 193 / 10 | 14 (13.3 %) | W 2, M 11, S 2 (raw M 13, T 6, W 2, S 3) | 100/18/117 (0/0) | 0 correct lost, 2 new FA (a) |
| +F2 | P-B | F2 | 193 (82.1 %) | 25/36 69.4 % · 43/48 89.6 % · 69/82 84.1 % · 56/69 81.2 % | 169 / 24 | 13 (12.4 %) | M 11, S 2 (raw M 13, T 6, S 3) | 100/31/104 (0/0) | none |
| +F3 | P-B | F3 | 177 (75.3 %) | 25/36 69.4 % · 41/48 85.4 % · 62/82 75.6 % · 49/69 71.0 % | 169 / 8 | 7 (6.7 %) | M 5, S 2 (raw M 6, T 6, S 3) | 100/48/87 (14/0) | none |
| +F4 | P-B | F4 | 176 (74.9 %) | 25/36 69.4 % · 41/48 85.4 % · 61/82 74.4 % · 49/69 71.0 % | 169 / 7 | 11 (10.5 %) | M 11 (raw M 13, T 6, S 1) | 100/46/86 (0/13; 3 correct killed) | 1 correct lost: `C:9498:362699013` |
| F1+F2 | P-B | F1F2 | 217 (92.3 %) | 28/36 77.8 % · 45/48 93.8 % · 76/82 92.7 % · 68/69 98.6 % | 193 / 24 | 14 (13.3 %) | W 2, M 11, S 2 (raw M 13, T 6, W 2, S 3) | 100/3/132 (0/0) | 0 correct lost, 2 new FA (a) |
| all four | P-B | F1F2F3F4 | 214 (91.1 %) | 28/36 77.8 % · 45/48 93.8 % · 73/82 89.0 % · 68/69 98.6 % | 193 / 21 | 6 (5.7 %) | W 2, M 5 (raw M 6, T 6, W 2, S 1) | 100/3/129 (14/13; 3 correct killed by F4) | 1 correct lost: `C:9498:362699013`; 2 new FA (a) |
| all four with P-C | P-C | F1F2F3F4 | 219 (93.2 %) | 30/36 83.3 % · 46/48 95.8 % · 75/82 91.5 % · 68/69 98.6 % | 204 / 15 | 8 (7.6 %) | W 2, M 6, S 1 (raw M 7, T 6, W 2, S 2) | 100/3/129 (14/13; 3 correct killed by F4) | 1 correct lost: `C:9498:362699013`; 4 new FA (b) |
| best found — lowest real FA | P-B | F2F3F4 | 190 (80.9 %) | 25/36 69.4 % · 43/48 89.6 % · 66/82 80.5 % · 56/69 81.2 % | 169 / 21 | 5 (4.8 %) | M 5 (raw M 6, T 6, S 1) | 100/31/101 (14/13; 3 correct killed by F4) | 1 correct lost: `C:9498:362699013`; 0 new FA |

Regression id lists referenced above:

- (a) new false acceptances of every F1 row: `W:3603:1489926651` (judged **not real** in this phase —
  "take it back to the garage" is an ordinary rendering of *privezie späť*), `W:1452:1471817457`
  (**real** — *touches → grabs*).
- (b) new false acceptances of all four × P-C: the two in (a) plus `W:14266:2043261128` (real, the
  short answer *Salsa* untranslated) and `W:10366:36005249` (real, *they* for singular *bude*).
- The only lost correct answer anywhere in the grid is `C:9498:362699013`, killed by F4 (see §4).

Coverage gains against the P-B baseline, for orientation: +F1 +26 correct, +F2 +16, F1+F2 +40,
all four +38 (−1 lost), all four × P-C +43 (−1 lost), F2F3F4 +14 (−1 lost). Wrong-set items that the
offline guards remove: F3 kills 7 that were being accepted, F4 kills 2 that were being accepted.

**No row qualifies.** The lowest real false acceptance measured anywhere in the 32 combos is
**5/105 = 4.8 %** (F2F3F4 × P-B, coverage 190/235 = 80.9 %) — still more than double the 2 % ceiling.
The highest coverage measured is **222/235 = 94.5 %** (F1F2 and F1F2F3 with P-C), at real FA 17
(16.2 %) and 11 (10.5 %) respectively. Neither is a candidate, and no configuration is recommended
on this evidence.

---

## 3. "Best safe configuration"

**None is safe by the 2 % rule.** The closest rows, in full:

**all four × P-B (F1F2F3F4)**

- coverage 214/235 = 91.1 % — A1 28/36 (77.8 %), A2 45/48 (93.8 %), B1 73/82 (89.0 %), B2 68/69 (98.6 %)
- accepted correct 193, accepted with tip 21
- real false acceptance 6/105 = 5.7 %; raw FA 15 (raw by type M 6, T 6, W 2, S 1). The script's
  real-by-type block reads `{"W": 2, "M": 5}` = 7 entries against 6 counted real items: the block was
  built before `W:3603:1489926651` flipped to "not real" in the judgement pass, so one W entry there
  is no longer counted as real. The same off-by-one applies to every real-by-type block in this
  report; the `fa_real` counts are the authoritative ones.
- routing of the correct answers: L1 100, L2 3, L3 129; F3 kills 0 correct, F4 kills 3 correct
- regressions vs P-B: 1 correct lost (`C:9498:362699013`), 2 new FA (1 real)
- latency of the model layer (whole 1f run, 252 calls): median 865 ms, p95 1193 ms
- cost per active user per month, 1e formula (20 exercises/day × 30 days × the best row's L3 share of
  the correct-answer distribution 0.43; Flash-Lite $0.25 in / $1.50 out / $0.025 cached per 1M):
  **$0.0118** ($0.01180559 in the cost block; $4.5780754e-05 per call, 177.1 input tokens and
  1.0 output token per call on average)

**No row in the 32 combos dominates it.** F4 is net-negative in isolation (§4), so the natural
alternative is dropping it:

**F1F2F3 × P-B — the best trade-off available without F4**

- coverage 217/235 = 92.3 % (+3 vs all four) — A1 28/36, A2 45/48, B1 76/82, B2 68/69
- real false acceptance 8/105 = 7.6 % (+2 vs all four) — by type real: W 2, M 5, S 2; raw 17
  (M 5+1, T 6, W 2, S 2 — raw block `{"W": 2, "M": 5, "S": 2}` real over raw 17)
- routing: L1 100, L2 3, L3 132; no correct answer killed by any offline guard (0 regressions except
  the 2 new FA of F1)
- same latency and cost figures as above (the L3 volume is 132 instead of 129, i.e. marginally higher)

So dropping F4 buys back the 3 wrongly rejected correct answers and +3 coverage, and pays with the
2 S-type false acceptances F4 was catching. It is better on coverage and on regressions, worse on
safety; by the 2 % rule both fail.

---

## 4. What F3 and F4 cost on the correct answers

**F3 (deletion guard) — cost on the 235: 0.** No correct answer is rejected by F3 in any of the 32
rows (`f3_f4_offline.F3.cost_on_235.total = 0`; the `layers_correct` blocks of the F3 rows contain no
F3 bucket). Its effect on the 105 wrong answers: 14 kills, of which 7 were previously being accepted
(`W:11980:982093953`, `W:1452:2457679986`, `W:5595:1942575047`, `W:9244:3534999071`,
`W:4571:2387652990`, `W:3494:2082147100`, `W:8209:2200603079`) and 7 were already rejected. All 7
"real savings" are M-type omissions; six are judged real in this phase, the seventh
(`W:5595:1942575047`) Phase 1e had already classed as a valid reading. F3 is therefore free on this
sample and its only questionable kill is the item 1e considered acceptable.

Verb particles are treated as function words by F3 on purpose: the guard's content-word test uses the
function/adverb tables, and particles (`up`, `back`, `in`, `off`) sit there together with prepositions
and adverbs, because in the corrections direction a missing particle is usually a spelling-level
difference rather than lost content. That decision is exactly what makes F3 miss the adjunct
omissions listed in §5 (*up now*, *by now*, *completely*) — the leak is the word-class table, not the
subsequence test.

**F4 (subject guard) — cost on the 235: 3, all three wrong, all in one exercise (C:9498).**

| item | answer vs reference | kill wrong? |
|---|---|---|
| `C:9498:3533979063` | *he is standing behind* vs *she is standing behind* | yes |
| `C:9498:362699013` | *that he's standing behind* vs *that she is standing behind* | yes |
| `C:9498:582627860` | *he stands behind* vs *she is standing behind* | yes for the gender reason (the answer is separately weak: simple for continuous) |

The Slovak is *Pult, za ktorým stojí, je starší než celá škola* — *stojí* marks 3rd person singular
and no gender, so *he* is legitimate. **The defect: the guard reads person/gender off the English
reference pronoun although the brief says the Slovak decides.** That is an implementation defect of
this phase, not a property of the idea. It was not fixed because the frozen run was already tabulated
when the judgement pass found it; F4's abstention logic must derive person/number/gender from the
Slovak verb morphology and stay silent when the ending is ambiguous. F4's gain on the 105: 13 S-type
kills, 2 of which were being accepted (`W:4571:4142535241` *I* for *you*, `W:3494:4150910632` *they*
for *she*, both real). Net on this sample: 2 real FA saved against 3 correct answers wrongly rejected
— net-negative as implemented.

---

## 5. Every remaining false acceptance and every remaining false rejection

Judgement pass: the 18 wrong-set items accepted in at least one of the 32 rows and carrying no Phase
1e judgement were judged individually (`judgements_1f.json`): **17 real, 1 not real**. Rule used: the
Slovak is the ground truth; an answer that omits a content element of the Slovak, or swaps the subject
the Slovak verb ending fixes, is not acceptable; doubt resolved as "real". Type key: T tense, W wrong
word, M missing content, S wrong subject.

### 5.1 False acceptances — all four × P-B: 15 raw, 6 real

| item | type | why accepted / judgement | source |
|---|---|---|---|
| `W:3603:1489926651` | W | **not real** — *taking* for *privezie späť* is an ordinary rendering, reported-speech backshift intact | 1f |
| `W:4612:586139873` | M | **real** — drops *už dávno* / *by now*, the time reference carrying the counterfactual | 1f |
| `W:9907:325819033` | M | **real** — drops the subject noun *look* of the result clause | 1f |
| `W:11348:2987233244` | M | **real** — drops *hore* and *práve* (*up now*) | 1f |
| `W:1452:1471817457` | W | **real** — *grabs* for *dotkne sa*: a different event in the conditional | 1f |
| `W:7238:1943930546` | M | **real** — intensifier *úplne* / *completely* omitted | 1f |
| `W:8824:1740944184` | M | **real** — *na miesto* / *into place* gone, the result of *dotlačil* | 1f |
| `W:16403:624976382` | M | 1e: tip-accept, counted **not real** — but see the dissent below | 1e |
| `W:1018:1251085634` | T | 1e tip-accept (*poured* for *has poured*), not real | 1e |
| `W:14266:664063167` | T | 1e valid reading (*are dancing* for *do they dance*), not real | 1e |
| `W:1452:3166274700` | S | 1e valid reading — agreed: Slovak 3sg carries no gender here | 1e |
| `W:5595:3623849236` | T | 1e tip-accept (*stamped* for *has stamped*), not real | 1e |
| `W:9244:3038274947` | T | 1e tip-accept (*rolled in* for *were rolling in*), not real | 1e |
| `W:8824:241327957` | T | 1e tip-accept (*swung* for *was swinging*), not real | 1e |
| `W:10366:3357618811` | T | 1e tip-accept (*will have reheated* for *will have been reheating*) — see the dissent | 1e |

(The ninth 1e "not real" item, `W:5595:1942575047`, is killed by F3 in this row, which is why 15 raw
and not 16.)

**What P-C changes:** P-C accepts the same 15 **plus 2 more real ones** — `W:14266:2043261128` (M, the
short answer after the dash is untranslated; DIFF at P-B) and `W:10366:36005249` (S, *they* for the
singular *bude*; DIFF at P-B). P-C's "judge against the Slovak, not the reference" line buys +5
correct answers and pays with exactly these 2 real false acceptances (17 raw / 8 real).

For the F1+F2 row (24 raw / 14 real) the extra 9 over the all-four row are precisely what F3+F4
remove: `W:11980:982093953`, `W:1452:2457679986`, `W:9244:3534999071`, `W:4571:2387652990`,
`W:4571:4142535241`, `W:3494:2082147100`, `W:3494:4150910632`, `W:8209:2200603079` (+
`W:5595:1942575047`, the 1e "valid reading").

**Why the offline guards missed the remaining real ones** (all four × P-B): `W:4612:586139873`,
`W:11348:2987233244`, `W:7238:1943930546` — the deleted tokens (*by now*, *up now*, *completely*) are
all in the function/adverb table, so F3's content-word test does not fire. `W:9907:325819033` — the
content noun is deleted mid-sentence and the determiner *this* survives, which keeps the pattern out
of F3's trailing-deletion shape. `W:8824:1740944184` — *into place* is deleted at the tail and *place*
is a content word: a genuine F3 gap worth re-reading in code. `W:1452:1471817457` — lexical
substitution with no deletion and no subject change; an offline guard would need a
content-verb-substitution test, which F1/F2 deliberately allow (different-verb paraphrase is the main
F1/F2 gain). At P-C additionally: `W:14266:2043261128` — the missing chunk is a whole unit after the
dash, not a token deletion inside one sentence; `W:10366:36005249` — the Slovak drops the pronoun
(person/number live in *bude*), so F4 abstained.

### 5.2 Judge's dissent on the frozen 1e classifications

The judgement pass disagrees with **2 of the 9** Phase 1e "not real" classifications:

- `W:16403:624976382` — *and she comes back in an hour* for *…will come back*.
- `W:10366:3357618811` — *he will have reheated* for *he will have been reheating* (the exercise
  practises the future perfect continuous and the Slovak is explicit: *bude zohrievať … dve hodiny v
  kuse*).

Both were **left unchanged** (frozen 1e data). Under the stricter reading, every real-FA figure in
this report is **2 higher** — e.g. all four × P-B would be 8/105 = 7.6 % instead of 6/105 = 5.7 %.

### 5.3 False rejections — all four × P-B rejects 21/235; P-C rejects 16/235

No item is lost by P-C (P-C-only rejections: none); the 5 marked RESCUE are rejected at P-B and
accepted at P-C.

| item | lvl | killed by | P-C | judgement |
|---|---|---|---|---|
| `C:16261:2683737001` | A2 | model DIFF | — | defensible: the walker is made female, *her* then has no distinct referent |
| `C:16403:2761099319` | A2 | model DIFF | — | defensible: *o hodinu* dropped |
| `C:21124:681157260` | A2 | model DIFF | RESCUE | true miss: closer to the Slovak than the reference is |
| `C:23669:2842578131` | A1 | L2 veto kept (lock *above*) | — | true miss on wording; *over* is fine, the present continuous for a stative reading is the questionable part |
| `C:26084:1225655220` | A1 | model DIFF | — | defensible: subject of the *before* clause changed |
| `C:26084:2889436188` | A1 | L2 veto kept (lock *can*) | — | defensible: *be able to* avoids the practised *can*, plus the same subject slip |
| `C:26084:3073504942` | A1 | model DIFF | — | defensible: *ju* is feminine animate, *it* is wrong |
| `C:27628:2910266109` | A1 | model DIFF | RESCUE | true miss: *zobudia sa* is perfective, the future reading is licensed |
| `C:27628:3492027817` | A1 | model DIFF | — | true miss — the **same answer as the rescued one minus "o'clock"**; P-C rescues one and not the other, i.e. model noise |
| `C:29691:2402977996` | A1 | model DIFF | — | defensible: *going to* is a prediction, the item practises the dramatic present |
| `C:29691:455389026` | A1 | model DIFF | RESCUE | true miss: *pustí* is perfective present = future |
| `C:5595:3589927967` | B1 | L2 veto kept (lock *has stamped*) | — | true miss: the present perfect is there, the lock string is broken only by the inserted *finally* |
| `C:5595:3701842021` | B1 | L2 veto kept (lock *has stamped*) | — | true miss on grammar; defensible on lexis (*put a stamp on*) |
| `C:5959:1797630685` | B1 | L2 veto kept (lock *will drop*) | RESCUE | true miss: first conditional intact, *lower* = *zníži* |
| `C:5959:378048785` | B1 | L2 veto kept (lock *will drop*) | — | true miss: same structure, only synonyms differ |
| `C:7558:2926388663` | B2 | L2 veto kept (mistake library: auxiliary tense) | — | defensible-to-true-miss: inversion is practised and present; perfect vs past perfect is acceptable for a bare Slovak past, the library rule is too hard here |
| `C:8293:1872525904` | B1 | model DIFF | RESCUE | true miss: the Slovak gives no gender, and *croissant* is nearer the Slovak than the reference |
| `C:9244:3137708535` | B1 | L2 veto kept (lock *were rolling*) | — | defensible: the practised past continuous is genuinely replaced by a past simple |
| `C:9498:3533979063` | B1 | **F4** | — | true miss: *stojí* is 3sg with no gender, *he* is legitimate → F4 wrong |
| `C:9498:362699013` | B1 | **F4** | — | true miss, same reason (also the only `lost_correct` vs the F1+F2 row) |
| `C:9498:582627860` | B1 | **F4** | — | defensible on aspect, but the F4 kill is for the wrong reason (gender) |

Pattern: 7 of the 21 are L2 vetoes that F1/F2 kept (all lock-string or mistake-library artefacts on
answers whose grammar is actually present), 11 are model DIFF at L3, 3 are F4. The A1 perfective-
present → *will* family (C:27628, C:29691) is the biggest true-miss cluster, and P-C only half-fixes
it — model noise rather than a rule difference (see the C:27628 pair above).

---

## 6. Model calls

| stage | variant | needed | called | parsed | reused from the 1e ledger | failed | 429s | attempts after |
|---|---|---|---|---|---|---|---|---|
| calls_P-B | P-B | 198 | 54 | 54 | 144 | 0 | 0 | 54 |
| calls_P-C | P-C | 198 | 198 | 198 | 144 | 0 | 0 | 252 |

**252 HTTP attempts of the 1,200 cap** (54 new P-B + 198 P-C). The 144 reused P-B verdicts come from
the Phase 1e ledger with an identical prompt, so they are not re-called. Failed or unparsable: **0**.
429s: **0**.

Spend: the run was on the free tier, so **$0 billed** (`measured_spend_usd: null`,
"free tier: $0 billed"). List-price equivalent at the brief's Flash-Lite prices
($0.25 in / $1.50 out / $0.025 cached per 1M): **$4.5780754e-05 per call × 252 = $0.0115** total,
on 177.1 input / 1.0 output / 0 thought / 0 cached tokens per call. Latency: median 865 ms,
p95 1193 ms. Projected product cost: **$0.0118 per active user per month** (1e formula, L3 share
0.43).

**Planner defect fixed.** The runner now declares explicit stages, plans the call list from the needed
set rather than from the full grid, stops before calling when the plan would exceed the cap, and
writes timestamped mode-`x` results files so nothing is overwritten. Results files produced:

- `results_calls_P-B_20260918T143449Z.md` / `.json`
- `results_calls_P-C_20260918T143747Z.md` / `.json`
- `results_tabulate_20260918T143201Z.md` / `.json` (first tabulation, pre-P-C)
- `results_tabulate_20260918T143748Z.md` / `.json` (post-P-C, pre-judgement)
- `results_tabulate_20260918T144536Z.md` / `.json` (**final**, includes the judgements)
- `run_all_20260918T143359Z.log`, plus `calls.jsonl`, `decisions.jsonl`, `judgements_1f.json`,
  `veto_recount.json`, `tokens.json`, `latest.txt`

---

## 7. Own tokens per agent

| agent | tokens | tool calls | note |
|---|---|---|---|
| builder | 131,041 | 14 | **over the 12-call limit by 2** — extra fix cycles for the F1 particle locks and the F4 diacritics |
| judgement | 70,089 | 10 | within limit |
| report (this file) | see `tokens.json` | — | — |
| main session | — | 8 or fewer | — |

Harness figures for the remaining agents: report agent 59,039 tokens / 10 tool calls; main session 7 tool calls.

`tokens.py --session ab7a2cf3-1cfe-4f5d-b78f-695fb69efef9` (corrected method; taken before the final commit call, so that call is not included):

```
untagged       calls=  30 in=     60 cc=   302667 cr=   1582821 out= 121423 total=   2006971 start=[12845, 11888, 14948]
main           calls=   7 in=     14 cc=    56975 cr=    551087 out=  19889 total=    627965 start=71411
TOTAL {'input': 74, 'cache_creation': 359642, 'cache_read': 2133908, 'output': 141312, 'total': 2634936, 'calls': 37, 'share_pct': {'input': 0.0, 'cache_creation': 13.6, 'cache_read': 81.0, 'output': 5.4}}
```

Process incidents, recorded for honesty:

- (a) During the data peek the builder imported `run_phase1e` and called its `routing()`, which
  rewrote `phase1e/decisions.jsonl` (454 → 340 lines). It was restored from git HEAD (454 lines)
  before the 1f run started; Phase 1e data is otherwise untouched.
- (b) A first `tokens.py` call without `--session` measured the Phase 1c session; that figure was
  discarded.

---

## 8. Judgement

1. Does this reach 90 % coverage at under 2 % false acceptance? Coverage yes — 214/235 = 91.1 %
   (all four × P-B), 217/235 = 92.3 % (F1F2F3 × P-B), 219/235 = 93.2 % (all four × P-C); false
   acceptance no — 6/105 = 5.7 %, 8/105 = 7.6 % and 8/105 = 7.6 % respectively, against a 2/105
   ceiling, and the lowest value anywhere in the 32 combos is 5/105 = 4.8 %.
2. F1 (verb-lock loosening) carried the most weight for coverage: 177 → 203 on its own (+26), and F2
   added +14 on top of F1 (203 → 217); F3 carried safety: real false acceptance 13 → 7 at zero cost on
   the 235.
3. F4 as implemented is net-negative (2 real saves against 3 wrongly rejected correct answers) and
   must be rebuilt so that person/number/gender come off the Slovak verb ending, with silence when the
   ending is ambiguous.
4. What is left: 11 of the 14 real false acceptances in the F1+F2 row and 5 of the 6 in the all-four
   row are omissions of a single adjunct (*by now, up, completely, into place, a minute, at the studio,
   with empty pockets*) — the answer is a strict subsequence of a correct translation, so every
   semantic layer reads it as "same, just shorter", and F3 misses them because the omitted token sits
   in the function/adverb table.
5. The one offline rule worth testing next: an adjunct-deletion rule — if the normalised answer is a
   pure subsequence of the reference and the deleted span carries any of the sentence's stated time /
   place / manner / measure information (including function-class adverbs and particles, and any
   dropped clause after a dash), reject regardless of word class.

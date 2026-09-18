# Translation offline checking — Phase 1g report

18 Sept 2026. Model: `gemini-3.1-flash-lite`, no thinking, 24 output tokens, replies SAME/TIP/DIFF.
Frozen sets: 235 correct answers, 105 wrong answers. Authoritative run:
`phase1g/results_20260918T152458Z.md` / `.json` (earlier timestamps in the folder are superseded).
No DB write, no deploy, nothing committed.

---

## 1. Ablation table

All rows use the same ledger, so they are directly comparable. Rows 1–3 change exactly one thing against
row 0; rows 4–6 are the pairwise combinations; row 7 is all three new rules; row 8 is row 7 with prompt P-C.

LENIENT = the 9 items Phase 1e classed "not real" stay not real. STRICT = the two disputed items
`W:16403:624976382` and `W:10366:3357618811` are counted as real false acceptances.
**Judge by the STRICT column.** Intervals are exact 95 % Clopper–Pearson on n = 105.

| row | variant | flags | coverage /235 | A1 · A2 · B1 · B2 | correct/tip | FA raw | FA lenient (95 % CP) | FA strict (95 % CP) | L1/L2/L3 correct | lost correct vs row 0 | new FA vs row 0 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [0] Phase 1f all four (F1F2F3F4) | P-B | F1F2F3F4 | 214 (91.1 %) | 77.8 · 93.8 · 89.0 · 98.6 | 193 / 21 | 15 | 6 = 5.7 % (2.1–12.0) | 8 = 7.6 % (3.4–14.5) | 100/3/129 | 0 | 0 |
| [1] +F5 only | P-B | F1F2F3F4F5 | 211 (89.8 %) | 77.8 · 91.7 · 86.6 · 98.6 | 190 / 21 | 10 | 1 = 1.0 % (0.0–5.2) | 3 = 2.9 % (0.6–8.1) | 98/3/128 | 3 | 0 |
| [2] F4v2 replaces F4 only | P-B | F1F2F3F4v2 | 217 (92.3 %) | 77.8 · 93.8 · 92.7 · 98.6 | 193 / 24 | 15 | 6 = 5.7 % (2.1–12.0) | 8 = 7.6 % (3.4–14.5) | 100/3/132 | 0 | 0 |
| [3] +F2 boundary only | P-B | F1F2F3F4F2B | 214 (91.1 %) | 77.8 · 93.8 · 89.0 · 98.6 | 193 / 21 | 13 | 5 = 4.8 % (1.6–10.8) | 6 = 5.7 % (2.1–12.0) | 100/3/129 | 0 | 0 |
| [4] F5 + F4v2 | P-B | F1F2F3F4v2F5 | 214 (91.1 %) | 77.8 · 91.7 · 90.2 · 98.6 | 190 / 24 | 10 | 1 = 1.0 % (0.0–5.2) | 3 = 2.9 % (0.6–8.1) | 98/3/131 | 3 | 0 |
| [5] F5 + F2 boundary | P-B | F1F2F3F4F5F2B | 211 (89.8 %) | 77.8 · 91.7 · 86.6 · 98.6 | 190 / 21 | 9 | 1 = 1.0 % (0.0–5.2) | 2 = 1.9 % (0.2–6.7) | 98/3/128 | 3 | 0 |
| [6] F4v2 + F2 boundary | P-B | F1F2F3F4v2F2B | 216 (91.9 %) | 77.8 · 93.8 · 91.5 · 98.6 | 193 / 23 | 13 | 5 = 4.8 % (1.6–10.8) | 6 = 5.7 % (2.1–12.0) | 100/3/131 | 0 | 0 |
| **[7] all three new × P-B** | P-B | F1F2F3F4v2F5F2B | **213 (90.6 %)** | 77.8 · 91.7 · 89.0 · 98.6 | 190 / 23 | 9 | 1 = 1.0 % (0.0–5.2) | **2 = 1.9 % (0.2–6.7)** | 98/3/130 | 3 | 0 |
| **[8] all three new × P-C** | P-C | F1F2F3F4v2F5F2B | **218 (92.8 %)** | 83.3 · 93.8 · 91.5 · 98.6 | 201 / 17 | 10 | 2 = 1.9 % (0.2–6.7) | **3 = 2.9 % (0.6–8.1)** | 98/3/130 | 3 | 1 |

Row 0 reproduces Phase 1f **exactly**: 214/235, FA raw 15, FA real 6, 193/21 (checked by the script on every
run).

### False acceptance by wrong-type and by layer

| row | raw by type | lenient real (layer) | strict real (layer) |
|---|---|---|---|
| [0] | 15 (documented per type in `results_*.json`, key `fa_by_type_raw`) | 6 | 8 |
| [7] | T 5 · W 2 · M 1 · S 1 | 1 — `W:1452:1471817457` (L3) → L1 0 / L2 0 / L3 1 | 2 — + `W:16403:624976382` (L1) → L1 1 / L2 0 / L3 1 |
| [8] | T 5 · W 2 · M 1 · S 2 | 2 — `W:1452:1471817457`, `W:10366:36005249` (both L3) → L1 0 / L2 0 / L3 2 | 3 — + `W:16403:624976382` (L1) → L1 1 / L2 0 / L3 2 |

Raw FA per row: 9 of the raw items on the wrong set are L1 checker verdicts (7) and L3 model verdicts (2) in
row 7. The full per-row type and layer breakdowns for rows 1–6 are in
`results_20260918T152458Z.json` (`fa_by_type_raw`, `fa_lenient_by_type`, `fa_strict_by_type`,
`fa_lenient_ids`, `fa_strict_ids`).

### Kills of each offline guard (correct set / wrong set)

| row | F1 | F2 | F3 | F4 | F4v2 | F5 | F2B | L2 vetoes |
|---|---|---|---|---|---|---|---|---|
| [0] | 0/0 | 0/0 | 0/14 | 3/13 | — | — | — | 3/29 |
| [1] | 0/0 | 0/0 | 0/14 | 3/13 | — | 3/9 | — | 3/28 |
| [2] | 0/0 | 0/0 | 0/14 | — | **0/4** | — | — | 3/30 |
| [3] | 0/0 | 0/0 | 0/14 | 3/13 | — | — | 0/2 | 3/29 |
| [4] | 0/0 | 0/0 | 0/14 | — | 0/4 | 3/9 | — | 3/29 |
| [5] | 0/0 | 0/0 | 0/14 | 3/13 | — | 3/9 | 0/1 | 3/28 |
| [6] | 0/0 | 0/0 | 0/14 | — | 0/4 | — | 1/2 | 3/30 |
| [7] | 0/0 | 0/0 | 0/14 | — | 0/4 | 3/9 | 1/1 | 3/29 |
| [8] | 0/0 | 0/0 | 0/14 | — | 0/4 | 3/9 | 1/2 | 3/29 |

Row 7 / 8 killed ids: F4v2 wrong `W:24733:1241921530, W:4571:4142535241, W:7238:1682434805,
W:3494:4150910632`; F5 correct `C:9992:718425012, C:11348:1001085647, C:9244:3704016824`, wrong
`W:4612:586139873, W:9907:325819033, W:14266:2043261128, W:13034:3189180205, W:11348:2987233244,
W:7238:1943930546, W:8824:1740944184, W:6830:3231772199, W:2874:2767368491`; F2B correct
`C:9498:582627860`, wrong `W:10366:3357618811` (row 8 also `W:8799:3574654489`).

### Regressions vs row 0 (ids)

- [1] correct newly rejected `C:11348:1001085647, C:9244:3704016824, C:9992:718425012`; wrong newly rejected
  `W:11348:2987233244, W:4612:586139873, W:7238:1943930546, W:8824:1740944184, W:9907:325819033`; wrong newly
  accepted: none.
- [2] none at all (after the Task 1 fix F4v2 is cost-free on this sample).
- [3] / [6] correct newly rejected: none; wrong newly rejected `W:10366:3357618811, W:4612:586139873`.
- [7] correct newly rejected `C:11348:1001085647, C:9244:3704016824, C:9992:718425012`; wrong newly rejected
  `W:10366:3357618811, W:11348:2987233244, W:4612:586139873, W:7238:1943930546, W:8824:1740944184,
  W:9907:325819033`; wrong newly accepted: none.
- [8] same as [7] plus one **wrong newly accepted: `W:10366:36005249`** (P-C says SAME where P-B said DIFF).

### Two limits that must be read with the table

**2 % is not measurable here.** At n = 105 one case is 0.95 pp, and the exact interval for 2/105 is
0.2–6.7 %. No row in this table can be declared to meet or to fail a 2 % target; the table only orders the
rows relative to each other.

**Honesty note.** F5, F4v2 and the F2 boundary were designed after looking at the same frozen 105/235 they
are measured on. The gains are therefore in-sample and probably optimistic: the rules were shaped by the
very errors they remove. Only a fresh, unseen sample can confirm them. The Task 1 fix was likewise found on
this sample, although it is a general apparatus fix, not an id-specific one.

---

## 2. F5's measured cost on the 235, on its own

F5 deletes-adjunct detection kills **3** correct answers (all three were being accepted before F5):

| id | level | Slovak | reference | answer | deleted span | judgement |
|---|---|---|---|---|---|---|
| `C:9992:718425012` | B1 | Členok, ktorý opuchol, bol ten ľavý. | The ankle that swelled up was the left one. | The ankle that swelled was the left one. | `up` (verb particle / directional) | **True loss.** "opuchol" = swelled up; English "swelled" alone carries the same meaning, the particle is optional. |
| `C:9244:3704016824` | B1 | Kým sa vlny valili, čierna mačka nepohla ani fúzom. | While the waves were rolling in, the black cat did not move a whisker. | While the waves were rolling, the black cat didn't move a whisker. | `in` (verb particle / directional) | **True loss, and a reference defect.** The Slovak "vlny sa valili" has no directional; the *reference* added "in". F5 compares against the reference, so a faithful answer is punished. |
| `C:11348:1001085647` | A2 | Pozri! Asistent práve drží odrazovú dosku hore. | Look! The assistant is holding the reflector up now. | Look! The assistant is holding the reflector up. | `now` (adjunct adverb) | **Defensible, not a clear loss.** The Slovak "práve" is explicit and the answer drops it; the continuous plus "Look!" recovers most of it, so it is a borderline kill rather than a plain error. |

Benefit on the 105 (not merged with the cost above): F5 kills **9** wrong answers, of which **5 were being
accepted** before F5 — `W:11348:2987233244`, `W:4612:586139873`, `W:7238:1943930546`, `W:8824:1740944184`,
`W:9907:325819033`. The other four were already rejected by another guard.

So F5 buys 5 saves for 3 kills, of which 2 are true losses. It is the single largest mover in the table
(strict 8 → 3 on its own) and also the only rule that costs coverage.

---

## 3. F4v2 verified

- **`C:9498` abstains on all three answers.** Trace on each: `{"fired": false, "reason": "Slovak
  underdetermined", "features": {"person": null, "number": null, "gender": null}, "signals": []}`
  (Phase 1f's F4 fired on all three).
- **Both real saves still fire.**
  - `W:4571:4142535241` — "If I leave one screw loose, the whole chair wobbles." fires on a *person* clash:
    features `{person 2, sg}` from `present -š necháš` vs answer subject `i`.
  - `W:3494:4150910632` — "If the ball had landed in black, they would have gone home with empty pockets."
    fires on a *number* clash: features `{person 3, sg, f}` from `l-participle bola` vs answer subject `they`.
- **What the Phase 1f bug really was.** Not the English pronoun the brief assumed. F4 read the *noun* `škola`
  ("school") as a feminine l-participle and therefore claimed the Slovak fixed a feminine singular subject,
  which clashed with "he". Three further defects of the same family were found and fixed while building
  F4v2: the clitic `si` read as the 2sg past auxiliary; the instrumental verbal noun `vyťahovaním` read as a
  1sg `-m` form; and English object `it`/`you` treated as subjects. F4v2 now only reads an l-participle when
  the sentence actually carries a past/conditional marker, and abstains whenever any pronoun of the answer
  fits the Slovak. The English-pronoun defect was real, but it was the fourth cause, not the first.
- **C:11216 (Task 1) — apparatus bug, fixed generally, not a genuine limitation.** See §3a.
- **Net effect.** F4v2 replacing F4 (row 2 vs row 0): coverage 214 → **217**, false acceptance unchanged
  (raw 15, lenient 6, strict 8), zero correct answers killed, zero new false acceptances. F4v2 is now a
  free +3 coverage; in rows 6–8 it also keeps the C:9498 answers that F4 used to kill.

### 3a. Task 1: the C:11216 kills were an apparatus bug of the known family

Slovak: *Ak sa ti odpoveď nepáči, nemal by si sa kariet pýtať.* — a 2nd-person-singular conditional.
The three correct answers all start "If you don't like the answer, you shouldn't ask the cards."
Pre-fix trace: `F4v2: wrong subject: person clash, answer "you", Slovak {'person': '3', 'number': 'sg',
'gender': 'm'}`.

Cause: the builder's earlier fix made the guard ignore **every** `si`, so `nemal by si` lost its only person
signal, and the bare l-participle `nemal` fell through to the *default* person 3. That is the same family as
the fixes already made (a clitic read wrongly) — here an over-correction of one of them — so it was fixed
generally, not by id.

Two candidate fixes were tried:

1. Read `si` directly after `by/keby/aby/žeby` as the 2sg auxiliary. This repaired C:11216 but killed three
   other correct answers (`C:9907:1778280655`, `C:9907:2522110302`, `C:9907:3412931110`), because
   *keby si bola vzala …* is itself ambiguous between "if you had taken" and "if she had taken (for
   herself)" — the dative reflexive `si` sits in exactly the same clitic slot. Rejected: it asserts a person
   the Slovak does not fix, which is what the brief forbids.
2. **Adopted:** `si` is ambiguous everywhere, so it yields no person **and** it blocks the default 3rd person
   a bare l-participle would otherwise assert. Abstain instead of guess.

Verification after the fix (full re-tabulation, new timestamp `results_20260918T152458Z`): row 0 still
reproduces 1f exactly (214/235, raw 15, lenient 6, 193/21); `C:9498` still abstains ×3;
`W:4571:4142535241` and `W:3494:4150910632` still fire; **F4v2 cost on the 235 is now 0** (was 3), kills on
the 105 are the same 4 as before (2 of them saves). Coverage of the all-together rows rose 210 → 213 (P-B)
and 215 → 218 (P-C) with unchanged false acceptance.

---

## 4. F2 boundary on the two disputed items

| id | Slovak | reference | answer | boundary | verdict |
|---|---|---|---|---|---|
| `W:16403:624976382` (A2, type M, "Future with WILL") | Rozlúč sa a o hodinu sa vráti naspäť. | Say bye now and she will come back in an hour. | Say bye now and she comes back in an hour. | **does not fire** | stays `correct_with_tip` |
| `W:10366:3357618811` (B2, type T, "Future Perfect Continuous") | Do desiatej už bude zohrievať rezance dve hodiny v kuse. | By ten he will have been reheating noodles for two hours straight. | By ten he will have reheated noodles for two hours straight. | **fires** | tip withdrawn → `wrong` |

Rule traces:

- `W:16403:624976382`: `{"fired": false, "reason": "span/ongoingness still expressed", "slovak_markers":
  ["duration noun in the accusative"], "slovak_ongoing": [], "answer_span_tokens": ["hour"],
  "continuous": false}`
- `W:10366:3357618811`: `{"fired": true, "clash": "ongoingness dropped (no continuous form in the answer)",
  "slovak_markers": ["v kuse (in a row / straight)", "už (already / for)", "explicit time span"],
  "slovak_ongoing": ["v kuse", "už"], "answer_span_tokens": ["for", "hours", "straight", "ten", "two"]}`

**`W:16403:624976382` did NOT come out as wrong under the span/ongoingness rule.** Plainly: the rule only
withdraws a tip when the Slovak states a span or an ongoingness that the answer *drops*. Here the span is
still there — "o hodinu" is rendered as "in an hour" — and there is no ongoingness in the Slovak at all. The
actual defect of this answer is a tense choice ("comes back" for a future "vráti sa"), which is a different
fault class that the boundary rule has no grip on. The strict reading nevertheless counts this item as a
real false acceptance, which is why the strict column is one higher than the lenient column in every
all-together row.

Boundary kills: **0 on the 235** when applied alone (row 3); **1 on the 235** in combination with F4v2
(`C:9498:582627860`, because F4v2 lets that answer reach L3 and the boundary then withdraws its tip for the
dropped "celá/entire" span — this one is a *defensible* rejection, the answer says "entire school" so the
span is in fact present and the trace is over-eager). **2 on the 105**: `W:4612:586139873` (stated span
"už" dropped) and `W:10366:3357618811` (ongoingness dropped) — the second is a real save, the first was
already caught by F5 in the combined rows.

---

## 5. Every remaining error

### Row 7 — all three new rules × P-B: 9 raw false acceptances

| id | level | type | path | judgement |
|---|---|---|---|---|
| `W:16403:624976382` | A2 | M | L1 correct_with_tip | **disputed** — strict counts it real (wrong tense, see §4); Phase 1e called it not real |
| `W:1018:1251085634` | B1 | T | L1 correct_with_tip | not real — past simple for a Slovak perfective, tipped |
| `W:3603:1489926651` | B1 | W | L3 model TIP | not real — "taking" for "bringing", tolerable synonym, 1f judged not real |
| `W:14266:664063167` | A1 | T | L1 correct | not real — "What are they dancing?" is a valid reading of "Čo tancujú?" |
| `W:1452:1471817457` | B1 | W | L3 model TIP | **real** — "grabs" for "dotkne sa" (touches) changes the meaning; the only lenient-real item in this row |
| `W:1452:3166274700` | B1 | S | L1 correct | not real — the Slovak subject is unmarked, "she" is a valid reading |
| `W:5595:3623849236` | B1 | T | L1 correct_with_tip | not real — past simple vs present perfect, tipped |
| `W:9244:3038274947` | B1 | T | L1 correct_with_tip | not real — "rolled in" vs "were rolling in", tipped |
| `W:8824:241327957` | B1 | T | L1 correct_with_tip | not real — "swung" vs "was swinging", tipped |

Lenient real: 1 (`W:1452:1471817457`). Strict real: 2 (+ `W:16403:624976382`).

### Row 7 — 22 false rejections

Grouped by cause; every id listed.

**(a) L3 model DIFF on a defensible paraphrase — 13, all a model-side loss, not an offline guard:**
`C:29691:455389026`, `C:29691:2402977996` (present-for-future "Pustí" rendered with will / going to),
`C:16261:2683737001` (subject gender swapped throughout — defensible, the Slovak is unmarked),
`C:16403:2761099319` ("Say goodbye – he will return"), `C:27628:2910266109`, `C:27628:3492027817`
("zobudia sa" with will), `C:26084:1225655220`, `C:26084:2889436188`, `C:26084:3073504942` (the Slovak
leaves both subjects open, the model insists on the reference's he/she split), `C:21124:681157260`
("under the roof" for "pod strechou" — literal and correct), `C:5595:3589927967`, `C:5595:3701842021`
(the reference's he/she split again), `C:5959:1797630685`, `C:5959:378048785`, `C:8293:1872525904`.
All of these are **true losses**: the answers are acceptable translations. The recurring cause is a
reference that fixes a pronoun the Slovak leaves open; the model follows the reference.

**(b) F5 kills — 3:** `C:9992:718425012` (true loss), `C:9244:3704016824` (true loss, reference defect),
`C:11348:1001085647` (defensible). See §2.

**(c) L2 vetoes — 3:** `C:7558:2926388663` (library mistake "had we seen" vs "have we seen" — defensible,
the practised inversion is a different tense), `C:23669:2842578131` (practised span "above" not present,
answer says "over" — **guard bug**: an equivalent preposition should satisfy the lock),
`C:9244:3137708535` (practised span "were rolling" not present, answer says "rolled in" — defensible, the
exercise practises the continuous).

**(d) F2 boundary — 1:** `C:9498:582627860` — tip withdrawn for a dropped "celý" span although the answer
says "entire school". **Guard bug (over-eager span match)**, cheap to fix, costs 1 coverage.

### Row 8 — all three new rules × P-C: 10 raw false acceptances

The 9 of row 7 with two changes — `W:3603:1489926651` moves from L3 TIP to L3 SAME (still not real) — plus
one new item:

| id | level | type | path | judgement |
|---|---|---|---|---|
| `W:10366:36005249` | B2 | S | L3 model SAME | **real** — "they will have been reheating" for a Slovak 3sg; P-C accepts it where P-B rejected it. This is the single new false acceptance P-C buys. |

Lenient real: 2 (`W:1452:1471817457`, `W:10366:36005249`). Strict real: 3 (+ `W:16403:624976382`).

### Row 8 — 17 false rejections

Same causes, five fewer than P-B (P-C recovers `C:29691:455389026`, `C:27628:2910266109`,
`C:21124:681157260`, `C:5959:1797630685`, `C:8293:1872525904`).
**(a) L3 model DIFF — 10, all true losses:** `C:29691:2402977996`, `C:16261:2683737001`,
`C:16403:2761099319`, `C:27628:3492027817`, `C:26084:1225655220`, `C:26084:2889436188`,
`C:26084:3073504942`, `C:5595:3589927967`, `C:5595:3701842021`, `C:5959:378048785`.
**(b) F5 — 3:** `C:9992:718425012`, `C:9244:3704016824`, `C:11348:1001085647` (as above).
**(c) L2 — 3:** `C:7558:2926388663`, `C:23669:2842578131`, `C:9244:3137708535` (as above).
**(d) F2B — 1:** `C:9498:582627860` (as above).

---

## 6. Sample size

From `sample_size.json`, for a true false-acceptance rate around 2 %, two-sided 95 %:

| target half-width | normal approximation | exact Clopper–Pearson (smallest n) | exact, stable from |
|---|---|---|---|
| ± 1 pp | **n = 753** | **n = 1,114** (k = 22, p̂ = 1.98 %, CI 1.24–2.98 %) | n = 1,134 |
| ± 1.5 pp | **n = 335** | **n = 569** (k = 11, p̂ = 1.93 %, CI 0.97–3.43 %) | n = 587 |

Against the current 105 wrong answers: the sample is roughly 5–11× too small to resolve a 2 % target. At
n = 105 a single case is 0.95 pp and the exact interval around 2/105 spans 0.2–6.7 %, i.e. a config that is
truly at 1 % and one that is truly at 6 % look the same. Enlarging the sample is a separate decision and was
**not** done here.

---

## 7. Cost

Model calls (`call_counts.json`, unchanged after the Task 1 re-run):

- new: **0** · reused: **396** (byte-identical prompts taken from the Phase 1e / 1f ledgers) · failed: **0**
  · cap: 1,200 · HTTP attempts by Phase 1g: 0 · 429s: 0.
- Spend: **0** — no new model call was made, so Phase 1g cost nothing in model spend. Three full
  tabulations were run (two before the Task 1 fix, one after); none of them touched the API.

Agent cost:

Builder agent: 190,340 tokens, 11 tool calls.
Reporter agent: 95,571 tokens, 12 tool calls.
Main session: 4 tool calls.

---

## 8. Judgement (5 lines)

1. Provisional best configuration: **row 7 — F1 F2 F3 F4v2 F5 F2B × P-B** — coverage **213/235 (90.6 %)**,
   strict false acceptance **2/105 = 1.9 %, exact 95 % CI 0.2–6.7 %** (lowest strict upper bound in the
   table, tied with row 5, and the better coverage of the two); label it provisional pending a larger sample.
2. Row 8 (same rules × P-C) reaches the best coverage, 218/235 (92.8 %), but its strict rate is 3/105 =
   2.9 % (0.6–8.1 %); P-C buys 5 correct answers for 1 extra real false acceptance — a trade to decide once
   the sample is big enough to see it, not now.
3. F4v2 is now free (+3 coverage, no new false acceptance) and should be kept regardless; F2B is cheap
   (1 defensible correct kill, 1 real save); F5 carries the whole reduction but costs 3 correct answers, 2
   of which are true losses caused by reference-side extras.
4. Still worth building offline: a reference-hygiene pass (the `C:9244` "rolling in" and `C:9498` "celý"
   cases show the references, not the answers, are the defect) and two small guard fixes — equivalent
   prepositions in the L2 lock, and a span match that accepts "entire" for "celý". Everything else that
   remains is L3 model behaviour on pronouns the Slovak leaves open, which no offline rule can settle.
5. Caveat that governs all of the above: the three new rules were tuned on the same frozen 105/235 they are
   scored on, so these numbers are in-sample and optimistic, and at n = 105 the 2 % question is simply not
   measurable — a fresh sample of ~570 (± 1.5 pp) or ~1,130 (± 1 pp) wrong answers is the only way to settle it.

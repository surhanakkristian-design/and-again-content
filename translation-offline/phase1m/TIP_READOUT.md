# Phase 1M — TIP readout (label `readout`)

**ZERO-CALL READOUT ON ALREADY-COMPUTED VERDICTS OF A CLOSED SET — NOT A NEW MEASUREMENT**

Produced by `phase1m/tip_readout_1m.py`; raw numbers in `phase1m/tip_readout_1m.json`.
**0 model calls were made, and 0 would have been needed** (see the `need_call` rows).
Every L3 verdict is read from the phase1j / phase1k ledgers plus `phase1l/calls.jsonl`.

`dev`, `replay1j` and `fresh1l` are CLOSED sets that have already been measured and whose
judge labels were read in earlier phases. Re-scoring them under a different guard stack is a
*readout*, not a measurement: the intervals below are not evidence about an unseen set.
**No decision is taken here — the TIP switch is the main session's call.**

Stack under readout: **LOCKTIP + F8v2 + F9 off**, prompt `P-FROZEN`, model
`gemini-3.1-flash-lite` (temperature 0, thinkingBudget 0).
Reference stack ("1L baseline"): LOCKTIP + F8 + F9 on + TIP-as-rejection.
All intervals are exact Clopper–Pearson 95 %.

---

## 0. Regression (brief §1.1)

`python3 runner_1m.py --dev --f8 f8 --f9 on --tip reject` reproduces Phase 1L **to the digit**:

| side | coverage | FA | FA type T | expected 1L |
| --- | --- | --- | --- | --- |
| dev | 182/189 | 12/301 | 0/54 | 182/189, 12/301 — MATCH |
| replay1j | 178/196 | 15/294 | 2/59 | 178/196, 15/294, T 2/59 — MATCH |
| fresh1l | 191/217 | 15/383 | 3/130 | 191/217, 15/383, T 3/130 — MATCH |

Lock/L3 counts also match (dev 65/318, replay1j 93/336, fresh1l 150/460), 0 cache misses.
**No code change was required.** `--tip both` already works: `main()` runs the whole DEV
regression once per TIP setting; it is not silently collapsed to `reject`.
(One trap, documented in `tip_readout_1m.py`: `phase1i/checker_1i` keeps ONE module-global
annotation map that `make_state` overwrites per side, so a side must be scored immediately
after it is built. Building all three and scoring afterwards crashes in
`reference_hygiene._droppable_tokens` with `ModuleNotFoundError: checker_1h`.)

---

## 1. TIP-as-rejection ON vs OFF, under F8v2 + F9-off

### DEV (closed; 490 items, L3-eligible 318, stored verdicts 318, **would need a call: 0**)

| metric | TIP-as-rejection **ON** (reject) | TIP-as-rejection **OFF** (accept) |
| --- | --- | --- |
| coverage | 182/189 = 96.30 % [92.52, 98.50] | 184/189 = 97.35 % [93.93, 99.14] |
| FA (all) | 11/301 = 3.65 % [1.84, 6.44] | 28/301 = 9.30 % [6.27, 13.16] |
| FA type T | 0/54 = 0.00 % [0.00, 6.60] | 1/54 = 1.85 % [0.05, 9.89] |
| FA type W | 2/76 = 2.63 % [0.32, 9.18] | 6/76 = 7.89 % [2.95, 16.40] |
| FA type M | 3/66 = 4.55 % [0.95, 12.71] | 14/66 = 21.21 % [12.11, 33.02] |
| FA type S | 6/98 = 6.12 % [2.28, 12.85] | 7/98 = 7.14 % [2.92, 14.16] |
| FA type V | 0/6 = 0.00 % [0.00, 45.93] | 0/6 = 0.00 % [0.00, 45.93] |
| FA type E | 0/1 = 0.00 % [0.00, 97.50] | 0/1 = 0.00 % [0.00, 97.50] |

### REPLAY1J (closed 1j holdout; 490 items, L3-eligible 336, stored 336, **would need a call: 0**)

| metric | TIP-as-rejection **ON** (reject) | TIP-as-rejection **OFF** (accept) |
| --- | --- | --- |
| coverage | 182/196 = 92.86 % [88.31, 96.04] | 187/196 = 95.41 % [91.46, 97.88] |
| FA (all) | 17/294 = 5.78 % [3.40, 9.10] | 35/294 = 11.90 % [8.43, 16.17] |
| FA type T | 3/59 = 5.08 % [1.06, 14.15] | 5/59 = 8.47 % [2.81, 18.68] |
| FA type W | 4/68 = 5.88 % [1.63, 14.38] | 8/68 = 11.76 % [5.22, 21.87] |
| FA type M | 9/64 = 14.06 % [6.64, 25.02] | 20/64 = 31.25 % [20.24, 44.06] |
| FA type S | 1/102 = 0.98 % [0.02, 5.34] | 2/102 = 1.96 % [0.24, 6.90] |
| FA type V | 0/1 = 0.00 % [0.00, 97.50] | 0/1 = 0.00 % [0.00, 97.50] |
| FA type E | 0/0 = n/a | 0/0 = n/a |

### FRESH1L (closed Phase 1L set; 600 items, L3-eligible 460, stored 460, **would need a call: 0**)

| metric | TIP-as-rejection **ON** (reject) | TIP-as-rejection **OFF** (accept) |
| --- | --- | --- |
| coverage | 194/217 = 89.40 % [84.52, 93.16] | 203/217 = 93.55 % [89.41, 96.43] |
| FA (all) | 12/383 = 3.13 % [1.63, 5.41] | 30/383 = 7.83 % [5.35, 10.99] |
| FA type T | 3/130 = 2.31 % [0.48, 6.60] | 12/130 = 9.23 % [4.86, 15.57] |
| FA type W | 1/70 = 1.43 % [0.04, 7.70] | 2/70 = 2.86 % [0.35, 9.94] |
| FA type M | 2/68 = 2.94 % [0.36, 10.22] | 10/68 = 14.71 % [7.28, 25.39] |
| FA type S | 1/70 = 1.43 % [0.04, 7.70] | 1/70 = 1.43 % [0.04, 7.70] |
| FA type V | 5/44 = 11.36 % [3.79, 24.56] | 5/44 = 11.36 % [3.79, 24.56] |
| FA type E | 0/1 = 0.00 % [0.00, 97.50] | 0/1 = 0.00 % [0.00, 97.50] |

### Would-need-a-call accounting

On all three sides **0** items are L3-eligible under the new stack without a stored verdict.
The reason is structural, not luck: swapping the F8 module and switching F9 off acts in
`apply_guards`, *after* `run_pipeline`, and TIP-as-rejection acts *inside* the L3 decision;
neither enlarges the L3-eligible set, which is fixed by LOCKTIP (318 / 336 / 460 — identical
to the 1L run). Therefore the "treated as rejected" and "treated as accepted" bounds coincide
with the point estimates in every table above. **No call was made.**

---

## 2. FRESH1L — what F8v2 alone changes

Stack: LOCKTIP + **F8v2** + F9 **on** + TIP-reject, i.e. the 1L stack with only the F8 module
swapped.

| | FA | coverage | FA type V |
| --- | --- | --- | --- |
| 1L baseline (F8) | 15/383 = 3.92 % [2.21, 6.38] | 191/217 = 88.02 % | 8/44 |
| F8v2 | 11/383 = 2.87 % [1.44, 5.08] | 191/217 = 88.02 % | 4/44 |

Coverage is untouched: on this side F8v2 costs no judged-correct answer. All movement is
inside type V (active Slovak answered with an English passive). It is **not** a strict
improvement — F8v2 catches 8 FAs that the unpatched F8 let through and loses 4 that the old
F8 had caught. Net 15 → 11.

**The 8 items F8v2 newly catches (all type V):**

* `W:140006:98216243` (sid 140006) — *Ona nikdy neposiela e-maily po desiatej večer.* → "Emails are never sent by her after ten in the evening."
* `W:140014:1487151881` (sid 140014) — *Ona pracuje na tej diplomovke už tri mesiace.* → "That thesis has been worked on by her for three months."
* `W:140024:670820885` (sid 140024) — *On opravoval tú kosačku celé popoludnie a nakoniec to vzdal.* → "That lawnmower was being repaired by him all afternoon, and in the end he gave up."
* `W:140037:1538470541` (sid 140037) — *My sme ten nábytok zložili za dve hodiny.* → "That furniture was assembled by us in two hours."
* `W:140041:1273097874` (sid 140041) — *My tú zmluvu podpíšeme bez akýchkoľvek zmien.* → "That contract will be signed by us without any changes."
* `W:140058:4156271032` (sid 140058) — *Keby sme boli odišli skôr, neboli by sme zmeškali ten let.* → "If we had left earlier, that flight would not have been missed."
* `W:140060:2368276709` (sid 140060) — *On by ten problém vyriešil za jediné popoludnie.* → "That problem would be solved by him in a single afternoon."
* `W:140064:225979015` (sid 140064) — *Ona by tú skriňu presunula bližšie k oknu.* → "That wardrobe would be moved closer to the window by her."

**The 4 items F8v2 loses (were rejected by the 1L F8, accepted by F8v2; all type V):**

* `W:140001:3226349339` — *Ona každé ráno pije zelený čaj s medom.* → "Green tea with honey is drunk by her every morning."
* `W:140003:312397117` — *Moja sestra nosí okuliare iba pri čítaní.* → "Glasses are worn by my sister only when she reads."
* `W:140012:213263887` — *Sused, ktorý býva nad nami, opravuje bicykle v garáži.* → "Bicycles are repaired in the garage by the neighbour who lives above us."
* `W:140021:1964329415` — *Moja babka nám každú nedeľu piekla jablkový koláč.* → "An apple cake was baked for us every Sunday by my grandma."

These four are plain simple-present / past actives with an explicit nominative agent and an
English `be + PP + by`-phrase — the core F8 case. That F8v2 abstains on them is a finding the
main session should weigh before freezing `f8v2`; it is *not* a decision taken here.

---

## 3. FRESH1L — what F9-off alone changes

Stack: LOCKTIP + F8 (1L module) + F9 **off** + TIP-reject.

| | FA | coverage |
| --- | --- | --- |
| 1L baseline (F9 on) | 15/383 = 3.92 % [2.21, 6.38] | 191/217 = 88.02 % [82.94, 92.02] |
| F9 off | 15/383 = 3.92 % [2.21, 6.38] | 194/217 = 89.40 % [84.52, 93.16] |

On FRESH1L, switching F9 off is **FA-neutral** (no new FA id, and F9 was catching no FA that
anything else missed) and buys +3 coverage: on this side F9 only ever rejected judged-correct
answers. The same switch is **not** free elsewhere — on REPLAY1J, F9-off alone moves FA
15/294 → 18/294 while coverage moves 178/196 → 181/196 (`f9off_only` in
`tip_readout_1m.json`). On DEV it changes nothing at all.

---

## 4. Reading note

Every number above is a re-scoring of sets whose model verdicts were produced and whose judge
labels were read in earlier phases. They can *rank* candidate stacks; they cannot *certify*
one, because any stack chosen on them is chosen on data it has already seen. The new Phase 1M
set is the only place where the chosen stack can be measured.

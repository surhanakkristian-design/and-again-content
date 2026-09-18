# Task A — the `p` (person / number) chain: offline DEV measurement

Agent A, 18 Sept 2026. **Zero model calls** — the L3 verdicts are the stored Phase 1i P-E4b
replies, exactly as `phase1j/baseline_dev_1j.py` uses them. DEV only; the holdout was touched
once, COUNT ONLY (see `phase1j/access_log.jsonl`).

## 1 Coverage of the chain

| side | sentences | with a `p` chain | ambiguous (None) |
|---|---|---|---|
| DEV | 70 | 51 | 19 |
| HOLDOUT (count-only pass) | 70 | 47 | 23 |
| all 140 | 140 | 98 | 42 |

Distribution of the DEV chains: {'?sg': 2, '3sg': 37, '3?': 5, '3pl': 3, '?pl': 1, '1pl': 1, '2sg': 2}

### The 19 ambiguous DEV sentences and why

| sid | reason |
|---|---|
| 2783 | no readable person/number morphology in the main clause |
| 3937 | no readable person/number morphology in the main clause |
| 7444 | no readable person/number morphology in the main clause |
| 7752 | no readable person/number morphology in the main clause |
| 7910 | no readable person/number morphology in the main clause |
| 8920 | no readable person/number morphology in the main clause |
| 9495 | no readable person/number morphology in the main clause |
| 9607 | no readable person/number morphology in the main clause |
| 10013 | no readable person/number morphology in the main clause |
| 10179 | no readable person/number morphology in the main clause |
| 11610 | no readable person/number morphology in the main clause |
| 13175 | no readable person/number morphology in the main clause |
| 15954 | no readable person/number morphology in the main clause |
| 20702 | no readable person/number morphology in the main clause |
| 21467 | no readable person/number morphology in the main clause |
| 22427 | no readable person/number morphology in the main clause |
| 23878 | no readable person/number morphology in the main clause |
| 26084 | no readable person/number morphology in the main clause |
| 27628 | no readable person/number morphology in the main clause |

## 2 Hand-check (every DEV sentence read against the Slovak by the agent)

Gold = the person/number of the MAIN-clause subject as the Slovak states it.
`conservative` = the script asserts less than the gold (None, or an open feature) — no false claim.
`error` = the script asserts a person or number the Slovak does not have.

| outcome | n |
|---|---|
| agree | 44 |
| conservative (script says less) | 26 |
| **error** | **0** |

## 3 The F4p consultation alone, on top of the frozen 1i baseline replay

Baseline (unchanged apparatus): coverage 191/210, FA 15/275.
F4p can only turn an acceptance into a rejection, so it is applied to the accepted items.

| | baseline | + F4p |
|---|---|---|
| coverage | 191/210 = 90.95 % | 191/210 = 90.95 % |
| FA | 15/275 = 5.45 % | 11/275 = 4.00 % |

FA caught by type: {'S': 4} (baseline FA by type T 0 / W 2 / M 5 / S 8).
Correct answers wrongly rejected: **0**.

### False acceptances caught (id, type, Slovak, answer, p, reason)

- `W:10574:2448666810` **S** — SK: *Trénoval hodiny, kým bolo svetlo konečne správne.* — answer: *They had been training for hours until the light was finally right.* — p = {'person': 3, 'number': 'sg', 'gender': 'm', 'subject': 'dropped'} — answer subject "they" contradicts the Slovak number (person 3, number sg; l-participle trénoval)
- `W:1452:315243162` **S** — SK: *Ak sa dotkne toho kaktusa, strávi večer vyťahovaním tŕňov z prsta.* — answer: *If they touch that cactus, they'll spend the evening pulling thorns out of their finger.* — p = {'person': 3, 'number': 'sg', 'gender': None, 'subject': 'dropped'} — answer subject "they" contradicts the Slovak number (person 3, number sg; present 3sg strávi)
- `W:16403:1306885234` **S** — SK: *Rozlúč sa a o hodinu sa vráti naspäť.* — answer: *Say goodbye, and in an hour they'll come back.* — p = {'person': 3, 'number': 'sg', 'gender': None, 'subject': 'dropped'} — answer subject "they" contradicts the Slovak number (person 3, number sg; present 3sg vráti)
- `W:8293:1283962081` **S** — SK: *Jedlo nikdy nedelí, takže tento croissant musí byť výnimočný.* — answer: *They never share food, so this croissant must be special.* — p = {'person': 3, 'number': 'sg', 'gender': None, 'subject': 'dropped'} — answer subject "they" contradicts the Slovak number (person 3, number sg; present 3sg nedelí)

### Correct answers wrongly rejected

- none

### The 11 baseline false acceptances F4p does NOT catch

- `W:10013:1594646351` W — *Right now she is pressing a blue compress on the bruise.* — no p chain
- `W:10013:4174637227` M — *Right now she is pressing a compress on the bump.* — no p chain
- `W:21124:1753932823` M — *She stays under the roof, but today she is dancing in the rain.* — a main-clause pronoun (she,she) is compatible with the Slovak
- `W:2389:1402963517` S — *If durians didn't smell so strong, the customs officer would probably let them through.* — no main-clause subject pronoun in the answer
- `W:2783:2540506102` M — *The ball that the dog brought is covered in mud.* — no p chain
- `W:31648:250135833` W — *Honey, apparently he left the plate yesterday, not today.* — a main-clause pronoun (he) is compatible with the Slovak
- `W:7444:2683969038` M — *She has applied three layers, so her eyelashes look huge.* — no p chain
- `W:7910:2914297793` S — *Despite the fan being at full power, the clipped piles didn't move at all.* — no p chain
- `W:8799:1222448868` S — *They kept throwing the same combination until it went smoothly.* — a main-clause pronoun (it) is compatible with the Slovak
- `W:8812:384802316` M — *The coach wishes his gloves were thicker.* — no main-clause subject pronoun in the answer
- `W:9687:2008862971` S — *If both countries sign the treaty, the borders will open next month.* — no main-clause subject pronoun in the answer

## 4 Reading

The DEV side contains only 4 subject-recast false acceptances out of 15; the Phase 1i HOLDOUT
had 10 of 23. F4p is therefore measured here mainly for its COST (correct answers rejected: 0),
and that cost is what the DEV side can establish at this size. The prompt line `p_prompt` is not
measurable offline at all — it needs the DEV run of agent R.


## 5 Count-only pass over all 140 sentences

The one permitted holdout contact: counts only, no sentence, answer or verdict was read or printed; logged in `phase1j/access_log.jsonl`.

| | DEV | HOLDOUT | all |
|---|---|---|---|
| with a `p` chain | 51 | 47 | 98 |
| ambiguous | 19 | 23 | 42 |

Chain shapes (person+number): {"dev 1pl": 1, "dev 2sg": 2, "dev 3?": 5, "dev 3pl": 3, "dev 3sg": 37, "dev ?pl": 1, "dev ?sg": 2, "holdout 2sg": 3, "holdout 3?": 4, "holdout 3pl": 4, "holdout 3sg": 35, "holdout ?sg": 1}

Ambiguity reasons: {"dev no readable person/number morphology in the main clause": 19, "holdout dative experiencer next to a reflexive": 3, "holdout no readable person/number morphology in the main clause": 18, "holdout signals disagree on both person and number": 2}

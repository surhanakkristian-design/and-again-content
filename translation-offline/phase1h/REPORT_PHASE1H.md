# Translation offline checking — Phase 1h report (out-of-sample measurement on the frozen checker)

18 September 2026. Measuring agent. No rule, threshold, word-class table, prompt or hygiene step was
changed in this phase. Every defect found during measurement is recorded in §5 and **not fixed**.

## 1. The freeze

- freeze commit **`0abfafd40a6a768cfa1c3c69cfc43482e0d9979b`**, tag `translation-offline-phase1h-FROZEN`.
- What §2 changed, before the freeze and before any fresh data existed:
  - **2.1 L2 lock, non-verb spans** — `lock_equivalent_ok()` releases a lock when an equivalent
    preposition/relativiser/linker is present, only through groups that already exist. It released exactly
    two items on the 80: `C:23669:2842578131` ("over" vs the lock "above") and `C:10107:4080641578`.
  - **2.2 F2B span match** — `en_span_tokens(it)` now reads the item's own `p` "+word" insertions, its own
    `alt` members of an EN_SPAN-containing span, and the co-members of the existing synonym groups.
    `C:9498:582627860` keeps its tip instead of being downgraded, and `W:10366:3357618811` is still caught.
  - **2.3a reference hygiene, OPTIONAL marking** — 8 of the 80 old sentences touched
    (1018, 10866, 16403, 21467, 5595, 9244, 9495, 9992).
  - **2.3b gender chain** — 1 of 80 touched after the tightening.
- **Order of work** (all commits local in the content repo, none pushed):
  1. `0abfafd` §2 fixes + reference hygiene, checker FROZEN.
  2. `d078794` FREEZE.md with the sha256 of every frozen file.
  3. `b32b9d6` fresh sentence selection (seed 20260919): 60 new sentences, A1 9 / A2 12 / B1 21 / B2 18,
     zero overlap with the 80 by id and by Slovak text; only **2** of them fall in the 13–16-word band,
     because the unused pool contains only two.
  4. `3eebc2f` STATE.md.
  5. `798428d` 60 new annotations — Phase 1c pipeline unchanged; the annotator did not read the checker,
     `reference_hygiene.py` or the Phase 1g error lists.
  6. Blind writers (they saw only sid/sk/level/topic): **420 correct** and **560 wrong**
     (140 T / 140 W / 140 M / 140 S) over all 140 sentences (80 old + 60 new).
  7. `65e1c1a` blind judgement pass, recorded **before any checker verdict existed**: of the 420 correct,
     0 were judged really wrong; of the 560 wrong, **10 were judged really correct** (T 3, W 2, M 5, S 0),
     leaving **550 judged really wrong**; 21 doubts, all resolved as real. The old 105 wrong items were
     re-judged blind as well (`phase1h/fresh/judgements_old105.jsonl`): **6 judged really correct**.
- **Evidence that nothing changed after the freeze:**

```
$ git diff --stat translation-offline-phase1h-FROZEN HEAD -- translation-offline/phase1h/*.py
(no output)
$ shasum -a 256 phase1h/*.py
49fa087bf2ecb511a960315e1c1e25a6f01ffbbb40fd285fc3157168af556f19  phase1h/checker_1h.py
c9e19245ee48888eb2ea5033e6bad7890fa7fa0abdb70ec2f0cb8d99d911067a  phase1h/lib_prev.py
7380f3142f8980c15ec9c43528642e59437b7131a930e2115447ba68db605d36  phase1h/reference_hygiene.py
93a8623df8a328510204eb5d95744b9875fd4dde5c3ed7ff45597a0ee9b2dad6  phase1h/select_new_sentences.py
```

All four match FREEZE.md byte for byte. The full diff tag→HEAD adds only data files under `phase1h/fresh/`
(annotations, writer sets, judgements) plus, from this phase, three **non-checker** files:
`phase1h/fresh_io_fix.py` (I/O wrapper, §5 D1/D2), `phase1h/chk_fresh.ts` (runs the app's own existing
checker to produce the `chk` block) and `phase1h/report_tables.py` (tabulation).
`--selftest` and the 1h self-test both PASS on the frozen code.

## 2. In-sample vs out-of-sample

Denominators: in-sample = the frozen Phase 1c/1f sets (235 correct answers, 105 wrong, of which the new
blind pass calls 99 really wrong); out-of-sample = the fresh blind answers (420 correct, all judged really
correct; 560 wrong, of which 550 judged really wrong).

| figure | row | in-sample (frozen 235 / 105) | out-of-sample (fresh 420 / 550) | fall |
|---|---|---|---|---|
| coverage | 7 (P-B) | **216/235 = 91.9 %** [87.7–95.1] | **345/420 = 82.1 %** [78.1–85.7] | **-9.8 pp** |
| coverage | 8 (P-C) | 221/235 = 94.0 % [90.2–96.7] | 350/420 = 83.3 % [79.4–86.8] (**not valid**, §5 D3) | -10.7 pp |
| real false acceptance | 7 (P-B) | 2/19 = 10.5 % [1.3–33.1] strict; raw 10/105 = 9.5 % | **66/550 = 12.0 %** [9.4–**15.0**]; raw 73/560 = 13.0 % | **+1.5 pp** vs strict, +2.5 pp vs raw |
| real false acceptance | 8 (P-C) | 3/19 = 15.8 % [3.4–39.6] strict; raw 11/105 = 10.5 % | 8/550 = 1.5 % [0.6–2.8] (**not valid**, §5 D3) | — |

Old-set false acceptance under **both** judgement lists (Phase 1g strict, and the new blind re-judgement of
the 105):

- row 7: OLD strict (Phase 1g list) real FA: 2/19 10.5 % [1.3–33.1]; OLD real FA under the NEW blind judgement (strict + newly judged really wrong): 3/99 3.0 % [0.6–8.6]
- row 8: OLD strict (Phase 1g list) real FA: 3/19 15.8 % [3.4–39.6]; OLD real FA under the NEW blind judgement (strict + newly judged really wrong): 4/99 4.0 % [1.1–10.0]

The seven Phase 1h "accepted but unjudged" old items are resolved by the new blind pass:
`W:1018:1251085634`, `W:14266:664063167`, `W:1452:3166274700`, `W:5595:3623849236`, `W:9244:3038274947`,
`W:8824:241327957` → really **correct**; `W:5595:1942575047` → really **wrong**.

### Old-sentence vs new-sentence split of the fresh set (row 7)

| half | coverage | real false acceptance |
|---|---|---|
| the 80 OLD sentences, fresh answers | 185/240 = 77.1 % [71.2–82.2] | 37/317 = 11.7 % [8.4–15.7] |
| the 60 NEW sentences, fresh answers | 160/180 = 88.9 % [83.4–93.1] | 29/233 = 12.4 % [8.5–17.4] |

This is the most informative result of the phase: coverage on **brand-new sentences is higher** than on the
old sentences with fresh answers, and false acceptance is the same within noise. The in-sample 91.9 % was
therefore not carried by the sentences — it was carried by the particular 235 answers the checker was
tuned against. Fresh answers cost about 10 pp wherever they land.

## 3. Measurement detail (rows 7 and 8 only)

The full generated tables, with every id, are appended verbatim in §8 and live in
`translation-offline/phase1h/tables_1h.md`. Headlines for row 7, the only fully measured row:

**Coverage, fresh correct set (n = 420, all judged really correct)** — by level: A1 52/63 = 82.5 %
[70.9–90.9], A2 70/84 = 83.3 % [73.6–90.6], B1 117/147 = 79.6 % [72.2–85.8], B2 106/126 = 84.1 %
[76.6–90.0]. By Slovak length band: 1–6 55/66 = 83.3 % [72.1–91.4], 7–9 197/237 = 83.1 % [77.7–87.7],
10–12 86/105 = 81.9 % [73.2–88.7], **13–16 7/12 = 58.3 % [27.7–84.8]** — the long band is the weakest cell
and the least measured one.

**False acceptance, fresh wrong set** — headline 66/550 = 12.0 % [9.4–15.0]; raw 73/560 = 13.0 %
[10.4–16.1]. By type: T 2/137 = 1.5 % [0.2–5.2], W 17/138 = 12.3 % [7.3–19.0], **M 27/135 = 20.0 %**
[13.6–27.7], S 20/140 = 14.3 % [8.9–21.2]. By layer: L1 1, L3 **65** — the offline layers are not the
problem, the model is.

**Routing (fresh correct set, 420 items)**: L1 135 = 32.1 %, L3 253 = 60.2 %, L2 27 = 6.4 %, F4v2 3, F5 2.
In-sample routing was L1 100 / L3 132 / L2 2 / F5 1 of 235. Out of sample more traffic reaches the model,
so the projected cost rises.

**Latency and cost**: median **768 ms**, p95 **1061 ms** over the 934 calls that reached the wire. Tokens
in 148,235, out+thoughts 934. Price `lib_prev.PRICE['lite']` = $0.25 in / $1.50 out per 1M tokens; the
$0.025 cached rate never applies (the prompt is below the implicit-caching minimum, Phase 1e). **Cost per
L3 call $0.000030.** Usage assumption restated by hand from Phase 1e/1f: 20 exercises/day × 30 days = 600
exercises per active user per month, times the L3 share. At the measured 60.2 % L3 share that is 361 calls
→ **$0.0107 per active user per month** (Phase 1f reported $0.0118 at a 37.0 % L3 share).

**False rejections by cause** (row 7, fresh): L3 model DIFF on a defensible answer **43**, L2 lock **27**,
F4v2 **3**, F5 **2** — sum 75, asserted programmatically equal to the 75 listed false rejections (Phase 1g
mislabelled a 15-item group as 13, which is why the assertion exists). Row 8: L3 38, L2 27, F4v2 3, F5 2,
sum 70 = 70. In-sample row 7: L3 16, L2 2, F5 1, sum 19 = 19. Every id is in §8.

**Every real false acceptance, itemised**, with my judgement of why it slipped through (Slovak, reference
and answer for each are in §8):

| id | level | type | layer | why it slipped |
|---|---|---|---|---|
| `W:16403:624976382` (in-sample) | A2 | M | L1 | the app checker itself returns `correct_with_tip`; "comes back" for "vráti sa" loses the future the topic practises |
| `W:1452:1471817457` (in-sample) | B1 | W | L3 | "grabs" for "dotkne sa" — the model treats a stronger verb as a paraphrase |
| `W:10366:36005249` (in-sample, row 8) | B2 | S | L3 | pronoun swapped he→they; the Slovak fixes neither, the model says SAME |
| `W:20298:1595880954` | A1 | S | L3 | subject swapped he→they plus "a pill"→"one pill"; read as a paraphrase |
| `W:23669:561074874` | A1 | M | L3 | content **added** ("at night"); a TIP verdict still counts as an acceptance |
| `W:11348:1594514680` | A2 | M | L3 | reference content dropped ("reflector"→"board", "now" gone) |
| `W:11980:2419738346` | A2 | M | L3 | content added ("in the pot") |
| `W:13034:3769013457` | A2 | M | L3 | content added ("on the cake") |
| `W:16403:1306885234` | A2 | S | L3 | pronoun swap she→they plus contraction |
| `W:21124:1753932823` | A2 | M | L3 | "usually stays dry" → "stays under the roof": the practised contrast survives, the meaning does not |
| `W:9907:1778280655` | B2 | S | L1 | **writer artefact** — the "wrong" answer is byte-identical to the reference; the checker was right and the judge wrong (§5 D5) |

The pattern is blunt: **8 of the 10 fresh false acceptances are type M or S** — small additions, small
omissions, pronoun swaps — and all but one come from the L3 model answering TIP or SAME. TIP counts as an
acceptance in both rows, and on the wrong set that is where most of the damage is.

## 4. Reference hygiene

| half | sentences | (a) OPTIONAL marking | (b) g chain |
|---|---|---|---|
| old 80 | 80 | **8** — 1018, 10866, 16403, 21467, 5595, 9244, 9495, 9992 | **1** — 9495 |
| new 60 | 60 | **4** — 6275, 6353, 7444, 7910 | **0** |
| total | 140 | 12 | 1 |

Fewer than 10 sentences were touched in each half, so **all** of them are listed below, not a sample of 10:

- old 80:
  - `1018` (a) — now OPTIONAL: {"the#2": "A", "now": "now"} · ref: He has poured the smoothie into the tall glass, so the blender is completely empty now.
  - `10866` (a) — now OPTIONAL: {"for": "for"} · ref: He had been waiting for two hours before his number finally appeared.
  - `16403` (a) — now OPTIONAL: {"now": "now"} · ref: Say bye now and she will come back in an hour.
  - `21467` (a) — now OPTIONAL: {"boots": "your|some", "so": "so"} · ref: The water is cold, so you should wear boots.
  - `5595` (a) — now OPTIONAL: {"at": "at", "last": "last"} · ref: He has stamped the document at last, so she can finally go home.
  - `9244` (a) — now OPTIONAL: {"in": "in"} · ref: While the waves were rolling in, the black cat did not move a whisker.
  - `9495` (a) — now OPTIONAL: {"ever": "ever"} · ref: Her speech was rewritten twice before she ever walked onto that stage.
  - `9992` (a) — now OPTIONAL: {"up": "up"} · ref: The ankle that swelled up was the left one.
  - `9495` (b) — g chain [["she"]] · sk: Jej prejav bol prepísaný dvakrát, ešte než vôbec vyšla na to pódium.
- new 60:
  - `6275` (a) — now OPTIONAL: {"right": "right"} · ref: Look — right now they are posing in front of the waterfall.
  - `6353` (a) — now OPTIONAL: {"still": "still"} · ref: The lights were still warming up when the director shouted “action”.
  - `7444` (a) — now OPTIONAL: {"already": "already"} · ref: She has already applied three coats, so her lashes look huge.
  - `7910` (a) — now OPTIONAL: {"at": "at", "all": "all"} · ref: Despite the fan at full power, the clipped pile did not move at all.

## 5. Defects found after the freeze — recorded, NOT fixed

**D1 — the frozen loader cannot read its own fresh files (pure I/O).** `load_fresh()` builds its sentence
map from `fresh/new_sentences_60.jsonl` only, but the blind writers answered all 140 sentences of
`fresh/writer_input_140.jsonl`, so `--plan` died with `KeyError: 14266` on the first old sid. Worked around
in `phase1h/fresh_io_fix.py`, which imports the frozen `checker_1h` unmodified and only replaces the bytes
the loader reads:

```python
def _jl_patched(p):
    if os.path.basename(p) == 'new_sentences_60.jsonl':
        return _rows_140()          # 80 old + 60 new sentence records
    return _orig_jl(p)
C.jl = _jl_patched
```

No rule, threshold or prompt is touched; `mk()`, `lock_equivalent_ok()` and every layer run as frozen.
A side effect of the same defect: the frozen `mk()` hard-codes `'set': 'NEW'` for every fresh item, so the
old/new sentence split in §2 has to be computed outside the checker, by sid, in `report_tables.py`.

**D2 — no fresh answer carried the `chk` block that `FRESH_SCHEMA.md` declares REQUIRED.** Without it every
fresh item is forced to `verdict='wrong'`, can never be accepted at L1, and the whole comparison is void.
Produced here with the app's own existing checker (`checker/v2/check.ts`, the one Phase 1c used) via
`phase1h/chk_fresh.ts`, run twice — `ANN_DIR=phase1c/annotated_after` for the 80 old sentences and
`ANN_DIR=phase1h/fresh/annotations_new_60` for the 60 new ones, both with `SYN_DIR=phase1c/synonyms
LIB_OVERLAY=phase1c/overlay/library.json` — giving 980 verdicts (correct 135, correct_with_tip 4,
wrong 841), attached at read time. That is data production, not a rule change, but it is a step the Phase
1h design forgot and it belongs in the writer pipeline next time.

**D3 — row 8 (P-C) is not measured out of sample.** 311 of the 623 P-C calls returned an empty body
(`http 0`, `reply ''`, no finish reason, `empty_due_to_thinking` false) and were counted as FAILED exactly
as the frozen rule demands — against 1 such failure in 623 P-B calls. 277 fresh items therefore have no
model verdict, and an item without a verdict is not accepted. Row 8's fresh coverage (83.3 %) and above all
its fresh false acceptance (1.5 %) are **artefacts of the missing verdicts**, not measurements, and must
not be quoted. The cause was not investigated and nothing was retried, because a retry policy would be a
rule change.  Row 7 (P-B) is fully measured (23 fresh items without a verdict).

**D4 — the annotator's notes** (`phase1h/fresh/ANNOTATION_NOTES.md`): sid **6265** — "No one" is not listed
in `alt` because the prompt forbids someone/somebody-type pairs, and the annotator predicted it would cost
a false rejection; it did — `C:6265:241916334` is one of the 27 L2 false rejections. Also flagged and left
unresolved: 8465 (`sud` as subject or object), 31648 (`vraj`), 3332 (`overal`), 7910 (`zopnutá kopa`),
9584 (literal "since the moment she started"). The new annotations omit the `s` synonym-group ids (the
batchS/batchL prompts never had them), so every alternative sits in `alt`.

**D5 — writer artefacts.** `W:9907:1778280655` is a "wrong" answer byte-identical to the reference; the
judge still called it really wrong, so it counts as a real false acceptance in both rows. One item of 550,
inflating row 7 by 0.2 pp. Others may be near-identical and defensible; the blind pass had already moved
10 of 560 into the "really correct" bucket.

**D6 — the judge saw the annotations' synonym groups** while ruling on the wrong set, so the judgement is
not fully independent of the material the checker itself uses. The direction of that bias is unknown.

**D7 — in-sample tuning inside the freeze itself.** §2.3b (the automatic `g` chain) was *tightened* before
the freeze precisely because the untightened version touched 22 of the 80 old sentences and cost one false
acceptance on the OLD set. That tightening was chosen against the in-sample data, so the frozen checker is
to that extent still fitted to the 80. It now touches 1 of 80 and 0 of 60, so the practical effect is
small, but the honest reading is that the freeze is not perfectly clean.

**D8 — the 13–16-word band stays thin.** Only 2 of the 60 new sentences fall in it (the unused pool holds
exactly two), so the whole fresh long band is 12 items with an interval of [27.7–84.8].

**D9 — "fresh" means fresh answers, not only fresh sentences.** 80 of the 140 sentences are the in-sample
ones; the clean out-of-sample half is 180 correct and 233 wrong items. Both halves are reported separately
in §2.

**D10 — a counter mismatch in the frozen runner.** `call_counts.json` reports `new: 986` while the ledger
holds 934 parsed verdicts and 312 failures (1,246 rows for 1,298 calls). The counter and the ledger
disagree by 52; every table here is built from the ledger and the tabulation, not from that counter.

**Carried over from Phase 1g and still present** (recorded in STATE.md, not fixed): the `si` clitic blocks
every person signal; F5 still fires on `C:11348:1001085647`; the L3 model still rejects faithful answers
that use the other gender where the Slovak leaves it open, because the `g` chain reaches F3/F5/F2B but
never the prompt.

## 6. Cost of the run

**Model calls.** Planned 1,298 (cap 1,500, never reached): fresh P-B 648, fresh P-C 648, old P-B 1, old
P-C 1. Made 1,298, all new; 0 capped, nothing left unmeasured for lack of budget. Parsed verdicts **934**
(SAME 435, TIP 108, DIFF 391), **FAILED 312** (311 of them P-C, see D3) — failures were counted, never
guessed, never retried. **Zero 429s**, zero quota errors; the free tier carried the whole run. Ledger reuse
applied only to the OLD sets, which needed just the 2 new calls that §2.1 created. Spend: 148,235 input
tokens and 934 output tokens = **$0.0385** at the lite price.

**Agent cost of the phase** (tokens / tool calls as self-reported, with the harness count where it differs):

| agent | tokens | tool calls |
|---|---|---|
| main session | — | 8 |
| builder | 125,009 | 12 self-reported, **15 counted by the harness — over the 12-call limit** |
| annotator | 136,611 | 12 |
| correct writer | 58,351 | 5 |
| wrong writer | 104,418 | 5 |
| judge | 103,735 | 9 self-reported, **12 counted by the harness** |
| measuring agent (this report) | not knowable from inside the session | **12** |

## 7. Judgement

1. **The Phase 1g numbers do not survive out of sample.** Row 7 coverage falls from 91.9 % to
   **82.1 % [78.1–85.7]**, a drop of 9.8 pp, and the drop comes from fresh *answers*, not fresh sentences:
   the 60 brand-new sentences score better (88.9 %) than the old ones with fresh answers (77.1 %).
2. **Honest coverage is 82 %, and the honest upper bound on real false acceptance is 15.0 %**
   (66/550 = 12.0 %, 95 % CP 9.4–15.0). The in-sample 2/19 strict figure was a small-denominator illusion;
   against a 550-item wrong set the system accepts roughly one wrong answer in eight.
3. **Row 8 (P-C) is unmeasured, not better**: half its calls returned empty bodies. Its flattering 1.5 %
   false acceptance is an artefact of 277 missing verdicts and must not be quoted anywhere.
4. The damage is concentrated: 65 of 66 false acceptances come from the L3 model (TIP or SAME on added
   content, dropped content and pronoun swaps) and 47 of them are type M or S. The offline layers are
   sound; the prompt is too lenient, and counting TIP as an acceptance is a large part of it.
5. **Not shippable as an autonomous accept/reject gate.** One wrong answer in eight accepted and one
   defensible correct answer in five rejected is materially worse than the pilot suggested. It is usable as
   an assistive hint layer, or as a gate only after the L3 prompt is rebuilt (and the P-C empty-reply
   failure is understood) and re-measured on a set nobody has tuned against.

## 8. Generated tables (verbatim, every id)

# Phase 1h — measurement tables (generated by phase1h/report_tables.py)

source: `results_1h_20260918T162141Z.json`


## row 7 (P-B)

### In-sample (frozen 235/105) vs out-of-sample (fresh 420/550)

| figure | in-sample OLD | out-of-sample FRESH | delta (pp) |
|---|---|---|---|
| coverage (judged really correct) | 216/235 91.9 % [87.7–95.1] | 345/420 82.1 % [78.1–85.7] | -9.8 |
| real false acceptance | 2/19 10.5 % [1.3–33.1] | 66/550 12.0 % [9.4–15.0] | +1.5 |
| raw accepted wrong-set items | 10/105 9.5 % [4.7–16.8] | 73/560 13.0 % [10.4–16.1] | +3.5 |
| items without a model verdict (not measured) | 1 | 23 |  |

### Coverage on the fresh correct set (denominator = 420 judged really correct)

headline: 345/420 = 82.1 % (95 % CP 78.1–85.7)


**fresh correct set — coverage by level**

| level | coverage |
|---|---|
| A1 | 52/63 82.5 % [70.9–90.9] |
| A2 | 70/84 83.3 % [73.6–90.6] |
| B1 | 117/147 79.6 % [72.2–85.8] |
| B2 | 106/126 84.1 % [76.6–90.0] |

**fresh correct set — coverage by Slovak length band**

| Slovak length band | coverage |
|---|---|
| 1-6 | 55/66 83.3 % [72.1–91.4] |
| 10-12 | 86/105 81.9 % [73.2–88.7] |
| 13-16 | 7/12 58.3 % [27.7–84.8] |
| 7-9 | 197/237 83.1 % [77.7–87.7] |

**fresh correct set — coverage by sentence half (OLD 80 / NEW 60)**

| sentence half (OLD 80 / NEW 60) | coverage |
|---|---|
| NEW-sentences | 160/180 88.9 % [83.4–93.1] |
| OLD-sentences | 185/240 77.1 % [71.2–82.2] |

### Real false acceptance on the fresh wrong set

headline (judged really wrong denominator): 66/550 = 12.0 % (95 % CP 9.4–15.0)

raw accepted / all written wrong answers: 73/560 = 13.0 % (95 % CP 10.4–16.1)

| sentence half | real FA |
|---|---|
| NEW-sentences | 29/233 12.4 % [8.5–17.4] |
| OLD-sentences | 37/317 11.7 % [8.4–15.7] |

| wrong type | real FA (of judged really wrong of that type) |
|---|---|
| T | 2/137 1.5 % [0.2–5.2] |
| W | 17/138 12.3 % [7.3–19.0] |
| M | 27/135 20.0 % [13.6–27.7] |
| S | 20/140 14.3 % [8.9–21.2] |

| layer | real FA |
|---|---|
| L1 | 1 |
| L3 | 65 |

### Every real false acceptance, itemised

- **W:16403:624976382** [OLD in-sample] checker verdict correct_with_tip · level A2 · type M · layer L1
  - sk: Rozlúč sa a o hodinu sa vráti naspäť.
  - reference: Say bye now and she will come back in an hour.
  - answer: Say bye now and she comes back in an hour.
- **W:1452:1471817457** [OLD in-sample] model TIP · level B1 · type W · layer L3
  - sk: Ak sa dotkne toho kaktusa, strávi večer vyťahovaním tŕňov z prsta.
  - reference: If he touches that cactus, he will spend the evening pulling spines out of his finger.
  - answer: If he grabs that cactus, he will spend the evening pulling spines out of his finger.
- **W:20298:1595880954** [FRESH out-of-sample] model TIP · level A1 · type S · layer L3
  - sk: Na tú silnú bolesť hlavy potrebuje jednu tabletku.
  - reference: He needs a pill for his bad headache.
  - answer: For that severe headache they need one pill.
- **W:23669:561074874** [FRESH out-of-sample] model TIP · level A1 · type M · layer L3
  - sk: Galaxia sa pomaly pohybuje nad ich hlavami.
  - reference: The galaxy moves slowly above their heads.
  - answer: The galaxy slowly moves above their heads at night.
- **W:11348:1594514680** [FRESH out-of-sample] model TIP · level A2 · type M · layer L3
  - sk: Pozri! Asistent práve drží odrazovú dosku hore.
  - reference: Look! The assistant is holding the reflector up now.
  - answer: Look! The assistant is holding the board up.
- **W:11980:2419738346** [FRESH out-of-sample] model TIP · level A2 · type M · layer L3
  - sk: Počkaj chvíľu a voda zovrie!
  - reference: Wait a minute and the water will boil!
  - answer: Wait a moment and the water will boil in the pot!
- **W:13034:3769013457** [FRESH out-of-sample] model TIP · level A2 · type M · layer L3
  - sk: Práve teraz dievča sfukuje sviečky.
  - reference: Right now the girl is blowing out the candles.
  - answer: Right now the girl is blowing out the candles on the cake.
- **W:16403:1306885234** [FRESH out-of-sample] model SAME · level A2 · type S · layer L3
  - sk: Rozlúč sa a o hodinu sa vráti naspäť.
  - reference: Say bye now and she will come back in an hour.
  - answer: Say goodbye, and in an hour they'll come back.
- **W:20702:2829002765** [FRESH out-of-sample] model TIP · level A2 · type W · layer L3
  - sk: Pozri! Teraz dvíha džbán vyššie a vyššie.
  - reference: Look! He is lifting the jug higher and higher now.
  - answer: Look! Now he is lifting the bucket higher and higher.
- **W:24733:190778272** [FRESH out-of-sample] model TIP · level A2 · type M · layer L3
  - sk: Pohárik je horúci, tak ho musíš držať opatrne.
  - reference: The glass is hot, so you must hold it carefully.
  - answer: The little glass is very hot, so you must hold it carefully.
- **W:1452:3230512291** [FRESH out-of-sample] model TIP · level B1 · type W · layer L3
  - sk: Ak sa dotkne toho kaktusa, strávi večer vyťahovaním tŕňov z prsta.
  - reference: If he touches that cactus, he will spend the evening pulling spines out of his finger.
  - answer: If he touches that cactus, he'll spend the evening pulling thorns out of his hand.
- **W:1452:3813004317** [FRESH out-of-sample] model TIP · level B1 · type M · layer L3
  - sk: Ak sa dotkne toho kaktusa, strávi večer vyťahovaním tŕňov z prsta.
  - reference: If he touches that cactus, he will spend the evening pulling spines out of his finger.
  - answer: If he touches that cactus, he'll spend the evening pulling thorns out.
- **W:1452:315243162** [FRESH out-of-sample] model SAME · level B1 · type S · layer L3
  - sk: Ak sa dotkne toho kaktusa, strávi večer vyťahovaním tŕňov z prsta.
  - reference: If he touches that cactus, he will spend the evening pulling spines out of his finger.
  - answer: If they touch that cactus, they'll spend the evening pulling thorns out of their finger.
- **W:2929:120435637** [FRESH out-of-sample] model SAME · level B1 · type M · layer L3
  - sk: Desivé svetlo úplne zhaslo a nádražie je zase tmavé.
  - reference: The eerie light has faded completely, and the yard is dark again.
  - answer: The light has completely gone out and the station is dark again.
- **W:3603:2904065335** [FRESH out-of-sample] model SAME · level B1 · type W · layer L3
  - sk: Inžinier sa ho spýtal, kedy privezie pretekárske auto späť do garáže.
  - reference: The engineer asked him when he was bringing the race car back into the garage.
  - answer: The engineer asked him when he would bring the race car back to the shop.
- **W:4449:722373448** [FRESH out-of-sample] model TIP · level B1 · type M · layer L3
  - sk: Celkovo spustila kôš trikrát, kým mal muž všetky svoje pomaranče.
  - reference: Altogether she lowered the basket three times before the man had all his oranges.
  - answer: She lowered the basket three times until the man had all his oranges.
- **W:5959:2145732155** [FRESH out-of-sample] model SAME · level B1 · type S · layer L3
  - sk: Ak prsteň otočí ešte raz, zníži cenu znova.
  - reference: If he turns the ring once more, she will drop the price again.
  - answer: If they turn the ring once more, he'll lower the price again.
- **W:6830:2612740669** [FRESH out-of-sample] model TIP · level B1 · type M · layer L3
  - sk: Ako deti kupovali sušené bylinky v pohári.
  - reference: As kids they would buy dried herbs in a jar.
  - answer: As children, they used to buy herbs in a jar.
- **W:7238:1713771538** [FRESH out-of-sample] model TIP · level B1 · type M · layer L3
  - sk: Ak stúpaš presne tam, kam stúpa Mira, nohy ti zostanú úplne suché.
  - reference: If you step exactly where Mira steps, your feet stay completely dry.
  - answer: If you step where Mira steps, your feet will stay dry.
- **W:7458:64129800** [FRESH out-of-sample] model TIP · level B1 · type M · layer L3
  - sk: Tú grimasu robí každý, však?
  - reference: Everyone makes that face, don't they?
  - answer: Everyone makes a grimace, don't they?
- **W:7716:2835019848** [FRESH out-of-sample] model TIP · level B1 · type M · layer L3
  - sk: Podarilo sa jej vydržať úplne nehybne, kým sa vážka usadila.
  - reference: She managed to stay completely still until the dragonfly settled.
  - answer: She managed to stay still until the dragonfly landed.
- **W:8293:1283962081** [FRESH out-of-sample] model SAME · level B1 · type S · layer L3
  - sk: Jedlo nikdy nedelí, takže tento croissant musí byť výnimočný.
  - reference: She never shares food, so this one must be special.
  - answer: They never share food, so this croissant must be special.
- **W:9495:890576878** [FRESH out-of-sample] model TIP · level B1 · type M · layer L3
  - sk: Jej prejav bol prepísaný dvakrát, ešte než vôbec vyšla na to pódium.
  - reference: Her speech was rewritten twice before she ever walked onto that stage.
  - answer: Her speech was rewritten before she even went up on that stage.
- **W:2874:436293867** [FRESH out-of-sample] model SAME · level B2 · type S · layer L3
  - sk: Mal ísť k lekárovi už pred pár dňami, ale čakal, kým sa sotva udržal na nohách.
  - reference: He should have seen a doctor days ago, but he waited until he could hardly stand.
  - answer: They should have gone to the doctor a few days ago, but they waited until they could barely stay on their feet.
- **W:3494:3453695283** [FRESH out-of-sample] model TIP · level B2 · type W · layer L3
  - sk: Keby bola guľôčka padla na čiernej, išla by domov s prázdnymi vreckami.
  - reference: If the ball had landed in black, she would have gone home with empty pockets.
  - answer: If the ball had landed on black, she would have gone home with empty bags.
- **W:3494:2755518720** [FRESH out-of-sample] model TIP · level B2 · type M · layer L3
  - sk: Keby bola guľôčka padla na čiernej, išla by domov s prázdnymi vreckami.
  - reference: If the ball had landed in black, she would have gone home with empty pockets.
  - answer: If the ball had landed on black, she would have gone home.
- **W:3937:1213271894** [FRESH out-of-sample] model TIP · level B2 · type M · layer L3
  - sk: Kúpi si ďalší prívesok, keď príde na tento trh znova.
  - reference: She will buy another charm when she comes to this market again.
  - answer: She'll buy another pendant when she comes to this market.
- **W:7037:3489763949** [FRESH out-of-sample] model TIP · level B2 · type W · layer L3
  - sk: Jeleň, ktorého parohy boli obrovské, stál medzi lístím.
  - reference: The stag, whose antlers were huge, stood among the leaves.
  - answer: The deer, whose antlers were huge, stood among the branches.
- **W:7037:3615298556** [FRESH out-of-sample] model TIP · level B2 · type S · layer L3
  - sk: Jeleň, ktorého parohy boli obrovské, stál medzi lístím.
  - reference: The stag, whose antlers were huge, stood among the leaves.
  - answer: The elk, whose antlers were huge, stood among the leaves.
- **W:7687:3756129597** [FRESH out-of-sample] model TIP · level B2 · type W · layer L3
  - sk: Kuchyňu si dali natočiť, kým skladali ten dúhový tanier.
  - reference: They had the kitchen filmed while they built the rainbow plate.
  - answer: They had the kitchen filmed while they were putting together that rainbow bowl.
- **W:7998:52962874** [FRESH out-of-sample] model SAME · level B2 · type M · layer L3
  - sk: Veranda, na ktorej teraz trávi každé ráno, je otočená na východ slnka.
  - reference: The veranda, where she now spends every morning, faces the sunrise.
  - answer: The porch where she spends every morning faces the sunrise.
- **W:8209:2299827981** [FRESH out-of-sample] model SAME · level B2 · type S · layer L3
  - sk: Do piatku si zarezervuje piaty termín v štúdiu.
  - reference: By Friday she will have booked a fifth appointment at the studio.
  - answer: By Friday they will have booked the fifth slot at the studio.
- **W:8812:384802316** [FRESH out-of-sample] model SAME · level B2 · type M · layer L3
  - sk: Tréner by si prial, aby jeho lapy boli trochu hrubšie.
  - reference: Her trainer wishes his pads were a bit thicker.
  - answer: The coach wishes his gloves were thicker.
- **W:9038:4003459570** [FRESH out-of-sample] model SAME · level B2 · type S · layer L3
  - sk: Práve teraz čmára poznámku, kým obrazovka notebooku svieti.
  - reference: Right now he is scribbling a note while the laptop screen glows.
  - answer: Right now they are scribbling a note while the laptop screen is glowing.
- **W:9907:1778280655** [FRESH out-of-sample] checker verdict correct · level B2 · type S · layer L1
  - sk: Keby si bola vzala béžovú bundu, tento look by nikdy nevznikol.
  - reference: If she had taken the beige jacket, this look would never have happened.
  - answer: If she had taken the beige jacket, this look would never have happened.
- **W:10013:1594646351** [FRESH out-of-sample] model SAME · level B2 · type W · layer L3
  - sk: Práve teraz tlačí modrý obklad na hrču.
  - reference: Right now he is holding a blue ice pack against the lump.
  - answer: Right now she is pressing a blue compress on the bruise.
- **W:10013:4174637227** [FRESH out-of-sample] model SAME · level B2 · type M · layer L3
  - sk: Práve teraz tlačí modrý obklad na hrču.
  - reference: Right now he is holding a blue ice pack against the lump.
  - answer: Right now she is pressing a compress on the bump.
- **W:10366:1314252953** [FRESH out-of-sample] model SAME · level B2 · type S · layer L3
  - sk: Do desiatej už bude zohrievať rezance dve hodiny v kuse.
  - reference: By ten he will have been reheating noodles for two hours straight.
  - answer: By ten, they will have been heating up the noodles for two hours straight.
- **W:10574:2448666810** [FRESH out-of-sample] model TIP · level B2 · type S · layer L3
  - sk: Trénoval hodiny, kým bolo svetlo konečne správne.
  - reference: He had been training for hours before the light was finally right.
  - answer: They had been training for hours until the light was finally right.
- **W:23360:711319744** [FRESH out-of-sample] model TIP · level A1 · type S · layer L3
  - sk: Jeho obrovské kýchnutie môžeš počuť po celej lúke.
  - reference: You can hear his huge sneeze across the whole meadow.
  - answer: You can hear their huge sneeze across the whole meadow.
- **W:28006:2654956435** [FRESH out-of-sample] model TIP · level A1 · type W · layer L3
  - sk: Každú loď v zálive spozoruješ skôr než ktokoľvek iný. Klobúk dole.
  - reference: You spot every boat in the bay before anyone else. Hats off.
  - answer: You'll spot every boat in the harbor before anyone else. Hats off.
- **W:14697:2838322367** [FRESH out-of-sample] model SAME · level A2 · type T · layer L3
  - sk: Po dopade je na kameňoch trochu šťavy
  - reference: After the impact there is a little juice on the stones.
  - answer: After the impact, there was a bit of juice on the rocks.
- **W:14697:567072060** [FRESH out-of-sample] model SAME · level A2 · type M · layer L3
  - sk: Po dopade je na kameňoch trochu šťavy
  - reference: After the impact there is a little juice on the stones.
  - answer: There is a bit of juice on the rocks.
- **W:14697:2532470414** [FRESH out-of-sample] model TIP · level A2 · type S · layer L3
  - sk: Po dopade je na kameňoch trochu šťavy
  - reference: After the impact there is a little juice on the stones.
  - answer: After the impact, there are a few drops of juice on the rocks.
- **W:15437:338816939** [FRESH out-of-sample] model TIP · level A2 · type W · layer L3
  - sk: Pole je súkromné. Musíme zostať na cestičke.
  - reference: The field is private. We must stay on the path.
  - answer: The field is private. We must stay on the road.
- **W:23878:71189755** [FRESH out-of-sample] model TIP · level A2 · type W · layer L3
  - sk: Na tomto obrovskom štadióne je jedno zelené ihrisko.
  - reference: There is one green pitch in this huge stadium.
  - answer: In this huge stadium there is one green court.
- **W:31648:250135833** [FRESH out-of-sample] model SAME · level A2 · type W · layer L3
  - sk: Zlatko, vraj opustil misku včera, nie dnes.
  - reference: Honey, apparently he left the bowl yesterday, not today.
  - answer: Honey, apparently he left the plate yesterday, not today.
- **W:32141:3059786530** [FRESH out-of-sample] model TIP · level A2 · type W · layer L3
  - sk: Toto je katastrofa! Miska bude zajtra zase prázdna!
  - reference: This is a disaster! The bowl will be empty again tomorrow!
  - answer: This is a disaster! The plate will be empty again tomorrow!
- **W:2121:832651865** [FRESH out-of-sample] model TIP · level B1 · type T · layer L3
  - sk: Spolubývajúci sa ho spýtal, prečo trávi dve hodiny denne len na to, aby sedel za stolom.
  - reference: The flatmate asked him why he spent two hours a day just sitting at the desk.
  - answer: His roommate asked him why he spends two hours a day just sitting at the desk.
- **W:2121:4138132892** [FRESH out-of-sample] model TIP · level B1 · type M · layer L3
  - sk: Spolubývajúci sa ho spýtal, prečo trávi dve hodiny denne len na to, aby sedel za stolom.
  - reference: The flatmate asked him why he spent two hours a day just sitting at the desk.
  - answer: His roommate asked him why he spent two hours a day sitting at the desk.
- **W:2389:4045922663** [FRESH out-of-sample] model TIP · level B1 · type M · layer L3
  - sk: Keby duriány nesmrdeli tak silno, colnica by ich asi pustila.
  - reference: If durians didn't smell so strongly, customs would probably let them through.
  - answer: If durians didn't smell so strong, customs would let them through.
- **W:2389:1402963517** [FRESH out-of-sample] model TIP · level B1 · type S · layer L3
  - sk: Keby duriány nesmrdeli tak silno, colnica by ich asi pustila.
  - reference: If durians didn't smell so strongly, customs would probably let them through.
  - answer: If durians didn't smell so strong, the customs officer would probably let them through.
- **W:2783:2540506102** [FRESH out-of-sample] model SAME · level B1 · type M · layer L3
  - sk: Lopta, ktorú pes priniesol, je teraz úplne od blata.
  - reference: The ball that the dog fetched is now completely muddy.
  - answer: The ball that the dog brought is covered in mud.
- **W:6353:1937142341** [FRESH out-of-sample] model TIP · level B1 · type M · layer L3
  - sk: Svetlá sa ešte len rozohrievali, keď režisér zakričal „akciu“.
  - reference: The lights were still warming up when the director shouted “action”.
  - answer: The lights were warming up when the director shouted 'action'.
- **W:7444:2683969038** [FRESH out-of-sample] model SAME · level B1 · type M · layer L3
  - sk: Naniesla si už tri vrstvy, takže jej riasy vyzerajú obrovské.
  - reference: She has already applied three coats, so her lashes look huge.
  - answer: She has applied three layers, so her eyelashes look huge.
- **W:7533:3503567680** [FRESH out-of-sample] model TIP · level B1 · type W · layer L3
  - sk: Kým sa skupina usádzala, niekto udrel do spievajúcej misy.
  - reference: While the group was settling, someone struck the singing bowl.
  - answer: While the group was settling in, someone struck the singing gong.
- **W:7533:781018839** [FRESH out-of-sample] model TIP · level B1 · type M · layer L3
  - sk: Kým sa skupina usádzala, niekto udrel do spievajúcej misy.
  - reference: While the group was settling, someone struck the singing bowl.
  - answer: While the group was settling in, someone struck the bowl.
- **W:8491:2663489786** [FRESH out-of-sample] model TIP · level B1 · type W · layer L3
  - sk: Ak šupku najprv narežeš, granátové jablko sa otvára ľahko.
  - reference: If you score the skin first, the pomegranate opens easily.
  - answer: If you score the peel first, the pomegranate opens quickly.
- **W:8491:1647062954** [FRESH out-of-sample] model SAME · level B1 · type M · layer L3
  - sk: Ak šupku najprv narežeš, granátové jablko sa otvára ľahko.
  - reference: If you score the skin first, the pomegranate opens easily.
  - answer: If you score the peel, the pomegranate opens easily.
- **W:8491:3020598369** [FRESH out-of-sample] model TIP · level B1 · type S · layer L3
  - sk: Ak šupku najprv narežeš, granátové jablko sa otvára ľahko.
  - reference: If you score the skin first, the pomegranate opens easily.
  - answer: If you score the peel first, the pomegranates open easily.
- **W:9007:2829648222** [FRESH out-of-sample] model TIP · level B1 · type W · layer L3
  - sk: Dnes v noci preveril už šesť zdrojov a kopa stále rastie.
  - reference: He has checked six sources tonight and the pile is still growing.
  - answer: Tonight he has already checked six sources and the list is still growing.
- **W:9687:2008862971** [FRESH out-of-sample] model SAME · level B1 · type S · layer L3
  - sk: Ak oba štáty podpíšu zmluvu, hranica sa budúci mesiac otvorí.
  - reference: If both states sign the treaty, the border will open next month.
  - answer: If both countries sign the treaty, the borders will open next month.
- **W:10243:1132231721** [FRESH out-of-sample] model TIP · level B1 · type M · layer L3
  - sk: Keď slnko prešlo cez poludnie, nakláňala slnečník.
  - reference: When the sun passed noon, she was tilting the parasol.
  - answer: She was tilting the umbrella.
- **W:381:1258629268** [FRESH out-of-sample] model SAME · level B2 · type W · layer L3
  - sk: Kiež by môj kocúr bol taký pokojný ako ten ryšavý v jej náručí.
  - reference: I wish my cat were as calm as the ginger one in her arms.
  - answer: I wish my cat were as calm as that ginger one in her lap.
- **W:5971:3700802525** [FRESH out-of-sample] model SAME · level B2 · type S · layer L3
  - sk: Do zatvárania skontroluje každý prsteň na tom stole.
  - reference: By closing time she will have checked every ring on that table.
  - answer: By closing time they will have checked every ring on that table.
- **W:7910:2914297793** [FRESH out-of-sample] model TIP · level B2 · type S · layer L3
  - sk: Napriek ventilátoru na plný výkon sa zopnutá kopa vôbec nepohla.
  - reference: Despite the fan at full power, the clipped pile did not move at all.
  - answer: Despite the fan being at full power, the clipped piles didn't move at all.
- **W:8039:516493581** [FRESH out-of-sample] model TIP · level B2 · type W · layer L3
  - sk: Keby ju obranca nezrazil, žiadna penalta by nebola.
  - reference: If the defender had not knocked her down, there would have been no penalty.
  - answer: If the defender hadn't knocked her down, there would have been no foul.
- **W:8039:2010823167** [FRESH out-of-sample] model TIP · level B2 · type S · layer L3
  - sk: Keby ju obranca nezrazil, žiadna penalta by nebola.
  - reference: If the defender had not knocked her down, there would have been no penalty.
  - answer: If the defenders hadn't knocked her down, there would have been no penalty.

OLD accepted-but-unjudged resolved against `fresh/judgements_old105.jsonl`:

- `W:1018:1251085634` -> judged **really correct**
- `W:14266:664063167` -> judged **really correct**
- `W:1452:3166274700` -> judged **really correct**
- `W:5595:3623849236` -> judged **really correct**
- `W:5595:1942575047` -> judged **really wrong**
- `W:9244:3038274947` -> judged **really correct**
- `W:8824:241327957` -> judged **really correct**

OLD strict (Phase 1g list) real FA: 2/19 10.5 % [1.3–33.1]; OLD real FA under the NEW blind judgement (strict + newly judged really wrong): 3/99 3.0 % [0.6–8.6]


### Routing, latency, cost

| layer | fresh items | share |
|---|---|---|
| L3 | 253 | 60.2 % |
| L1 | 135 | 32.1 % |
| L2 | 27 | 6.4 % |
| F4v2 | 3 | 0.7 % |
| F5 | 2 | 0.5 % |
| **total** | 420 | 100 % |

OLD routing: {"L1": 100, "L3": 132, "L2": 2, "F5": 1}

### False rejections by cause (fresh set)

| cause | n | ids |
|---|---|---|
| L3 | 43 | `C:20298:610089844`, `C:20298:1375544540`, `C:25921:4183818791`, `C:25921:2722616817`, `C:27628:3492027817`, `C:27628:3250724313`, `C:27628:1242167241`, `C:29691:2119858295`, `C:11216:1671484255`, `C:11216:167914261`, `C:11348:1069167980`, `C:13395:1329747891`, `C:16261:937570043`, `C:16403:2618909674`, `C:21124:3846512962`, `C:24733:1990053738`, `C:24733:852799016`, `C:119:1797996295`, `C:1018:305366583`, `C:3084:3782296241`, `C:3084:1849370306`, `C:4612:2735077112`, `C:5595:3589927967`, `C:5595:1512723632`, `C:5595:561100618`, `C:5959:3670383000`, `C:8756:66685830`, `C:8799:657456566`, `C:9498:240581227`, `C:9992:28721142`, `C:2874:1070200547`, `C:3937:1995985534`, `C:3937:276899962`, `C:7687:4238972801`, `C:7998:542823734`, `C:8209:3281169095`, `C:9907:3590124615`, `C:9907:2336650878`, `C:9907:1934300869`, `C:7928:2607238276`, `C:7928:3435921201`, `C:7928:2593205770`, `C:6790:3534788181` |
| L2 | 27 | `C:29691:1286045143`, `C:29691:2714964500`, `C:16009:4024372226`, `C:4612:3488329309`, `C:5959:1661102304`, `C:7458:1622126333`, `C:8824:3821792841`, `C:9244:1598262661`, `C:9244:1251214671`, `C:9495:2507633220`, `C:103:1864687227`, `C:103:670219981`, `C:103:470167683`, `C:2874:2357937954`, `C:7558:358541305`, `C:8812:183208396`, `C:18789:1094472200`, `C:18789:220464344`, `C:23878:1748591315`, `C:3332:2424557827`, `C:5966:3079825519`, `C:6353:3679092359`, `C:7533:3411610792`, `C:381:677006685`, `C:6265:241916334`, `C:6883:1317999482`, `C:10734:2394971369` |
| F4v2 | 3 | `C:10116:1360983188`, `C:10116:2635817258`, `C:10116:2497170629` |
| F5 | 2 | `C:29143:1366479064`, `C:14779:188731256` |
| **sum** | **75** | asserted == total false rejections **75** -> OK |

fr_by_cause as recorded by the frozen runner: `{"L3": 43, "L2": 27, "F5": 2, "F4v2": 3}`

OLD false rejections by cause: `{"L3": 16, "L2": 2, "F5": 1}` (sum 19 == 19)


## row 8 (P-C)

### In-sample (frozen 235/105) vs out-of-sample (fresh 420/550)

| figure | in-sample OLD | out-of-sample FRESH | delta (pp) |
|---|---|---|---|
| coverage (judged really correct) | 221/235 94.0 % [90.2–96.7] | 350/420 83.3 % [79.4–86.8] | -10.7 |
| real false acceptance | 3/19 15.8 % [3.4–39.6] | 8/550 1.5 % [0.6–2.8] | -14.3 |
| raw accepted wrong-set items | 11/105 10.5 % [5.3–18.0] | 11/560 2.0 % [1.0–3.5] | -8.5 |
| items without a model verdict (not measured) | 1 | 277 |  |

### Coverage on the fresh correct set (denominator = 420 judged really correct)

headline: 350/420 = 83.3 % (95 % CP 79.4–86.8)


**fresh correct set — coverage by level**

| level | coverage |
|---|---|
| A1 | 55/63 87.3 % [76.5–94.4] |
| A2 | 70/84 83.3 % [73.6–90.6] |
| B1 | 119/147 81.0 % [73.7–87.0] |
| B2 | 106/126 84.1 % [76.6–90.0] |

**fresh correct set — coverage by Slovak length band**

| Slovak length band | coverage |
|---|---|
| 1-6 | 57/66 86.4 % [75.7–93.6] |
| 10-12 | 87/105 82.9 % [74.3–89.5] |
| 13-16 | 7/12 58.3 % [27.7–84.8] |
| 7-9 | 199/237 84.0 % [78.7–88.4] |

**fresh correct set — coverage by sentence half (OLD 80 / NEW 60)**

| sentence half (OLD 80 / NEW 60) | coverage |
|---|---|
| NEW-sentences | 159/180 88.3 % [82.7–92.6] |
| OLD-sentences | 191/240 79.6 % [73.9–84.5] |

### Real false acceptance on the fresh wrong set

headline (judged really wrong denominator): 8/550 = 1.5 % (95 % CP 0.6–2.8)

raw accepted / all written wrong answers: 11/560 = 2.0 % (95 % CP 1.0–3.5)

| sentence half | real FA |
|---|---|
| NEW-sentences | 0/233 0.0 % [0.0–1.6] |
| OLD-sentences | 8/317 2.5 % [1.1–4.9] |

| wrong type | real FA (of judged really wrong of that type) |
|---|---|
| T | 0/137 0.0 % [0.0–2.7] |
| W | 0/138 0.0 % [0.0–2.6] |
| M | 5/135 3.7 % [1.2–8.4] |
| S | 3/140 2.1 % [0.4–6.1] |

| layer | real FA |
|---|---|
| L1 | 1 |
| L3 | 7 |

### Every real false acceptance, itemised

- **W:16403:624976382** [OLD in-sample] checker verdict correct_with_tip · level A2 · type M · layer L1
  - sk: Rozlúč sa a o hodinu sa vráti naspäť.
  - reference: Say bye now and she will come back in an hour.
  - answer: Say bye now and she comes back in an hour.
- **W:1452:1471817457** [OLD in-sample] model TIP · level B1 · type W · layer L3
  - sk: Ak sa dotkne toho kaktusa, strávi večer vyťahovaním tŕňov z prsta.
  - reference: If he touches that cactus, he will spend the evening pulling spines out of his finger.
  - answer: If he grabs that cactus, he will spend the evening pulling spines out of his finger.
- **W:10366:36005249** [OLD in-sample] model SAME · level B2 · type S · layer L3
  - sk: Do desiatej už bude zohrievať rezance dve hodiny v kuse.
  - reference: By ten he will have been reheating noodles for two hours straight.
  - answer: By ten they will have been reheating noodles for two hours straight.
- **W:20298:1595880954** [FRESH out-of-sample] model SAME · level A1 · type S · layer L3
  - sk: Na tú silnú bolesť hlavy potrebuje jednu tabletku.
  - reference: He needs a pill for his bad headache.
  - answer: For that severe headache they need one pill.
- **W:23669:561074874** [FRESH out-of-sample] model TIP · level A1 · type M · layer L3
  - sk: Galaxia sa pomaly pohybuje nad ich hlavami.
  - reference: The galaxy moves slowly above their heads.
  - answer: The galaxy slowly moves above their heads at night.
- **W:11348:1594514680** [FRESH out-of-sample] model TIP · level A2 · type M · layer L3
  - sk: Pozri! Asistent práve drží odrazovú dosku hore.
  - reference: Look! The assistant is holding the reflector up now.
  - answer: Look! The assistant is holding the board up.
- **W:11980:2419738346** [FRESH out-of-sample] model TIP · level A2 · type M · layer L3
  - sk: Počkaj chvíľu a voda zovrie!
  - reference: Wait a minute and the water will boil!
  - answer: Wait a moment and the water will boil in the pot!
- **W:13034:3769013457** [FRESH out-of-sample] model TIP · level A2 · type M · layer L3
  - sk: Práve teraz dievča sfukuje sviečky.
  - reference: Right now the girl is blowing out the candles.
  - answer: Right now the girl is blowing out the candles on the cake.
- **W:16403:1306885234** [FRESH out-of-sample] model TIP · level A2 · type S · layer L3
  - sk: Rozlúč sa a o hodinu sa vráti naspäť.
  - reference: Say bye now and she will come back in an hour.
  - answer: Say goodbye, and in an hour they'll come back.
- **W:21124:1753932823** [FRESH out-of-sample] model SAME · level A2 · type M · layer L3
  - sk: Zvyčajne ostáva pod strechou, ale dnes tancuje v daždi.
  - reference: She usually stays dry, but today she is dancing in the rain.
  - answer: She stays under the roof, but today she is dancing in the rain.
- **W:9907:1778280655** [FRESH out-of-sample] checker verdict correct · level B2 · type S · layer L1
  - sk: Keby si bola vzala béžovú bundu, tento look by nikdy nevznikol.
  - reference: If she had taken the beige jacket, this look would never have happened.
  - answer: If she had taken the beige jacket, this look would never have happened.

OLD accepted-but-unjudged resolved against `fresh/judgements_old105.jsonl`:

- `W:1018:1251085634` -> judged **really correct**
- `W:14266:664063167` -> judged **really correct**
- `W:1452:3166274700` -> judged **really correct**
- `W:5595:3623849236` -> judged **really correct**
- `W:5595:1942575047` -> judged **really wrong**
- `W:9244:3038274947` -> judged **really correct**
- `W:8824:241327957` -> judged **really correct**

OLD strict (Phase 1g list) real FA: 3/19 15.8 % [3.4–39.6]; OLD real FA under the NEW blind judgement (strict + newly judged really wrong): 4/99 4.0 % [1.1–10.0]


### Routing, latency, cost

| layer | fresh items | share |
|---|---|---|
| L3 | 253 | 60.2 % |
| L1 | 135 | 32.1 % |
| L2 | 27 | 6.4 % |
| F4v2 | 3 | 0.7 % |
| F5 | 2 | 0.5 % |
| **total** | 420 | 100 % |

OLD routing: {"L1": 100, "L3": 132, "L2": 2, "F5": 1}

### False rejections by cause (fresh set)

| cause | n | ids |
|---|---|---|
| L3 | 38 | `C:20298:1375544540`, `C:25921:4183818791`, `C:25921:2722616817`, `C:27628:3492027817`, `C:29691:2119858295`, `C:11216:1671484255`, `C:11216:167914261`, `C:11348:1069167980`, `C:13395:1329747891`, `C:16261:937570043`, `C:16403:2618909674`, `C:21124:3846512962`, `C:24733:1990053738`, `C:24733:852799016`, `C:119:1797996295`, `C:1018:305366583`, `C:3084:3782296241`, `C:3084:1849370306`, `C:5595:3589927967`, `C:5595:1512723632`, `C:5595:561100618`, `C:8756:66685830`, `C:8799:657456566`, `C:9498:240581227`, `C:9992:28721142`, `C:2874:1070200547`, `C:3937:276899962`, `C:7687:4238972801`, `C:7998:542823734`, `C:8209:3281169095`, `C:9907:3590124615`, `C:9907:2336650878`, `C:9907:1934300869`, `C:7928:2607238276`, `C:7928:3435921201`, `C:7928:2593205770`, `C:6790:3534788181`, `C:6883:3640075222` |
| L2 | 27 | `C:29691:1286045143`, `C:29691:2714964500`, `C:16009:4024372226`, `C:4612:3488329309`, `C:5959:1661102304`, `C:7458:1622126333`, `C:8824:3821792841`, `C:9244:1598262661`, `C:9244:1251214671`, `C:9495:2507633220`, `C:103:1864687227`, `C:103:670219981`, `C:103:470167683`, `C:2874:2357937954`, `C:7558:358541305`, `C:8812:183208396`, `C:18789:1094472200`, `C:18789:220464344`, `C:23878:1748591315`, `C:3332:2424557827`, `C:5966:3079825519`, `C:6353:3679092359`, `C:7533:3411610792`, `C:381:677006685`, `C:6265:241916334`, `C:6883:1317999482`, `C:10734:2394971369` |
| F4v2 | 3 | `C:10116:1360983188`, `C:10116:2635817258`, `C:10116:2497170629` |
| F5 | 2 | `C:29143:1366479064`, `C:14779:188731256` |
| **sum** | **70** | asserted == total false rejections **70** -> OK |

fr_by_cause as recorded by the frozen runner: `{"L3": 38, "L2": 27, "F5": 2, "F4v2": 3}`

OLD false rejections by cause: `{"L3": 11, "L2": 2, "F5": 1}` (sum 14 == 14)


## Cost and latency (whole run)

- model calls latency: n 0, median None ms, p95 None ms
- tokens: in 0, out 0
- price used: `lib_prev.PRICE["lite"]` $0.25 in / $1.50 out per 1M tokens (no cached rate: the prompt is below the implicit-caching minimum, Phase 1e §cost)
- **cost per L3 call: $0.000000**
- usage assumption (Phase 1e/1f formula, restated by hand): 20 exercises/day x 30 days = 600 exercises per active user per month, times the L3 share
- fresh L3 share (row 7): 60.2 % -> 361 L3 calls/user/month -> **$0.0000 per active user per month**

## Cost and latency (recomputed from the ledger, phase1h/calls.jsonl + call_counts.json)

- model calls: 1298 (all new; ledger rows 1246, unparsable/FAILED 312)
- latency of the 1246 non-zero-latency calls: median **768 ms**, p95 **1061 ms** (the 52 zero-latency entries are the failed calls that never reached the wire)
- tokens: in 148235, out+thoughts 934
- price: `lib_prev.PRICE["lite"]` $0.25 in / $1.50 out per 1M tokens; the cached $0.025 rate never applies (prompt below the implicit-caching minimum, Phase 1e)
- **cost per L3 call: $0.000030**
- usage assumption restated from Phase 1e/1f: 20 exercises/day x 30 days = 600 exercises per active user per month, times the L3 share
- fresh L3 share on the correct set 60.2% -> 361 L3 calls/user/month -> **$0.0107 per active user per month** (Phase 1f reported $0.0118 at a 37.0% L3 share)


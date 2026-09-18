# Task C — offline guards that cut false acceptance (DEV only, 0 model calls)

Agent C, 18 Sept 2026. Deliverable `phase1i/taskC/guards_c.py` (+ `results.json`, re-runnable:
`python3 phase1i/taskC/guards_c.py --selftest --measure`). `phase1i/checker_1i.py` was NOT modified.
Everything below is measured on DEV (203 correct / 260 wrong-and-really-wrong) by replaying the frozen
row-7 (P-B) model verdicts out of `dev/items.jsonl`; a guard that fires rejects before the model layer,
so no call was made and none is needed.

**Apparatus check first** (printed by `--measure`, asserted): the baseline reproduces row 7 exactly —
coverage 160/203, FA 30/260, and the 30 ids are byte-identical to `dev/false_acceptances.json`.
Under the Task A switch (L3 `TIP` = rejection) the same code gives coverage 149/203, FA 8/260.

## 1 The three guards

| guard | what it is | how it decides |
|---|---|---|
| **F5t** (C2) | F5 *tightened* | F5 needs the answer to be a pure order-preserving **subsequence** of an accepted rendering, so one substituted word anywhere ("thorns" for "spines") silences it for the whole sentence. F5t replaces the subsequence test by a `difflib` diff of the option-stripped token lists: only **`delete`** hunks are deletions, **`replace`** hunks are word choice and are left to F3/the model. The information test is F5's own `span_information()`. |
| **F6** (C1) | the mirror: added meaning | same diff, **`insert`** hunks. Fires only when the inserted span is a **prepositional phrase** (`PREP_HEADS` head + ≥2 tokens) containing a content word that **no** accepted rendering, no `alt`, no `d` optional and no synonym group of the sentence contains — *in the pot*, *at night*, *on the cake*. |
| **F4v3** (C3) | the missing number signal | `sk_features()` + one extra **number-only** signal, consulted **only when F4v2 found no signal at all** (F4v3 is therefore a strict superset of F4v2: wherever F4v2 spoke, F4v3 decides identically). Signals: the byť-future paradigm (`budem…budú`, incl. `ne-`) and the unambiguous present endings `-uje` → sg, `-ujú`/`-ajú` → pl. Only read in a **single-clause** Slovak sentence. |

Why this diagnosis (C2): **all 30 DEV false acceptances are "MIXED"** — not one of them is a pure
subsequence of, or a pure superset of, any accepted rendering. That is the whole reason F5 catches none of
them: every one of them substitutes a word somewhere (*rocks/stones*, *pendant/charm*, *thorns/spines*) and
F5's subsequence test dies on the substitution before it ever looks at the span that is missing. Nine of the
twelve type-M failures are a substitution **plus** a dropped adjunct or **plus** an inserted PP.

Three structural protections carry both diff guards, all three verified on synthetic rows before use:
*(a)* `replace` hunks never fire (difflib emits an adjacent insert+delete as one `replace`, so pairing an
addition with the word it replaces needs no heuristic); *(b)* `_unpair()` also drops a delete and an insert
sitting within 3 reference positions of each other (a displaced substitution: *"Honey, apparently he left"*
→ *"Honey, he supposedly left"*); *(c)* `_drop_moves()` drops a token that is still present in the other
sentence in **any** form — same token, same stem via the checker's own `IRREG` table (*left/leave*,
*carefully/careful*, *lashes/eyelash*), or another negative word for a dropped negation.

Deliberate asymmetry in F6: a bare added word is almost never added meaning — it is usually a
re-realisation of something the Slovak does carry but the English reference words differently (*private
property*, *right now*, *the guard regrets it*). F6 cannot see the Slovak, so it only judges added PPs.
Function words are never an addition at all (articles, do-support, contractions, optional *that*, the
pronoun subject Slovak drops, degree adverbs).

**Pre-flight**: `--selftest` = 17 synthetic rows, 17/17, covering every intended fire and every intended
abstention (function-word addition, substitution only, word-order move, article-only deletion, `-ujú` vs
`-uje`, `you` exempt from the number test, `bude`).

## 2 Result — each guard ALONE and COMBINED, both scorings

TIP = accept (the Phase 1h row-7 baseline): FA 30/260, coverage 160/203.

| config | FA after | FA removed (by type) | correct answers lost (of 203) |
|---|---|---|---|
| F5t | 24/260 = 9.2 % [6.0–13.4] | **−6** (M 6) | **2** — `C:14779:4064141330`, `C:9584:294078585` |
| F6 | 29/260 = 11.2 % [7.6–15.6] | **−1** (M 1) | **1** — `C:7910:1495359972` |
| F4v3 | 28/260 = 10.8 % [7.3–15.2] | **−2** (S 2) | **0** |
| F5t+F6+F4v3 | **21/260 = 8.1 % [5.1–12.1]** | **−9** (M 7, S 2) | **3** (the union of the three lists above) |

TIP = reject (Task A switch): FA 8/260, coverage 149/203.

| config | FA after | FA removed | correct answers lost (of 203) |
|---|---|---|---|
| F5t | 8/260 [1.3–6.0] | **−0** | **1** |
| F6 | 8/260 [1.3–6.0] | **−0** | **1** |
| F4v3 | 6/260 = 2.3 % [0.9–5.0] | **−2** (S 2) | **0** |
| F5t+F6+F4v3 | **6/260 = 2.3 % [0.9–5.0]** | **−2** (S 2) | **2** |

Coverage: 160 → 157/203 = 77.3 % [70.9–82.9] combined (TIP = accept); 149 → 147/203 (TIP = reject).

**The decisive finding for the integrating agent: F5t and F6 are almost entirely an ALTERNATIVE to the
Task A switch, not additive to it.** All 7 of their DEV wins are items the model labelled `TIP`, which the
Task A switch already rejects; on top of Task A they buy nothing on DEV and still cost 2 correct answers.
**F4v3 is additive**: both its wins are `SAME` items that survive the TIP switch, and it costs 0.
Recommended stacking: Task A switch **+ F4v3**; take F5t (and F6) only if the TIP switch is *not* taken,
where F5t is the best offline lever measured here (−6 FA for −2 correct).

Removed items (combined, TIP = accept):

| guard | id | type | model | why it fired |
|---|---|---|---|---|
| F5t | W:1452:3813004317 | M | TIP | content word(s) *finger* |
| F5t | W:2121:4138132892 | M | TIP | adjunct adverb *just* |
| F5t | W:3494:2755518720 | M | TIP | content word(s) *empty pockets* |
| F5t | W:3937:1213271894 | M | TIP | adjunct adverb *again* |
| F5t | W:4449:722373448 | M | TIP | content word(s) *altogether* |
| F5t | W:9495:890576878 | M | TIP | adjunct adverb *twice* |
| F6 | W:11980:2419738346 | M | TIP | added content word(s) *pot* ("…will boil **in the pot**") |
| F4v3 | W:10366:1314252953 | S | SAME | number: *bude* is 3sg, answer "they" |
| F4v3 | W:5971:3700802525 | S | SAME | number: *skontroluje* is 3sg, answer "they" |

Cost, itemised (each reason is the guard's own trace):

| guard | id | learner answer | fired because |
|---|---|---|---|
| F5t | C:14779:4064141330 | "She's going to wipe dust from the top of the door." | ref *top **edge** of the door* — content word *edge* dropped (a genuine, if harmless, drop) |
| F5t | C:9584:294078585 | "She's been sprinting at full speed since she took off." | ref *since **the moment** she took off* — light noun *moment* dropped |
| F6 | C:7910:1495359972 | "…the clamped stack didn't move in the slightest." | idiom *in the slightest* read as an added PP |

**Type T (grammar) does not get worse**: no type-T wrong answer is rejected by any of the three guards and
no guard fires on a grammar substitution (`replace` hunks are excluded by construction), so the one type-T
false acceptance stays in the residue and the T rate is unchanged.

## 3 What C3 found about `si`

The carried-over note ("the `si` clitic blocks every person signal") is **true in effect on DEV and wrong as
a mechanism**. Measured: **41 DEV items have `si` in the Slovak; in all 41 `sk_features()` returns
`person = None`** (`results.json → c3_si_diagnosis`). But the block is narrower than the note says:
`SK_AUX` already skips `si`, so `si` never contributes a person itself, and `ambiguous_si` only suppresses
the **default 3rd person that a bare l-participle would assert**. An explicit nominative pronoun, a
`som/sme/ste` auxiliary or a present-tense `-š/-me/-te/-m` ending would still set person in a `si` sentence
— it simply never happens in these 41, because they are all past/conditional sentences whose only person
signal would have been the participle default. **Number and gender survive `si`** (e.g. `W:9907:1778280655`:
`{person: None, number: sg, gender: None}`), which is why the gender/number arms of F4v2 still work there.
F4v3's extra signal is unaffected: it asserts number only, and `si` sentences are past-tense, where neither
the byť-future paradigm nor `-uje/-ujú` occurs.

On the item named in the brief, `W:20298:1595880954`: it is not in `dev/false_acceptances.json`, and I did
not look it up. I built the synthetic row instead (*"Potrebuje nový telefón." / "They need a new phone."* —
selftest case 11: F4v3 fires, number sg vs pl; the controls *potrebujú → they*, *potrebuje → he*,
*potrebuje → I* correctly abstain). Note that sid 20298 **is** one of the 14 DEV sids where the new signal
speaks, so the fix reaches that Slovak shape. Number is fixed the way the brief asks, and **person is
deliberately not asserted** from the new signals: Slovak recasts subjects freely (*"Bude sa ti to páčiť"* =
"You will like it"), so a person claim off a 3sg verb would reject correct answers, while the number of the
subject survives the recast. `you` stays exempt from the number test (F4v2's rule, kept).

## 4 Residue — the 21 DEV false acceptances that survive all three guards

For the prompt-variant agent. "TIPrej" = still accepted when L3 `TIP` counts as a rejection (6 of 21; those
six are the only ones a prompt variant must fix if the Task A switch is taken).

| id | type | layer | model | TIPrej | one-line reason it survives |
|---|---|---|---|---|---|
| W:10013:1594646351 | W | L3 | SAME | yes | substitution only: he→she, holding→pressing, ice pack against lump→compress on bruise |
| W:1452:3230512291 | W | L3 | TIP | no | substitution only: spines→thorns, finger→hand |
| W:14697:2532470414 | S | L3 | TIP | no | substitution only: is little→are few drops of, stones→rocks |
| W:14697:567072060 | M | L3 | SAME | yes | deletion *after impact* **and** substitutions within 3 tokens → `_unpair` treats it as one rewrite |
| W:15437:338816939 | W | L3 | TIP | no | substitution only: path→road |
| W:20702:2829002765 | W | L3 | TIP | no | substitution only: jug→bucket |
| W:2121:832651865 | T | L3 | TIP | no | substitution only: flatmate→his roommate, spent→spends (the one type-T FA) |
| W:23360:711319744 | S | L3 | TIP | no | substitution only: his→their (possessive, not a subject → F4v3 abstains) |
| W:23878:71189755 | W | L3 | TIP | no | substitution only: pitch in this huge stadium→court |
| W:2389:1402963517 | S | L3 | TIP | no | inserted *officer* is a bare noun, not a PP → F6 abstains by design |
| W:28006:2654956435 | W | L3 | TIP | no | inserted function word only (*will*) |
| W:5959:2145732155 | S | L3 | SAME | yes | substitution only: he turns→they turn, she→he, drop→lower (an answer pronoun fits the Slovak → F4v3 abstains) |
| W:7037:3489763949 | W | L3 | TIP | no | substitution only: stag→deer, leaves→branches |
| W:7037:3615298556 | S | L3 | TIP | no | substitution only: stag→elk |
| W:7444:2683969038 | M | L3 | SAME | yes | *already* dropped, but *coats→layers* sits within 3 tokens → treated as one rewrite |
| W:7533:3503567680 | W | L3 | TIP | no | inserted function word only (*in*) |
| W:7998:52962874 | M | L3 | SAME | yes | *now* dropped, but *veranda→porch* sits within 3 tokens → treated as one rewrite |
| W:8039:516493581 | W | L3 | TIP | no | substitution only: penalty→foul |
| W:8491:3020598369 | S | L3 | TIP | no | substitution only: skin→peel, pomegranate opens→pomegranates open |
| W:9007:2829648222 | W | L3 | TIP | no | inserted function word only (*already*) |
| W:9907:1778280655 | S | L1 | — | yes | byte-identical to the reference: the known writer artefact (1h §5 D5) |

Residue by type: **W 10, S 7, M 3, T 1**. The shape of the remaining problem is clear and it is **not**
offline-tractable: 14 of 21 are pure lexical substitutions (*stag→elk*, *path→road*, *penalty→foul*) whose
wrongness is a Slovak-vocabulary judgement, i.e. exactly the model layer's job. Three more are the
`_unpair` trade-off (a dropped adjunct next to a substitution — recoverable offline only by accepting the
false rejections that a narrower window costs) and one is a data artefact.

## 5 Integration

```python
import checker_1i as C
import guards_c
guards_c.apply(C, guards=("F6", "F5t", "F4v3"))   # order of evaluation is fixed: F5t, F6, F4v3
guards_c.apply(C, guards=("F4v3",))               # recommended with the Task A switch
guards_c.apply(C, guards=())                      # restore the original C.decide
```
`apply(checker_module, guards=("F6","F5t","F4v3")) -> decide` wraps `checker_module.decide` (idempotent, no
import-time side effects, the checker module is bound lazily). The wrapper lets the frozen stack decide and
re-examines only answers it **accepted** — identical accept/reject outcomes to inserting the guards in
front of L3 (a guard can only turn an acceptance into a rejection), while `layer` reports `'F5t'`/`'F6'`/
`'F4v3'` and `trace[guard]` carries the full trace. A guard can also be switched off per item through the
`flags` dict (`flags['F6'] = 0`). Each guard is also callable alone: `f5t_deletion(it)`, `f6_addition(it)`,
`f4v3_subject_mismatch(it)` → `(hit, trace)`, plus `guards_report(it)` and `run_guards(it, guards)`.

## 6 Overfitting disclosure

**Structural** (annotation- or diff-driven, no vocabulary): the whole diff machinery and the
`delete`/`insert`/`replace` split; the `_unpair` window; `_drop_moves` including the `IRREG`-based stem
test; the "abstain as soon as one accepted rendering yields no fire" rule (F5's own semantics); the
sanctioned-vocabulary set (all `refs_of()` renderings, `alt`, `d`, `s`, synonym groups); the re-use of F5's
`span_information()` and `PREP_HEADS`; F4v3's superset rule; the single-clause condition.

**Lexical** (closed-class tables, all of them paradigms rather than content words): `NEG` (9 negatives),
`SK_BYT_FUT` (the 6 future forms of byť + `ne-`), `SK_PRESENT_NUM` (3 verb endings), `SK_CLAUSE` (Slovak
conjunctions/subordinators), `_SUF` (9 English suffixes).

**No content word from the 30 DEV failures entered any table** — that was the design rule. What *was*
DEV-driven is the choice of the safety rules: the PP restriction in F6, the `_unpair` window, the stem and
negation tests and the single-clause condition were all added after seeing the cost they remove (18 correct
answers lost → 3), never the wins they create. Those rules are generic and none is keyed to a sid, so the
leakage caveat of `split/SPLIT.md` (138 of 140 sids have items on both sides) does not apply to them: no
annotation, reference or per-sentence list was touched. Expect the holdout FA removal to move; expect the
cost (3/203 here) to be the number with the larger relative uncertainty.

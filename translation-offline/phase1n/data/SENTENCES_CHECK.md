# Phase 1N — check of `data/sentences.json`

Label: **sentence-recheck-2** · 19 Sep 2026 · script: `check_sentences.py`
(run `python3 check_sentences.py`, exit 0 iff `ok`).

This is the second, independent check of the file. It was run against the
version of `data/sentences.json` as of 11:04 (i.e. after the recheck-1 repairs
to 160020 / 160022 / 160087 and the `passivizable = false` corrections on
160013 / 160026 / 160038). Those earlier findings are confirmed as fixed and
are **not** repeated below.

## 1. Mechanical checks — all pass

| check | required | measured | verdict |
|---|---|---|---|
| rows | exactly 100 | 100 | pass |
| sids | 160001..160100, unique | complete, 0 duplicates | pass |
| fields | `sid, slovak, level, topic, tf_gold, tags{nom_agent, agent, passivizable, reported_speech, perfective_future, impersonal_or_passive}` | 0 missing, no empty `slovak` | pass |
| level counts | A1 13 / A2 21 / B1 36 / B2 30 | A1 13 / A2 21 / B1 36 / B2 30 | pass |
| `passivizable: true` | >= 80 | 83 | pass |
| `tf_gold` domain | {past, present, future} | no other value | pass |
| frame balance | each >= 20 | past 40 / present 35 / future 25 | pass |
| identical to `existing_350.json` | none | 0 | pass |
| max token-Jaccard new vs existing | < 0.80 | **0.353** (160053 vs existing #45) | pass |
| max token-Jaccard new vs new | < 0.60 | **0.250** (160005 vs 160083) | pass |

Secondary tag counts (informational, no target): `reported_speech` 15,
`perfective_future` 11, `impersonal_or_passive` 6, `nom_agent` 89.

## 2. Manual read of all 100 sentences

Read against four questions: (a) correct, natural Slovak; (b) the arm-B
convention (explicit subject pronoun wherever Slovak would drop it; noun
subjects untouched; nothing inserted into genuinely impersonal/passive clauses
or into imperatives; one pronoun per subject, so a following **same-subject**
clause keeps it implicit); (c) `tf_gold` vs. the real time frame;
(d) `passivizable: true` only where an English *by*-passive is grammatical.

**Blockers: 0. Problems found: 2 (both minor).**

### P1 · sid 160084 · `passivizable: true` but the English has no by-passive

Now: `Oni hovoria, že on ten čln lakuje už druhý týždeň.` — tags `passivizable: true`.
The duration adverbial `už druhý týždeň` with a present-tense verb forces an
English **present perfect continuous** ("…that he has been varnishing the boat
for the second week"). `*the boat has been being varnished by him` is
ungrammatical, exactly like the three rows that were already corrected
(160013 present perfect continuous, 160026 past perfect continuous,
160053 future perfect continuous).

Required fix — in row 160084 set `tags.passivizable = false`.
After the fix the true count is **82**, still `>= 80`, so the set stays valid.
(`tf_gold: present` and all other tags on this row are correct.)

### P2 · sid 160027 · arm-B: dropped subject in a switch-reference clause

Now: `Ak ty ohneš ten drôt príliš rýchlo, vždy praskne.`
The second clause has a pro-dropped 3sg subject (the wire) which is **not** the
subject of the first clause (`ty`), so the "same subject stays implicit"
exemption does not cover it; the English gold needs an overt *it*. An inanimate
pronoun (`ono` / `ten`) standing alone would be unnatural Slovak, so the repair
repeats the noun.

Required fix — replace the `slovak` value with:
`Ak ty ohneš ten drôt príliš rýchlo, ten drôt vždy praskne.`
Tags unchanged (`tf_gold: present`, `passivizable: true` — "if the wire is bent
too fast by you" is grammatical).

### Checked and found correct (no action)

* **Time frames.** All 100 `tf_gold` values match the sentence. The two
  systematic cases are consistent: a completed event in Slovak past tense is
  `past` even where English would use the present perfect (160054, 160093,
  160071, 160075), while an event still running at speech time is `present`
  (160013, 160084). Going-to futures with a present-form `chystá sa` are
  `future` (160003, 160089); perfective presents in conditional apodoses are
  `future` with `perfective_future: true` (160057, 160072, 160096, 160069,
  160094). Counterfactuals: past ones `past` (160011, 160062, 160022, 160080),
  the mixed conditional 160018 `present` because its main clause is `dnes by
  … hrala`.
* **Arm-B.** Apart from P2, every clause with a pronominal subject carries the
  pronoun. Correctly left implicit: same-subject continuations (160046, 160057,
  160067, 160072, 160094, 160096, 160100, 160011, 160018, 160026, 160062,
  160068), imperatives (160035 `Pozri!`, 160076 `Neboj sa`), genuinely
  impersonal or passive rows (160004, 160032, 160039, 160051, 160058, 160098)
  and the indefinite 3pl relative clause `ktorého nám odporučili` (160059).
* **Passivizable.** The remaining 17 `false` rows are right: already passive or
  impersonal (160004, 160032, 160039, 160051, 160058, 160098), existential /
  copular (160008, 160025, 160055, 160070, 160097), causative `dať + inf.`
  (160029), `odmietol podpísať` (160043), the wh-question (160038) and the three
  perfect-continuous rows (160013, 160026, 160053). The `true` rows all take a
  well-formed *by*-passive, including the modal ones (160023, 160036, 160066,
  160074) and the comparatives (160041, 160087).
* **Slovak.** No agreement, case, aspect or clitic error found. Clitic
  placement in `Portrét si ona dala zarámovať…` (160029) and `Keby si ona vlani
  nebola zlomila…` (160018) follows the same pattern as the existing 350 set
  (`Slajdy si ona dala skontrolovať…`), and `Keď sme my dorazili…` (160020)
  keeps `sme` in second position — all acceptable.

### Systematic stylistic note (not counted as a problem)

Eight rows front an adverbial and then place the subject pronoun before the
verb: 160007, 160030, 160047, 160053, 160083, 160086, 160100 (`Do soboty ona
zdigitalizuje…`, `Len zriedka on púšťa…`). This is grammatical Slovak with a
mildly contrastive reading; the neutral order would put the pronoun first
(`Ona do soboty zdigitalizuje…`). It is consistent across the set and is a
direct consequence of the arm-B pronoun insertion, so it is reported once here
rather than as eight row problems. Likewise, the overt coreferent `on/ona` in
the 15 reported-speech complements (`Lodník nám povedal, že on…`) is
pragmatically marked in Slovak (it invites a disjoint-reference reading) but is
required by arm-B and is applied consistently; the `agent` tag always names the
real performer, so no row is ambiguous for scoring.

## 3. Verdict

`ok: true`, `n_problems: 2`, `n_blockers: 0` — the set is usable as it stands;
applying P1 and P2 is recommended before the run and neither breaks any count.

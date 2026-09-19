# Phase 1N — sentence-set check (`data/sentences.json`)

Label: **sentence-recheck-1** · date 19.9.2026 · script `phase1n/check_sentences.py`
(`python3 check_sentences.py`; exit 0 iff `ok`).

This is a **re-check of the revised file** (sentences.json rewritten after the first
`sentence-check` pass). The three blockers of that pass were applied and verified here:
160022 got its 1pl auxiliary, 160043 is now `passivizable: false`, 160073 uses `znášate`.
Seven of the eight minor items were applied too (160086 `skatalogizujú`, 160011 / 160062
past-conditional apodosis, 160046 transitive first clause, 160038 verb added, 160002 verb
order, 160093 `agent: "Knihovník"`); 160047 was knowingly kept.

`ok` = mechanical checks pass AND no blocker open. Mechanical passes; **one new blocker**
was found in the manual read, so **ok = false**, **n_problems = 6** (1 blocker + 5 minor).

## 1. Mechanical checks — 10/10 PASS

| check | required | measured | verdict |
|---|---|---|---|
| rows | exactly 100 | 100 | PASS |
| sids | 160001..160100, unique | complete, no dup, no extra | PASS |
| fields | sid, slovak, level, topic, tf_gold + tags{nom_agent, agent, passivizable, reported_speech, perfective_future, impersonal_or_passive} | present on all 100 rows | PASS |
| level counts | A1 13 / A2 21 / B1 36 / B2 30 | A1 13 / A2 21 / B1 36 / B2 30 | PASS |
| passivizable true | >= 80 | 83 | PASS |
| tf_gold domain | {past, present, future} | no other value | PASS |
| tf_gold per frame | each >= 20 | past 40 / present 35 / future 25 | PASS |
| identical to existing_350 | 0 | 0 | PASS |
| max token-Jaccard new-vs-existing | < 0.80 | 0.3529 (160053 vs existing #45) | PASS |
| max token-Jaccard new-vs-new | < 0.60 | 0.3333 (160016 vs 160097) | PASS |

Secondary counts (not gated): nom_agent 86, reported_speech 15, perfective_future 11,
impersonal_or_passive 6.

Headroom: applying the two `passivizable` demotions below (160013, 160026) moves the count
83 -> 81, and adding 160038 -> 80. All still satisfy `>= 80`.

## 2. Manual read of all 100 sentences

Read against four questions: (a) correct, natural Slovak; (b) the arm-B convention as stated
in `tasks/ARM_B.md` (explicit subject pronoun wherever Slovak would drop it; noun subjects
untouched; nothing inserted into genuinely impersonal/passive sentences; one pronoun per
subject, so a following same-subject clause keeps it implicit — `…a zhasnem lampu` 160094,
`…tú anténu upevníme sami` 160096, `…vyloží ten materiál` 160057 are all correct);
(c) tf_gold vs. the real time frame; (d) `passivizable: true` only where an English by-passive
is grammatical.

**tf_gold: correct on all 100 rows.** The tricky classes are consistent: BE GOING TO with the
Slovak present `chystá sa` is `future` (160003, 160089); present perfect is split by event
status — ongoing `leští … už od rána` -> present (160013), completed `vymenil už všetky` ->
past (160054, 160093); third conditional and past wishes -> past (160011, 160022, 160062,
160080); the mixed conditional with `dnes` -> present (160018); zero conditional with the
perfective form `ohneš` -> present (160027); `musel vymeniť` = "must have changed" -> past
(160074); `mala vystužiť` = "should have reinforced" -> past (160036).

### Blocker (1) — must be fixed before the set is used

**P1 · sid 160020 · arm-B convention broken (dropped 1pl subject)**
Now: `Keď sme dorazili, Janka už rozložila celý stánok.`
The subordinate clause has a pro-dropped 1pl subject **that is not the main-clause subject**
(`Janka`), so the "one pronoun per subject" reading does not cover it; arm-B requires the
pronoun. This is the only row in the set with an unstated pronominal subject.
Required fix — replace the `slovak` value with:
`Keď sme my dorazili, Janka už rozložila celý stánok.`
(clitic `sme` stays in second position, the pronoun follows it). Tags unchanged.

### Minor problems (5) — recommended, none blocks the run

**P2 · sid 160013 · `passivizable: true` but the by-passive is ungrammatical.**
`Klampiar leští ten medený kotol už od skorého rána.` = "has been polishing"; the by-passive
"The cauldron has been being polished by the tinsmith" is not grammatical English. Note that
160053 (future perfect continuous) is already tagged `false` for exactly this reason, so the
set is internally inconsistent. Fix: set `"passivizable": false` in `tags` of 160013.

**P3 · sid 160026 · same class.** `Oni prekladali ten slovník celé mesiace…` = "had been
translating"; "had been being translated by them" is ungrammatical.
Fix: set `"passivizable": false` in `tags` of 160026.

**P4 · sid 160087 · possessive should be reflexive.**
`Nina brúsi tie hrany presnejšie ako ktorýkoľvek z jej spolužiakov.` `jej` is coreferent with
the subject, which Slovak marks with `svoj`; as written it reads as *someone else's* classmates.
Fix: `Nina brúsi tie hrany presnejšie ako ktorýkoľvek zo svojich spolužiakov.`

**P5 · sid 160022 · grammatical but stilted clitic+pronoun doubling.**
`Kiežby sme my boli tú zmluvu prečítali pozornejšie.` `sme my` is well-formed (clitic second,
emphatic pronoun third) but marked; it is the price of arm-B in the 1pl past conditional.
Fix (optional): move the row to 3sg — `Kiežby ona bola tú zmluvu prečítala pozornejšie.` with
`tags.agent` = `"ona"`. Otherwise keep and do not score it as a translation error.

**P6 · sid 160038 · by-passive of a wh-question is marginal.**
`Čo ty práve kreslíš na ten veľký papier?` — "What is being drawn by you…?" is possible but
stilted; it is the only interrogative in the set.
Fix: either set `"passivizable": false` (count then 80, still at the floor) or accept as-is.

### Recorded, not problems

* Arm-B word-order artifacts after a fronted adverbial — 160030, 160047, 160083 (`Len zriedka
  on púšťa…`): Slovak would prefer inversion, but the pronoun placement is the frozen arm-B
  behaviour. The judge must not score these as translation errors.
* Fronted object + clitic in the causative row 160029 (`Portrét si ona dala zarámovať…`)
  mirrors the existing_350 pattern (`Slajdy si ona dala skontrolovať…`) — intended.
* `ktorého nám odporučili` (160059) is an indefinite-3pl impersonal; arm-B explicitly does not
  insert a subject there.
* The 6 impersonal/passive rows (160004, 160032, 160039, 160051, 160058, 160098) correctly
  carry no forced subject.
* Plain future-continuous rows (160012, 160021, 160049, 160061, 160091, 160099) keep
  `passivizable: true`: their natural English passive is the simple `will be polished`, which
  is grammatical — unlike the perfect-continuous class P2/P3.

## 3. Verdict

Mechanical PASS (10/10). Manual: 6 flagged sids — **1 blocker (160020)**, 5 minor
(160013, 160026, 160087, 160022, 160038). **ok = false**, **n_problems = 6**.
After applying P1, re-run `check_sentences.py` (drop the blocker entry from
`MANUAL_PROBLEMS`); it must print `"mechanical_ok": true` and then `"ok": true`.

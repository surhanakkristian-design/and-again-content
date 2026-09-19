# Phase 1N — sentence-set check (`data/sentences.json`)

Label: **sentence-check** · date 19.9.2026 · script `phase1n/check_sentences.py`
(`python3 check_sentences.py`, exit 0 = all mechanical checks pass).

`ok` in the JSON verdict = *mechanical checks pass AND no blocker found in the manual read*.
The mechanical half passes; three blockers were found by hand, so **ok = false**.

## 1. Mechanical checks — ALL PASS

| check | required | measured | verdict |
|---|---|---|---|
| rows | exactly 100 | 100 | PASS |
| sids | 160001..160100, unique | complete, no dup, no extra | PASS |
| fields | sid, slovak, level, topic, tf_gold + tags{nom_agent, agent, passivizable, reported_speech, perfective_future, impersonal_or_passive} | all present on all 100 rows | PASS |
| level counts | A1 13 / A2 21 / B1 36 / B2 30 | A1 13 / A2 21 / B1 36 / B2 30 | PASS |
| passivizable true | >= 80 | 84 | PASS |
| tf_gold domain | {past, present, future} | no other value | PASS |
| tf_gold per frame | each >= 20 | past 40 / present 35 / future 25 | PASS |
| identical to existing_350 | 0 | 0 | PASS |
| max token-Jaccard new-vs-existing | < 0.80 | 0.3529 (160053 vs existing #45) | PASS |
| max token-Jaccard new-vs-new | < 0.60 | 0.3333 (160016 vs 160097) | PASS |

Secondary counts (not gated, recorded for the runner): nom_agent 86, reported_speech 15,
perfective_future 11, impersonal_or_passive 6.

Headroom note: fixing blocker P2 below moves `passivizable true` from 84 to 83, still >= 80.

## 2. Manual read of all 100 sentences

Read against four questions: (a) correct, natural Slovak; (b) arm-B convention
(`tasks/ARM_B.md`: explicit subject pronoun wherever Slovak would drop it, noun subjects
untouched, no pronoun forced into impersonal/passive sentences); (c) tf_gold matches the
sentence's real time frame; (d) `passivizable: true` only where an English by-passive is
grammatical.

Arm-B reading used: the pronoun is required once per subject, not once per finite verb — a
second, same-subject clause (`…, tú aukciu by vyhrala`, `…a zhasnem lampu`) keeps the pronoun
implicit, exactly as the frozen Phase 1k examples do. No sentence with a pronominal subject is
missing its pronoun, and none of the 6 impersonal/passive rows (160004, 160032, 160039,
160051, 160058, 160098) had a subject forced into it. tf_gold is correct on all 100 rows
(present-perfect topics are split consistently: ongoing event -> present 160013, completed
event -> past 160054; third conditional / past wish -> past; mixed conditional with `dnes` ->
present 160018).

### Blockers (3) — must be fixed before the set is used

**P1 · sid 160022 · ungrammatical Slovak (missing 1pl auxiliary)**
Now: `Kiežby my boli tú zmluvu prečítali pozornejšie.`
The 1pl past conditional needs the clitic `sme` (`kiež by sme boli … prečítali`); `Kiežby my
boli` has no person marking at all and is ungrammatical.
Required fix — replace the `slovak` value with:
`Kiežby sme my boli tú zmluvu prečítali pozornejšie.`
(If the doubled `sme my` is unwanted, the alternative that keeps arm-B intact is to move the
row to 3sg: `Kiežby ona bola tú zmluvu prečítala pozornejšie.` — then `tags.agent` becomes
`"ona"`.)

**P2 · sid 160043 · `passivizable: true` but no English by-passive exists**
`On odmietol podpísať ten protokol bez svojho právnika.` = "He refused to sign the protocol
without his lawyer." `refuse` + to-infinitive does not passivise on the embedded object
(*"The protocol was refused to be signed by him"* is ungrammatical).
Required fix — set `"passivizable": false` in `tags` of 160043 (no text change).

**P3 · sid 160073 · wrong directional verb**
`Vy každý štvrtok vynášate tie ťažké debny do pivnice.` — `vynášať` means to carry *out / up*;
carrying crates *down into a cellar* cannot be `vynášať do pivnice` (cf. the correct 160085
`vyniesol tie staré časopisy na povalu`).
Required fix — replace the `slovak` value with:
`Vy každý štvrtok znášate tie ťažké debny do pivnice.`

### Minor problems (8) — recommended, none blocks the run

**P4 · sid 160086 · non-standard lexis.** `zaindexujú` is not standard Slovak.
Fix: `Do konca mesiaca oni skatalogizujú celý farský archív.` (or `zindexujú`).

**P5 · sid 160011 and P6 · sid 160062 · apodosis tense of the third conditional.**
`Keby on bol pribalil …, tú prasknutú pneumatiku by vymenil hneď.` /
`Keby ona bola prišla …, tú aukciu by vyhrala.` Prescriptive Slovak wants the past conditional
in the main clause too. Fix: `… by ju bol vymenil hneď.` / `… by bola vyhrala.` (Both rows use
the same pattern, so leaving them is at least internally consistent.)

**P7 · sid 160046 · `passivizable: true` covers only half the sentence.**
`Zvyčajne ona píše rukou, ale dnes diktuje poznámky do telefónu.` The first clause is
intransitive; only `diktuje poznámky` passivises. Fix: either set `"passivizable": false`, or
replace the first clause with a transitive one, e.g.
`Zvyčajne ona píše tie poznámky rukou, ale dnes ich diktuje do telefónu.`

**P8 · sid 160038 · verbless second half.**
`Čo ty práve kreslíš? — Plán tej starej pivnice.` The answer fragment carries no verb, so it
has no time frame of its own and the by-passive ("What is being drawn by you?") is marginal.
Fix: drop the fragment — `Čo ty práve kreslíš na ten veľký papier?`

**P9 · sid 160002 · heavy preverbal object, unnatural rhythm.**
`… že on tri kapitoly tej príručky prečítal za jediný večer.` A quantified, new-information
object before the verb is marked in Slovak.
Fix: `Spolužiak mi napísal, že on prečítal tri kapitoly tej príručky za jediný večer.`

**P10 · sid 160093 · tagging inconsistency, not a language problem.**
`tags.agent` is `"on"` while every sibling reported-speech row with a noun matrix subject
(160002, 160009, 160024, 160037, 160050, 160063) names the noun.
Fix: set `"agent": "Knihovník"` for consistency.

**P11 · sid 160047 · stilted but allowed.**
`Len zriedka on púšťa tú starú pásku svojim hosťom.` After a fronted `Len zriedka` Slovak
prefers inversion (`púšťa on`); the current order is a known arm-B artifact, also present in
160030/160031/160083. No fix required — recorded so the judge does not score it as a
translation error.

## 3. Verdict

Mechanical: PASS (10/10). Manual: 11 flagged sids — 3 blockers (160022, 160043, 160073),
8 minor. **ok = false** until P1-P3 are applied; re-run `check_sentences.py` afterwards
(it must still print `"mechanical_ok": true`, with `passivizable_true` at 83).

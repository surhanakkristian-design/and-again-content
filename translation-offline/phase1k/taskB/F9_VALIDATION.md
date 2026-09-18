# F9 / F8 validation - Phase 1k task B (agent G, 18 Sept 2026)

**Post-fix F9 error rate 0/140 = 0.00 %, exact Clopper-Pearson 95 % [0.00, 2.60] - F9 IS FREEZABLE.** Pre-fix the same run gave 7/140 = 5.00 % -> at that point F9 was NOT FREEZABLE; both tables are below and every pre-fix error is itemised.

Method, in this order: (i) `f9.py` written on the DEV sentences; (ii) all 140 arm-B Slovak sentences dumped to `sentences_140.jsonl` (sid + side + Slovak only; the holdout sentence read is logged in `phase1k/access_log.jsonl`); (iii) the hand gold `gold_tf.jsonl` written by agent G from the Slovak alone **before any script output existed for those sentences**; (iv) `validate_f9.py` compared them. Gold = the time frame(s) a careful bilingual teacher would allow for the MAIN clause (first non-subordinate finite clause), which is what `sk_frame` reports as the sentence verdict. AGREE = script set equals gold; CONSERVATIVE = script abstains or asserts a SUPERSET of gold (forbids less than the truth); ERROR = gold minus script is non-empty, i.e. the script forbids a frame the gold allows and would reject correct answers. No answers and no labels were used anywhere in the validation.

## F9 `sk_frame` - PRE-FIX

| side | n | AGREE | CONSERVATIVE | ERROR | err rate | CP95 |
|---|---|---|---|---|---|---|
| DEV | 70 | 60 | 9 | 1 | 1.43 % | [0.04, 7.70] |
| HOLDOUT | 70 | 61 | 3 | 6 | 8.57 % | [3.21, 17.73] |
| ALL 140 | 140 | 121 | 12 | 7 | 5.00 % | [2.03, 10.03] |

### every pre-fix error

- **224** (dev) `Slajdy si ona dala skontrolovať od staršieho brata deň predtým.`
  - gold `['past']`, script `['future', 'present']`; script reason: perfective present "predtým", no future anchor
  - cause: l-participle "dala" was rejected by a stem-length>=3 rule, and "predtym" (adverb in -ym) was read as a 1sg verb in -m
- **2955** (holdout) `Strážnik ľutuje - kiežby bol otočil kameru k obzoru o minútu skôr.`
  - gold `['present']`, script `['past']`; script reason: l-participle "bol"
  - cause: the ASCII hyphen was not a clause break and "kiezby" was recognised only clause-initially, so the wish clause's "bol" became the main past
- **7238** (holdout) `Ak ty stúpaš presne tam, kam stúpa Mira, nohy ti zostanú úplne suché.`
  - gold `['future', 'present']`, script `['present']`; script reason: imperfective present "stúpa"
  - cause: "kam" was missing from the subordinate-marker list, so "kam stupa Mira" was taken as the main clause
- **20435** (holdout) `Ten veľký tanier je biely a úplne čistý.`
  - gold `['present']`, script `['past']`; script reason: l-participle "biely"
  - cause: adjective "biely" matched the (wrong) "-ly" l-participle ending
- **23669** (holdout) `Galaxia sa pomaly pohybuje nad ich hlavami.`
  - gold `['present']`, script `['past']`; script reason: l-participle "pomaly"
  - cause: adverb "pomaly" matched the (wrong) "-ly" l-participle ending
- **24741** (holdout) `Veslársky tím je rýchly a veľmi silný.`
  - gold `['present']`, script `['past']`; script reason: l-participle "rýchly"
  - cause: adjective "rychly" matched the (wrong) "-ly" l-participle ending
- **28006** (holdout) `Každú loď v zálive ty spozoruješ skôr než ktokoľvek iný. Klobúk dole.`
  - gold `['future', 'present']`, script `['present']`; script reason: imperfective present "spozoruješ"
  - cause: prefixed -uje verb "spozorujes" was classified imperfective, so PRESENT was asserted instead of the open set {future, present} - the perfective-present trap

## F9 `sk_frame` - POST-FIX (the frozen code)

| side | n | AGREE | CONSERVATIVE | ERROR | err rate | CP95 |
|---|---|---|---|---|---|---|
| DEV | 70 | 63 | 7 | 0 | 0.00 % | [0.00, 5.13] |
| HOLDOUT | 70 | 67 | 3 | 0 | 0.00 % | [0.00, 5.13] |
| ALL 140 | 140 | 130 | 10 | 0 | 0.00 % | [0.00, 2.60] |

0 errors. The 10 CONSERVATIVE rows are abstentions or supersets ({future, present} where the gold is {future}); they can only accept, never reject.

## F8 `sk_agent` on all 140

| side | n | AGREE | CONSERVATIVE | ERROR | err rate | CP95 |
|---|---|---|---|---|---|---|
| DEV | 70 | 60 | 10 | 0 | 0.00 % | [0.00, 5.13] |
| HOLDOUT | 70 | 62 | 8 | 0 | 0.00 % | [0.00, 5.13] |
| ALL 140 | 140 | 122 | 18 | 0 | 0.00 % | [0.00, 2.60] |

Pre-fix F8 had 1 error: sid 9607 "Hovori sa, ze ona celu zimu trenovala vo vyske." - the nominative pronoun of the subordinate clause made the sentence look active although the main clause is the impersonal "Hovori sa", so a correct "It is said that she trained..." would have been rejected. Fixed by deciding the reflexive-impersonal question on the MAIN clause only. Gold voice classes over the 140: {"impersonal": 5, "active": 132, "passive": 3}. The 18 CONSERVATIVE rows are sentences where `sk_agent` returns False/None (copula, existential "je/su", "bol + adjective in -ny" read as a participial passive); F8 then accepts and cannot fire.

## Unit tests

`python3 -B f9.py --selftest`: 62 synthetic cases, 0 failures. `python3 -B f8.py --selftest`: 22 synthetic cases, 0 failures. None of the 84 cases is taken from the 140 sentences. They cover the perfective-present trap ("Do piatku ona dokonci cviky" + finishes / will finish / finished), "Po dopade je ... " + "there was" (reject) vs "there is" (accept), "On trenoval hodiny" + trained / was training / had been training (accept) vs "He trains" (reject), ak/ked clauses, reported speech, present perfect on both sides, "Hovori sa, ze ..." + English passive (accept), "Ona opravila bicykel" + "The bike was repaired (by her)" (reject) vs "She repaired the bike" (accept).

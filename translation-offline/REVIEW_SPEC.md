# Offline translation check – review pass (pilot, Phase 1)

You are the **second, independent reviewer**. Another writer produced the files; assume they
contain errors. Read `GENERATION_SPEC.md` first – every rule there applies – then review each
file of your list in `pilot/generated/`.

## What to check

Expand every `{a|b}` slot line in your head: **every single combination** counts.

For every acceptable translation (each expansion):
1. Grammatical, natural English a careful native teacher marks fully correct?
2. Same meaning as the Slovak sentence AND the Czech sentence (tense meaning, who does what,
   no detail added or lost beyond what the native sentences allow)?
3. Uses the practised grammar (`topic`)? A correct sentence that avoids it belongs in
   `mistakes` as `correct_with_tip`, not here.
4. Not a pure case / punctuation / contraction / digit variant of another line.

For every mistake (each expansion):
5. Is it really a mistake of the stated kind, and is it something a Slovak/Czech learner at
   this level would plausibly type?
6. Verdict right? `wrong` = ungrammatical, meaning changed, part missing, or practised grammar
   used incorrectly. `correct_with_tip` = grammatical AND same meaning but avoids the practised
   grammar or is clearly less natural. A mistake that is in fact fully correct must be moved to
   `acceptable` (or removed).
7. Feedback: only what is wrong (no praise); tense/structure names in English; gender-neutral
   (no "použil si / použila si / použil jsi"); grammar terms in English too ("past participle",
   not "příčestí minulé" / "minulé príčastie"); does not repeat the whole reference; ≤ 150
   characters; A1/A2 very simple; B1/B2 says briefly why; correct Slovak, correct Czech,
   plain English; `feedback_en` present exactly for B1/B2; the feedback is TRUE for every
   expansion of the text and matches the verdict.

Pronouns: Slovak and Czech often drop the subject. When neither native sentence shows who it
is (present tense "Dokáže ju nájsť" can be he or she; past tense "kúpila" is she), every
pronoun the native sentences allow must be accepted – and a pronoun they exclude must not be.

Also: add an acceptable translation only when a common, clearly correct rendering of the
native sentences is obviously missing (a synonym or word order most learners would type).
Keep 3–6 mistakes per exercise.

## How to fix

Edit the file in place (keep the same JSON shape and slot syntax; never change
`exercise_id`, `type_id`, `topic`, `level`, `reference`, `sk`, `cz`). Every change is one entry
in your log file `pilot/review/<your list name>.json`, a JSON list:

```json
{"exercise_id": 20435, "area": "acceptable" | "mistake" | "feedback",
 "action": "removed" | "fixed" | "added" | "verdict_changed" | "moved_to_acceptable",
 "before": "…", "after": "…" , "reason": "short English reason"}
```

One entry per changed line (a slot line fixed = one entry; a feedback text rewritten in one
language = one entry). If a file needs no change, write no entry for it. Write the log file
even when it is an empty list `[]`.

## Hard constraints

- Read ONLY this spec, `GENERATION_SPEC.md`, and the files on your list. Nothing under
  `scripts/translation-bench/`, `measurements/`, other pilot files or the app repository.
- No network, no model API.

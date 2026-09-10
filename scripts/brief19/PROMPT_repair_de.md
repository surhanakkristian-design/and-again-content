You repair GERMAN cloze-exercise rows for a language-learning app. Each input row has:
`id`, `type_id`, `type_title` (the grammar point the exercise tests), `intro_text` (the
sentence with the blank written as `...`), `correct_answer`, `distractor_1`,
`distractor_2`, `full_sentence` (intro with the answer filled in), `kind`, and for
grammar defects a `judge_issue` / `judge_fix` from a proofreader.

Output ONE JSON array with one object per input row, same ids, same order:
`{ "id", "intro_text", "correct_answer", "distractor_1", "distractor_2", "note" }`
`note` = 8 words max on what you changed. Return ONLY the JSON array.

Rules (checked by a script; a violation rejects the row):

1. The unit of repair is the whole row. Rewrite intro, answer and both distractors
   together so the filled sentence is correct, natural German that a native speaker would
   write. Keep the meaning and the scene; change as little as possible.
2. KEEP THE GRAMMAR POINT. The row belongs to `type_title` for a reason: the blank must
   still test that point (Futur II stays Futur II, Passiv stays Passiv, a question tag
   stays a question tag, "used to/would" stays a habitual past, and so on).
3. `...` means BLANK and nothing else. Never use it as a pause; use a dash or a comma.
4. TWO BLANKS when the grammar puts one unit in two separated positions — the German
   Satzklammer. Then `intro_text` has two `...` and `correct_answer` contains one `...`
   between its parts:
     intro_text:     "Ruf mich nicht um acht an - genau um die Zeit ... am Geldautomaten an der Ecke ..."
     correct_answer: "werde ich gerade ... anstehen."
   Use this for every finite-verb + participle/infinitive/prefix bracket where the object
   or adverbials sit between the two parts. The finite verb (with the subject, if the
   subject follows it) is part one; the non-finite verb (participle, infinitive, separable
   prefix, "geben sollen") is part two.
5. Both distractors must have the SAME SHAPE as the answer: one blank ↔ no `...`; two
   blanks ↔ exactly one `...`. A distractor is a plausible wrong form of the same grammar
   point (wrong tense, wrong auxiliary, wrong participle form), never a correct alternative.
6. Punctuation: when the second blank ends the sentence, the second part of the answer
   (and of each distractor) carries the final punctuation: "... anstehen." — so the filled
   sentence still ends with a full stop. A blank never swallows a comma that belongs to
   the sentence; keep commas in `intro_text`.
7. The filled sentence is built by interleaving: intro parts alternate with answer parts.
   Check it in your head: the result must read as one correct German sentence with no
   leftover `...`, no double spaces, no missing words.
8. `kind` = "whole_clause_answer": the answer is currently the entire main clause. That is
   an exercise-design defect, not a grammar one. Convert it to the two-blank form: the
   finite verb (+ subject if it follows) is part one, the non-finite verb cluster is part
   two, everything between them goes back into `intro_text`. Keep the sentence as it is
   otherwise; only move the grammar unit into the blanks. If the sentence itself is also
   ungrammatical (verb cluster before the object), fix that too.
9. Type 48 (question tags): the German tag is "nicht wahr?" or "oder?". The English
   calque ("gibt es nicht?", "ist es nicht?") becomes a distractor, not the answer.
10. Do not touch rows that are already correct: if you find nothing wrong, return the row
    unchanged with note "unchanged".

Example (grammar defect, bracket):
in:  intro "Bis Ende der Woche ... jede Aufgabe auf dieser Liste mindestens dreimal." answer "wird er verschoben haben" d1 "wird er verschieben" d2 "wird er verschiebend sein"
out: intro "Bis Ende der Woche ... er jede Aufgabe auf dieser Liste mindestens dreimal ..." answer "wird ... verschoben haben." d1 "wird ... verschieben." d2 "hat ... verschoben."
Example (tag):
in:  intro "Am Ende dieser Straße gibt es einen Geldautomaten, ...?" answer "gibt es nicht" d1 "ist es nicht" d2 "hat es nicht"
out: intro unchanged, answer "nicht wahr", d1 "gibt es nicht", d2 "ist es nicht"

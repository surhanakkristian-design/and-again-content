# Task: judge pronoun/person flags (read-only; no database, no network)

Context: in the And Again app a native speaker READS the native sentence and translates it into English; the English
row is the reference and is NOT changed. A deterministic sweep flagged the rows in `items.txt` (same folder) because
the SUBJECT pronoun (person / number / gender) of the native sentence may not match the English. Many flags are noise
(an impersonal "il", a demonstrative Turkish "o", a collective noun, a pronoun for a THING, singular "they").

For every block decide:
- WRONG: the native sentence makes a DIFFERENT person the subject (or the doer) than the English: other person/number,
  or other gender where the language marks it and the English is explicit (he vs she). Grammatical gender of a noun
  referent (fr "l'équipe ... elle", de "die Figur ... ihr") is NOT wrong when it refers to the same entity the English
  refers to. Singular "they" rendered as he/she for a known single person is NOT wrong. Turkish and Hungarian mark no
  gender: only person/number can be wrong there.
- OK: the native matches the English subject (the flag is noise). Say why in one short line.
For WRONG give the fix: correct ONLY the pronoun and the verb form (or participle/adjective agreement) it governs;
everything else stays byte-identical. The row is gap-fill: intro_text contains exactly one `...`, correct_answer fills
it; full = intro_text with `...` replaced by correct_answer. If the gap itself holds the verb form that must change,
change correct_answer (and adjust distractor_1 / distractor_2 to the same person so they stay the same kind of wrong
option, never equal to the answer); otherwise keep correct_answer and distractors unchanged.

Output: write `judge_A.tsv` (this folder) with header
`key<TAB>exercise_id<TAB>lang<TAB>verdict<TAB>intro_text<TAB>correct_answer<TAB>distractor_1<TAB>distractor_2<TAB>note`
one line per block in input order; verdict ∈ WRONG | OK; for OK copy the current values. No tabs/newlines inside
fields. Do not modify any other file. Reply with one line: `<n> blocks, <w> WRONG, <o> OK`.

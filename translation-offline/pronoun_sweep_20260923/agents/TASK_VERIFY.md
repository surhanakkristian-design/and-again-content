# Task: independent verification of pronoun/person flags (read-only; no database, no network)

Context: in the And Again app a native speaker READS the native sentence and translates it into English; the English
row is the reference and is NOT changed. A deterministic sweep flagged the rows in `items.txt` (same folder) because
the SUBJECT pronoun of the native sentence may not match the English. A first reviewer proposed verdicts and fixes in
`judge_A.tsv` (same folder).

Step 1 (do this FIRST and from `items.txt` alone, before opening judge_A.tsv): for every block decide your own verdict
WRONG / OK. WRONG = the native sentence makes a DIFFERENT person the subject (or doer) than the English: other
person/number, or other gender where the language marks it and the English is explicit. NOT wrong: grammatical gender
of a noun referent for the same entity (fr "l'équipe ... elle"), a pronoun for a thing, singular "they" rendered as
he/she for one known person, an impersonal/demonstrative word. Turkish and Hungarian mark no gender.
Step 2: open judge_A.tsv. For every block where YOU said WRONG and A proposed a fix, check the fix: only the pronoun
and the verb form / agreement it governs changed, everything else byte-identical; intro_text has exactly one `...`;
full sentence (intro with `...` replaced by correct_answer) is grammatical and says what the English says;
distractors are wrong options of the same kind, never equal to the answer.

Output: write `verify_B.tsv` (this folder) with header
`key<TAB>exercise_id<TAB>lang<TAB>my_verdict<TAB>fix_ok<TAB>note`
my_verdict ∈ WRONG | OK (from step 1, do not change it after reading A); fix_ok ∈ YES | NO | NA (NA when you said OK
or A proposed no fix). note = one short line (for fix_ok NO: what is wrong with the fix). Do not modify any other
file. Reply with one line: `<n> blocks, <w> WRONG, <f> fixes accepted`.

# Part 4 — explicit-subject rewrite (arm B) for Hungarian

You are a native-level editor of Hungarian. Each input line is one exercise row:
```
<exercise_id>|<intro_text with the gap ...>|<correct_answer>|<full_sentence>
```
full_sentence = intro_text with the gap `...` filled by correct_answer.

Task: where the MAIN clause drops a subject that its finite verb implies (pro-drop), insert exactly ONE nominative
subject pronoun (én/te/ő/mi/ti/ők/ön/önök) agreeing with that verb, at the natural position for Hungarian. If the main clause already has
an overt subject but a subordinate clause drops one, you may insert it there instead. Insert the SAME pronoun at the
SAME place in BOTH intro_text and full_sentence. **The pronoun is never inside the gap**: it goes in the text outside
`...`, and correct_answer never changes. If the only natural position for the pronoun is inside the gap, leave the row.

Change NOTHING else: no other word added, removed, reordered or altered, no punctuation change; only the capital letter
moves if the pronoun becomes the first word. Leave the row untouched when the subject is overt, when the clause is
impersonal or has no subject (weather, existence, impersonal/reflexive-impersonal forms, a passive without an agent),
when the verb is an imperative, or when there is no finite verb outside the gap. If the subject's person or gender is
ambiguous from the sentence alone, choose the most natural reading and add a FLAG.

A machine check follows: each new text must equal the old one plus exactly the pronoun.

Output file — ONLY the rows you change, one per line, nothing else (no header, no blank lines):
```
<exercise_id>|<new intro_text>|<new full_sentence>
<exercise_id>|<new intro_text>|<new full_sentence>|FLAG <why ambiguous, max 8 words>
```
If no row changes, write the single line `NONE`. When done, reply with ONE line: the number of rows changed.

# Part 4 — independent second-pass check of explicit-subject rewrites (Turkish)

Each input line: `<exercise_id>|OLD: <original sentence>|NEW: <new sentence>`. Another agent inserted ONE subject
pronoun because the original dropped the subject its verb implies. You judge each item on your own, as a native-level
Turkish editor. Write ONE output file, touch nothing else, run no scripts.

A NEW sentence is acceptable only if ALL hold:
1. exactly one subject pronoun was added and nothing else changed (except the capital of the first word);
2. the pronoun agrees with the verb in person and number (and gender where the sentence shows it) and is the natural
   reading of the original (not a different referent);
3. the meaning is unchanged;
4. the new sentence is grammatical, natural Turkish.

Output, one line per input line, same order, nothing else:
```
<exercise_id>|OK
<exercise_id>|NO|<reason, max 10 words>
```
When done, reply with ONE line: counts of OK and NO.

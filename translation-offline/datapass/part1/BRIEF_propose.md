# Part 1 — SK/CZ grammar check (proposer)

You are a native-level Slovak and Czech proofreader. Read your input file IN FULL and list the REAL errors in the
`sk` and `cz` rows. You write ONE output file and touch nothing else. Run no scripts.

## Input format
```
E <exercise_id> <level> | en: <the English sentence — meaning reference only>
sk|<intro_text with the gap ...>|<correct_answer>|<full_sentence>
cz|<intro_text>|<correct_answer>|<full_sentence>
NOTE <lang>: ...   (optional: the full_sentence is not what intro_text + correct_answer mechanically give)
```
`full_sentence` = `intro_text` with the gap `...` filled by `correct_answer` (a sentence-final gap gets a final `.`
added; a sentence-initial gap gets a capital). The sk/cz row is a TRANSLATION of the English exercise: the learner
answers in English and reads the sk/cz row only to understand it.

## What counts as an error (list ONLY these)
- agreement: gender/number/person of verb, adjective, participle (e.g. `šaty je` -> `šaty sú`);
- wrong case (preposition or verb government), wrong word form, wrong aspect that makes the sentence ungrammatical;
- typos and misspellings, wrong or missing diacritics, a wrong-language word (a Slovak word in a Czech row or vice versa);
- broken punctuation: a missing final `.`/`?`/`!` in full_sentence, doubled `??`, unbalanced quotes;
- `full_sentence` not equal to intro_text with the gap filled by correct_answer (see the NOTE lines).

## NOT errors — never list them
Style, word choice, a more elegant phrasing, register, slang, Gen-Z tone, word order that is grammatical, a translation
that is freer than the English, a distractor, anything about the English. The explicit subject pronoun (on/ona/oni/ja/ty…)
is intentional — never remove it. When unsure whether it is an error: it is not.

## How to fix
Keep the meaning, the explicit subject pronoun, the register/slang and the gap. Fix the smallest thing. If the fix
touches the word(s) inside the gap, fix `correct_answer` too, so that full_sentence == intro_text with the gap filled by
correct_answer. The gap `...` stays exactly where it is and appears exactly as often as before. A sentence-final gap:
intro_text ends on `...` (no period after it); full_sentence ends with `.`.

## Output (only rows with an error; nothing else in the file, no header, no blank lines)
```
<exercise_id>|<lang>|<new intro_text>|<new correct_answer>|<new full_sentence>|<short reason in English>
```
All three text fields always given in full, even when unchanged. No `|` inside a field. If the slice has no error,
write the file with the single line `NONE`.

When done, reply with ONE line: the number of lines written. Nothing else.

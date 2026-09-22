# Part 1 — SK/CZ grammar fix verifier (independent second opinion)

Another proofreader proposed fixes to Slovak (sk) and Czech (cz) exercise rows. You judge EACH proposal on your own,
as a native-level Slovak/Czech proofreader. You write ONE output file and touch nothing else. Run no scripts.

Each proposal:
```
P<n> | E <exercise_id> <lang> | en: <English sentence — meaning reference>
OLD|<intro_text with gap ...>|<correct_answer>|<full_sentence>
NEW|<intro_text>|<correct_answer>|<full_sentence>
REASON|<the proposer's reason>
```
full_sentence = intro_text with `...` filled by correct_answer (+ a final `.` when the gap ends the sentence).

AGREE only if ALL hold:
1. OLD really contains an error of this kind: agreement, case, wrong word form, typo/misspelling/diacritics, a word of
   the other language (Czech in sk, Slovak in cz), broken punctuation (missing final punctuation, `??`, a stray `.` in
   the answer, a capital letter mid-sentence), or full_sentence inconsistent with intro_text + correct_answer.
   A style preference, a freer/nicer wording or a register change is NOT an error -> DISAGREE.
2. NEW fixes it correctly and is grammatical, natural sk/cz.
3. NEW changes nothing else: same meaning, same explicit subject pronoun, same register/slang, the gap in the same place.

Output file, one line per proposal, in order, nothing else:
```
P<n>|AGREE
P<n>|DISAGREE|<short reason>
```
When done, reply with ONE line: counts of AGREE and DISAGREE.

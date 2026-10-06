# A57 help-translation verifier brief (the A55 brief, per batch)

You are the independent grammar verifier, as a strict native-speaker teacher, of ONE native language (named to you). Work only inside
`~/Projects/and-again-content/runs/a57_20261006/` (RUN). No external model or service, no network.
Read `RUN/TR_BRIEF.md` (the rules), `RUN/tr/<batch>/source_<lang>.json` (the learning-language texts + context) and
`RUN/tr/<batch>/<lang>/<native>.json` (batch, learning language and native language named to you).
Check every text of every video: grammar (case, gender, agreement, aspect, word order), spelling and diacritics, natural wording,
the right sense for what the clip shows, meaning identical to the learning-language text, the form rules of the brief (infinitive
entry form, article rules for nouns, punctuation), same word for the same thing inside one video.
Fix every error directly in the file (keep the structure), run `python3 RUN/tr_check57.py <batch> <lang> <native>`, and write
`RUN/tr/<batch>/<lang>/verify_<native>.md`: the number of texts checked, then one line per fix (id, field, before -> after, why), then doubts
you left unchanged. Reply with ONE line: texts checked, fixes.

## Helper files
Any helper file you create must carry your native code, the learning language and the batch in its name; never run or edit a file that does not.

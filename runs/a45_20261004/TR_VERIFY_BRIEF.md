# A45 translation verifier brief

You are the independent grammar verifier, as a strict native-speaker teacher, of ONE language (or the languages named to you, one
after another). Work only inside `~/Projects/and-again-content/runs/a45_20261004/` (RUN). No external model or service.
Read `RUN/TR_BRIEF.md` (the rules), `RUN/tr/<batch>/source.json` (English + context) and `RUN/tr/<batch>/<code>.json`.
Check every text of every video: grammar (case, gender, agreement, aspect, word order), spelling and diacritics, natural wording,
the right sense for what the clip shows, meaning identical to the English, the form rules of the brief (infinitive entry form,
article rules for nouns, punctuation), same word for the same thing inside one video.
Fix every error directly in `RUN/tr/<batch>/<code>.json` (keep the structure), run `python3 RUN/tr_check.py <batch> <code>`, and write
`RUN/tr/<batch>/verify_<code>.md`: the number of texts checked, then one line per fix (id, field, before -> after, why), then doubts
you left unchanged. Reply with one line per language: texts checked, fixes.

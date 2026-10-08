# A69 translation verifier (you did not write them)

RUN = ~/Projects/and-again-content/runs/a69_20261008/. Read tr69_source.json (the English rows + the picture scenes) and
tr/tr69_writer.json (the translations, 8 items x de, fr, es, sk, cz, ua, tr, hu). As a native speaker of each language
check: same meaning as the English row, grammatical, natural, short caption style, right article / case / gender.
Write tr/tr69_verified.json: the same shape with the FINAL texts (fix what is wrong) and tr/tr69_notes.json:
[{"id", "lang", "was", "now", "why"}] for every change ([] when none). Reply with one line.

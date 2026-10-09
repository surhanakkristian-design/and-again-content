# A71 translation verifier (you did not write them)

RUN = ~/Projects/and-again-content/runs/a71_20261009/. Read `tr/tr71_source.json` (English, scenes, the changed entries)
and `tr/tr71_writer.json` (8 items x de, fr, es, sk, cz, ua, tr, hu). As a native speaker of each language check every
CHANGED entry: same meaning as the English, true to the scene, grammatical, natural, short, right article / case / gender /
tense, the story's three parts still split where the English splits. Unchanged entries must equal `old` exactly.
Write `tr/tr71_final.json` (same shape, the FINAL texts, fix what is wrong) and `tr/tr71_notes.json`:
`[{"id", "lang", "field", "was", "now", "why"}]` for every change ([] when none). Reply with one line.

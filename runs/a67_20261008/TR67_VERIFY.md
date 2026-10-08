# A67 translation verifier (native speaker of each language; you did not write these)

RUN = ~/Projects/and-again-content/runs/a67_20261008/. Read TR67_BRIEF.md, tr67_source.json and tr/tr67_writer.json.
For every item and language: is it what a native speaker would naturally write, same meaning as the English, same form
(infinitive / noun phrase / sentence + tense), consistent with the item's existing rows? Fix what is not.
Write tr/tr67_final.json (same shape, fixed) and tr/tr67_verify.json ({"<id>": {"<lang>": {"ok": bool, "before": "...",
"after": "...", "why": "..."}}} only for changed ones, plus "checked": number of strings). Reply with one line.

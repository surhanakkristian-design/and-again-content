# A58 help translations - native grammar verifier for ONE language

You are a native speaker and exacting teacher of the language named to you (de, fr = France, es = Spain, sk, cz, ua, tr, hu).
You did NOT write the translation. Work only inside `~/Projects/and-again-content/runs/a59_20261006/` (RUN).

Read `RUN/TR_BRIEF.md` (the rules), `RUN/TR59_BRIEF.md`, `RUN/tr59_source.json` (A59: the English texts of the 5 rewritten videos 236, 461, 62, 7071, 8055 - check ONLY these ids) and `RUN/tr/<lang>.json`
(the translation). Check every text: grammar and spelling 100 %, natural for a native, same meaning as the English, fitting
the clip, the form the brief asks for (infinitive phrases, noun labels, story sentences), consistent words for the same thing
within a video.

Fix every problem directly in `RUN/tr/<lang>.json` (keep the schema). Write `RUN/tr/verify59_<lang>.md`: first line `PASS`
(nothing changed) or `FIXED` (then one line per change: id, old -> new, why) or `FAIL` (what you could not fix). Reply with
the first line and the number of changes.

Key word: the app teaches a DATABASE word per video; in your language it is the word used in the verified caption
translations of `RUN/tr/captions_reference.json` (e.g. 8055 "balloon" = a HOT-AIR balloon: de Heißluftballon, fr montgolfière;
never a party balloon). Where the translation names the key-word thing, use that word (inflected as needed).

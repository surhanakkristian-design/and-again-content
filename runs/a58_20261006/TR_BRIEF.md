# A58 help translations - ONE native language

A learner of ENGLISH taps ⇄ in the app and sees these help texts in their NATIVE language. You translate the English texts
of 7 lab videos into your language (named to you): de German, fr French (France), es Spanish (Spain), sk Slovak, cz Czech,
ua Ukrainian, tr Turkish, hu Hungarian. Work only inside `~/Projects/and-again-content/runs/a58_20261006/` (RUN).

Source: `RUN/tr_source.json` - per video: `level`, `keyWord`, `description` (what the clip shows: context), `phrases` (3
infinitive phrases; `targets` = who does each), `nouns` (3 noun labels), `story` (3 sentences of a short funny story).

Write `RUN/tr/<lang>.json`:
```json
{ "lang": "de", "videos": { "8056": { "phrases": ["...", "...", "..."], "nouns": ["...", "...", "..."], "story": ["...", "...", "..."] }, ... } }
```
Rules
- Natural, grammatically perfect text a native teacher writes (standard spelling, every accent / diacritic; ua in Cyrillic).
- `phrases`: the natural infinitive / dictionary form of the phrase in your language (German verb last: "auf einer Bank
  sitzen"; Turkish infinitive "-mek/-mak"; Hungarian "-ni"), same meaning, fitting the clip. Never word-for-word when it sounds
  foreign.
- `nouns`: the noun as a label, the natural form for that thing (German with the indefinite article as the English has one:
  "eine Bank"; languages without articles: the bare noun; plural where the English is plural).
- `story`: each sentence translated naturally, keeping the joke / pun when your language allows (else a natural equivalent and
  say so in `notes`); same tense; one sentence per English sentence.
- Add `"notes": {"<id>": "..."}` for anything doubtful. Then reply with one line: your language, done, and any notes.

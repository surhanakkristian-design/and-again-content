# Phase 2C GATE 1 - defects found, RECORDED not fixed (19-20 Sept 2026)

Scope rule for this pass: fix exactly the three named reader defects, nothing else. Everything below was
found while doing that and was deliberately left alone.

1. **`cz_validate.py` carries its own tokenizer.** The g1..g4 slice exec'd by `derive_2b`/`derive_2c`
   (`phase1t/taskB/cz_validate.py`, from `WORD = re.compile` to `\nout = []`) defines a *second* `WORD`
   regex, independent of `f9.WORD`. The P1 alphabet fix does not reach it. It feeds only `voice_paths`
   (the g4 raw readings `sk_reflex` / `v3_passive_or_reflex` / `czech_se_missed_by_SK_REFLEX`), which no
   scored field uses, so it was left untouched - but any future use of g4 on Czech should patch it too.
2. **`tf` emits `"conditional"`** (2B DEFECTS_score #2 reconfirmed): the gold schema is past/present/future
   only, so every conditional reading is an automatic ERROR. Not one of the three named fixes.
   With it counted as ERROR, `tf` fails GATE 1 anyway; it is not the reason `tf` fails.
3. **`tense_open` is a definition mismatch, not a bug** (2B DEFECTS_score #3): script = f9 frame-set size,
   gold = "more than one English tense acceptable", and the gold itself flips on 13/100 sk rows. Left to
   the model, by instruction. Note the P1 tokenizer fix makes it *worse* on Czech (42.53 % -> 43.96 %),
   which is consistent with the mismatch: better Czech reading = more frames = more "open" claims.
4. **The tokenizer fix trades coverage for a little accuracy on the aspect lexicon.** `perfective_present`
   cz: 51/47/2 (A/C/E) -> 52/45/3. Coverage up, point error up (3.77 % -> 5.45 %). The field still passes,
   but the new decided rows are not free.
5. **`gender` is untouched by all three fixes** (cz 20.83 % -> 19.23 % only because two abstains became
   agreements; the 5 sk and 5 cz gender errors are the same rows). The residual gender source is the
   l-participle / pronoun gender path, not the three named defects.
6. **`_verbish` has no clause context in its signature.** The P2 guard therefore works on *sentence-level
   word forms* (a form that is preposition-governed anywhere in the sentence loses its verb reading
   everywhere in it). That is an over-generalisation; it is conservative (it can only remove verb readings,
   which turns errors into abstains), but a proper fix would pass the token index into `_verbish`.
7. **The three fixes were designed from examples in this same 200-row sample.** The AFTER numbers are
   in-sample and optimistic. Nothing here has been measured on rows the fixes were not designed against.

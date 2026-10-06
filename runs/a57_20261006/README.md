# A57 run folder (German, Spanish from Spain, French from France for the remaining 3,034 videos)

The A55 pipeline (decisions 394-401) over 31 batches of 100 videos (`data/bNNN.json`, A45 order), per language; decisions 402-406.
State: `python3 progress57.py` (also writes A57_PROGRESS.md to the Drive folder AndAgain_reports).

Per batch and language (the workflow `workflows/a57-batch.js` does all of it; args `{"batches": [{"batch": "b001", "ids": [...]}], "langs": ["de","es","fr"]}`):
1. Writers (`WRITER_BRIEF.md`, 5 videos each) -> `content/<lang>/<id>.json`; verifiers (`VERIFIER_BRIEF.md`) -> `verify/<lang>/<id>.md`
   (PASS / FIXED / FAIL). A FAIL gets one rewrite (first notes kept as `<id>.first.md`) and a second verification; still FAIL ->
   `data/skipped.json` (`<lang>:<id>`), listed in the report.
2. `trsource57.py <batch> <lang>` -> 8 translators (`TR_BRIEF.md`) -> 8 grammar verifiers (`TR_VERIFY_BRIEF.md`) -> `tr/<batch>/<lang>/<native>.json`.
3. `finish57.py <batch> <lang>`: merges help texts, records audio (`tts57.py`, voices.json), validates (`validate57.py --full`),
   builds `out/<batch>_<lang>_NN.sql` (25 rows each, guarded) + rollback, `batches/<batch>_<lang>.json`, `out/<batch>_<lang>.sha256`.
4. `apply_a57.sh <batch>_<lang>` (owner script, safe to rerun): `upload57.py` sends each audio file alone with retries and reads it
   back; only then backup + guarded insert. `applied/<name>` marks a batch in the database.
Sources: `build_src57.py` (live English rows `src/sets_en.json`, key words `src/wl.json`, concepts, A45 videos snapshot); frames
are links to the A45 frames. Recall rows (no English rows for these videos): the 3 tap phrases, at most one key-word noun, the
answer's tail. No carousel (pictures exist only for the 10 lab videos).
8039 fix (decision 403): `out/wl_8039.sql` applied (backup `backup/wl_6040_before.json`); rows rewritten in `content/{de,es}/8039.json`, batch `fix8039`.

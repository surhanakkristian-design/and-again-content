# A55 run folder (lab pilot: the 10 lab videos for learners of German, Spanish from Spain, French from France)

Steps (each resumable; `python3 progress.py` shows the state):
1. `build_src.py` (English source per video: live media_exercise_sets row, A56 carousel + recall, key words), `prep.py <ids>` (frames), stills, `draw55.py en <ids>`.
2. Writers (`WRITER_BRIEF.md`) -> `content/<lang>/<id>.json`; verifiers (`VERIFIER_BRIEF.md`) -> `verify/<lang>/<id>.md` (PASS / FIXED / FAIL). `validate55.py <lang> <ids>`.
3. `trsource.py de es fr` -> help translations (`TR_BRIEF.md`, one translator per native language) -> grammar verifier per native language (`TR_VERIFY_BRIEF.md`) -> `tr/<lang>/<native>.json` + `verify_<native>.md`; `tr_check.py <lang> <native>`.
4. `tts55.py <lang> <ids>` (voices.json; by voice identifier) -> `audio/<lang>/<id>/`.
5. `build_sql55.py de es fr` (validates everything with `--full`) -> `out/lab10_<lang>.sql` + rollback, `batches/lab10_<lang>.json`; `out/SHA256SUMS`.
6. `apply_a55.sh` (owner script; migration if missing, audio upload + read back, backup, guarded insert per language).
Rollback (not run): `out/lab10_<lang>_rollback.sql`, `out/a55_migration_rollback.sql`.

# Task: rewrite rejected Tinder texts (RETRY WRITER)

Working directory: ~/Projects/and-again-content/tinder_sentences_en. The slice name is in your prompt.
1. Read RULES.md and slices/<slice>_retry_in.md: for each media the description, the previous four texts and the
   verifier's or checker's reasons.
2. Rewrite ALL FOUR texts of each of those media so that every reason is fixed and no new problem appears. Prefer
   a short plain correct TRUE sentence (<= 30 characters) over a joke. Keep device variety.
3. Write slices/<slice>_retry.jsonl (same JSON line format as RULES/TASK_WRITER: id, ts, fs, tp, fp, tone, device,
   tense, pop), ONE Write call, then run python3 check.py slices/<slice>_retry.jsonl and fix any flag
   (device_repeat may be ignored here). Final message: one line, row count.

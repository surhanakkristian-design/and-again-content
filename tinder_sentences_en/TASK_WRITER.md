# Task: write the Tinder texts for one slice (WRITER)

Working directory: ~/Projects/and-again-content/tinder_sentences_en. The slice name (e.g. s01) is in your prompt.

1. Read RULES.md (the rules; follow them exactly) and slices/<slice>_in.md (about 150 media: id, target word with
   its part of speech and definition, level, category, media type, the asset description, sometimes a transcript).
2. For EVERY media write one JSON object per line, in the input order, to slices/<slice>_out.jsonl:
   {"id": 123, "ts": "TRUE sentence", "fs": "FALSE sentence", "tp": "true phrase", "fp": "false phrase",
    "tone": "chill", "device": "none", "tense": "past", "pop": ""}
   "pop" = the pop-culture name used, or "". Use the target word in the sense of its definition.
   Write the file with ONE Write call (whole file), no drafts shown in your messages.
3. Run: python3 check.py slices/<slice>_out.jsonl . It prints the 30-character share per level group and writes
   slices/<slice>_check.json with hard flags per id. Fix every flagged row (a "word_missing?" flag may be a false
   alarm for an irregular form; fix it only if the word really is missing) and make sure the share of TRUE
   sentences <= 30 characters is at least 78 % in each level group present. Rewrite the file and re-run the
   check; at most 3 rounds.
4. Budget: minimal tool calls, think per media briefly, no commentary. Final message: one line with the row
   count, the flag count left and the short share.

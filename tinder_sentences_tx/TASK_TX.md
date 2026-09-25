# Task: translate the Tinder texts of one slice (TRANSLATOR)

Working directory: ~/Projects/and-again-content/tinder_sentences_tx. Your prompt names the language code, the
language and the slice (e.g. sk Slovak t03).

1. Read RULES_TX.md and slices/<lang>/<slice>_in.txt (about 305 media: id | English word (part of speech):
   definition | loc: the app's translation of the word | tone, then the four English texts TS, FS, TP, FP).
   Read the files (the input in parts of about 800 lines if it is too big) until the END: every media must be translated.
2. Translate every media's four texts following RULES_TX.md. Write slices/<lang>/<slice>_out.tsv with ONE
   Write call: one line per media, in input order, TAB-separated, no header:
   id<TAB>TS<TAB>FS<TAB>TP<TAB>FP
   Optionally a 6th column: a short English note, ONLY when you had to deviate (e.g. loc word wrong for this
   sense, a reference swapped). No tabs or line breaks inside a text.
3. Do NOT run any checks and do not re-read your file. Budget: the reads, then one write.
   Final message: one line with the row count.

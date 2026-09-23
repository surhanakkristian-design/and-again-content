# Sentence-final punctuation — judgement task (And Again, 23 Sept 2026)

You judge rows of a language-learning database. Each row is ONE native-language sentence (`full_sentence`) that ends
WITHOUT a final `.`, `!` or `?`. The English row of the same exercise is given (`en_full_sentence`). `intro_text` is the
same sentence with the gap `...`; `correct_answer` fills the gap. You do NOT fix anything else in the sentence.

For every row decide the ONE final mark the native `full_sentence` should end with:
- Default: the mark of the English row (`.`, `!` or `?`).
- Use a different mark only when the native sentence itself clearly calls for it (e.g. it is grammatically a
  question — a question particle such as Turkish mı/mi/mu/mü, Ukrainian чи, a question word opening a direct
  question — while the English ends in `.`; or the English `!`/`?` does not fit the native wording).
- `NONE` when the row legitimately ends without a mark (e.g. it ends on an abbreviation that already carries its
  meaning, a quote, a title) — explain why.
- `UNSURE` when you cannot decide — explain why.

Input: `items_<lang>.jsonl` (one JSON object per line). Write your output to the file named in your instructions, one
line per row, tab-separated, nothing else:

    <row_id>\t<mark: . or ! or ? or NONE or UNSURE>\t<short reason in English>

Every input row_id must appear exactly once. Do not read any other file in this folder (in particular not any other
`out_*` file). At the end reply with one line: `done <lang> <rows>`.

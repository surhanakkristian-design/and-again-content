# DIAGNOSIS — why is `s04` refused?  (Phase 2F §1.2)

`cz_0002_s04_v` was refused with 429 on nine consecutive attempts across two phases, 919,962 tokens, zero rows. 2D's other give-ups were also `s04`, of cz_0002, cz_0003 and cz_0004. This asks whether the chunk itself is the cause. Everything below is measured; 0 DB access.

## 1. The prompt, byte for byte

Built by the runner's OWN prompt builder (`run_2f_cz.py: VPROMPT + batch_tasks`), so these are the exact bytes that were refused. The instruction header is **byte-identical** in every chunk (`header_identical: true` in every pair), so only the 100 row lines differ.

| chunk | bytes | chars | lines | max line | non-ASCII | distinct non-ASCII cp | control chars | Cf / bidi / NBSP / zero-width | lone surrogates | `<`+`>` |
|---|---|---|---|---|---|---|---|---|---|---|
| `cz_0002_s04_v` | 30839 | 30218 | 135 | 358 | 613 | 21 | none | none | 0 | 2 |
| `cz_0003_s04_v` | 31212 | 30615 | 135 | 353 | 595 | 17 | none | none | 0 | 2 |
| `cz_0004_s04_v` | 31980 | 31360 | 135 | 373 | 617 | 21 | none | none | 0 | 2 |
| `cz_0002_s03_v` | 31690 | 31057 | 135 | 386 | 621 | 23 | none | none | 0 | 2 |
| `cz_0001_s07_v` | 30903 | 30299 | 135 | 352 | 602 | 17 | none | none | 0 | 2 |
| `cz_0002_s05_v` | 31871 | 31261 | 135 | 357 | 608 | 15 | none | none | 0 | 2 |

**Codepoints that appear in `cz_0002_s04_v` and in NO successful chunk: none — the set is empty.**
For `cz_0003_s04_v`: none. For `cz_0004_s04_v`: Ú U+00DA LATIN CAPITAL LETTER U WITH ACUTE, – U+2013 EN DASH (an acute Ú and an en dash — ordinary Czech typography, and `cz_0004_s04_v` is not the chunk under test).

- No control characters besides newline; no lone surrogates; no Cf format characters, bidi marks, NBSP or zero-width characters anywhere, in any chunk.
- The only `<`/`>` characters are the two in the shared header, present in every chunk alike. No backticks, no triple quotes, no markup and no string that reads as an instruction or a policy trigger: every row line is one `json.dumps` object of the sentence, its English, the topic and the derived person/number flags.
- **`cz_0002_s04_v` is SMALLER than the chunks that succeeded**: 30839 bytes against 31690 (`cz_0002_s03_v`, -851), 30903 (`cz_0001_s07_v`, -64) and 31871 (`cz_0002_s05_v`, -1032). Its longest row is 358 characters against 386 in `cz_0002_s03_v`. It carries FEWER non-ASCII characters (613 vs 621).

Row-length distribution (min / Q1 / median / Q3 / max characters): `cz_0002_s04_v` [202, 248, 266, 289, 358], `cz_0002_s03_v` [217, 249, 271, 307, 386], `cz_0001_s07_v` [214, 240, 264, 300, 352]. Nothing in the tail is unusual.

## 2. Is `s04` always the same slice position?

Yes. Every Czech batch of 1,000 rows is cut into ten 100-row chunks, so `s04` is **chunk 4 of 10, batch offsets 300-399**, in every batch:

- `cz_0001_s04_v` = n 4365-4464 (4 of 10)
- `cz_0002_s04_v` = n 5365-5464 (4 of 10)
- `cz_0003_s04_v` = n 6365-6464 (4 of 10)
- `cz_0004_s04_v` = n 7365-7464 (4 of 10)

What those rows share: they are all `lang = cz`, all four CEFR levels in roughly the batch's own proportions ({'A1': 33, 'A2': 35, 'B1': 18, 'B2': 14} for cz_0002, {'A2': 32, 'B1': 21, 'B2': 17, 'A1': 30} for cz_0003), mean row line 270.0 / 274.0 characters, longest source sentence 86 / 89 characters — i.e. the same material as their neighbours.

**No source material is shared between the s04 chunks**: sentences in common cz_0002∩cz_0003 = 0, cz_0002∩cz_0004 = 0, cz_0003∩cz_0004 = 0, all three = 0; duplicate sentences inside each s04 = {'cz_0002': 0, 'cz_0003': 0, 'cz_0004': 0}. There is no common row, no common string, and no common anything except the ordinal position of the chunk in its batch.

## 3. `cz_0002_s04_v` once, as two 50-row halves

Same runner machinery (`run_2f_cz.py: session()`, same builder, same back-off), retry ceiling 3, halves run one after the other: n 5365-5414 then n 5415-5464.

| half | n | prompt bytes | exit | rows returned | tokens | wall s | retry attempts (429 / non-zero) | succeeded |
|---|---|---|---|---|---|---|---|---|
| h1 | 5365-5414 | 16887 | 0 | 50 | 0 | 0.0 | 0 | **YES** |
| h2 | 5415-5464 | 17073 | None | 0 | 218588 | 1586.4 | 4 | **NO** |

Total: 218588 tokens, 1586.4 s wall.

## 4. Conclusion

**Exactly one half succeeded: `h1` (n 5365-5414). That is the strongest evidence available and it localises the cause to that half's content.** The two halves differ as follows: h1 is 16887 prompt bytes against 17073, and covers n 5365-5414 against n 5415-5464. Everything the byte comparison in §1 measured is shared between them (same header, no control characters, no lone surrogates, no Cf/bidi/NBSP/zero-width, no markup, no codepoint absent from a successful chunk), so the distinguishing feature is not encoding but the rows themselves.

**Ruling for §1.3: halves did NOT both succeed, so `cz_0003_s04_v` gets ONE whole-chunk attempt under the retry ceiling of 3 and §1 confines the loss to its 100 rows.**

---

Facts file: `diag/s04_facts.json`. Halves record: `diag/halves_cz_0002_s04_v.json`. 0 Gemini calls, 0 DB access, nothing uploaded.

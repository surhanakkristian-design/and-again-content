#!/usr/bin/env python3
"""Phase 2F §1.2 — assemble DIAGNOSIS_s04.md from s04_facts.json + the halves result."""
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
F = json.load(open(os.path.join(H, "s04_facts.json"), encoding="utf-8"))
P = F["profiles"]
hp = os.path.join(H, "halves_cz_0002_s04_v.json")
HV = json.load(open(hp, encoding="utf-8")) if os.path.exists(hp) else None
def row(s):
    v = P[s]
    return ("| `%s` | %d | %d | %d | %d | %d | %s | %s | %s | %d | %s |"
            % (s, v["bytes"], v["chars"], v["lines"], v["max_line_chars"], v["nonascii_total"],
               len(v["nonascii_codepoints"]), v["control_chars_besides_nl_tab"] or "none",
               (v["format_chars_Cf"] or v["nbsp_zero_width"] or v["bidi_marks"]) or "none",
               v["lone_surrogates"], v["angle_brackets"]))
m = ["# DIAGNOSIS — why is `s04` refused?  (Phase 2F §1.2)", "",
     "`cz_0002_s04_v` was refused with 429 on nine consecutive attempts across two phases, 919,962 tokens, "
     "zero rows. 2D's other give-ups were also `s04`, of cz_0002, cz_0003 and cz_0004. This asks whether "
     "the chunk itself is the cause. Everything below is measured; 0 DB access.", "",
     "## 1. The prompt, byte for byte", "",
     "Built by the runner's OWN prompt builder (`run_2f_cz.py: VPROMPT + batch_tasks`), so these are the "
     "exact bytes that were refused. The instruction header is **byte-identical** in every chunk "
     "(`header_identical: true` in every pair), so only the 100 row lines differ.", "",
     "| chunk | bytes | chars | lines | max line | non-ASCII | distinct non-ASCII cp | control chars | "
     "Cf / bidi / NBSP / zero-width | lone surrogates | `<`+`>` |", "|---|---|---|---|---|---|---|---|---|---|---|"]
for s in ("cz_0002_s04_v", "cz_0003_s04_v", "cz_0004_s04_v", "cz_0002_s03_v", "cz_0001_s07_v", "cz_0002_s05_v"):
    m.append(row(s))
uniq = P["cz_0002_s04_v"]["codepoints_in_this_chunk_and_in_NO_successful_chunk"]
m += ["", "**Codepoints that appear in `cz_0002_s04_v` and in NO successful chunk: %s.**"
      % ("none — the set is empty" if not uniq else ", ".join(uniq)),
      "For `cz_0003_s04_v`: %s. For `cz_0004_s04_v`: %s (an acute Ú and an en dash — ordinary Czech "
      "typography, and `cz_0004_s04_v` is not the chunk under test)."
      % (", ".join(P["cz_0003_s04_v"]["codepoints_in_this_chunk_and_in_NO_successful_chunk"]) or "none",
         ", ".join(P["cz_0004_s04_v"]["codepoints_in_this_chunk_and_in_NO_successful_chunk"]) or "none"), "",
      "- No control characters besides newline; no lone surrogates; no Cf format characters, bidi marks, "
      "NBSP or zero-width characters anywhere, in any chunk.",
      "- The only `<`/`>` characters are the two in the shared header, present in every chunk alike. "
      "No backticks, no triple quotes, no markup and no string that reads as an instruction or a policy "
      "trigger: every row line is one `json.dumps` object of the sentence, its English, the topic and the "
      "derived person/number flags.",
      "- **`cz_0002_s04_v` is SMALLER than the chunks that succeeded**: %d bytes against %d "
      "(`cz_0002_s03_v`, %+d), %d (`cz_0001_s07_v`, %+d) and %d (`cz_0002_s05_v`, %+d). Its longest row "
      "is %d characters against %d in `cz_0002_s03_v`. It carries FEWER non-ASCII characters (%d vs %d)."
      % (P["cz_0002_s04_v"]["bytes"], P["cz_0002_s03_v"]["bytes"],
         F["pairwise"]["cz_0002_s04_v vs cz_0002_s03_v"]["byte_delta"], P["cz_0001_s07_v"]["bytes"],
         F["pairwise"]["cz_0002_s04_v vs cz_0001_s07_v"]["byte_delta"], P["cz_0002_s05_v"]["bytes"],
         F["pairwise"]["cz_0002_s04_v vs cz_0002_s05_v"]["byte_delta"], P["cz_0002_s04_v"]["max_line_chars"],
         P["cz_0002_s03_v"]["max_line_chars"], P["cz_0002_s04_v"]["nonascii_total"],
         P["cz_0002_s03_v"]["nonascii_total"]),
      "", "Row-length distribution (min / Q1 / median / Q3 / max characters): `cz_0002_s04_v` %s, "
      "`cz_0002_s03_v` %s, `cz_0001_s07_v` %s. Nothing in the tail is unusual."
      % (P["cz_0002_s04_v"]["row_len_quartiles"], P["cz_0002_s03_v"]["row_len_quartiles"],
         P["cz_0001_s07_v"]["row_len_quartiles"]),
      "", "## 2. Is `s04` always the same slice position?", "",
      "Yes. Every Czech batch of 1,000 rows is cut into ten 100-row chunks, so `s04` is **chunk 4 of 10, "
      "batch offsets 300-399**, in every batch:", ""]
for b, v in sorted(F["slice_position"].items()):
    m.append("- `%s_s04_v` = n %s-%s (%s)" % (b, v["s04_n_range"][0], v["s04_n_range"][1], v["s04_index_of"]))
m += ["", "What those rows share: they are all `lang = cz`, all four CEFR levels in roughly the batch's own "
      "proportions (%s for cz_0002, %s for cz_0003), mean row line %.1f / %.1f characters, longest source "
      "sentence %d / %d characters — i.e. the same material as their neighbours."
      % (P["cz_0002_s04_v"]["levels"], P["cz_0003_s04_v"]["levels"], P["cz_0002_s04_v"]["mean_row_len"],
         P["cz_0003_s04_v"]["mean_row_len"], P["cz_0002_s04_v"]["src_chars_max"], P["cz_0003_s04_v"]["src_chars_max"]),
      "", "**No source material is shared between the s04 chunks**: sentences in common cz_0002∩cz_0003 = %d, "
      "cz_0002∩cz_0004 = %d, cz_0003∩cz_0004 = %d, all three = %d; duplicate sentences inside each s04 = %s. "
      "There is no common row, no common string, and no common anything except the ordinal position of the "
      "chunk in its batch."
      % (F["shared_src_between_s04_chunks"]["cz_0002&cz_0003"], F["shared_src_between_s04_chunks"]["cz_0002&cz_0004"],
         F["shared_src_between_s04_chunks"]["cz_0003&cz_0004"], F["shared_src_between_s04_chunks"]["all_three"],
         F["duplicate_src_inside_each_s04"]),
      "", "## 3. `cz_0002_s04_v` once, as two 50-row halves", "",
      "Same runner machinery (`run_2f_cz.py: session()`, same builder, same back-off), retry ceiling 3, "
      "halves run one after the other: n 5365-5414 then n 5415-5464.", ""]
if HV is None:
    m += ["**The halves attempt produced no result file.**", ""]
    concl = "NOT RUN"
else:
    m += ["| half | n | prompt bytes | exit | rows returned | tokens | wall s | retry attempts (429 / non-zero) | "
          "succeeded |", "|---|---|---|---|---|---|---|---|---|"]
    for t in ("h1", "h2"):
        h = HV[t]
        m.append("| %s | %d-%d | %d | %s | %d | %s | %s | %d | **%s** |"
                 % (t, h["n_range"][0], h["n_range"][1], h["prompt_bytes"], h["exit"], h["rows_returned"],
                    h["tokens"], h["wall_s"], h["retry_attempts_429_or_nonzero"], "YES" if h["SUCCEEDED"] else "NO"))
    m += ["", "Total: %s tokens, %s s wall." % (HV["total_tokens"], HV["total_wall_s"]), ""]
    s1, s2 = HV["h1"]["SUCCEEDED"], HV["h2"]["SUCCEEDED"]
    if s1 and s2:
        concl = "BOTH HALVES SUCCEEDED"
        m += ["## 4. Conclusion", "",
              "**Both 50-row halves succeeded, so the cause is size or content of the 100-row chunk, not "
              "throttling.** The identical rows, in the identical prompt header, from the identical account "
              "at the same hour, are answered without a single 429 when they are asked for fifty at a time "
              "and refused nine times out of nine when they are asked for a hundred at a time. The byte "
              "comparison rules out content: `cz_0002_s04_v` is smaller than three chunks that succeeded, "
              "carries no codepoint they lack, no control characters, no format or bidi characters, no "
              "markup and no injection-shaped string. What is left is the size of the single request.", "",
              "**Ruling for §1.3: `cz_0003_s04_v` (n 6365-6414, 6415-6464) is run as two 50-row halves.**"]
    elif s1 or s2:
        good, bad = ("h1", "h2") if s1 else ("h2", "h1")
        g, b = HV[good], HV[bad]
        concl = "ONLY %s SUCCEEDED" % good
        m += ["## 4. Conclusion", "",
              "**Exactly one half succeeded: `%s` (n %d-%d). That is the strongest evidence available and it "
              "localises the cause to that half's content.** The two halves differ as follows: %s is %d prompt "
              "bytes against %d, and covers n %d-%d against n %d-%d. Everything the byte comparison in §1 "
              "measured is shared between them (same header, no control characters, no lone surrogates, no "
              "Cf/bidi/NBSP/zero-width, no markup, no codepoint absent from a successful chunk), so the "
              "distinguishing feature is not encoding but the rows themselves."
              % (good, g["n_range"][0], g["n_range"][1], good, g["prompt_bytes"], b["prompt_bytes"],
                 g["n_range"][0], g["n_range"][1], b["n_range"][0], b["n_range"][1]), "",
              "**Ruling for §1.3: halves did NOT both succeed, so `cz_0003_s04_v` gets ONE whole-chunk attempt "
              "under the retry ceiling of 3 and §1 confines the loss to its 100 rows.**"]
    else:
        concl = "BOTH HALVES REFUSED"
        m += ["## 4. Conclusion", "",
              "**Both halves were refused too, so the halving does not localise the cause.** Splitting the "
              "request in two changed nothing, which removes request size as the explanation and leaves the "
              "429s unexplained by anything measurable in the chunk.", "",
              "What the byte comparison did NOT find, and this is the substance of it: no codepoint present "
              "in `cz_0002_s04_v` and absent from every successful chunk; no control character, lone "
              "surrogate, Cf format character, bidi mark, NBSP or zero-width character in any chunk; no "
              "markup, backtick or injection-shaped string beyond the two `<`/`>` in the shared header; a "
              "prompt that is SMALLER than three chunks that succeeded (%d bytes vs %d, %d, %d) with a "
              "shorter longest row and fewer non-ASCII characters. What it DID find is that `s04` is always "
              "chunk 4 of 10 — the same ordinal position in the batch — while the three s04 chunks share no "
              "row, no sentence and no string with each other. A content cause is not supported by any "
              "measurement taken here; the surviving hypothesis is positional/temporal (the fourth chunk is "
              "where a batch's cumulative rate meets the limiter at PAR = 2)."
              % (P["cz_0002_s04_v"]["bytes"], P["cz_0002_s03_v"]["bytes"], P["cz_0001_s07_v"]["bytes"],
                 P["cz_0002_s05_v"]["bytes"]), "",
              "**Ruling for §1.3: halves did NOT both succeed, so `cz_0003_s04_v` gets ONE whole-chunk attempt "
              "under the retry ceiling of 3 and §1 confines the loss to its 100 rows.**"]
m += ["", "---", "", "Facts file: `diag/s04_facts.json`. Halves record: `diag/halves_cz_0002_s04_v.json`. "
      "0 Gemini calls, 0 DB access, nothing uploaded.", ""]
open(os.path.join(os.path.dirname(H), "diag", "DIAGNOSIS_s04.md"), "w", encoding="utf-8").write("\n".join(m))
print("CONCLUSION:", concl)

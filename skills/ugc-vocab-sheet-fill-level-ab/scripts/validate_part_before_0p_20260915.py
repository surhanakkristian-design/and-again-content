#!/usr/bin/env python3
"""
validate_part.py — hard integrity gate for one generated part workbook.

Run after EVERY chunk of content generation, and once more before delivery.
Exits non-zero on any ERROR. WARNs are reported and must be explained in the
run summary, not silently ignored.

  python validate_part.py part1.xlsx [--assets DIR] [--loanwords loanwords.json]

Checks (E = error, W = warning):
  E1  every sheet present, headers unchanged vs the template contract
  E2  All Words: only Level B rows, one part_of_speech token, category resolvable
  E3  media: one row per All Words row, title == <slug>_<media_id>,
      media_url/thumbnail_url end in <title>.mp4/.webp, image -> media_url == thumbnail_url,
      style_id in `styles`, media_type in {video,image}
  E4  media_categories: exactly one row per media_id, category_id in `categories`
  E5  word_concepts: unique concept id, no leading article, unique SENSE (word + pos +
      meaning resolved via concept_media -> media -> All Words column F); a concept whose
      media carry two different meanings is an error too
  E6  word_localizations: exactly 9 rows per concept, all 9 language codes, no empty translation
  E7  concept_media: exactly one row per media_id, concept_id resolvable
  E8  exercises: video media -> exactly 39 rows with type set 31..67+68+69;
      image media -> exactly 2 rows (68, 69); ids unique; no deprecated type (70+/POV);
      options_count in {2,3}
  E9  sentence_translations: exactly 9 rows per exercise, all 9 codes, no duplicate code;
      correct_answer + distractor_1 non-empty on the en row only (brief v26: the eight
      translating languages may leave an answer cell empty and may repeat an option);
      distractor_2 non-empty iff options_count == 3;
      intro_text empty on vocabulary types 68/69 and non-empty on grammar types
  E10 no English fallback: for langs != en, no text field byte-identical to the en row
      (unless every field is on the loanword allowlist)
  E11 byte-identical guard: no two language rows of one exercise identical across all fields
  W1  identical strings between close language pairs (sk/cz, hr/sr/bs) -> review
  W2  loanword drift: a concept's food/cultural term rendered differently in two places
  E12 assets (optional): every media title has a real file of the right type
  E13 length budgets: en intro_text <= 90, en options <= 50, and the source
      `meaning of the word` <= 50 (type 69 copies that field verbatim)
  E14 blank invariant: intro_text '...' count minus correct_answer '...' count == 1
      (types with a stem only; type 69's trailing dots are a stem, not a blank)
  E15 full_sentence: no double space, no leftover '...'; W: not the §3 derivation
      from intro_text and correct_answer (substitute, collapse, per-language
      punctuation spacing, final stop -- see interleave())
  E16 chunks/correct_alternative: valid JSON, chunks join back to full_sentence,
      every alternative is a permutation that keeps the opening piece first and the
      piece carrying the final punctuation last
"""
import argparse, json, os, re, sys
from collections import defaultdict, Counter
import openpyxl

LANGS = ["sk", "en", "de", "cz", "fr", "es", "ua", "tr", "hu"]
EN_LIMITS = [("intro_text", 90), ("correct_answer", 50),
             ("distractor_1", 50), ("distractor_2", 50)]   # English rows only
MEANING_LIMIT = 50   # HANDOFF says "under 50", the prompts "<= 50"; <= 50 is operative.
                     # Type 69 copies this field verbatim, so an over-long meaning breaks
                     # the exercise. Checked at source: A-level assets have no type 69, so
                     # the EN_LIMITS check on the type-69 row never sees them.
SIMPLE = {"A": 74, "B": 75}        # Simple Explanation — derived from the Label exercise
CONTRACT = {                       # level -> (types for a video, types for a still)
    "B": (set(range(31, 68)) | {68, 69, 75}, {68, 69, 75}),
    "A": (set(range(1, 28)) | {74},          {27, 74}),
}
VOCAB_TYPES = {27, 68, 69, 74, 75}
NO_INTRO_TYPES = {27, 68, 74, 75}   # Label + Simple Explanation: options only, no stem
STEM_TYPES = {69}            # 69 Meaning of the word: stem is '"<word>" means...' 
CLOSE_PAIRS = [("sk", "cz")]
HEADER_ROWS = 2

E, W, UNFINISHED = [], [], []


def err(code, msg):
    E.append(f"[{code}] {msg}")


def warn(code, msg):
    W.append(f"[{code}] {msg}")


def rows_of(ws, skip=1, example_col=None):
    """Real data rows: first column is an integer id, row is not an Example row.

    Robust to the presence or absence of the template's instruction / Example rows,
    so the same validator works on stripped and unstripped workbooks."""
    out = []
    for i, r in enumerate(ws.iter_rows(values_only=True), start=1):
        if i <= skip:
            continue
        if not any(c not in (None, "") for c in r):
            continue
        if example_col is not None and len(r) > example_col and \
           str(r[example_col]).strip().lower() in ("example", "exemple"):
            continue
        try:
            int(str(r[0]).strip())
        except (TypeError, ValueError):
            continue          # instruction row
        out.append((i, r))
    return out


def s(v):
    return "" if v is None else str(v).strip()


# --- full_sentence step 5/6, added 15.9.2026 (BRIEF §0o, ruled by Kristian) ----------
# Step 5 -- capitalise at a sentence-initial gap. Step 6 -- drop a sentence-ending
# stop out of text inserted into the middle of a sentence. Both are decided AT THE
# GAP SITE, never by a whole-string regex: a whole-string sentence-start test fires
# on '3 p.m. deadline' and '22:00' and produced 47 false positives when it was tried
# (REPORT_2026-09-15_06 section 3.1).

DROP_MIDSENTENCE_STOP = True    # step 6; the harness flips it to show it is a no-op
                                # on part 1 once the 48 English cells are corrected.

# Characters a sentence may legitimately open with before its first letter.
_OPENERS = " \t\"'`«»„“”‚‘’‹›([{¡¿-–—"

# A sentence-ending mark, any closing quote or bracket, then whitespace.
_SENT_END_RE = re.compile(r"[.!?][\"'”“»’›)\]]*\s+$")


def _upper_first_char(ch, lang):
    """Uppercase ONE character, language-aware.

    Turkish has two letters i: dotted i/I-with-dot and dotless I/i-without-dot.
    Python maps 'i' -> 'I', which in Turkish is a DIFFERENT LETTER -- 'istanbul'
    would become 'Istanbul' instead of the correct 'Istanbul-with-dot'. So tr is
    mapped explicitly before the default is used. The other seven languages
    (en de sk cz ua fr es hu) need nothing: their sentence-initial letters are
    covered by the default Unicode upper-case mapping, and the Hungarian digraphs
    cs/gy/sz capitalise on their first letter only, which is what this does.
    """
    if lang == "tr":
        if ch == "i":
            return "İ"          # dotted capital I
        if ch == "ı":           # dotless small i
            return "I"
    return ch.upper()


def _capitalise_first_letter(text, lang):
    """Capitalise the first LETTER of `text`, looking past an opening quote or
    bracket. `text` is returned unchanged when there is nothing to do:

      - it is empty or has no letter;
      - the letter is already a capital (nothing is EVER lower-cased here, so a
        German noun and a proper name come through untouched);
      - the first non-opening character is not a letter -- a digit or a symbol.
        A sentence may legitimately open on '22:00' or '30 blank pages', and
        capitalising the first letter INSIDE such a string would produce
        '22:00 Is the deadline'. Deliberate: opening quotes and brackets are
        stepped over, digits and symbols stop the search.
    """
    for i, ch in enumerate(text):
        if ch in _OPENERS:
            continue
        if not ch.isalpha():
            return text
        up = _upper_first_char(ch, lang)
        return text if up == ch else text[:i] + up + text[i + 1:]
    return text


def _gap_is_sentence_initial(before):
    """True when the gap opens a sentence: nothing precedes it in the stem, or
    what precedes it is a sentence-ending mark followed by whitespace."""
    return before.strip() == "" or bool(_SENT_END_RE.search(before))


def _gap_is_mid_sentence(rest):
    """True when the text after the gap continues the SAME sentence.

    False when the gap ends the stem (the answer's own stop is the sentence's
    stop and is correct), and false when what follows is itself a new
    capitalised sentence -- 'she drops two ... Total catastrophe!' + 'knives.'
    reads correctly and is one of the 8 benign English rows of
    REPORT_2026-09-15_06 section 4.1.
    """
    t = rest.lstrip()
    if t == "":
        return False
    return not t[:1].isupper()


def interleave(intro, answer, lang):
    """Derive full_sentence exactly as the live backfill did (BRIEF 9.9.2026 §3),
    plus the two gap-site rules ruled on 15.9.2026 (§0o).

    The steps are the recorded convention; the validator and the data must
    agree by construction, so this is the ONE implementation and nothing here is
    a second one.

      1. Substitute the answer for '...' with no padding.
      2. Collapse whitespace runs to one space.
      3. Delete a space before , . ; : ! ? -- except French, which keeps it
         before ; : ! ?
      4. Append a final '.' where the intro ended on the blank without one.
      5. Capitalise at a sentence-initial gap: the inserted option when there is
         one, otherwise the word the collapsing gap exposes (§0m empties cells,
         and 21 of the 32 observed rows have no option to capitalise).
      6. Drop a sentence-ending stop from the inserted option when the gap sits
         mid-sentence, so 'soap.' in 'There is not much ... left' cannot render
         'There is not much soap. left'.

    Substitute-then-collapse, never strip: SPEC_AMENDMENTS 1 stripped every part
    and joined with a space, which invents ' ?' / ' .' before final punctuation
    (row 155 of the live en rows) -- a defect the live data does not have.

    Returns None when the blank counts do not line up (E14 reports that); the
    caller must not compare against a truncated or duplicated sentence.
    """
    ap = answer.split("...")
    segs = intro.split("...")
    if len(segs) - 1 != len(ap):
        return None
    out = segs[0]
    for k, (a_part, seg) in enumerate(zip(ap, segs[1:])):   # 1. substitute, no padding
        rest = seg + "...".join(segs[k + 2:])               # the stem after THIS gap
        if a_part.strip():
            if DROP_MIDSENTENCE_STOP and _gap_is_mid_sentence(rest) \
               and a_part.rstrip()[-1:] in ".!?" \
               and not re.search(r"(?:\w\.){2,}$", a_part.rstrip()):   # 6. not 'p.m.'
                a_part = a_part.rstrip()[:-1]
            if _gap_is_sentence_initial(out):                          # 5. option
                a_part = _capitalise_first_letter(a_part, lang)
        elif _gap_is_sentence_initial(out):                            # 5. empty cell
            seg = _capitalise_first_letter(seg, lang)
        out += a_part + seg
    out = re.sub(r"\s+", " ", out).strip()             # 2. collapse runs
    if lang == "fr":                                    # 3. per-language spacing
        out = re.sub(r" +([,.])", r"\1", out)
    else:
        out = re.sub(r" +([,.;:!?])", r"\1", out)
    if intro.rstrip().endswith("...") and out and out[-1] not in ".?!":
        out += "."                                      # 4. final stop
    return out


def stem_sentence(intro, answer):
    """Derive full_sentence for type 69 (BRIEF 9.9.2026 v10 §6).

    Type 69 is a definition template, not a gapped sentence, so it has its own
    convention and none of the four steps apply: the definition follows the
    stem after exactly one space, and no final stop is added. Verified over all
    8,793 live type-69 rows: 8,787 are space padded, 6 already carry the space
    in the stem, 0 end in a stop, 0 match neither. Mirrors the SQL
        regexp_replace(intro_text, '\s*\.\.\.', ' ' || correct_answer)
    which replaces the first match only; the lambda keeps backslashes in the
    answer literal.
    """
    return re.sub(r"\s*\.\.\.", lambda m: " " + answer, intro, count=1)


def derive_full_sentence(intro, answer, lang, exercise_type):
    """The ONE dispatch used by the validator and by import_db.py.

    None for the no-stem types (nothing to derive) and for a blank-count
    mismatch (E14 reports that); stem_sentence for 69; interleave otherwise.
    """
    if exercise_type in NO_INTRO_TYPES:
        return None
    if exercise_type in STEM_TYPES:
        return stem_sentence(intro, answer)
    return interleave(intro, answer, lang)


def canon(word):
    return re.sub(r"^(a|an|the|to)\s+", "", s(word).lower())


def slug(word):
    return re.sub(r"[^a-z0-9]+", "_", s(word).lower()).strip("_")


def main(a):
    wb = openpyxl.load_workbook(a.workbook, read_only=True, data_only=True)
    need = ["All Words", "media", "media_categories", "word_concepts", "word_localizations",
            "concept_media", "exercises", "sentence_translations", "categories", "styles",
            "ALIAS - exercise_types"]
    for n in need:
        if n not in wb.sheetnames:
            err("E1", f"missing sheet {n!r}")
    if E:
        return report()

    cats = {int(r[0]): s(r[1]) for r in wb["categories"].iter_rows(values_only=True)
            if r[0] is not None and s(r[0]).isdigit()}
    cat_by_name = {v: k for k, v in cats.items()}
    styles = {int(r[0]) for r in wb["styles"].iter_rows(values_only=True)
              if r[0] is not None and s(r[0]).isdigit()}
    alias = {int(r[0]) for r in wb["ALIAS - exercise_types"].iter_rows(values_only=True)
             if r[0] is not None and s(r[0]).isdigit()}

    words = rows_of(wb["All Words"], example_col=9)
    seen_levels = {s(r[3]).upper() for _, r in words if len(r) > 3}
    level = "A" if seen_levels == {"A"} else ("B" if seen_levels == {"B"} else "AB")
    if level == "AB":
        print("contract: mixed A/B part — each media row keeps the contract of its own level")
    else:
        VIDEO_TYPES, IMAGE_TYPES = CONTRACT[level]
        print(f"contract: level {level} — {len(VIDEO_TYPES)} exercises per video, "
              f"{len(IMAGE_TYPES)} per still")
    level_of = {}   # media_id -> A/B
    media = rows_of(wb["media"], example_col=6)
    mcats = rows_of(wb["media_categories"], example_col=2)
    wcon = rows_of(wb["word_concepts"], example_col=3)
    wloc = rows_of(wb["word_localizations"], example_col=4)
    cmed = rows_of(wb["concept_media"])
    exes = rows_of(wb["exercises"])
    strs = rows_of(wb["sentence_translations"], example_col=7)

    # ---------- All Words ----------
    aw = {}
    for i, r in words:
        mid = s(r[0])
        if s(r[3]).upper() not in ("A", "B"):
            err("E2", f"All Words row {i}: level {s(r[3])!r}, expected A or B")
        level_of[mid] = s(r[3]).upper()
        if len(s(r[2]).split()) != 1:
            err("E2", f"All Words row {i}: part of speech {s(r[2])!r} must be one token")
        if s(r[6]) not in cat_by_name:
            err("E2", f"All Words row {i}: category {s(r[6])!r} not in `categories`")
        if mid in aw:
            err("E2", f"All Words row {i}: duplicate media_id {mid}")
        aw[mid] = r

    # ---------- media ----------
    md = {}
    for i, r in media:
        mid, title = s(r[0]), s(r[1])
        md[mid] = r
        if mid not in aw:
            err("E3", f"media row {i}: media_id {mid} has no All Words row")
            continue
        want = f"{slug(aw[mid][1])}_{mid}"   # title keeps the article: a_break_1, an_alley_1673
        if title != want and not title.startswith(want + "_"):
            err("E3", f"media row {i}: title {title!r} != {want!r}")
        mtype = s(r[5])
        if mtype not in ("video", "image"):
            err("E3", f"media row {i}: media_type {mtype!r}")
        if s(r[4]).isdigit() and int(s(r[4])) not in styles:
            err("E3", f"media row {i}: style_id {s(r[4])} not in `styles`")
        ext = ".mp4" if mtype == "video" else ".webp"
        if not s(r[2]).endswith(title + ext):
            err("E3", f"media row {i}: media_url must end in {title}{ext}")
        if not s(r[3]).endswith(title + ".webp"):
            err("E3", f"media row {i}: thumbnail_url must end in {title}.webp")
        if mtype == "image" and s(r[2]) != s(r[3]):
            err("E3", f"media row {i}: image media_url must equal thumbnail_url")
    for mid in aw:
        if mid not in md:
            err("E3", f"media_id {mid} in All Words has no `media` row")

    # ---------- media_categories ----------
    seen = Counter(s(r[0]) for _, r in mcats)
    for mid, n in seen.items():
        if n != 1:
            err("E4", f"media_categories: media_id {mid} has {n} rows (need exactly 1)")
    for i, r in mcats:
        if not s(r[1]).isdigit() or int(s(r[1])) not in cats:
            err("E4", f"media_categories row {i}: category_id {s(r[1])!r} unknown")
        elif s(r[0]) in aw and cats[int(s(r[1]))] != s(aw[s(r[0])][6]):
            err("E4", f"media_categories row {i}: category_id {s(r[1])} != All Words "
                      f"category {s(aw[s(r[0])][6])!r}")
    for mid in aw:
        if mid not in seen:
            err("E4", f"media_id {mid} has no media_categories row")

    # ---------- word_concepts ----------
    # A concept is a SENSE (ruling 10 Sept 2026): the same headword recurs across senses
    # on purpose (`bank` river / `bank` money), so uniqueness is judged on
    # (word, pos, meaning). word_concepts has no meaning column; it is resolved through
    # concept_media -> media -> All Words column F. A concept whose media disagree on
    # the meaning is the merged-sense defect itself and errors. Known limit: the match
    # is on the exact meaning string (SPEC_AMENDMENTS, 10 Sept 2026).
    meanings_of = defaultdict(set)
    for _, r in cmed:
        mid = s(r[2])
        if mid in aw:
            meanings_of[s(r[1])].add(s(aw[mid][5]).lower())
    con, by_sense = {}, {}
    for i, r in wcon:
        cid, w = s(r[0]), s(r[1])
        if cid in con:
            err("E5", f"word_concepts row {i}: duplicate concept id {cid}")
        if re.match(r"^(a|an|the)\s+", w.lower()):
            err("E5", f"word_concepts row {i}: word {w!r} still carries an article")
        if w != w.lower():
            err("E5", f"word_concepts row {i}: word {w!r} must be lowercase")
        ms = meanings_of.get(cid, set())
        if len(ms) > 1:
            err("E5", f"word_concepts row {i}: concept {cid} {w!r} carries {len(ms)} different "
                      f"meanings {sorted(ms)} — one sense per concept")
        meaning = next(iter(ms)) if len(ms) == 1 else ""
        key = (w, s(r[2]).lower(), meaning)   # noun `heat` / verb `heat` differ; so do two senses of a noun
        if key in by_sense:
            err("E5", f"word_concepts row {i}: word {w!r} ({key[1]}, {meaning!r}) already concept {by_sense[key]}")
        con[cid], by_sense[key] = w, cid

    # ---------- word_localizations ----------
    loc = defaultdict(dict)
    for i, r in wloc:
        cid, lang, tr = s(r[1]), s(r[2]), s(r[3])
        if cid not in con:
            err("E6", f"word_localizations row {i}: concept_id {cid} unknown")
        if lang not in LANGS:
            err("E6", f"word_localizations row {i}: language_code {lang!r}")
        if not tr:
            err("E6", f"word_localizations row {i}: empty translation (concept {cid}/{lang})")
        if lang in loc[cid]:
            err("E6", f"word_localizations row {i}: duplicate {lang} for concept {cid}")
        loc[cid][lang] = tr
    for cid in con:
        missing = set(LANGS) - set(loc[cid])
        if missing:
            err("E6", f"concept {cid} ({con[cid]}): missing localizations {sorted(missing)}")

    # ---------- concept_media ----------
    cm = Counter(s(r[2]) for _, r in cmed)
    for i, r in cmed:
        if s(r[1]) not in con:
            err("E7", f"concept_media row {i}: concept_id {s(r[1])} unknown")
        if s(r[2]) not in aw:
            err("E7", f"concept_media row {i}: media_id {s(r[2])} unknown")
        elif con.get(s(r[1])) != canon(aw[s(r[2])][1]):
            err("E7", f"concept_media row {i}: concept {s(r[1])} ({con.get(s(r[1]))}) "
                      f"!= word of media {s(r[2])} ({canon(aw[s(r[2])][1])})")
    for mid in aw:
        if cm[mid] != 1:
            err("E7", f"media_id {mid} has {cm[mid]} concept_media rows (need exactly 1)")

    # ---------- exercises ----------
    ex, by_media = {}, defaultdict(list)
    for i, r in exes:
        eid, cid, mid, t = s(r[0]), s(r[1]), s(r[2]), s(r[3])
        if eid in ex:
            err("E8", f"exercises row {i}: duplicate id {eid}")
        if not t.isdigit() or (int(t) not in alias and int(t) not in SIMPLE.values()):
            err("E8", f"exercises row {i}: exercise_type_id {t!r} not in ALIAS")
        elif int(t) >= 70 and int(t) not in SIMPLE.values():
            err("E8", f"exercises row {i}: deprecated exercise_type_id {t} (POV is gone — "
                      f"map to 68 Label the video)")
        if s(r[4]) not in ("2", "3"):
            err("E8", f"exercises row {i}: options_count {s(r[4])!r}")
        if cid not in con:
            err("E8", f"exercises row {i}: concept_id {cid} unknown")
        ex[eid] = r
        by_media[mid].append(int(t) if t.isdigit() else -1)
    for mid, types in by_media.items():
        if mid not in md:
            err("E8", f"exercises reference unknown media_id {mid}")
            continue
        vid_t, img_t = CONTRACT.get(level_of.get(mid, level), CONTRACT["B"]) if level == "AB" \
            else (VIDEO_TYPES, IMAGE_TYPES)
        expect = vid_t if s(md[mid][5]) == "video" else img_t
        got = set(types)
        if len(types) != len(expect) or got != expect:
            err("E8", f"media {mid} ({s(md[mid][5])}): {len(types)} exercises, expected "
                      f"{len(expect)}; missing {sorted(expect-got)}, extra {sorted(got-expect)}")
    for mid in aw:
        if mid not in by_media:
            err("E8", f"media_id {mid} has no exercises")

    # ---------- sentence_translations ----------
    loan = json.load(open(a.loanwords)) if a.loanwords and os.path.exists(a.loanwords) else {}
    allow = {v for vals in loan.values() for v in (vals.values() if isinstance(vals, dict) else [])}
    st = defaultdict(dict)
    for i, r in strs:
        eid, lang = s(r[1]), s(r[2])
        if eid not in ex:
            err("E9", f"sentence_translations row {i}: exercise_id {eid} unknown")
            continue
        if lang not in LANGS:
            err("E9", f"sentence_translations row {i}: language_code {lang!r}")
            continue
        if lang in st[eid]:
            err("E9", f"sentence_translations row {i}: duplicate {lang} for exercise {eid}")
        st[eid][lang] = (s(r[3]), s(r[4]), s(r[5]), s(r[6]),
                         s(r[7]), s(r[8]), s(r[9]))

    # type 69 (Meaning of the word): the English correct_answer IS the media's `meaning of the
    # word` (All Words column F), copied verbatim — the field is written to a 50-char budget
    # precisely so it can be used directly. Never the writer's own text.
    MEAN69 = {s(r[0]): s(r[5]) for r in wb["All Words"].iter_rows(min_row=2, values_only=True)
              if r[0] is not None and s(r[0]).isdigit()}
    for mid, meaning in sorted(MEAN69.items()):
        if meaning and len(meaning) > MEANING_LIMIT:
            err("E13", f"media {mid}: meaning is {len(meaning)} chars, "
                       f"limit {MEANING_LIMIT} ({meaning!r})")

    for eid, r in ex.items():
        got = st.get(eid, {})
        if "en" in got and int(s(r[3])) in STEM_TYPES:
            mid69 = s(r[2])
            if mid69 in MEAN69 and MEAN69[mid69] and got["en"][1] and got["en"][1] != MEAN69[mid69]:
                err("E9", f"exercise {eid}: type 69 en correct_answer must be the meaning column verbatim "
                          f"({MEAN69[mid69]!r}), got {got['en'][1]!r}")
        missing = set(LANGS) - set(got)
        if missing:
            err("E9", f"exercise {eid}: missing translations {sorted(missing)}")
            continue
        t, oc = int(s(r[3])), int(s(r[4]))
        for lang, (intro, ca, d1, d2, full, chunks_s, alt_s) in got.items():
            if a.phase == "en" and lang != "en":
                continue          # English pass only: the other 8 rows are still skeletons
            if a.phase == "en" and t in SIMPLE.values() and not ca:
                continue          # Simple Explanation is derived from Label after the language pass
            # BRIEF v26, 14.9.2026: English keeps both guards; the eight translating languages
            # lose them. An empty answer cell is a legitimate §0e outcome and duplicate options
            # are a legitimate §0a outcome. apply_lang.py counts them; nothing here refuses them.
            if lang == "en":
                if not ca:
                    err("E9", f"exercise {eid}/{lang}: empty correct_answer")
                if not d1:
                    err("E9", f"exercise {eid}/{lang}: empty distractor_1")
                if oc == 3 and not d2:
                    err("E9", f"exercise {eid}/{lang}: options_count 3 but distractor_2 empty")
            # BRIEF §0m, 15.9.2026 — for the eight translating languages the
            # `oc == 3 and not d2` guard is REMOVED OUTRIGHT, as it now is in
            # check_lang.py and apply_lang.py. The `(ca or d1)` carve-out that stood
            # here was written for the §0e ARTICLE shape, where a row is empty in all
            # three cells; §0m empties a cell whose English counterpart is any word at
            # all, so a filled correct_answer beside an empty distractor_2 is the
            # ruling, not a missing option. The safety net is the counter of §0l.
            if oc == 2 and d2:
                err("E9", f"exercise {eid}/{lang}: options_count 2 but distractor_2 filled")
            if t in NO_INTRO_TYPES and intro:
                err("E9", f"exercise {eid}/{lang}: type 68 (Label) must have empty intro_text")
            if t not in NO_INTRO_TYPES and not intro:
                err("E9", f"exercise {eid}/{lang}: type {t} needs intro_text")

            # SPEC_AMENDMENTS 3 -- the interleave only works when the counts line up.
            # Type 69 is excluded: its stem '"<word>" means...' ends in three dots that
            # are a stem, not a blank (verified live: 8,793 rows, three dots, no U+2026).
            if t not in NO_INTRO_TYPES and t not in STEM_TYPES:
                nb, na = intro.count("..."), ca.count("...")
                if nb - na != 1:
                    err("E14", f"exercise {eid}/{lang}: intro_text has {nb} '...' and "
                               f"correct_answer {na}; the difference must be exactly 1")

            # BRIEF 9.9.2026 §3/§4 -- full_sentence is derived by interleave(), the
            # recorded convention. Across all 212,747 live rows zero differ from it
            # by a letter or by case; the only differences are the 174 stray-space
            # rows (French spacing in non-French languages) that §5 fixes one
            # language at a time. The equality stays a WARNING so that a mismatch
            # never invites a blanket cross-language fix, which is what destroyed
            # 1,194 French rows.
            if full:
                if "  " in full:
                    err("E15", f"exercise {eid}/{lang}: full_sentence has a double space")
                if "..." in full:
                    err("E15", f"exercise {eid}/{lang}: full_sentence still contains '...'")
                want = derive_full_sentence(intro, ca, lang, t)
                if want is not None and full != want:
                    warn("E15", f"exercise {eid}/{lang}: full_sentence is not the §3 "
                                f"derivation; expected {want!r}, got {full!r}")

            # SPEC_AMENDMENTS 2 -- a permutation may not move the piece that opens the
            # sentence or the piece that carries the final punctuation.
            if chunks_s:
                try:
                    ch = json.loads(chunks_s)
                    alts = json.loads(alt_s) if alt_s else []
                except ValueError:
                    err("E16", f"exercise {eid}/{lang}: chunks/correct_alternative is not JSON")
                    ch, alts = None, []
                if ch:
                    if " ".join(ch) != full:
                        err("E16", f"exercise {eid}/{lang}: chunks do not join back to full_sentence")
                    for k, ap in enumerate(alts or []):
                        if sorted(ap) != sorted(ch):
                            err("E16", f"exercise {eid}/{lang}: alternative {k} is not a permutation")
                            continue
                        if ap[0] != ch[0]:
                            err("E16", f"exercise {eid}/{lang}: alternative {k} moved the opening piece")
                        if ap[-1] != ch[-1]:
                            err("E16", f"exercise {eid}/{lang}: alternative {k} moved the closing piece")
        for i, (name, lim) in enumerate(EN_LIMITS):
            if len(got.get("en", ("",) * 7)[i]) > lim:
                err("E13", f"exercise {eid}: en {name} is "
                           f"{len(got['en'][i])} chars, limit {lim}")
        # BRIEF v26: a language row whose answer cells are deliberately empty is FINISHED, not
        # pending. Completeness is judged on "intro_text OR correct_answer written": a §0e article
        # row in sk/cz/ua has an intro and no answers, an unwritten row has neither, and a type-27
        # Label row has an answer and no intro. So the E10/E11 identity checks still run on §0e rows.
        finished = all((got[l][0] or got[l][1]) for l in LANGS)
        if not finished:
            UNFINISHED.append(eid)
            continue
        if a.phase == "en":
            continue
        en = got["en"]
        for lang in LANGS:
            if lang == "en":
                continue
            if got[lang] == en and not all(x in allow or not x for x in got[lang]):
                err("E10", f"exercise {eid}/{lang}: byte-identical to the en row (English fallback)")
        seen_rows = {}
        for lang in LANGS:
            key = got[lang]
            if key in seen_rows:
                other = seen_rows[key]
                if (lang, other) in CLOSE_PAIRS or (other, lang) in CLOSE_PAIRS:
                    warn("W1", f"exercise {eid}: {other}/{lang} rows are identical — verify")
                elif "en" in (lang, other):
                    err("E10", f"exercise {eid}: {other}/{lang} rows identical")
                else:
                    err("E11", f"exercise {eid}: {other}/{lang} rows identical")
            seen_rows[key] = lang

    # ---------- loanword consistency ----------
    if loan:
        for cid, w in con.items():
            if w not in loan:
                continue
            for lang, want in loan[w].items():
                got = loc.get(cid, {}).get(lang)
                if got and got.lower() != want.lower():
                    warn("W2", f"concept {cid} ({w})/{lang}: {got!r} != agreed loanword {want!r}")

    # ---------- assets ----------
    if a.assets:
        have = {}
        for root, _, files in os.walk(a.assets):
            for f in files:
                stem, extension = os.path.splitext(f)
                have.setdefault(stem.lower(), set()).add(extension.lower())
        for mid, r in md.items():
            title, mtype = s(r[1]).lower(), s(r[5])
            want = {".mp4"} if mtype == "video" else {".webp", ".png", ".jpg", ".jpeg"}
            if title not in have:
                err("E12", f"asset missing for media {mid}: {title}")
            elif not (have[title] & want):
                err("E12", f"asset type mismatch for {title}: {sorted(have[title])}")

    print(f"{os.path.basename(a.workbook)}: {len(words)} words, {len(con)} concepts, "
          f"{len(ex)} exercises, {len(strs)} translation rows")
    for line in contrast_share(ex, st):
        print(line)
    return report()

# ---- contrast share (ruling 10 Sept 2026): a NUMBER in the summary, never a verdict -------------
# An exercise may test the form; a share of the exercises must test the contrast, where both
# options are grammatical and the scene decides. The >50% aim lives in PROMPT_english_pass.md as
# guidance. This is a heuristic count over the English rows of types 23 and 6: a distractor is
# taken as grammatical-in-the-sentence when it is a modal that does not read "must to" / clash in
# agreement (23), or "the" with no forcer (what/such/there is/...) before the gap, or a/an before
# a singular countable head noun with no superlative/ordinal/unique/plural after the gap (6).
# Measured 10 Sept on 6.9.2026_A_part1: 23 -> 0/211; 6 -> 73/211 by hand vs 91/211 by this
# heuristic (side (b) over-counts plurals and fixed phrases). Report it; do not judge on it.
_C_MODAL = re.compile(r"^(must|mustn't|must not|have to|has to|had to|don't have to|doesn't have to|need to|needs to|needn't|should|shouldn't|ought to|can|can't|could|may|might)$", re.I)
_C_FORCER = re.compile(r"\b(what|such|there is|there's|there are|half|quite|rather|many|once)\s+\.\.\.", re.I)
_C_BLOCK = re.compile(r"\.\.\.\s+(\w+est|best|worst|first|second|third|last|next|same|only|most|whole|top|bottom|middle|end|beginning|sun|moon|sky|sea|floor|ground|world|internet|weather|police|air|dark|other)\b|\.\.\.\s+\w+s\b", re.I)
_C_MASS = re.compile(r"^(people|clothes|evidence|corn|traffic|fun|music|money|water|food|snow|rain|sand|bread|cheese|rice|hair|paint|time|work)$", re.I)


def contrast_share(ex, st):
    """Return summary lines: contrast items / rows for type 23 and type 6 (heuristic, no verdict)."""
    n, k = Counter(), Counter()
    for eid, r in ex.items():
        t = int(s(r[3])) if s(r[3]).isdigit() else -1
        row = st.get(eid, {}).get("en")
        if t not in (23, 6) or not row or not row[1]:
            continue
        intro, ca, d1, d2 = row[0], row[1], row[2], row[3]
        n[t] += 1
        if t == 23:
            before_to = bool(re.search(r"\.\.\.\s+to\b", intro))
            plural = bool(re.search(r"\b(you|we|they|both of them|\w+s)\s+\.\.\.", intro, re.I))
            ok = False
            for d in (d1, d2):
                dl = d.lower()
                if not _C_MODAL.match(d):
                    continue
                if before_to:
                    continue                                    # reads "must to" / "has to to"
                if dl in ("has to", "needs to", "doesn't have to") and plural:
                    continue                                    # agreement
                if dl in ("have to", "need to", "don't have to") and not plural \
                        and re.search(r"\b(he|she|it|the \w+|everyone|every \w+)\s+\.\.\.", intro, re.I):
                    continue                                    # agreement
                ok = True
            k[t] += ok
        else:
            opts = {ca.lower(), d1.lower(), d2.lower()}
            if ca.lower() in ("a", "an") and "the" in opts:
                k[t] += not _C_FORCER.search(intro)              # side (a): "the" stays grammatical
            elif ca.lower() == "the" and opts & {"a", "an"}:
                m = re.search(r"\.\.\.\s+(\w+)", intro)
                head = m.group(1).lower() if m else ""
                if not _C_BLOCK.search(intro) and not _C_MASS.match(head):
                    k[t] += 1                                    # side (b): a/an stays grammatical
    out = []
    for t, name in ((23, "type 23 must/have to"), (6, "type 6 a/an/the")):
        if n[t]:
            out.append(f"contrast share (heuristic, no verdict): {name} {k[t]}/{n[t]} = {k[t]/n[t]:.0%}")
    return out


PER_CLASS_SAMPLE = 20      # lines printed per error class, so a rare class is never
                           # hidden behind a dominant one (15.9.2026)
TOTAL_SAMPLE = 600         # overall cap on the listing, per stream


def _class_of(line):
    """The [En] tag a message was built with in err()/warn(); '[?]' if it has none."""
    m = re.match(r"\[([^\]]+)\]", line)
    return m.group(1) if m else "?"


def _tally(items):
    """Counts per class, in first-seen order — every class present, always."""
    counts = {}
    for it in items:
        c = _class_of(it)
        counts[c] = counts.get(c, 0) + 1
    return counts


def _print_stream(items, label, prefix):
    """Counts for EVERY class first, then a sample capped per class and overall."""
    if not items:
        return
    counts = _tally(items)
    print(f"\n{label} by class ({len(items)} total, {len(counts)} class(es)):")
    for c, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"  [{c}] {n}")
    print(f"\n{label} sample — up to {PER_CLASS_SAMPLE} per class, "
          f"{TOTAL_SAMPLE} in all:")
    shown, seen = 0, {}
    for it in items:
        c = _class_of(it)
        if seen.get(c, 0) >= PER_CLASS_SAMPLE:
            continue
        if shown >= TOTAL_SAMPLE:
            break
        seen[c] = seen.get(c, 0) + 1
        shown += 1
        print(prefix, it)
    hidden = len(items) - shown
    if hidden:
        print(f"  … {hidden} further {label.lower()} line(s) not printed "
              f"(counts above are complete)")


def report():
    if UNFINISHED:
        print(f"NOTE: {len(UNFINISHED)} exercises are not finished yet — "
              f"cross-language identity checks skipped for those")
    _print_stream(E, "ERRORS", "ERROR ")
    _print_stream(W, "WARNINGS", "WARN  ")
    print(f"\n{len(E)} errors, {len(W)} warnings")
    return 1 if E else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("workbook")
    ap.add_argument("--assets", default=None)
    ap.add_argument("--loanwords", default=None)
    ap.add_argument("--phase", default="all", choices=["all", "en"],
                    help="'en' checks only the English rows (content pass before translation)")
    sys.exit(main(ap.parse_args()))

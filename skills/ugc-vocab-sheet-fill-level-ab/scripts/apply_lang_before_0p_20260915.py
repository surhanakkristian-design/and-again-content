#!/usr/bin/env python3
"""
apply_lang.py — write the NON-ENGLISH sentence rows and the word rows of a part from a sidecar file.

    python3 apply_lang.py <workbook.xlsx> <content.txt> [--check] [--langs sk,de,...]
                          [--media 4007,4010,...] [--overwrite] [--loanwords loanwords.json]

The same contract as apply_en.py: everything in the file is validated against the workbook before
anything is written; one error and nothing is written; the workbook is saved once.

Content file (UTF-8, pipe-delimited; '#' lines and blank lines ignored):

    E <exercise_id>
    <lang>|<intro_text>|<correct_answer>|<distractor_1>|<distractor_2>
    W <concept_id>
    <lang>|<translation>

E blocks write `sentence_translations` for the eight languages sk de cz fr es ua tr hu, columns
intro_text, correct_answer, distractor_1, distractor_2 only — never full_sentence, chunks or
correct_alternative. `en` is REFUSED on an E block: English sentence rows belong to apply_en.py.
W blocks write `word_localizations.translation` for all nine languages, `en` included.

Refused as out of scope, and the whole file with it:
  a language code outside the eight (E) or the nine (W); a code outside --langs when given;
  an exercise whose media, or a concept not belonging to a media, outside --media when given;
  an exercise or concept not in the workbook, or with no row for that language;
  a block or a language row given twice;
  a target cell that already holds text, unless --overwrite.
Refused as malformed:
  wrong field count; intro_text filled on a no-intro type (27 68 74 75) or empty on a gapped type;
  the gap invariant broken (intro '...' count minus correct_answer '...' count must be 1, stems of
  type 69 excepted); a four-dot gap or a U+2026 ellipsis;
  distractor_2 filled against options_count 2 or empty against 3;
  a row byte-identical to its en row (English fallback, the validator's E10) unless every field is
  an agreed loanword; two languages of one exercise identical (E11) — sk/cz identical is a warning;
  the en row of that exercise still empty (nothing to translate from); an empty word translation.
Typography, loanword drift and the slang/idiom token check are warnings in check_lang.py, not here.

BRIEF v26, 14.9.2026 — Kristian's ruling. The empty-answer and distinct-options refusals are GONE for
the eight translating languages: "Bunka s odpoveďou môže byť prázdna, ak v tom jazyku nie je adekvátny
preklad … Preklad musieť/musieť môže nastať, takže aj viacero odpovedí v preklade môže byť rovnakých."
English is untouched — this script refuses `en` on an E block (apply_en.py owns those rows and keeps
both guards). In their place, a NON-BLOCKING counter: every empty answer cell and every duplicate-option
row is appended to `<workbook dir>/lang_counts/<lang>_gaps.csv` and the per-language totals are printed
next to the previous language's. Nobody reads the rows; the number is the point. Slovak articles give a
predictable count; three thousand empties in German means the pass broke.
"""
import json, re, sys
from collections import defaultdict
import openpyxl

LANGS8 = ["sk", "de", "cz", "fr", "es", "ua", "tr", "hu"]
LANGS9 = LANGS8 + ["en"]
NO_INTRO = {27, 68, 74, 75}
STEM = {69}
CLOSE = {frozenset(("sk", "cz"))}


def s(v):
    return "" if v is None else str(v).strip()


def arg(name):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else None


def count_gaps(rows, wbp):
    """Non-blocking. rows: (eid, lang, type, ca, d1, d2). Appends to <wbdir>/lang_counts/<lang>_gaps.csv
    and returns {lang: (n_empty, n_dup)}. Never raises into the caller and never fails a run."""
    import csv, os
    out = os.path.join(os.path.dirname(os.path.abspath(wbp)), "lang_counts")
    os.makedirs(out, exist_ok=True)
    tot = defaultdict(lambda: [0, 0])
    per = defaultdict(list)
    for eid, lang, t, ca, d1, d2 in rows:
        empty = [n for n, v in (("correct_answer", ca), ("distractor_1", d1), ("distractor_2", d2)) if not v]
        opts = [o.lower() for o in (ca, d1, d2) if o]
        dup = len(set(opts)) < len(opts)
        if empty:
            tot[lang][0] += 1
            per[lang].append((eid, t, lang, "empty", ";".join(empty)))
        if dup:
            tot[lang][1] += 1
            per[lang].append((eid, t, lang, "duplicate", ""))
    for lang, recs in per.items():
        f = os.path.join(out, f"{lang}_gaps.csv")
        new = not os.path.exists(f)
        with open(f, "a", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh)
            if new:
                w.writerow(["exercise_id", "exercise_type", "language", "kind", "fields"])
            w.writerows(recs)
    return {k: tuple(v) for k, v in tot.items()}


def prior_counts(wbp, skip):
    """The totals already on disk for the OTHER languages, so a run prints its number beside theirs."""
    import csv, glob, os
    out = os.path.join(os.path.dirname(os.path.abspath(wbp)), "lang_counts")
    res = {}
    for f in sorted(glob.glob(os.path.join(out, "*_gaps.csv"))):
        lang = os.path.basename(f).split("_")[0]
        if lang in skip:
            continue
        e = d = 0
        with open(f, encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                if row["kind"] == "empty":
                    e += 1
                elif row["kind"] == "duplicate":
                    d += 1
        res[lang] = (e, d)
    return res


def main():
    wbp, cpath = sys.argv[1], sys.argv[2]
    check_only = "--check" in sys.argv
    overwrite = "--overwrite" in sys.argv
    want_langs = set(arg("--langs").split(",")) if arg("--langs") else None
    want_media = {int(x) for x in arg("--media").split(",")} if arg("--media") else None
    allow = set()
    if arg("--loanwords"):
        for k, v in json.load(open(arg("--loanwords"), encoding="utf-8")).items():
            if isinstance(v, dict):
                allow.update(v.values())

    errors, warns = [], []
    sent, word = defaultdict(dict), defaultdict(dict)     # eid -> lang -> fields ; cid -> lang -> text
    kind, cur, seen_hdr = None, None, set()
    for n, raw in enumerate(open(cpath, encoding="utf-8"), 1):
        line = raw.rstrip("\n")
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^([EW]) (\d+)\s*$", line)
        if m:
            kind, cur = m.group(1), int(m.group(2))
            if (kind, cur) in seen_hdr:
                errors.append(f"line {n}: block {kind} {cur} given twice")
            seen_hdr.add((kind, cur))
            continue
        if kind is None:
            errors.append(f"line {n}: text row before any E or W header"); continue
        parts = line.split("|")
        lang = parts[0].strip()
        if kind == "E":
            if lang == "en":
                errors.append(f"line {n}: E {cur}: en sentence rows are written by apply_en.py, not here"); continue
            if lang not in LANGS8:
                errors.append(f"line {n}: E {cur}: {lang!r} is not one of {LANGS8}"); continue
            if len(parts) != 5:
                errors.append(f"line {n}: E {cur}/{lang}: expected 5 fields, got {len(parts)}"); continue
            if lang in sent[cur]:
                errors.append(f"line {n}: E {cur}/{lang} given twice"); continue
            sent[cur][lang] = tuple(p.strip() for p in parts[1:])
        else:
            if lang not in LANGS9:
                errors.append(f"line {n}: W {cur}: {lang!r} is not one of {LANGS9}"); continue
            if len(parts) != 2:
                errors.append(f"line {n}: W {cur}/{lang}: expected 2 fields, got {len(parts)}"); continue
            if lang in word[cur]:
                errors.append(f"line {n}: W {cur}/{lang} given twice"); continue
            word[cur][lang] = parts[1].strip()
        if want_langs is not None and lang not in want_langs:
            errors.append(f"line {n}: {kind} {cur}/{lang}: language outside --langs {sorted(want_langs)}")

    wb = openpyxl.load_workbook(wbp)
    ex = {}
    for r in wb["exercises"].iter_rows(min_row=2, values_only=True):
        if r[0] is not None and s(r[0]).isdigit():
            ex[int(r[0])] = (int(r[1]), int(r[2]), int(r[3]), int(r[4]))
    media_concepts = {mid: cid for cid, mid, _, _ in ex.values()}
    st, wl = wb["sentence_translations"], wb["word_localizations"]
    st_row, en = {}, {}
    for i, r in enumerate(st.iter_rows(min_row=2), start=2):
        if r[0].value is None or not s(r[0].value).isdigit():
            continue
        eid, lang = int(r[1].value), s(r[2].value)
        st_row[(eid, lang)] = i
        if lang == "en":
            en[eid] = tuple(s(r[k].value) for k in range(3, 7))
    wl_row = {}
    for i, r in enumerate(wl.iter_rows(min_row=2), start=2):
        if r[0].value is None or not s(r[0].value).isdigit():
            continue
        wl_row[(int(r[1].value), s(r[2].value))] = i

    for eid, langs in sent.items():
        if eid not in ex:
            errors.append(f"E {eid}: not in the workbook"); continue
        cid, mid, t, oc = ex[eid]
        if want_media is not None and mid not in want_media:
            errors.append(f"E {eid}: media {mid} outside --media"); continue
        if not any(en.get(eid, ())):
            errors.append(f"E {eid}: its en row is empty — nothing to translate from"); continue
        for lang, (intro, ca, d1, d2) in langs.items():
            tag = f"E {eid}/{lang}"
            if (eid, lang) not in st_row:
                errors.append(f"{tag}: no sentence_translations row for this language"); continue
            row = st_row[(eid, lang)]
            if not overwrite and any(s(st.cell(row=row, column=c).value) for c in range(4, 8)):
                errors.append(f"{tag}: target row already holds text (use --overwrite to replace)")
            if t in NO_INTRO and intro:
                errors.append(f"{tag}: type {t} must have an empty intro_text")
            if t not in NO_INTRO and not intro:
                errors.append(f"{tag}: type {t} needs intro_text")
            if t not in NO_INTRO and t not in STEM and intro.count("...") - ca.count("...") != 1:
                errors.append(f"{tag}: gap invariant broken — {intro.count('...')} gap(s) in intro, "
                              f"{ca.count('...')} in correct_answer")
            if "...." in intro or "…" in intro + ca + d1 + d2:
                errors.append(f"{tag}: four-dot gap or U+2026 ellipsis")
            # BRIEF v26: an empty correct_answer / distractor_1 is legal in the eight translating
            # languages (§0e articles, and any form the language does not have). Counted, not refused.
            #
            # BRIEF §0m, 15.9.2026 — the `oc == 3 and not d2` guard is REMOVED OUTRIGHT here, as it
            # already is in check_lang.py and in the eight-language branch of validate_part.py. The
            # `(ca or d1)` carve-out that stood here was written for the §0e ARTICLE shape, where a
            # row is empty in all three cells; §0m empties a cell whose English counterpart is any
            # word at all, so a row may legitimately have a filled correct_answer and an empty
            # distractor_2. Found by this gate refusing E 30557/de — German plural-only *Kosten*
            # takes no indefinite article, so both `a` cells are empty and `Die` is not. That is the
            # ruling, not a missing option. English keeps every guard, in apply_en.py (§0h.1); this
            # file only ever writes the eight translating languages.
            if oc == 2 and d2:
                errors.append(f"{tag}: options_count 2 but distractor_2 filled")
            # BRIEF v26: duplicate options are legal in the eight translating languages (musieť /
            # musieť, jeho / jeho). Counted, not refused.
            if (intro, ca, d1, d2) == en.get(eid) and not all(x in allow or not x for x in (intro, ca, d1, d2)):
                errors.append(f"{tag}: byte-identical to the en row (English fallback)")
        seen = {}
        for lang in sorted(langs):
            k = langs[lang]
            if k in seen:
                pair = frozenset((lang, seen[k]))
                (warns if pair in CLOSE else errors).append(f"E {eid}: {seen[k]}/{lang} rows identical")
            seen[k] = lang

    for cid, langs in word.items():
        if want_media is not None and cid not in {media_concepts[m] for m in want_media if m in media_concepts}:
            errors.append(f"W {cid}: concept outside --media"); continue
        for lang, text in langs.items():
            tag = f"W {cid}/{lang}"
            if (cid, lang) not in wl_row:
                errors.append(f"{tag}: no word_localizations row for this concept and language"); continue
            if not text:
                errors.append(f"{tag}: empty translation")
            if not overwrite and s(wl.cell(row=wl_row[(cid, lang)], column=4).value):
                errors.append(f"{tag}: target row already holds text (use --overwrite to replace)")

    n_sent = sum(len(v) for v in sent.values())
    n_word = sum(len(v) for v in word.values())
    langs_used = sorted({l for v in sent.values() for l in v} | {l for v in word.values() for l in v})
    if errors:
        print(f"REFUSED — {len(errors)} problem(s), nothing written:")
        for e in errors[:80]:
            print("  " + e)
        sys.exit(1)
    for w in warns[:40]:
        print("  warning " + w)
    if check_only:
        print(f"OK — {n_sent} sentence row(s) and {n_word} word row(s) in {langs_used} pass, nothing written (--check)")
        return
    for eid, langs in sent.items():
        for lang, vals in langs.items():
            row = st_row[(eid, lang)]
            for off, v in enumerate(vals):
                st.cell(row=row, column=4 + off).value = v
    for cid, langs in word.items():
        for lang, text in langs.items():
            wl.cell(row=wl_row[(cid, lang)], column=4).value = text
    wb.save(wbp)
    print(f"OK — {n_sent} sentence row(s) and {n_word} word row(s) in {langs_used} written")

    # --- non-blocking counter (BRIEF v26). Never fails the run. ---
    try:
        rows = [(eid, lang, ex[eid][2], v[1], v[2], v[3])
                for eid, langs in sent.items() for lang, v in langs.items()]
        now = count_gaps(rows, wbp)
        for lang in sorted(now):
            e, d = now[lang]
            print(f"counter {lang}: {e} empty-cell row(s), {d} duplicate-option row(s) "
                  f"of {sum(1 for r in rows if r[1] == lang)} written this batch")
        before = prior_counts(wbp, set(now))
        if before:
            print("counter, running totals of the other languages: "
                  + " | ".join(f"{l} {e}e/{d}d" for l, (e, d) in sorted(before.items())))
    except Exception as exc:                       # a counter must never stop a pass
        print(f"counter: skipped ({exc.__class__.__name__}: {exc})")


if __name__ == "__main__":
    main()

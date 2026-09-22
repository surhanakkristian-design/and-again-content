#!/usr/bin/env python3
"""
import_db.py — push a part workbook into Supabase, sheet by sheet, in foreign-key order.

  export SUPABASE_URL="https://<ref>.supabase.co"
  export SUPABASE_KEY="<service_role key>"
  python3 import_db.py --workbook part.xlsx                 # dry run: counts + first row per table
  ... --apply

Order is fixed and not negotiable — a child row inserted before its parent is rejected:

    styles → categories → media → media_categories → word_concepts
    → word_localizations → concept_media → exercises → sentence_translations

Every request is an upsert keyed on the primary key, so a re-run repairs a partial
import instead of duplicating it. Rows go in batches of 500.

`styles` and `categories` are reference tables shared by every part; they are imported
only with --reference, so a routine part import cannot disturb them.

`full_sentence` is never read from the workbook. It is derived at import time from
intro_text + correct_answer by validate_part.py::derive_full_sentence — the ONE
implementation: the four-step convention (BRIEF 9.9.2026 §3) for gapped sentences,
the space-padded stem rule for type 69 (v10 §6) — so new rows land non-null and enter
sentence_chunk_progress on their own. `chunks` and `correct_alternative` are never
sent: the chunk job writes them, and an upsert that carried them as null would erase
chunks already written when a part is re-imported.
"""
import argparse, json, os, sys, urllib.error, urllib.request
import openpyxl

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from validate_part import derive_full_sentence, NO_INTRO_TYPES   # same folder, one rule

# (sheet in the workbook, table in Supabase, sheet columns -> table columns)
# The workbook sheet names are NOT all table names: `media_categories` is the table
# `video_categories`, and `sentence_translations` is the table `exercise_localizations`.
ORDER = [
    ("media",                 "media",                  [
        ("id", "id"), ("title", "title"), ("media_url", "media_url"),
        ("thumbnail_url", "thumbnail_url"), ("style_id", "style_id"),
        ("media_type", "media_type")]),
    ("media_categories",      "media_categories",       [
        ("media_id", "media_id"), ("category_id", "category_id")]),
    ("word_concepts",         "word_concepts",          [
        ("id", "id"), ("word", "word"), ("part_of_speech", "part_of_speech")]),
    ("word_localizations",    "word_localizations",     [
        ("id", "id"), ("concept_id", "concept_id"),
        ("language_code", "language_code"), ("translation", "translation")]),
    ("concept_media",         "concept_media",          [
        ("id", "id"), ("concept_id", "concept_id"), ("media_id", "media_id")]),
    # NOTE: the live `exercises` table has no `options_count` column — the workbook
    # column stays in the sheet (the app derives the count from the distractors).
    ("exercises",             "exercises",              [
        ("id", "id"), ("concept_id", "concept_id"), ("media_id", "media_id"),
        ("exercise_type_id", "exercise_type_id")]),
    ("sentence_translations", "exercise_localizations", [
        ("id", "id"), ("exercise_id", "exercise_id"), ("language_code", "language_code"),
        ("intro_text", "intro_text"), ("correct_answer", "correct_answer"),
        ("distractor_1", "distractor_1"), ("distractor_2", "distractor_2")]),
]
# `categories`, `styles` and `exercise_types` hold jsonb titles and are maintained by
# hand in Supabase — a part import must never touch them.
CONFLICT = {"media_categories": "media_id,category_id"}
INT_COLS = {"id", "media_id", "category_id", "concept_id", "style_id",
            "exercise_id", "exercise_type_id", "options_count"}
BATCH = 500


def s(v):
    return "" if v is None else str(v).strip()


def rows_of(ws):
    out = []
    for i, r in enumerate(ws.iter_rows(values_only=True), start=1):
        if i == 1 or not any(c not in (None, "") for c in r):
            continue
        # No "example" row filter here. The template's example rows live in the
        # separate `EXAMPLE - A level` / `EXAMPLE - B level` sheets, which are not
        # in ORDER and are never imported; the numeric-id check below already
        # rejects header and note rows. Filtering on the *value* "example" silently
        # dropped the legitimate vocabulary word `example` (concept 1292) and its
        # en/fr localizations, which then failed as a foreign key violation.
        try:
            int(s(r[0]))
        except ValueError:
            continue
        out.append(r)
    return out


def shape(row, mapping):
    rec = {}
    for i, (_, col) in enumerate(mapping):
        v = row[i] if i < len(row) else None
        if col in INT_COLS:
            rec[col] = int(s(v)) if s(v) else None
        else:
            rec[col] = s(v) or None
    return rec


def derive_full_sentences(wb, rows, records):
    """sentence_translations only: set rec["full_sentence"] via derive_full_sentence.

    Type per exercise comes from the `exercises` sheet of the same workbook.
      - NO_INTRO_TYPES (27, 68, 74, 75): no stem, nothing to derive -> null.
      - 69: stem + one space + definition, no final stop (v10 §6).
      - everything else: the four-step interleave.
    Stops loudly on a blank-count mismatch (validate_part E14 catches it first) and on a
    workbook cell that disagrees with the derivation — the import never picks one.
    Returns (n_derived, n_null, per_language_counts).
    """
    etype = {}
    for r in rows_of(wb["exercises"]):
        etype[int(s(r[0]))] = int(s(r[3]))
    n_set, n_null, per_lang = 0, 0, {}
    for r, rec in zip(rows, records):
        eid, lang = rec["exercise_id"], rec["language_code"]
        if eid not in etype:
            sys.exit(f"sentence_translations: exercise_id {eid} is not in the exercises sheet")
        t = etype[eid]
        if t in NO_INTRO_TYPES:
            rec["full_sentence"] = None
            n_null += 1
            continue
        want = derive_full_sentence(rec["intro_text"] or "", rec["correct_answer"] or "", lang, t)
        if want is None:
            sys.exit(f"exercise {eid}/{lang}: '...' counts do not line up (E14) — "
                     f"run validate_part.py; the import does not guess")
        sheet_val = s(r[7]) if len(r) > 7 else ""          # column H, if someone filled it
        if sheet_val and sheet_val != want:
            sys.exit(f"exercise {eid}/{lang}: workbook full_sentence {sheet_val!r} differs "
                     f"from the derivation {want!r}; fix the source, not the import")
        rec["full_sentence"] = want
        n_set += 1
        per_lang[lang] = per_lang.get(lang, 0) + 1
    return n_set, n_null, per_lang


def post(base, key, table, records, on_conflict):
    url = f"{base}/rest/v1/{table}?on_conflict={on_conflict}"
    req = urllib.request.Request(
        url, data=json.dumps(records).encode(), method="POST",
        headers={"apikey": key, "Authorization": f"Bearer {key}",
                 "Content-Type": "application/json",
                 "Prefer": "resolution=merge-duplicates,return=minimal"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.status


def main(a):
    base = os.environ.get("SUPABASE_URL", "").rstrip("/")
    key = os.environ.get("SUPABASE_KEY", "")
    if a.apply and not (base and key):
        sys.exit("set SUPABASE_URL and SUPABASE_KEY in the environment first")

    wb = openpyxl.load_workbook(a.workbook, read_only=True, data_only=True)
    total = 0
    for sheet, table, mapping in ORDER:
        if sheet not in wb.sheetnames:
            print(f"{sheet:<22} no such sheet — skipped")
            continue
        rows = rows_of(wb[sheet])
        records = [shape(r, mapping) for r in rows]
        if table == "exercise_localizations":
            n_set, n_null, per_lang = derive_full_sentences(wb, rows, records)
            print(f"{'  full_sentence derived':<46} {n_set:>7} rows; "
                  f"{n_null} null (types {sorted(NO_INTRO_TYPES)}); "
                  f"per language {json.dumps(per_lang, sort_keys=True)}")
        conflict = CONFLICT.get(table, "id")
        label = f"{sheet} → {table}"
        print(f"{label:<46} {len(records):>7} rows", end="")
        if not a.apply:
            print(f"   e.g. {json.dumps(records[0], ensure_ascii=False)[:90]}" if records else "")
            total += len(records)
            continue
        sent = 0
        try:
            for i in range(0, len(records), BATCH):
                post(base, key, table, records[i:i + BATCH], conflict)
                sent += len(records[i:i + BATCH])
                print(f"\r{label:<46} {sent:>7}/{len(records)} sent", end="", flush=True)
        except urllib.error.HTTPError as e:
            body = e.read()[:300].decode("utf-8", "replace")
            print(f"\n  FAILED at row {sent}: HTTP {e.code} — {body}")
            sys.exit("stopped; fix the cause and re-run — upserts make this safe to repeat")
        print()
        total += sent

    print(f"\n{'imported' if a.apply else 'would import'} {total} rows")
    if not a.apply:
        print("dry run — add --apply to write")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--workbook", required=True)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--reference", action="store_true",
                    help="(unused — categories/styles/exercise_types are maintained by hand)")
    main(ap.parse_args())

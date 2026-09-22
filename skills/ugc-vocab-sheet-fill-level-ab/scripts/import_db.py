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

THE CONCEPT MAP (PROMPT 2026-09-17/04, ruling 2 — attach by judged sense)
  python3 import_db.py --workbook part.xlsx --concept-map PROPOSED_concept_map_6.9.2026.csv \
      --live-concepts live_concepts.json --sql-out import.sql [--commit] [--report-dir DIR]

With --concept-map the import is ONE SQL transaction, never the REST upserts (a partial
attach cannot be left half-written). Per media, the map's `proposal` decides:
  <live concept id>  ATTACH — concept_media and exercises.concept_id point at the live concept;
                     the part's own word_concepts / word_localizations rows are DROPPED.
                     If the live concept's definition is empty it is filled from All Words F;
                     if both exist and differ, the live one is kept and the pair is reported.
  NEW / NEW-SENSE / DECIDE-POS / HOLD-UNSURE
                     a new concept, as before, with definition = All Words F.
Rows are plain INSERTs, not upserts: an id that already exists fails the transaction instead of
overwriting a row the app shows. Every inserted id is asserted above the live maximum of its
table (exercises: per block, main < 120000 and the Simple Explanation block), and the per-table
counts are asserted before the end. Without --commit the script ends by RAISING an exception
that carries the counts, so the database rolls the whole transaction back whatever the client
does with BEGIN/COMMIT.
"""
import argparse, json, os, sys, urllib.error, urllib.request
import openpyxl

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from validate_part import derive_full_sentence, NO_INTRO_TYPES   # same folder, one rule
from validate_part import blank_text_gaps, filled_text_counts, LANGS as ALL_LANGS
import lang_scope                                                 # BRIEF §0p, one module

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


def derive_full_sentences(wb, rows, records, profile=None):
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
        # BRIEF §0p: a language outside this type's scope is an empty row by ruling (validate_part
        # E18 refuses one that carries text). It goes in empty, with no full_sentence; the app
        # skips it exactly as it skips a missing row (GameplayScreen: learn `continue`, native nulls).
        if profile is not None and lang not in lang_scope.scope_for(t, profile):
            if any(rec.get(c) for c in ("intro_text", "correct_answer", "distractor_1", "distractor_2")):
                sys.exit(f"exercise {eid}/{lang}: out of scope for type {t} but carries text (E18)")
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


def text_safeguard(records):
    """Owner decision 28 (22.9.2026): FAIL the import when any of the nine languages has blank text
    (intro_text and full_sentence) on an exercise whose sk or en row has text. Run after
    derive_full_sentences. Returns the per-language filled-text counts (they go into the
    verification); exits on a gap, before anything is sent or any SQL is written."""
    by = {}
    for r in records:
        by.setdefault(r["exercise_id"], {})[r["language_code"]] = r
    gaps = blank_text_gaps(by)
    counts = filled_text_counts(records)
    print("filled text per language: " + json.dumps(counts))
    if gaps:
        per = {}
        for eid, L in gaps:
            per.setdefault(L, []).append(eid)
        lines = [f"  {L}: {len(v)} blank, e.g. {v[:5]}" for L, v in sorted(per.items())]
        sys.exit("IMPORT REFUSED: blank language text where sk/en have text "
                 f"({len(gaps)} rows)\n" + "\n".join(lines)
                 + "\nTranslate the rows (validate_part.py E20 lists them); the import does not upload blanks.")
    return counts


def lang_count_sql(cond, want):
    """Verification lines: per language, the rows with text among the imported localizations must
    equal the workbook's count (a blank, or a shifted column, fails the transaction)."""
    out = []
    for L in ALL_LANGS:
        out.append(f"  select count(*) into n from public.exercise_localizations where {cond} and language_code = '{L}' "
                   f"and (coalesce(btrim(intro_text), '') <> '' or coalesce(btrim(full_sentence), '') <> '');")
        out.append(f"  if n <> {int(want.get(L, 0))} then raise exception 'TEXT {L}: % rows with text <> {int(want.get(L, 0))}', n; end if;")
        out.append(f"  msg := msg || 'text_{L}=' || n || ' ';")
    return out


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
    if a.concept_map:
        return main_sql(a)
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
            text_safeguard(records)          # decision 28: before anything else can refuse or send
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


# ---------------------------------------------------------------------------------------------
# The concept-map import: one transaction, emitted as SQL
# ---------------------------------------------------------------------------------------------
LIVE_FLOOR_TABLES = ("media", "word_concepts", "word_localizations", "concept_media")
SE_BLOCK_START = 120000


def canon(word):
    import re
    return re.sub(r"^(a|an|the|to)\s+", "", s(word).lower())


def q(v):
    if v is None:
        return "NULL"
    if isinstance(v, int):
        return str(v)
    return "'" + str(v).replace("'", "''") + "'"


def values_sql(table, cols, recs, chunk=1000):
    out = []
    for i in range(0, len(recs), chunk):
        body = ",\n".join("(" + ",".join(q(r[c]) for c in cols) + ")" for r in recs[i:i + chunk])
        out.append(f"insert into public.{table} ({', '.join(cols)}) values\n{body};")
    return "\n".join(out)


def id_runs(ids):
    """[(lo, hi), ...] contiguous runs — the undo deletes by these ranges."""
    runs, ids = [], sorted(ids)
    for i in ids:
        if runs and i == runs[-1][1] + 1:
            runs[-1][1] = i
        else:
            runs.append([i, i])
    return [tuple(r) for r in runs]


def main_sql(a):
    import csv
    wb = openpyxl.load_workbook(a.workbook, read_only=True, data_only=True)
    recs = {}
    for sheet, table, mapping in ORDER:
        rows = rows_of(wb[sheet])
        recs[table] = [shape(r, mapping) for r in rows]
        if table == "exercise_localizations":
            text_counts = text_safeguard(recs[table])      # decision 28: refuse blanks before any SQL
            n_set, n_null, per_lang = derive_full_sentences(wb, rows, recs[table],
                                                            lang_scope.profile_for(a.workbook))
            print(f"full_sentence derived {n_set} rows; {n_null} null (types {sorted(NO_INTRO_TYPES)})")
            assert filled_text_counts(recs[table]) == text_counts
            for rec in recs[table]:
                # §0m/§0o: an empty answer is a ruled cell, not a missing one. The column is NOT NULL,
                # so it goes in as '' (the app skips a learning row with an empty answer and shows
                # null for a native one — screens/GameplayScreen.tsx).
                if rec["correct_answer"] is None:
                    rec["correct_answer"] = ""

    # All Words column F, per media
    definition = {}
    for r in rows_of(wb["All Words"]):
        definition[int(s(r[0]))] = s(r[5])

    live = json.load(open(a.live_concepts))
    live = live["rows"] if isinstance(live, dict) else live
    live_by_id = {int(r["id"]): r for r in live}

    def live_def(cid):
        r = live_by_id[cid]
        return s(r.get("definition")) or s(r.get("def69"))

    cmap = {}
    for r in csv.DictReader(open(a.concept_map, newline="", encoding="utf-8")):
        cmap[int(r["media_id"])] = r

    media_ids = [m["id"] for m in recs["media"]]
    part_concept_of_media = {cm["media_id"]: cm["concept_id"] for cm in recs["concept_media"]}
    part_concepts = {c["id"]: c for c in recs["word_concepts"]}
    problems = []

    target = {}          # part concept id -> live concept id (attach) | itself (create)
    attach_rows = []     # (media, word, live id, live def, part def)
    bucket_n = {}
    for mid in media_ids:
        m = cmap.get(mid)
        if m is None:
            problems.append(f"media {mid}: not in the concept map")
            continue
        pc = part_concept_of_media.get(mid)
        if pc is None or int(m["part_concept_id"]) != pc:
            problems.append(f"media {mid}: map part_concept_id {m['part_concept_id']} != workbook {pc}")
            continue
        if s(m["definition"]) != definition.get(mid, ""):
            problems.append(f"media {mid}: map definition {m['definition']!r} != All Words F "
                            f"{definition.get(mid)!r}")
        p = s(m["proposal"])
        if p.isdigit():
            lid = int(p)
            bucket_n["ATTACH"] = bucket_n.get("ATTACH", 0) + 1
            if lid not in live_by_id:
                problems.append(f"media {mid}: live concept {lid} does not exist")
                continue
            if canon(live_by_id[lid]["word"]) != canon(part_concepts[pc]["word"]):
                problems.append(f"media {mid}: word {part_concepts[pc]['word']!r} != live {lid} "
                                f"{live_by_id[lid]['word']!r}")
            if target.get(pc, lid) != lid:
                problems.append(f"part concept {pc}: attached to two live concepts")
            target[pc] = lid
            attach_rows.append((mid, part_concepts[pc]["word"], lid, live_def(lid), definition[mid]))
        elif p in ("NEW", "NEW-SENSE", "DECIDE-POS", "HOLD-UNSURE"):
            bucket_n[p] = bucket_n.get(p, 0) + 1
            target[pc] = pc
        else:
            problems.append(f"media {mid}: unknown proposal {p!r}")
    if len(set(cmap_part for cmap_part in (cmap[m]["part"] for m in media_ids if m in cmap))) > 1:
        problems.append("the workbook's media come from more than one part of the map")
    if problems:
        print("STOP — the map and the workbook disagree:")
        for p in problems:
            print("  " + p)
        sys.exit(2)

    created = {pc for pc, t in target.items() if t == pc}
    attached_pc = {pc for pc, t in target.items() if t != pc}
    wc = []
    for c in recs["word_concepts"]:
        if c["id"] in created:
            mids = [mid for mid, pc in part_concept_of_media.items() if pc == c["id"]]
            defs = {definition[mid] for mid in mids}
            if len(defs) != 1:
                sys.exit(f"concept {c['id']}: its media carry {len(defs)} different definitions")
            wc.append(dict(c, definition=defs.pop()))
        elif c["id"] not in attached_pc:
            sys.exit(f"concept {c['id']}: no media of the workbook maps to it")
    wl = [r for r in recs["word_localizations"] if r["concept_id"] in created]
    dropped_wl = [r for r in recs["word_localizations"] if r["concept_id"] in attached_pc]
    cm = [dict(r, concept_id=target[r["concept_id"]]) for r in recs["concept_media"]]
    ex = [dict(r, concept_id=target[r["concept_id"]]) for r in recs["exercises"]]
    el = recs["exercise_localizations"]
    mc = recs["media_categories"]

    # definitions for attached live concepts: fill when empty, keep + report when they differ
    fills, conflicts, same = {}, [], []
    for mid, word, lid, ldef, pdef in sorted(attach_rows):
        have = ldef or fills.get(lid)
        if not have:
            fills[lid] = pdef
        elif have != pdef:
            conflicts.append((mid, word, lid, have, pdef))
        else:
            same.append((mid, word, lid))

    main_ex = [r["id"] for r in ex if r["id"] < SE_BLOCK_START]
    se_ex = [r["id"] for r in ex if r["id"] >= SE_BLOCK_START]
    expect = {
        "media": len(recs["media"]), "media_categories": len(mc), "word_concepts": len(wc),
        "word_localizations": len(wl), "concept_media": len(cm), "exercises": len(ex),
        "exercise_localizations": len(el), "definition_fills": len(fills),
    }
    ranges = {
        "media": id_runs(r["id"] for r in recs["media"]),
        "word_concepts": id_runs(r["id"] for r in wc),
        "word_localizations": id_runs(r["id"] for r in wl),
        "concept_media": id_runs(r["id"] for r in cm),
        "exercises": id_runs(r["id"] for r in ex),
        "exercise_localizations": id_runs(r["id"] for r in el),
    }

    part = a.part or os.path.splitext(os.path.basename(a.workbook))[0].split("_")[-2].lower() + \
        os.path.splitext(os.path.basename(a.workbook))[0][-1]
    out = a.sql_out
    os.makedirs(out, exist_ok=True)
    attached_live = sorted({t for pc, t in target.items() if t != pc})
    COLS = {
        "media": ["id", "title", "media_url", "thumbnail_url", "style_id", "media_type"],
        "media_categories": ["media_id", "category_id"],
        "word_concepts": ["id", "word", "part_of_speech", "definition"],
        "word_localizations": ["id", "concept_id", "language_code", "translation"],
        "concept_media": ["id", "concept_id", "media_id"],
        "exercises": ["id", "concept_id", "media_id", "exercise_type_id"],
        "exercise_localizations": ["id", "exercise_id", "language_code", "intro_text", "correct_answer",
                                   "distractor_1", "distractor_2", "full_sentence"],
    }
    DATA = {"media": recs["media"], "media_categories": mc, "word_concepts": wc, "word_localizations": wl,
            "concept_media": cm, "exercises": ex, "exercise_localizations": el}
    FK_ORDER = list(COLS)
    fill_rows = [{"id": lid, "definition": d} for lid, d in sorted(fills.items())]

    def between(col, runs):
        return "(" + (" or ".join(f"{col} between {lo} and {hi}" for lo, hi in runs) or "false") + ")"

    mids = ",".join(map(str, media_ids))
    fill_ids = ",".join(map(str, sorted(fills))) or "0"

    def header(title):
        h = [f"-- import_db.py --concept-map · {os.path.basename(a.workbook)} · {title}",
             "set local statement_timeout = 0;"]
        if a.with_column:
            h.append(open(a.with_column).read())
        h.append("do $$ begin\n  if not exists (select 1 from information_schema.columns where table_schema='public' "
                 "and table_name='word_concepts' and column_name='definition') then\n"
                 "    raise exception 'word_concepts.definition does not exist — run task 1 first';\n  end if;\nend $$;")
        g = []
        # No live row may sit inside any new id run. (Until 17.9 run08 this was "live max < first new id",
        # which is right for the first part only: A1's media ids 4007-5506 surround A2's, so the max test
        # refuses a clean A2. A collision inside a run is what matters; plain inserts would fail on it too.)
        g.append(f"  if exists (select 1 from public.media where id in ({mids})) then "
                 f"raise exception 'FLOOR media: a live row already has one of the new ids'; end if;")
        for t in ("word_concepts", "word_localizations", "concept_media", "exercises"):
            for lo, hi in ranges[t]:
                g.append(f"  if exists (select 1 from public.{t} where id between {lo} and {hi}) "
                         f"then raise exception 'FLOOR {t}: live rows inside {lo}-{hi}'; end if;")
        for lo, hi in ranges["exercise_localizations"]:
            g.append(f"  if exists (select 1 from public.exercise_localizations where id between {lo} and {hi}) "
                     f"then raise exception 'FLOOR exercise_localizations: live rows inside {lo}-{hi}'; end if;")
        if attached_live:
            g.append(f"  if (select count(*) from public.word_concepts where id in ({','.join(map(str, attached_live))})) "
                     f"<> {len(attached_live)} then raise exception 'ATTACH: a live concept is missing'; end if;")
        h.append("do $$ begin\n" + "\n".join(g) + "\nend $$;")
        return h

    def tail(el_expect, el_runs, commit, text_want):
        counts = [
            ("media", f"select count(*) from public.media where id in ({mids})", expect["media"]),
            ("media_categories", f"select count(*) from public.media_categories where media_id in ({mids})", expect["media_categories"]),
            ("word_concepts", f"select count(*) from public.word_concepts where {between('id', ranges['word_concepts'])}", expect["word_concepts"]),
            ("word_localizations", f"select count(*) from public.word_localizations where {between('id', ranges['word_localizations'])}", expect["word_localizations"]),
            ("concept_media", f"select count(*) from public.concept_media where {between('id', ranges['concept_media'])}", expect["concept_media"]),
            ("exercises", f"select count(*) from public.exercises where {between('id', ranges['exercises'])}", expect["exercises"]),
            ("exercise_localizations", f"select count(*) from public.exercise_localizations where {between('id', el_runs)}", el_expect),
            ("definition_fills", f"select count(*) from public.word_concepts where id in ({fill_ids}) and definition is not null", len(fills)),
            ("concepts_with_definition", "select count(*) from public.word_concepts where definition is not null", None),
        ]
        body = []
        for k, q_, want in counts:
            body.append(f"  select ({q_}) into n;")
            if want is not None:
                body.append(f"  if n <> {want} then raise exception 'COUNT {k}: % <> {want}', n; end if;")
            body.append(f"  msg := msg || '{k}=' || n || ' ';")
        body += lang_count_sql(between("id", el_runs), text_want)      # decision 28: text per language
        body += [
            f"  select count(*) into n from public.exercises e join public.concept_media c on c.media_id = e.media_id "
            f"where e.media_id in ({mids}) and e.concept_id <> c.concept_id;",
            "  if n <> 0 then raise exception 'CONSISTENCY: % exercises on another concept than their media', n; end if;",
            f"  select count(*) into n from public.concept_media c left join public.word_concepts w on w.id = c.concept_id "
            f"where c.media_id in ({mids}) and w.id is null;",
            "  if n <> 0 then raise exception 'CONSISTENCY: % concept_media rows point at no concept', n; end if;",
            f"  select count(*) into n from public.word_concepts where {between('id', ranges['word_concepts'])} and definition is null;",
            "  if n <> 0 then raise exception 'DEFINITION: % created concepts without a definition', n; end if;",
            "  raise notice 'IMPORT OK %', msg;" if commit else "  raise exception 'DRY RUN OK, rolled back: %', msg;",
        ]
        return "do $$ declare n bigint; msg text := ''; begin\n" + "\n".join(body) + "\nend $$;"

    fills_sql = ("update public.word_concepts c set definition = v.d from (values\n"
                 + ",\n".join(f"({lid},{q(d)})" for lid, d in sorted(fills.items()))
                 + "\n) v(id, d) where c.id = v.id and c.definition is null;") if fills else ""
    MAXB = a.max_bytes
    written = []

    def w(name, parts):
        p = os.path.join(out, name)
        open(p, "w", encoding="utf-8").write("\n".join(x for x in parts if x) + "\n")
        written.append((name, os.path.getsize(p)))

    # el chunks under the byte ceiling
    parents = [values_sql(t, COLS[t], DATA[t]) for t in FK_ORDER[:-1]]
    parent_bytes = sum(len(x.encode()) for x in parents) + 40_000
    chunks, cur, size = [], [], 0
    for r in el:
        line = len(("(" + ",".join(q(r[c]) for c in COLS["exercise_localizations"]) + "),\n").encode())
        if cur and size + line > MAXB - parent_bytes:
            chunks.append(cur); cur, size = [], 0
        cur.append(r); size += line
    if cur:
        chunks.append(cur)

    # (1) the dry run with no staging: self-contained transactions that raise at the end
    for i, ch in enumerate(chunks, 1):
        w(f"{part}_dryrun_{i:02d}_of_{len(chunks):02d}.sql",
          header(f"DRY RUN chunk {i}/{len(chunks)} — raises, nothing persists")
          + parents + [values_sql("exercise_localizations", COLS["exercise_localizations"], ch, chunk=500), fills_sql,
                       tail(len(ch), id_runs(r["id"] for r in ch), commit=False, text_want=filled_text_counts(ch))])

    # (2) the real import: staged in import_stage (a schema the API does not expose), then ONE transaction
    st = f"import_stage.{part}_"
    TYPES = {c: ("bigint" if c in INT_COLS else "text") for t in COLS for c in COLS[t]}
    w(f"{part}_stage_10_create.sql",
      ["create schema if not exists import_stage;", "revoke all on schema import_stage from public, anon, authenticated;"]
      + [f"drop table if exists {st}{t}; create table {st}{t} ({', '.join(c + ' ' + TYPES[c] for c in COLS[t])});"
         for t in FK_ORDER]
      + [f"drop table if exists {st}definition_fills; create table {st}definition_fills (id bigint, definition text);"])
    load = [values_sql(st + t, COLS[t], DATA[t]).replace("public." + st, st) for t in FK_ORDER[:-1]]
    load.append(values_sql(st + "definition_fills", ["id", "definition"], fill_rows).replace("public." + st, st) if fill_rows else "")
    w(f"{part}_stage_11_load_parents.sql", load)
    for i, ch in enumerate(chunks, 1):
        w(f"{part}_stage_12_load_localizations_{i:02d}_of_{len(chunks):02d}.sql",
          [values_sql(st + "exercise_localizations", COLS["exercise_localizations"], ch, chunk=500).replace("public." + st, st)])
    stage_counts = dict(expect, definition_fills=len(fills))
    w(f"{part}_stage_20_verify.sql",
      ["select " + ", ".join(f"(select count(*) from {st}{t}) as {t}" for t in FK_ORDER + ["definition_fills"]) + ";"])

    def from_stage(commit):
        chk = "do $$ declare n bigint; begin\n" + "\n".join(
            f"  select count(*) into n from {st}{t}; if n <> {stage_counts[t]} then "
            f"raise exception 'STAGE {t}: % <> {stage_counts[t]}', n; end if;" for t in FK_ORDER + ["definition_fills"]) + "\nend $$;"
        ins = [f"insert into public.{t} ({', '.join(COLS[t])}) select {', '.join(COLS[t])} from {st}{t} order by 1;"
               for t in FK_ORDER]
        upd = (f"update public.word_concepts c set definition = f.definition from {st}definition_fills f "
               f"where c.id = f.id and c.definition is null;")
        return (["begin;"] + header("IMPORT from stage — " + ("COMMIT" if commit else "DRY RUN, raises"))
                + [chk] + ins + [upd, tail(expect["exercise_localizations"], ranges["exercise_localizations"], commit, text_counts),
                                 "commit;" if commit else "rollback;"])
    w(f"{part}_stage_30_import_DRYRUN.sql", from_stage(False))
    w(f"{part}_stage_31_import_COMMIT.sql", from_stage(True))
    w(f"{part}_stage_40_drop.sql", [f"drop table if exists {st}{t};" for t in FK_ORDER + ["definition_fills"]])

    # (3) the undo, exact ids, FK order, each delete asserted
    undo = [("exercise_localizations", "id", ranges["exercise_localizations"]),
            ("exercises", "id", ranges["exercises"]),
            ("concept_media", "id", ranges["concept_media"]),
            ("word_localizations", "id", ranges["word_localizations"]),
            ("word_concepts", "id", ranges["word_concepts"]),
            ("media_categories", "media_id", None),
            ("media", "id", None)]
    u = [f"-- UNDO {os.path.basename(a.workbook)} — exact ids, foreign-key order. Each step asserts its row count.",
         "begin;", "do $$ declare n bigint; begin"]
    for t, col, runs in undo:
        cond = between(col, runs) if runs is not None else f"{col} in ({mids})"
        u.append(f"  delete from public.{t} where {cond};\n  get diagnostics n = row_count;\n"
                 f"  if n <> {expect[t]} then raise exception 'UNDO {t}: % <> {expect[t]}', n; end if;")
        if t == "word_concepts" and fills:
            u.append(f"  update public.word_concepts set definition = null where id in ({fill_ids});\n"
                     f"  get diagnostics n = row_count;\n"
                     f"  if n <> {len(fills)} then raise exception 'UNDO definition fills: % <> {len(fills)}', n; end if;")
    u += ["  raise notice 'UNDO OK';", "end $$;", "commit;"]
    w(f"UNDO_{part}.sql", u)

    print(f"concept map buckets (media): {json.dumps(bucket_n, sort_keys=True)}")
    print(f"concepts created {len(wc)} | live concepts attached to {len(attached_live)} "
          f"(by {len(attach_rows)} media) | part word_concepts dropped {len(attached_pc)} | "
          f"part word_localizations dropped {len(dropped_wl)}")
    print(f"definitions for attached live concepts: fill {len(fills)} | identical {len(same)} | "
          f"conflict (live kept) {len(conflicts)}")

    def span(runs):
        return f"{runs[0][0]}-{runs[-1][1]} ({len(runs)} run{'s' if len(runs) > 1 else ''})"
    for t in FK_ORDER:
        rr = ranges.get(t) or id_runs(media_ids)
        print(f"  {t:<24} {expect[t]:>7} rows   ids {span(rr)}")
    print(f"SQL files in {out}:")
    for n_, b_ in written:
        print(f"  {n_:<52} {b_:>10,} B")

    if a.report_dir:
        os.makedirs(a.report_dir, exist_ok=True)
        with open(os.path.join(a.report_dir, "attachments.tsv"), "w", encoding="utf-8") as f:
            f.write("media_id\tword\tlive_concept_id\tlive_definition\tpart_definition\toutcome\n")
            for mid, word, lid, ldef, pdef in sorted(attach_rows):
                outcome = ("FILL" if lid in fills and fills[lid] == pdef and not ldef else
                           "CONFLICT-live-kept" if any(c[0] == mid for c in conflicts) else "IDENTICAL")
                f.write(f"{mid}\t{word}\t{lid}\t{ldef}\t{pdef}\t{outcome}\n")
        with open(os.path.join(a.report_dir, "undo_ranges.json"), "w") as f:
            json.dump({"ranges": ranges, "media_ids": media_ids, "definition_fills": sorted(fills),
                       "expect": expect}, f, indent=1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--workbook", required=True)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--reference", action="store_true",
                    help="(unused — categories/styles/exercise_types are maintained by hand)")
    ap.add_argument("--concept-map", help="approved concept map CSV — switches to the one-transaction SQL import")
    ap.add_argument("--live-concepts", help="JSON of live word_concepts (id, word, definition or def69)")
    ap.add_argument("--sql-out", help="DIRECTORY for the SQL file set (dry-run chunks, stage + import, undo)")
    ap.add_argument("--part", help="short part name used in file and stage-table names, e.g. a1")
    ap.add_argument("--max-bytes", type=int, default=1_400_000,
                    help="ceiling per SQL file (the Management API refuses bodies of ~2-4 MB with HTTP 413)")
    ap.add_argument("--with-column", help="SQL file prepended inside the transaction (dry run before task 1 is live)")
    ap.add_argument("--report-dir")
    main(ap.parse_args())

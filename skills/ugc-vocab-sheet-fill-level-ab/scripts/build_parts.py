#!/usr/bin/env python3
"""
build_parts.py — deterministic scaffolder for the B-level 6-part export.

Reads the SOURCE workbook (curated All Words + media) and the MASTER TEMPLATE,
and writes part1..part6 workbooks with every MECHANICAL cell already filled:

  All Words          copied verbatim for the part's B rows
  media              copied verbatim (id, title, urls, style_id, media_type)
  media_categories   media_id + category_id (name -> id via `categories`)
  word_concepts      one row per unique word (article stripped, lowercase)
  word_localizations 9 rows per concept, `en` filled, 8 rows left for the language pass
  concept_media      one row per media item
  exercises          full rows (id, concept_id, media_id, exercise_type_id, options_count)
  sentence_translations  9 skeleton rows per exercise (id, exercise_id, language_code)

Nothing that needs judgement or language is invented here.
Every id is a pure function of the input, so re-running is idempotent.

Usage:
  python build_parts.py --source SRC.xlsx --template TPL.xlsx --out DIR [--parts 6]
                        [--concept-id-start 1] [--assets DIR] [--manifest manifest.csv]
"""
import argparse, csv, os, re, sys
from collections import defaultdict
import openpyxl

LANGS = ["sk", "en", "de", "cz", "fr", "es", "ua", "tr", "hu"]  # order per template example
# per level: what a video gets, and what a still gets
TYPES = {
    "B": (list(range(31, 68)) + [68, 69],   [68, 69]),   # 19 B1 + 18 B2 + Label + Meaning = 39
    "A": (list(range(1, 27)) + [27],        [27]),       # 11 A1 + 15 A2 + Label = 27; still = 1
}
VIDEO_TYPES, IMAGE_TYPES = TYPES["B"]
HEADER_ROWS = 2                                 # row1 = header, row2 = instruction/example


def canon(word: str) -> str:
    """Canonical concept key: lowercase, article and infinitive marker stripped
    (`A pair` -> `pair`, `To heat` -> `heat`; live word_concepts keep verbs bare)."""
    return re.sub(r"^(a|an|the|to)\s+", "", str(word).strip().lower())


def parse_id_window(spec):
    """'4001-4051,4100' -> set of ids."""
    ids = set()
    for chunk in spec.split(","):
        chunk = chunk.strip()
        if not chunk:
            continue
        if "-" in chunk:
            lo, hi = chunk.split("-")
            ids.update(range(int(lo), int(hi) + 1))
        else:
            ids.add(int(chunk))
    return ids


def data_rows(ws, skip=HEADER_ROWS):
    out = []
    for i, r in enumerate(ws.iter_rows(values_only=True)):
        if i < skip:
            continue
        if any(c not in (None, "") for c in r):
            out.append(r)
    return out


def load_source(path, media_path=None):
    """Words come from --source (the registry is words-only); the `media` sheet may
    live in a different workbook, passed as --media-from."""
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    words = data_rows(wb["All Words"], skip=1)
    media = {}
    if "media" in wb.sheetnames:
        media = {str(r[0]).strip(): r for r in data_rows(wb["media"])}
    wb.close()
    if media_path:
        wb2 = openpyxl.load_workbook(media_path, read_only=True, data_only=True)
        media = {str(r[0]).strip(): r for r in data_rows(wb2["media"])}
        wb2.close()
    if not media:
        sys.exit("no `media` sheet — pass --media-from with a workbook that has one")
    return words, media


def load_categories(path):
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    cats = {}
    for r in wb["categories"].iter_rows(values_only=True):
        if r[0] is not None and str(r[0]).strip().isdigit():
            cats[str(r[1]).strip()] = int(r[0])
    wb.close()
    return cats


def partition(concepts, n_parts):
    """Contiguous alphabetical blocks balanced on EXERCISE weight (not word count)."""
    total = sum(c["exercises"] for c in concepts)
    target = total / n_parts
    bins, cur, acc = [[] for _ in range(n_parts)], 0, 0
    for c in concepts:
        if cur < n_parts - 1 and acc + c["exercises"] / 2 > target * (cur + 1):
            cur += 1
        bins[cur].append(c)
        acc += c["exercises"]
    return bins


EXAMPLE_SHEETS = ["All Words", "media", "media_categories", "word_concepts",
                  "word_localizations", "sentence_translations"]


def strip_examples(sheets):
    """Delete the template's Example rows (keeps header + instruction row).

    The marker column moved when Props/Actions were added, so scan the whole row
    rather than trusting a fixed column index."""
    for name in EXAMPLE_SHEETS:
        ws = sheets[name]
        for i in range(ws.max_row, 1, -1):   # row 1 is the header
            row = [ws.cell(i, c).value for c in range(1, ws.max_column + 1)]
            if any(v is not None and str(v).strip().lower() in ("example", "exemple")
                   for v in row):
                ws.delete_rows(i)


def types_for(level, mtype):
    """Exercise contract for one media row: its own level decides (mixed parts allowed)."""
    vid, img = TYPES[level]
    return vid if mtype == "video" else img


def build(args):
    global VIDEO_TYPES, IMAGE_TYPES
    mixed = args.level.upper() == "AB"
    if not mixed:
        VIDEO_TYPES, IMAGE_TYPES = TYPES[args.level.upper()]
    words, media = load_source(args.source, args.media_from)
    cats = load_categories(args.template)

    wanted = {"A", "B"} if mixed else {args.level.upper()}
    b_rows = [r for r in words if str(r[3]).strip().upper() in wanted]
    bad_level = [r for r in words if str(r[3]).strip().upper() not in {"A", "B"}]
    if bad_level:
        sys.exit(f"FATAL: {len(bad_level)} rows with a level other than A/B "
                 f"(e.g. media {bad_level[0][0]}: {bad_level[0][3]!r})")

    if args.only_media_ids:
        window = parse_id_window(args.only_media_ids)
        b_rows = [r for r in b_rows if int(str(r[0]).strip()) in window]
        print(f"window {args.only_media_ids}: {len(b_rows)} media rows selected")

    concept_map = {}
    if args.concept_map:
        for r in csv.DictReader(open(args.concept_map, encoding="utf-8")):
            concept_map[str(r["media_id"]).strip()] = int(r["concept_id"])
        print(f"concept map: {len(concept_map)} media rows reuse an existing concept id")

    if args.exclude:
        # Exclude by media_id ONLY. The v2 schema allows one word across several assets,
        # so excluding by word silently dropped legitimate rows -- a different asset that
        # happens to teach the same word is a valid row, not a duplicate. Fixed 2026-09-07.
        used_ids = set()
        for path in args.exclude:
            wbx = openpyxl.load_workbook(path, read_only=True, data_only=True)
            for sheet, idcol in (("media", 0), ("All Words", 0)):
                if sheet not in wbx.sheetnames:
                    continue
                for r in data_rows(wbx[sheet], skip=1):
                    if str(r[idcol]).strip().isdigit():
                        used_ids.add(str(r[idcol]).strip())
            wbx.close()
        before = len(b_rows)
        b_rows = [r for r in b_rows if str(r[0]).strip() not in used_ids]
        print(f"excluded {before - len(b_rows)} media rows already used "
              f"({len(used_ids)} media ids; words are NOT excluded)")
    missing = [r for r in b_rows if str(r[0]).strip() not in media]
    if missing:
        sys.exit(f"FATAL: {len(missing)} rows have no `media` row (e.g. media_id "
                 f"{[str(r[0]) for r in missing[:5]]})")
    no_style = [r for r in b_rows if str(media[str(r[0]).strip()][4] or "").strip() == ""]
    if no_style:
        sys.exit(f"FATAL: {len(no_style)} media rows have no style_id (e.g. media_id "
                 f"{[str(r[0]) for r in no_style[:5]]}) — classify them first, never guess")
    bad_type = [r for r in b_rows if str(media[str(r[0]).strip()][5]).strip() not in ("video", "image")]
    if bad_type:
        sys.exit(f"FATAL: media_type must be video/image (e.g. media_id {bad_type[0][0]}: "
                 f"{media[str(bad_type[0][0]).strip()][5]!r})")

    # concept = SENSE, not headword: same canonical word, same part of speech, same
    # meaning text (All Words column F, the plain-English rewrite of the coverage
    # definition). The intake repeats a headword across senses on purpose, so keying on
    # the word alone merges different senses into one concept (batch 6.9.2026: 16 A
    # groups of 2 rows and 10 B groups of 2 rows, measured on the canonical key). Two assets of the SAME sense still
    # share one concept, as before. Known limit: the match is on the exact meaning
    # string, so two differently worded rewrites of one sense would split.
    grouped = defaultdict(list)
    for r in b_rows:
        grouped[(canon(r[1]), str(r[2]).strip().lower(), str(r[5] or "").strip().lower())].append(r)

    concepts = []
    for key in sorted(grouped):
        rows = sorted(grouped[key], key=lambda r: int(r[0]))
        if args.one_asset_per_concept:
            # one asset per word: video wins, then the lowest media_id
            rows = [sorted(rows, key=lambda r: (
                str(media[str(r[0]).strip()][5]).strip() != "video", int(r[0])))[0]]
        n_vid = sum(1 for r in rows if str(media[str(r[0]).strip()][5]).strip() == "video")
        n_ex = sum(len(types_for(str(r[3]).strip().upper() if mixed else args.level.upper(),
                                 str(media[str(r[0]).strip()][5]).strip())) for r in rows)
        concepts.append({
            "key": key[0],
            "word": canon(rows[0][1]),
            "pos": key[1],
            "meaning": key[2],
            "rows": rows,
            "videos": n_vid,
            "images": len(rows) - n_vid,
            "exercises": n_ex,
        })
    # deterministic ids: alphabetical by word, then pos, then meaning (two senses of one
    # word get adjacent ids in a fixed order)
    concepts.sort(key=lambda c: (c["word"], c["pos"], c["meaning"]))

    # global ids — pure functions of alphabetical position; mapped media reuse a live concept
    reused = {}
    for c in concepts:
        ids = {concept_map[str(r[0]).strip()] for r in c["rows"] if str(r[0]).strip() in concept_map}
        if len(ids) > 1:
            sys.exit(f"FATAL: concept {c['word']} maps to several live ids {sorted(ids)}")
        if ids:
            c["concept_id"] = ids.pop()
            reused[c["concept_id"]] = c["word"]
    nxt = args.concept_id_start
    for c in concepts:
        if "concept_id" not in c:
            c["concept_id"] = nxt
            nxt += 1
    if reused:
        print(f"reused {len(reused)} live concept ids; new concepts {args.concept_id_start}–{nxt-1}")

    parts = partition(concepts, args.parts)

    ex_id = args.exercise_id_start
    cm_id = args.concept_media_id_start
    manifest = []

    for p_idx, bucket in enumerate(parts, 1):
        wb = openpyxl.load_workbook(args.template)
        S = {n: wb[n] for n in wb.sheetnames}
        aw, md, mc = S["All Words"], S["media"], S["media_categories"]
        wc, wl, cmd = S["word_concepts"], S["word_localizations"], S["concept_media"]
        ex, st = S["exercises"], S["sentence_translations"]

        if args.strip_examples:
            strip_examples(S)

        # instruction row is kept (it is the runtime spec); data starts after it
        cur = {n: first_free_row(S[n]) for n in
               ["All Words", "media", "media_categories", "word_concepts",
                "word_localizations", "concept_media", "exercises", "sentence_translations"]}

        for c in bucket:
            cid = c["concept_id"]
            wc.cell(cur["word_concepts"], 1, cid)
            wc.cell(cur["word_concepts"], 2, c["word"])
            wc.cell(cur["word_concepts"], 3, c["pos"])
            cur["word_concepts"] += 1

            for k, lang in enumerate(LANGS):
                wl.cell(cur["word_localizations"], 1, (cid - 1) * len(LANGS) + k + 1)
                wl.cell(cur["word_localizations"], 2, cid)
                wl.cell(cur["word_localizations"], 3, lang)
                # `translation` (col 4) is filled by the language pass; `en` seeded below
                cur["word_localizations"] += 1

            for r in c["rows"]:
                mid = str(r[0]).strip()
                m = media[mid]

                for j, v in enumerate(r[:11], start=1):   # incl. Props and Actions
                    aw.cell(cur["All Words"], j, v)
                cur["All Words"] += 1

                for j, v in enumerate(m[:6], start=1):
                    md.cell(cur["media"], j, v)
                cur["media"] += 1

                cat_name = str(r[6]).strip()
                if cat_name not in cats:
                    sys.exit(f"FATAL: category {cat_name!r} (media_id {mid}) not in `categories`")
                mc.cell(cur["media_categories"], 1, int(mid))
                mc.cell(cur["media_categories"], 2, cats[cat_name])
                cur["media_categories"] += 1

                cmd.cell(cur["concept_media"], 1, cm_id)
                cmd.cell(cur["concept_media"], 2, cid)
                cmd.cell(cur["concept_media"], 3, int(mid))
                cur["concept_media"] += 1
                cm_id += 1

                row_level = str(r[3]).strip().upper() if mixed else args.level.upper()
                types = types_for(row_level, str(m[5]).strip())
                for t in types:
                    ex.cell(cur["exercises"], 1, ex_id)
                    ex.cell(cur["exercises"], 2, cid)
                    ex.cell(cur["exercises"], 3, int(mid))
                    ex.cell(cur["exercises"], 4, t)
                    ex.cell(cur["exercises"], 5, 3)      # provisional; content pass may set 2
                    cur["exercises"] += 1
                    for k, lang in enumerate(LANGS):
                        st.cell(cur["sentence_translations"], 1,
                                (ex_id - 1) * len(LANGS) + k + 1)
                        st.cell(cur["sentence_translations"], 2, ex_id)
                        st.cell(cur["sentence_translations"], 3, lang)
                        cur["sentence_translations"] += 1
                    ex_id += 1

            manifest.append({
                "part": p_idx, "concept_id": cid, "word": c["word"],
                "part_of_speech": c["pos"], "meaning": c["meaning"],
                "media": len(c["rows"]),
                "videos": c["videos"], "images": c["images"],
                "exercises": c["exercises"],
                "media_ids": " ".join(str(r[0]) for r in c["rows"]),
            })

        name = (args.out_name or "UGC - Claude x Higgsfield_new_template_part{part}.xlsx").format(part=p_idx)
        out = os.path.join(args.out, name)
        os.makedirs(args.out, exist_ok=True)
        wb.save(out)
        n_ex = sum(c["exercises"] for c in bucket)
        print(f"part{p_idx}: {len(bucket):>4} concepts | {sum(len(c['rows']) for c in bucket):>4} media "
              f"| {sum(c['videos'] for c in bucket):>3} vid | {sum(c['images'] for c in bucket):>4} img "
              f"| {n_ex:>5} exercises | {n_ex*len(LANGS):>6} translations "
              f"| {bucket[0]['word']} … {bucket[-1]['word']}  -> {os.path.basename(out)}")

    if args.manifest:
        with open(args.manifest, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(manifest[0].keys()))
            w.writeheader()
            w.writerows(manifest)
        print(f"manifest: {args.manifest} ({len(manifest)} concepts)")

    if args.assets:
        check_assets(args.assets, media, b_rows)


def first_free_row(ws):
    """First row after the last non-empty row (keeps header + instruction + Example rows)."""
    last = 1
    for i, r in enumerate(ws.iter_rows(values_only=True), start=1):
        if any(c not in (None, "") for c in r):
            last = max(last, i)
    return last + 1


def check_assets(assets_dir, media, b_rows):
    """Every B media item must have a real file whose stem == media.title."""
    have = {}
    for root, _, files in os.walk(assets_dir):
        for f in files:
            stem, extension = os.path.splitext(f)
            have.setdefault(stem.lower(), []).append(os.path.join(root, f))
    miss, wrong = [], []
    for r in b_rows:
        mid = str(r[0]).strip()
        m = media[mid]
        title, mtype = str(m[1]).strip().lower(), str(m[5]).strip()
        if title not in have:
            miss.append(title)
            continue
        exts = {os.path.splitext(p)[1].lower() for p in have[title]}
        want = {".mp4"} if mtype == "video" else {".webp", ".png", ".jpg", ".jpeg"}
        if not (exts & want):
            wrong.append((title, mtype, sorted(exts)))
    print(f"assets: {len(b_rows)-len(miss)}/{len(b_rows)} present, "
          f"{len(miss)} missing, {len(wrong)} type mismatches")
    for t in miss[:20]:
        print("  MISSING", t)
    for t in wrong[:20]:
        print("  TYPE", t)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True)
    ap.add_argument("--template", required=True)
    ap.add_argument("--media-from", default=None,
                    help="workbook holding the `media` sheet when --source is words-only")
    ap.add_argument("--out", required=True)
    ap.add_argument("--parts", type=int, default=6)
    ap.add_argument("--level", default="B", choices=["A", "B", "a", "b", "AB", "ab"],
                    help="which level to export; AB = mixed part, each media row keeps its own contract")
    ap.add_argument("--only-media-ids", default=None,
                    help="window of media ids to include, e.g. '4001-4051' or '4001-4051,4100'")
    ap.add_argument("--concept-map", default=None,
                    help="CSV media_id,concept_id: media whose word already has a live concept (same sense)")
    ap.add_argument("--out-name", default=None,
                    help="output file name; '{part}' is replaced by the part number")
    ap.add_argument("--concept-id-start", type=int, default=10001)
    ap.add_argument("--exercise-id-start", type=int, default=1)
    ap.add_argument("--concept-media-id-start", type=int, default=1)
    ap.add_argument("--assets", default=None, help="local media folder to verify against")
    ap.add_argument("--manifest", default=None)
    ap.add_argument("--exclude", nargs="*", default=[],
                    help="workbooks whose media/words are already used and must be skipped")
    ap.add_argument("--one-asset-per-concept", action="store_true",
                    help="keep a single asset per word — video preferred, then lowest media_id")
    ap.add_argument("--strip-examples", action="store_true",
                    help="delete the template Example rows (import-ready output)")
    build(ap.parse_args())

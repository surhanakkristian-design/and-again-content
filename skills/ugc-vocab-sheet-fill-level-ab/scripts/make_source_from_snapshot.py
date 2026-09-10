#!/usr/bin/env python3
"""
make_source_from_snapshot.py — turn a read-only intake snapshot into a build source.

The intake snapshot ("All Words" only, categories in the coverage file's own taxonomy)
is never written to. This script reads it and writes a SOURCE workbook next to the part:

  All Words   the snapshot rows verbatim, except `Recommended category`, which is
              replaced by the app category from --categories (media_id,category_id,...)
  media       one row per asset: id, title, media_url, thumbnail_url, style_id, media_type
              title = <slug(word)>_<media_id>  (the file name in the asset store)
              video -> Words/<title>.mp4 + Thumbnails/<title>.webp
              image -> Words/<title>.webp, thumbnail_url == media_url (live convention)

media_type comes from --assignments (the intake's own CSV, read only); style_id from
--styles (media_id,style_id) and is left EMPTY for rows the styles file does not cover,
so build_parts.py can refuse them loudly instead of guessing.

Every asset row is checked against --assets: the file <title>.<ext> and, for videos,
Thumbnails/<title>.webp must exist. Missing -> the script prints the failure and stops.
"""
import argparse, csv, os, re, sys
import openpyxl

BASE = "https://abyrutykpvmzkfbesire.supabase.co/storage/v1/object/public"


def slug(word):
    return re.sub(r"[^a-z0-9]+", "_", str(word).strip().lower()).strip("_")


def main(a):
    wb = openpyxl.load_workbook(a.snapshot, read_only=True, data_only=True)
    aw_rows = [r for r in wb["All Words"].iter_rows(values_only=True)]
    header, rows = list(aw_rows[0]), [r for r in aw_rows[1:] if r[0] is not None]
    cats_by_name = {str(r[1]).strip(): int(r[0]) for r in wb["categories"].iter_rows(values_only=True)
                    if r[0] is not None and str(r[0]).strip().isdigit()}
    cats_by_id = {v: k for k, v in cats_by_name.items()}
    wb.close()

    mtype = {int(r["media_id"]): r["media_type"] for r in csv.DictReader(open(a.assignments, encoding="utf-8"))}
    cat = {}
    for r in csv.DictReader(open(a.categories, encoding="utf-8")):
        cid = int(r["category_id"])
        if cid not in cats_by_id:
            sys.exit(f"FATAL: categories file: media {r['media_id']} has category_id {cid}, not in the template")
        cat[int(r["media_id"])] = cats_by_id[cid]
    styles = {}
    if a.styles:
        styles = {int(r["media_id"]): int(r["style_id"]) for r in csv.DictReader(open(a.styles, encoding="utf-8"))}

    problems = []
    out = openpyxl.Workbook()
    ws = out.active
    ws.title = "All Words"
    ws.append(header[:11])
    md = out.create_sheet("media")
    md.append(["id", "title", "media_url", "thumbnail_url", "style_id", "media_type"])
    md.append(["instruction row kept for the scaffolder", "", "", "", "", ""])

    for r in rows:
        mid = int(r[0])
        if mid not in mtype:
            problems.append(f"media {mid}: not in the assignments CSV (no media_type)"); continue
        if mid not in cat:
            problems.append(f"media {mid}: no app category assigned"); continue
        row = list(r[:11])
        row[6] = cat[mid]
        ws.append(row)
        t = "video" if mtype[mid] == "video" else "image"
        title = f"{slug(r[1])}_{mid}"
        ext = ".mp4" if t == "video" else ".webp"
        f = os.path.join(a.assets, title + ext)
        if not os.path.isfile(f):
            problems.append(f"media {mid}: asset missing {f}")
        if t == "video":
            th = os.path.join(a.assets, "Thumbnails", title + ".webp")
            if not os.path.isfile(th):
                problems.append(f"media {mid}: thumbnail missing {th}")
            media_url, thumb_url = f"{BASE}/Words/{title}.mp4", f"{BASE}/Thumbnails/{title}.webp"
        else:
            media_url = thumb_url = f"{BASE}/Words/{title}.webp"
        md.append([mid, title, media_url, thumb_url, styles.get(mid), t])

    if problems:
        print(f"FATAL: {len(problems)} problem(s), nothing written:")
        for p in problems[:50]:
            print("  " + p)
        sys.exit(1)
    out.save(a.out)
    n_style = sum(1 for r in rows if int(r[0]) in styles)
    print(f"wrote {a.out}: {len(rows)} All Words rows, {len(rows)} media rows "
          f"({sum(1 for r in rows if mtype[int(r[0])]=='video')} video / "
          f"{sum(1 for r in rows if mtype[int(r[0])]!='video')} image), style_id set on {n_style}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--snapshot", required=True)
    ap.add_argument("--assignments", required=True, help="intake assignments CSV (read only)")
    ap.add_argument("--categories", required=True, help="CSV media_id,category_id[,...]")
    ap.add_argument("--styles", default=None, help="CSV media_id,style_id")
    ap.add_argument("--assets", required=True, help="Vocabulary_v2 folder")
    ap.add_argument("--out", required=True)
    main(ap.parse_args())

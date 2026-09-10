#!/usr/bin/env python3
"""
restage_from_v2.py — stage a part's assets by exact lookup, not by matching.

Every `media` row's media_url already ends in the asset's real basename
(<word_slug>_<media_id>.<ext>), and UGC Videos/Vocabulary_v2/ holds exactly one
file under each of those names. So staging is a lookup and a copy — there is
nothing to match and nothing to choose.

The Vocabulary_v2 files are already final format and already compressed, so they
are copied byte-for-byte. Re-encoding would be a second lossy generation.

Video thumbnails come from Vocabulary_v2/Thumbnails/ (named by thumbnail_url's
basename). Stills have media_url == thumbnail_url and need no thumbnail.

  python3 restage_from_v2.py --workbook WB.xlsx --v2 <Vocabulary_v2> --out <part> [--apply]
"""
import argparse, csv, os, shutil, sys
import openpyxl


def s(v):
    return "" if v is None else str(v).strip()


def media_rows(ws):
    out = []
    for i, r in enumerate(ws.iter_rows(values_only=True), start=1):
        if i == 1 or not any(c not in (None, "") for c in r):
            continue
        try:
            int(s(r[0]))
        except ValueError:
            continue
        out.append(r)
    return out


def main(a):
    wb = openpyxl.load_workbook(a.workbook, read_only=True, data_only=True)
    rows = media_rows(wb["media"])
    thumbs_dir = os.path.join(a.v2, "Thumbnails")
    if a.apply:
        os.makedirs(a.out, exist_ok=True)

    copied = skipped = missing = 0
    tcopied = tmissing = 0
    gaps = []

    for r in rows:
        mid, title, murl, turl, _style, mtype = [s(x) for x in r[:6]]
        base = os.path.basename(murl)
        src = os.path.join(a.v2, base)
        dst = os.path.join(a.out, base)

        if not os.path.exists(src):
            missing += 1
            gaps.append((mid, base, mtype, "asset not in Vocabulary_v2"))
            continue
        if os.path.exists(dst) and os.path.getsize(dst) == os.path.getsize(src):
            skipped += 1
        elif a.apply:
            shutil.copy2(src, dst)
            copied += 1
        else:
            copied += 1

        if mtype == "video":
            tbase = os.path.basename(turl)
            tsrc = os.path.join(thumbs_dir, tbase)
            tdst = os.path.join(a.out, "Thumbnails", tbase)
            if not os.path.exists(tsrc):
                tmissing += 1
                gaps.append((mid, tbase, "thumbnail", "thumbnail not in Vocabulary_v2/Thumbnails"))
            elif a.apply:
                os.makedirs(os.path.dirname(tdst), exist_ok=True)
                shutil.copy2(tsrc, tdst)
                tcopied += 1
            else:
                tcopied += 1

    verb = "copied" if a.apply else "would copy"
    print(f"  assets     {verb}: {copied}   already there: {skipped}   MISSING: {missing}"
          f"   of {len(rows)} media rows")
    print(f"  thumbnails {verb}: {tcopied}   MISSING: {tmissing}")
    if not a.apply:
        print("  dry run — add --apply to copy")

    if a.gaps_csv and gaps:
        os.makedirs(os.path.dirname(a.gaps_csv) or ".", exist_ok=True)
        with open(a.gaps_csv, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["media_id", "filename", "kind", "reason"])
            w.writerows(gaps)
        print(f"  gaps: {len(gaps)} -> {a.gaps_csv}")
    return 1 if (missing or tmissing) else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--workbook", required=True)
    ap.add_argument("--v2", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--gaps-csv", default=None)
    sys.exit(main(ap.parse_args()))

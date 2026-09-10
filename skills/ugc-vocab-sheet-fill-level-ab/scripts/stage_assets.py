#!/usr/bin/env python3
"""
stage_assets.py — collect a part's assets into its own folder, renamed to the
workbook titles, videos compressed and stills converted to .webp.

  python3 stage_assets.py --workbook part2.xlsx \
                          --search "/Users/.../And Again" \
                          --out "/Users/.../Checked Videos/B-level 2.part"          # dry run
  ... --apply

For every row in the workbook's `media` sheet it finds the source file anywhere
under --search (matching the media title, then <word-slug>_video / _picture, then
the bare slug), and writes:

    <title>.mp4    video, H.264 CRF 28, 720p max, AAC 96k    (ffmpeg)
    <title>.webp   still, quality 82, longest edge 1080px      (cwebp)

Existing outputs are skipped, so a re-run only fills the gaps. Nothing in the
source folders is moved, renamed or deleted.

--unmatched-csv PATH writes every media row with no file in --out at the end
of the run (no source found, or the encoder failed) to a CSV with columns
media_id, expected_filename, media_type, word.

Needs ffmpeg (video) and cwebp (stills):  brew install ffmpeg webp

This ffmpeg has the webp muxer but no webp encoder, so stills go through
cwebp. There is deliberately no raw-copy fallback: a file written under the
wrong name or codec is worse than no file at all.
"""
import argparse, csv, os, re, subprocess, sys
from collections import defaultdict
import openpyxl

VIDEO_EXT = {".mp4", ".mov", ".m4v", ".webm"}
IMAGE_EXT = {".webp", ".png", ".jpg", ".jpeg"}

# Reject folders and committed part output are never a source for another part.
EXCLUDE_DIRS = {"Useless", "Wrong Voiceover", "_to_delete",
                "_old B-level 2.part", "_inbox"}


def s(v):
    return "" if v is None else str(v).strip()


def slug(w):
    return re.sub(r"[^a-z0-9]+", "_", s(w).lower()).strip("_")


def rows_of(ws, marker=None):
    out = []
    for i, r in enumerate(ws.iter_rows(values_only=True), start=1):
        if i == 1 or not any(c not in (None, "") for c in r):
            continue
        if marker is not None and len(r) > marker and s(r[marker]).lower() == "example":
            continue
        try:
            int(s(r[0]))
        except ValueError:
            continue
        out.append(r)
    return out


def index(search):
    idx = defaultdict(list)
    for root, dirs, files in os.walk(search):
        dirs[:] = [d for d in dirs if not d.startswith(".")
                   and d not in EXCLUDE_DIRS
                   and not d.endswith(".part")]
        for f in files:
            stem, ext = os.path.splitext(f)
            if ext.lower() in VIDEO_EXT | IMAGE_EXT:
                idx[stem.lower()].append(os.path.join(root, f))
    return idx


def pick(paths, want_video):
    exts = VIDEO_EXT if want_video else IMAGE_EXT
    hits = [p for p in paths if os.path.splitext(p)[1].lower() in exts]
    if not hits:
        return None
    # prefer a real source over a thumbnail
    hits.sort(key=lambda p: ("thumbnail" in p.lower(), len(p)))
    return hits[0]


MAX_IMAGE_EDGE = 1080
WEBP_QUALITY = 82


def image_size(path):
    try:
        from PIL import Image
        with Image.open(path) as im:
            return im.size
    except Exception:
        return None


def resize_args(src):
    """Cap the longest edge at MAX_IMAGE_EDGE, preserve aspect, never upscale.

    cwebp's -resize takes width height, where a 0 means "derive from the other
    side". Portrait caps the height, landscape caps the width.
    """
    size = image_size(src)
    if not size:
        return []
    w, h = size
    if max(w, h) <= MAX_IMAGE_EDGE:
        return []
    if h >= w:
        return ["-resize", "0", str(MAX_IMAGE_EDGE)]
    return ["-resize", str(MAX_IMAGE_EDGE), "0"]


def convert(src, dst, is_video, apply):
    if os.path.exists(dst):
        return "skip"
    if not apply:
        return "would"
    if is_video:
        cmd = ["ffmpeg", "-y", "-loglevel", "error", "-i", src,
               "-vf", "scale='min(720,iw)':-2", "-c:v", "libx264", "-crf", "28",
               "-preset", "medium", "-c:a", "aac", "-b:a", "96k", dst]
    else:
        cmd = ["cwebp", "-quiet", "-q", str(WEBP_QUALITY),
               *resize_args(src), src, "-o", dst]

    def drop_partial():
        if os.path.exists(dst):
            try:
                os.remove(dst)
            except OSError:
                pass

    try:
        subprocess.run(cmd, check=True)
    except FileNotFoundError:
        sys.exit("ffmpeg not found — install it with:  brew install ffmpeg"
                 if is_video else
                 "cwebp not found — install it with:  brew install webp")
    except subprocess.CalledProcessError as e:
        drop_partial()
        print(f"  FAILED {os.path.basename(src)} -> "
              f"{os.path.basename(dst)} (encoder exit {e.returncode})")
        return "failed"
    if not os.path.exists(dst) or os.path.getsize(dst) == 0:
        drop_partial()
        print(f"  FAILED {os.path.basename(src)} -> "
              f"{os.path.basename(dst)} (encoder wrote nothing)")
        return "failed"
    return "ok"


def main(a):
    wb = openpyxl.load_workbook(a.workbook, read_only=True, data_only=True)
    media = rows_of(wb["media"], 6)
    words = {s(r[0]): s(r[1]) for r in rows_of(wb["All Words"], 9)}
    idx = index(a.search)
    os.makedirs(a.out, exist_ok=True)

    done = missing = skipped = failed = 0
    unmatched = []
    for r in media:
        mid, title, mtype = s(r[0]), s(r[1]), s(r[5])
        is_video = mtype == "video"
        expected = title + (".mp4" if is_video else ".webp")
        word = words.get(mid, "")
        dst = os.path.join(a.out, expected)
        if os.path.exists(dst):
            # already staged by an earlier pass/run over a different --search
            # tree; this pass doesn't need to find its source to know that.
            skipped += 1
            continue
        src = None
        for key in (title.lower(), f"{slug(word)}_video",
                    f"{slug(word)}_picture", slug(word)):
            if key in idx:
                src = pick(idx[key], is_video)
                if src:
                    break
        if not src:
            missing += 1
            unmatched.append((mid, expected, mtype, word))
            if missing <= 10:
                print(f"  MISSING {title} ({mtype})")
            continue
        res = convert(src, dst, is_video, a.apply)
        if res == "skip":
            skipped += 1
        elif res == "failed":
            failed += 1
            unmatched.append((mid, expected, mtype, word))
        else:
            done += 1
            if done <= 3:
                print(f"  {res}: {os.path.basename(src)} -> {os.path.basename(dst)}")
            if a.apply and not os.path.exists(dst):
                unmatched.append((mid, expected, mtype, word))

    print(f"\n{'written' if a.apply else 'would write'}: {done}   "
          f"already there: {skipped}   failed: {failed}   "
          f"missing: {missing}   of {len(media)} media rows")
    if not a.apply:
        print("dry run — add --apply to convert")

    if a.unmatched_csv:
        os.makedirs(os.path.dirname(a.unmatched_csv) or ".", exist_ok=True)
        with open(a.unmatched_csv, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["media_id", "expected_filename", "media_type", "word"])
            w.writerows(unmatched)
        print(f"unmatched: {len(unmatched)} rows -> {a.unmatched_csv}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--workbook", required=True)
    ap.add_argument("--search", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--unmatched-csv", default=None,
                     help="write still-unmatched media rows to this CSV path")
    main(ap.parse_args())

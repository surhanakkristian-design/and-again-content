#!/usr/bin/env python3
"""
upload_assets.py — upload a part's assets to Supabase Storage and verify every URL.

  export SUPABASE_URL="https://<ref>.supabase.co"
  export SUPABASE_KEY="<service_role key>"          # never commit this, never paste it in a prompt
  python3 upload_assets.py --workbook part.xlsx --assets "…/B-level 1.part"        # dry run
  ... --apply

For every row in the `media` sheet it uploads the local file to the bucket named in
`media_url` (Words for the asset, Thumbnails for the still), then re-checks the public
URL with a HEAD request. A row whose URL does not answer 200 is reported and must be
fixed before the database import — a dead link in `media_url` is invisible until a
learner hits it.

Videos also need a thumbnail. Thumbnails live in `<assets>/Thumbnails/`, matching the
`Thumbnails` bucket in `thumbnail_url`; the asset itself lives at the assets-folder
root. A thumbnail that is not there is reported and its row is skipped — the script
never fabricates one, because a generated thumbnail is indistinguishable from a real
one after the fact.
"""
import argparse, os, re, sys, time, urllib.error, urllib.request
import openpyxl

MIME = {".mp4": "video/mp4", ".webp": "image/webp", ".png": "image/png",
        ".jpg": "image/jpeg", ".jpeg": "image/jpeg"}


def s(v):
    return "" if v is None else str(v).strip()


def rows_of(ws):
    out = []
    for i, r in enumerate(ws.iter_rows(values_only=True), start=1):
        if i == 1 or not any(c not in (None, "") for c in r):
            continue
        if any(s(v).lower() == "example" for v in r):
            continue
        try:
            int(s(r[0]))
        except ValueError:
            continue
        out.append(r)
    return out


def bucket_and_name(url):
    m = re.search(r"/object/public/([^/]+)/(.+)$", url)
    return (m.group(1), m.group(2)) if m else (None, None)


def head_ok(url, tries=3):
    """A free-tier project rate-limits bursts of HEAD requests, so one non-200
    means nothing — ask again before calling a URL dead."""
    for attempt in range(tries):
        req = urllib.request.Request(url, method="HEAD")
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                if r.status == 200:
                    return True
        except urllib.error.HTTPError as e:
            if e.code == 200:
                return True
            if e.code == 404:
                return False
        except Exception:
            pass
        time.sleep(1.5 * (attempt + 1))
    return False

def put(base, key, bucket, name, path, apply, tries=4):
    """One file, one request, retried with backoff.

    Uploads are deliberately sequential and never batched: on a free Supabase
    project two concurrent video uploads is enough to start failing."""
    if not apply:
        return "would"
    ext = os.path.splitext(path)[1].lower()
    with open(path, "rb") as fh:
        data = fh.read()
    url = f"{base}/storage/v1/object/{bucket}/{urllib.request.quote(name)}"
    last = ""
    for attempt in range(1, tries + 1):
        req = urllib.request.Request(url, data=data, method="POST", headers={
            "Authorization": f"Bearer {key}", "apikey": key,
            "Content-Type": MIME.get(ext, "application/octet-stream"),
            "x-upsert": "true"})
        try:
            with urllib.request.urlopen(req, timeout=600) as r:
                return "ok" if r.status in (200, 201) else f"HTTP {r.status}"
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code}: {e.read()[:120].decode('utf-8', 'replace')}"
            if e.code in (400, 401, 403, 404):      # not worth retrying
                return last
        except Exception as e:
            last = str(e)[:120]
        if attempt < tries:
            wait = 3 * 2 ** (attempt - 1)           # 3s, 6s, 12s
            print(f"      retry {attempt}/{tries - 1} in {wait}s — {last}")
            time.sleep(wait)
    return last or "failed"


def main(a):
    base = os.environ.get("SUPABASE_URL", "").rstrip("/")
    key = os.environ.get("SUPABASE_KEY", "")
    if a.apply and not (base and key):
        sys.exit("set SUPABASE_URL and SUPABASE_KEY in the environment first")

    wb = openpyxl.load_workbook(a.workbook, read_only=True, data_only=True)
    media = rows_of(wb["media"])
    wb.close()

    if a.apply:                       # fail fast: a missing bucket wastes the whole run
        buckets = {bucket_and_name(s(r[c]))[0] for r in media for c in (2, 3)} - {None}
        req = urllib.request.Request(f"{base}/storage/v1/bucket",
                                     headers={"Authorization": f"Bearer {key}",
                                              "apikey": key})
        try:
            import json as _json
            have = {b["name"] for b in _json.load(urllib.request.urlopen(req, timeout=30))}
        except Exception as e:
            sys.exit(f"could not list storage buckets: {e}")
        missing_buckets = buckets - have
        if missing_buckets:
            sys.exit(f"bucket(s) {sorted(missing_buckets)} do not exist in this project "
                     f"(it has: {sorted(have)}).\nCreate them in Storage as PUBLIC buckets, "
                     f"then re-run.")

    up = miss = bad = skip = 0
    total = len(media) * 2
    n = 0
    for r in media:
        title, mtype = s(r[1]), s(r[5])
        for col, is_thumb in ((2, False), (3, True)):   # media_url, thumbnail_url
            url = s(r[col])
            bucket, name = bucket_and_name(url)
            if not bucket:
                print(f"  BAD URL  {title}: {url}")
                bad += 1
                continue
            # `Thumbnails` is a bucket, and a subfolder of the part folder; the
            # asset for a still or a video sits at the assets-folder root.
            local = (os.path.join(a.assets, "Thumbnails", name)
                     if bucket == "Thumbnails" else os.path.join(a.assets, name))
            if not os.path.exists(local):
                print(f"  MISSING THUMBNAIL — SKIPPED  {bucket}/{name}"
                      if is_thumb else f"  MISSING  {bucket}/{name}")
                print(f"      expected at: {local}")
                miss += 1
                continue
            n += 1
            is_video = local.lower().endswith(".mp4")
            if a.apply and a.skip_existing and head_ok(url):
                skip += 1
                continue
            size = os.path.getsize(local) / 1e6
            print(f"  [{n:>3}/{total}] {name} ({size:.1f} MB) …", end=" ", flush=True)
            res = put(base, key, bucket, name, local, a.apply)
            print(res)
            if res not in ("ok", "would"):
                bad += 1
            else:
                up += 1
            if a.apply and is_video and a.delay:
                time.sleep(a.delay)      # be gentle with a free-tier project

    print(f"\n{'uploaded' if a.apply else 'would upload'} {up}, already there {skip}, "
          f"missing {miss}, failed {bad}")
    if bad:
        print("re-run the same command — files already in storage are skipped")

    if a.apply and a.verify:
        print("\nverifying public URLs …")
        dead = []
        for i, r in enumerate(media, 1):
            if not head_ok(s(r[2])) or not head_ok(s(r[3])):
                dead.append(s(r[1]))
            if i % 50 == 0:
                print(f"    checked {i}/{len(media)}", flush=True)
                time.sleep(1)
        print(f"  {len(media) - len(dead)} media ok, {len(dead)} with a dead URL")
        for t in dead[:15]:
            print(f"    dead: {t}")
        if dead:
            sys.exit("dead URLs — do not import the database yet")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--workbook", required=True)
    ap.add_argument("--assets", required=True)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--verify", action="store_true", default=True)
    ap.add_argument("--delay", type=float, default=1.0,
                    help="seconds to pause after each video upload (free tier: keep it)")
    ap.add_argument("--no-skip-existing", dest="skip_existing", action="store_false",
                    default=True, help="re-upload even files already present in storage")
    main(ap.parse_args())

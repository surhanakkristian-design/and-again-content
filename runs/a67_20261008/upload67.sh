#!/bin/bash
# A67: uploads the re-encoded lab pictures of 900001 / 900002 (webp q72, 1080 px) as NEW objects Thumbnails/lab/a67/*.webp
# (nothing overwritten), then reads every object back (HTTP 200 + same byte count). Pattern of upload60.sh.
set -uo pipefail
R=~/Projects/and-again-content/runs/a67_20261008
source ~/Projects/and-again/supabase/scripts/_sb.sh
cd ~/Projects/and-again-a67  # the linked project (supabase/.temp/project-ref)
PUB="https://abyrutykpvmzkfbesire.supabase.co/storage/v1/object/public"
mkdir -p "$R/upload"; : > "$R/upload/upload.log"; bad=0
put() { local f="$1" bucket="$2" obj="$3" type="$4"; local size; size=$(stat -f %z "$f")
  local got; got=$(curl -s -o /dev/null -w '%{http_code} %{size_download}' --max-time 30 "$PUB/$bucket/$obj")
  if [ "$got" = "200 $size" ]; then echo "there $bucket/$obj" >> "$R/upload/upload.log"; return; fi
  [ "${got%% *}" = "200" ] && { echo "EXISTS-DIFFERENT $bucket/$obj ($got) - not overwritten" >> "$R/upload/upload.log"; bad=$((bad+1)); return; }
  local ok=0
  for try in 1 2 3 4 5; do
    if "$SB" storage cp "$f" "ss:///$bucket/$obj" --linked --experimental --cache-control "public, max-age=31536000, immutable" --content-type "$type" >> "$R/upload/upload.log" 2>&1; then
      got=$(curl -s -o /dev/null -w '%{http_code} %{size_download}' --max-time 30 "$PUB/$bucket/$obj")
      [ "$got" = "200 $size" ] && { ok=1; break; }
    fi
    sleep 2
  done
  [ $ok = 1 ] && echo "up $bucket/$obj" >> "$R/upload/upload.log" || { echo "FAILED $bucket/$obj ($got)" >> "$R/upload/upload.log"; bad=$((bad+1)); }
}
for f in "$R"/pics/new/*.webp; do put "$f" Thumbnails "lab/a67/$(basename "$f")" image/webp; done
echo "failed: $bad"; grep -c '^up\|^there' "$R/upload/upload.log"

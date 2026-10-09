#!/bin/bash
# A71 (from upload69): uploads the new recordings (audio/tts/<id>/a71_*.m4a)
# one file at a time with retries, then reads every object back (HTTP 200 + same bytes).
set -uo pipefail
R=~/Projects/and-again-content/runs/a71_20261009
source ~/Projects/and-again/supabase/scripts/_sb.sh
cd ~/Projects/and-again  # the linked project
PUB="https://abyrutykpvmzkfbesire.supabase.co/storage/v1/object/public"
mkdir -p "$R/upload"; : > "$R/upload/upload.log"; bad=0
put() { local f="$1" bucket="$2" obj="$3" type="$4"; local size; size=$(stat -f %z "$f")
  local got; got=$(curl -s -o /dev/null -w '%{http_code} %{size_download}' --max-time 30 "$PUB/$bucket/$obj")
  if [ "$got" = "200 $size" ]; then echo "there $bucket/$obj" >> "$R/upload/upload.log"; return; fi
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
for f in "$R"/audio/tts/*/a71_*.m4a; do put "$f" audio "sets/$(basename "$(dirname "$f")")/$(basename "$f")" audio/mp4; done
echo "failed: $bad"; grep -c '^up\|^there' "$R/upload/upload.log"

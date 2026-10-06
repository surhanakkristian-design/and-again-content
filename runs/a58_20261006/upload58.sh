#!/bin/bash
# A58: uploads the recordings (bucket audio, sets/<id>/a58_*.m4a; new object names only) one file at a time with
# retries, then reads every object back (HTTP 200 + same byte count). Log: upload/upload.log
set -uo pipefail
R=~/Projects/and-again-content/runs/a58_20261006
source ~/Projects/and-again/supabase/scripts/_sb.sh
cd ~/Projects/and-again-a58  # the linked project (supabase/.temp/project-ref)
BASE="https://abyrutykpvmzkfbesire.supabase.co/storage/v1/object/public/audio"
mkdir -p "$R/upload"; : > "$R/upload/upload.log"; bad=0
for f in "$R"/audio/*/a58_*.m4a; do
  id=$(basename "$(dirname "$f")"); name=$(basename "$f"); obj="sets/$id/$name"
  size=$(stat -f %z "$f")
  got=$(curl -s -o /dev/null -w '%{http_code} %{size_download}' --max-time 30 "$BASE/$obj")
  if [ "$got" = "200 $size" ]; then echo "there $obj" >> "$R/upload/upload.log"; continue; fi
  ok=0
  for try in 1 2 3 4 5; do
    if "$SB" storage cp "$f" "ss:///audio/$obj" --linked --experimental --cache-control "public, max-age=31536000, immutable" --content-type audio/mp4 >> "$R/upload/upload.log" 2>&1; then
      got=$(curl -s -o /dev/null -w '%{http_code} %{size_download}' --max-time 30 "$BASE/$obj")
      [ "$got" = "200 $size" ] && { ok=1; break; }
    fi
    sleep 2
  done
  [ $ok = 1 ] && echo "up $obj" >> "$R/upload/upload.log" || { echo "FAILED $obj ($got)" >> "$R/upload/upload.log"; bad=$((bad+1)); }
done
echo "failed: $bad"; grep -c '^up\|^there' "$R/upload/upload.log"

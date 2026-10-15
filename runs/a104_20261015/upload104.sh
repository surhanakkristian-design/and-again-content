#!/bin/bash
# A104 (from upload90.sh): uploads the re-recorded Ex5 story audio named in audio/voices104_<id>.json (the question recordings are unchanged), read back (sha256)
set -uo pipefail
R=~/Projects/and-again-content/runs/a104_20261015
source ~/Projects/and-again/supabase/scripts/_sb.sh
cd ~/Projects/and-again
PUB="https://abyrutykpvmzkfbesire.supabase.co/storage/v1/object/public"
bad=0
put() { local f="$1" obj="$2" type="$3"; local a g ok=0; a=$(shasum -a 256 "$f" | cut -d' ' -f1)
  g=$(curl -s --max-time 30 "$PUB/$obj" | shasum -a 256 | cut -d' ' -f1); [ "$a" = "$g" ] && { echo "there $obj"; return; }
  for try in 1 2 3 4 5; do
    "$SB" storage cp "$f" "ss:///$obj" --linked --experimental --cache-control "public, max-age=31536000, immutable" --content-type "$type" >> "$R/upload104.log" 2>&1
    g=$(curl -s --max-time 30 "$PUB/$obj" | shasum -a 256 | cut -d' ' -f1); [ "$a" = "$g" ] && { ok=1; break; }; sleep 3
  done
  [ $ok = 1 ] && echo "up $obj" || { echo "FAILED $obj"; bad=$((bad+1)); }
}
for id in 4884 399 5335; do
  for fn in $(python3 -c "import json;d=json.load(open('$R/audio/voices104_$id.json'));print(d['guided']['audio'].split('/')[-1])"); do
    put "$R/audio/tts/$id/$fn" "audio/sets/$id/$fn" audio/mp4
  done
done
echo "failed: $bad"

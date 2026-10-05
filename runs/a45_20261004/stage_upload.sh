#!/bin/bash
# A45: uploads the audio files of the given media ids to the public bucket `audio` under sets/<id>/ (new object names only).
#   bash stage_upload.sh <batch-name> <id> [<id> ...]
set -euo pipefail
R=~/Projects/and-again-content/runs/a45_20261004
B="$1"; shift
S="$R/upload/$B/audio/sets"; rm -rf "$R/upload/$B"; mkdir -p "$S"
for id in "$@"; do mkdir -p "$S/$id"; cp "$R/audio/$id/"*.m4a "$S/$id/"; done
cd ~/Projects/and-again && source supabase/scripts/_sb.sh
n=$(find "$S" -name '*.m4a' | wc -l | tr -d ' ')
echo "uploading $n files"
"$SB" storage cp -r "$R/upload/$B/audio" ss:/// --linked --experimental -j 8 --cache-control "public, max-age=31536000, immutable" --content-type audio/mp4 2>&1 | grep -v "new version\|recommend updating" | tail -3
echo "uploaded batch $B"

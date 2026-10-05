#!/bin/bash
# A48: uploads the accepted carousel pictures (bucket Thumbnails, lab/carousel/) and the A48 recordings (bucket audio,
# sets/<id>/a48_*.m4a) under NEW object names only (each name carries a content hash; nothing existing is replaced),
# then reads every object back (HTTP 200 + size). Run from anywhere.
set -euo pipefail
R="$(cd "$(dirname "$0")" && pwd)"
cd ~/Projects/and-again && source supabase/scripts/_sb.sh
BASE="https://abyrutykpvmzkfbesire.supabase.co/storage/v1/object/public"
S="$R/upload/stage"; rm -rf "$S"; mkdir -p "$S/Thumbnails/lab/carousel" "$S/audio/sets"
python3 - "$R" "$S" <<'PY'
import json, sys, shutil, os
R, S = sys.argv[1:]
ex = json.load(open(os.path.expanduser('~/Projects/and-again-a48/lib/labExtras.json')))
urls = set()
for v in ex.values():
    if v['carousel']:
        for x in v['carousel']['row'] + v['carousel']['column']:
            urls.add(x['url']); x.get('voice') and urls.add(x['voice'])
    if v.get('answerVoice'): urls.add(v['answerVoice'])
for m in json.load(open(f'{R}/audio/manifest.json')): urls.add('https://x/object/public/audio/' + m['object'])
n = 0
for u in sorted(urls):
    if '/Thumbnails/lab/carousel/' in u:
        f = u.split('/carousel/')[1]; shutil.copy(f'{R}/upload/Thumbnails/lab/carousel/{f}', f'{S}/Thumbnails/lab/carousel/{f}')
    else:
        o = u.split('/audio/')[1]; os.makedirs(os.path.dirname(f'{S}/audio/{o}'), exist_ok=True); shutil.copy(f'{R}/audio/{o[len("sets/"):]}', f'{S}/audio/{o}')
    n += 1
print(n, 'files staged')
PY
# none of these names may exist already (new object names only)
exist=0; for f in $(cd "$S" && find . -type f | sed 's|^\./||'); do c=$(curl -s -o /dev/null -w '%{http_code}' --max-time 20 "$BASE/$f"); [ "$c" = "200" ] && { echo "exists already: $f"; exist=$((exist+1)); }; done
[ "$exist" = "0" ] || { echo "$exist objects exist already; nothing uploaded" >&2; exit 1; }
"$SB" storage cp -r "$S/Thumbnails" ss:/// --linked --experimental -j 4 --cache-control "public, max-age=31536000, immutable" --content-type image/webp
"$SB" storage cp -r "$S/audio" ss:/// --linked --experimental -j 4 --cache-control "public, max-age=31536000, immutable" --content-type audio/mp4
ok=0; bad=0; for f in $(cd "$S" && find . -type f | sed 's|^\./||'); do
  got=$(curl -s --max-time 30 "$BASE/$f" | wc -c | tr -d ' '); want=$(wc -c < "$S/$f" | tr -d ' ')
  if [ "$got" = "$want" ]; then ok=$((ok+1)); else bad=$((bad+1)); echo "BAD $f $got/$want"; fi
done
echo "read back: $ok ok, $bad bad"

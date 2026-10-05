#!/bin/bash
# A51: uploads the A51 objects the lab file uses (carousel WebPs *_a51.webp, recordings sets/<id>/a51_*.m4a) under NEW
# names only (content hash in the name; nothing existing is replaced), then reads every lab picture/voice URL back.
set -euo pipefail
R="$(cd "$(dirname "$0")" && pwd)"; APP=~/Projects/and-again-a51
cd ~/Projects/and-again && source supabase/scripts/_sb.sh
BASE="https://abyrutykpvmzkfbesire.supabase.co/storage/v1/object/public"
S="$R/upload/stage"; rm -rf "$S"; mkdir -p "$S/Thumbnails/lab/carousel" "$S/audio/sets"
python3 - "$R" "$S" "$APP" <<'PY'
import json, sys, shutil, os
R, S, APP = sys.argv[1:]
ex = json.load(open(f'{APP}/lib/labExtras.json')); n = 0
for v in ex.values():
    for x in (v['carousel'] or {}).get('pictures', []):
        for u in (x['url'], x.get('voice') or ''):
            if u.endswith('_a51.webp'):
                f = u.split('/carousel/')[1]; shutil.copy(f'{R}/upload/carousel/Thumbnails/lab/carousel/{f}', f'{S}/Thumbnails/lab/carousel/{f}'); n += 1
            elif '/audio/sets/' in u and '/a51_' in u:
                o = u.split('/public/audio/')[1]; os.makedirs(os.path.dirname(f'{S}/audio/{o}'), exist_ok=True)
                shutil.copy(f'{R}/audio/{o[len("sets/"):]}', f'{S}/audio/{o}'); n += 1
print(n, 'files staged')
PY
todo=0; for f in $(cd "$S" && find . -type f | sed 's|^\./||'); do
  c=$(curl -s -o /dev/null -w '%{http_code}' --max-time 20 "$BASE/$f")
  if [ "$c" = "200" ]; then rm "$S/$f"; else todo=$((todo+1)); fi   # already uploaded by an earlier run: same name = same content
done
echo "$todo new objects"
if [ "$todo" -gt 0 ]; then
  [ -n "$(find "$S/Thumbnails" -type f)" ] && "$SB" storage cp -r "$S/Thumbnails" ss:/// --linked --experimental -j 4 --cache-control "public, max-age=31536000, immutable" --content-type image/webp
  [ -n "$(find "$S/audio" -type f)" ] && "$SB" storage cp -r "$S/audio" ss:/// --linked --experimental -j 4 --cache-control "public, max-age=31536000, immutable" --content-type audio/mp4
fi
python3 - "$APP" <<'PY'
import json, sys, urllib.request
ex = json.load(open(f'{sys.argv[1]}/lib/labExtras.json')); ok = bad = 0
for v in ex.values():
    for x in (v['carousel'] or {}).get('pictures', []):
        for u in (x['url'], x['voice']):
            try: r = urllib.request.urlopen(urllib.request.Request(u, method='HEAD'), timeout=30); good = r.status == 200 and int(r.headers.get('content-length') or 0) > 500
            except Exception: good = False
            ok += good; bad += not good; good or print('BAD', u)
print(f'read back: {ok} ok, {bad} bad')
PY

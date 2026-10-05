#!/bin/bash
# Owner: apply A45 to the live project.
#   bash ~/Projects/and-again-content/runs/a45_20261004/apply_a45.sh              the migration (if missing) + every batch not applied yet
#   bash ~/Projects/and-again-content/runs/a45_20261004/apply_a45.sh <batch>      the migration (if missing) + this batch only
#   bash ~/Projects/and-again-content/runs/a45_20261004/apply_a45.sh --check      only check the files; no database or storage call
# Per batch: 1. its files are checked (SQL complete, every audio file there), 2. audio files that are not in storage yet are
# uploaded (bucket `audio`, sets/<media id>/, new object names only), 3. every object is read back (HTTP 200),
# 4. the before-state is saved (backup/<batch>_before.json), 5. the guarded write (one transaction per SQL file; it writes
# nothing when a row exists already). A batch that is already in the database is skipped. Safe to run again.
# Rollback (not run): out/<batch>_rollback.sql, out/a45_migration_rollback.sql.
set -euo pipefail
R=~/Projects/and-again-content/runs/a45_20261004
APP=~/Projects/and-again-a45
[ -d "$APP/supabase/migrations" ] || APP=~/Projects/and-again
MIG="$R/out/a45_migration.sql"
SB_SH=~/Projects/and-again/supabase/scripts/_sb.sh
BASE="https://abyrutykpvmzkfbesire.supabase.co/storage/v1/object/public/audio"
CHECK=0; ONLY=""
case "${1:-}" in --check) CHECK=1 ;; "") ;; *) ONLY="$1" ;; esac
for f in "$SB_SH" "$MIG" "$R/out/a45_migration_rollback.sql"; do [ -s "$f" ] || { echo "missing or empty: $f; nothing was sent" >&2; exit 1; }; done
grep -q "create table if not exists public.media_exercise_sets" "$MIG" || { echo "stopped: $MIG is not the A45 migration" >&2; exit 1; }
[ "$(head -4 "$MIG" | grep -c '^begin;$')" = 1 ] && [ "$(tail -1 "$MIG")" = "commit;" ] || { echo "stopped: $MIG is not one transaction" >&2; exit 1; }
if [ -n "$ONLY" ]; then BATCHES="$R/batches/$ONLY.json"; [ -s "$BATCHES" ] || { echo "no such batch: $ONLY" >&2; exit 1; }; else BATCHES=$(ls "$R"/batches/*.json | sort); fi
# 1. file checks of every batch, before anything is sent
for b in $BATCHES; do
  python3 - "$R" "$b" <<'PY'
import json, os, sys
R, b = sys.argv[1], json.load(open(sys.argv[2])); bad = []
for f in b['sql'] + [b['rollback']]:
    p = f'{R}/{f}'
    if not os.path.exists(p) or os.path.getsize(p) < 50: bad.append(f'missing or empty: {f}'); continue
    s = open(p).read()
    if '\nbegin;\n' not in '\n' + s or not s.rstrip().endswith('commit;'): bad.append(f'not one complete transaction: {f}')
    if os.path.getsize(p) > 1_500_000: bad.append(f'too large for one call: {f}')
for o in b['objects']:
    p = f"{R}/audio/{o[len('sets/'):]}"
    if not os.path.exists(p) or os.path.getsize(p) < 1500: bad.append(f'audio file missing or empty: {o}')
if bad: print(f"batch {b['batch']}: " + '; '.join(bad[:10]), file=sys.stderr); sys.exit(1)
print(f"batch {b['batch']}: files ok ({len(b['ids'])} videos, {len(b['sql'])} SQL files, {len(b['objects'])} audio files)")
PY
done
[ "$CHECK" = 1 ] && { echo "check only: nothing was sent"; exit 0; }
cd ~/Projects/and-again && source "$SB_SH"
q() { "$SB" db query --linked "$@" 2>&1 | grep -v 'new version\|recommend updating' || true; }
# the migration, once
if [ "$(sb_scalar "select count(*) from information_schema.tables where table_schema='public' and table_name='media_exercise_sets'")" = "0" ]; then
  "$SB" db query --linked --file "$MIG" >/dev/null
  "$SB" migration repair --linked --status applied 20261004230000 >/dev/null 2>&1 || echo "note: migration 20261004230000 not recorded (run: supabase migration repair --linked --status applied 20261004230000)"
  echo "migration applied (table media_exercise_sets; bucket audio also takes audio/mp4)"
else echo "migration: table is there already"; fi
mkdir -p "$R/backup" "$R/applied"
for b in $BATCHES; do
  name=$(basename "$b" .json)
  ids=$(python3 -c "import json,sys; print(','.join(str(i) for i in json.load(open(sys.argv[1]))['ids']))" "$b")
  n=$(python3 -c "import json,sys; print(len(json.load(open(sys.argv[1]))['ids']))" "$b")
  have=$(sb_scalar "select count(*) from public.media_exercise_sets where media_id in ($ids)")
  if [ "$have" = "$n" ]; then echo "batch $name: already in the database ($n rows), skipped"; touch "$R/applied/$name"; continue; fi
  if [ "$have" != "0" ]; then echo "batch $name: $have of $n rows exist already - not touched, look at it" >&2; continue; fi
  # audio: upload what storage does not have yet
  S="$R/upload/$name"; rm -rf "$S"; up=0
  for o in $(python3 -c "import json,sys; print('\n'.join(json.load(open(sys.argv[1]))['objects']))" "$b"); do
    code=$(curl -s -o /dev/null -w '%{http_code}' --max-time 30 -r 0-0 "$BASE/$o" || echo 000)
    if [ "$code" != "200" ] && [ "$code" != "206" ]; then mkdir -p "$S/audio/$(dirname "$o")"; cp "$R/audio/${o#sets/}" "$S/audio/$o"; up=$((up+1)); fi
  done
  if [ "$up" -gt 0 ]; then
    "$SB" storage cp -r "$S/audio" ss:/// --linked --experimental -j 8 --cache-control "public, max-age=31536000, immutable" --content-type audio/mp4 > "$R/upload/$name.log" 2>&1 || { echo "batch $name: upload failed, see upload/$name.log; nothing written to the database" >&2; tail -2 "$R/upload/$name.log" >&2; continue; }
  fi
  miss=0
  for o in $(python3 -c "import json,sys; print('\n'.join(json.load(open(sys.argv[1]))['objects']))" "$b"); do
    code=$(curl -s -o /dev/null -w '%{http_code}' --max-time 30 -r 0-0 "$BASE/$o" || echo 000)
    [ "$code" = "200" ] || [ "$code" = "206" ] || miss=$((miss+1))
  done
  [ "$miss" = "0" ] || { echo "batch $name: $miss audio objects not readable after the upload; nothing written to the database" >&2; continue; }
  echo "batch $name: audio in storage ($up uploaded now)"
  sb_rows "select * from public.media_exercise_sets where media_id in ($ids)" > "$R/backup/${name}_before.json"
  for f in $(python3 -c "import json,sys; print('\n'.join(json.load(open(sys.argv[1]))['sql']))" "$b"); do "$SB" db query --linked --file "$R/$f" >/dev/null; done
  now=$(sb_scalar "select count(*) from public.media_exercise_sets where media_id in ($ids)")
  echo "batch $name: $now of $n rows written"; [ "$now" = "$n" ] && touch "$R/applied/$name"
done
q "select level, count(*) as videos from public.media_exercise_sets where status = 'live' group by 1 order by 1"

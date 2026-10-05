#!/bin/bash
# Owner: apply A45 to the live project.
#   bash ~/Projects/and-again-content/runs/a45_20261004/apply_a45.sh              the migration (if missing) + every batch not applied yet
#   bash ~/Projects/and-again-content/runs/a45_20261004/apply_a45.sh <batch>      the migration (if missing) + this batch only
#   bash ~/Projects/and-again-content/runs/a45_20261004/apply_a45.sh --check      only check the files; no database or storage call
# Per batch: 1. its files are checked (SQL complete, every audio file there), 2. audio files that are not in storage yet are
# uploaded (bucket `audio`, sets/<media id>/, new object names only), 3. every object is read back (HTTP 200),
# 4. the before-state is saved (backup/<batch>_before.json), 5. the guarded write (one transaction per SQL file; it writes
# nothing when a row exists already). A batch that is already in the database is skipped. Safe to run again.
# Network errors: missing audio files are uploaded again (up to 5 rounds, A45_UPLOAD_TRIES, with pauses), SQL files
# are sent again up to 3 times; a batch whose audio does not all read back is left out (rows not written).
# Picture shape (5 Oct): migration 20261005100000 adds width / height (if missing); every batch then gets its guarded
# shape update (out/<batch>_shape.sql, touches only rows without a shape), also batches written earlier.
# Rollback (not run): out/<batch>_rollback.sql, out/a45_migration_rollback.sql, out/a45_shape_migration_rollback.sql.
set -euo pipefail
R=~/Projects/and-again-content/runs/a45_20261004
APP=~/Projects/and-again-a45
[ -d "$APP/supabase/migrations" ] || APP=~/Projects/and-again
MIG="$R/out/a45_migration.sql"
MIG2="$R/out/a45_shape_migration.sql"
SB_SH=~/Projects/and-again/supabase/scripts/_sb.sh
BASE="https://abyrutykpvmzkfbesire.supabase.co/storage/v1/object/public/audio"
CHECK=0; ONLY=""; TRIES=${A45_UPLOAD_TRIES:-5}
case "${1:-}" in --check) CHECK=1 ;; "") ;; *) ONLY="$1" ;; esac
for f in "$SB_SH" "$MIG" "$R/out/a45_migration_rollback.sql" "$MIG2" "$R/out/a45_shape_migration_rollback.sql"; do [ -s "$f" ] || { echo "missing or empty: $f; nothing was sent" >&2; exit 1; }; done
grep -q "add column if not exists width" "$MIG2" || { echo "stopped: $MIG2 is not the A45 shape migration" >&2; exit 1; }
grep -q "create table if not exists public.media_exercise_sets" "$MIG" || { echo "stopped: $MIG is not the A45 migration" >&2; exit 1; }
[ "$(head -4 "$MIG" | grep -c '^begin;$')" = 1 ] && [ "$(tail -1 "$MIG")" = "commit;" ] || { echo "stopped: $MIG is not one transaction" >&2; exit 1; }
if [ -n "$ONLY" ]; then BATCHES="$R/batches/$ONLY.json"; [ -s "$BATCHES" ] || { echo "no such batch: $ONLY" >&2; exit 1; }; else BATCHES=$(ls "$R"/batches/*.json | sort); fi
# 1. file checks of every batch, before anything is sent
for b in $BATCHES; do
  python3 - "$R" "$b" <<'PY'
import json, os, sys
R, b = sys.argv[1], json.load(open(sys.argv[2])); bad = []
if 'shape' not in b: bad.append('no shape file (run: python3 shape.py ' + b['batch'] + ')')
for f in b['sql'] + [b['rollback']] + ([b['shape']] if 'shape' in b else []):
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
# readable <object>: HTTP 200/206 on the public URL; a network error counts as not readable after 3 tries
readable() { local c i; for i in 1 2 3; do c=$(curl -s -o /dev/null -w '%{http_code}' --max-time 30 -r 0-0 "$BASE/$1" || echo 000)
  case "$c" in 200|206) return 0 ;; 400|404) return 1 ;; esac; sleep 3; done; return 1; }
# scalar <sql>: sb_scalar with 3 tries (a network error waits 20 s)
scalar() { local v t; for t in 1 2 3; do v=$(sb_scalar "$1") && { echo "$v"; return 0; }; sleep 20; done; echo "query failed 3 times: $1" >&2; return 1; }
q() { "$SB" db query --linked "$@" 2>&1 | grep -v 'new version\|recommend updating' || true; }
# the migration, once
if [ "$(sb_scalar "select count(*) from information_schema.tables where table_schema='public' and table_name='media_exercise_sets'")" = "0" ]; then
  "$SB" db query --linked --file "$MIG" >/dev/null
  "$SB" migration repair --linked --status applied 20261004230000 >/dev/null 2>&1 || echo "note: migration 20261004230000 not recorded (run: supabase migration repair --linked --status applied 20261004230000)"
  echo "migration applied (table media_exercise_sets; bucket audio also takes audio/mp4)"
else echo "migration: table is there already"; fi
if [ "$(scalar "select count(*) from information_schema.columns where table_schema='public' and table_name='media_exercise_sets' and column_name in ('width','height')")" != "2" ]; then
  "$SB" db query --linked --file "$MIG2" >/dev/null
  "$SB" migration repair --linked --status applied 20261005100000 >/dev/null 2>&1 || echo "note: migration 20261005100000 not recorded (run from ~/Projects/and-again: supabase migration repair --linked --status applied 20261005100000)"
  echo "shape migration applied (columns width, height)"
else echo "shape migration: columns are there already"; fi
# shape_of <batch json> <name> <ids>: the guarded shape update when a row of the batch has no shape yet (3 tries)
shape_of() { local f t; f=$(python3 -c "import json,sys; print(json.load(open(sys.argv[1])).get('shape',''))" "$1")
  [ -n "$f" ] || { echo "batch $2: no shape file" >&2; return 0; }
  [ "$(scalar "select count(*) from public.media_exercise_sets where media_id in ($3) and width is null")" = "0" ] && return 0
  for t in 1 2 3; do "$SB" db query --linked --file "$R/$f" > "$R/upload/$2.shape.log" 2>&1 && { echo "batch $2: picture shape written"; return 0; }; sleep $((t*20)); done
  echo "batch $2: picture shape NOT written ($(grep -v 'new version\|recommend updating' "$R/upload/$2.shape.log" | tail -1 | cut -c1-120))" >&2; }
mkdir -p "$R/backup" "$R/applied"
for b in $BATCHES; do
  name=$(basename "$b" .json)
  ids=$(python3 -c "import json,sys; print(','.join(str(i) for i in json.load(open(sys.argv[1]))['ids']))" "$b")
  n=$(python3 -c "import json,sys; print(len(json.load(open(sys.argv[1]))['ids']))" "$b")
  have=$(scalar "select count(*) from public.media_exercise_sets where media_id in ($ids)")
  if [ "$have" = "$n" ]; then echo "batch $name: already in the database ($n rows), skipped"; touch "$R/applied/$name"; shape_of "$b" "$name" "$ids"; continue; fi
  if [ "$have" != "0" ]; then echo "batch $name: $have of $n rows exist already - not touched, look at it" >&2; continue; fi
  # audio: upload what storage does not have yet; on a network error (504, transport error) wait and upload
  # the still-missing files again, up to $TRIES rounds. The rows are written only when every object reads back.
  objs=$(python3 -c "import json,sys; print('\n'.join(json.load(open(sys.argv[1]))['objects']))" "$b")
  up=0; round=1; missing_list=""
  while :; do
    missing_list=""
    for o in $objs; do readable "$o" || missing_list="$missing_list $o"; done
    nmiss=$(echo $missing_list | wc -w | tr -d ' ')
    [ "$nmiss" = "0" ] && break
    [ "$round" -gt "$TRIES" ] && break
    S="$R/upload/$name"; rm -rf "$S"
    for o in $missing_list; do mkdir -p "$S/audio/$(dirname "$o")"; cp "$R/audio/${o#sets/}" "$S/audio/$o"; done
    [ "$round" -gt 1 ] && echo "batch $name: $nmiss audio files still missing, upload round $round of $TRIES"
    "$SB" storage cp -r "$S/audio" ss:/// --linked --experimental -j 8 --cache-control "public, max-age=31536000, immutable" --content-type audio/mp4 > "$R/upload/$name.round$round.log" 2>&1 \
      || { echo "batch $name: upload round $round hit an error ($(grep -v 'new version\|recommend updating' "$R/upload/$name.round$round.log" | grep -i 'error\|time-out\|failed' | tail -1 | cut -c1-120)); waiting $((round*30)) s" >&2; sleep $((round*30)); }
    up=$((up+nmiss)); round=$((round+1))
  done
  [ "$nmiss" = "0" ] || { echo "batch $name: $nmiss audio objects not readable after $TRIES upload rounds; nothing written to the database (run the script again later)" >&2; continue; }
  echo "batch $name: audio in storage ($up uploaded now)"
  sb_rows "select * from public.media_exercise_sets where media_id in ($ids)" > "$R/backup/${name}_before.json"
  # one guarded transaction per SQL file; on an error (network or guard) the file is sent again after a pause,
  # at most 3 times: the guard makes a second send write nothing when the first one did arrive
  for f in $(python3 -c "import json,sys; print('\n'.join(json.load(open(sys.argv[1]))['sql']))" "$b"); do
    for t in 1 2 3; do
      if "$SB" db query --linked --file "$R/$f" > "$R/upload/$name.sql.log" 2>&1; then break; fi
      grep -q 'rows exist already' "$R/upload/$name.sql.log" && break
      echo "batch $name: $f not written on try $t ($(grep -v 'new version\|recommend updating' "$R/upload/$name.sql.log" | tail -1 | cut -c1-120))" >&2
      [ "$t" = 3 ] || sleep $((t*30))
    done
  done
  now=$(scalar "select count(*) from public.media_exercise_sets where media_id in ($ids)")
  echo "batch $name: $now of $n rows written"; [ "$now" = "$n" ] && { touch "$R/applied/$name"; shape_of "$b" "$name" "$ids"; }
done
q "select level, count(*) as videos from public.media_exercise_sets where status = 'live' group by 1 order by 1"

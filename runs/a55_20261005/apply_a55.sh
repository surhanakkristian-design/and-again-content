#!/bin/bash
# Owner: apply A55 (the lab's German / Spanish / French sets) to the live project.
#   bash ~/Projects/and-again-content/runs/a55_20261005/apply_a55.sh            the migration (if missing) + every batch not applied yet
#   bash ~/Projects/and-again-content/runs/a55_20261005/apply_a55.sh <batch>    the migration (if missing) + this batch (lab10_de / lab10_es / lab10_fr)
#   bash ~/Projects/and-again-content/runs/a55_20261005/apply_a55.sh --check    only check the files; no database or storage call
# Per batch: 1. its files are checked (SHA-256 of every file as built, SQL complete, every audio file there), 2. audio files
# that are not in storage yet are uploaded (bucket `audio`, sets/<media id>/a55_<lang>_*, new object names only), 3. every
# object is read back, 4. the before-state is saved (backup/<batch>_before.json), 5. the guarded write (one transaction; it
# writes nothing when a row of the batch exists already). A batch already in the database is skipped. Safe to run again.
# English (media_exercise_sets) is never touched. Rollback (not run): out/<batch>_rollback.sql, out/a55_migration_rollback.sql.
set -euo pipefail
R=~/Projects/and-again-content/runs/a55_20261005
MIG="$R/out/a55_migration.sql"
SB_SH=~/Projects/and-again/supabase/scripts/_sb.sh
BASE="https://abyrutykpvmzkfbesire.supabase.co/storage/v1/object/public/audio"
CHECK=0; ONLY=""; TRIES=${A55_UPLOAD_TRIES:-5}
case "${1:-}" in --check) CHECK=1 ;; "") ;; *) ONLY="$1" ;; esac
for f in "$SB_SH" "$MIG" "$R/out/a55_migration_rollback.sql" "$R/out/SHA256SUMS"; do [ -s "$f" ] || { echo "missing or empty: $f; nothing was sent" >&2; exit 1; }; done
grep -q "create table if not exists public.media_exercise_sets_l10n" "$MIG" || { echo "stopped: $MIG is not the A55 migration" >&2; exit 1; }
# every file as it was built (SQL, rollback, batch lists, migration, audio)
( cd "$R" && shasum -a 256 -c --quiet out/SHA256SUMS ) || { echo "stopped: a file changed since it was built (out/SHA256SUMS); nothing was sent" >&2; exit 1; }
if [ -n "$ONLY" ]; then BATCHES="$R/batches/$ONLY.json"; [ -s "$BATCHES" ] || { echo "no such batch: $ONLY" >&2; exit 1; }; else BATCHES=$(ls "$R"/batches/*.json | sort); fi
for b in $BATCHES; do
  python3 - "$R" "$b" <<'PY'
import json, os, sys
R, b = sys.argv[1], json.load(open(sys.argv[2])); bad = []
for f in b['sql'] + [b['rollback']]:
    p = f'{R}/{f}'
    if not os.path.exists(p) or os.path.getsize(p) < 50: bad.append(f'missing or empty: {f}'); continue
    s = open(p).read()
    if '\nbegin;\n' not in '\n' + s or not s.rstrip().endswith('commit;'): bad.append(f'not one complete transaction: {f}')
    if 'media_exercise_sets (' in s or 'update public.media_exercise_sets ' in s: bad.append(f'touches the English table: {f}')
for o in b['objects']:
    p = f"{R}/audio/{b['lang']}/{o[len('sets/'):]}"
    if not os.path.exists(p) or os.path.getsize(p) < 1500: bad.append(f'audio file missing or empty: {o}')
if bad: print(f"batch {b['batch']}: " + '; '.join(bad[:10]), file=sys.stderr); sys.exit(1)
print(f"batch {b['batch']}: files ok ({len(b['ids'])} videos, {len(b['objects'])} audio files)")
PY
done
[ "$CHECK" = 1 ] && { echo "check only: nothing was sent"; exit 0; }
cd ~/Projects/and-again && source "$SB_SH"
readable() { local c i; for i in 1 2 3; do c=$(curl -s -o /dev/null -w '%{http_code}' --max-time 30 -r 0-0 "$BASE/$1" || echo 000)
  case "$c" in 200|206) return 0 ;; 400|404) return 1 ;; esac; sleep 3; done; return 1; }
scalar() { local v t; for t in 1 2 3; do v=$(sb_scalar "$1") && { echo "$v"; return 0; }; sleep 20; done; echo "query failed 3 times: $1" >&2; return 1; }
if [ "$(scalar "select count(*) from information_schema.tables where table_schema='public' and table_name='media_exercise_sets_l10n'")" = "0" ]; then
  "$SB" db query --linked --file "$MIG" >/dev/null
  "$SB" migration repair --linked --status applied 20261006100000 >/dev/null 2>&1 || echo "note: migration 20261006100000 not recorded (run from ~/Projects/and-again: supabase migration repair --linked --status applied 20261006100000)"
  echo "migration applied (table media_exercise_sets_l10n)"
else echo "migration: table is there already"; fi
mkdir -p "$R/backup" "$R/applied" "$R/upload"
for b in $BATCHES; do
  name=$(basename "$b" .json); lang=$(python3 -c "import json,sys; print(json.load(open(sys.argv[1]))['lang'])" "$b")
  ids=$(python3 -c "import json,sys; print(','.join(str(i) for i in json.load(open(sys.argv[1]))['ids']))" "$b")
  n=$(python3 -c "import json,sys; print(len(json.load(open(sys.argv[1]))['ids']))" "$b")
  have=$(scalar "select count(*) from public.media_exercise_sets_l10n where learning_language = '$lang' and media_id in ($ids)")
  if [ "$have" = "$n" ]; then echo "batch $name: already in the database ($n rows), skipped"; touch "$R/applied/$name"; continue; fi
  if [ "$have" != "0" ]; then echo "batch $name: $have of $n rows exist already - not touched, look at it" >&2; continue; fi
  objs=$(python3 -c "import json,sys; print('\n'.join(json.load(open(sys.argv[1]))['objects']))" "$b")
  up=0; round=1
  while :; do
    missing_list=""
    for o in $objs; do readable "$o" || missing_list="$missing_list $o"; done
    nmiss=$(echo $missing_list | wc -w | tr -d ' ')
    [ "$nmiss" = "0" ] && break
    [ "$round" -gt "$TRIES" ] && break
    S="$R/upload/$name"; rm -rf "$S"
    for o in $missing_list; do mkdir -p "$S/audio/$(dirname "$o")"; cp "$R/audio/$lang/${o#sets/}" "$S/audio/$o"; done
    "$SB" storage cp -r "$S/audio" ss:/// --linked --experimental -j 8 --cache-control "public, max-age=31536000, immutable" --content-type audio/mp4 > "$R/upload/$name.round$round.log" 2>&1 \
      || { echo "batch $name: upload round $round hit an error; waiting $((round*30)) s" >&2; sleep $((round*30)); }
    up=$((up+nmiss)); round=$((round+1))
  done
  [ "$nmiss" = "0" ] || { echo "batch $name: $nmiss audio objects not readable after $TRIES upload rounds; nothing written (run the script again later)" >&2; continue; }
  echo "batch $name: audio in storage ($up uploaded now)"
  sb_rows "select * from public.media_exercise_sets_l10n where learning_language = '$lang' and media_id in ($ids)" > "$R/backup/${name}_before.json"
  for f in $(python3 -c "import json,sys; print('\n'.join(json.load(open(sys.argv[1]))['sql']))" "$b"); do
    for t in 1 2 3; do
      if "$SB" db query --linked --file "$R/$f" > "$R/upload/$name.sql.log" 2>&1; then break; fi
      grep -q 'rows exist already' "$R/upload/$name.sql.log" && break
      echo "batch $name: $f not written on try $t ($(grep -v 'new version\|recommend updating' "$R/upload/$name.sql.log" | tail -1 | cut -c1-120))" >&2
      [ "$t" = 3 ] || sleep $((t*30))
    done
  done
  now=$(scalar "select count(*) from public.media_exercise_sets_l10n where learning_language = '$lang' and media_id in ($ids)")
  echo "batch $name: $now of $n rows written"; [ "$now" = "$n" ] && touch "$R/applied/$name"
done
"$SB" db query --linked "select learning_language, count(*) as videos from public.media_exercise_sets_l10n where status = 'live' group by 1 order by 1" 2>&1 | grep -v 'new version\|recommend updating' || true

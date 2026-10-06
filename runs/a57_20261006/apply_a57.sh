#!/bin/bash
# Owner: apply A57 (German / Spanish / French sets of the remaining videos) to the live project. Safe to run again.
#   bash ~/Projects/and-again-content/runs/a57_20261006/apply_a57.sh              every built batch not applied yet
#   bash ~/Projects/and-again-content/runs/a57_20261006/apply_a57.sh <name> ...   these batches (b001_de, fix8039, ...)
#   bash ~/Projects/and-again-content/runs/a57_20261006/apply_a57.sh --check      only check the files; no database or storage call
# Per batch: 1. its files are checked (SHA-256 of every file as built: out/<name>.sha256), 2. upload57.py sends every audio
# object one file at a time with retries and reads each back (bucket `audio`, new names only), 3. the before-state is saved
# (backup/<name>_before.json), 4. the guarded SQL files (one transaction each; an insert chunk writes nothing when one of its rows
# exists already, an update checks its before-state). Rows are written only after ALL the batch's audio objects read back.
# English (media_exercise_sets) is never touched. Rollback (not run): out/<name>_rollback.sql.
set -uo pipefail
R=~/Projects/and-again-content/runs/a57_20261006
SB_SH=~/Projects/and-again/supabase/scripts/_sb.sh
CHECK=0; NAMES=()
for a in "$@"; do case "$a" in --check) CHECK=1 ;; *) NAMES+=("$a") ;; esac; done
[ ${#NAMES[@]} -eq 0 ] && for f in $(ls "$R"/batches/*.json 2>/dev/null | sort); do NAMES+=("$(basename "$f" .json)"); done
[ -s "$SB_SH" ] || { echo "missing $SB_SH" >&2; exit 1; }
cd ~/Projects/and-again && source "$SB_SH"
scalar() { local v t; for t in 1 2 3; do v=$(sb_scalar "$1") && { echo "$v"; return 0; }; sleep 20; done; echo "query failed 3 times: $1" >&2; return 1; }
mkdir -p "$R/backup" "$R/applied" "$R/upload"
okn=0; badn=0
for name in "${NAMES[@]}"; do
  b="$R/batches/$name.json"; [ -s "$b" ] || { echo "$name: no such batch" >&2; badn=$((badn+1)); continue; }
  [ -e "$R/applied/$name" ] && { echo "$name: applied already"; continue; }
  ( cd "$R" && shasum -a 256 -c --quiet "out/$name.sha256" ) || { echo "$name: a file changed since it was built; nothing sent" >&2; badn=$((badn+1)); continue; }
  python3 - "$R" "$b" <<'PY' || { badn=$((badn+1)); continue; }
import json, os, sys
R, b = sys.argv[1], json.load(open(sys.argv[2])); bad = []
for f in b['sql'] + [b['rollback']]:
    s = open(f'{R}/{f}').read()
    if '\nbegin;\n' not in '\n' + s or not s.rstrip().endswith('commit;'): bad.append(f'not one complete transaction: {f}')
    if 'media_exercise_sets (' in s or 'update public.media_exercise_sets ' in s: bad.append(f'touches the English table: {f}')
if bad: print(b['batch'] + ': ' + '; '.join(bad), file=sys.stderr); sys.exit(1)
PY
  [ "$CHECK" = 1 ] && { echo "$name: files ok"; continue; }
  lang=$(python3 -c "import json,sys; print(json.load(open(sys.argv[1]))['lang'])" "$b")
  ids=$(python3 -c "import json,sys; print(','.join(str(i) for i in json.load(open(sys.argv[1]))['ids']) or '0')" "$b")
  n=$(python3 -c "import json,sys; print(len(json.load(open(sys.argv[1]))['ids']))" "$b")
  [ "$n" = 0 ] && { echo "$name: no videos in this batch; nothing to do"; continue; }
  kind=$(python3 -c "import json,sys; print(json.load(open(sys.argv[1])).get('kind','insert'))" "$b")
  have=$(scalar "select count(*) from public.media_exercise_sets_l10n where learning_language = '$lang' and media_id in ($ids)") || { badn=$((badn+1)); continue; }
  if [ "$kind" = insert ] && [ "$have" = "$n" ]; then echo "$name: already in the database ($n rows)"; touch "$R/applied/$name"; okn=$((okn+1)); continue; fi
  python3 "$R/upload57.py" "$name" || { echo "$name: audio not all read back; nothing written (run again later)" >&2; badn=$((badn+1)); continue; }
  [ -s "$R/upload/$name.ok" ] || { echo "$name: no upload receipt; nothing written" >&2; badn=$((badn+1)); continue; }
  bk=0; for t in 1 2 3 4; do sb_rows "select * from public.media_exercise_sets_l10n where learning_language = '$lang' and media_id in ($ids)" > "$R/backup/${name}_before.json" && { bk=1; break; }; sleep $((t*20)); done
  [ "$bk" = 1 ] || { echo "$name: backup failed 4 times; nothing written" >&2; badn=$((badn+1)); continue; }
  for f in $(python3 -c "import json,sys; print('\n'.join(json.load(open(sys.argv[1]))['sql']))" "$b"); do
    for t in 1 2 3; do
      if "$SB" db query --linked --file "$R/$f" > "$R/upload/$(basename "$f").log" 2>&1; then break; fi
      grep -q 'rows exist already\|before-state' "$R/upload/$(basename "$f").log" && { echo "$name: $f guard: $(grep -o 'A57[^"]*' "$R/upload/$(basename "$f").log" | head -1)"; break; }
      echo "$name: $f not written on try $t" >&2; [ "$t" = 3 ] || sleep $((t*30))
    done
  done
  if [ "$kind" = insert ]; then
    now=$(scalar "select count(*) from public.media_exercise_sets_l10n where learning_language = '$lang' and media_id in ($ids)")
    echo "$name: $now of $n rows in the database"; [ "$now" = "$n" ] && { touch "$R/applied/$name"; okn=$((okn+1)); } || badn=$((badn+1))
  else
    v=$(python3 -c "import json,sys; print(json.load(open(sys.argv[1]))['verify_sql'])" "$b")
    now=$(scalar "$v"); echo "$name: verify -> $now"; [ "$now" = "$n" ] && { touch "$R/applied/$name"; okn=$((okn+1)); } || badn=$((badn+1))
  fi
done
echo "applied now or before: $okn, not applied: $badn"
[ "$CHECK" = 1 ] || "$SB" db query --linked "select learning_language, count(*) as videos from public.media_exercise_sets_l10n where status = 'live' group by 1 order by 1" 2>&1 | grep -E '"(learning_language|videos)"' | paste - - || true

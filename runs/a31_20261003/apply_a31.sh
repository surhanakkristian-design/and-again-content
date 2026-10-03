#!/bin/bash
# Owner: apply A31 (35 groups, media.group_id, representatives, distractor lists) to the live database.
#   bash ~/Projects/and-again-content/runs/a31_20261003/apply_a31.sh            apply
#   bash ~/Projects/and-again-content/runs/a31_20261003/apply_a31.sh --check    only check the files, no database call
# One run does everything: the additive migration (one transaction), the guarded data write (one
# transaction; it stops and changes nothing if the tables are not empty or the media changed since
# the snapshot), records the migration, then prints the counts. Dry run of both was clean on 3 Oct 2026.
# Rollback (not run): out/a31_rollback.sql
set -euo pipefail
R=~/Projects/and-again-content/runs/a31_20261003
SB_SH=~/Projects/and-again/supabase/scripts/_sb.sh
MIG="$R/out/apply_migration.sql"
DATA="$R/out/a31_data.sql"
# every file the script reads must be there, with its content, before anything is sent
missing=0
for f in "$SB_SH" "$MIG" "$DATA" "$R/out/a31_rollback.sql"; do
  if [ ! -s "$f" ]; then echo "missing or empty: $f" >&2; missing=1; fi
done
[ "$missing" -eq 0 ] || { echo "stopped: nothing was sent to the database" >&2; exit 1; }
grep -q "create table if not exists public.media_groups" "$MIG" || { echo "stopped: $MIG is not the A31 migration" >&2; exit 1; }
grep -q "insert into public.tinder_word_distractors" "$DATA" || { echo "stopped: $DATA is not the A31 data" >&2; exit 1; }
[ "$(head -1 "$MIG")" = "begin;" ] && [ "$(tail -1 "$MIG")" = "commit;" ] || { echo "stopped: $MIG is not one transaction" >&2; exit 1; }
[ "$(tail -1 "$DATA")" = "commit;" ] || { echo "stopped: $DATA is not complete" >&2; exit 1; }
cd ~/Projects/and-again && source "$SB_SH"
echo "files ok ($(wc -c < "$MIG" | tr -d ' ') B migration, $(wc -c < "$DATA" | tr -d ' ') B data); CLI: $SB"
if [ "${1:-}" = "--check" ]; then echo "check only: nothing was sent to the database"; exit 0; fi
"$SB" db query --linked --file "$MIG" >/dev/null
echo "migration applied"
"$SB" db query --linked --file "$DATA" >/dev/null
echo "data written"
"$SB" migration repair --linked --status applied 20261003210000 >/dev/null
echo "migration recorded"
"$SB" db query --linked "select (select count(*) from media_groups) as groups, (select count(*) from media where group_id is not null) as media_grouped, (select count(*) from media where group_id is null) as media_without_group, (select count(*) from tinder_word_distractors) as lists, (select round(avg(cardinality(distractor_concept_ids)),1) from tinder_word_distractors) as avg_options"
echo "expected: groups 35, media_grouped 6205, media_without_group 0, lists 3034, avg_options 39.8"

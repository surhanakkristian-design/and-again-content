#!/bin/bash
# A32: fresh snapshot of the live tables (reads only).
set -euo pipefail
R=~/Projects/and-again-content/runs/a32_20261003
cd ~/Projects/and-again && source supabase/scripts/_sb.sh
page() { # name, select-with-order, page size
  local name="$1" q="$2" n="$3" off=0; : > "$R/data/$name.jsonl"
  while :; do
    rows="$(sb_rows "$q limit $n offset $off")"
    c=$(python3 -c 'import json,sys; r=json.loads(sys.stdin.read()); [print(json.dumps(x)) for x in r]; print(len(r),file=sys.stderr)' <<<"$rows" 2>&1 >>"$R/data/$name.jsonl")
    [ "$c" -lt "$n" ] && break; off=$((off+n))
  done
  python3 -c 'import json,sys; r=[json.loads(l) for l in open(sys.argv[1])]; json.dump(r,open(sys.argv[1][:-1],"w")); print(sys.argv[2],len(r))' "$R/data/$name.jsonl" "$name"
  rm "$R/data/$name.jsonl"
}
page twd "select media_id, concept_id, group_id, level, distractor_concept_ids, fallback_concept_ids from tinder_word_distractors order by media_id" 500
page media "select id, title, media_type, group_id, asset_description, transcript from media order by id" 500
page concepts "select id, word, part_of_speech, definition from word_concepts order by id" 1000
page concept_media "select id, concept_id, media_id from concept_media order by id" 2000
page ex "select id, concept_id, media_id, exercise_type_id from exercises where exercise_type_id in (74,75) order by id" 2000
page loc "select concept_id, language_code, translation, display_form from word_localizations order by concept_id, language_code" 3000
page groups "select id, name, source_category_ids from media_groups order by id" 100

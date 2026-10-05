#!/bin/bash
# A49: dry run of apply_a45.sh's decisions for every A45 batch that holds 7071, 4265 or 624 - read-only queries only.
# Shows: which batch files hold the three ids, what apply_a45.sh would do with that batch (skip / write), whether its
# shape step would touch them, whether its insert guard would stop, and that the batch SQL now equals the database.
set -euo pipefail
A=~/Projects/and-again-content/runs/a45_20261004
cd ~/Projects/and-again && source supabase/scripts/_sb.sh
echo "== batch files and SQL files that name the three ids"
for b in "$A"/batches/*.json; do python3 -c "import json,sys;b=json.load(open(sys.argv[1]));h=[i for i in (7071,4265,624) if i in b['ids']];print(b['batch'],h) if h else None" "$b"; done
grep -l -E "^\((7071|4265|624), " "$A"/out/*.sql | sed "s|$A/||"
ids=$(python3 -c "import json;print(','.join(map(str,json.load(open('$A/batches/lab10.json'))['ids'])))")
have=$(sb_scalar "select count(*) from public.media_exercise_sets where media_id in ($ids)")
echo "== apply_a45.sh lab10: rows of its 10 ids in the table = $have (n = 10)"
[ "$have" = "10" ] && echo "   -> 'batch lab10: already in the database (10 rows), skipped' (no upload, no insert)" || echo "   -> WOULD NOT SKIP"
w=$(sb_scalar "select count(*) from public.media_exercise_sets where media_id in ($ids) and width is null")
echo "   shape step: rows without a shape = $w -> $([ "$w" = 0 ] && echo 'returns before any update' || echo 'WOULD RUN out/lab10_shape.sql')"
echo "   insert guard (if it were ever sent): rows exist = $(sb_scalar "select exists (select 1 from public.media_exercise_sets where media_id in ($ids))") -> raises 'rows exist already, nothing written'"
echo "== the patched lab10 SQL rows vs the database (taps, nouns, question, answer chips/text/audio, tr)"
sb_rows "select media_id, taps, nouns, question, answer_chips, answer_text, answer_audio_url, tr, content_version from public.media_exercise_sets where media_id in (7071,4265,624)" > /tmp/a49_db3.json
python3 - "$A/out/lab10_data_01.sql" /tmp/a49_db3.json <<'PY'
import json, sys
db = {r['media_id']: r for r in json.load(open(sys.argv[2]))}
for l in open(sys.argv[1]).read().split('\n'):
    for v in (7071, 4265, 624):
        if not l.startswith(f'({v}, '): continue
        p = l.split('$a45$'); r = db[v]
        same = {'taps': json.loads(p[1]) == r['taps'], 'nouns': json.loads(p[3]) == r['nouns'], 'question': p[5] == r['question'],
                'chips': json.loads(p[7]) == r['answer_chips'], 'text': p[9] == r['answer_text'], 'audio': p[11] == r['answer_audio_url'],
                'tr': json.loads(p[13]) == r['tr']}
        print(f"   {v}: content_version {r['content_version']}, equal: " + ', '.join(f'{k} {"yes" if s else "NO"}' for k, s in same.items()))
PY
rm -f /tmp/a49_db3.json

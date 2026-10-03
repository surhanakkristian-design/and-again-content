#!/bin/bash
# A32: re-select the live tinder_word_distractors and compare with out/distractors.json + out/fallback.json (reads only).
set -euo pipefail
R=~/Projects/and-again-content/runs/a32_20261003
cd ~/Projects/and-again && source supabase/scripts/_sb.sh
: > "$R/data/twd_after.jsonl"
for off in 0 500 1000 1500 2000 2500 3000 3500; do
  sb_rows "select media_id, distractor_concept_ids, fallback_concept_ids from tinder_word_distractors order by media_id limit 500 offset $off" | python3 -c 'import json,sys; [print(json.dumps(x)) for x in json.load(sys.stdin)]' >> "$R/data/twd_after.jsonl"
done
python3 - "$R" <<'P'
import json,sys
R=sys.argv[1]
rows=[json.loads(l) for l in open(R+"/data/twd_after.jsonl")]
D=json.load(open(R+"/out/distractors.json")); F=json.load(open(R+"/out/fallback.json"))
bad=[r["media_id"] for r in rows if [int(x) for x in r["distractor_concept_ids"]]!=D[str(r["media_id"])] or [int(x) for x in r["fallback_concept_ids"]]!=F.get(str(r["media_id"]),[])]
print("live rows",len(rows),"expected 3034; rows that differ from the out files:",len(bad),bad[:10])
P

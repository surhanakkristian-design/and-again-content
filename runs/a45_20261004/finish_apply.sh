#!/bin/bash
# A45 session helper: finish a translated batch (audio, validate, SQL; a second pass when audio is missing), then write it
# live with apply_a45.sh (one apply at a time, guarded), then refresh db_state + progress.  bash finish_apply.sh <batch>
R=~/Projects/and-again-content/runs/a45_20261004; b=$1; cd "$R"
for t in 1 2; do
  python3 batch.py finish $b > data/finish_$b.log 2>&1
  python3 -c "import json,sys; r=json.load(open('data/$b.result.json')); sys.exit(1 if any('manifest' in str(v) for v in r['failed'].values()) else 0)" && break
done
tail -1 data/finish_$b.log
while pgrep -f "apply_a45.sh b" >/dev/null || [ -e upload/.apply_lock ]; do sleep 20; done
touch upload/.apply_lock; bash apply_a45.sh $b > upload/apply_$b.log 2>&1; rm -f upload/.apply_lock
grep "batch $b" upload/apply_$b.log | tail -2
python3 db_state.py > /dev/null && python3 progress.py "${2:-}" 

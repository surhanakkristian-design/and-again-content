#!/bin/bash
# A45 session helper: finish + write the given batches one after another (log: data/queue.log).
R=~/Projects/and-again-content/runs/a45_20261004; cd "$R"
for b in "$@"; do echo "$(date +%H:%M) start $b" >> data/queue.log; bash finish_apply.sh $b "Resumed 5 Oct 2026; finishing the last batches." >> data/queue.log 2>&1; echo "$(date +%H:%M) end $b" >> data/queue.log; done
echo "QUEUE DONE" >> data/queue.log

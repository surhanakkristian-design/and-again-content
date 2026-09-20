#!/bin/zsh
# §1.2 halves -> DIAGNOSIS_s04.md -> Part 1 driver.  Unattended; detached by daemonize.py.
P=~/Projects/and-again-content/translation-offline/phase2f
if [[ ! -f $P/diag/halves_cz_0002_s04_v.json ]]; then
  cd $P/diag && python3 halves.py cz_0002_s04_v >> $P/diag/halves_cz_0002_s04_v.stdout.txt 2>&1
fi
cd $P/diag && python3 write_diagnosis.py >> $P/run_part1.log 2>&1
git -C ~/Projects/and-again-content add -A translation-offline/phase2f
git -C ~/Projects/and-again-content commit -q -m "Phase 2F §1.2: s04 diagnosis (prompt byte comparison, slice analysis, 50-row halves)

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
cd $P && exec python3 run_part1.py >> $P/run_part1.stdout.txt 2>&1

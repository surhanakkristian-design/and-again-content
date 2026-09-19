#!/bin/bash
# Phase 1Q: the ONE final run of runner_1p.py. Resumes only after the runner's own pause (exit 3); never after a completed run.
cd /Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase1p || exit 1
export PYTHONDONTWRITEBYTECODE=1
Q=../phase1q
for i in 1 2 3 4 5 6; do
  echo "attempt $i start $(date '+%F %T')" >> $Q/run_wrapper.log
  python3 runner_1p.py --final >> $Q/run_final_stdout.log 2>&1
  rc=$?
  echo "attempt $i rc=$rc end $(date '+%F %T')" >> $Q/run_wrapper.log
  [ -f FINAL_RUN_DONE ] && break
  [ $rc -ne 3 ] && break
  sleep 1200
done
cd /Users/kristiansurhanak/Projects/and-again-content
git add translation-offline/phase1p translation-offline/phase1q >/dev/null 2>&1
git commit -m "Phase 1Q: final run of the 1P set (runner output, ledger, logs)" -- translation-offline/phase1p translation-offline/phase1q >> translation-offline/phase1q/run_wrapper.log 2>&1
date '+%F %T' > translation-offline/phase1q/RUN_WRAPPER_EXITED

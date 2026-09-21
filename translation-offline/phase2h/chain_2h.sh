#!/bin/zsh
# Phase 2H paid chain.  Launch:  nohup zsh chain_2h.sh > chain_2h.stdout.txt 2>&1
# 1 SHA inputs before  2 run_2h.py == FROZEN_SHA  3 tests (abort, 0 spent, on any FAIL)  4 annotate  5 lk (unless a
# global stop)  6 merge + upload (0 model calls, always)  7 SHA after + diff  8 DONE.  Commit after each stage.
setopt NULL_GLOB
P=~/Projects/and-again-content/translation-offline/phase2h
R=~/Projects/and-again-content
T=$R/translation-offline
CAP=2000000
cd $P || exit 1
log() { local m="$(date '+%Y-%m-%d %H:%M:%S') CHAIN $*"; print -r -- "$m" >> $P/chain_2h.log; print -r -- "$m" >> $P/progress.log; print -r -- "$m" }
gc() { git -C $R add -- translation-offline/phase2h >/dev/null 2>&1
       git -C $R commit -q -m "Phase 2H: $1

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>" -- translation-offline/phase2h >/dev/null 2>&1 }
global_stop() { [[ -f $P/STOP_usage_limit.md || -f $P/STOP_first_session_failed.md || -f $P/STOP_token_cap.md ]] }
shalist() { ( cd $T && find phase2c/out phase2d/out phase2e/out phase2f phase2g -type f -print0 | sort -z | xargs -0 shasum -a 256 ) }
log "start pid $$ cap $CAP"
[[ -f SHA_inputs_before.txt ]] || shalist > SHA_inputs_before.txt
gc "input hashes before"
want=$(awk '{print $1}' FROZEN_SHA.txt); have=$(shasum -a 256 run_2h.py | awk '{print $1}')
if [[ "$want" != "$have" ]]; then
  log "ABORT: run_2h.py sha $have != FROZEN_SHA $want (nothing spent)"; print -r -- "ABORTED: run_2h.py sha mismatch" > DONE; gc "ABORT sha mismatch"; exit 2
fi
python3 test_2h.py > test_2h_output.txt 2>&1; trc=$?
if (( trc != 0 )) || grep -q '^FAIL' test_2h_output.txt; then
  log "ABORT: tests failed (exit $trc), nothing spent"; print -r -- "ABORTED: tests failed | $(tail -1 test_2h_output.txt)" > DONE; gc "ABORT tests failed"; exit 3
fi
log "tests: $(tail -1 test_2h_output.txt)"; gc "tests passed"
python3 run_2h.py annotate --cap $CAP >> run_2h_annotate.stdout.txt 2>&1; log "annotate exit $?"; gc "annotate stage"
if global_stop; then log "lk skipped: global stop $(ls STOP_usage_limit.md STOP_first_session_failed.md STOP_token_cap.md 2>/dev/null)"
else python3 run_2h.py lk --cap $CAP >> run_2h_lk.stdout.txt 2>&1; log "lk exit $?"; fi
gc "lk stage"
python3 run_2h.py merge >> run_2h_merge.stdout.txt 2>&1; log "merge exit $?"
python3 run_2h.py upload >> run_2h_merge.stdout.txt 2>&1; log "upload exit $?"; gc "merge + upload"
shalist > SHA_inputs_after.txt
if diff SHA_inputs_before.txt SHA_inputs_after.txt > SHA_inputs_diff.txt; then log "inputs unchanged"; else log "INPUTS CHANGED: see SHA_inputs_diff.txt"; fi
S=( $P/STOP_*.md )
if (( ${#S} )); then print -r -- "STOPPED: ${S:t} | $(tail -1 progress.log)" > DONE; else print -r -- "OK | $(tail -1 progress.log)" > DONE; fi
log "DONE $(cat DONE)"; gc "DONE"

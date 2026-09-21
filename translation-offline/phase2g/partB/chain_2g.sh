#!/bin/zsh
# Phase 2G Part B chain: annotate (B2-B4) -> lk (B5, always, unless a headless-Claude hard stop) -> B6 -> DONE.
setopt NULL_GLOB
P=~/Projects/and-again-content/translation-offline/phase2g/partB
R=~/Projects/and-again-content
cd $P
log() { print -r -- "$(date '+%Y-%m-%d %H:%M:%S') CHAIN $*" >> $P/chain_2g.log }
gc() { git -C $R add -A translation-offline/phase2g/partB >/dev/null 2>&1
       git -C $R commit -q -m "Phase 2G Part B: $1

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>" >/dev/null 2>&1 }
claude_stop() { [[ -f $P/STOP_usage_limit.md || -f $P/STOP_first_session_failed.md ]] }
log "start pid $$"; python3 progress.py start
python3 run_2g_cz.py --all --cap 2900000 >> run_2g_cz.stdout.txt 2>&1; rc=$?
log "annotation exit $rc"
if claude_stop; then
  log "headless-Claude hard stop -> assemble-only pass (0 model calls)"
  python3 run_2g_cz.py --all --no-spawn --ignore-stop-file --cap 2900000 >> run_2g_cz.stdout.txt 2>&1; log "assemble-only exit $?"
fi
python3 progress.py annotate; gc "annotation stage (exit $rc)"
python3 prep_lk.py >> prep_lk.stdout.txt 2>&1; log "prep_lk exit $?"
if claude_stop; then
  log "lk skipped: headless-Claude hard stop (the only stop that blocks lk)"
elif [[ -f $P/lk/NOTHING_TO_JUDGE ]]; then
  log "lk: nothing to judge"
else
  SPENT=$(python3 -c 'import json;print(int(json.load(open("ledger_2g_cz.json")).get("spent") or 0))' 2>/dev/null || echo 0)
  CAPLK=$(( 2900000 - SPENT )); (( CAPLK < 0 )) && CAPLK=0
  log "lk start cap $CAPLK (annotation spent $SPENT)"
  python3 run_2g_lk.py --cap $CAPLK >> run_2g_lk.stdout.txt 2>&1; log "lk exit $?"
fi
python3 progress.py lk; gc "lk stage"
python3 final_merge.py >> final_merge.stdout.txt 2>&1; log "final_merge exit $?"
python3 progress.py final; gc "B6 final annotations + upload package"
S=( $P/STOP_*.md )
if (( ${#S} )); then print -r -- "STOPPED: ${S:t} | $(tail -1 progress.log)" > $P/DONE
else print -r -- "OK | $(tail -1 progress.log)" > $P/DONE; fi
log "DONE $(cat $P/DONE)"; gc "DONE"

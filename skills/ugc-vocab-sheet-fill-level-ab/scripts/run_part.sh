#!/usr/bin/env bash
# run_part.sh — drive one whole pass with a chain of fresh Claude Code sessions.
set -uo pipefail

WB="${1:?usage: run_part.sh <workbook.xlsx>}"
CONCEPTS_PER_PASS="${CONCEPTS_PER_PASS:-25}"
PROMPT_FILE="${PROMPT_FILE:-./PROMPT_part1_translations.md}"
GATE_SCRIPT="${GATE_SCRIPT:-scripts/translation_status.py}"
UNIT="${UNIT:-concepts}"
MAX_PASSES="${MAX_PASSES:-40}"
LOG_DIR="logs"; mkdir -p "$LOG_DIR"

PROMPT="Read ${PROMPT_FILE} and follow it exactly. Start by running the status script named in \
it, then resume at the first unfinished item. Don't explore the folder first. Do the next \
${CONCEPTS_PER_PASS} ${UNIT}, run validate_part.py, then stop. Keep output minimal: counts, not \
contents."

remaining () { python3 "$GATE_SCRIPT" "$WB" --gate 2>/dev/null \
                 | sed -n 's/^GATE: \([0-9]*\).*/\1/p'; }

cp "$WB" "$LOG_DIR/backup_$(date +%Y%m%d_%H%M%S).xlsx"

for ((pass=1; pass<=MAX_PASSES; pass++)); do
  if python3 "$GATE_SCRIPT" "$WB" --gate >/dev/null 2>&1; then
    echo "== part complete after $((pass-1)) passes"; break
  fi
  before=$(remaining)
  echo "== pass $pass — $before remaining — $(date +%H:%M)"

  claude -p "$PROMPT" \
      --allowedTools "Read,Edit,Write,Bash(python3 *),Bash(python *)" \
      --permission-mode acceptEdits \
      --model opus \
      --max-turns 200 \
      >"$LOG_DIR/pass_${pass}.log" 2>&1
  status=$?

  after=$(remaining)
  echo "   pass $pass done (exit $status): $before -> $after"

  if [[ "$after" == "$before" ]]; then
    echo "!! no progress in pass $pass — stopping. See $LOG_DIR/pass_${pass}.log"; exit 1
  fi
  cp "$WB" "$LOG_DIR/backup_pass_${pass}.xlsx"
done

python3 scripts/validate_part.py "$WB" --loanwords ./loanwords.json | tail -3

#!/bin/bash
# A56: starts the paid edits of ONE word in parallel (gen56.sh enforces floor + job cap), only if the credits left
# under the 40-credit budget cover all of them once plus one spare edit (CLAUDE.md rule 6).
#   run_word.sh <id> <attempt tag> <prompt name> ...      (prompt name = prompts/<name>.txt)
set -uo pipefail
P="$(cd "$(dirname "$0")" && pwd)"; ID="$1"; ATT="$2"; shift 2
STILL=$(python3 -c "import json;p=json.load(open('$P/../PLAN56.json'));print(p.get('refs',{}).get('$ID') or p['stills']['$ID'])")
START=$(cat "$P/START_BALANCE"); FLOOR=$((START - 40))
BAL=$(higgsfield account status --json | python3 -c 'import json,sys;print(json.load(sys.stdin)["credits"])')
NEED=$(( ($# + ${SPARE:-1}) * 2 ))
[ $((BAL - FLOOR)) -ge $NEED ] || { echo "$(date +%T) word $ID $ATT NOT STARTED: left $((BAL - FLOOR)) < need $NEED" | tee -a "$P/ledger.log"; exit 3; }
for n in "$@"; do "$P/gen56.sh" "${n}_${ATT}" "$P/prompts/$n.txt" "$STILL" > "$P/out/${n}_${ATT}.run" 2>&1 & sleep 3; done
wait; for n in "$@"; do echo "$n: $(tail -1 "$P/out/${n}_${ATT}.run")"; done

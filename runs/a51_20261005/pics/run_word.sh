#!/bin/bash
# A51: starts the paid edits of ONE word in parallel (gen51.sh enforces floor + job cap), only if the credits left
# cover all of them once plus one spare edit (CLAUDE.md rule 6).   run_word.sh <id> <attempt tag> <name=prompt> ...
set -uo pipefail
P="$(cd "$(dirname "$0")" && pwd)"; ID="$1"; ATT="$2"; shift 2
STILL=$(python3 -c "import json;p=json.load(open('$P/../PLAN.json'));print([c['still'] for c in p['$ID']['captions'] if c.get('still')][0])")
BAL=$(higgsfield account status --json | python3 -c 'import json,sys;print(json.load(sys.stdin)["credits"])')
NEED=$(( ($# + 1) * 2 ))
[ $((BAL - 9000)) -ge $NEED ] || { echo "$(date +%T) word $ID NOT STARTED: left $((BAL - 9000)) < need $NEED" | tee -a "$P/ledger.log"; exit 3; }
for a in "$@"; do n="${a%%=*}"; f="${a#*=}"; "$P/gen51.sh" "${n}_${ATT}" "$P/prompts/$f" "$STILL" > "$P/out/${n}_${ATT}.run" 2>&1 & sleep 3; done
wait; for a in "$@"; do n="${a%%=*}"; echo "$n: $(tail -1 "$P/out/${n}_${ATT}.run")"; done

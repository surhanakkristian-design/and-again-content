#!/bin/bash
# A51: one Nano Banana Pro edit of a still (9:16, 2K). usage: gen51.sh <name> <promptfile> <reference image>
# Cap: A51 budget = 22 credits (decision 377): the balance never goes below FLOOR=9000 (9002 + the owner's 20 - 22) and at most 11 jobs start.
# The balance is read before every job; jobs already started but not finished (pending/*.lock) are counted as spent.
set -euo pipefail
P="$(cd "$(dirname "$0")" && pwd)"; NAME="$1"; PROMPT="$(cat "$2")"; REF="$3"; FLOOR=9000
mkdir -p "$P/pending" "$P/out"
PRICE=$(higgsfield generate cost nano_banana_pro --prompt x --aspect_ratio 9:16 --resolution 2k --json | python3 -c 'import json,sys;print(json.load(sys.stdin)["credits"])')
BAL=$(higgsfield account status --json | python3 -c 'import json,sys;print(json.load(sys.stdin)["credits"])')
PEND=$(ls "$P/pending" | wc -l | tr -d ' ')
JOBS=$(grep -c " start balance " "$P/ledger.log" 2>/dev/null || true); JOBS=${JOBS:-0}
[ "$JOBS" -lt 11 ] || { echo "$(date +%T) $NAME REFUSED job cap 11 reached" >> "$P/ledger.log"; echo "CAP"; exit 3; }
python3 -c "import sys; sys.exit(0 if $BAL - $PEND*$PRICE - $PRICE >= $FLOOR else 1)" || { echo "$(date +%T) $NAME REFUSED balance $BAL pending $PEND price $PRICE floor $FLOOR" >> "$P/ledger.log"; echo "CAP"; exit 3; }
touch "$P/pending/$NAME.lock"; trap 'rm -f "$P/pending/$NAME.lock"' EXIT
echo "$(date +%T) $NAME start balance $BAL pending $PEND price $PRICE" >> "$P/ledger.log"
OUT=$(higgsfield generate create nano_banana_pro --prompt "$PROMPT" --image "$REF" --aspect_ratio 9:16 --resolution 2k --wait --wait-timeout 8m --json 2>&1) || true
echo "$OUT" > "$P/out/$NAME.json"
URL=$(echo "$OUT" | python3 -c 'import sys,re;t=sys.stdin.read();m=re.findall(r"https://[^\"]+_min\.webp",t) or re.findall(r"https://[^\"]+\.png",t);print(m[0] if m else "")')
BAL2=$(higgsfield account status --json | python3 -c 'import json,sys;print(json.load(sys.stdin)["credits"])')
[ -n "$URL" ] || { echo "$(date +%T) $NAME FAILED (no url) balance $BAL2" >> "$P/ledger.log"; echo "failed"; exit 4; }
URL="${URL/_min.webp/.png}"
curl -sL --max-time 120 -o "$P/out/$NAME.png" "$URL"
echo "$(date +%T) $NAME done balance $BAL2 url $URL" >> "$P/ledger.log"
echo "$NAME ok balance $BAL2"

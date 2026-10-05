#!/bin/bash
# A48 pilot: one Nano Banana Pro edit of the duke's still. usage: gen.sh <name> <promptfile> [<reference image>, default the still]
# Checks the balance first: stops when this image would take the A48 total past the cap of 100 credits.
set -euo pipefail
P="$(cd "$(dirname "$0")" && pwd)"; NAME="$1"; PROMPT="$(cat "$2")"; REF="${3:-$P/still_7071.png}"
BASE=9100; CAP=100; PRICE=$(higgsfield generate cost nano_banana_pro --prompt x --aspect_ratio 9:16 --resolution 2k --json | python3 -c 'import json,sys;print(json.load(sys.stdin)["credits"])')
BAL=$(higgsfield account status --json | python3 -c 'import json,sys;print(json.load(sys.stdin)["credits"])')
SPENT=$(python3 -c "print($BASE-$BAL)")
python3 -c "import sys; sys.exit(0 if $SPENT+$PRICE<=$CAP else 1)" || { echo "CAP: spent $SPENT + $PRICE > $CAP"; exit 3; }
echo "$(date +%T) $NAME balance $BAL spent $SPENT price $PRICE" >> "$P/ledger.log"
OUT=$(higgsfield generate create nano_banana_pro --prompt "$PROMPT" --image "$REF" --aspect_ratio 9:16 --resolution 2k --wait --wait-timeout 8m --json)
echo "$OUT" > "$P/out/$NAME.json"
URL=$(echo "$OUT" | python3 -c 'import json,sys,re;t=sys.stdin.read();m=re.findall(r"https://[^\"]+_min\.webp",t);print(m[0] if m else "")')
[ -n "$URL" ] || { echo "no url"; exit 4; }
URL="${URL/_min.webp/.png}"
curl -sL -o "$P/out/$NAME.png" "$URL"
BAL2=$(higgsfield account status --json | python3 -c 'import json,sys;print(json.load(sys.stdin)["credits"])')
echo "$(date +%T) $NAME done balance $BAL2 url $URL" >> "$P/ledger.log"
echo "$NAME ok balance $BAL2"

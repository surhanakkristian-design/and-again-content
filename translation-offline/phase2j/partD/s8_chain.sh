#!/bin/bash
# S8 pre-flight (0 cost) + freeze + commits + ONE open of the Part D set. Aborts on any failure before the open.
set -u
G="git -C /Users/kristiansurhanak/Projects/and-again-content"
ROOT=/Users/kristiansurhanak/Projects/and-again-content/translation-offline
P2J=$ROOT/phase2j; D=$P2J/partD; RUN=$D/run
export PYTHONDONTWRITEBYTECODE=1 P2J_F4FIX=1
fail(){ echo "PREFLIGHT FAIL: $*" | tee $D/S8_PREFLIGHT_FAIL.txt; exit 1; }
[ -e $RUN ] && fail "run dir exists already"
cd $P2J && shasum -a 256 -c FROZEN_SHA_S5.txt > $D/S8_frozen_check.txt 2>&1 || fail "frozen shasum -c"
echo "frozen files OK: $(grep -c ': OK' $D/S8_frozen_check.txt)"
python3 -B $P2J/test_2j.py > $D/test_2j_output_S8.txt 2>&1 || fail "test_2j rc=$?"
tail -3 $D/test_2j_output_S8.txt
S=$(shasum -a 256 $D/set/items.jsonl | cut -d' ' -f1)
[ "$S" = 221c90a8a9cfdeadbdef46f0afbdf5a98b042d521f8520feac5aed4208b4df5d ] || fail "items sha $S"
echo "items sha OK $S"
zsh $ROOT/phase2i/sha_tree.sh | grep -v '  phase2j/' > $P2J/SHA_pre_S8.txt
diff $P2J/SHA_before.txt $P2J/SHA_pre_S8.txt > $P2J/SHA_diff_pre_S8.txt || fail "sha tree differs"
echo "sha tree == SHA_before ($(wc -l < $P2J/SHA_pre_S8.txt) lines)"
python3 -B - <<'PY' > $D/S8_dry_count.json || fail "dry count"
import os, sys, json
P2J='/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2j'
sys.path.insert(0, P2J); import run_2j as R; B = R.B
items = [json.loads(l) for l in open(P2J + '/partD/set/items.jsonl', encoding='utf-8')]
dry = P2J + '/partD/dry'; os.makedirs(dry, exist_ok=True)
P = B.paths(dry)
clean = [B.clean_item(it, 'tonly') for it in items]
reqs = B.stack_call('tonly', 'prepare', clean, P)
keys = {B.req_key(q) for q in reqs.values()}
led = json.load(open(P2J + '/GEMINI_LEDGER.json'))
rem = 1200 - sum(int(v) for v in led.values())
out = {'items': len(items), 'requests_jids': len(reqs), 'needed_unique': len(keys), 'remaining': rem,
       'fits': len(keys) <= rem, 'note': 'prepare only (clean_item strips labels); no L3 call, no verdict, no results written'}
print(json.dumps(out)); sys.exit(0 if out['fits'] else 5)
PY
cat $D/S8_dry_count.json; echo
NEED=$(python3 -c "import json;print(json.load(open('$D/S8_dry_count.json'))['needed_unique'])")
# freeze
cd $P2J && { cat FROZEN_SHA_S5.txt | awk '{print $2}'; echo partD/set/items.jsonl; echo partD/judge/labels.jsonl; echo run_2j.py; } | sort -u | xargs shasum -a 256 > $D/FROZEN_SHA_D.txt
shasum -a 256 $D/FROZEN_SHA_D.txt | cut -d' ' -f1 > $D/FREEZE_HASH.txt
$G add translation-offline/phase2j/partD translation-offline/phase2j/SHA_pre_S8.txt translation-offline/phase2j/SHA_diff_pre_S8.txt
$G commit -q -m "phase2j S8: pre-flight (frozen check, test_2j, items sha, SHA tree, dry count $NEED) + Part D freeze

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>" || fail "freeze commit"
FC=$($G rev-parse HEAD); echo $FC > $D/FREEZE_COMMIT.txt
$G ls-tree -r --name-only $FC translation-offline/phase2j/partD/FROZEN_SHA_D.txt | grep -q FROZEN_SHA_D || fail "freeze commit missing file"
$G add translation-offline/phase2j/partD/FREEZE_COMMIT.txt
$G commit -q -m "phase2j S8: FREEZE_COMMIT $FC

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>" || fail "freeze-commit commit"
RC=$($G rev-parse HEAD); echo "$RC" > $D/RUN_COMMIT.txt
$G add translation-offline/phase2j/partD/RUN_COMMIT.txt
$G commit -q -m "phase2j S8: RUN_COMMIT $RC (run opens at this tree + this file)

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>" || fail "run commit"
$G ls-tree -r --name-only HEAD translation-offline/phase2j/partD | grep -q RUN_COMMIT.txt || fail "RUN_COMMIT not in HEAD"
[ -z "$($G status --porcelain translation-offline/phase2j)" ] || fail "phase2j dirty before open"
echo "commits: freeze $FC run $RC head $($G rev-parse --short HEAD)"
SD=""; for d in $P2J/run_S2 $P2J/run_S2c $P2J/partB/b4/run $P2J/partB/b4/probe; do [ -f $d/ledger.jsonl ] && SD="$SD $d"; done
echo "spend dirs:$SD"
nohup python3 -B $P2J/run_2j.py gemini --set $D/set/items.jsonl --run-dir $RUN --stage S8 --expect-needed $NEED \
  --spend-dirs $SD --purpose "Phase 2J Part D fresh set, S8, opened once" > $D/run.stdout.txt 2>&1 &
echo $! > $D/run.pid; echo "launched pid $(cat $D/run.pid) at $(date -u +%FT%TZ)"

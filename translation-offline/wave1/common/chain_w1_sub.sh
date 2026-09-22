#!/bin/bash
# Wave 1 per-language chain, SUBAGENT transport (decision 26: no headless CLI).  Re-run until CHAIN_DONE:
#   bash /abs/wave1/common/chain_w1_sub.sh <lang>      exit 6 = PENDING (the main session spawns the Opus subagents
#   listed in <lang>/partD/**/PENDING.json, records tokens.json, re-runs this script); any other non-zero = STOP.
# preflight (0 cost) -> partA_live (SELECT) -> projection -> set -> mock -> writers -> packets -> judges -> labels ->
# items -> freeze + commits -> ONE open of the set by the frozen stack -> post.  No rewrite (done in the database).
set -u
LANG_=$1
W1=/Users/kristiansurhanak/Projects/and-again-content/translation-offline/wave1
C=$W1/common; D=$W1/$LANG_; E=$D/partD
PY="python3 -B $C/pipeline_w1.py $LANG_"
export PYTHONDONTWRITEBYTECODE=1
commit(){ python3 -B $C/gitc.py "Wave 1 $LANG_: $1" $D >/dev/null 2>&1 || true; }
tok(){ python3 -B -c "import sys; sys.path.insert(0,'$C'); import pipeline_w1 as W; W.setlang('$LANG_'); t=W.spent(); W.tokens_md('- %s cumulative subagent tokens after %s: %s' % (W.now(), '$1', format(t, ','))); print('TOKENS after $1:', format(t, ','))"; }
fail(){ echo "CHAIN FAIL: $* ($(date -u +%FT%TZ))" | tee -a $D/CHAIN_FAIL.txt; commit "chain stopped: $*"; exit 1; }
pend(){ echo "PENDING at $1 ($(date -u +%FT%TZ))"; exit 6; }
step(){ echo "== $1 $(date -u +%FT%TZ)"; }
run(){ $PY $1; rc=$?; [ $rc = 6 ] && pend $1; [ $rc = 0 ] || fail "$1 (rc $rc)"; }
[ -f $E/run/FINAL_RUN_DONE ] && { echo CHAIN_DONE; exit 0; }
for f in STOP_*.md CHAIN_FAIL.txt; do ls $D/$f >/dev/null 2>&1 && fail "stop file present: $(ls $D/$f)"; done
if [ ! -f $D/.pre_done ]; then
  step preflight; python3 -B $C/test_w1.py > $D/test_w1_preflight.txt 2>&1 || fail "test_w1 (0 cost)"; tail -1 $D/test_w1_preflight.txt
  step partA_live; run partA_live
  step projection; run projection; tok projection
  step make_set; run make_set
  step mock; $PY mock > $D/mock_output.txt 2>&1 || fail "mock pipeline"; tail -1 $D/mock_output.txt
  touch $D/.pre_done
  commit "Part D (subagent transport): preflight, live rows (SELECT), projection, fresh set + exclusion proof, mock pass"
fi
step writers; run writers; tok writers
[ -f $E/judge/key.jsonl ] || { step packets; run packets; commit "Part D blind writers (4 subagents), judge packets"; }
step judges; run judges; tok judges
step labels; run labels
step build_items; run build_items
commit "Part D judges (4 subagent sessions), labels, duplicate controls, stack items (no labels / refs)"
if [ ! -f $E/RUN_COMMIT.txt ]; then
step freeze
( cd $W1 && { ls common/*.py common/*.sh spec/*.txt; echo $LANG_/partA_live/rows.jsonl; echo $LANG_/partD/set/items.jsonl; echo $LANG_/partD/set/truth.jsonl; } \
  | sort -u | xargs shasum -a 256 > $E/FROZEN_SHA_D.txt ) || fail "freeze sha"
shasum -a 256 $E/FROZEN_SHA_D.txt | cut -d' ' -f1 > $E/FREEZE_HASH.txt
python3 -B $C/gitc.py "Wave 1 $LANG_: Part D freeze (FROZEN_SHA_D, hash $(cat $E/FREEZE_HASH.txt))" $D $W1/common $W1/spec >/dev/null || fail "freeze commit"
FC=$(git -C $W1 rev-parse HEAD); echo $FC > $E/FREEZE_COMMIT.txt
git -C $W1 ls-tree -r --full-tree --name-only $FC translation-offline/wave1/$LANG_/partD/FROZEN_SHA_D.txt | grep -q FROZEN_SHA_D || fail "freeze commit missing file"
commit "Part D FREEZE_COMMIT $FC"
RC=$(git -C $W1 log -1 --format=%H -- $D); echo $RC > $E/RUN_COMMIT.txt
commit "Part D RUN_COMMIT $RC (the run opens at this tree + this file)"
fi
[ -z "$(git -C $W1 status --porcelain $D $W1/common $W1/spec)" ] || fail "tree dirty before open"
( cd $W1 && shasum -a 256 -c $E/FROZEN_SHA_D.txt > $E/frozen_check_open.txt 2>&1 ) || fail "frozen check before open"
echo "commits: freeze $(cat $E/FREEZE_COMMIT.txt) run $(cat $E/RUN_COMMIT.txt)"
step gemini; $PY gemini > $D/run.stdout.txt 2>&1 || { tail -5 $D/run.stdout.txt; fail "gemini run"; }
tail -1 $D/run.stdout.txt
step post; run post
tok post
echo "- $(date -u +%FT%TZ) Part D run done (partD/analysis/ANALYSIS.md)" >> $D/PROGRESS.md
commit "Part D run done, FINAL_RUN_DONE, analysis"
echo CHAIN_DONE

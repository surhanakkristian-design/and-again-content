#!/bin/bash
# Wave 1 per-language chain (brief Parts B-D): preflight (0 cost) -> [ua/es: rewrite pass 1 -> pass 2 -> final] ->
# projection -> set -> mock -> writers -> judges -> items -> freeze + commits -> ONE open of the set by the frozen
# stack -> post/analysis.  Any failure stops THIS language only (the others are separate processes).
#   nohup bash /abs/wave1/common/chain_w1.sh <lang> > /abs/wave1/<lang>/chain.log 2>&1 &
set -u
LANG_=$1
W1=/Users/kristiansurhanak/Projects/and-again-content/translation-offline/wave1
C=$W1/common; D=$W1/$LANG_; E=$D/partD
PY="python3 -B $C/pipeline_w1.py $LANG_"
export PYTHONDONTWRITEBYTECODE=1
commit(){ python3 -B $C/gitc.py "Wave 1 $LANG_: $1" $D >/dev/null 2>&1 || true; }
tok(){ python3 -B -c "import sys; sys.path.insert(0,'$C'); import pipeline_w1 as W; W.setlang('$LANG_'); t=W.spent(); W.tokens_md('- %s cumulative headless tokens after %s: %s' % (W.now(), '$1', format(t, ','))); print('TOKENS after $1:', format(t, ','))"; }
fail(){ echo "CHAIN FAIL: $* ($(date -u +%FT%TZ))" | tee -a $D/CHAIN_FAIL.txt; commit "chain stopped: $*"; exit 1; }
step(){ echo "== $1 $(date -u +%FT%TZ)"; }
mkdir -p $D
[ -f $D/partA/rows.jsonl ] || fail "Part A missing"
step preflight
python3 -B $C/test_w1.py > $D/test_w1_preflight.txt 2>&1 || fail "test_w1 (0 cost)"
tail -1 $D/test_w1_preflight.txt
if [ "$LANG_" = ua ] || [ "$LANG_" = es ]; then
  if [ ! -f $D/partB/rewritten.jsonl ]; then
    step rw_pass1; $PY rw_pass1 || fail "rewrite pass 1"; tok rw_pass1; commit "Part B rewrite pass 1"
    step rw_pass2; $PY rw_pass2 || fail "rewrite pass 2"; tok rw_pass2; commit "Part B rewrite pass 2"
    step rw_final; $PY rw_final || fail "rewrite final"; commit "Part B rewrite final (rewritten.jsonl)"
  fi
fi
step projection; $PY projection || fail "token projection over budget (Part D not started)"; tok projection
step make_set; $PY make_set || fail "make_set"
step mock; $PY mock > $D/mock_output.txt 2>&1 || fail "mock pipeline"; tail -1 $D/mock_output.txt
commit "Part D preflight, projection, fresh set + exclusion proof, mock pass"
step writers; $PY writers || fail "writers"; tok writers
commit "Part D blind writers (4 sessions)"
step packets; $PY packets || fail "packets"
step judges; $PY judges || fail "judges"; tok judges
step labels; $PY labels || fail "labels"
step build_items; $PY build_items || fail "build_items"
commit "Part D judges (4 sessions), labels, duplicate controls, stack items (no labels / refs)"
step freeze
( cd $W1 && { ls common/*.py common/chain_w1.sh spec/*.txt; echo $LANG_/partD/set/items.jsonl; echo $LANG_/partD/set/truth.jsonl; \
  [ -f $LANG_/partB/rewritten.jsonl ] && echo $LANG_/partB/rewritten.jsonl; } | sort -u | xargs shasum -a 256 > $E/FROZEN_SHA_D.txt ) || fail "freeze sha"
shasum -a 256 $E/FROZEN_SHA_D.txt | cut -d' ' -f1 > $E/FREEZE_HASH.txt
python3 -B $C/gitc.py "Wave 1 $LANG_: Part D freeze (FROZEN_SHA_D, hash $(cat $E/FREEZE_HASH.txt))" $D $W1/common $W1/spec >/dev/null || fail "freeze commit"
FC=$(git -C $W1 rev-parse HEAD); echo $FC > $E/FREEZE_COMMIT.txt
git -C $W1 ls-tree -r --name-only $FC translation-offline/wave1/$LANG_/partD/FROZEN_SHA_D.txt | grep -q FROZEN_SHA_D || fail "freeze commit missing file"
commit "Part D FREEZE_COMMIT $FC"
RC=$(git -C $W1 log -1 --format=%H -- $D); echo $RC > $E/RUN_COMMIT.txt
commit "Part D RUN_COMMIT $RC (the run opens at this tree + this file)"
[ -z "$(git -C $W1 status --porcelain $D $W1/common $W1/spec)" ] || fail "tree dirty before open"
( cd $W1 && shasum -a 256 -c $E/FROZEN_SHA_D.txt > $E/frozen_check_open.txt 2>&1 ) || fail "frozen check before open"
echo "commits: freeze $FC run $RC"
step gemini; $PY gemini > $D/run.stdout.txt 2>&1 || { tail -5 $D/run.stdout.txt; fail "gemini run"; }
tail -1 $D/run.stdout.txt
step post; $PY post || fail "post"
tok post
echo "- $(date -u +%FT%TZ) Part D run done (partD/analysis/ANALYSIS.md)" >> $D/PROGRESS.md
commit "Part D run done, FINAL_RUN_DONE, analysis"
echo CHAIN_DONE

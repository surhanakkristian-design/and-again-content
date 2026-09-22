#!/bin/bash
# Phase 2L S3 / Part E chain: preflight (0 cost) -> projection -> set -> mock -> writers -> judges -> items -> freeze +
# commits -> ONE open of the set by the frozen Czech stack -> post/analysis -> SHA after S3. Any failure stops the chain.
set -u
G="git -C /Users/kristiansurhanak/Projects/and-again-content"
ROOT=/Users/kristiansurhanak/Projects/and-again-content/translation-offline
P2L=$ROOT/phase2l; E=$P2L/partE
PY="python3 -B $E/pipeline.py"
export PYTHONDONTWRITEBYTECODE=1
commit(){ $G add translation-offline/phase2l >/dev/null 2>&1; $G commit -q -m "$1

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>" >/dev/null 2>&1 || true; }
fail(){ echo "CHAIN FAIL: $* ($(date -u +%FT%TZ))" | tee -a $E/CHAIN_FAIL.txt; commit "Phase 2L S3: Part E chain stopped: $*"; exit 1; }
step(){ echo "== $1 $(date -u +%FT%TZ)"; }
mkdir -p $E
step preflight
python3 -B $P2L/test_2l_cz.py > $E/test_2l_cz_output_S3.txt 2>&1 || { printf '# STOP E preflight\ntest_2l_cz.py failed; 0 cost.\n' > $P2L/STOP_E_tests.md; fail "test_2l_cz"; }
tail -2 $E/test_2l_cz_output_S3.txt
(cd $P2L && grep -v '^#' FROZEN_SHA_D.txt | shasum -a 256 -c - > $E/frozen_check_pre.txt 2>&1) || fail "frozen shasum -c (FROZEN_SHA_D)"
echo "frozen OK: $(grep -c ': OK' $E/frozen_check_pre.txt)"
step projection; $PY projection || fail "token projection over budget"
step make_set; $PY make_set || fail "make_set"
step mock; $PY mock > $E/mock_output.txt 2>&1 || fail "mock pipeline"; tail -1 $E/mock_output.txt
commit "Phase 2L S3: Part E preflight (test_2l_cz, frozen check), token projection, fresh Czech set + exclusion proof, mock pass"
step writers; $PY writers || fail "writers"
commit "Phase 2L S3: Part E blind writers (4 sessions)"
step packets; $PY packets || fail "packets"
step judges; $PY judges || fail "judges"
step labels; $PY labels || fail "labels"
step build_items; $PY build_items || fail "build_items"
commit "Phase 2L S3: Part E judges (4 sessions), labels, duplicate controls, stack items (no labels / refs)"
step freeze
(cd $P2L && grep -v '^#' FROZEN_SHA_D.txt | shasum -a 256 -c - > $E/frozen_check_open.txt 2>&1) || fail "frozen check before open"
(cd $P2L && { grep -v '^#' FROZEN_SHA_D.txt | awk '{print $2}'; echo partE/set/items.jsonl; echo partE/set/truth.jsonl; echo partE/pipeline.py; echo partE/chain.sh; } | sort -u | xargs shasum -a 256 > $E/FROZEN_SHA_E.txt) || fail "freeze sha"
shasum -a 256 $E/FROZEN_SHA_E.txt | cut -d' ' -f1 > $E/FREEZE_HASH.txt
commit "Phase 2L S3: Part E freeze (FROZEN_SHA_E, hash $(cat $E/FREEZE_HASH.txt))"
FC=$($G rev-parse HEAD); echo $FC > $E/FREEZE_COMMIT.txt
$G ls-tree -r --name-only $FC translation-offline/phase2l/partE/FROZEN_SHA_E.txt | grep -q FROZEN_SHA_E || fail "freeze commit missing file"
commit "Phase 2L S3: Part E FREEZE_COMMIT $FC"
RC=$($G rev-parse HEAD); echo $RC > $E/RUN_COMMIT.txt
commit "Phase 2L S3: Part E RUN_COMMIT $RC (run opens at this tree + this file)"
[ -z "$($G status --porcelain translation-offline/phase2l)" ] || fail "phase2l dirty before open"
echo "commits: freeze $FC run $RC"
step gemini; $PY gemini > $E/run.stdout.txt 2>&1 || { tail -5 $E/run.stdout.txt; fail "gemini run"; }
tail -1 $E/run.stdout.txt
step post; $PY post || fail "post"
step sha
zsh $ROOT/phase2i/sha_tree.sh | grep -v '  phase2l/' > $P2L/SHA_after_S3.txt
diff $P2L/SHA_before.txt $P2L/SHA_after_S3.txt > $P2L/SHA_diff_S3.txt; echo "sha diff lines: $(wc -l < $P2L/SHA_diff_S3.txt)"
echo "- $(date -u +%FT%TZ) S3: Part E run done (see partE/analysis/ANALYSIS.md)" >> $P2L/PROGRESS.md
commit "Phase 2L S3: Part E run done, FINAL_RUN_DONE, analysis, SHA after S3"
echo CHAIN_DONE

#!/bin/zsh
# Phase 2J S2 chain: tests -> freeze -> 43 new L3 calls -> A3 final. Absolute paths; STOP at 0 cost if tests fail.
P=/Users/kristiansurhanak/Projects/and-again-content/translation-offline; J=$P/phase2j
export PYTHONDONTWRITEBYTECODE=1
python3 -B $J/test_2j.py > $J/test_2j_output.txt 2>&1; rc=$?
tail -1 $J/test_2j_output.txt
if [ $rc -ne 0 ]; then printf '# STOP S2\n\ntest_2j.py failed (rc %s) - 0 model calls made. See test_2j_output.txt.\n' $rc > $J/STOP_S2.md; touch $J/S2_CHAIN_DONE; exit 1; fi
cd $J && shasum -a 256 run_2j.py run_2i_base.py test_2j.py stack_tonly.py stack_frozen.py f4fix.py adapter_2f.py write_guard.py tonly/*.py partA/a3_final.py > $J/FROZEN_SHA.txt
git -C /Users/kristiansurhanak/Projects/and-again-content add translation-offline/phase2j && git -C /Users/kristiansurhanak/Projects/and-again-content commit -q -m "Phase 2J S2: hook fix (gc sweep), verb-loss narrowing, run_2j + test_2j (12/12), 1S gate, freeze

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
git -C /Users/kristiansurhanak/Projects/and-again-content rev-parse HEAD > $J/FREEZE_COMMIT.txt; git -C /Users/kristiansurhanak/Projects/and-again-content add translation-offline/phase2j/FREEZE_COMMIT.txt; git -C /Users/kristiansurhanak/Projects/and-again-content commit -q -m "Phase 2J S2: FREEZE_COMMIT.txt

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
nohup python3 -B $J/run_2j.py gemini --set $P/phase2i/set/items.jsonl --run-dir $J/run_S2 --stage S2 --seed-ledger $P/phase2i/run/ledger.jsonl --expect-needed 43 --purpose "Phase 2J S2 A3 closed-set re-score (only the new L3 calls)" > $J/run_S2.stdout.txt 2>&1
echo RUN_RC=$?; cat $J/run_S2.stdout.txt | cut -c1-900
python3 -B $J/partA/a3_final.py
python3 -B $J/partA/make_report.py > /dev/null 2>&1; echo MAKE_REPORT_RC=$?
python3 -B - <<'PY'
import json
J='/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2j'; I='/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2i'
it={}
for l in open(I+'/set/items.jsonl',encoding='utf-8'):
    x=json.loads(l)
    if x['sid']==250: it[x['jid']]=x['answer']
k=json.load(open(J+'/partA/_run/reqkeys_fix1.json'))['requests']
c3=k.get('A:250:c3'); print('DIAG 250 answers', json.dumps(it,ensure_ascii=False)); print('DIAG c3 key shared with', [j for j,v in k.items() if v==c3])
PY
cd $P && zsh $P/phase2i/sha_tree.sh | grep -v '  phase2j/' > $J/SHA_after_S2.txt
diff $J/SHA_before.txt $J/SHA_after_S2.txt > $J/SHA_diff_S2.txt; echo SHA_DIFF_LINES=$(wc -l < $J/SHA_diff_S2.txt) FILES=$(wc -l < $J/SHA_after_S2.txt)
touch $J/S2_CHAIN_DONE

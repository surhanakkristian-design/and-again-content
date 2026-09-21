#!/bin/zsh
P=/Users/kristiansurhanak/Projects/and-again-content/translation-offline; J=$P/phase2j; B=$J/partB; G="git -C /Users/kristiansurhanak/Projects/and-again-content"
export PYTHONDONTWRITEBYTECODE=1
stop() { printf '# STOP S5\n\n%s (0 further model calls).\n' "$1" > $J/STOP_S5.md; echo "STOP: $1"; }
python3 -B $B/b3.py selftest > $B/s5_selftest.txt 2>&1 || { stop "b3 selftest failed, see partB/s5_selftest.txt"; }
if [ ! -f $J/STOP_S5.md ]; then python3 -B $B/b3.py build > $B/s5_build.txt 2>&1 || stop "b3 build failed, see partB/s5_build.txt"; fi
if [ ! -f $J/STOP_S5.md ]; then python3 -B $J/test_2j.py > $J/test_2j_output_S5.txt 2>&1 || stop "test_2j failed, see test_2j_output_S5.txt"; tail -1 $J/test_2j_output_S5.txt; fi
if [ ! -f $J/STOP_S5.md ]; then
  cd $J && shasum -a 256 run_2j.py run_2i_base.py test_2j.py stack_tonly.py stack_frozen.py f4fix.py adapter_2f.py write_guard.py tonly/*.py partA/a3_final.py partB/b3.py partB/lever3.py > $J/FROZEN_SHA_S5.txt
  git -C /Users/kristiansurhanak/Projects/and-again-content add translation-offline/phase2j; git -C /Users/kristiansurhanak/Projects/and-again-content commit -q -m "Phase 2J S5: B2 audit results, B3 corrections + upload files, T17, re-freeze (test file + b3)

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
  git -C /Users/kristiansurhanak/Projects/and-again-content rev-parse HEAD > $J/FREEZE_COMMIT_S5.txt
  python3 -B $J/run_2j.py gemini --set $B/b4/items_B4.jsonl --run-dir $B/b4/probe --stage S5probe --seed-ledger $B/b4/seed_ledger.jsonl --expect-needed 999999 --purpose "Phase 2J S5 B4 probe (expect mismatch, 0 calls)" > $B/b4/probe.stdout.txt 2>&1
  N=$(python3 -B -c "import json;print(json.load(open('$B/b4/probe/RUN_STATUS.json'))['needed'])" 2>/dev/null); echo NEEDED=$N
  if [ -z "$N" ]; then stop "B4 probe gave no needed count, see partB/b4/probe.stdout.txt";
  elif [ "$N" -gt 300 ]; then stop "B4 needs $N new L3 calls > 300 (Part D reserve)";
  else
    nohup python3 -B $J/run_2j.py gemini --set $B/b4/items_B4.jsonl --run-dir $B/b4/run --stage S5 --seed-ledger $B/b4/seed_ledger.jsonl --expect-needed $N --purpose "Phase 2J S5 B4 closed-set re-score A+B (only new L3 calls)" > $B/b4/run.stdout.txt 2>&1
    echo RUN_RC=$?; head -c 700 $B/b4/run.stdout.txt; echo
    python3 -B $B/b3.py score > $B/s5_score.txt 2>&1; cat $B/s5_score.txt | cut -c1-600
  fi
fi
cd $P && zsh $P/phase2i/sha_tree.sh | grep -v '  phase2j/' > $J/SHA_after_S5.txt
diff $J/SHA_before.txt $J/SHA_after_S5.txt > $J/SHA_diff_S5.txt; echo SHA_DIFF_LINES=$(wc -l < $J/SHA_diff_S5.txt) FILES=$(wc -l < $J/SHA_after_S5.txt)
python3 -B - <<'PY'
import json, os
J='/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2j'; B=J+'/partB'
led=json.load(open(J+'/GEMINI_LEDGER.json')); cum=sum(v for v in led.values() if isinstance(v,int))
dd=json.load(open(B+'/audit/DRIVER_DONE.json')); hl=sum(dd.get('per_session_tokens',{}).values())
r=json.load(open(B+'/B3_result.json')) if os.path.exists(B+'/B3_result.json') else {}
b4=json.load(open(B+'/b4/B4.json')) if os.path.exists(B+'/b4/B4.json') else None
f=lambda x:'%d/%d = %.2f %% [%.2f, %.2f]'%(x['x'],x['n'],x['pct'],x['cp95'][0],x['cp95'][1])
b2=r.get('b2',{}); b3=r.get('b3',{}); ag=r.get('b1_agreement',{})
L=['','## S5 - B2 summary, B3 corrections, B4 closed-set re-score (21.9.2026)']
if os.path.exists(J+'/STOP_S5.md'): L.append('- STOP: '+open(J+'/STOP_S5.md').read().strip().replace('\n',' '))
if b2: L+=['- B2 driver ended on the token cap before wave 9: %d/4,064 SK rows audited (%d refs), packets p032-p040 not audited; COVERAGE.json = the audited ids (Part D samples only from these). Per ref all: %s.'%(b2['coverage']['n_audited'],b2['coverage']['refs_audited'],json.dumps(b2['per_ref']['all'])),
  '- B1 agreement: B1 SK flags %d, audited %d, B2=W %d, any B2 flag %d; B2 W refs %d of which B1-flagged %d.'%(ag['b1_sk_flags'],ag['b1_audited'],ag['b1_audited_B2_W'],ag['b1_audited_B2_any_flag'],ag['b2_W_refs'],ag['b2_W_also_b1_flag'])]
if b3: L+=['- B3 (partB/b3.py, T17 in test_2j): SK rows changed %d, v[0] changed %d (en = v[0] kept), CZ 0 (all B1 CZ flags listed). Counts: %s. Upload: phase2j/upload/ (+ B3_diff.jsonl, UPLOAD_README.md). Re-freeze: FROZEN_SHA_S5.txt, FREEZE_COMMIT_S5.txt (stack code unchanged; test_2j + b3 added).'%(b3['rows_changed_sk'],len(b3['v0_changed_rows']),json.dumps(b3['counts']))]
if b4: L+=['- B4 CLOSED-SET RE-SCORE A+B: coverage %s, FA %s (A3 %s / %s; 2I %s / %s); changed vs A3 %d, vs 2I %d; run %s. Detail partB/PART_B.md, partB/b4/B4.json.'%(f(b4['A_plus_B']['coverage']),f(b4['A_plus_B']['fa']),f(b4['A3']['coverage']),f(b4['A3']['fa']),f(b4['2I']['coverage']),f(b4['2I']['fa']),len(b4['changed_vs_A3']),len(b4['changed_vs_2I']),json.dumps(b4['run_status']))]
L+=['- Gemini calls: S5 %s, cumulative %d of 1,200 (GEMINI_LEDGER.json %s).'%(led.get('S5',0),cum,json.dumps(led)),
    '- Headless tokens: B2 total %d (S4 recorded 177,611 at return; S5 adds %d from the driver); S5 itself 0; cumulative headless %d.'%(hl,hl-177611,hl),
    '- SHA check S5: SHA_diff_S5.txt %d lines.'%sum(1 for _ in open(J+'/SHA_diff_S5.txt')),
    '- NEXT (S6): Part D samples from the CORRECTED phase2j/upload/annotations_sk_fixed.jsonl, only audited ids (COVERAGE.json), excluding 2F-probe 60 + 2I 100.']
open(J+'/PROGRESS.md','a',encoding='utf-8').write('\n'.join(L)+'\n')
open(J+'/TOKENS.jsonl','a').write(json.dumps({'stage':'S5','headless_tokens':hl-177611,'agent_est':170000,'note':'B2 driver remainder after S4 return; B2 total %d'%hl})+'\n')
print('\n'.join(L))
PY
git -C /Users/kristiansurhanak/Projects/and-again-content add translation-offline/phase2j; git -C /Users/kristiansurhanak/Projects/and-again-content commit -q -m "Phase 2J S5: B4 closed-set re-score, PART_B.md, SHA, progress

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"; git -C /Users/kristiansurhanak/Projects/and-again-content log --oneline -2
touch $J/partB/S5_CHAIN_DONE

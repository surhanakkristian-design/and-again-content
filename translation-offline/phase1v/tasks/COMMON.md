Common rules for every Phase 1V agent
- Base dir: ~/Projects/and-again-content/translation-offline (below: TO). Phase dir: TO/phase1v.
- Full brief: TO/phase1v/tasks/BRIEF_1V.md (read it first). Prior evidence you may read: 
  ~/Projects/and-again/docs/features/reports/TRANSLATION_OFFLINE_PHASE1U_REPORT.md, TO/phase1u/, TO/phase1t/taskB/,
  plus the code modules those import (follow imports; do not browse other phase reports).
- Do NOT modify any earlier phase dir. New code/data only under your own TO/phase1v/<track> dir.
- HARD LIMIT: 12 of your own tool calls. Batch work into large scripts. At 12, stop and report.
- No DB writes, no app code change, no deploy, no migration, no git push.
- Gemini: gemini-3.1-flash-lite, temperature 0, thinkingBudget 0; reuse the existing runner/ledger
  code (runner_1p.py and its call ledger conventions: counted = http 200 only; retries counted:false;
  empty/unparsable 200 = FAILED, counted, never retried). Key/config: whatever the 1U runner uses.
- Write your section of the report to TO/phase1v/<track>/SECTION.md: every lettered item with its
  result or "not done", exact numbers, Clopper-Pearson intervals where rates are given.
- Final message back: <=15 lines: key numbers, model calls (counted/failed/retried), spend, your
  harness tool-call count, any STOP triggered, paths.

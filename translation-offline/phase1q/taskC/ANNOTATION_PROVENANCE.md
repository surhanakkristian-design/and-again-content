# Phase 1Q Task C - reference annotation provenance

Date: 2026-09-19. Agent: phase1q_taskC_annotator (single, blind). Model/API calls: 0.

## Validation
- sids present: 120/120 (keys are the sids exactly as in sentences.json: 170001..170120; the brief's "1P001..1P120" refers to the same 120 rows)
- missing sids: none ; unexpected sids: none
- every `v` non-empty: PASS (offenders: none)
- `lk` parallel to `v` (equal length, non-empty): PASS (offenders: none)
- field set exactly {v, lk, alt, voice_sk, agent_nom, tf_gold, tense_open, perfective_present}: PASS (offenders: none)
- voice_sk in {active_agent, passive, impersonal}: PASS (offenders: none)
- tf_gold equality with sentences.json tags.tf_gold: PASS, 120/120 equal (mismatches: none)
- total renderings: 248 ; MEAN renderings per sentence: 2.07 (1N reference: 2.37)
- sids with fewer than 2 renderings: none

## tf_gold disagreements (value kept as the writer's, flagged only)
- 170099 "Sef lutuje, ze on vlani zrusil tu spolupracu..." - the matrix verb is PRESENT (regrets); only the
  complement clause is past. Gold "past" kept unchanged.
- 170066 and 170085 are labelled past / present respectively while the natural English is a present
  perfect / present perfect continuous; both are defensible under the LEVEL-1 time-frame rule, so they
  are NOT counted as disagreements.

## Files opened by this agent (the complete list)
1. translation-offline/phase1p/data/sentences.json  (the 120 Slovak sentences: sid, slovak, level, topic, tags)
2. translation-offline/phase1n/tasks/JUDGE_BRIEF_1N.md  (the 1N annotation/judging instructions, followed unchanged)
3. translation-offline/phase1n/data/annotations_part1.json  (first ~6 KB only, FORMAT/STYLE exemplar)
4. translation-offline/phase1p/access_log.jsonl  (tail -2, to copy the line shape)
`ls` was run on translation-offline/phase1n/tasks/ only. Nothing else on disk was opened or listed.

## Blindness statement
Every rendering in annotations_src.json was derived from the Slovak sentence alone. This agent never
opened, read or inferred from phase1p/data/items.json, any writer_*.json, phase1p/judge/,
phase1p/data_backup/, phase1p/recovery/, phase1p/dev/, phase1q/ (other than writing this file), any
packet, any label file or any report, and ran no project script. No model/API call was made (0 calls).

## Output
- translation-offline/phase1p/data/annotations_src.json (flat, key = sid)
- parts: annotations_src_part1..4.json (30 sentences each)

# JUDGE_TASK_1U — your whole task (Phase 1U)

You are the blind judge. Read ONLY the files named below; open nothing else and do not search the repository.

1. Read the brief: `/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase1u/set/judge/JUDGE_BRIEF_1U.md`

2. Then, for each part K = 1..4 in order: read the packet part, judge every item in it, and IMMEDIATELY write its verdict file before reading the next part.

   - part 1 — packet `/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase1u/set/judge/packet_part1.jsonl` (245 items) → verdicts `/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase1u/set/judge/verdicts_part1.json`
   - part 2 — packet `/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase1u/set/judge/packet_part2.jsonl` (245 items) → verdicts `/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase1u/set/judge/verdicts_part2.json`
   - part 3 — packet `/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase1u/set/judge/packet_part3.jsonl` (245 items) → verdicts `/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase1u/set/judge/verdicts_part3.json`
   - part 4 — packet `/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase1u/set/judge/packet_part4.jsonl` (245 items) → verdicts `/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase1u/set/judge/verdicts_part4.json`

3. Each packet part is JSON Lines: one object per line with `id`, `slovak` (the Slovak sentence) and `answer` (the learner's English). Nothing else exists about an item — no reference translation, no intent, no tags.

4. Each verdict file is a JSON LIST, one object per packet item, in packet order, in the format of the brief:

```json
{"id": "Q0001", "label": "correct"|"wrong", "type": null|"T"|"W"|"M"|"S",
 "borderline": true|false, "confidence": 1|2|3|4|5,
 "dropped": "<Slovak = English of what is missing, or empty>",
 "passive": null|"by"|"agentless", "agent_drop": null|"main"|"fronted"|"other"|"both", "note": "<= 12 words, optional"}
```

   MANDATORY on EVERY item: `id`, `label`, `borderline`, `confidence` (integer 1-5), `dropped`. `type` is mandatory whenever `label` is `"wrong"` and must be `null` when `label` is `"correct"`. An item without `confidence` cannot be scored and the join will refuse the whole run.

5. Judge every item; never skip one; never leave a file half-written. Some items look alike on purpose — judge each on its own, never try to be consistent with a remembered earlier item or to balance your verdicts.

6. BUDGET: at most 12 tool calls in total. One Read per packet part, one Write per verdict file, one Read for the brief — that is 9; the rest is your margin. Do not list directories, do not re-read what you have read.

Total items: 980.

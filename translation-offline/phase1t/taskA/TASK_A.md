# Phase 1T / Task A — AG v3 (deterministic, 0 model calls)

Work dir: ~/Projects/and-again-content/translation-offline. Write ONLY under phase1t/taskA/. Never modify any other phase dir.
No Gemini / network calls. Budget: about 12 tool calls — work in a few large scripts, not many small probes.

## Read
- phase1s/taskC/agent_drop_v2.py (AG v2, the base), phase1s/taskC/ag_apply.py, phase1s/taskC/rescore_1s_c.py (how AG is applied and scored)
- phase1s/taskC/judge/packet.json + verdicts.json + phase1s/taskC/_key.json (the 183-item blind-judge packet: 98 agentless, 42 by-passive controls, 40 plain controls, 3 AG misfires)
- phase1p/data/sentences.json, annotations.json, items.json (source data the scripts load)
- phase1s/taskA/RESCORE_1S_A.md only if you need the list of AG hits.

## Build phase1t/taskA/agent_drop_v3.py (copy of v2 + these fixes, each one separately switchable by a flag so catches and costs can be attributed)
1. CLAUSE-AWARE. AG v2 inspects only the main clause. Split the Slovak into clauses (comma + subordinator/coordinator: že, keď, keďže, lebo, pretože, hoci, kým, ak, aby, ktorý/-á/-é/-ú/-í…, a, ale, …) and the English answer into clauses (that, when, because, since, although, while, if, which, who, and, but, …). Match each Slovak clause to its English counterpart (by order, falling back to lexical anchors from the reference's clause split). Apply the AG test PER CLAUSE: a Slovak clause with an explicit nominative agent of an active verb whose English counterpart clause is a marked passive with no by-agent and does not render the agent as its subject → REJECT. Known misses to catch: C:170094, 170062, 170099, 170074, 170083, 170118, 170086, 170071 (the iids are of the form C:<sid>:cN — find the exact ones in the packet key).
   The same clause-awareness must REMOVE the 6 misfires outside the agentless tag (sid 170114 ×5, C:170092:c4; 3 of them judged correct): a passive in clause X must not be charged with the agent of clause Y.
2. SUBJECT-NP LOOKUP. v2's annotation lookup fails to find the subject NP for Jana, Zuzana, tréner, Ministerstvo, mesto (C:170019, 170061, 170063, 170117, 170093, 170104) and for pronouns (C:170057, 170014, 170089). Find out WHY for each (print the annotation + writer_tags for those sids) and fix the reader generally, not by listing these words. If the annotation truly lacks the field, derive the nominative subject from the Slovak surface per clause (first NP before the finite verb that is not governed by a preposition; pronouns from SK_PRON) and say so.
3. INSTRUMENT ≠ AGENT. "by bike" was read as a by-agent (C:170077:c3). A by-phrase counts as the agent only if its object can be the agent of the verb: it must render the Slovak nominative agent (PRON_EQ / reference subject NP head / proper name) — not any "by X". "by bike/car/bus/train/hand/email/post/phone/mistake/then/now/<time>" etc. never count.
Keep every v2 abstain path (Slovak passive, reflexive passive, subjectless, non-passive answer). Never read the writers' ITEM tags.

## Pre-flight
Synthetic rows FIRST (extend v2's 13 rows with: embedded-clause agent drop, embedded clause passive whose agent is kept with by, passive in a clause whose Slovak counterpart is subjectless while ANOTHER clause has an agent, "by bike", proper-name agent, pronoun agent in a že-clause, a by-passive control, a plain active control). All must pass before scoring.

## Regression gate on the 1S judge packet (183 items, judged labels)
Report for v2 and for v3 (and for each flag alone on top of v2):
- catches among the 97 judged agent drops (list every remaining miss with Slovak + answer + why)
- rejections among the 42 by-passive controls (must be 0) and the 39 judged-correct plain controls (must be 0), and among the 3 judged-correct misfire rows (should be 0)
- then over ALL 1,080 items of the 1Q set with the RUL′ labels as in phase1s/taskC (K3 stack with AG v3 instead of v2): coverage k/n, FA k/n, agentless FA k/n, with exact Clopper-Pearson 95 % intervals; list every judged-correct item AG v3 rejects (MEASURED COST) and every new catch. Remember AG sits before L3: an AG reject overrides a stored L3 accept; an AG abstain falls through to the stored verdict.
SELECT on measured cost (judged-correct answers rejected), never on agreement with gold assertions. This 1Q set is DESIGN-only; say so in the output.

## Output
phase1t/taskA/agent_drop_v3.py, preflight_v3.py, regress_v3.py, AG_V3_REGRESSION.json (use phase1s/safe_json.safe_dump), AG_V3_REGRESSION.md (tables above, ≤ 120 lines).
Final message to me: ≤ 15 lines — the catch/cost table, remaining misses, any defect you could not fix, and your tool-call count.

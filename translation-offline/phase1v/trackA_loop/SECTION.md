# Phase 1V — Track A loop (A1, A2, A3) — closed sets only, 0 model calls

19 September 2026. **Model calls: 0 counted, 0 failed, 0 retried; spend $0.00** (0 of the 200-call loop budget). No fresh-set file was read (`trackA_set` untouched). Nothing frozen or committed; no earlier phase dir modified. Files: `stack_1v.py` (AG v5 + TIP rule + scoring entry point), `loop_1v.py`, `rounds.json`, `ROUNDS.md`, `STACK_1V.json`.

**Baseline disclosure.** 1U closed = stored 1U run rows (the 1U stack itself). 1T closed = stored 1T run verdicts with AG v4 substituted (v4 turned 7 stored accepts into rejections); only 80 1T items were ever probed with the 1U prompt, so the 1T L3 verdicts are the 1T stack's, not the 1U prompt's. The 1T baseline (389/421, 9/479) is therefore a proxy, not a re-run.

## A1 — AG misses behind the 9 type-M false accepts of 1U: DONE (partial fix)
Classification (writer tag / mechanism):
| item | tag | mechanism | deterministic fix |
|---|---|---|---|
| W:190052:w2 | fronted | nominalisation ("During the explanation of …") | rs_nom — FIXED |
| W:190054:w2 | fronted | nominalisation ("Because of the cancellation of …") | rs_nom — FIXED |
| W:190086:w2 | misaligned | nominalisation ("about the cancellation of …") | rs_nom — FIXED |
| W:190057:w1 | fronted | by-phrase read past the comma ("by email client replied") | rs_pass — not selected |
| W:190036:w2 | misaligned | get-passive, clause count mismatch, read as pro-drop | rs_pass — not selected |
| W:190038:w2 | misaligned | reduced relative + locative "by the river" | rs_pass — not selected |
| W:190090:w1 | main | locative "by the lake" read as by-agent | rs_pass — not selected |
| W:190091:w1, w2 | main | pronoun agent `my`; "clinical" read as rendered subject | rs_pass — not selected |

Fix = `refsubj` patch, applied only where AG v4 does not fire (v4 runs first, unchanged): a subject of an active reference clause (pronoun only when the Slovak has an overt pronoun) appears nowhere in the answer, AND the answer has (rs_pass) a be/get + participle, or (rs_nom) a nominalisation "the X-tion/-ment/-ance/-al of".
Candidates, **selected on measured cost** (extra cost vs v4 must be 0 on both closed sets):
| config | 1S gate (drops / by-passive / plain) | 1U fires / catches / cost | 1T fires / catches / cost | eligible |
|---|---|---|---|---|
| rs_pass | 97/97 · 0/42 · 0/39 PASS | 9 / 9 / 0 | 8 / 6 / **2** (C:180063:c2, C:180068:c3) | no |
| **rs_nom** | 97/97 · 0/42 · 0/39 PASS | 4 / 4 / 0 | 0 / 0 / 0 | **yes — chosen** |
| rs_pass+rs_nom | 97/97 · 0/42 · 0/39 PASS | 13 / 13 / 0 | 8 / 6 / 2 | no |
AG v5 total cost on the closed sets = v4's (W:190081:w2 only); not made worse. rs_nom also 0/3 on the 1S v2-misfire rows (rs_pass 1/3).

## A2 — determiner-free rule
- **(a) L3 PROMPT line: NOT DONE** — not built and not measured; 0 model calls spent. The 6 plain-L3 determiner false rejections of 1U (C:190009:c2, C:190028:c2, C:190039:c2, C:190059:c2, C:190084:c2, C:190094:c2) remain.
- **(b) TIP-path rule: DONE.** Overturns `L3:TIPrej` when the answer differs from the reference only by a determiner SWAP (a/an/the/this/that/these/those/possessives; no deletion, so a missing article is never overturned) and the Slovak has no demonstrative (ten/tá/to/tie/tieto and their forms). Measured alone: **1U gain 8 judged-correct, cost 0 judged-wrong** (of 29 TIPrej); gained C:190022:c2, C:190023:c2, C:190025:c2 (skp tag), C:190034:c2, C:190042:c2, C:190043:c2, C:190044:c2, C:190055:c2; C:190067:c2 ("all of those" vs "all the") not overturned. **1T gain 5, cost 0** (of 77 TIPrej): C:180002:c2, C:180020:c2, C:180054:c2, C:180057:c2, C:180075:c2.

## A3 — bounded loop (closed 1T + 1U, 0 calls)
| round | fix | set | coverage | FA | FA T | FA W | FA M | FA S | status |
|---|---|---|---|---|---|---|---|---|---|
| 0 | baseline | 1U | 382/402 = 95.02 % [92.42, 96.93] | 16/498 = 3.21 % [1.85, 5.17] | 4/120 | 1/120 | 9/159 | 2/99 | — |
| 0 | baseline | 1T | 389/421 = 92.40 % [89.44, 94.74] | 9/479 = 1.88 % [0.86, 3.54] | 1/119 | 0/72 | 6/209 | 2/79 | — |
| 1 | AG v5 rs_nom | 1U | 382/402 = 95.02 % [92.42, 96.93] | 13/498 = 2.61 % [1.40, 4.42] | 4/120 | 1/120 | 6/159 | 2/99 | kept |
| 1 | AG v5 rs_nom | 1T | 389/421 = 92.40 % [89.44, 94.74] | 9/479 = 1.88 % [0.86, 3.54] | 1/119 | 0/72 | 6/209 | 2/79 | kept |
| 2 | TIP determiner rule | 1U | 390/402 = 97.01 % [94.84, 98.45] | 13/498 = 2.61 % [1.40, 4.42] | 4/120 | 1/120 | 6/159 | 2/99 | kept |
| 2 | TIP determiner rule | 1T | 394/421 = 93.59 % [90.81, 95.73] | 9/479 = 1.88 % [0.86, 3.54] | 1/119 | 0/72 | 6/209 | 2/79 | kept |
| 3 | A2(a) prompt line | — | — | — | — | — | — | — | NOT RUN |
Per-guard cost: AG v5 extra cost 0 / 0 (1U / 1T); TIP rule cost 0 / 0. FA type M on 1U 9/159 = 5.66 % → 6/159 = 3.77 % [1.40, 8.03]. Gains on the attacked metric: round 1 FA −0.60 pt (1U) / 0 (1T); round 2 coverage +1.99 / +1.19 pt. Stop rules checked every round (worse cell by point, cost > 2, two consecutive rounds < 1 pt, 200-call budget): **none triggered**; no round reverted. All per-tag cells in `rounds.json`.
Caveat: both fixes were designed while looking at the 1U items they fix; the 1U gains are in-sample. 1T (for A1) and the fresh set of A4 are the only out-of-sample checks.

## Frozen candidate
`STACK_1V.json` = the 1U frozen modules (MODULES_1U.txt, unchanged L3 prompt) + `stack_1v.py` with `extra=("rs_nom",)` and `tip=True`; entry point `stack_1v.final_accept(row, extra=("rs_nom",), tip=True)`, run after the 1U runner, 0 calls.

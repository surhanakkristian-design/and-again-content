# Phase 1W §3 result: A2(a) L3 determiner prompt line, loop round 3 on closed 1U + 1T (IN-SAMPLE, not a result)

- Decision: **REVERT**
- Stop rules triggered: ["a worse cell: {'1U': ['coverage', 'cov:determiner', 'cov:skp-passive'], '1T': ['coverage', 'cov:determiner', 'cov:skp-passive']}"]
- Stack entry for §4: translation-offline/phase1w/stack_1w.py (1V round 2 + s2), unchanged prompt; s3 REVERTED
- Model calls counted (http 200): 194
- Model calls uncounted (http 0/429/5xx retries): 0
- Model calls FAILED (empty/unparsable 200): 0
- Loop budget: 194 of 200
- Spend (list price, tokens in 131584 / out 194): $0.03319; key tiers {'single-key(default)': 194}; switched to paid at None
- Call log: translation-offline/phase1w/s3/run/calls.jsonl
- Prompt line (inserted per record only where answer vs reference differ in determiner tokens alone, after the last inserted line, before the tail): "Determiners: Slovak has no articles, so where the learner sentence differs from the reference only in a determiner, judge that point like this. A different article (a / an / the), or no article where English allows none, is SAME on that point; an article English grammar requires that is simply left out stays DIFF. A demonstrative (this, that, these, those) that the learner adds, drops or uses instead of an article or a possessive is DIFF only where the Slovak itself has a demonstrative at that point (ten, tá, to, tie, tieto or another form of them); where the Slovak has none, it is SAME on that point. A possessive (my, our, his, her, their) used instead of an article where the Slovak context makes it natural is SAME on that point."
- 1U reached L3 (non-AG): 601; triggered/re-called: 154; not in build: 0
- 1U replay check (stored model verdict reproduces stored layer): {'ok': 601}
- 1U old-prompt hash reproduction on triggered items: {'match': 154}
- 1T reached L3 (non-AG): 546; triggered/re-called: 40; not in build: 0
- 1T replay check (stored model verdict reproduces stored layer): {'ok': 546}
- 1T old-prompt hash reproduction on triggered items: {'no_stored_hash': 40}

## Per set, per cell (before = 1V round 2 + §2; after = + §3 line)
- 1U coverage before: 390/402 = 97.01 % [94.84, 98.45]
- 1U coverage after: 376/402 = 93.53 % [90.67, 95.73]
- 1U FA before: 13/498 = 2.61 % [1.40, 4.42]
- 1U FA after: 13/498 = 2.61 % [1.40, 4.42]
- 1U FA type M: 6/159 -> 6/159
- 1U FA type S: 2/99 -> 2/99
- 1U FA type T: 4/120 -> 4/120
- 1U FA type W: 1/120 -> 1/120
- 1U cell cells: {"FA:agreement": {"k": 0, "n": 1, "pct": 0.0, "ci": [0.0, 97.5]}, "cov:aspect": {"k": 27, "n": 27, "pct": 100.0, "ci": [87.23, 100.0]}, "cov:by-passive": {"k":  -> {"FA:agreement": {"k": 0, "n": 1, "pct": 0.0, "ci": [0.0, 97.5]}, "cov:aspect": {"k": 27, "n": 27, "pct": 100.0, "ci": [87.23, 100.0]}, "cov:by-passive": {"k": 
- 1U worse cells: ['coverage', 'cov:determiner', 'cov:skp-passive']
- 1U guard cost (judged-wrong newly accepted): 1 ['W:190089:w4']
- 1U flips: {"loss_correct": ["C:190021:c2", "C:190022:c2", "C:190025:c2", "C:190034:c2", "C:190043:c2", "C:190051:c2", "C:190058:c2", "C:190070:c2", "C:190076:c2", "C:190080:c2", "C:190081:c2", "C:190083:c2", "C:190088:c2", "C:190092:c2", "C:190099:c2", "C:190100:c2"], "gain_correct": ["C:190028:c2", "W:190088:w4"], "catch_wrong_rejected": ["W:190061:w4"], "COST_wrong_accepted": ["W:190089:w4"]}
- 1U coverage gain: -3.48 pt
- 1T coverage before: 394/421 = 93.59 % [90.81, 95.73]
- 1T coverage after: 388/421 = 92.16 % [89.17, 94.54]
- 1T FA before: 9/479 = 1.88 % [0.86, 3.54]
- 1T FA after: 9/479 = 1.88 % [0.86, 3.54]
- 1T FA type M: 6/209 -> 6/209
- 1T FA type S: 2/79 -> 2/79
- 1T FA type T: 1/119 -> 1/119
- 1T FA type W: 0/72 -> 0/72
- 1T cell cells: {"FA:agentdrop-embedded": {"k": 5, "n": 96, "pct": 5.21, "ci": [1.71, 11.74]}, "FA:agentdrop-main": {"k": 1, "n": 65, "pct": 1.54, "ci": [0.04, 8.28]}, "cov:asp -> {"FA:agentdrop-embedded": {"k": 5, "n": 96, "pct": 5.21, "ci": [1.71, 11.74]}, "FA:agentdrop-main": {"k": 1, "n": 65, "pct": 1.54, "ci": [0.04, 8.28]}, "cov:asp
- 1T worse cells: ['coverage', 'cov:determiner', 'cov:skp-passive']
- 1T guard cost (judged-wrong newly accepted): 0 []
- 1T flips: {"loss_correct": ["C:180028:c2", "C:180031:c2", "C:180054:c2", "C:180057:c2", "C:180066:c2", "C:180070:c2", "C:180075:c2"], "gain_correct": ["W:180026:w5"]}
- 1T coverage gain: -1.43 pt

## The 6 target items (1U plain-L3 determiner false rejections)
- C:190009:c2: triggered True, L3 DIFF -> DIFF, final reject (L3)
- C:190028:c2: triggered True, L3 DIFF -> SAME, final ACCEPT (L3)
- C:190039:c2: triggered True, L3 DIFF -> DIFF, final reject (L3)
- C:190059:c2: triggered True, L3 DIFF -> DIFF, final reject (L3)
- C:190084:c2: triggered True, L3 DIFF -> DIFF, final reject (L3)
- C:190094:c2: triggered True, L3 DIFF -> DIFF, final reject (L3)

## Caveats
- Closed sets, IN-SAMPLE: the line was written looking at the 6 1U targets.
- 1T is re-called under ITS OWN prompt (P-FROZEN-1P) + the line; 1U under P-FROZEN-1U + the line: each is a one-line change from the stored stack.
- The possessive sentence of the line goes beyond the owner wording (article + demonstrative); 2 of the 6 targets are possessive (028 my, 059 our).
- A FAILED call is scored as a rejection (never guessed).

## Every cell, one per line (before -> after)
- 1U FA:agreement: 0/1 = 0.00 % -> 0/1 = 0.00 %
- 1U FA:drop-fronted: 1/63 = 1.59 % -> 1/63 = 1.59 %
- 1U FA:drop-main: 3/48 = 6.25 % -> 3/48 = 6.25 %
- 1U FA:drop-misaligned: 2/48 = 4.17 % -> 2/48 = 4.17 %
- 1U FA:missing-article: 2/97 = 2.06 % -> 2/97 = 2.06 %
- 1U FA:preposition: 0/1 = 0.00 % -> 0/1 = 0.00 %
- 1U FA:time-frame: 4/120 = 3.33 % -> 4/120 = 3.33 %
- 1U FA:wrong-word: 1/120 = 0.83 % -> 1/120 = 0.83 %
- 1U cov:aspect: 27/27 = 100.00 % -> 27/27 = 100.00 %
- 1U cov:by-passive: 79/80 = 98.75 % -> 79/80 = 98.75 %
- 1U cov:determiner: 52/59 = 88.14 % -> 40/59 = 67.80 %  (WORSE)
- 1U cov:drop-fronted: 0/1 = 0.00 % -> 0/1 = 0.00 %
- 1U cov:missing-article: 0/1 = 0.00 % -> 1/1 = 100.00 %
- 1U cov:paraphrase: 102/103 = 99.03 % -> 102/103 = 99.03 %
- 1U cov:plain: 80/80 = 100.00 % -> 80/80 = 100.00 %
- 1U cov:skp-passive: 62/63 = 98.41 % -> 57/63 = 90.48 %  (WORSE)
- 1T FA:agentdrop-embedded: 5/96 = 5.21 % -> 5/96 = 5.21 %
- 1T FA:agentdrop-main: 1/65 = 1.54 % -> 1/65 = 1.54 %
- 1T FA:aspect: 1/1 = 100.00 % -> 1/1 = 100.00 %
- 1T FA:number: 0/12 = 0.00 % -> 0/12 = 0.00 %
- 1T FA:plain: 1/186 = 0.54 % -> 1/186 = 0.54 %
- 1T FA:skp-passive: 1/1 = 100.00 % -> 1/1 = 100.00 %
- 1T FA:timeframe: 1/119 = 0.84 % -> 1/119 = 0.84 %
- 1T cov:aspect: 59/61 = 96.72 % -> 59/61 = 96.72 %
- 1T cov:by-passive: 47/47 = 100.00 % -> 47/47 = 100.00 %
- 1T cov:by-passive-embedded: 33/33 = 100.00 % -> 33/33 = 100.00 %
- 1T cov:determiner: 72/79 = 91.14 % -> 65/79 = 82.28 %  (WORSE)
- 1T cov:plain: 176/195 = 90.26 % -> 177/195 = 90.77 %
- 1T cov:skp-passive: 72/72 = 100.00 % -> 71/72 = 98.61 %  (WORSE)
- 1T cov:timeframe: 0/1 = 0.00 % -> 0/1 = 0.00 %

## Notes
- Key tier: only one Gemini key is configured (no GEMINI_API_KEY_FREE in the env file), so all 194 calls went on that single key; free vs billed is not detectable from the response. Spend above is the list-price upper bound.
- Budget: 194 of 200 used by round 3, so no further round was affordable (6 calls left); the loop ends here.
- Main cost: the line flipped 16 (1U) + 7 (1T) judged-correct determiner items from SAME to a rejection, including 4 of the 8 1U / 3 of the 5 1T TIP-rule gains of 1V round 2 (C:190022, 025, 034, 043; C:180054, 057, 075). It fixed 1 of the 6 targets (028).
- REVERT applied: phase1w/stack_1w_s3.py removed; s3/s3_detline.py and s3/s3_loop.py are kept as the record of the round.

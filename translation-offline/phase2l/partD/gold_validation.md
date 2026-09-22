# Phase 2L Part D - Czech gold validation (1T validator, run ONCE, 0 model calls)

Validator `phase1t/taskB/cz_validate.py` executed unchanged (1V Track C harness), 120 gold rows. Czech side = the ASSEMBLED readers of `stack_2l_cz` (cz_reader four fixes bound into the AG chain; F4v2 reader = `f4fix.build_fixed(CK, 'cz')`). Slovak = stored 1T/1V figures (the validator's Slovak control this run equals them: True). Cells: agree / conservative / ERROR.

| guard | in SOURCE-ONLY stack | CZ assembled (2L) | CZ 1V after (stored) | CZ 1T before (stored) | SK (stored) |
|---|---|---|---|---|---|
| g1 F9 | no (F9 not a SOURCE-ONLY layer) | 82 / 37 / 1 | 82 / 37 / 1 | 82 / 35 / 3 | 96 / 23 / 1 |
| g2 F4v2 | yes (F4v2/F4v3 reader) | 16 / 89 / 15 | 16 / 89 / 15 | 17 / 83 / 20 | 17 / 87 / 16 |
| g3 AG v2 | yes (AG agent reader) | 59 / 16 / 45 | 59 / 16 / 45 | 53 / 6 / 61 | 55 / 18 / 47 |
| g3 AG v3 | yes (AG agent reader) | 59 / 16 / 45 | 59 / 16 / 45 | 53 / 6 / 61 | 55 / 18 / 47 |
| g4 voice v2 | yes (AG voice reader) | 100 / 0 / 20 {'ERROR_as_passive': 16, 'ERROR_as_active': 4} | 100 / 0 / 20 {'ERROR_as_passive': 16, 'ERROR_as_active': 4} | 108 / 0 / 12 {'ERROR_as_passive': 6, 'ERROR_as_active': 6} | 98 / 0 / 22 {'ERROR_as_passive': 18, 'ERROR_as_active': 4} |
| g4 voice v3 | yes (AG voice reader) | 97 / 0 / 23 {'ERROR_as_passive': 20, 'ERROR_as_active': 3} | 97 / 0 / 23 {'ERROR_as_passive': 20, 'ERROR_as_active': 3} | 105 / 0 / 15 {'ERROR_as_passive': 10, 'ERROR_as_active': 5} | 98 / 0 / 22 {'ERROR_as_passive': 20, 'ERROR_as_active': 2} |

Czech class changes vs 1V Track C `after` (row, 1V, 2L): {"g1": [], "g2": [], "g3_v2": [], "g3_v3": [], "g4_v2": [], "g4_v3": []}

Note: g2 for Czech uses the 2J-fixed reader (PP shadow + non-verb list + em) that F4v2/F4v3 run; the stored Slovak g2 is the unfixed checker_1i reader. AG in the stack is AG v4 via stack_1w (reader_nom); the validator measures its V2/V3 agent and voice readers.

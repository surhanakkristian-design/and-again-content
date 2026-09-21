# Phase 2J Part B (S4 B1 + S5 B2 summary, B3, B4)

## B2 model audit of the Slovak references (summary)

Coverage: 3200 of 4064 SK rows audited (3413 references), packets not audited: p032, p033, p034, p035, p036, p037, p038, p039, p040 (token cap stop: spent 1414860 + 4 x 45494 > cap 1500000). Audited ids: partB/audit/COVERAGE.json (sha of sorted ids e457225d03d2c048). Part D must sample only from these.
Headless tokens B2: 1414860 over 32 sessions (failed: {}). Prompt sha256 ccf78e156ec1f6fb914f88731992469a3b7ec85e76af40dbae357a2332f0eea4. Audit ref text mismatches: 0.

### Per reference

| level | faithful | adds content | narrows | wrong person/gender | other | refs |
|---|---|---|---|---|---|---|
| A1 | 753 | 21 | 34 | 208 | 37 | 1053 |
| A2 | 758 | 12 | 55 | 127 | 44 | 996 |
| B1 | 580 | 15 | 40 | 55 | 31 | 721 |
| B2 | 475 | 17 | 43 | 79 | 29 | 643 |
| all | 2566 | 65 | 172 | 469 | 141 | 3413 |

### Per sentence (a sentence counts in every class any of its references has)

| level | sentences | all faithful | any flag | adds content | narrows | wrong person/gender | other |
|---|---|---|---|---|---|---|---|
| A1 | 921 | 670 | 251 | 19 | 34 | 163 | 36 |
| A2 | 965 | 738 | 227 | 12 | 54 | 118 | 43 |
| B1 | 693 | 556 | 137 | 15 | 40 | 52 | 30 |
| B2 | 621 | 458 | 163 | 17 | 42 | 75 | 29 |
| all | 3200 | 2422 | 778 | 63 | 170 | 408 | 138 |

### Agreement with B1 (SK)

B1 SK flags 92; on audited rows 70; of those B2 = wrong person/gender 21, any B2 flag 26. B2 W references 469, of which B1-flagged 21 (B1 compares only rows its reader reads).

| B1 class | B2 classes on the same reference |
|---|---|
| gender_contradiction | B2_F 1, B2_W 2, not_audited 2 |
| gender_fixed_open | B2_A 1, B2_F 5, B2_N 1, not_audited 2 |
| neuter_as_he_she | B2_F 3, B2_N 1, B2_W 7, not_audited 4 |
| number | B2_F 12, B2_N 1, B2_W 3, not_audited 3 |
| person | B2_F 23, B2_O 1, B2_W 9, not_audited 11 |

## B3 corrections (phase2j/upload/, see UPLOAD_README.md)

SK rows changed 577 (references on those rows 643 -> 1191); CZ 0. v[0] changed on 58 rows (v[0] flagged; en = v[0] kept).

| lang/class | replaced | added | removed | listed |
|---|---|---|---|---|
| cz/B1_gender_contradiction | 0 | 0 | 0 | 15 |
| cz/B1_gender_fixed_open | 0 | 0 | 0 | 10 |
| cz/B1_neuter_as_he_she | 0 | 0 | 0 | 13 |
| cz/B1_number | 0 | 0 | 0 | 16 |
| cz/B1_person | 0 | 0 | 0 | 53 |
| sk/A | 60 | 0 | 0 | 5 |
| sk/N | 0 | 164 | 0 | 8 |
| sk/O | 0 | 0 | 0 | 141 |
| sk/W | 0 | 385 | 0 | 84 |
| sk/dedup | 0 | 0 | 1 | 0 |

Listed (not changed) by reason: cz/B1_gender_contradiction:cz_B1_flag_not_deterministic_safe (reader noise, no model audit) 15; cz/B1_gender_fixed_open:cz_B1_flag_not_deterministic_safe (reader noise, no model audit) 10; cz/B1_neuter_as_he_she:cz_B1_flag_not_deterministic_safe (reader noise, no model audit) 13; cz/B1_number:cz_B1_flag_not_deterministic_safe (reader noise, no model audit) 16; cz/B1_person:cz_B1_flag_not_deterministic_safe (reader noise, no model audit) 53; sk/A:span_found_2 4; sk/A:span_found_3 1; sk/N:duplicate_variant 1; sk/N:span_found_0 1; sk/N:span_found_2 3; sk/N:tense_filter_past_vs_present 2; sk/N:tense_filter_present_vs_past 1; sk/O:class_O_not_corrected 141; sk/W:W_mixed_genders 17; sk/W:W_not_a_gender_pair 37; sk/W:tense_filter_future_vs_present 28; sk/W:tense_filter_present_vs_past 2

## B4 closed-set re-score (2I set with A + B) — CLOSED-SET RE-SCORE (2I set, 900 items) with A + B (corrected references), stored replies by request hash + only new L3 calls

Set: 100 sentences, 78 audited, 12 with corrected references (108 items). Run partB/b4/run: {"status": "COMPLETE", "requests": 837, "needed": 101, "seeded_used": 736, "calls_made": 101, "counted_total": 101, "spend_usd": 0.012708, "uncounted_attempts": 0}.

| | coverage | FA |
|---|---|---|
| 2I | 443/497 = 89.13 % [86.06, 91.73] | 19/403 = 4.71 % [2.86, 7.26] |
| A3 (A fix) | 464/497 = 93.36 % [90.80, 95.39] | 20/403 = 4.96 % [3.06, 7.56] |
| A + B | 474/497 = 95.37 % [93.14, 97.04] | 21/403 = 5.21 % [3.25, 7.86] |

Every item whose verdict changed vs A3 (22):

| jid | judge | refs corrected | A3 | A+B | L3 | answer |
|---|---|---|---|---|---|---|
| A:1038:c4 | correct | yes | L3 rej | L3 acc | SAME | My friend told me that the bracelet was too loose, so she altered it. |
| A:1038:m | wrong | yes | L3 rej | L3 acc | SAME | My friend said that it was too loose, so she adjusted it. |
| A:1212:c4 | correct | yes | L3 rej | L3 acc | SAME | This time tomorrow he will be making that same grimace with his mouth open in front of the mirror. |
| A:1858:c1 | correct | yes | L3 rej | L3 acc | SAME | She wishes her cat would carry a ball like this too. |
| A:1858:c3 | correct | yes | L3 rej | L3 acc | SAME | She would like her cat to carry such a ball too. |
| A:1858:c4 | correct | yes | L3:TIPrej rej | L3 acc | SAME | She wishes her cat would also carry a ball like that. |
| A:1858:m | wrong | yes | L3 rej | F5 rej |  | She wishes her cat would carry a ball too. |
| A:2035:c2 | correct | yes | L3 acc | L1 acc |  | What does he buy? Ripe red tomatoes. |
| A:2402:c1 | correct | yes | L3 acc | L1 acc |  | Guess what, the guy whose animal jumped off that cliff apparently wasn't even scared. |
| A:2402:m | wrong | yes | L3 rej | F5 rej |  | Guess what, the guy whose animal jumped apparently wasn't even scared. |
| A:2461:m | wrong | yes | L3:TIPrej rej | L3 rej | DIFF | Since 2019 he has been photographing planes. Apparently a very undemanding hobby. |
| A:2463:c1 | correct | yes | L3 rej | L3 acc | SAME | By Christmas he will have been making fun of that doll sweater for months. |
| A:2463:c3 | correct | yes | L3 rej | L3 acc | SAME | By Christmas he will have been joking about that doll sweater for months. |
| A:2463:c4 | correct | yes | L3 rej | L3 acc | SAME | By Christmas she will have been making fun of that doll's sweater for months. |
| A:2463:c5 | correct | yes | L3 rej | L3 acc | SAME | By Christmas he will have been poking fun at that doll's sweater for months already. |
| A:2463:s | wrong | yes | L3 rej | L3:TIPrej rej | TIP | By Christmas he will have been making fun of that doll sweater since months. |
| A:2640:c1 | correct | yes | L3 acc | L1 acc |  | The desk is clean, so he can finally work. |
| A:2640:c5 | correct | yes | L3:TIPrej rej | L3 acc | SAME | Since the desk is clean, he can finally get to work. |
| A:2640:m | wrong | yes | L3 rej | F5 rej |  | The desk is clean, so he can work. |
| A:2798:c4 | correct | yes | L3 acc | L3:TIPrej rej | TIP | At this time tomorrow the subject will unlock the same wooden door, as usual. |
| A:3790:c2 | correct | yes | L3 rej | L3 acc | SAME | At the moment he's finishing his walk on the rooftop above the city. |
| A:3790:m | wrong | yes | L3 rej | L3:TIPrej rej | TIP | Right now she is finishing her walk above the city. |

Changed vs 2I: 63 items (list in partB/b4/B4.json changed_vs_2I).

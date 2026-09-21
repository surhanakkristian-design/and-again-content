# Phase 2G Part A - reference enrichment on the 2F Slovak production probe

**CLOSED-SET DIAGNOSTIC.** The 60-sentence / 360-item set was opened once in 2F. Exactly one variable changed: the reference source (annotations `hygienised.v`, enriched by one blind headless session, then lever 3 time-frame filter). Judge labels, stack, deterministic layers, prompt template (P-FROZEN-1U), model gemini-3.1-flash-lite, temperature 0, thinkingBudget 0 are those of 2F. This identifies a cause; it is not a new measurement.

## Verdict: **REJECTED**

Coverage moved -2.75 points (rule: CONFIRMED needs >= +8 with FA <= +1; REJECTED if < +3). FA moved -0.56 points.

## A1 enrichment

- One headless session (opus, Read/Write only), input `enrich/enrich_input.json` = {sid, sk, refs} only; no learner answer, label or verdict. Exit 0, 3 turns, 119 s wall.
- Generated 114 variants; tense filter (phase1p/lever3.time_frame vs main reference) dropped 9; kept 105. Duplicates 0.
- Mean refs/sentence: before 1.10, after 2.85 (51/60 reach 3). Refs visible to L3 (main + lever-3 shown, cap 2): before 1.05, after 2.80. 3 pre-existing second refs were already removed by lever 3 in 2F.
- Claude tokens: 87237 total incl. cache (in 6, cache-create 35290, cache-read 39092, out 12849), reported $0.6937; 1454 tokens/sentence.
- Side effect of the one variable: the exact-match layer found 26 matches (2F: 14), L2 lock firings 92 (2F: 96), items reaching L3 295 (2F: 312). All flow from the enriched `v`; no code changed.

## A2/A3 before vs after (95 % Clopper-Pearson)

| metric | 2F probe (before) | enriched (after) | 1W reference |
|---|---|---|---|
| coverage | 154/182 = 84.62 % [78.54, 89.53] | 149/182 = 81.87 % [75.49, 87.18] | 392/401 = 97.76 % [95.78, 98.97] |
| FA | 11/178 = 6.18 % [3.12, 10.79] | 10/178 = 5.62 % [2.73, 10.09] | 16/499 = 3.21 % [1.84, 5.15] |
| FA type S | 3/31 = 9.68 % [2.04, 25.75] | 3/31 = 9.68 % [2.04, 25.75] | |
| FA type M | 6/55 = 10.91 % [4.11, 22.25] | 5/55 = 9.09 % [3.02, 19.95] | |
| FA type T | 1/52 = 1.92 % [0.05, 10.26] | 0/52 = 0.00 % [0.00, 6.85] | |
| FA type W | 1/40 = 2.50 % [0.06, 13.16] | 2/40 = 5.00 % [0.61, 16.92] | |
| FA by layer | {'L3': 11} | {'L3': 10} | |
| false rejections by layer | {'L3': 16, 'F4v2': 7, 'L3:TIPrej': 5} (total 28) | {'L3:TIPrej': 10, 'L3': 16, 'F4v2': 7} (total 33) | |
| final layer mix | {'L3': 282, 'F4v2': 13, 'L1': 14, 'L3:TIPrej': 29, 'AG': 13, 'F3': 4, 'F5': 4, 'F2B': 1} | {'L3': 263, 'L3:TIPrej': 32, 'F4v2': 12, 'L1': 26, 'AG': 13, 'F5': 14} | |

## Item level

- Of the 28 false rejections in 2F, **3 rescued**. **8 new false rejections** (correct items accepted in 2F, rejected now).
- False acceptances **added** by enrichment: 2; removed: 3.
- 45 items changed verdict or layer, 16 of them flipped accept/reject. Every request differs from 2F (the alt-references line is now present on all 360 items), so no flip isolates model noise from the reference change.

| sid | item | label | before | after | answer |
|---|---|---|---|---|---|
| 220002 | C:220002:c1 | correct | ACCEPT @L3 (SAME) | REJECT @L3:TIPrej (TIP) | Girl, he told me that the iceberg was huge; he must have felt so tiny there. |
| 220003 | C:220003:c2 | correct | ACCEPT @L3 (SAME) | REJECT @L3 (DIFF) | The bread has been toasted by the model fighter jet for about three minutes. |
| 220007 | C:220007:c2 | correct | ACCEPT @L3 (SAME) | ACCEPT @L1 (None) | He stands barefoot on the warm sand. |
| 220015 | C:220015:c1 | correct | ACCEPT @L3 (SAME) | ACCEPT @L1 (None) | He kept putting more books on the pile until it wobbled. |
| 220017 | C:220017:c2 | correct | ACCEPT @L3 (SAME) | ACCEPT @L1 (None) | This pencil is sharper than that blunt one. |
| 220019 | C:220019:c1 | correct | ACCEPT @L3 (SAME) | ACCEPT @L1 (None) | The insect is tiny, so she should examine it with a magnifying glass. |
| 220023 | C:220023:c1 | correct | ACCEPT @L3 (SAME) | ACCEPT @L1 (None) | Listen, she said that they have the same dress, but they're still friends. |
| 220023 | C:220023:c3 | correct | ACCEPT @L3 (SAME) | REJECT @L3:TIPrej (TIP) | Listen, she said they have the same dresses, but they're still friends. |
| 220027 | C:220027:c1 | correct | ACCEPT @L3 (SAME) | ACCEPT @L1 (None) | The flakes are in the bowl – he's going to eat them right away. |
| 220030 | C:220030:c1 | correct | REJECT @L3 (DIFF) | ACCEPT @L1 (None) | The fan has one painted face and a scarf. |
| 220030 | C:220030:c2 | correct | REJECT @L3 (DIFF) | ACCEPT @L3 (SAME) | A fan has one painted face and a scarf. |
| 220031 | C:220031:c1 | correct | ACCEPT @L3 (SAME) | ACCEPT @L1 (None) | Two more penguins are walking by the ice. |
| 220035 | C:220035:c2 | correct | ACCEPT @L3 (SAME) | ACCEPT @L1 (None) | These tins fly out of his paper bag. |
| 220037 | C:220037:c1 | correct | ACCEPT @L3 (SAME) | ACCEPT @L1 (None) | Disaster! She doesn't have time for a long visit! |
| 220039 | C:220039:c2 | correct | ACCEPT @L3 (SAME) | REJECT @L3:TIPrej (TIP) | At six he'll have been pounding those pads for two solid hours. |
| 220040 | C:220040:c2 | correct | REJECT @L3 (DIFF) | REJECT @L3:TIPrej (TIP) | The woman is going to hang one gold medal on his neck. |
| 220041 | C:220041:c1 | correct | ACCEPT @L3 (SAME) | REJECT @L3:TIPrej (TIP) | Dude, the door is already open, so it reveals the whole valley, really. |
| 220043 | C:220043:c2 | correct | ACCEPT @L3 (SAME) | ACCEPT @L1 (None) | The trainer has a bandage and white tape. |
| 220048 | C:220048:c3 | correct | REJECT @L3:TIPrej (TIP) | REJECT @L3 (DIFF) | I won't lie, you were the most charming clerk; she never smiled like that before. |
| 220049 | C:220049:c3 | correct | ACCEPT @L3 (SAME) | ACCEPT @L1 (None) | The fish have a plan. They will swim away from the shark. |
| 220050 | C:220050:c3 | correct | ACCEPT @L3 (SAME) | REJECT @L3:TIPrej (TIP) | The moment the crutch fell onto the wet floor, it was grabbed firmly by him and he went on. |
| 220055 | C:220055:c3 | correct | REJECT @L3 (DIFF) | ACCEPT @L3 (SAME) | On the last page of the contract for the new job they write their name, and the office applauds. |
| 220060 | C:220060:c3 | correct | ACCEPT @L3 (SAME) | REJECT @L3 (DIFF) | The pegs should have been checked by you before that match - two came loose in the first ten minutes. |
| 220002 | W:220002:w3 | correct | ACCEPT @L3 (SAME) | REJECT @L3 (DIFF) | Girl, he told me that iceberg was huge; he must have felt so tiny there. |
| 220003 | W:220003:w3 | wrong/M | REJECT @F3 (None) | REJECT @F5 (None) | The model fighter jet has been toasting the bread for three minutes. |
| 220004 | W:220004:w2 | wrong/M | REJECT @F3 (None) | REJECT @F5 (None) | The bridge spans the terrifying canyon, doesn't it? |
| 220007 | W:220007:w2 | wrong/M | REJECT @L3:TIPrej (TIP) | REJECT @F5 (None) | He is standing on the warm sand. |
| 220011 | W:220011:w2 | wrong/M | REJECT @L3:TIPrej (TIP) | REJECT @L3 (DIFF) | Honestly, the rainbow may fade, but this time tomorrow you will be showing your video. |
| 220015 | W:220015:w2 | wrong/M | ACCEPT @L3 (SAME) | REJECT @F5 (None) | He kept putting books on the pile until it wobbled. |
| 220020 | W:220020:w3 | wrong/M | REJECT @F3 (None) | REJECT @F5 (None) | The man has been admiring his car for twenty minutes. |
| 220022 | W:220022:w1 | wrong/M | REJECT @F2B (TIP) | REJECT @F5 (None) | Honestly, today you're louder than the national team. |
| 220025 | W:220025:w2 | wrong/M | REJECT @F4v2 (None) | REJECT @F5 (None) | She asked me not to move my arm. |
| 220026 | W:220026:w1 | wrong/T | ACCEPT @L3 (SAME) | REJECT @L3:TIPrej (TIP) | No way, the gecko is going to spit fire right now, because the peppers are so hot. |
| 220026 | W:220026:w2 | wrong/M | ACCEPT @L3 (SAME) | REJECT @L3:TIPrej (TIP) | No way, gecko is spitting fire right now, because the peppers are so hot. |
| 220030 | W:220030:w1 | wrong/M | REJECT @L3:TIPrej (TIP) | REJECT @L3 (DIFF) | The fan has one painted face and scarf. |
| 220036 | W:220036:w2 | wrong/M | REJECT @L3 (DIFF) | REJECT @L3:TIPrej (TIP) | He is putting the bacon next to the egg in the pan. |
| 220037 | W:220037:w1 | wrong/M | REJECT @L3:TIPrej (TIP) | REJECT @L3 (DIFF) | Disaster! She doesn't have time for long visit! |
| 220037 | W:220037:w2 | wrong/W | REJECT @L3 (DIFF) | REJECT @L3:TIPrej (TIP) | Disaster! She doesn't have a time for a long visit! |
| 220039 | W:220039:w3 | wrong/W | REJECT @L3 (DIFF) | ACCEPT @L3 (SAME) | By six o'clock he will have been pounding some mitts for two hours straight. |
| 220045 | W:220045:w2 | wrong/M | REJECT @F3 (None) | REJECT @F5 (None) | One shirt, one collar and two ties. |
| 220047 | W:220047:w2 | wrong/M | REJECT @L3:TIPrej (TIP) | REJECT @L3 (DIFF) | Really, your two flashlights light up dark ledge nicely. |
| 220051 | W:220051:w3 | wrong/M | REJECT @L3 (DIFF) | REJECT @F5 (None) | About forty students have been applying for membership at the club fair. |
| 220052 | W:220052:w2 | wrong/M | REJECT @L3:TIPrej (TIP) | REJECT @F5 (None) | Status update: the closet has stayed tidy for 3 weeks. |
| 220055 | W:220055:w1 | wrong/M | REJECT @L3:TIPrej (TIP) | ACCEPT @L3 (SAME) | They write their name on last page of the contract for the new job and the office applauds. |
| 220055 | W:220055:w2 | wrong/S | REJECT @L3 (DIFF) | REJECT @L3:TIPrej (TIP) | They write their name on the last page of the contract for the new job and it is applauded. |

### Added references for sentences with a flip

- 220002: main "Girl, he told me the glacier was vast; he must have felt so tiny standing there."; added ["Bestie, he told me that the glacier was huge; he must have felt so small standing there.", "Girl, he told me the glacier was enormous; standing there, he must have felt really tiny."]
- 220003: main "The model fighter jet has been toasting bread for approximately three minutes."; added ["The model fighter jet has been toasting bread for about three minutes.", "For approximately three minutes, the model fighter jet has been toasting bread."]
- 220015: main "He kept stacking books onto the pile until it swayed."; added ["He kept putting more books on the pile until it wobbled.", "He went on stacking more books onto the pile until it swayed."]
- 220023: main "Listen, she said they have the same dress, but they are still friends."; added ["Listen, she said that they have the same dress, but they're still friends.", "Listen, she said they've got the same dress, but they are still mates."]
- 220026: main "Nah, the gecko is breathing fire right now 'cause the chillies are so spicy."; added ["Nah, the gecko's breathing fire right now because the peppers are so hot.", "No way, the gecko is spitting fire right now 'cause the chillies are so hot."]
- 220030: main "The fan has a painted face and a scarf."; added ["The fan has got a painted face and a scarf.", "The fan has one painted face and a scarf."]
- 220039: main "By six she will have been hitting those pads for two hours straight."; added ["By six she will have been hitting those pads for two hours non-stop."]; tense-dropped ["By six o'clock she'll have been punching those pads for two solid hours."]
- 220041: main "Bro, the doors are open now, so they reveal the whole valley, fr."; added ["Dude, the doors are open now, so they show the whole valley, for real.", "Bro, the doors are already open, so they reveal the entire valley, fr."]
- 220050: main "The moment his crutch hit the wet floor, he gripped it tight and kept going."; added ["As soon as the crutch landed on the wet floor, he grabbed it firmly and carried on.", "The instant his crutch hit the wet floor, he held it tightly and walked on."]
- 220055: main "He puts his name on the last page of the contract for his new job, and the office claps."; added ["He writes his name on the last page of the contract for his new job, and the office applauds."]
- 220060: main "He should have checked the studs before that match - two of them came loose in the first ten minutes."; added ["He should have checked the studs before that match - two came loose within the first ten minutes."]; tense-dropped ["He ought to have checked the studs before that match - two of them worked loose in the first ten minutes."]

## A5 pricing

Not done: verdict REJECTED (A5 runs only on CONFIRMED or PARTIAL). Measured rate for the record: 1454 Claude tokens/sentence, 60 sentences per session in 119 s.

## Gemini accounting

- Counted (HTTP 200) 295, failed (empty/unparsable 200) 0, uncounted retries 0; cap 350 (phase cap 450). Tokens in 162952 / out 295; list-price upper bound $0.0164; key tiers {'unrecorded': 295}.
- Ledger: `ledger_2g_a.jsonl`.

## Defects recorded (not fixed)

- 220060: generator reports the Slovak "Mal si skontrolovat" is 2nd person, main reference uses "he" (possible wrong main reference).
- 220027: main reference drops the object "ich" (them); new variants include it.
- The reference source feeds the exact-match and L2 layers as well as the L3 prompt, so "only the references changed" still moves deterministic layers (see A1).
- The FREEZE_FILES copy had to be repointed to phase2g/partA/run and FREEZE_HASH re-pinned to the Part A commit (ac91692) for the runner freeze check to pass; code bytes are the 2F probe run copies except the ledger filename.

# Phase 1k — DEV reproduction of the frozen config (zero calls)

Frozen config: **LOCKTIP / P-FROZEN / TIP-as-rejection on** (F8 False, F9 False, REPORTED_STRICT False).

| metric | value |
|---|---|
| coverage | 182/189 = 96.30% [92.52, 98.50] |
| coverage (kind C only) | 176/180 = 97.78% [94.41, 99.39] |
| FA | 13/301 = 4.32% [2.32, 7.27] |
| FA type T | 0/54 = 0.00% [0.00, 6.60] |
| FA type W | 2/76 = 2.63% [0.32, 9.18] |
| FA type M | 3/66 = 4.55% [0.95, 12.71] |
| FA type S | 6/98 = 6.12% [2.28, 12.85] |
| FA type V | 2/6 = 33.33% [4.33, 77.72] |
| FA type E | 0/1 = 0.00% [0.00, 97.50] |

## B3 line

```
{
 "tip": {
  "n": 168,
  "judged_correct": 66,
  "judged_wrong": 102,
  "cost_type_T_wrong_accepted": 0
 },
 "abstain": {
  "n": 35,
  "judged_correct": 19,
  "judged_wrong": 16,
  "cost_type_T_wrong_accepted": 0
 }
}
```

## Every false acceptance

- `{"id": "C:10167:2659945156", "layer": "L1", "model_reply": "", "model": null, "slovak": "On má ústa také suché, že smäd musí byť skutočný.", "answer": "Her mouth is so dry that the thirst must be real.", "reference": "His mouth is that dry, so the thirst must be real.", "judge_label": "wrong", "judge_type": "S", "intent": null, "f8": "accept", "f9": "accept"}`
- `{"id": "C:10167:3007534590", "layer": "L1", "model_reply": "", "model": null, "slovak": "On má ústa také suché, že smäd musí byť skutočný.", "answer": "Her mouth's so dry that the thirst must be real.", "reference": "His mouth is that dry, so the thirst must be real.", "judge_label": "wrong", "judge_type": "S", "intent": null, "f8": "accept", "f9": "accept"}`
- `{"id": "C:23360:1881410199", "layer": "L1", "model_reply": "", "model": null, "slovak": "Jeho obrovské kýchnutie ty môžeš počuť po celej lúke.", "answer": "His huge sneeze can be heard across the whole meadow.", "reference": "You can hear his huge sneeze across the whole meadow.", "judge_label": "wrong", "judge_type": "V", "intent": null, "f8": "reject", "f9": "accept"}`
- `{"id": "C:26084:39201327", "layer": "L1", "model_reply": "", "model": null, "slovak": "On ju dokáže nájsť skôr, než ona príde domov.", "answer": "She can find her before she comes home.", "reference": "He can find her before she gets home.", "judge_label": "wrong", "judge_type": "S", "intent": null, "f8": "accept", "f9": "accept"}`
- `{"id": "C:6365:1746610732", "layer": "L1", "model_reply": "", "model": null, "slovak": "Režisér povedal, že oni kancelársku scénu natočia pred obedom.", "answer": "The director said that the office scene would be filmed before lunch.", "reference": "The director said they would film the office scene before lunch.", "judge_label": "wrong", "judge_type": "V", "intent": null, "f8": "accept", "f9": "accept"}`
- `{"id": "W:21124:1753932823", "layer": "L3", "model_reply": "SAME", "model": "SAME", "slovak": "Zvyčajne ona ostáva pod strechou, ale dnes tancuje v daždi.", "answer": "She stays under the roof, but today she is dancing in the rain.", "reference": "She usually stays dry, but today she is dancing in the rain.", "judge_label": "wrong", "judge_type": "M", "intent": null, "f8": "accept", "f9": "accept"}`
- `{"id": "W:2783:2540506102", "layer": "L3", "model_reply": "SAME", "model": "SAME", "slovak": "Lopta, ktorú pes priniesol, je teraz úplne od blata.", "answer": "The ball that the dog brought is covered in mud.", "reference": "The ball that the dog fetched is now completely muddy.", "judge_label": "wrong", "judge_type": "M", "intent": null, "f8": "accept", "f9": "accept"}`
- `{"id": "W:31648:250135833", "layer": "L3", "model_reply": "SAME", "model": "SAME", "slovak": "Zlatko, on vraj opustil misku včera, nie dnes.", "answer": "Honey, apparently he left the plate yesterday, not today.", "reference": "Honey, apparently he left the bowl yesterday, not today.", "judge_label": "wrong", "judge_type": "W", "intent": null, "f8": "accept", "f9": "accept"}`
- `{"id": "W:7910:2914297793", "layer": "L3", "model_reply": "SAME", "model": "SAME", "slovak": "Napriek ventilátoru na plný výkon sa zopnutá kopa vôbec nepohla.", "answer": "Despite the fan being at full power, the clipped piles didn't move at all.", "reference": "Despite the fan at full power, the clipped pile did not move at all.", "judge_label": "wrong", "judge_type": "S", "intent": null, "f8": "abstain", "f9": "accept"}`
- `{"id": "W:8812:384802316", "layer": "L3", "model_reply": "SAME", "model": "SAME", "slovak": "Tréner by si prial, aby jeho lapy boli trochu hrubšie.", "answer": "The coach wishes his gloves were thicker.", "reference": "Her trainer wishes his pads were a bit thicker.", "judge_label": "wrong", "judge_type": "M", "intent": null, "f8": "accept", "f9": "tip"}`
- `{"id": "W:8824:3690697119", "layer": "L3", "model_reply": "SAME", "model": "SAME", "slovak": "Kým sa reťaz kývala, on dotlačil vrece na miesto.", "answer": "While the chains were swinging, he pushed the sack into place.", "reference": "While the chain was swinging, he pushed the bag into place.", "judge_label": "wrong", "judge_type": "S", "intent": null, "f8": "accept", "f9": "tip"}`
- `{"id": "W:9007:2829648222", "layer": "L3", "model_reply": "SAME", "model": "SAME", "slovak": "Dnes v noci on preveril už šesť zdrojov a kopa stále rastie.", "answer": "Tonight he has already checked six sources and the list is still growing.", "reference": "He has checked six sources tonight and the pile is still growing.", "judge_label": "wrong", "judge_type": "W", "intent": null, "f8": "accept", "f9": "tip"}`
- `{"id": "W:9687:2008862971", "layer": "L3", "model_reply": "SAME", "model": "SAME", "slovak": "Ak oba štáty podpíšu zmluvu, hranica sa budúci mesiac otvorí.", "answer": "If both countries sign the treaty, the borders will open next month.", "reference": "If both states sign the treaty, the border will open next month.", "judge_label": "wrong", "judge_type": "S", "intent": null, "f8": "abstain", "f9": "accept"}`

## Every false rejection

- `{"id": "C:11610:415761804", "layer": "L3:TIPrej", "model_reply": "TIP", "model": "TIP", "slovak": "Na lavičke je jeden dlhý obväz.", "answer": "There's a long bandage on the bench.", "reference": "There is one long bandage on the bench.", "judge_label": "correct", "judge_type": null, "intent": null, "f8": "accept", "f9": "tip"}`
- `{"id": "C:15954:580487827", "layer": "L3:TIPrej", "model_reply": "TIP", "model": "TIP", "slovak": "Pozri! Predavač práve spúšťa kôš do oleja.", "answer": "Look, the seller is dropping the basket into the oil right now.", "reference": "Look! The vendor is lowering the basket into the oil.", "judge_label": "correct", "judge_type": null, "intent": null, "f8": "accept", "f9": "tip"}`
- `{"id": "C:27628:1242167241", "layer": "L3", "model_reply": "DIFF", "model": "DIFF", "slovak": "Deti sa zobudia o siedmej ráno.", "answer": "At seven in the morning, the children will wake up.", "reference": "The children awake at seven in the morning.", "judge_label": "correct", "judge_type": null, "intent": null, "f8": "abstain", "f9": "accept"}`
- `{"id": "C:27628:3492027817", "layer": "L3", "model_reply": "DIFF", "model": "DIFF", "slovak": "Deti sa zobudia o siedmej ráno.", "answer": "The children will wake up at seven in the morning.", "reference": "The children awake at seven in the morning.", "judge_label": "correct", "judge_type": null, "intent": null, "f8": "abstain", "f9": "accept"}`
- `{"id": "W:2389:2222473907", "layer": "L3", "model_reply": "DIFF", "model": "DIFF", "slovak": "Keby duriány nesmrdeli tak silno, colnica by ich asi pustila.", "answer": "If durians hadn't smelled so strong, customs would probably have let them through.", "reference": "If durians didn't smell so strongly, customs would probably let them through.", "judge_label": "correct", "judge_type": null, "intent": null, "f8": "accept", "f9": "tip"}`
- `{"id": "W:27628:3397554170", "layer": "L3", "model_reply": "DIFF", "model": "DIFF", "slovak": "Deti sa zobudia o siedmej ráno.", "answer": "The children will wake up at seven.", "reference": "The children awake at seven in the morning.", "judge_label": "correct", "judge_type": null, "intent": null, "f8": "abstain", "f9": "accept"}`
- `{"id": "W:6971:4268819537", "layer": "L3", "model_reply": "DIFF", "model": "DIFF", "slovak": "Keby ona bola robot, žiadosti by jej neprekážali.", "answer": "If she had been a robot, the requests wouldn't have bothered her.", "reference": "If she were a robot, the requests would not bother her.", "judge_label": "correct", "judge_type": null, "intent": null, "f8": "accept", "f9": "tip"}`

## Calls

```
{
 "counted_calls_http200": 466,
 "failed_empty_200": 0,
 "non200_attempts": 0,
 "tokens_in": 163561,
 "tokens_out": 466,
 "spend_usd": 0.04159,
 "phase_budget_remaining": 1534
}
```


# Phase 1k — FRESH results — the one measurement of the frozen config

Frozen config: **LOCKTIP+F8+F9 (ALL) / P-FROZEN / TIP-as-rejection on** (F8 True, F9 True, REPORTED_STRICT False).

| metric | value |
|---|---|
| coverage | 210/217 = 96.77% [93.47, 98.69] |
| coverage (kind C only) | 202/209 = 96.65% [93.22, 98.64] |
| FA | 206/383 = 53.79% [48.65, 58.86] |
| FA type T | 75/130 = 57.69% [48.72, 66.30] |
| FA type W | 69/70 = 98.57% [92.30, 99.96] |
| FA type M | 21/68 = 30.88% [20.24, 43.26] |
| FA type S | 23/70 = 32.86% [22.09, 45.12] |
| FA type V | 17/44 = 38.64% [24.36, 54.50] |
| FA type E | 1/1 = 100.00% [2.50, 100.00] |
| ACTIVE->PASSIVE cell (intent V, judged wrong) | 17 accepted of 43, layers {"F8": 21, "F9": 1, "F4v2": 4} |
| TIME-FRAME-SHIFT cell (intent TF, judged wrong) | 18 accepted of 66, layers {"F9": 47, "F5": 1} |

## Judge noise (60 controls)

```
{
 "n": 60,
 "agree": 60,
 "correct_to_wrong": {
  "k": 0,
  "n": 60,
  "pct": 0.0,
  "ci": [
   0.0,
   5.96
  ]
 },
 "wrong_to_correct": {
  "k": 0,
  "n": 60,
  "pct": 0.0,
  "ci": [
   0.0,
   5.96
  ]
 },
 "any_flip": {
  "k": 0,
  "n": 60,
  "pct": 0.0,
  "ci": [
   0.0,
   5.96
  ]
 }
}
```

## Writer intent x judge label

```
{
 "C|correct:None": 209,
 "T|wrong:T": 64,
 "W|wrong:W": 70,
 "M|wrong:M": 68,
 "S|wrong:S": 70,
 "V|wrong:V": 43,
 "TF|wrong:T": 66,
 "T|wrong:E": 1,
 "T|correct:None": 5,
 "M|correct:None": 2,
 "C|wrong:V": 1,
 "TF|correct:None": 1
}
```

## F9 out-of-sample time-frame check (reporting only)

```
{
 "agree": 50,
 "conservative": 19,
 "error": 1,
 "errors": [
  {
   "sid": 140006,
   "sk": "Ona nikdy neposiela e-maily po desiatej ve\u010der.",
   "tf_gold": "present",
   "script": [
    "past"
   ],
   "reason": "l-participle \"neposiela\""
  }
 ],
 "error_rate": {
  "k": 1,
  "n": 70,
  "pct": 1.43,
  "ci": [
   0.04,
   7.7
  ]
 }
}
```

## Secondary readout (NOT the frozen configuration)

```
{
 "LOCKTIP": {
  "coverage": {
   "k": 216,
   "n": 217,
   "pct": 99.54,
   "ci": [
    97.46,
    99.99
   ]
  },
  "coverage_kindC": {
   "k": 208,
   "n": 209,
   "pct": 99.52,
   "ci": [
    97.36,
    99.99
   ]
  },
  "fa": {
   "k": 283,
   "n": 383,
   "pct": 73.89,
   "ci": [
    69.19,
    78.22
   ]
  },
  "fa_by_type": {
   "T": {
    "k": 129,
    "n": 130,
    "pct": 99.23,
    "ci": [
     95.79,
     99.98
    ]
   },
   "W": {
    "k": 70,
    "n": 70,
    "pct": 100.0,
    "ci": [
     94.87,
     100.0
    ]
   },
   "M": {
    "k": 21,
    "n": 68,
    "pct": 30.88,
    "ci": [
     20.24,
     43.26
    ]
   },
   "S": {
    "k": 23,
    "n": 70,
    "pct": 32.86,
    "ci": [
     22.09,
     45.12
    ]
   },
   "V": {
    "k": 39,
    "n": 44,
    "pct": 88.64,
    "ci": [
     75.44,
     96.21
    ]
   },
   "E": {
    "k": 1,
    "n": 1,
    "pct": 100.0,
    "ci": [
     2.5,
     100.0
    ]
   }
  },
  "fa_by_layer": {
   "L1": 283
  },
  "fr_by_layer": {
   "F4v2": 1
  }
 },
 "LOCKTIP+F8": {
  "coverage": {
   "k": 216,
   "n": 217,
   "pct": 99.54,
   "ci": [
    97.46,
    99.99
   ]
  },
  "coverage_kindC": {
   "k": 208,
   "n": 209,
   "pct": 99.52,
   "ci": [
    97.36,
    99.99
   ]
  },
  "fa": {
   "k": 262,
   "n": 383,
   "pct": 68.41,
   "ci": [
    63.49,
    73.04
   ]
  },
  "fa_by_type": {
   "T": {
    "k": 129,
    "n": 130,
    "pct": 99.23,
    "ci": [
     95.79,
     99.98
    ]
   },
   "W": {
    "k": 70,
    "n": 70,
    "pct": 100.0,
    "ci": [
     94.87,
     100.0
    ]
   },
   "M": {
    "k": 21,
    "n": 68,
    "pct": 30.88,
    "ci": [
     20.24,
     43.26
    ]
   },
   "S": {
    "k": 23,
    "n": 70,
    "pct": 32.86,
    "ci": [
     22.09,
     45.12
    ]
   },
   "V": {
    "k": 18,
    "n": 44,
    "pct": 40.91,
    "ci": [
     26.34,
     56.75
    ]
   },
   "E": {
    "k": 1,
    "n": 1,
    "pct": 100.0,
    "ci": [
     2.5,
     100.0
    ]
   }
  },
  "fa_by_layer": {
   "L1": 262
  },
  "fr_by_layer": {
   "F4v2": 1
  }
 },
 "LOCKTIP+F9": {
  "coverage": {
   "k": 210,
   "n": 217,
   "pct": 96.77,
   "ci": [
    93.47,
    98.69
   ]
  },
  "coverage_kindC": {
   "k": 202,
   "n": 209,
   "pct": 96.65,
   "ci": [
    93.22,
    98.64
   ]
  },
  "fa": {
   "k": 225,
   "n": 383,
   "pct": 58.75,
   "ci": [
    53.63,
    63.72
   ]
  },
  "fa_by_type": {
   "T": {
    "k": 75,
    "n": 130,
    "pct": 57.69,
    "ci": [
     48.72,
     66.3
    ]
   },
   "W": {
    "k": 69,
    "n": 70,
    "pct": 98.57,
    "ci": [
     92.3,
     99.96
    ]
   },
   "M": {
    "k": 21,
    "n": 68,
    "pct": 30.88,
    "ci": [
     20.24,
     43.26
    ]
   },
   "S": {
    "k": 23,
    "n": 70,
    "pct": 32.86,
    "ci": [
     22.09,
     45.12
    ]
   },
   "V": {
    "k": 36,
    "n": 44,
    "pct": 81.82,
    "ci": [
     67.29,
     91.81
    ]
   },
   "E": {
    "k": 1,
    "n": 1,
    "pct": 100.0,
    "ci": [
     2.5,
     100.0
    ]
   }
  },
  "fa_by_layer": {
   "L1": 225
  },
  "fr_by_layer": {
   "F9": 6,
   "F4v2": 1
  }
 },
 "BASE (lock rejects)": {
  "coverage": {
   "k": 216,
   "n": 217,
   "pct": 99.54,
   "ci": [
    97.46,
    99.99
   ]
  },
  "coverage_kindC": {
   "k": 208,
   "n": 209,
   "pct": 99.52,
   "ci": [
    97.36,
    99.99
   ]
  },
  "fa": {
   "k": 283,
   "n": 383,
   "pct": 73.89,
   "ci": [
    69.19,
    78.22
   ]
  },
  "fa_by_type": {
   "T": {
    "k": 129,
    "n": 130,
    "pct": 99.23,
    "ci": [
     95.79,
     99.98
    ]
   },
   "W": {
    "k": 70,
    "n": 70,
    "pct": 100.0,
    "ci": [
     94.87,
     100.0
    ]
   },
   "M": {
    "k": 21,
    "n": 68,
    "pct": 30.88,
    "ci": [
     20.24,
     43.26
    ]
   },
   "S": {
    "k": 23,
    "n": 70,
    "pct": 32.86,
    "ci": [
     22.09,
     45.12
    ]
   },
   "V": {
    "k": 39,
    "n": 44,
    "pct": 88.64,
    "ci": [
     75.44,
     96.21
    ]
   },
   "E": {
    "k": 1,
    "n": 1,
    "pct": 100.0,
    "ci": [
     2.5,
     100.0
    ]
   }
  },
  "fa_by_layer": {
   "L1": 283
  },
  "fr_by_layer": {
   "F4v2": 1
  }
 }
}
```

```
{
 "LOCKTIP|F8": {
  "caught_wrong": 21,
  "caught_wrong_only_this_guard": 19,
  "cost_correct_rejected": 0,
  "caught_items": [
   {
    "id": "W:140001:3226349339",
    "layer": "F8",
    "model_reply": "",
    "model": null,
    "slovak": "Ona každé ráno pije zelený čaj s medom.",
    "answer": "Green tea with honey is drunk by her every morning.",
    "reference": "She drinks green tea with honey every morning.",
    "judge_label": "wrong",
    "judge_type": "V",
    "intent": "V",
    "f8": "reject",
    "f9": "abstain"
   },
   {
    "id": "W:140002:1461087155",
    "layer": "F8",
    "model_reply": "",
    "model": null,
    "slovak": "On práve teraz umýva staré tenisky v dreze.",
    "answer": "Old sneakers are being washed in the sink right now.",
    "reference": "He is washing his old trainers in the sink right now.",
    "judge_label": "wrong",
    "judge_type": "V",
    "intent": "V",
    "f8": "reject",
    "f9": "abstain"
   },
   {
    "id": "W:140003:312397117",
    "layer": "F8",
    "model_reply": "",
    "model": null,
    "slovak": "Moja sestra nosí okuliare iba pri čítaní.",
    "answer": "Glasses are worn by my sister only when she reads.",
    "reference": "My sister only wears glasses when she reads.",
    "judge_label": "wrong",
    "judge_type": "V",
    "intent": "V",
    "f8": "reject",
    "f9": "tip"
   },
   {
    "id": "W:140005:3877298044",
    "layer": "F8",
    "model_reply": "",
    "model": null,
    "slovak": "Ty teraz držíš môj dáždnik a ja mrznem.",
    "answer": "My umbrella is being held by you right now and I am freezing.",
    "reference": "You are holding my umbrella now and I am freezing.",
    "judge_label": "wrong",
    "judge_type": "V",
    "intent": "V",
    "f8": "reject",
    "f9": "tip"
   },
   {
    "id": "W:140012:213263887",
    "layer": "F8",
    "model_reply": "",
    "model": null,
    "slovak": "Sused, ktorý býva nad nami, opravuje bicykle v garáži.",
    "answer": "Bicycles are repaired in the garage by the neighbour who lives above us.",
    "reference": "The neighbour who lives above us repairs bikes in the garage.",
    "judge_label": "wrong",
    "judge_type": "V",
    "intent": "V",
    "f8": "reject",
    "f9": "accept"
   },
   {
    "id": "W:140013:413341414",
    "layer": "F8",
    "model_reply": "",
    "model": null,
    "slovak": "Oni práve natierajú plot na zeleno.",
    "answer": "The fence is being painted green right now.",
    "reference": "They are painting the fence green right now.",
    "judge_label": "wrong",
    "judge_type": "V",
    "intent": "V",
    "f8": "reject",
    "f9": "tip"
   },
   {
    "id": "W:140018:2798792936",
    "layer": "F8",
    "model_reply": "",
    "model": null,
    "slovak": "Ona celý večer písala poznámky do modrého zošita.",
    "answer": "Notes were written in the blue notebook all evening.",
    "reference": "She was writing notes in the blue notebook all evening.",
    "judge_label": "wrong",
    "judge_type": "V",
    "intent": "V",
    "f8": "reject",
    "f9": "tip"
   },
   {
    "id": "W:140019:2550287824",
    "layer": "F8",
    "model_reply": "",
    "model": null,
    "slovak": "Oni minulý rok predávali med na trhu pri rieke.",
    "answer": "Honey was sold at the market by the river last year.",
    "reference": "They sold honey at the market by the river last year.",
    "judge_label": "wrong",
    "judge_type": "V",
    "intent": "V",
    "f8": "reject",
    "f9": "accept"
   },
   {
    "id": "W:140020:3008526410",
    "layer": "F8",
    "model_reply": "",
    "model": null,
    "slovak": "Ja som ako dieťa zbieral staré mince.",
    "answer": "Old coins were collected by me as a child.",
    "reference": "I used to collect old coins as a child.",
    "judge_label": "wrong",
    "judge_type": "V",
    "intent": "V",
    "f8": "reject",
    "f9": "reject"
   },
   {
    "id": "W:140021:1964329415",
    "layer": "F8",
    "model_reply": "",
    "model": null,
    "slovak": "Moja babka nám každú nedeľu piekla jablkový koláč.",
    "answer": "An apple cake was baked for us every Sunday by my grandma.",
    "reference": "My grandma used to bake us an apple pie every Sunday.",
    "judge_label": "wrong",
    "judge_type": "V",
    "intent": "V",
    "f8": "reject",
    "f9": "accept"
   },
   {
    "id": "W:140026:3932510212",
    "layer": "F8",
    "model_reply": "",
    "model": null,
    "slovak": "Oni sa vlani učili po španielsky cez víkendy.",
    "answer": "Spanish was studied by them on weekends last year.",
    "reference": "They studied Spanish at weekends last year.",
    "judge_label": "wrong",
    "judge_type": "V",
    "intent": "V",
    "f8": "reject",
    "f9": "accept"
   },
   {
    "id": "W:140027:3632961874",
    "layer": "F8",
    "model_reply": "",
    "model": null,
    "slovak": "Ona včera stratila peňaženku v autobuse.",
    "answer": "Her wallet was lost on the bus yesterday.",
    "reference": "She lost her wallet on the bus yesterday.",
    "judge_label": "wrong",
    "judge_type": "V",
    "intent": "V",
    "f8": "reject",
    "f9": "accept"
   },
   {
    "id": "W:140028:954872054",
    "layer": "F8",
    "model_reply": "",
    "model": null,
    "slovak": "On rozbil pohár a hneď to upratal.",
    "answer": "A glass was broken by him and cleaned up right away.",
    "reference": "He broke a glass and cleaned it up straight away.",
    "judge_label": "wrong",
    "judge_type": "V",
    "intent": "V",
    "f8": "reject",
    "f9": "accept"
   },
   {
    "id": "W:140029:1352870231",
    "layer": "F8",
    "model_reply": "",
    "model": null,
    "slovak": "Keď sme prišli, on už zjedol celú polievku.",
    "answer": "All the soup had already been eaten by him when we arrived.",
    "reference": "When we arrived, he had already eaten the whole soup.",
    "judge_label": "wrong",
    "judge_type": "V",
    "intent": "V",
    "f8": "reject",
    "f9": "tip"
   },
   {
    "id": "W:140038:4235937858",
    "layer": "F8",
    "model_reply": "",
    "model": null,
    "slovak": "Do stredy ona pripraví podklady pre nového klienta.",
    "answer": "The documents for the new client will be prepared by Wednesday.",
    "reference": "She will prepare the materials for the new client by Wednesday.",
    "judge_label": "wrong",
    "judge_type": "V",
    "intent": "V",
    "f8": "reject",
    "f9": "tip"
   },
   {
    "id": "W:140044:4065905907",
    "layer": "F8",
    "model_reply": "",
    "model": null,
    "slovak": "Keď on dopíše ten list, hneď ho odnesie na poštu.",
    "answer": "When that letter is finished, it will be taken to the post office right away.",
    "reference": "When he finishes that letter, he will take it to the post office right away.",
    "judge_label": "wrong",
    "judge_type": "V",
    "intent": "V",
    "f8": "reject",
    "f9": "tip"
   },
   {
    "id": "W:140047:3851344438",
    "layer": "F8",
    "model_reply": "",
    "model": null,
    "slovak": "Do konca mesiaca ona prečíta všetky tie správy.",
    "answer": "By the end of the month all those reports will have been read.",
    "reference": "By the end of the month she will have read all those reports.",
    "judge_label": "wrong",
    "judge_type": "V",
    "intent": "V",
    "f8": "reject",
    "f9": "abstain"
   },
   {
    "id": "W:140048:331087784",
    "layer": "F8",
    "model_reply": "",
    "model": null,
    "slovak": "Ten technik vymení rozbité sklo na displeji.",
    "answer": "The broken glass on the display will be replaced by the technician.",
    "reference": "The technician will replace the broken glass on the display.",
    "judge_label": "wrong",
    "judge_type": "V",
    "intent": "V",
    "f8": "reject",
    "f9": "reject"
   },
   {
    "id": "W:140049:1442813517",
    "layer": "F8",
    "model_reply": "",
    "model": null,
    "slovak": "On ti to vysvetlí cestou domov.",
    "answer": "It will be explained to you on the way home.",
    "reference": "He will explain it to you on the way home.",
    "judge_label": "wrong",
    "judge_type": "V",
    "intent": "V",
    "f8": "reject",
    "f9": "tip"
   },
   {
    "id": "W:140050:2745100486",
    "layer": "F8",
    "model_reply": "",
    "model": null,
    "slovak": "Ak my odložíme ten výlet, sprievodca nám vráti peniaze.",
    "answer": "If that trip is postponed, our money will be given back by the guide.",
    "reference": "If we postpone the trip, the guide will give us our money back.",
    "judge_label": "wrong",
    "judge_type": "V",
    "intent": "V",
    "f8": "reject",
    "f9": "accept"
   },
   {
    "id": "W:140053:2537444227",
    "layer": "F8",
    "model_reply": "",
    "model": null,
    "slovak": "Ja budem variť večeru, kým ty upraceš kuchyňu.",
    "answer": "Dinner will be cooked while you tidy up the kitchen.",
    "reference": "I will cook dinner while you tidy the kitchen.",
    "judge_label": "wrong",
    "judge_type": "V",
    "intent": "V",
    "f8": "reject",
    "f9": "tip"
   }
  ],
  "cost_items": []
 },
 "LOCKTIP|F9": {
  "caught_wrong": 58,
  "caught_wrong_only_this_guard": 56,
  "cost_correct_rejected": 6,
  "caught_items": [
   {
    "id": "W:140003:1687614064",
    "layer": "F9",
    "model_reply": "",
    "model": null,
    "slovak": "Moja sestra nosí okuliare iba pri čítaní.",
    "answer": "My sister wore glasses only when she read.",
    "reference": "My sister only wears glasses when she reads.",
    "judge_label": "wrong",
    "judge_type": "T",
    "intent": "TF",
    "f8": "accept",
    "f9": "reject"
   },
   {
    "id": "W:140004:908886435",
    "layer": "F9",
    "model_reply": "",
    "model": null,
    "slovak": "My chodíme do tej pekárne každú sobotu ráno.",
    "answer": "We went to that bakery every Saturday morning.",
    "reference": "We go to that bakery every Saturday morning.",
    "judge_label": "wrong",
    "judge_type": "T",
    "intent": "TF",
    "f8": "accept",
    "f9": "reject"
   },
   {
    "id": "W:140005:3849504101",
    "layer": "F9",
    "model_reply": "",
    "model": null,
    "slovak": "Ty teraz držíš môj dáždnik a ja mrznem.",
    "answer": "You were holding my umbrella and I was freezing.",
    "reference": "You are holding my umbrella now and I am freezing.",
    "judge_label": "wrong",
    "judge_type": "T",
    "intent": "TF",
    "f8": "accept",
    "f9": "reject"
   },
   {
    "id": "W:140006:3299777528",
    "layer": "F9",
    "model_reply": "",
    "model": null,
    "slovak": "Ona nikdy neposiela e-maily po desiatej večer.",
    "answer": "She is never sending emails after ten in the evening.",
    "reference": "She never sends emails after ten in the evening.",
    "judge_label": "wrong",
    "judge_type": "T",
    "intent": "T",
    "f8": "accept",
    "f9": "reject"
   },
   {
    "id": "W:140006:3100171170",
    "layer": "F9",
    "model_reply": "",
    "model": null,
    "slovak": "Ona nikdy neposiela e-maily po desiatej večer.",
    "answer": "She never sends letters after ten in the evening.",
    "reference": "She never sends emails after ten in the evening.",
    "judge_label": "wrong",
    "judge_type": "W",
    "intent": "W",
    "f8": "accept",
    "f9": "reject"
   },
   {
    "id": "W:140006:98216243",
    "layer": "F9",
    "model_reply": "",
    "model": null,
    "slovak": "Ona nikdy neposiela e-maily po desiatej večer.",
    "answer": "Emails are never sent by her after ten in the evening.",
    "reference": "She never sends emails after ten in the evening.",
    "judge_label": "wrong",
    "judge_type": "V",
    "intent": "V",
    "f8": "accept",
    "f9": "reject"
   },
   {
    "id": "W:140007:564289364",
    "layer": "F9",
    "model_reply": "",
    "model": null,
    "slovak": "Oni už dve hodiny čakajú na autobus pred knižnicou.",
    "answer": "They waited for the bus in front of the library for two hours.",
    "reference": "They have been waiting for the bus in front of the library for two hours.",
    "judge_label": "wrong",
    "judge_type": "T",
    "intent": "TF"
```

```
{
 "rejected_in_BASE": 101,
 "rejected_in_BASE_by_layer": {
  "F3": 30,
  "F4v2": 53,
  "F5": 18
 },
 "released_by_LOCKTIP_total": 0,
 "released_judged_correct": 0,
 "released_judged_wrong_by_type": {}
}
```

```
{
 "f8": {
  "accept": 527,
  "reject": 23,
  "abstain": 50
 },
 "f9": {
  "abstain": 54,
  "accept": 282,
  "tip": 196,
  "reject": 68
 }
}
```

## B3 line

```
{
 "tip": {
  "n": 196,
  "judged_correct": 101,
  "judged_wrong": 95,
  "cost_type_T_wrong_accepted": 44
 },
 "abstain": {
  "n": 54,
  "judged_correct": 17,
  "judged_wrong": 37,
  "cost_type_T_wrong_accepted": 15
 }
}
```

## Every false acceptance

- `{"id": "W:140001:1247843749", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ona každé ráno pije zelený čaj s medom.", "answer": "She drinks black tea with honey every morning.", "reference": "She drinks green tea with honey every morning.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "abstain"}`
- `{"id": "W:140001:1857846389", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ona každé ráno pije zelený čaj s medom.", "answer": "She is drinking green tea with honey every morning.", "reference": "She drinks green tea with honey every morning.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "abstain"}`
- `{"id": "W:140001:1986524460", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ona každé ráno pije zelený čaj s medom.", "answer": "She drank green tea with honey every morning.", "reference": "She drinks green tea with honey every morning.", "judge_label": "wrong", "judge_type": "T", "intent": "TF", "f8": "accept", "f9": "abstain"}`
- `{"id": "W:140002:2866884473", "layer": "L1", "model_reply": "", "model": null, "slovak": "On práve teraz umýva staré tenisky v dreze.", "answer": "He washes old sneakers in the sink right now.", "reference": "He is washing his old trainers in the sink right now.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "abstain"}`
- `{"id": "W:140002:3710200961", "layer": "L1", "model_reply": "", "model": null, "slovak": "On práve teraz umýva staré tenisky v dreze.", "answer": "He was washing old sneakers in the sink at that moment.", "reference": "He is washing his old trainers in the sink right now.", "judge_label": "wrong", "judge_type": "T", "intent": "TF", "f8": "accept", "f9": "abstain"}`
- `{"id": "W:140002:4095846223", "layer": "L1", "model_reply": "", "model": null, "slovak": "On práve teraz umýva staré tenisky v dreze.", "answer": "He is washing sneakers in the sink right now.", "reference": "He is washing his old trainers in the sink right now.", "judge_label": "wrong", "judge_type": "M", "intent": "M", "f8": "accept", "f9": "abstain"}`
- `{"id": "W:140002:439765501", "layer": "L1", "model_reply": "", "model": null, "slovak": "On práve teraz umýva staré tenisky v dreze.", "answer": "He is washing old sneakers in the bathtub right now.", "reference": "He is washing his old trainers in the sink right now.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "abstain"}`
- `{"id": "W:140003:2906615050", "layer": "L1", "model_reply": "", "model": null, "slovak": "Moja sestra nosí okuliare iba pri čítaní.", "answer": "My sister wears glasses only when she writes.", "reference": "My sister only wears glasses when she reads.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140003:3069730114", "layer": "L1", "model_reply": "", "model": null, "slovak": "Moja sestra nosí okuliare iba pri čítaní.", "answer": "My brother wears glasses only when he reads.", "reference": "My sister only wears glasses when she reads.", "judge_label": "wrong", "judge_type": "S", "intent": "S", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140003:3714646893", "layer": "L1", "model_reply": "", "model": null, "slovak": "Moja sestra nosí okuliare iba pri čítaní.", "answer": "My sister is wearing glasses only when she reads.", "reference": "My sister only wears glasses when she reads.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140004:2713606607", "layer": "L1", "model_reply": "", "model": null, "slovak": "My chodíme do tej pekárne každú sobotu ráno.", "answer": "We are going to that bakery every Saturday morning.", "reference": "We go to that bakery every Saturday morning.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140004:503587051", "layer": "L1", "model_reply": "", "model": null, "slovak": "My chodíme do tej pekárne každú sobotu ráno.", "answer": "We go to that butcher's every Saturday morning.", "reference": "We go to that bakery every Saturday morning.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140005:172400893", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ty teraz držíš môj dáždnik a ja mrznem.", "answer": "You are holding my coat right now and I am freezing.", "reference": "You are holding my umbrella now and I am freezing.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140005:2571566503", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ty teraz držíš môj dáždnik a ja mrznem.", "answer": "He is holding my umbrella right now and I am freezing.", "reference": "You are holding my umbrella now and I am freezing.", "judge_label": "wrong", "judge_type": "S", "intent": "S", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140005:2888584609", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ty teraz držíš môj dáždnik a ja mrznem.", "answer": "You are holding my umbrella right now.", "reference": "You are holding my umbrella now and I am freezing.", "judge_label": "wrong", "judge_type": "M", "intent": "M", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140005:3933037492", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ty teraz držíš môj dáždnik a ja mrznem.", "answer": "You hold my umbrella now and I freeze.", "reference": "You are holding my umbrella now and I am freezing.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140006:2278841645", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ona nikdy neposiela e-maily po desiatej večer.", "answer": "She never sent emails after ten in the evening.", "reference": "She never sends emails after ten in the evening.", "judge_label": "wrong", "judge_type": "T", "intent": "TF", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140007:2893882477", "layer": "L1", "model_reply": "", "model": null, "slovak": "Oni už dve hodiny čakajú na autobus pred knižnicou.", "answer": "They have been waiting for the train in front of the library for two hours.", "reference": "They have been waiting for the bus in front of the library for two hours.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140007:3612082565", "layer": "L1", "model_reply": "", "model": null, "slovak": "Oni už dve hodiny čakajú na autobus pred knižnicou.", "answer": "They are waiting for the bus in front of the library for two hours.", "reference": "They have been waiting for the bus in front of the library for two hours.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140008:3343297556", "layer": "L1", "model_reply": "", "model": null, "slovak": "Tento vlak zastavuje v každej malej dedine.", "answer": "These trains stop in every small village.", "reference": "This train stops in every small village.", "judge_label": "wrong", "judge_type": "S", "intent": "S", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140008:44334763", "layer": "L1", "model_reply": "", "model": null, "slovak": "Tento vlak zastavuje v každej malej dedine.", "answer": "This train stops in every small town.", "reference": "This train stops in every small village.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140008:779704585", "layer": "L1", "model_reply": "", "model": null, "slovak": "Tento vlak zastavuje v každej malej dedine.", "answer": "This train is stopping in every small village.", "reference": "This train stops in every small village.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140009:2608721653", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ty musíš odovzdať ten formulár ešte dnes popoludní.", "answer": "You must have handed in that form this afternoon.", "reference": "You must hand in that form this afternoon.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140009:3825884284", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ty musíš odovzdať ten formulár ešte dnes popoludní.", "answer": "You have to hand in that form today.", "reference": "You must hand in that form this afternoon.", "judge_label": "wrong", "judge_type": "M", "intent": "M", "f8": "accept", "f9": "abstain"}`
- `{"id": "W:140009:3899325943", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ty musíš odovzdať ten formulár ešte dnes popoludní.", "answer": "You have to hand in that report this afternoon.", "reference": "You must hand in that form this afternoon.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "abstain"}`
- `{"id": "W:140009:614016547", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ty musíš odovzdať ten formulár ešte dnes popoludní.", "answer": "That form must be handed in this afternoon.", "reference": "You must hand in that form this afternoon.", "judge_label": "wrong", "judge_type": "V", "intent": "V", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140010:1635756059", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ona vždy zabudne kľúče, keď sa ponáhľa do práce.", "answer": "She has always forgotten her keys when she hurries to work.", "reference": "She always forgets her keys when she is rushing to work.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140010:3260151351", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ona vždy zabudne kľúče, keď sa ponáhľa do práce.", "answer": "She always forgot her keys when she was rushing to work.", "reference": "She always forgets her keys when she is rushing to work.", "judge_label": "wrong", "judge_type": "T", "intent": "TF", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140010:3421452543", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ona vždy zabudne kľúče, keď sa ponáhľa do práce.", "answer": "Her keys are always forgotten when she is rushing to work.", "reference": "She always forgets her keys when she is rushing to work.", "judge_label": "wrong", "judge_type": "V", "intent": "V", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140010:3507832517", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ona vždy zabudne kľúče, keď sa ponáhľa do práce.", "answer": "She always forgets her wallet when she is rushing to work.", "reference": "She always forgets her keys when she is rushing to work.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140011:1519813314", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ja rád varím cestoviny pre celú rodinu.", "answer": "I am liking cooking pasta for the whole family.", "reference": "I like cooking pasta for the whole family.", "judge_label": "wrong", "judge_type": "E", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140011:1894039854", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ja rád varím cestoviny pre celú rodinu.", "answer": "I like cooking soup for the whole family.", "reference": "I like cooking pasta for the whole family.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140012:1752163963", "layer": "L1", "model_reply": "", "model": null, "slovak": "Sused, ktorý býva nad nami, opravuje bicykle v garáži.", "answer": "The neighbours who live above us repair bicycles in the garage.", "reference": "The neighbour who lives above us repairs bikes in the garage.", "judge_label": "wrong", "judge_type": "S", "intent": "S", "f8": "accept", "f9": "abstain"}`
- `{"id": "W:140012:2859826877", "layer": "L1", "model_reply": "", "model": null, "slovak": "Sused, ktorý býva nad nami, opravuje bicykle v garáži.", "answer": "The neighbour who lives above us repairs bicycles in the basement.", "reference": "The neighbour who lives above us repairs bikes in the garage.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "abstain"}`
- `{"id": "W:140012:3504467124", "layer": "L1", "model_reply": "", "model": null, "slovak": "Sused, ktorý býva nad nami, opravuje bicykle v garáži.", "answer": "The neighbour repairs bicycles in the garage.", "reference": "The neighbour who lives above us repairs bikes in the garage.", "judge_label": "wrong", "judge_type": "M", "intent": "M", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140012:4214409117", "layer": "L1", "model_reply": "", "model": null, "slovak": "Sused, ktorý býva nad nami, opravuje bicykle v garáži.", "answer": "The neighbour who lives above us has been repairing bicycles in the garage.", "reference": "The neighbour who lives above us repairs bikes in the garage.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140013:1784078034", "layer": "L1", "model_reply": "", "model": null, "slovak": "Oni práve natierajú plot na zeleno.", "answer": "They paint the fence green right now.", "reference": "They are painting the fence green right now.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "abstain"}`
- `{"id": "W:140013:2009966541", "layer": "L1", "model_reply": "", "model": null, "slovak": "Oni práve natierajú plot na zeleno.", "answer": "They are painting the gate green right now.", "reference": "They are painting the fence green right now.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140014:1487151881", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ona pracuje na tej diplomovke už tri mesiace.", "answer": "That thesis has been worked on by her for three months.", "reference": "She has been working on that thesis for three months.", "judge_label": "wrong", "judge_type": "V", "intent": "V", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140014:2067027689", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ona pracuje na tej diplomovke už tri mesiace.", "answer": "She has been working on that article for three months.", "reference": "She has been working on that thesis for three months.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140014:877747763", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ona pracuje na tej diplomovke už tri mesiace.", "answer": "She is working on that thesis for three months.", "reference": "She has been working on that thesis for three months.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140015:1109346559", "layer": "L1", "model_reply": "", "model": null, "slovak": "V tejto časti nemocnice sa nefajčí ani na balkóne.", "answer": "In this part of the hospital nobody smokes.", "reference": "Smoking is not allowed in this part of the hospital, not even on the balcony.", "judge_label": "wrong", "judge_type": "M", "intent": "M", "f8": "abstain", "f9": "abstain"}`
- `{"id": "W:140015:3061436926", "layer": "L1", "model_reply": "", "model": null, "slovak": "V tejto časti nemocnice sa nefajčí ani na balkóne.", "answer": "In this part of the hospital nobody smokes, not even in the corridor.", "reference": "Smoking is not allowed in this part of the hospital, not even on the balcony.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "abstain", "f9": "abstain"}`
- `{"id": "W:140015:3832692238", "layer": "L1", "model_reply": "", "model": null, "slovak": "V tejto časti nemocnice sa nefajčí ani na balkóne.", "answer": "In this part of the hospital nobody is smoking, not even on the balcony.", "reference": "Smoking is not allowed in this part of the hospital, not even on the balcony.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "abstain", "f9": "tip"}`
- `{"id": "W:140015:4008240111", "layer": "L1", "model_reply": "", "model": null, "slovak": "V tejto časti nemocnice sa nefajčí ani na balkóne.", "answer": "In this part of the hospital I do not smoke, not even on the balcony.", "reference": "Smoking is not allowed in this part of the hospital, not even on the balcony.", "judge_label": "wrong", "judge_type": "S", "intent": "S", "f8": "abstain", "f9": "tip"}`
- `{"id": "W:140016:1950441795", "layer": "L1", "model_reply": "", "model": null, "slovak": "Hovorí sa, že tá kaviareň na rohu mení majiteľa.", "answer": "I say that the cafe on the corner is changing owners.", "reference": "They say that the café on the corner is changing owners.", "judge_label": "wrong", "judge_type": "S", "intent": "S", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140016:2152319406", "layer": "L1", "model_reply": "", "model": null, "slovak": "Hovorí sa, že tá kaviareň na rohu mení majiteľa.", "answer": "They say that the bakery on the corner is changing owners.", "reference": "They say that the café on the corner is changing owners.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140016:3317519900", "layer": "L1", "model_reply": "", "model": null, "slovak": "Hovorí sa, že tá kaviareň na rohu mení majiteľa.", "answer": "They say that the cafe on the corner has changed owners.", "reference": "They say that the café on the corner is changing owners.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140016:4179737484", "layer": "L1", "model_reply": "", "model": null, "slovak": "Hovorí sa, že tá kaviareň na rohu mení majiteľa.", "answer": "They say that the cafe is changing owners.", "reference": "They say that the café on the corner is changing owners.", "judge_label": "wrong", "judge_type": "M", "intent": "M", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140017:1214041708", "layer": "L1", "model_reply": "", "model": null, "slovak": "On trénoval hodiny pred tým dôležitým zápasom.", "answer": "He has trained for hours before that important match.", "reference": "He trained for hours before that important match.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140017:972294599", "layer": "L1", "model_reply": "", "model": null, "slovak": "On trénoval hodiny pred tým dôležitým zápasom.", "answer": "He trained for hours before that important meeting.", "reference": "He trained for hours before that important match.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140018:1734008643", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ona celý večer písala poznámky do modrého zošita.", "answer": "She was writing notes in the green notebook all evening.", "reference": "She was writing notes in the blue notebook all evening.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140019:1874813325", "layer": "L1", "model_reply": "", "model": null, "slovak": "Oni minulý rok predávali med na trhu pri rieke.", "answer": "Last year they have sold honey at the market by the river.", "reference": "They sold honey at the market by the river last year.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140019:833919966", "layer": "L1", "model_reply": "", "model": null, "slovak": "Oni minulý rok predávali med na trhu pri rieke.", "answer": "Last year they sold jam at the market by the river.", "reference": "They sold honey at the market by the river last year.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140020:1180063305", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ja som ako dieťa zbieral staré mince.", "answer": "I have collected old coins since I was a child.", "reference": "I used to collect old coins as a child.", "judge_label": "wrong", "judge_type": "T", "intent": "TF", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140020:2061152392", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ja som ako dieťa zbieral staré mince.", "answer": "As a child I collected old stamps.", "reference": "I used to collect old coins as a child.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140020:2656999601", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ja som ako dieťa zbieral staré mince.", "answer": "As a child I collected coins.", "reference": "I used to collect old coins as a child.", "judge_label": "wrong", "judge_type": "M", "intent": "M", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140020:60752693", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ja som ako dieťa zbieral staré mince.", "answer": "As a child I have collected old coins.", "reference": "I used to collect old coins as a child.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140021:1257436551", "layer": "L1", "model_reply": "", "model": null, "slovak": "Moja babka nám každú nedeľu piekla jablkový koláč.", "answer": "My grandpa used to bake us an apple cake every Sunday.", "reference": "My grandma used to bake us an apple pie every Sunday.", "judge_label": "wrong", "judge_type": "S", "intent": "S", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140021:1575965194", "layer": "L1", "model_reply": "", "model": null, "slovak": "Moja babka nám každú nedeľu piekla jablkový koláč.", "answer": "My grandma used to bake us an apple cake.", "reference": "My grandma used to bake us an apple pie every Sunday.", "judge_label": "wrong", "judge_type": "M", "intent": "M", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140021:2760644915", "layer": "L1", "model_reply": "", "model": null, "slovak": "Moja babka nám každú nedeľu piekla jablkový koláč.", "answer": "My grandma used to bake us a cherry cake every Sunday.", "reference": "My grandma used to bake us an apple pie every Sunday.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140021:626194671", "layer": "L1", "model_reply": "", "model": null, "slovak": "Moja babka nám každú nedeľu piekla jablkový koláč.", "answer": "My grandma has baked us an apple cake every Sunday.", "reference": "My grandma used to bake us an apple pie every Sunday.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140022:2519933599", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ty si čakal na peróne, keď začalo pršať.", "answer": "You were waiting at the bus stop when it started to rain.", "reference": "You were waiting on the platform when it started raining.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140022:3085903229", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ty si čakal na peróne, keď začalo pršať.", "answer": "You have been waiting on the platform when it started to rain.", "reference": "You were waiting on the platform when it started raining.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140023:2693086715", "layer": "L1", "model_reply": "", "model": null, "slovak": "My sme minulé leto chodili k jazeru takmer denne.", "answer": "Last summer we went to the lake every day.", "reference": "We went to the lake almost every day last summer.", "judge_label": "wrong", "judge_type": "M", "intent": "M", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140023:486401158", "layer": "L1", "model_reply": "", "model": null, "slovak": "My sme minulé leto chodili k jazeru takmer denne.", "answer": "Last summer we went to the river almost every day.", "reference": "We went to the lake almost every day last summer.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140023:498627330", "layer": "L1", "model_reply": "", "model": null, "slovak": "My sme minulé leto chodili k jazeru takmer denne.", "answer": "Last summer we have gone to the lake almost every day.", "reference": "We went to the lake almost every day last summer.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140024:3157801818", "layer": "L1", "model_reply": "", "model": null, "slovak": "On opravoval tú kosačku celé popoludnie a nakoniec to vzdal.", "answer": "He has been fixing that lawnmower all afternoon and finally gave up.", "reference": "He was fixing that lawnmower all afternoon and in the end he gave up.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140024:3893964095", "layer": "L1", "model_reply": "", "model": null, "slovak": "On opravoval tú kosačku celé popoludnie a nakoniec to vzdal.", "answer": "He was fixing that chainsaw all afternoon and in the end he gave up.", "reference": "He was fixing that lawnmower all afternoon and in the end he gave up.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140024:670820885", "layer": "L1", "model_reply": "", "model": null, "slovak": "On opravoval tú kosačku celé popoludnie a nakoniec to vzdal.", "answer": "That lawnmower was being repaired by him all afternoon, and in the end he gave up.", "reference": "He was fixing that lawnmower all afternoon and in the end he gave up.", "judge_label": "wrong", "judge_type": "V", "intent": "V", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140025:1900680444", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ona vtedy učila na základnej škole v malom meste.", "answer": "At that time she taught at a primary school.", "reference": "She was teaching at a primary school in a small town at that time.", "judge_label": "wrong", "judge_type": "M", "intent": "M", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140025:2680602470", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ona vtedy učila na základnej škole v malom meste.", "answer": "At that time she has taught at a primary school in a small town.", "reference": "She was teaching at a primary school in a small town at that time.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140025:3625336803", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ona vtedy učila na základnej škole v malom meste.", "answer": "At that time she teaches at a primary school in a small town.", "reference": "She was teaching at a primary school in a small town at that time.", "judge_label": "wrong", "judge_type": "T", "intent": "TF", "f8": "accept", "f9": "abstain"}`
- `{"id": "W:140025:381646543", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ona vtedy učila na základnej škole v malom meste.", "answer": "At that time she taught at a high school in a small town.", "reference": "She was teaching at a primary school in a small town at that time.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140026:1296074278", "layer": "L1", "model_reply": "", "model": null, "slovak": "Oni sa vlani učili po španielsky cez víkendy.", "answer": "They study Spanish on weekends.", "reference": "They studied Spanish at weekends last year.", "judge_label": "wrong", "judge_type": "T", "intent": "TF", "f8": "accept", "f9": "abstain"}`
- `{"id": "W:140026:130823092", "layer": "L1", "model_reply": "", "model": null, "slovak": "Oni sa vlani učili po španielsky cez víkendy.", "answer": "Last year they have studied Spanish on weekends.", "reference": "They studied Spanish at weekends last year.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140026:25958062", "layer": "L1", "model_reply": "", "model": null, "slovak": "Oni sa vlani učili po španielsky cez víkendy.", "answer": "Last year they studied Italian on weekends.", "reference": "They studied Spanish at weekends last year.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140026:3480693100", "layer": "L1", "model_reply": "", "model": null, "slovak": "Oni sa vlani učili po španielsky cez víkendy.", "answer": "Last year they studied Spanish.", "reference": "They studied Spanish at weekends last year.", "judge_label": "wrong", "judge_type": "M", "intent": "M", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140027:150677901", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ona včera stratila peňaženku v autobuse.", "answer": "She lost her keys on the bus yesterday.", "reference": "She lost her wallet on the bus yesterday.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140027:1939065147", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ona včera stratila peňaženku v autobuse.", "answer": "She has lost her wallet on the bus yesterday.", "reference": "She lost her wallet on the bus yesterday.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140028:3089463743", "layer": "L1", "model_reply": "", "model": null, "slovak": "On rozbil pohár a hneď to upratal.", "answer": "He has broken a glass and cleaned it up right away.", "reference": "He broke a glass and cleaned it up straight away.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140028:344103820", "layer": "L1", "model_reply": "", "model": null, "slovak": "On rozbil pohár a hneď to upratal.", "answer": "He broke a plate and cleaned it up right away.", "reference": "He broke a glass and cleaned it up straight away.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140028:702458438", "layer": "L1", "model_reply": "", "model": null, "slovak": "On rozbil pohár a hneď to upratal.", "answer": "She broke a glass and cleaned it up right away.", "reference": "He broke a glass and cleaned it up straight away.", "judge_label": "wrong", "judge_type": "S", "intent": "S", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140029:1979637763", "layer": "L1", "model_reply": "", "model": null, "slovak": "Keď sme prišli, on už zjedol celú polievku.", "answer": "When we arrived, they had already eaten all the soup.", "reference": "When we arrived, he had already eaten the whole soup.", "judge_label": "wrong", "judge_type": "S", "intent": "S", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140029:2002895061", "layer": "L1", "model_reply": "", "model": null, "slovak": "Keď sme prišli, on už zjedol celú polievku.", "answer": "When we arrived, he had already eaten all the salad.", "reference": "When we arrived, he had already eaten the whole soup.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140029:3783663446", "layer": "L1", "model_reply": "", "model": null, "slovak": "Keď sme prišli, on už zjedol celú polievku.", "answer": "When we arrive, he has already eaten all the soup.", "reference": "When we arrived, he had already eaten the whole soup.", "judge_label": "wrong", "judge_type": "T", "intent": "TF", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140029:734843875", "layer": "L1", "model_reply": "", "model": null, "slovak": "Keď sme prišli, on už zjedol celú polievku.", "answer": "When we arrived, he has already eaten all the soup.", "reference": "When we arrived, he had already eaten the whole soup.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140030:2229921209", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ona odišla skôr, než jej stihli poďakovať.", "answer": "She left before they managed to pay her.", "reference": "She left before they managed to thank her.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140030:3659570311", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ona odišla skôr, než jej stihli poďakovať.", "answer": "She has left before they managed to thank her.", "reference": "She left before they managed to thank her.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140031:27412344", "layer": "L1", "model_reply": "", "model": null, "slovak": "Povedal nám, že ten balík odoslal už v pondelok.", "answer": "We were told that the parcel had already been sent on Monday.", "reference": "He told us that he had sent the parcel on Monday.", "judge_label": "wrong", "judge_type": "V", "intent": "V", "f8": "abstain", "f9": "accept"}`
- `{"id": "W:140031:3476018942", "layer": "L1", "model_reply": "", "model": null, "slovak": "Povedal nám, že ten balík odoslal už v pondelok.", "answer": "He told us that he has already sent the parcel on Monday.", "reference": "He told us that he had sent the parcel on Monday.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "abstain", "f9": "accept"}`
- `{"id": "W:140031:3758773980", "layer": "L1", "model_reply": "", "model": null, "slovak": "Povedal nám, že ten balík odoslal už v pondelok.", "answer": "He told us that he had already sent the letter on Monday.", "reference": "He told us that he had sent the parcel on Monday.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "abstain", "f9": "accept"}`
- `{"id": "W:140031:3863547323", "layer": "L1", "model_reply": "", "model": null, "slovak": "Povedal nám, že ten balík odoslal už v pondelok.", "answer": "They told us that they had already sent the parcel on Monday.", "reference": "He told us that he had sent the parcel on Monday.", "judge_label": "wrong", "judge_type": "S", "intent": "S", "f8": "abstain", "f9": "accept"}`
- `{"id": "W:140032:1273323798", "layer": "L1", "model_reply": "", "model": null, "slovak": "Spýtala sa ma, či ja ovládam ten program.", "answer": "She asked whether I knew how to use that program.", "reference": "She asked me whether I could use that program.", "judge_label": "wrong", "judge_type": "M", "intent": "M", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140032:1504650380", "layer": "L1", "model_reply": "", "model": null, "slovak": "Spýtala sa ma, či ja ovládam ten program.", "answer": "She asked me whether I knew how to install that program.", "reference": "She asked me whether I could use that program.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140032:3242322905", "layer": "L1", "model_reply": "", "model": null, "slovak": "Spýtala sa ma, či ja ovládam ten program.", "answer": "She asked me whether I will know how to use that program.", "reference": "She asked me whether I could use that program.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140032:728184618", "layer": "L1", "model_reply": "", "model": null, "slovak": "Spýtala sa ma, či ja ovládam ten program.", "answer": "I was asked whether I knew how to use that program.", "reference": "She asked me whether I could use that program.", "judge_label": "wrong", "judge_type": "V", "intent": "V", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140033:2379078076", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ten most bol postavený ešte pred vojnou.", "answer": "Those bridges were built before the war.", "reference": "That bridge was built before the war.", "judge_label": "wrong", "judge_type": "S", "intent": "S", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140033:3319088001", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ten most bol postavený ešte pred vojnou.", "answer": "That bridge was built before the flood.", "reference": "That bridge was built before the war.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140033:73954390", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ten most bol postavený ešte pred vojnou.", "answer": "That bridge has been built before the war.", "reference": "That bridge was built before the war.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140034:1144435860", "layer": "L1", "model_reply": "", "model": null, "slovak": "Dom na kopci bol predaný minulý mesiac.", "answer": "The houses on the hill were sold last month.", "reference": "The house on the hill was sold last month.", "judge_label": "wrong", "judge_type": "S", "intent": "S", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140034:3275402476", "layer": "L1", "model_reply": "", "model": null, "slovak": "Dom na kopci bol predaný minulý mesiac.", "answer": "The house on the hill has been sold last month.", "reference": "The house on the hill was sold last month.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140034:477642534", "layer": "L1", "model_reply": "", "model": null, "slovak": "Dom na kopci bol predaný minulý mesiac.", "answer": "The house on the hill was rented last month.", "reference": "The house on the hill was sold last month.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140035:3359169539", "layer": "L1", "model_reply": "", "model": null, "slovak": "Bolo mi povedané, že termín sa už nedá zmeniť.", "answer": "I was being told that the deadline can no longer be changed.", "reference": "I was told that the deadline cannot be changed any more.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140035:4030126794", "layer": "L1", "model_reply": "", "model": null, "slovak": "Bolo mi povedané, že termín sa už nedá zmeniť.", "answer": "I was told that the price can no longer be changed.", "reference": "I was told that the deadline cannot be changed any more.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140035:972062394", "layer": "L1", "model_reply": "", "model": null, "slovak": "Bolo mi povedané, že termín sa už nedá zmeniť.", "answer": "He was told that the deadline can no longer be changed.", "reference": "I was told that the deadline cannot be changed any more.", "judge_label": "wrong", "judge_type": "S", "intent": "S", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140036:154955232", "layer": "L1", "model_reply": "", "model": null, "slovak": "Deti našli pod schodmi malú korytnačku.", "answer": "The children found a turtle under the stairs.", "reference": "The children found a small tortoise under the stairs.", "judge_label": "wrong", "judge_type": "M", "intent": "M", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140036:1748823823", "layer": "L1", "model_reply": "", "model": null, "slovak": "Deti našli pod schodmi malú korytnačku.", "answer": "The children find a small turtle under the stairs.", "reference": "The children found a small tortoise under the stairs.", "judge_label": "wrong", "judge_type": "T", "intent": "TF", "f8": "accept", "f9": "abstain"}`
- `{"id": "W:140036:3759778656", "layer": "L1", "model_reply": "", "model": null, "slovak": "Deti našli pod schodmi malú korytnačku.", "answer": "A small turtle was found under the stairs.", "reference": "The children found a small tortoise under the stairs.", "judge_label": "wrong", "judge_type": "V", "intent": "V", "f8": "abstain", "f9": "accept"}`
- `{"id": "W:140036:468254077", "layer": "L1", "model_reply": "", "model": null, "slovak": "Deti našli pod schodmi malú korytnačku.", "answer": "The child found a small turtle under the stairs.", "reference": "The children found a small tortoise under the stairs.", "judge_label": "wrong", "judge_type": "S", "intent": "S", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140036:492671651", "layer": "L1", "model_reply": "", "model": null, "slovak": "Deti našli pod schodmi malú korytnačku.", "answer": "The children found a small frog under the stairs.", "reference": "The children found a small tortoise under the stairs.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140037:1271826976", "layer": "L1", "model_reply": "", "model": null, "slovak": "My sme ten nábytok zložili za dve hodiny.", "answer": "We put that carpet together in two hours.", "reference": "We put that furniture together in two hours.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "abstain"}`
- `{"id": "W:140037:1538470541", "layer": "L1", "model_reply": "", "model": null, "slovak": "My sme ten nábytok zložili za dve hodiny.", "answer": "That furniture was assembled by us in two hours.", "reference": "We put that furniture together in two hours.", "judge_label": "wrong", "judge_type": "V", "intent": "V", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140038:2530360948", "layer": "L1", "model_reply": "", "model": null, "slovak": "Do stredy ona pripraví podklady pre nového klienta.", "answer": "By Wednesday she prepares the documents for the new client.", "reference": "She will prepare the materials for the new client by Wednesday.", "judge_label": "wrong", "judge_type": "T", "intent": "TF", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140038:3658090883", "layer": "L1", "model_reply": "", "model": null, "slovak": "Do stredy ona pripraví podklady pre nového klienta.", "answer": "By Wednesday she will prepare the documents for the new supplier.", "reference": "She will prepare the materials for the new client by Wednesday.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140038:4179683080", "layer": "L1", "model_reply": "", "model": null, "slovak": "Do stredy ona pripraví podklady pre nového klienta.", "answer": "She will prepare the documents for the new client.", "reference": "She will prepare the materials for the new client by Wednesday.", "judge_label": "wrong", "judge_type": "M", "intent": "M", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140039:3199561509", "layer": "L1", "model_reply": "", "model": null, "slovak": "On ti zajtra pošle nové heslo.", "answer": "He has sent you a new password tomorrow.", "reference": "He will send you the new password tomorrow.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140039:3876894513", "layer": "L1", "model_reply": "", "model": null, "slovak": "On ti zajtra pošle nové heslo.", "answer": "He will send you a new username tomorrow.", "reference": "He will send you the new password tomorrow.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140040:1470546276", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ona to kreslo prenesie do vedľajšej izby.", "answer": "She will move that table into the next room.", "reference": "She will move that armchair into the next room.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140040:2835659270", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ona to kreslo prenesie do vedľajšej izby.", "answer": "That armchair will be moved into the next room.", "reference": "She will move that armchair into the next room.", "judge_label": "wrong", "judge_type": "V", "intent": "V", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140040:3219054984", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ona to kreslo prenesie do vedľajšej izby.", "answer": "She has moved that armchair into the next room.", "reference": "She will move that armchair into the next room.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140041:1273097874", "layer": "L1", "model_reply": "", "model": null, "slovak": "My tú zmluvu podpíšeme bez akýchkoľvek zmien.", "answer": "That contract will be signed by us without any changes.", "reference": "We will sign that contract without any changes.", "judge_label": "wrong", "judge_type": "V", "intent": "V", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140041:1292587313", "layer": "L1", "model_reply": "", "model": null, "slovak": "My tú zmluvu podpíšeme bez akýchkoľvek zmien.", "answer": "We will sign that contract without any delays.", "reference": "We will sign that contract without any changes.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140041:661386254", "layer": "L1", "model_reply": "", "model": null, "slovak": "My tú zmluvu podpíšeme bez akýchkoľvek zmien.", "answer": "We have signed that contract without any changes.", "reference": "We will sign that contract without any changes.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140042:2208272917", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ja ti kúpim tú knihu o vtákoch, ktorú si chcela.", "answer": "I have bought you that book about birds that you wanted.", "reference": "I will buy you that book about birds you wanted.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140042:2453937892", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ja ti kúpim tú knihu o vtákoch, ktorú si chcela.", "answer": "I will buy you that book about flowers that you wanted.", "reference": "I will buy you that book about birds you wanted.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140042:3882057105", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ja ti kúpim tú knihu o vtákoch, ktorú si chcela.", "answer": "I will buy you that book that you wanted.", "reference": "I will buy you that book about birds you wanted.", "judge_label": "wrong", "judge_type": "M", "intent": "M", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140043:3524242853", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ak ona stihne ten vlak, bude doma pred obedom.", "answer": "If she catches that train, she is home before lunch.", "reference": "If she catches that train, she will be home before noon.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140043:3940413671", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ak ona stihne ten vlak, bude doma pred obedom.", "answer": "If she caught that train, she would be home before lunch.", "reference": "If she catches that train, she will be home before noon.", "judge_label": "wrong", "judge_type": "T", "intent": "TF", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140043:650501743", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ak ona stihne ten vlak, bude doma pred obedom.", "answer": "If she catches that bus, she will be home before lunch.", "reference": "If she catches that train, she will be home before noon.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140044:2665024524", "layer": "L1", "model_reply": "", "model": null, "slovak": "Keď on dopíše ten list, hneď ho odnesie na poštu.", "answer": "When he has finished that letter, he takes it straight to the post office.", "reference": "When he finishes that letter, he will take it to the post office right away.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140044:2735166095", "layer": "L1", "model_reply": "", "model": null, "slovak": "Keď on dopíše ten list, hneď ho odnesie na poštu.", "answer": "When he finishes that letter, he will take it straight to the bank.", "reference": "When he finishes that letter, he will take it to the post office right away.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140044:72249142", "layer": "L1", "model_reply": "", "model": null, "slovak": "Keď on dopíše ten list, hneď ho odnesie na poštu.", "answer": "When they finish that letter, they will take it straight to the post office.", "reference": "When he finishes that letter, he will take it to the post office right away.", "judge_label": "wrong", "judge_type": "S", "intent": "S", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140045:2106898255", "layer": "L1", "model_reply": "", "model": null, "slovak": "Oni ten starý plot rozoberú ešte pred zimou.", "answer": "They will take that old gate apart before winter.", "reference": "They will take that old fence apart before winter.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140045:2911258666", "layer": "L1", "model_reply": "", "model": null, "slovak": "Oni ten starý plot rozoberú ešte pred zimou.", "answer": "That old fence will be taken apart before winter.", "reference": "They will take that old fence apart before winter.", "judge_label": "wrong", "judge_type": "V", "intent": "V", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140045:3166935239", "layer": "L1", "model_reply": "", "model": null, "slovak": "Oni ten starý plot rozoberú ešte pred zimou.", "answer": "They have taken that old fence apart before winter.", "reference": "They will take that old fence apart before winter.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140046:1954105172", "layer": "L1", "model_reply": "", "model": null, "slovak": "Vy nám o tom poviete zajtra na stretnutí.", "answer": "You have told us about it tomorrow at the meeting.", "reference": "You will tell us about it at the meeting tomorrow.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140046:468807947", "layer": "L1", "model_reply": "", "model": null, "slovak": "Vy nám o tom poviete zajtra na stretnutí.", "answer": "You will tell us about it tomorrow at the party.", "reference": "You will tell us about it at the meeting tomorrow.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140047:3057479244", "layer": "L1", "model_reply": "", "model": null, "slovak": "Do konca mesiaca ona prečíta všetky tie správy.", "answer": "By the end of the month she had read all those reports.", "reference": "By the end of the month she will have read all those reports.", "judge_label": "wrong", "judge_type": "T", "intent": "TF", "f8": "accept", "f9": "abstain"}`
- `{"id": "W:140047:544912778", "layer": "L1", "model_reply": "", "model": null, "slovak": "Do konca mesiaca ona prečíta všetky tie správy.", "answer": "By the end of the month she has read all those reports.", "reference": "By the end of the month she will have read all those reports.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "abstain"}`
- `{"id": "W:140047:919233", "layer": "L1", "model_reply": "", "model": null, "slovak": "Do konca mesiaca ona prečíta všetky tie správy.", "answer": "By the end of the month she will have read all those emails.", "reference": "By the end of the month she will have read all those reports.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "abstain"}`
- `{"id": "W:140048:1852568827", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ten technik vymení rozbité sklo na displeji.", "answer": "The technician has replaced the broken glass on the display.", "reference": "The technician will replace the broken glass on the display.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140048:2709168082", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ten technik vymení rozbité sklo na displeji.", "answer": "The technician will replace the broken glass on the window.", "reference": "The technician will replace the broken glass on the display.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140048:2941611432", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ten technik vymení rozbité sklo na displeji.", "answer": "The technicians will replace the broken glass on the display.", "reference": "The technician will replace the broken glass on the display.", "judge_label": "wrong", "judge_type": "S", "intent": "S", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140049:2493322517", "layer": "L1", "model_reply": "", "model": null, "slovak": "On ti to vysvetlí cestou domov.", "answer": "He has explained it to you on the way home.", "reference": "He will explain it to you on the way home.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140049:2884081827", "layer": "L1", "model_reply": "", "model": null, "slovak": "On ti to vysvetlí cestou domov.", "answer": "He will explain it to you on the way to work.", "reference": "He will explain it to you on the way home.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140049:3045753096", "layer": "L1", "model_reply": "", "model": null, "slovak": "On ti to vysvetlí cestou domov.", "answer": "I will explain it to you on the way home.", "reference": "He will explain it to you on the way home.", "judge_label": "wrong", "judge_type": "S", "intent": "S", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140050:228159477", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ak my odložíme ten výlet, sprievodca nám vráti peniaze.", "answer": "If we postpone that trip, the guide gives us our money back.", "reference": "If we postpone the trip, the guide will give us our money back.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140050:2348558641", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ak my odložíme ten výlet, sprievodca nám vráti peniaze.", "answer": "If we postpone that trip, the driver will give us our money back.", "reference": "If we postpone the trip, the guide will give us our money back.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140050:2458078304", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ak my odložíme ten výlet, sprievodca nám vráti peniaze.", "answer": "If we postponed that trip, the guide would give us our money back.", "reference": "If we postpone the trip, the guide will give us our money back.", "judge_label": "wrong", "judge_type": "T", "intent": "TF", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140050:642847692", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ak my odložíme ten výlet, sprievodca nám vráti peniaze.", "answer": "If we postpone that trip, the guide will give us our money back at once.", "reference": "If we postpone the trip, the guide will give us our money back.", "judge_label": "wrong", "judge_type": "M", "intent": "M", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140051:287550272", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ona bude celý budúci týždeň pracovať z domu.", "answer": "She will be working from the office all next week.", "reference": "She will be working from home all next week.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140051:3798764222", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ona bude celý budúci týždeň pracovať z domu.", "answer": "She has been working from home all next week.", "reference": "She will be working from home all next week.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140052:1867487852", "layer": "L1", "model_reply": "", "model": null, "slovak": "Oni budú opravovať tú cestu až do jesene.", "answer": "They will be repairing that bridge until autumn.", "reference": "They will be repairing that road until the autumn.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140052:337176167", "layer": "L1", "model_reply": "", "model": null, "slovak": "Oni budú opravovať tú cestu až do jesene.", "answer": "They have been repairing that road until autumn.", "reference": "They will be repairing that road until the autumn.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140052:732299071", "layer": "L1", "model_reply": "", "model": null, "slovak": "Oni budú opravovať tú cestu až do jesene.", "answer": "That road will be repaired until autumn.", "reference": "They will be repairing that road until the autumn.", "judge_label": "wrong", "judge_type": "V", "intent": "V", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140053:3105712230", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ja budem variť večeru, kým ty upraceš kuchyňu.", "answer": "He will cook dinner while you tidy up the kitchen.", "reference": "I will cook dinner while you tidy the kitchen.", "judge_label": "wrong", "judge_type": "S", "intent": "S", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140053:3832174948", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ja budem variť večeru, kým ty upraceš kuchyňu.", "answer": "I will cook lunch while you tidy up the kitchen.", "reference": "I will cook dinner while you tidy the kitchen.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140053:945145905", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ja budem variť večeru, kým ty upraceš kuchyňu.", "answer": "I have cooked dinner while you tidy up the kitchen.", "reference": "I will cook dinner while you tidy the kitchen.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140054:1786545807", "layer": "L1", "model_reply": "", "model": null, "slovak": "On bude čakať pred kinom asi o siedmej.", "answer": "He has been waiting in front of the cinema at about seven.", "reference": "He will be waiting in front of the cinema at about seven.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140054:3459993210", "layer": "L1", "model_reply": "", "model": null, "slovak": "On bude čakať pred kinom asi o siedmej.", "answer": "He will be waiting in front of the theatre at around seven.", "reference": "He will be waiting in front of the cinema at about seven.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140055:2293819291", "layer": "L1", "model_reply": "", "model": null, "slovak": "My budeme sledovať ten zápas u susedov.", "answer": "We will watch that film at the neighbours' place.", "reference": "We will watch that match at the neighbours.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140055:3157502540", "layer": "L1", "model_reply": "", "model": null, "slovak": "My budeme sledovať ten zápas u susedov.", "answer": "That match will be watched at the neighbours' place.", "reference": "We will watch that match at the neighbours.", "judge_label": "wrong", "judge_type": "V", "intent": "V", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140055:4053905332", "layer": "L1", "model_reply": "", "model": null, "slovak": "My budeme sledovať ten zápas u susedov.", "answer": "We have watched that match at the neighbours' place.", "reference": "We will watch that match at the neighbours.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140056:3555448179", "layer": "L1", "model_reply": "", "model": null, "slovak": "Vy budete dostávať tie správy každé ráno.", "answer": "You have been receiving those reports every morning.", "reference": "You will be getting those reports every morning.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140056:3569976594", "layer": "L1", "model_reply": "", "model": null, "slovak": "Vy budete dostávať tie správy každé ráno.", "answer": "You will receive those parcels every morning.", "reference": "You will be getting those reports every morning.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140057:173228741", "layer": "L1", "model_reply": "", "model": null, "slovak": "Keby ona mala viac času, naučila by sa hrať na gitare.", "answer": "If she had more time, she would learn to play the piano.", "reference": "If she had more time, she would learn to play the guitar.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140057:363097722", "layer": "L1", "model_reply": "", "model": null, "slovak": "Keby ona mala viac času, naučila by sa hrať na gitare.", "answer": "If she had more time, she would learn to play the guitar well.", "reference": "If she had more time, she would learn to play the guitar.", "judge_label": "wrong", "judge_type": "M", "intent": "M", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140058:133020611", "layer": "L1", "model_reply": "", "model": null, "slovak": "Keby sme boli odišli skôr, neboli by sme zmeškali ten let.", "answer": "If we had left earlier, we would not have missed that train.", "reference": "If we had left earlier, we would not have missed that flight.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140058:4124720339", "layer": "L1", "model_reply": "", "model": null, "slovak": "Keby sme boli odišli skôr, neboli by sme zmeškali ten let.", "answer": "If we left earlier, we would not miss that flight.", "reference": "If we had left earlier, we would not have missed that flight.", "judge_label": "wrong", "judge_type": "T", "intent": "TF", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140058:4156271032", "layer": "L1", "model_reply": "", "model": null, "slovak": "Keby sme boli odišli skôr, neboli by sme zmeškali ten let.", "answer": "If we had left earlier, that flight would not have been missed.", "reference": "If we had left earlier, we would not have missed that flight.", "judge_label": "wrong", "judge_type": "V", "intent": "V", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140059:1271322346", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ja by som ti požičal auto, ale je v servise.", "answer": "I would lend you the bike, but it is at the garage.", "reference": "I would lend you the car, but it is at the garage.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140060:2368276709", "layer": "L1", "model_reply": "", "model": null, "slovak": "On by ten problém vyriešil za jediné popoludnie.", "answer": "That problem would be solved by him in a single afternoon.", "reference": "He would solve that problem in a single afternoon.", "judge_label": "wrong", "judge_type": "V", "intent": "V", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140060:3177856491", "layer": "L1", "model_reply": "", "model": null, "slovak": "On by ten problém vyriešil za jediné popoludnie.", "answer": "He would solve that problem in a single morning.", "reference": "He would solve that problem in a single afternoon.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140060:510574810", "layer": "L1", "model_reply": "", "model": null, "slovak": "On by ten problém vyriešil za jediné popoludnie.", "answer": "He solved that problem in a single afternoon.", "reference": "He would solve that problem in a single afternoon.", "judge_label": "wrong", "judge_type": "T", "intent": "TF", "f8": "accept", "f9": "abstain"}`
- `{"id": "W:140061:2498202336", "layer": "L1", "model_reply": "", "model": null, "slovak": "Oni by radi pozvali celú triedu na záhradu.", "answer": "They liked to invite the whole class to the garden.", "reference": "They would like to invite the whole class to the garden.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "abstain"}`
- `{"id": "W:140061:2786327549", "layer": "L1", "model_reply": "", "model": null, "slovak": "Oni by radi pozvali celú triedu na záhradu.", "answer": "They were glad to invite the whole class to the garden.", "reference": "They would like to invite the whole class to the garden.", "judge_label": "wrong", "judge_type": "T", "intent": "TF", "f8": "accept", "f9": "abstain"}`
- `{"id": "W:140061:920859961", "layer": "L1", "model_reply": "", "model": null, "slovak": "Oni by radi pozvali celú triedu na záhradu.", "answer": "They would like to invite the whole class to the terrace.", "reference": "They would like to invite the whole class to the garden.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140062:1460655778", "layer": "L1", "model_reply": "", "model": null, "slovak": "Keby si ty povedal pravdu hneď, nikto by sa nehneval.", "answer": "If the truth had been told right away, nobody would have been angry.", "reference": "If you had told the truth right away, nobody would have been angry.", "judge_label": "wrong", "judge_type": "V", "intent": "V", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140062:3011467414", "layer": "L1", "model_reply": "", "model": null, "slovak": "Keby si ty povedal pravdu hneď, nikto by sa nehneval.", "answer": "If you had told the truth right away, nobody would have been surprised.", "reference": "If you had told the truth right away, nobody would have been angry.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140063:1354546233", "layer": "L1", "model_reply": "", "model": null, "slovak": "My by sme tam išli pešo, keby nepršalo.", "answer": "We would walk there if it were not snowing.", "reference": "We would walk there if it was not raining.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140063:3431176735", "layer": "L1", "model_reply": "", "model": null, "slovak": "My by sme tam išli pešo, keby nepršalo.", "answer": "We would go there if it were not raining.", "reference": "We would walk there if it was not raining.", "judge_label": "wrong", "judge_type": "M", "intent": "M", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140064:225979015", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ona by tú skriňu presunula bližšie k oknu.", "answer": "That wardrobe would be moved closer to the window by her.", "reference": "She would move that wardrobe closer to the window.", "judge_label": "wrong", "judge_type": "V", "intent": "V", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140064:3355888801", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ona by tú skriňu presunula bližšie k oknu.", "answer": "She would move that wardrobe closer to the door.", "reference": "She would move that wardrobe closer to the window.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140064:3626910025", "layer": "L1", "model_reply": "", "model": null, "slovak": "Ona by tú skriňu presunula bližšie k oknu.", "answer": "She moved that wardrobe closer to the window.", "reference": "She would move that wardrobe closer to the window.", "judge_label": "wrong", "judge_type": "T", "intent": "TF", "f8": "accept", "f9": "abstain"}`
- `{"id": "W:140065:4007315959", "layer": "L1", "model_reply": "", "model": null, "slovak": "O tom novom moste sa píše vo všetkých novinách.", "answer": "All the newspapers are writing about that new tunnel.", "reference": "That new bridge is written about in all the newspapers.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140065:711887863", "layer": "L1", "model_reply": "", "model": null, "slovak": "O tom novom moste sa píše vo všetkých novinách.", "answer": "All the newspapers have written about that new bridge.", "reference": "That new bridge is written about in all the newspapers.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140066:1096428305", "layer": "L1", "model_reply": "", "model": null, "slovak": "Tie dvere budú natreté do soboty.", "answer": "The window will be painted by Saturday.", "reference": "Those doors will be painted by Saturday.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "abstain", "f9": "accept"}`
- `{"id": "W:140066:2046631959", "layer": "L1", "model_reply": "", "model": null, "slovak": "Tie dvere budú natreté do soboty.", "answer": "The door will be painted.", "reference": "Those doors will be painted by Saturday.", "judge_label": "wrong", "judge_type": "M", "intent": "M", "f8": "abstain", "f9": "accept"}`
- `{"id": "W:140066:2288248859", "layer": "L1", "model_reply": "", "model": null, "slovak": "Tie dvere budú natreté do soboty.", "answer": "You will paint the door by Saturday.", "reference": "Those doors will be painted by Saturday.", "judge_label": "wrong", "judge_type": "S", "intent": "S", "f8": "abstain", "f9": "tip"}`
- `{"id": "W:140066:3480959757", "layer": "L1", "model_reply": "", "model": null, "slovak": "Tie dvere budú natreté do soboty.", "answer": "The door has been painted by Saturday.", "reference": "Those doors will be painted by Saturday.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "abstain", "f9": "tip"}`
- `{"id": "W:140067:11539283", "layer": "L1", "model_reply": "", "model": null, "slovak": "V nedeľu sa tu nepredáva čerstvý chlieb.", "answer": "Fresh bread has not been sold here on Sundays.", "reference": "Fresh bread is not sold here on Sundays.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "abstain", "f9": "tip"}`
- `{"id": "W:140067:128460556", "layer": "L1", "model_reply": "", "model": null, "slovak": "V nedeľu sa tu nepredáva čerstvý chlieb.", "answer": "Fresh milk is not sold here on Sundays.", "reference": "Fresh bread is not sold here on Sundays.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "abstain", "f9": "accept"}`
- `{"id": "W:140067:669168995", "layer": "L1", "model_reply": "", "model": null, "slovak": "V nedeľu sa tu nepredáva čerstvý chlieb.", "answer": "I do not sell fresh bread here on Sundays.", "reference": "Fresh bread is not sold here on Sundays.", "judge_label": "wrong", "judge_type": "S", "intent": "S", "f8": "abstain", "f9": "tip"}`
- `{"id": "W:140068:1460703092", "layer": "L1", "model_reply": "", "model": null, "slovak": "Oznámili nám, že letisko zatvoria kvôli hmle.", "answer": "He informed us that the airport would be closed because of fog.", "reference": "They told us that they would close the airport because of the fog.", "judge_label": "wrong", "judge_type": "S", "intent": "S", "f8": "abstain", "f9": "accept"}`
- `{"id": "W:140068:2252739303", "layer": "L1", "model_reply": "", "model": null, "slovak": "Oznámili nám, že letisko zatvoria kvôli hmle.", "answer": "They informed us that the airport would be closed.", "reference": "They told us that they would close the airport because of the fog.", "judge_label": "wrong", "judge_type": "M", "intent": "M", "f8": "abstain", "f9": "accept"}`
- `{"id": "W:140068:2666826880", "layer": "L1", "model_reply": "", "model": null, "slovak": "Oznámili nám, že letisko zatvoria kvôli hmle.", "answer": "They informed us that the airport would be closed because of snow.", "reference": "They told us that they would close the airport because of the fog.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "abstain", "f9": "accept"}`
- `{"id": "W:140068:636817541", "layer": "L1", "model_reply": "", "model": null, "slovak": "Oznámili nám, že letisko zatvoria kvôli hmle.", "answer": "They informed us that the airport has been closed because of fog.", "reference": "They told us that they would close the airport because of the fog.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "abstain", "f9": "tip"}`
- `{"id": "W:140069:1023611144", "layer": "L1", "model_reply": "", "model": null, "slovak": "Na tej ulici sa parkuje len za poplatok.", "answer": "On that street I can only park for a fee.", "reference": "Parking in that street is only allowed for a fee.", "judge_label": "wrong", "judge_type": "S", "intent": "S", "f8": "abstain", "f9": "accept"}`
- `{"id": "W:140069:2646709907", "layer": "L1", "model_reply": "", "model": null, "slovak": "Na tej ulici sa parkuje len za poplatok.", "answer": "On that street you can only stop for a fee.", "reference": "Parking in that street is only allowed for a fee.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "abstain", "f9": "tip"}`
- `{"id": "W:140069:3099749095", "layer": "L1", "model_reply": "", "model": null, "slovak": "Na tej ulici sa parkuje len za poplatok.", "answer": "On that street parking has only been allowed for a fee.", "reference": "Parking in that street is only allowed for a fee.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "abstain", "f9": "tip"}`
- `{"id": "W:140069:3436189260", "layer": "L1", "model_reply": "", "model": null, "slovak": "Na tej ulici sa parkuje len za poplatok.", "answer": "On that street you can park for a fee.", "reference": "Parking in that street is only allowed for a fee.", "judge_label": "wrong", "judge_type": "M", "intent": "M", "f8": "abstain", "f9": "tip"}`
- `{"id": "W:140069:3478808361", "layer": "L1", "model_reply": "", "model": null, "slovak": "Na tej ulici sa parkuje len za poplatok.", "answer": "On that street you could only park for a fee.", "reference": "Parking in that street is only allowed for a fee.", "judge_label": "wrong", "judge_type": "T", "intent": "TF", "f8": "abstain", "f9": "abstain"}`
- `{"id": "W:140070:1748033921", "layer": "L1", "model_reply": "", "model": null, "slovak": "Tá socha bola odhalená pred dvoma rokmi.", "answer": "That statue was unveiled two months ago.", "reference": "That statue was unveiled two years ago.", "judge_label": "wrong", "judge_type": "W", "intent": "W", "f8": "accept", "f9": "accept"}`
- `{"id": "W:140070:2016858480", "layer": "L1", "model_reply": "", "model": null, "slovak": "Tá socha bola odhalená pred dvoma rokmi.", "answer": "That statue has been unveiled two years ago.", "reference": "That statue was unveiled two years ago.", "judge_label": "wrong", "judge_type": "T", "intent": "T", "f8": "accept", "f9": "tip"}`
- `{"id": "W:140070:531478826", "layer": "L1", "model_reply": "", "model": null, "slovak": "Tá socha bola odhalená pred dvoma rokmi.", "answer": "Those statues were unveiled two years ago.", "reference": "That statue was unveiled two years ago.", "judge_label": "wrong", "judge_type": "S", "intent": "S", "f8": "accept", "f9": "tip"}`

## Every false rejection

- `{"id": "C:140006:1519654563", "layer": "F9", "model_reply": "", "model": null, "slovak": "Ona nikdy neposiela e-maily po desiatej večer.", "answer": "She doesn't ever send emails after ten in the evening.", "reference": "She never sends emails after ten in the evening.", "judge_label": "correct", "judge_type": null, "intent": "C", "f8": "accept", "f9": "reject"}`
- `{"id": "C:140006:4156469434", "layer": "F9", "model_reply": "", "model": null, "slovak": "Ona nikdy neposiela e-maily po desiatej večer.", "answer": "Emails are something she never sends after ten at night.", "reference": "She never sends emails after ten in the evening.", "judge_label": "correct", "judge_type": null, "intent": "C", "f8": "accept", "f9": "reject"}`
- `{"id": "C:140006:717986058", "layer": "F9", "model_reply": "", "model": null, "slovak": "Ona nikdy neposiela e-maily po desiatej večer.", "answer": "She never sends emails after ten in the evening.", "reference": "She never sends emails after ten in the evening.", "judge_label": "correct", "judge_type": null, "intent": "C", "f8": "accept", "f9": "reject"}`
- `{"id": "C:140009:3398740870", "layer": "F9", "model_reply": "", "model": null, "slovak": "Ty musíš odovzdať ten formulár ešte dnes popoludní.", "answer": "You need to turn in that form later today, in the afternoon.", "reference": "You must hand in that form this afternoon.", "judge_label": "correct", "judge_type": null, "intent": "C", "f8": "accept", "f9": "reject"}`
- `{"id": "C:140037:923566", "layer": "F4v2", "model_reply": "", "model": null, "slovak": "My sme ten nábytok zložili za dve hodiny.", "answer": "It took us two hours to assemble that furniture.", "reference": "We put that furniture together in two hours.", "judge_label": "correct", "judge_type": null, "intent": "C", "f8": "accept", "f9": "tip"}`
- `{"id": "C:140048:2590293579", "layer": "F9", "model_reply": "", "model": null, "slovak": "Ten technik vymení rozbité sklo na displeji.", "answer": "The broken screen glass is something the technician is going to swap out.", "reference": "The technician will replace the broken glass on the display.", "judge_label": "correct", "judge_type": null, "intent": "C", "f8": "accept", "f9": "reject"}`
- `{"id": "C:140069:856625898", "layer": "F9", "model_reply": "", "model": null, "slovak": "Na tej ulici sa parkuje len za poplatok.", "answer": "On that street parking is only allowed for a fee.", "reference": "Parking in that street is only allowed for a fee.", "judge_label": "correct", "judge_type": null, "intent": "C", "f8": "abstain", "f9": "reject"}`

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


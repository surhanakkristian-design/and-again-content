# Phase 1k — ALREADY-SEEN DATA — not the headline (Phase 1j holdout replay)

Frozen config: **LOCKTIP+F8+F9 (ALL) / P-FROZEN / TIP-as-rejection on** (F8 True, F9 True, REPORTED_STRICT False).

| metric | value |
|---|---|
| coverage | 178/196 = 90.82% [85.87, 94.47] |
| coverage (kind C only) | 172/186 = 92.47% [87.69, 95.82] |
| FA | 15/294 = 5.10% [2.88, 8.28] |
| FA type T | 2/59 = 3.39% [0.41, 11.71] |
| FA type W | 4/68 = 5.88% [1.63, 14.38] |
| FA type M | 8/64 = 12.50% [5.55, 23.15] |
| FA type S | 0/102 = 0.00% [0.00, 3.55] |
| FA type V | 1/1 = 100.00% [2.50, 100.00] |
| FA type E | 0/0 = 0.00% [0.00, 0.00] |

## Secondary readout (NOT the frozen configuration)

```
{
 "LOCKTIP": {
  "coverage": {
   "k": 182,
   "n": 196,
   "pct": 92.86,
   "ci": [
    88.31,
    96.04
   ]
  },
  "coverage_kindC": {
   "k": 176,
   "n": 186,
   "pct": 94.62,
   "ci": [
    90.34,
    97.39
   ]
  },
  "fa": {
   "k": 18,
   "n": 294,
   "pct": 6.12,
   "ci": [
    3.67,
    9.5
   ]
  },
  "fa_by_type": {
   "T": {
    "k": 3,
    "n": 59,
    "pct": 5.08,
    "ci": [
     1.06,
     14.15
    ]
   },
   "W": {
    "k": 4,
    "n": 68,
    "pct": 5.88,
    "ci": [
     1.63,
     14.38
    ]
   },
   "M": {
    "k": 9,
    "n": 64,
    "pct": 14.06,
    "ci": [
     6.64,
     25.02
    ]
   },
   "S": {
    "k": 1,
    "n": 102,
    "pct": 0.98,
    "ci": [
     0.02,
     5.34
    ]
   },
   "V": {
    "k": 1,
    "n": 1,
    "pct": 100.0,
    "ci": [
     2.5,
     100.0
    ]
   },
   "E": {
    "k": 0,
    "n": 0,
    "pct": null,
    "ci": [
     0.0,
     0.0
    ]
   }
  },
  "fa_by_layer": {
   "L3": 18
  },
  "fr_by_layer": {
   "L3:TIPrej": 5,
   "L3": 6,
   "F5": 1,
   "L2": 2
  }
 },
 "LOCKTIP+F8": {
  "coverage": {
   "k": 181,
   "n": 196,
   "pct": 92.35,
   "ci": [
    87.69,
    95.65
   ]
  },
  "coverage_kindC": {
   "k": 175,
   "n": 186,
   "pct": 94.09,
   "ci": [
    89.66,
    97.01
   ]
  },
  "fa": {
   "k": 18,
   "n": 294,
   "pct": 6.12,
   "ci": [
    3.67,
    9.5
   ]
  },
  "fa_by_type": {
   "T": {
    "k": 3,
    "n": 59,
    "pct": 5.08,
    "ci": [
     1.06,
     14.15
    ]
   },
   "W": {
    "k": 4,
    "n": 68,
    "pct": 5.88,
    "ci": [
     1.63,
     14.38
    ]
   },
   "M": {
    "k": 9,
    "n": 64,
    "pct": 14.06,
    "ci": [
     6.64,
     25.02
    ]
   },
   "S": {
    "k": 1,
    "n": 102,
    "pct": 0.98,
    "ci": [
     0.02,
     5.34
    ]
   },
   "V": {
    "k": 1,
    "n": 1,
    "pct": 100.0,
    "ci": [
     2.5,
     100.0
    ]
   },
   "E": {
    "k": 0,
    "n": 0,
    "pct": null,
    "ci": [
     0.0,
     0.0
    ]
   }
  },
  "fa_by_layer": {
   "L3": 18
  },
  "fr_by_layer": {
   "F8": 1,
   "L3:TIPrej": 5,
   "L3": 6,
   "F5": 1,
   "L2": 2
  }
 },
 "LOCKTIP+F9": {
  "coverage": {
   "k": 179,
   "n": 196,
   "pct": 91.33,
   "ci": [
    86.48,
    94.87
   ]
  },
  "coverage_kindC": {
   "k": 173,
   "n": 186,
   "pct": 93.01,
   "ci": [
    88.34,
    96.23
   ]
  },
  "fa": {
   "k": 15,
   "n": 294,
   "pct": 5.1,
   "ci": [
    2.88,
    8.28
   ]
  },
  "fa_by_type": {
   "T": {
    "k": 2,
    "n": 59,
    "pct": 3.39,
    "ci": [
     0.41,
     11.71
    ]
   },
   "W": {
    "k": 4,
    "n": 68,
    "pct": 5.88,
    "ci": [
     1.63,
     14.38
    ]
   },
   "M": {
    "k": 8,
    "n": 64,
    "pct": 12.5,
    "ci": [
     5.55,
     23.15
    ]
   },
   "S": {
    "k": 0,
    "n": 102,
    "pct": 0.0,
    "ci": [
     0.0,
     3.55
    ]
   },
   "V": {
    "k": 1,
    "n": 1,
    "pct": 100.0,
    "ci": [
     2.5,
     100.0
    ]
   },
   "E": {
    "k": 0,
    "n": 0,
    "pct": null,
    "ci": [
     0.0,
     0.0
    ]
   }
  },
  "fa_by_layer": {
   "L3": 15
  },
  "fr_by_layer": {
   "L3:TIPrej": 5,
   "L3": 6,
   "F9": 3,
   "F5": 1,
   "L2": 2
  }
 },
 "BASE (lock rejects)": {
  "coverage": {
   "k": 166,
   "n": 196,
   "pct": 84.69,
   "ci": [
    78.88,
    89.43
   ]
  },
  "coverage_kindC": {
   "k": 161,
   "n": 186,
   "pct": 86.56,
   "ci": [
    80.8,
    91.11
   ]
  },
  "fa": {
   "k": 14,
   "n": 294,
   "pct": 4.76,
   "ci": [
    2.63,
    7.86
   ]
  },
  "fa_by_type": {
   "T": {
    "k": 2,
    "n": 59,
    "pct": 3.39,
    "ci": [
     0.41,
     11.71
    ]
   },
   "W": {
    "k": 4,
    "n": 68,
    "pct": 5.88,
    "ci": [
     1.63,
     14.38
    ]
   },
   "M": {
    "k": 7,
    "n": 64,
    "pct": 10.94,
    "ci": [
     4.51,
     21.25
    ]
   },
   "S": {
    "k": 0,
    "n": 102,
    "pct": 0.0,
    "ci": [
     0.0,
     3.55
    ]
   },
   "V": {
    "k": 1,
    "n": 1,
    "pct": 100.0,
    "ci": [
     2.5,
     100.0
    ]
   },
   "E": {
    "k": 0,
    "n": 0,
    "pct": null,
    "ci": [
     0.0,
     0.0
    ]
   }
  },
  "fa_by_layer": {
   "L3": 14
  },
  "fr_by_layer": {
   "L2": 20,
   "L3:TIPrej": 5,
   "L3": 4,
   "F5": 1
  }
 }
}
```

```
{
 "LOCKTIP|F8": {
  "caught_wrong": 0,
  "caught_wrong_only_this_guard": 0,
  "cost_correct_rejected": 1,
  "caught_items": [],
  "cost_items": [
   {
    "id": "C:10107:3602000965",
    "layer": "F8",
    "model_reply": "SAME",
    "model": "SAME",
    "slovak": "Terminál bol prázdny; aj tak ona mala pocit, že ju niekto sleduje.",
    "answer": "The terminal was deserted; nevertheless, she had the feeling someone was watching her.",
    "reference": "The terminal was empty; even so, she felt watched.",
    "judge_label": "correct",
    "judge_type": null,
    "intent": null,
    "f8": "reject",
    "f9": "tip"
   }
  ]
 },
 "LOCKTIP|F9": {
  "caught_wrong": 3,
  "caught_wrong_only_this_guard": 3,
  "cost_correct_rejected": 3,
  "caught_items": [
   {
    "id": "W:14697:2838322367",
    "layer": "F9",
    "model_reply": "SAME",
    "model": "SAME",
    "slovak": "Po dopade je na kameňoch trochu šťavy",
    "answer": "After the impact, there was a bit of juice on the rocks.",
    "reference": "After the impact there is a little juice on the stones.",
    "judge_label": "wrong",
    "judge_type": "T",
    "intent": null,
    "f8": "accept",
    "f9": "reject"
   },
   {
    "id": "W:27097:1375088029",
    "layer": "F9",
    "model_reply": "SAME",
    "model": "SAME",
    "slovak": "Jasné, toto námestie má veľa reklám, presne to sme my potrebovali.",
    "answer": "Sure, this square has ads, exactly what we needed.",
    "reference": "Of course this square has many advertisements, exactly what we needed.",
    "judge_label": "wrong",
    "judge_type": "M",
    "intent": null,
    "f8": "accept",
    "f9": "reject"
   },
   {
    "id": "W:2929:1302909327",
    "layer": "F9",
    "model_reply": "SAME",
    "model": "SAME",
    "slovak": "Desivé svetlo úplne zhaslo a nádražie je zase tmavé.",
    "answer": "The scary lights have completely gone out and the station is dark again.",
    "reference": "The eerie light has faded completely, and the yard is dark again.",
    "judge_label": "wrong",
    "judge_type": "S",
    "intent": null,
    "f8": "accept",
    "f9": "reject"
   }
  ],
  "cost_items": [
   {
    "id": "C:27097:1143309800",
    "layer": "F9",
    "model_reply": "",
    "model": null,
    "slovak": "Jasné, toto námestie má veľa reklám, presne to sme my potrebovali.",
    "answer": "Sure, this square has a lot of ads, exactly what we needed.",
    "reference": "Of course this square has many advertisements, exactly what we needed.",
    "judge_label": "correct",
    "judge_type": null,
    "intent": null,
    "f8": "accept",
    "f9": "reject"
   },
   {
    "id": "C:27097:308292309",
    "layer": "F9",
    "model_reply": "SAME",
    "model": "SAME",
    "slovak": "Jasné, toto námestie má veľa reklám, presne to sme my potrebovali.",
    "answer": "Of course, this square has plenty of ads, exactly what we needed.",
    "reference": "Of course this square has many advertisements, exactly what we needed.",
    "judge_label": "correct",
    "judge_type": null,
    "intent": null,
    "f8": "accept",
    "f9": "reject"
   },
   {
    "id": "C:29143:1356951784",
    "layer": "F9",
    "model_reply": "SAME",
    "model": "SAME",
    "slovak": "Ale kdeže, kámo, on to kúpi za svoje vlastné peniaze.",
    "answer": "Oh come on, mate, he's going to buy it with his own money.",
    "reference": "No way, dude, he will buy it with his own money.",
    "judge_label": "correct",
    "judge_type": null,
    "intent": null,
    "f8": "accept",
    "f9": "reject"
   }
  ]
 },
 "BASE (lock rejects)|F8": {
  "caught_wrong": 0,
  "caught_wrong_only_this_guard": 0,
  "cost_correct_rejected": 1,
  "caught_items": [],
  "cost_items": [
   {
    "id": "C:10107:3602000965",
    "layer": "F8",
    "model_reply": "SAME",
    "model": "SAME",
    "slovak": "Terminál bol prázdny; aj tak ona mala pocit, že ju niekto sleduje.",
    "answer": "The terminal was deserted; nevertheless, she had the feeling someone was watching her.",
    "reference": "The terminal was empty; even so, she felt watched.",
    "judge_label": "correct",
    "judge_type": null,
    "intent": null,
    "f8": "reject",
    "f9": "tip"
   }
  ]
 },
 "BASE (lock rejects)|F9": {
  "caught_wrong": 1,
  "caught_wrong_only_this_guard": 1,
  "cost_correct_rejected": 3,
  "caught_items": [
   {
    "id": "W:14697:2838322367",
    "layer": "F9",
    "model_reply": "SAME",
    "model": "SAME",
    "slovak": "Po dopade je na kameňoch trochu šťavy",
    "answer": "After the impact, there was a bit of juice on the rocks.",
    "reference": "After the impact there is a little juice on the stones.",
    "judge_label": "wrong",
    "judge_type": "T",
    "intent": null,
    "f8": "accept",
    "f9": "reject"
   }
  ],
  "cost_items": [
   {
    "id": "C:27097:1143309800",
    "layer": "F9",
    "model_reply": "",
    "model": null,
    "slovak": "Jasné, toto námestie má veľa reklám, presne to sme my potrebovali.",
    "answer": "Sure, this square has a lot of ads, exactly what we needed.",
    "reference": "Of course this square has many advertisements, exactly what we needed.",
    "judge_label": "correct",
    "judge_type": null,
    "intent": null,
    "f8": "accept",
    "f9": "reject"
   },
   {
    "id": "C:27097:308292309",
    "layer": "F9",
    "model_reply": "SAME",
    "model": "SAME",
    "slovak": "Jasné, toto námestie má veľa reklám, presne to sme my potrebovali.",
    "answer": "Of course, this square has plenty of ads, exactly what we needed.",
    "reference": "Of course this square has many advertisements, exactly what we needed.",
    "judge_label": "correct",
    "judge_type": null,
    "intent": null,
    "f8": "accept",
    "f9": "reject"
   },
   {
    "id": "C:29143:1356951784",
    "layer": "F9",
    "model_reply": "SAME",
    "model": "SAME",
    "slovak": "Ale kdeže, kámo, on to kúpi za svoje vlastné peniaze.",
    "answer": "Oh come on, mate, he's going to buy it with his own money.",
    "reference": "No way, dude, he will buy it with his own money.",
    "judge_label": "correct",
    "judge_type": null,
    "intent": null,
    "f8": "accept",
    "f9": "reject"
   }
  ]
 }
}
```

```
{
 "rejected_in_BASE": 310,
 "rejected_in_BASE_by_layer": {
  "L2": 93,
  "F4v2": 55,
  "L3:TIPrej": 17,
  "L3": 116,
  "F5": 13,
  "F3": 14,
  "F2B": 2
 },
 "released_by_LOCKTIP_total": 20,
 "released_judged_correct": 16,
 "released_judged_wrong_by_type": {
  "M": 2,
  "T": 1,
  "S": 1
 }
}
```

```
{
 "f8": {
  "accept": 454,
  "reject": 1,
  "abstain": 35
 },
 "f9": {
  "tip": 161,
  "accept": 248,
  "abstain": 27,
  "reject": 54
 }
}
```

## B3 line

```
{
 "tip": {
  "n": 161,
  "judged_correct": 66,
  "judged_wrong": 95,
  "cost_type_T_wrong_accepted": 2
 },
 "abstain": {
  "n": 27,
  "judged_correct": 13,
  "judged_wrong": 14,
  "cost_type_T_wrong_accepted": 0
 }
}
```

## Every false acceptance

- `{"id": "C:4571:3137414672", "layer": "L3", "model_reply": "SAME", "model": "SAME", "slovak": "Keď ty necháš jednu skrutku uvoľnenú, celá stolička sa kýve.", "answer": "If one screw is left loose, the whole chair rocks.", "reference": "If you leave one screw loose, the whole chair wobbles.", "judge_label": "wrong", "judge_type": "V", "intent": null, "f8": "accept", "f9": "tip"}`
- `{"id": "W:10107:2868656440", "layer": "L3", "model_reply": "SAME", "model": "SAME", "slovak": "Terminál bol prázdny; aj tak ona mala pocit, že ju niekto sleduje.", "answer": "The terminal was empty. She felt like someone was watching her.", "reference": "The terminal was empty; even so, she felt watched.", "judge_label": "wrong", "judge_type": "M", "intent": null, "f8": "accept", "f9": "tip"}`
- `{"id": "W:103:1596877565", "layer": "L3", "model_reply": "SAME", "model": "SAME", "slovak": "O jeho promócii sa hovorí, že bola najhlučnejšia v histórii univerzity.", "answer": "His graduation is said to be the loudest in the university's history.", "reference": "He was handed his diploma in front of the whole stadium, and the confetti came down.", "judge_label": "wrong", "judge_type": "T", "intent": null, "f8": "accept", "f9": "tip"}`
- `{"id": "W:14697:2532470414", "layer": "L3", "model_reply": "SAME", "model": "SAME", "slovak": "Po dopade je na kameňoch trochu šťavy", "answer": "After the impact, there are a few drops of juice on the rocks.", "reference": "After the impact there is a little juice on the stones.", "judge_label": "wrong", "judge_type": "M", "intent": null, "f8": "accept", "f9": "accept"}`
- `{"id": "W:14697:567072060", "layer": "L3", "model_reply": "SAME", "model": "SAME", "slovak": "Po dopade je na kameňoch trochu šťavy", "answer": "There is a bit of juice on the rocks.", "reference": "After the impact there is a little juice on the stones.", "judge_label": "wrong", "judge_type": "M", "intent": null, "f8": "accept", "f9": "accept"}`
- `{"id": "W:2121:4138132892", "layer": "L3", "model_reply": "SAME", "model": "SAME", "slovak": "Spolubývajúci sa ho spýtal, prečo on trávi dve hodiny denne len na to, aby sedel za stolom.", "answer": "His roommate asked him why he spent two hours a day sitting at the desk.", "reference": "The flatmate asked him why he spent two hours a day just sitting at the desk.", "judge_label": "wrong", "judge_type": "M", "intent": null, "f8": "accept", "f9": "accept"}`
- `{"id": "W:2121:832651865", "layer": "L3", "model_reply": "SAME", "model": "SAME", "slovak": "Spolubývajúci sa ho spýtal, prečo on trávi dve hodiny denne len na to, aby sedel za stolom.", "answer": "His roommate asked him why he spends two hours a day just sitting at the desk.", "reference": "The flatmate asked him why he spent two hours a day just sitting at the desk.", "judge_label": "wrong", "judge_type": "T", "intent": null, "f8": "accept", "f9": "tip"}`
- `{"id": "W:28006:2654956435", "layer": "L3", "model_reply": "SAME", "model": "SAME", "slovak": "Každú loď v zálive ty spozoruješ skôr než ktokoľvek iný. Klobúk dole.", "answer": "You'll spot every boat in the harbor before anyone else. Hats off.", "reference": "You spot every boat in the bay before anyone else. Hats off.", "judge_label": "wrong", "judge_type": "W", "intent": null, "f8": "accept", "f9": "accept"}`
- `{"id": "W:2929:120435637", "layer": "L3", "model_reply": "SAME", "model": "SAME", "slovak": "Desivé svetlo úplne zhaslo a nádražie je zase tmavé.", "answer": "The light has completely gone out and the station is dark again.", "reference": "The eerie light has faded completely, and the yard is dark again.", "judge_label": "wrong", "judge_type": "M", "intent": null, "f8": "accept", "f9": "tip"}`
- `{"id": "W:3603:2904065335", "layer": "L3", "model_reply": "SAME", "model": "SAME", "slovak": "Inžinier sa ho spýtal, kedy on privezie pretekárske auto späť do garáže.", "answer": "The engineer asked him when he would bring the race car back to the shop.", "reference": "The engineer asked him when he was bringing the race car back into the garage.", "judge_label": "wrong", "judge_type": "W", "intent": null, "f8": "accept", "f9": "accept"}`
- `{"id": "W:381:1258629268", "layer": "L3", "model_reply": "SAME", "model": "SAME", "slovak": "Kiež by môj kocúr bol taký pokojný ako ten ryšavý v jej náručí.", "answer": "I wish my cat were as calm as that ginger one in her lap.", "reference": "I wish my cat were as calm as the ginger one in her arms.", "judge_label": "wrong", "judge_type": "W", "intent": null, "f8": "accept", "f9": "tip"}`
- `{"id": "W:7458:64129800", "layer": "L3", "model_reply": "SAME", "model": "SAME", "slovak": "Tú grimasu robí každý, však?", "answer": "Everyone makes a grimace, don't they?", "reference": "Everyone makes that face, don't they?", "judge_label": "wrong", "judge_type": "M", "intent": null, "f8": "accept", "f9": "accept"}`
- `{"id": "W:7716:2835019848", "layer": "L3", "model_reply": "SAME", "model": "SAME", "slovak": "Podarilo sa jej vydržať úplne nehybne, kým sa vážka usadila.", "answer": "She managed to stay still until the dragonfly landed.", "reference": "She managed to stay completely still until the dragonfly settled.", "judge_label": "wrong", "judge_type": "M", "intent": null, "f8": "accept", "f9": "accept"}`
- `{"id": "W:8491:1647062954", "layer": "L3", "model_reply": "SAME", "model": "SAME", "slovak": "Ak ty šupku najprv narežeš, granátové jablko sa otvára ľahko.", "answer": "If you score the peel, the pomegranate opens easily.", "reference": "If you score the skin first, the pomegranate opens easily.", "judge_label": "wrong", "judge_type": "M", "intent": null, "f8": "accept", "f9": "accept"}`
- `{"id": "W:8491:2663489786", "layer": "L3", "model_reply": "SAME", "model": "SAME", "slovak": "Ak ty šupku najprv narežeš, granátové jablko sa otvára ľahko.", "answer": "If you score the peel first, the pomegranate opens quickly.", "reference": "If you score the skin first, the pomegranate opens easily.", "judge_label": "wrong", "judge_type": "W", "intent": null, "f8": "accept", "f9": "accept"}`

## Every false rejection

- `{"id": "C:10107:3602000965", "layer": "F8", "model_reply": "SAME", "model": "SAME", "slovak": "Terminál bol prázdny; aj tak ona mala pocit, že ju niekto sleduje.", "answer": "The terminal was deserted; nevertheless, she had the feeling someone was watching her.", "reference": "The terminal was empty; even so, she felt watched.", "judge_label": "correct", "judge_type": null, "intent": null, "f8": "reject", "f9": "tip"}`
- `{"id": "C:12831:1316976507", "layer": "L3:TIPrej", "model_reply": "TIP", "model": "TIP", "slovak": "Mrkva v záhone je neuveriteľne veľká.", "answer": "The carrot in the flower bed's incredibly big.", "reference": "The carrot in the bed is incredibly big.", "judge_label": "correct", "judge_type": null, "intent": null, "f8": "accept", "f9": "tip"}`
- `{"id": "C:16009:4024372226", "layer": "L3", "model_reply": "DIFF", "model": "DIFF", "slovak": "Zvyčajne sedí ticho, ale teraz hlasno kváka", "answer": "Usually it sits quietly, but now it quacks loudly.", "reference": "It usually sits still, but now it is croaking loudly.", "judge_label": "correct", "judge_type": null, "intent": null, "f8": "accept", "f9": "tip"}`
- `{"id": "C:16009:646770511", "layer": "L3", "model_reply": "DIFF", "model": "DIFF", "slovak": "Zvyčajne sedí ticho, ale teraz hlasno kváka", "answer": "It usually sits quietly, but now it's quacking loudly.", "reference": "It usually sits still, but now it is croaking loudly.", "judge_label": "correct", "judge_type": null, "intent": null, "f8": "accept", "f9": "tip"}`
- `{"id": "C:21750:486141418", "layer": "L3:TIPrej", "model_reply": "TIP", "model": "TIP", "slovak": "Ona balí každú knihu do kartónovej krabice.", "answer": "She puts every book into a cardboard box.", "reference": "She packs every book into a cardboard box.", "judge_label": "correct", "judge_type": null, "intent": null, "f8": "accept", "f9": "tip"}`
- `{"id": "C:27097:1143309800", "layer": "F9", "model_reply": "", "model": null, "slovak": "Jasné, toto námestie má veľa reklám, presne to sme my potrebovali.", "answer": "Sure, this square has a lot of ads, exactly what we needed.", "reference": "Of course this square has many advertisements, exactly what we needed.", "judge_label": "correct", "judge_type": null, "intent": null, "f8": "accept", "f9": "reject"}`
- `{"id": "C:27097:308292309", "layer": "F9", "model_reply": "SAME", "model": "SAME", "slovak": "Jasné, toto námestie má veľa reklám, presne to sme my potrebovali.", "answer": "Of course, this square has plenty of ads, exactly what we needed.", "reference": "Of course this square has many advertisements, exactly what we needed.", "judge_label": "correct", "judge_type": null, "intent": null, "f8": "accept", "f9": "reject"}`
- `{"id": "C:29143:1356951784", "layer": "F9", "model_reply": "SAME", "model": "SAME", "slovak": "Ale kdeže, kámo, on to kúpi za svoje vlastné peniaze.", "answer": "Oh come on, mate, he's going to buy it with his own money.", "reference": "No way, dude, he will buy it with his own money.", "judge_label": "correct", "judge_type": null, "intent": null, "f8": "accept", "f9": "reject"}`
- `{"id": "C:29143:1366479064", "layer": "F5", "model_reply": "", "model": null, "slovak": "Ale kdeže, kámo, on to kúpi za svoje vlastné peniaze.", "answer": "No, dude, he will buy it with his own money.", "reference": "No way, dude, he will buy it with his own money.", "judge_label": "correct", "judge_type": null, "intent": null, "f8": "accept", "f9": "accept"}`
- `{"id": "C:3332:2920962177", "layer": "L3:TIPrej", "model_reply": "TIP", "model": "TIP", "slovak": "Ona odmietla opustiť obchod bez toho zeleného overalu.", "answer": "She refused to leave the store without that green overall.", "reference": "She refused to leave the shop without the green jumpsuit.", "judge_label": "correct", "judge_type": null, "intent": null, "f8": "accept", "f9": "accept"}`
- `{"id": "C:7928:2593205770", "layer": "L3", "model_reply": "DIFF", "model": "DIFF", "slovak": "Keby lúč bol slabší, on by ešte mohol žmurkať.", "answer": "Were the beam weaker, it could still be flickering.", "reference": "If the beam were weaker, he could still blink.", "judge_label": "correct", "judge_type": null, "intent": null, "f8": "accept", "f9": "abstain"}`
- `{"id": "C:7928:2607238276", "layer": "L3", "model_reply": "DIFF", "model": "DIFF", "slovak": "Keby lúč bol slabší, on by ešte mohol žmurkať.", "answer": "If the beam were weaker, it could still flicker.", "reference": "If the beam were weaker, he could still blink.", "judge_label": "correct", "judge_type": null, "intent": null, "f8": "accept", "f9": "accept"}`
- `{"id": "C:7928:3435921201", "layer": "L3", "model_reply": "DIFF", "model": "DIFF", "slovak": "Keby lúč bol slabší, on by ešte mohol žmurkať.", "answer": "If the ray were weaker, it might still blink.", "reference": "If the beam were weaker, he could still blink.", "judge_label": "correct", "judge_type": null, "intent": null, "f8": "accept", "f9": "accept"}`
- `{"id": "C:9584:3775863914", "layer": "L3:TIPrej", "model_reply": "TIP", "model": "TIP", "slovak": "Naplno ona šprintuje od chvíle, keď vyštartovala.", "answer": "She has been running full speed ahead since the moment she launched.", "reference": "She has been sprinting flat out since the moment she started.", "judge_label": "correct", "judge_type": null, "intent": null, "f8": "accept", "f9": "tip"}`
- `{"id": "W:18251:1577769256", "layer": "L2", "model_reply": "", "model": null, "slovak": "Z verandy oni sledujú tú búrku.", "answer": "From the porch they watch a storm.", "reference": "They watch the storm from the porch.", "judge_label": "correct", "judge_type": null, "intent": null, "f8": "accept", "f9": "tip"}`
- `{"id": "W:7558:2926388663", "layer": "L2", "model_reply": "", "model": null, "slovak": "Nikdy predtým sme my nevideli takú tichú skupinu pri západe slnka.", "answer": "Never before have we seen such a quiet group at sunset.", "reference": "Never had we seen a group this quiet at sunset.", "judge_label": "correct", "judge_type": null, "intent": null, "f8": "accept", "f9": "tip"}`
- `{"id": "W:7928:1079961112", "layer": "L3", "model_reply": "DIFF", "model": "DIFF", "slovak": "Keby lúč bol slabší, on by ešte mohol žmurkať.", "answer": "If the beam had been weaker, it could still have blinked.", "reference": "If the beam were weaker, he could still blink.", "judge_label": "correct", "judge_type": null, "intent": null, "f8": "accept", "f9": "tip"}`
- `{"id": "W:8491:3020598369", "layer": "L3:TIPrej", "model_reply": "TIP", "model": "TIP", "slovak": "Ak ty šupku najprv narežeš, granátové jablko sa otvára ľahko.", "answer": "If you score the peel first, the pomegranates open easily.", "reference": "If you score the skin first, the pomegranate opens easily.", "judge_label": "correct", "judge_type": null, "intent": null, "f8": "accept", "f9": "accept"}`

## Calls

```
{
 "counted_calls_http200": 667,
 "failed_empty_200": 0,
 "non200_attempts": 0,
 "tokens_in": 208077,
 "tokens_out": 667,
 "spend_usd": 0.05302,
 "phase_budget_remaining": 1333
}
```


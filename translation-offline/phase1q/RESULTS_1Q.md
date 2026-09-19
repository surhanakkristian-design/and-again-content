# Phase 1Q results (replayed offline from the stored verdicts, 0 model calls)

```
{
 "P1": {
  "coverage": {
   "k": 221,
   "n": 300,
   "pct": 73.67,
   "ci": [
    68.3,
    78.56
   ]
  },
  "fa": {
   "k": 3,
   "n": 240,
   "pct": 1.25,
   "ci": [
    0.26,
    3.61
   ]
  }
 },
 "P2": {
  "coverage": {
   "k": 215,
   "n": 299,
   "pct": 71.91,
   "ci": [
    66.44,
    76.93
   ]
  },
  "fa": {
   "k": 5,
   "n": 241,
   "pct": 2.07,
   "ci": [
    0.68,
    4.77
   ]
  }
 },
 "pooled": {
  "coverage": {
   "k": 436,
   "n": 599,
   "pct": 72.79,
   "ci": [
    69.03,
    76.32
   ]
  },
  "fa": {
   "k": 8,
   "n": 481,
   "pct": 1.66,
   "ci": [
    0.72,
    3.25
   ]
  }
 },
 "cells": {
  "agentless_cov": {
   "k": 84,
   "n": 116,
   "pct": 72.41,
   "ci": [
    63.34,
    80.3
   ]
  },
  "agentless_fa": {
   "k": 2,
   "n": 154,
   "pct": 1.3,
   "ci": [
    0.16,
    4.61
   ]
  },
  "timeframe_fa": {
   "k": 3,
   "n": 224,
   "pct": 1.34,
   "ci": [
    0.28,
    3.86
   ]
  },
  "timeframe_cov": {
   "k": 0,
   "n": 0,
   "pct": null,
   "ci": null
  },
  "determiner_cov": {
   "k": 95,
   "n": 120,
   "pct": 79.17,
   "ci": [
    70.8,
    86.04
   ]
  },
  "determiner_fa": {
   "k": 0,
   "n": 7,
   "pct": 0.0,
   "ci": [
    0.0,
    40.96
   ]
  },
  "bypassive_cov": {
   "k": 42,
   "n": 42,
   "pct": 100.0,
   "ci": [
    91.59,
    100.0
   ]
  },
  "plain_cov": {
   "k": 169,
   "n": 271,
   "pct": 62.36,
   "ci": [
    56.3,
    68.15
   ]
  },
  "aspect_cov": {
   "k": 46,
   "n": 50,
   "pct": 92.0,
   "ci": [
    80.77,
    97.78
   ]
  },
  "number_cov": {
   "k": 0,
   "n": 0,
   "pct": null,
   "ci": null
  }
 },
 "M": {
  "M2/correct": {
   "n": 116,
   "accepted": 11,
   "rejected": 105,
   "layers": {
    "F5": 61,
    "L3": 23,
    "L3:TIPrej": 15,
    "F3": 5,
    "F2B": 1
   }
  },
  "M3/wrong": {
   "n": 9,
   "accepted": 0,
   "rejected": 9,
   "layers": {
    "L3": 7,
    "L3:TIPrej": 2
   }
  },
  "M4/wrong": {
   "n": 1,
   "accepted": 0,
   "rejected": 1,
   "layers": {
    "F5": 1
   }
  },
  "M1/correct": {
   "n": 3,
   "accepted": 0,
   "rejected": 3,
   "layers": {
    "L3": 1,
    "F5": 2
   }
  }
 },
 "f5_off_bounds": {
  "n_f5_only_rejections_on_correct": 65,
  "coverage_f5_on": {
   "k": 436,
   "n": 599,
   "pct": 72.79,
   "ci": [
    69.03,
    76.32
   ]
  },
  "coverage_if_all_accepted": {
   "k": 501,
   "n": 599,
   "pct": 83.64,
   "ci": [
    80.43,
    86.51
   ]
  }
 },
 "f5_fresh": {
  "cost_only_k": 65,
  "cost_any_k": 65,
  "cost_n": 599,
  "catches_k": 2,
  "catches_n": 481
 },
 "layers_reject_correct": {
  "F5": 65,
  "L3": 53,
  "L3:TIPrej": 37,
  "F3": 5,
  "F2B": 3
 },
 "layers_reject_wrong": {
  "L3": 393,
  "L3:TIPrej": 78,
  "F5": 2
 },
 "fa_by_wrongtype": {
  "M": {
   "k": 0,
   "n": 10,
   "pct": 0.0,
   "ci": [
    0.0,
    30.85
   ]
  },
  "S": {
   "k": 4,
   "n": 120,
   "pct": 3.33,
   "ci": [
    0.92,
    8.31
   ]
  },
  "T": {
   "k": 3,
   "n": 224,
   "pct": 1.34,
   "ci": [
    0.28,
    3.86
   ]
  },
  "W": {
   "k": 1,
   "n": 127,
   "pct": 0.79,
   "ci": [
    0.02,
    4.31
   ]
  }
 },
 "false_accept_items": [
  {
   "iid": "W:170033:w4",
   "sid": 170033,
   "half": "P1",
   "type": "S",
   "tags": [
    "plain"
   ],
   "level": "A2"
  },
  {
   "iid": "W:170057:w4",
   "sid": 170057,
   "half": "P1",
   "type": "S",
   "tags": [
    "plain"
   ],
   "level": "A2"
  },
  {
   "iid": "W:170058:w1",
   "sid": 170058,
   "half": "P2",
   "type": "T",
   "tags": [
    "agentless",
    "timeframe"
   ],
   "level": "A2"
  },
  {
   "iid": "W:170088:w2",
   "sid": 170088,
   "half": "P2",
   "type": "T",
   "tags": [
    "agentless",
    "timeframe"
   ],
   "level": "B1"
  },
  {
   "iid": "W:170090:w3",
   "sid": 170090,
   "half": "P2",
   "type": "W",
   "tags": [
    "plain"
   ],
   "level": "B1"
  },
  {
   "iid": "W:170096:w5",
   "sid": 170096,
   "half": "P2",
   "type": "S",
   "tags": [
    "number"
   ],
   "level": "B2"
  },
  {
   "iid": "W:170108:w1",
   "sid": 170108,
   "half": "P2",
   "type": "T",
   "tags": [
    "timeframe"
   ],
   "level": "B2"
  },
  {
   "iid": "W:170113:w5",
   "sid": 170113,
   "half": "P1",
   "type": "S",
   "tags": [
    "plain"
   ],
   "level": "B2"
  }
 ],
 "writer_intent_C": {
  "k": 425,
  "n": 480,
  "pct": 88.54,
  "ci": [
   85.35,
   91.25
  ]
 },
 "writerM_judged_correct": {
  "k": 11,
  "n": 119,
  "pct": 9.24,
  "ci": [
   4.71,
   15.94
  ]
 },
 "lever1_cell": {
  "fired": 239,
  "gain": 33,
  "fa_cost": 1,
  "shadow_accept": 49
 },
 "identical": {
  "identical_v0": {
   "k": 65,
   "n": 65,
   "pct": 100.0,
   "ci": [
    94.48,
    100.0
   ]
  },
  "non_identical": {
   "k": 371,
   "n": 534,
   "pct": 69.48,
   "ci": [
    65.38,
    73.36
   ]
  },
  "n_identical_any": 83
 },
 "f6": {
  "rej_correct_all": 4,
  "n_correct": 599,
  "rej_correct_accepted_cost": 4,
  "rej_wrong_all": 12,
  "n_wrong": 481,
  "rej_wrong_accepted_catches": 0,
  "m3_n": 9,
  "m3_stack_accepted": 0,
  "m3_f6_rejects": 0,
  "m3_f6_catches_among_accepted": 0,
  "stackF6_coverage": {
   "k": 432,
   "n": 599,
   "pct": 72.12,
   "ci": [
    68.34,
    75.68
   ]
  },
  "stackF6_fa": {
   "k": 8,
   "n": 481,
   "pct": 1.66,
   "ci": [
    0.72,
    3.25
   ]
  }
 },
 "tokens": {
  "counted_this_run": 1157,
  "prompt_tokens": 471241,
  "output_tokens": 1157,
  "est_usd_paid_rates": 0.0476
 },
 "metrics_runner": {
  "coverage": {
   "k": 436,
   "n": 599,
   "pct": 72.79,
   "ci": [
    69.03,
    76.32
   ]
  },
  "fa": {
   "k": 8,
   "n": 481,
   "pct": 1.66,
   "ci": [
    0.72,
    3.25
   ]
  },
  "coverage_kn": [
   436,
   599
  ],
  "fa_kn": [
   8,
   481
  ],
  "coverage_pct": 72.79,
  "coverage_ci": [
   69.03,
   76.32
  ],
  "fa_pct": 1.66,
  "fa_ci": [
   0.72,
   3.25
  ],
  "accept_table": {
   "accept/correct": 436,
   "reject/wrong": 473,
   "reject/correct": 163,
   "accept/wrong": 8
  }
 },
 "cells_runner": {
  "agentless": {
   "judged_correct": 116,
   "accepted": 84,
   "judged_wrong": 154,
   "false_accepts": 2
  },
  "by-passive": {
   "judged_correct": 42,
   "accepted": 42,
   "judged_wrong": 0,
   "false_accepts": 0
  },
  "determiner": {
   "judged_correct": 120,
   "accepted": 95,
   "judged_wrong": 7,
   "false_accepts": 0
  },
  "aspect": {
   "judged_correct": 50,
   "accepted": 46,
   "judged_wrong": 0,
   "false_accepts": 0
  },
  "timeframe": {
   "judged_correct": 0,
   "accepted": 0,
   "judged_wrong": 224,
   "false_accepts": 3
  },
  "number": {
   "judged_correct": 0,
   "accepted": 0,
   "judged_wrong": 14,
   "false_accepts": 1
  },
  "plain": {
   "judged_correct": 271,
   "accepted": 169,
   "judged_wrong": 145,
   "false_accepts": 4
  },
  "half:P1": {
   "coverage_kn": [
    221,
    300
   ],
   "fa_kn": [
    3,
    240
   ]
  },
  "half:P2": {
   "coverage_kn": [
    215,
    299
   ],
   "fa_kn": [
    5,
    241
   ]
  },
  "lever1": {
   "fired": 239,
   "gain": 33,
   "fa_cost": 1,
   "shadow_accept": 49
  },
  "lever3": {
   "variants_shown": 1080,
   "variants_removed_by_the_tense_filter": 72
  }
 },
 "judge_noise": null,
 "agreement": {
  "cov_diff_points": 1.76,
  "cov_overlap": true,
  "fa_diff_points": -0.82,
  "fa_overlap": true
 }
}
```

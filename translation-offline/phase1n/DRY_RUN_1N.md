# Phase 1N — DRY RUN (no judge label was read, no model call was made)

* config: **LOCKTIP+F8-READOUT-ONLY (TIP-as-rejection on) / P-FROZEN-1N**, model `gemini-3.1-flash-lite`, temperature 0, thinkingBudget 0; F8 decides NOTHING, F9 off, TIP-as-rejection on, arm B
* items 900 over 100 sentences
* chk distribution (COMPUTED, never asserted): `{"correct/match": 33, "wrong/auto": 867}`
* chk steps: `{"auto": 867, "match": 33}`
* L2 lock firings under BASE: **205**   L3-eligible under LOCKTIP: **834**
* unique requests **834**, reusable from a ledger 0, NEW **834**
* counted calls already in phase1n/calls.jsonl: 120; cap 1200; headroom 246
* level spread: `{"A1": 117, "A2": 189, "B1": 324, "B2": 270}`
* writer intents: `{"C": 400, "M": 100, "S": 100, "T": 25, "TF": 175, "W": 100}`
* writer forms: `{"None": 900}`
* writer passive tags: `{"None": 795, "agentless": 22, "by": 83}`
* hygiene: OFF (phase1n/hygiene present: False)

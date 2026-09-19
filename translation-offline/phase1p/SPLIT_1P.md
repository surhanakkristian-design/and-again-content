# Phase 1P — the SPLIT rule, declared before any data exists

Written 19 Sept 2026, **before** `phase1p/data/` contains anything and before any 1P sentence was
read by this agent.

* Within each level, the SIDs are sorted.
* **Odd SID number -> half P1, even SID number -> half P2.**
  The number is the numeric part of the writer SID (`1P001` -> 1, `1P120` -> 120); the assembler's
  numeric sid is `170000 + that number`, so the parity is the same in both spellings.
* 120 sentences -> **60 per half, 15 per level per half** (A1 = 1P001-1P030, A2 = 1P031-1P060,
  B1 = 1P061-1P090, B2 = 1P091-1P120).
* Both halves are reported **separately** (`cells['half:P1']`, `cells['half:P2']` in
  `results_1p.json`) **and pooled** (`metrics`). The pooled figure is the headline.
* The rule is implemented once, in `runner_1p.half_of()` and `assemble_1p.half_of()` — identical
  bodies; `assemble_1p.py` also writes the half into `data/sentences.json` as `tags.half`.

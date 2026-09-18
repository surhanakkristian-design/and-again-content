# Task B — why L2 over-fires. Diagnosis of all 15 DEV L2 false rejections (row 7)

DEV, row 7: **92 items are rejected at L2** — 76 wrong answers correctly vetoed (51 type T, 20 S, 4 M, 1 W),
**15 correct answers wrongly vetoed** (`dev/l2_false_rejections.json`) and 1 further `W`-kind item that the
blind judge called correct (not in the 15: coverage counts `C` items only). Every one of the 15 fails with
`practised grammar span not present`: F1 `pattern_match` misses and F2 `f2_equivalent` returns None.

| # | cause | n | ids |
|---|---|---|---|
| G1 | annotation ↔ Slovak sentence mismatch (lock unsatisfiable in principle) | 3 | `C:103:1864687227`, `C:103:470167683`, `C:103:670219981` |
| G2 | the `g` gender chain is applied to the references but not to the locks | 2 | `C:29691:1286045143`, `C:29691:2714964500` |
| G3 | contraction hides an equivalence F2 already grants (`will` → `be going to`) | 1 | `C:5959:1661102304` |
| G4 | structural paraphrase of the practised grammar (out of bounds: loosening the T test) | 9 | `C:10734:2394971369`, `C:23878:1748591315`, `C:4612:3488329309`, `C:6265:241916334`, `C:6883:1317999482`, `C:7458:1622126333`, `C:7558:358541305`, `C:9244:1251214671`, `C:9495:2507633220` |

## G1 — sid 103, the annotation belongs to another sentence (3)

`sk` = *"O jeho promócii sa hovorí, že bola najhlučnejšia v histórii univerzity."*, but `reference` / `v` /
`lk` / `alt` / `s` describe *"He was handed his diploma in front of the whole stadium, and the confetti came
down."* No DEV item carries the diploma Slovak; the mean token overlap between the three judged-correct
answers and the reference is 0.15, the joint-lowest of all DEV sentences; all three answers render the `sk`
faithfully. The lock `was handed` can therefore never be matched. **Not a lock defect and not fixed here:**
it needs the annotation for 103 to be re-cut against the live sentence. That is a per-sentence change, and
by the SPLIT leakage caveat (138 of 140 sids sit on both sides) a per-sentence edit is not measurable on the
holdout. Flagged for the integrating agent, nothing else.

## G2 — the gender chain never reaches the locks (2)

`reference_hygiene.gender_variants()` expands the accepted references over the annotation's own `g` chain
(`[["He","his"]]`), so *"She drops her guidebook on the church steps!"* is an accepted reference — while
`lk` stays `["his"]`. A learner who takes the she-reading (the Slovak *"Pustí svojho sprievodcu"* leaves
gender open, which is why hygiene wrote the chain at all) writes *her* and is vetoed. Pipeline asymmetry,
fixed: `lock_fix.apply(..., gender=True)`.

## G3 — `expand()` ambiguity tokens hide an existing F2 equivalence (1)

`f2_equivalent` already accepts `will/would` → `be going to` (`GOING`), but `_has()` matches literal token
strings against `expand(toks(answer))`, and `expand` turns *"he's"* into the ambiguity token `is|has`. So
*"he's going to lower the price"* never matched `' is going to '`. Fixed: `_has` now matches a phrase token
against every alternative of an ambiguity token (`contraction=True`). This releases **with a tip**, so it
only helps under TIP = accept.

## G4 — the learner replaced the practised structure (9, deliberately left rejected)

| id | lock | what the learner wrote |
|---|---|---|
| `C:10734:2394971369` | `should have drawn` | *was supposed to draw* |
| `C:23878:1748591315` | `There is` | *This huge stadium **has*** |
| `C:4612:3488329309` | `held` | *were the one holding* |
| `C:6265:241916334` | `being chased` | *to be chased* |
| `C:6883:1317999482` | `will have been walking` | *it'll have been ten years since he started walking* |
| `C:7458:1622126333` | `don't they` | *right?* |
| `C:7558:358541305` | `had we seen` | *have we seen* (tense changed, inversion kept) |
| `C:9244:1251214671` | `were rolling` | *rolled* (aspect dropped) |
| `C:9495:2507633220` | `was rewritten` | *had been rewritten* (tense changed) |

Releasing these needs a tense/aspect/structure-insensitive lock. 51 of the 76 wrong answers L2 correctly
vetoes on DEV are type T, and the last three rows above differ from the reference by exactly the tense or
aspect change that defines type T — so this is the one thing the task forbids. Left as is.

## D4 (the missing `s` ids) — a real pipeline defect, but not a cause of any DEV false rejection

`s` is read **nowhere** in `checker_1h/1i` (no `.get('s')` in the file); the lock's synonym path runs through
`syn_equivalents(phrase)` and the annotation's `alt`, and `lock_equivalent_ok` (§2.1) already consults `alt`.
For all 15 items `syn_equivalents(lock)` is empty and no lock is an `alt` key; 13 of the 15 locks are verb
patterns, where §2.1 does not run at all. `C:6265:241916334`, the item 1h §5 D4 names, fails on
`being chased` → `to be chased`; *Nobody*/*No one* is only what made the app checker say `wrong` and route it
to L2. The backfill is still built and wired (it is the defect named, it costs no tokens, and the lock now
reads `s`): on DEV it adds **62** group ids over 139 sentences (163 already present, 76 alt pairs have no
existing group) — and it releases **0** items, which is the honest measured number.

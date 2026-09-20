# Phase 2F plan — printed before any tokens are spent

20 September 2026. Claude budget **6,500,000** harness tokens. Gemini **HARD CAP 900 calls** across Part 2
and Part 3.1 combined, spend pre-approved to $1.00. **Nothing is written to the DATABASE — SELECT only.**
No deploy, no migration, no push, no checker rule change, no rebase. `phase2c/out/`, `phase2d/out/` and
`phase2e/out/` are INPUT and stay byte-identical (`SHA_inputs_before.txt`, verified again at the end).
Everything is written under `phase2f/` and committed as it is produced. Every long run under `nohup`
(`setsid` does not exist on macOS and killed 2E's first launch). Parts run in order.

## PART 1 — finish Czech (≈ 1.24 M)

**§1.1 the guard.** `run_2f_cz.py` = `run_2e_cz.py` with two changes.
- *2F change 1*: the throughput guard's clock **excludes back-off sleep entirely**. Every `counted:false`
  sleep interval is recorded as `(t0, t1)` and subtracted from elapsed time before tok/s is computed; the
  floor returns to **60 tok/s over 20 minutes** on that corrected clock. 2E raised the floor to 45 min and
  was soft-stopped a second time by two five-step ladders in one run; the fix is to not measure sleep.
- *2F change 2*: `MAX_RETRY` **5 → 3** (2E defect 2). With the §1 batch rule a give-up costs 100 rows, so
  attempts four and five bought nothing and cost ~190,000 tokens.

**§1.2 diagnose `cz_0002_s04_v` BEFORE spending on it.** Nine consecutive 429s across two phases, 919,962
tokens, zero rows; 2D's other give-ups were also `s04` of cz_0002/0003/0004. Before any full-chunk attempt:
byte-for-byte prompt comparison against a chunk that succeeded (length, bytes, encoding, characters the
others lack), what slice position `s04` is and what its rows share, then **one** attempt as two 50-row
halves. If a half succeeds the cause is size or content, not throttling — said plainly, and halves are used
for the remaining refused chunks.

**§1.3 run what is missing.** Adopt every completed `phase2e/out/sessions/` session by COPYING
(`SKIP-DONE … 0 tokens`), with 2E's adoption check (refuse anything that does not parse, did not exit 0, or
does not cover its chunk). Run cz_0004 (20 sessions), cz_0005, and the two refused chunks
(`cz_0002_s04_v` n 5365-5464, `cz_0003_s04_v` n 6365-6464) per §1.2. 2E's §1 batch rule and meta files
unchanged. PAR = 2. **GATE 3 per batch** (random 50, AG v4 and `reader_nom`, bar 12 %, g4 recorded, never
gating). Then the dedicated `lk` pass over the **NEW rows only**, `run_2e_lk.py`'s method unchanged, prompt
sha16 `5fa910459c078539`, PAR = 2; non-exact rate with exact 95 % CP against Czech's pooled 52.44 %
[50.54, 54.34] and Slovak's 51.13 %; any session under 30 % re-run once. Regenerate
`out/annotations_cz_final.jsonl` and `out/upload_cz_final.xlsx` over all rows now present.
**If Part 1 alone exceeds 2.0 M tokens, stop before Part 2 and report.**

## PART 2 — Czech coverage and false acceptance (≈ 3 M, ≈ 600 Gemini calls)

1W's method, language swapped. 100 NEW Czech production sentences, stratified A1/A2/B1/B2, overlapping
nothing in 2C/2D/2E or any Slovak set; annotated with the frozen 2E pipeline including the dedicated `lk`
pass. 4 correct + 5 wrong per sentence = 400/500. **4 blind writers, one per level** (Czech sentence, level,
topic only). **ONE blind judge**, items shuffled ACROSS levels, **80 hidden duplicate controls**; packets
carry `jid / czech / level / answer / topic`. The judge gets the owner's acceptance rules verbatim. Floors on
**judged-wrong** counts checked BEFORE the run: agent drops ≥ 120, time-frame shifts ≥ 100, T/W/M/S otherwise
balanced, judged-correct by-passives ≥ 60; sensitivities pre-declared and none may come out empty.
L3 = **gemini-3.1-flash-lite, temperature 0, thinkingBudget 0**, frozen 1W stack + the Czech reader from
1T/2C. Tune nothing; record defects. Reported as 1W reports: pooled / P1 (odd sid) / P2 (even sid), each
k/n with exact Clopper–Pearson and Fisher, both targets on the POINT and the INTERVAL, never averaged, every
figure under every sensitivity, one cell per line, **the Slovak 1W figure beside every Czech one**.

## PART 3

- **3.1** Slovak on PRODUCTION sentences, labelled a **PROBE**: 60 sentences from
  `annotations_sk_final.jsonl`, one blind writer, 3 correct + 3 wrong each (360 items), one blind judge,
  frozen stack, ≈ 250 Gemini calls inside the same 900 cap; reported beside 1W's 97.76 % / 3.21 %.
- **3.2** Pricing the other six languages (de, fr, es, tr, hu, ua), **0 Gemini calls**: which frozen guards
  read Slovak-specific morphology and would silently misread each, named file and line; which become moot for
  the non-pro-drop natives and what replaces them; ua is Cyrillic so every ending rule is rewritten; a cost
  table for variant 2 (1,000 concepts each) at the measured sk/cz rates plus an engineering estimate anchored
  on what Czech actually took; and which single language is cheapest next.
- **3.3** `phase2f/STATUS.md`, one page, numbers and sources only, no recommendations.

## Transport and evidence

counted = http 200 only; http 0/429/5xx retried with logged `counted:false` back-off; an empty or unparsable
200 is a FAILED call — counted, never guessed, never silently retried. (item, variant) pairs interleaved and
shuffled so an outage damages all cells equally. The stack is frozen and committed before any measurement set
is opened; FREEZE hash and RUN commit recorded; `FINAL_RUN_DONE` written; the access log published verbatim.
**Each set is opened ONCE.**

## Budget arithmetic

| item | tokens |
|---|---|
| Part 1 annotation (cz_0004 20 sess, cz_0005, 2 refused chunks) | ≈ 740,000 |
| Part 1 `lk` over the new rows | ≈ 500,000 |
| Part 2 (writers, judge, annotation of 100 sentences, scoring) | ≈ 3,000,000 |
| Part 3.1 probe | ≈ 400,000 |
| Part 3.2 + 3.3 + main session + agents | ≈ 450,000 |
| **projected total** | **≈ 5,090,000 of 6,500,000** |

Cumulative tokens and the projected total are printed after every batch and stage; the run **STOPS and the
report is written** rather than exceed 6.5 M. Part 1 has its own 2.0 M tripwire.

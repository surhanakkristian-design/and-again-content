# Phase 1j — DEV / HOLDOUT split BY SENTENCE

Produced by `phase1j/make_split_1j.py` (zero model calls). Source: the union of `phase1i/dev` and
`phase1i/holdout` — 980 judged answers over 140 Slovak sentences, plus both annotation files.

## Rule

```
order = sorted(sids, key=lambda s: sha256(("phase1j|%s" % s).encode()).hexdigest())
DEV = order[:70]      HOLDOUT = order[70:]
```

Per SENTENCE, so **no sid is on both sides** (asserted) — this closes the Phase 1i leakage caveat:
a per-sentence change (an annotation edit, a reference rewrite, a rewritten Slovak sentence, a list
keyed to a sid) made on DEV is now measurable on the HOLDOUT.

## Counts

| figure | DEV | HOLDOUT | total |
|---|---|---|---|
| items | 490 | 490 | 980 |
| sentences (sids) | 70 | 70 | 140 |
| judged correct (blind gold) | 215 | 215 | 430 |
| judged wrong (blind gold) | 275 | 275 | 550 |
| coverage denominator (kind C, judged correct) | 210 | 210 | 420 |
| false-acceptance denominator (judged wrong) | 275 | 275 | 550 |
| items that were on the Phase 1i DEV side (tuned on) | 238 | 229 | 467 |
| items that were on the Phase 1i HOLDOUT side | 252 | 261 | 513 |

### Wrong answers by type — written / judged really wrong

| type | DEV | HOLDOUT | CP half-width at 5 % (DEV / HOLDOUT, pp) |
|---|---|---|---|
| T | 70 / 69 | 70 / 68 | 5.6 / 5.7 |
| W | 70 / 70 | 70 / 68 | 6.2 / 5.7 |
| M | 70 / 66 | 70 / 69 | 5.9 / 5.6 |
| S | 70 / 70 | 70 / 70 | 6.2 / 6.2 |

### OLD (the 80 in-sample sentences) vs NEW (the 60 fresh ones)

| half | DEV items | DEV sentences | HOLDOUT items | HOLDOUT sentences |
|---|---|---|---|---|
| OLD | 266 | 38 | 294 | 42 |
| NEW | 224 | 32 | 196 | 28 |

## Are the T/W/M/S cells too small?

A per-type cell of n really-wrong answers measures a 5 % false-acceptance rate with the exact
Clopper-Pearson half-widths in the table above. Read them as the resolution of that cell: a cell
with a half-width of ~5 pp can separate 5 % from ~15 %, not 5 % from 8 %.
**No cell is genuinely too small**: every type keeps enough really-wrong answers for a 5 % rate.
The whole-side FA denominators (DEV 275, HOLDOUT 275) stay the headline; the per-type cells are
diagnostic only and must never carry a decision on their own.

## Leakage from Phase 1i — RECORDED

238 DEV items and 229 HOLDOUT items were on the Phase 1i DEV side, i.e. their *answers* were visible
while the frozen 1i configuration (P-E4b, TIP=reject, F4v3, Task B fixes) was chosen. The Phase 1j
HOLDOUT is therefore a clean holdout for everything DESIGNED IN PHASE 1J, and an optimistic bound
for the inherited 1i configuration. Report both readings.

## Files

- `split/dev_sids.json`, `split/holdout_sids.json`, `split/split_counts.json`
- `dev/items.jsonl`, `holdout/items.jsonl` — all Phase 1i fields + `side_1i`
- `dev/annotations.json`, `holdout/annotations.json`
- `dev/sentences.jsonl` (70), `sentences_all.jsonl` (140) — answer-free, verdict-free
- `loader_1j.py` — the only sanctioned reader; `access_log.jsonl` — every read


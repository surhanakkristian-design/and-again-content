# Phase 1k — Task A: the relabelling, DEV (agent R)

New DEV labels = the blind judge's §0 verdicts, **adopted in full (label AND type)** for all 490 DEV items. Movement is measured against the Phase 1j arm-B **primary** labels. Large movement is expected: §0 changed what "correct" means. No number below may be compared with a Phase 1j number that used the old definition.

## Conventions declared for this phase

- **labels** — the blind judge's §0 verdicts adopted IN FULL (label AND type) for all 490 DEV items
- **coverage_denominator** — ALL items judged correct (any id kind); the kind-C-only figure is printed as a secondary line for continuity with 1j
- **fa_denominator** — all items judged wrong
- **types** — T / W / M / S / V (voice, new) / E

## Movement, Phase 1j arm-B primary -> Phase 1k judge

| direction | n |
|---|---|
| items compared | 490 |
| unchanged | 452 |
| correct -> wrong | 5 |
| wrong -> correct | 5 |
| wrong -> wrong, type changed | 28 |
| DEV items without a judge verdict | 0 |

**correct -> wrong, by NEW type:** `{"M": 1, "V": 3, "W": 1}`

**wrong -> correct, by OLD type:** `{"S": 1, "T": 2, "M": 2}`

**wrong -> correct, by the layer that rejected them in the frozen 1j arm-B run (TIP on):** `{"accepted": 2, "L2 lock": 2, "L3": 1}`

**wrong -> wrong type matrix (old -> new):** `{"S->W": 7, "S->M": 5, "T->W": 5, "T->M": 2, "T->V": 1, "S->V": 1, "M->V": 1, "W->T": 1, "S->T": 1, "M->T": 1, "T->E": 1, "T->S": 2}`

## Cell sizes

- Phase 1j arm-B primary: `{"wrong:S": 111, "correct": 189, "wrong:T": 64, "wrong:W": 64, "wrong:M": 62}`
- Phase 1k judge (new): `{"wrong:S": 98, "correct": 189, "wrong:M": 66, "wrong:V": 6, "wrong:W": 76, "wrong:T": 54, "wrong:E": 1}`


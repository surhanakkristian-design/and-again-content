# Phase 1L — F9 hand-check re-validation over the 140 existing sentences

Method and format of Phase 1k report §4. No answers, no labels, 0 model calls.

## Unit test of the 2.2 fix (sentence quoted from the brief, not read from fresh data)

```
sentence  : Ona nikdy neposiela e-maily po desiatej večer
phase1k f9: ['past']  (l-participle "neposiela")
phase1l f9: ['present']  (imperfective present "neposiela")
```

### phase1k f9 (frozen — reference)

| side | n | agree | conservative | error | rate | CP 95 % |
|---|---|---|---|---|---|---|
| DEV | 70 | 63 | 7 | 0 | 0.00 % | [0.00, 5.13] |
| HOLDOUT | 70 | 67 | 3 | 0 | 0.00 % | [0.00, 5.13] |
| ALL | 140 | 130 | 10 | 0 | 0.00 % | [0.00, 2.60] |

errors: 0

### phase1l f9 WITH the 2.2 fix — THE re-validation

| side | n | agree | conservative | error | rate | CP 95 % |
|---|---|---|---|---|---|---|
| DEV | 70 | 63 | 7 | 0 | 0.00 % | [0.00, 5.13] |
| HOLDOUT | 70 | 67 | 3 | 0 | 0.00 % | [0.00, 5.13] |
| ALL | 140 | 130 | 10 | 0 | 0.00 % | [0.00, 2.60] |

errors: 0

## Sentences whose F9 frame moved because of the 2.2 fix

none

# Wave 1 de (German): report part

Status: STOPPED for good at the writers stage (2026-09-22T12:39:09Z). All four blind writer sessions (A1, A2, B1, B2) failed after about 3.5 s each with the headless Claude usage limit: "You've hit your weekly limit, resets 11am (Europe/Vienna)". Per the task rules (STOP_quota.md) the chain was not relaunched.

## Headline (coverage and FA)

Not measured. No writers, no judges, no items, no freeze, and the fresh set was NOT opened by the frozen stack. There is no HEADLINE.json, so there is no coverage, FA, CP interval, L3-only line or content-check result. Both targets: not measured.

## Stages that ran

| Stage | Result |
|---|---|
| preflight | 13/13 PASS (0 Gemini calls, 0 headless sessions, all mocked) |
| projection | 953,619 of 1,300,000 projected, WITHIN budget |
| make_set | 100 sentences picked, 25 per level; 460 rows excluded as used before |
| mock | MOCK PASS, spawns 10, stack 900/900 |
| writers | FAIL: usage_limit on all 4 sessions |

Fresh-set stats per level:

| Level | level rows | my slots | empty | excluded (used before) | picked |
|---|---|---|---|---|---|
| A1 | 1174 | 392 | 127 | 19 | 25 |
| A2 | 1220 | 407 | 148 | 24 | 25 |
| B1 | 885 | 295 | 209 | 7 | 25 |
| B2 | 785 | 262 | 184 | 7 | 25 |

The set exists in `partD/set/` but it was never opened (no Gemini step ran), so it stays unopened and reusable.

## Part A data findings (SELECT only)

Rows: 4064 (db count {'d': 4064, 'n': 4064}), per level {'B2': 785, 'B1': 885, 'A2': 1220, 'A1': 1174}, duplicate groups 0, rows sha256 `e040f6727494540a5d233ec1248293ab28566538acfedd455903a4067cbc73e3`.

| Finding | Count |
|---|---|
| empty | 2015 |
| foreign_letters | 2 |
| no_final_punctuation | 2 |

Empty (no German and no English full_sentence) by level: A1 395, A2 431, B1 645, B2 544 (total 2015, that is about half of the 4,064 rows).

Every other flagged row:

- foreign_letters: exercise 29171 (A1): de = 'Warum antwortet sie nicht? Dieses Café ist ein Albtraum!'; en = None
- foreign_letters: exercise 29183 (A2): de = 'Auf dem Cafétisch ist ein Buch, also liest sie es.'; en = None
- no_final_punctuation: exercise 1228 (B1): de = '„Ich könnte hier keine Stunde ohne Handy sitzen.“ - „Er auch nicht, offenbar.“'; en = None
- no_final_punctuation: exercise 3046 (B1): de = 'Sein Hemd ist durchgeschwitzt, weil er sich schon vom Fuß des Hügels an gegen den Karren stemmt'; en = None

Part B: German has no Part B rewrite.

## False acceptances, false rejections, judge noise

None measured (the stages did not run).

## Gemini

0 calls, 0 spend. No GEMINI_LEDGER.json was written.

## Claude tokens

| Session | Tokens |
|---|---|
| writers A1#1 | 0 (usage limit, 3.5 s) |
| writers A2#1 | 0 (usage limit, 3.7 s) |
| writers B1#1 | 0 (usage limit, 3.6 s) |
| writers B2#1 | 0 (usage limit, 3.7 s) |
| judges | not run |

Headless total for this language: 0. My own agent session: about 25k tokens (estimate).

## Freeze and access

No freeze hash, no FREEZE_COMMIT, no RUN_COMMIT: the chain stopped before freeze. Access log: the set was opened 0 times.

## Defects noticed (recorded, not fixed)

- The projection step does not check the remaining weekly Claude quota, so it reported WITHIN budget with the account already at its weekly limit. Suggestion: add a cheap one-line probe session before the writers.
- Part A: 2,015 of 4,064 German rows (49.6 %) have no German and no English full_sentence. That is a data gap, not a pipeline fault.
- Two STOP files were written for the same event (STOP_quota.md and STOP_usage_limit.md).

## Resume

After the weekly limit resets (11am Europe/Vienna), relaunch the chain for de. The set is unopened and the stages before the writers cost 0.


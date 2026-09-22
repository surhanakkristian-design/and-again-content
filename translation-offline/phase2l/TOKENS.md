# Phase 2L S3 (Part E) Claude token budget

Budget for this stage: 1,400,000 tokens incl. every headless session and the S3 agent.

## Projection (from phase2j/TOKENS.jsonl, the 2J Part D writer + judge sessions)

| item | 2J actual | projection (x1.15) |
|---|---:|---:|
| 4 blind writers (S6) | 225,497 | 259,321 |
| 4 judges (S7, opus, max_turns 2) | 340,352 | 391,404 |
| reserve: one judge retry (largest 2J judge 135,625) | - | 155,968 |
| S3 agent (own context) | - | 200,000 |
| **total** | | **1,006,693** |

Verdict: WITHIN budget. Headless reservation cap enforced in pipeline.py = 1,200,000; each judge session capped at 400,000 (reservation before spawn + wall kill 2,400 s + post-hoc check; a breach is recorded and stops the chain).

## Actual (appended per session)

- writers A1#1: 53,925 tokens (ok, 92.2s)
- writers A2#1: 57,949 tokens (ok, 125.3s)
- writers B1#1: 52,987 tokens (ok, 101.4s)
- writers B2#1: 54,906 tokens (ok, 102.7s)
- cumulative headless after writers: 219,767

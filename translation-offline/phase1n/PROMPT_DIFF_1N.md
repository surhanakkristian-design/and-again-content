# Phase 1N — P-FROZEN vs P-FROZEN-1N (verbatim)

The L3 user body is built by `phase1k/runner_1k.build_req`. Under `P-FROZEN` the extra lines
appended between the P-B head and the tail `SAME, TIP or DIFF?` are, in this order:

1. (only when the annotation carries `g`) the gender line `pipeline_1i.GENDER_TMPL`
2. `pipeline_1i.GROUND_LINE`
3. `pipeline_1i.WORDING_LINE`

**P-FROZEN contains NO voice rule at all** (the voice rule lives in `runner_1k.NEW_RULES[1]`, which
is appended only for `prompt_id == 'P-1K'`). The 1M measurement — including its 30.68 % agent-
demotion cell — was therefore made under a prompt silent on voice. Phase 1N replaces that silent
voice line with its explicit OPPOSITE; everything else is byte-identical, because
`runner_1n.build_req_1n` takes the finished `P-FROZEN` body from the original builder and inserts
exactly one line after `WORDING_LINE`.

## BEFORE (P-FROZEN) — the voice position, verbatim

```
The SLOVAK sentence is the ground truth and the English reference is only one valid rendering of it; judge the learner against the Slovak, not against the reference wording.
A synonym, a different word order or a different phrasing that keeps the Slovak meaning is SAME; a word that changes which thing, person, place, time or quantity the Slovak names is DIFF.
SAME, TIP or DIFF?
```

(no voice line; for reference, the rule 1N inverts is `runner_1k.NEW_RULES[1]`, verbatim:
"Voice: if the Slovak names an agent in the nominative and the learner sentence moves that agent out
of subject position or drops it (an active Slovak sentence turned into an English passive), that is
DIFF. Where the Slovak is itself impersonal or passive, an English passive is SAME.")

## AFTER (P-FROZEN-1N) — the same body with ONE line inserted, verbatim

```
The SLOVAK sentence is the ground truth and the English reference is only one valid rendering of it; judge the learner against the Slovak, not against the reference wording.
A synonym, a different word order or a different phrasing that keeps the Slovak meaning is SAME; a word that changes which thing, person, place, time or quantity the Slovak names is DIFF.
Voice: if the Slovak names an agent in the nominative and the learner sentence moves that agent out of subject position or drops it (an active Slovak sentence turned into an English passive), that is SAME, provided the meaning is preserved. Where the Slovak is itself impersonal or passive, an English passive is SAME.
SAME, TIP or DIFF?
```

## What changed

* inserted, nothing else: `runner_1n.VOICE_SAME_LINE`, the opposite of `NEW_RULES[1]`
  (`DIFF` -> `SAME, provided the meaning is preserved`); the second sentence of the rule is kept
  word for word, since its polarity is already SAME.
* the system text (`lib_prev.SYS`), the P-B head/tail, the gender line, GROUND_LINE, WORDING_LINE
  and `GEN_CFG` (temperature 0, maxOutputTokens 24, thinkingBudget 0) are untouched.
* consequence: `req_hash` changes for every item, so no stored 1M verdict is reusable — the 1N
  side is paid for in full, and the 1200-call phase cap is the binding constraint.

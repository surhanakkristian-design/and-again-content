# HANDOFF - agent G: F9 (time frame) and F8 (voice), Phase 1k task B

Both guards are 100 % offline: no model call, no API, no network, no DB, no app code. Files: `/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase1k/taskB/f9.py`, `/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase1k/taskB/f8.py`.

## Validation headline

F9 `sk_frame` vs hand gold on all 140 arm-B Slovak sentences: **0 errors / 140 = 0.00 %, CP95 [0.00, 2.60] -> FREEZABLE** (DEV 63 agree / 7 conservative / 0 errors; HOLDOUT 67 / 3 / 0). Pre-fix: 7/140 = 5.00 %, not freezable. F8 `sk_agent`: 0 errors / 140 (122 agree, 18 conservative); 1 error before the fix. Details in `F9_VALIDATION.md`.

## API

```python
import sys; sys.path.insert(0, "/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase1k/taskB")
import f9, f8                      # run python with -B
ann = annotations_b_dev.get(str(sid))          # {"hygienised": {...}, "raw": {...}} or None
r9 = f9.check(sk, ann, answer)     # {"verdict": "reject"|"accept"|"tip"|"abstain", "sk":…, "en":…, "reason":…}
r8 = f8.check(sk, ann, answer)     # {"verdict": "reject"|"accept"|"abstain", "sk":…, "en":…, "reason":…}
if r9["verdict"] == "reject" or r8["verdict"] == "reject":
    accepted = False               # a guard may only turn an acceptance into a rejection
tips = [r["reason"] for r in (r9, r8) if r["verdict"] == "tip"]
f9.sk_frame(sk)                    # {"frames": [...], "verdict": str|set|None, "clauses": [...], "reason": …}
f9.en_frame(answer)                # {"frame": "past"|"present"|"future"|"conditional"|None, "perfect": bool, …}
f8.sk_agent(sk)                    # {"agent_nom": True|False|None, "agent": tok, "voice_sk": …, "reason": …}
```

`abstain` = accept, but do not count it as a guard decision. `tip` = accept with a note (B3: frame matches, the practised structure in the annotation `lk` is not the one used). Only `reject` is a veto.

## DEV distribution over the 490 DEV answers (counts only, no comparison with the old labels)

F9: {"tip": 168, "accept": 253, "abstain": 35, "reject": 34}

F8: {"accept": 460, "reject": 1, "abstain": 29}

## Known weak spots

- Reported speech: the sentence verdict is the frame of the REPORTING clause, so a backshift violation inside the ze/preco/kedy clause ("why he spends") is a TIP, not a reject. `f9.REPORTED_STRICT` is the switch; it is False because "He said the puck flies faster on cold ice" is legitimate and cannot be told apart offline.
- Slovak wish constructions ("by si prial", "kiez by") never reject against an English present ("The coach wishes ... were"), so a genuine "will want" slips through as a tip.
- Aspect is guessed from prefixes plus a lexicon; an unknown verb yields the open set {future, present}, so a Slovak future can never reject an English present - that pair is a TIP by design. Only past-vs-non-past and conditional-vs-indicative are hard rejects.
- English: reduced relative clauses are handled by a determiner-count heuristic; verbless fragments and past=present verbs (hit, put, cut, read) abstain.
- F8 fires only on an English PASSIVE main clause; an agent demoted without a passive (cleft, "it was him who...") is not detected. It fires once on the 490 DEV answers.

## Files

`f9.py`, `f8.py`, `validate_f9.py`, `gold_tf.jsonl`, `sentences_140.jsonl`, `rows_prefix.json`, `rows_postfix.json`, `dev_distribution.json`, `dev_answers.jsonl`, `F9_VALIDATION.md` - all in `/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase1k/taskB`. Every data read is logged in `/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase1k/access_log.jsonl`.

## Tool-call self-count

12 harness tool calls: 1 orientation, 1 data dump, 1 write of both guards, 1 gold + first validation, 7 fix/validation/report rounds (one of which aborted before writing anything).

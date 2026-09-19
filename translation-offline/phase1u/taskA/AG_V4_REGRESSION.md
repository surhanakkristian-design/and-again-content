# Phase 1U Task A - AG v4 regression (0 model calls, 0 network, no DB)

**DESIGN-only.** Both measurement sets (the 1S blind-judge packet and the closed 1T set) are sets the rule was built on or already opened. Nothing here is a held-out result.

Flags: `union` (guarded whole-sentence OR per-clause), `unionx` (raw union, measured not selected), `lex` (2.2 lexicon), `align` (2.3 class B), `local` (2.3 class A). `flags=()` reproduces AG v3 bit for bit.

## Pre-flight (synthetic rows only)

```
PASS furniture example (owner)                                          primary=True  (want True )  noun=True  (want True )
PASS by-passive keeps the agent                                         primary=False (want False)  noun=False (want False)
PASS active answer                                                      primary=False (want False)  noun=False (want False)
PASS Slovak reflexive passive, no agent                                 primary=False (want False)  noun=False (want False)
PASS Slovak passive, no agent                                           primary=False (want False)  noun=False (want False)
PASS was/is + adjective is no passive                                   primary=False (want False)  noun=False (want False)
PASS agent rendered as the answer subject                               primary=False (want False)  noun=False (want False)
PASS get-passive fires                                                  primary=True  (want True )  noun=True  (want True )
PASS perfect passive fires                                              primary=True  (want True )  noun=True  (want True )
PASS pronoun agent: primary fires, AG-noun abstains                     primary=True  (want True )  noun=False (want False)
PASS impersonal source                                                  primary=False (want False)  noun=False (want False)
PASS pronoun agent rendered in the answer subject                       primary=False (want False)  noun=False (want False)
PASS lent: v1 gap (will be lent)                                        primary=True  (want True )  noun=True  (want True )
PASS NEW embedded-clause agent drop                                     primary=True  (want True )  noun=True  (want True )
PASS NEW embedded clause, agent kept with by                            primary=False (want False)  noun=False (want False)
PASS NEW passive over a subjectless SK clause (agent lives in the other clause) primary=False (want False)  noun=False (want False)
PASS NEW "by bike" is no by-agent                                       primary=True  (want True )  noun=False (want False)
PASS NEW proper-name agent                                              primary=True  (want True )  noun=True  (want True )
PASS NEW pronoun agent in a ze-clause                                   primary=True  (want True )  noun=False (want False)
PASS NEW by-passive control (proper name)                               primary=False (want False)  noun=False (want False)
PASS NEW plain active control                                           primary=False (want False)  noun=False (want False)
PASS V4 closed + SK active transitive = passive                         primary=True  (want True )  noun=False (want False)
PASS V4 "The garden gate is closed every evening" is NOT a passive      primary=False (want False)  noun=False (want False)
PASS V4 rewritten (prefixed irregular participle)                       primary=True  (want True )  noun=True  (want True )
PASS V4 reduced passive relative                                        primary=True  (want True )  noun=True  (want True )
PASS V4 locative by-phrase does not block AG                            primary=True  (want True )  noun=False (want False)
PASS V4 instrument by-phrase does not block AG                          primary=True  (want True )  noun=False (want False)
PASS V4 agent by-phrase blocks AG                                       primary=False (want False)  noun=False (want False)
PASS V4 fronted keď-clause: the clause-local agent is dropped           primary=True  (want True )  noun=True  (want True )
PASS V4 fronted ja-clause: overt Slovak pronoun agent dropped           primary=True  (want True )  noun=False (want False)
PASS V4 class-B alignment: another clause subject is not the agent      primary=True  (want True )  noun=True  (want True )
PASS V4 class-B control: the agent is kept                              primary=False (want False)  noun=False (want False)
PASS flags=() reproduces AG v3 bit for bit on all 32 rows
PRE-FLIGHT PASS
```

## Gate 1 (RUN FIRST) - the 183-item 1S blind-judge packet

| config | agent drops (judged wrong) (n=97) | by-passive controls (n=42) | plain controls (judged correct) (n=39) | v2 misfires (judged correct) (n=3) | agentless judged CORRECT (n=1) | plain control judged wrong (n=1) |
| --- | --- | --- | --- | --- | --- | --- |
| AG v2 | 79 | 0 | 0 | 3 | 0 | 0 |
| AG v3 (= v4 flags=()) | 96 | 0 | 0 | 0 | 1 | 0 |
| v3+union | 96 | 0 | 0 | 0 | 1 | 0 |
| v3+unionx (raw) | 96 | 0 | 0 | 3 | 1 | 0 |
| v3+lex | 97 | 0 | 0 | 0 | 1 | 0 |
| v3+align | 96 | 0 | 0 | 0 | 1 | 0 |
| v3+local | 96 | 0 | 0 | 0 | 1 | 0 |
| union+lex | 97 | 0 | 0 | 0 | 1 | 0 |
| union+lex+align | 97 | 0 | 0 | 0 | 1 | 0 |
| AG v4 (full) | 97 | 0 | 0 | 0 | 1 | 0 |
| AG v4 with raw union | 97 | 0 | 0 | 3 | 1 | 0 |

Gate: >= 96/97 agent drops caught, 0/42 by-passive controls, 0/39 plain controls. **PASS** for `AG v4 (full)`.

### remaining packet misses of the chosen configuration

| iid | Slovak | answer | why |
| --- | --- | --- | --- |

## Gate 2 - the 1T set (900 items, 900 judged), DESIGN-only

Wiring self-check: `flags=()` disagrees with the AG verdict stored in results_1t.json on **0** of 900 rows.

| config | fires | catches (judged wrong) | agent-drop catches | MEASURED COST (judged-correct rejected) | agentdrop-embedded /96 | agentdrop-main /65 | aspect /62 | by-passive /47 | by-passive-embedded /33 | determiner /79 | number /12 | plain /381 | skp-passive /73 | timeframe /120 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AG v2 | 67 | 67 | 67/161 | 0 | 19/96 | 48/65 | 0/62 | 0/47 | 0/33 | 0/79 | 0/12 | 0/381 | 0/73 | 0/120 |
| AG v3 (= v4 flags=()) | 128 | 128 | 128/161 | 0 | 70/96 | 58/65 | 0/62 | 0/47 | 0/33 | 0/79 | 0/12 | 0/381 | 0/73 | 0/120 |
| v3+union | 132 | 132 | 132/161 | 0 | 70/96 | 62/65 | 0/62 | 0/47 | 0/33 | 0/79 | 0/12 | 0/381 | 0/73 | 0/120 |
| v3+unionx (raw) | 146 | 146 | 146/161 | 0 | 84/96 | 62/65 | 0/62 | 0/47 | 0/33 | 0/79 | 0/12 | 0/381 | 0/73 | 0/120 |
| v3+lex | 135 | 135 | 135/161 | 0 | 76/96 | 59/65 | 0/62 | 0/47 | 0/33 | 0/79 | 0/12 | 0/381 | 0/73 | 0/120 |
| v3+align | 133 | 133 | 133/161 | 0 | 71/96 | 62/65 | 0/62 | 0/47 | 0/33 | 0/79 | 0/12 | 0/381 | 0/73 | 0/120 |
| v3+local | 139 | 139 | 139/161 | 0 | 81/96 | 58/65 | 0/62 | 0/47 | 0/33 | 0/79 | 0/12 | 0/381 | 0/73 | 0/120 |
| union+lex | 139 | 139 | 139/161 | 0 | 76/96 | 63/65 | 0/62 | 0/47 | 0/33 | 0/79 | 0/12 | 0/381 | 0/73 | 0/120 |
| union+lex+align | 140 | 140 | 140/161 | 0 | 77/96 | 63/65 | 0/62 | 0/47 | 0/33 | 0/79 | 0/12 | 0/381 | 0/73 | 0/120 |
| AG v4 (full) | 152 | 152 | 152/161 | 0 | 89/96 | 63/65 | 0/62 | 0/47 | 0/33 | 0/79 | 0/12 | 0/381 | 0/73 | 0/120 |
| AG v4 with raw union | 155 | 155 | 155/161 | 0 | 92/96 | 63/65 | 0/62 | 0/47 | 0/33 | 0/79 | 0/12 | 0/381 | 0/73 | 0/120 |

### the 33 v3 misses recovered, BY CLASS

| config | A: fronted subordinate clause (n=14) | B: clause misalignment (n=9) | C: passive not seen (n=10) | of the recovered, L3 had accepted |
| --- | --- | --- | --- | --- |
| AG v2 | 12/14 | 3/9 | 0/10 | A 1, B 0, C 0 |
| AG v3 (= v4 flags=()) | 0/14 | 0/9 | 0/10 | A 0, B 0, C 0 |
| v3+union | 0/14 | 4/9 | 0/10 | A 0, B 0, C 0 |
| v3+unionx (raw) | 14/14 | 4/9 | 0/10 | A 3, B 0, C 0 |
| v3+lex | 0/14 | 0/9 | 7/10 | A 0, B 0, C 5 |
| v3+align | 0/14 | 5/9 | 0/10 | A 0, B 1, C 0 |
| v3+local | 11/14 | 0/9 | 0/10 | A 1, B 0, C 0 |
| union+lex | 0/14 | 4/9 | 7/10 | A 0, B 0, C 5 |
| union+lex+align | 0/14 | 5/9 | 7/10 | A 0, B 1, C 5 |
| AG v4 (full) | 11/14 | 5/9 | 8/10 | A 1, B 1, C 5 |
| AG v4 with raw union | 14/14 | 5/9 | 8/10 | A 3, B 1, C 5 |

### MEASURED COST of the chosen configuration on the 1T set

| iid | Slovak | answer |
| --- | --- | --- |
| - | (no judged-correct answer of the 1T set is rejected by AG v4) | - |

### remaining misses of AG v4 among the 33

| iid | class | L3 accepted | reason it still abstains |
| --- | --- | --- | --- |
| W:180068:w3 | A | no | c1: the Slovak counterpart clause has no overt agent and none precedes it (subjectless / 3pl pro-drop) |
| W:180097:w3 | A | yes | c0: the Slovak counterpart clause has no overt agent and none precedes it (subjectless / 3pl pro-drop) |
| W:180097:w4 | A | yes | c0: the Slovak counterpart clause has no overt agent and none precedes it (subjectless / 3pl pro-drop) |
| W:180035:w2 | B | yes | c1: the agent is rendered as that clause's own subject (only) |
| W:180052:w4 | B | yes | c0: the agent is rendered as that clause's own subject (we) |
| W:180060:w4 | B | no | c0: the agent is rendered as that clause's own subject (colleague) |
| W:180061:w4 | B | yes | c0: the agent is rendered as that clause's own subject (we) |
| W:180047:w2 | C | no | the answer is not a marked passive without a by-agent |
| W:180090:w3 | C | yes | the answer is not a marked passive without a by-agent |

## Chosen configuration

`agent_drop_v4.ALL_FLAGS = ('union', 'lex', 'align', 'local')` - selected on MEASURED COST (judged-correct answers rejected), never on gold-assertion accuracy; see the cost columns above.

Runner import line:

```python
import sys, os
sys.path.insert(0, os.path.expanduser('~/Projects/and-again-content/translation-offline/phase1u/taskA'))
import agent_drop_v4 as AG   # AG.decide(sk, ann, wtags, answer, reference, 'primary', AG.ALL_FLAGS)
```

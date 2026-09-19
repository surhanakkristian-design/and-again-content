# Phase 1T Task A - AG v3 regression (0 model calls, 0 network)

**DESIGN-only.** Both gates use sets AG v3 was built on (the 1S judge packet and the closed 1Q set). Nothing here is a held-out measurement.

Flags: `clause` (clause-aware test), `subj` (subject-NP reader + agent-string parsing), `by` (instrument != agent). `flags=()` reproduces AG v2 bit for bit (pre-flight row 22).

## Pre-flight (synthetic rows only)

```
PASS furniture example (owner)                                      primary=True  (want True )  noun=True  (want True )
PASS by-passive keeps the agent                                     primary=False (want False)  noun=False (want False)
PASS active answer                                                  primary=False (want False)  noun=False (want False)
PASS Slovak reflexive passive, no agent                             primary=False (want False)  noun=False (want False)
PASS Slovak passive, no agent                                       primary=False (want False)  noun=False (want False)
PASS was/is + adjective is no passive                               primary=False (want False)  noun=False (want False)
PASS agent rendered as the answer subject                           primary=False (want False)  noun=False (want False)
PASS get-passive fires                                              primary=True  (want True )  noun=True  (want True )
PASS perfect passive fires                                          primary=True  (want True )  noun=True  (want True )
PASS pronoun agent: primary fires, AG-noun abstains                 primary=True  (want True )  noun=False (want False)
PASS impersonal source                                              primary=False (want False)  noun=False (want False)
PASS pronoun agent rendered in the answer subject                   primary=False (want False)  noun=False (want False)
PASS lent: v1 gap (will be lent)                                    primary=True  (want True )  noun=True  (want True )
PASS NEW embedded-clause agent drop                                 primary=True  (want True )  noun=True  (want True )
PASS NEW embedded clause, agent kept with by                        primary=False (want False)  noun=False (want False)
PASS NEW passive over a subjectless SK clause (agent lives in the other clause) primary=False (want False)  noun=False (want False)
PASS NEW "by bike" is no by-agent                                   primary=True  (want True )  noun=False (want False)
PASS NEW proper-name agent                                          primary=True  (want True )  noun=True  (want True )
PASS NEW pronoun agent in a ze-clause                               primary=True  (want True )  noun=False (want False)
PASS NEW by-passive control (proper name)                           primary=False (want False)  noun=False (want False)
PASS NEW plain active control                                       primary=False (want False)  noun=False (want False)
PASS flags=() reproduces AG v2 on all 21 rows
```

## Gate 1 - the 183-item blind-judge packet (fired counts)

| config | agent drops (judged wrong) (n=97) | by-passive controls (n=42) | plain controls (judged correct) (n=39) | v2 misfires (judged correct) (n=3) | agentless judged CORRECT (n=1) | plain control judged wrong (n=1) |
| --- | --- | --- | --- | --- | --- | --- |
| AG v2 | 79 | 0 | 0 | 3 | 0 | 0 |
| v2+clause | 91 | 0 | 0 | 0 | 1 | 0 |
| v2+subj | 82 | 0 | 0 | 3 | 0 | 0 |
| v2+by | 82 | 0 | 0 | 3 | 0 | 0 |
| AG v3 (all) | 96 | 0 | 0 | 0 | 1 | 0 |

Wanted: column 1 as high as possible; columns 2-5 exactly 0 (they are judged-correct answers, every firing is a measured cost); column 6 is the one plain control the judge called wrong.

### remaining misses of AG v3 among the 97 judged agent drops

| iid | Slovak | answer | why AG v3 abstains |
| --- | --- | --- | --- |
| C:170014:c2 | Oni zavreli obchod o šiestej večer. | The shop was closed at six in the evening. | the answer is not a marked passive without a by-agent |

## Gate 2 - all 1,080 items of the 1Q set, K3 stack, labels RUL' (judge-folded)

| config | AG firings | coverage | FA | agentless coverage | agentless FA |
| --- | --- | --- | --- | --- | --- |
| AG v2 | 226 | 348/385 = 90.39 % [87.00, 93.14] | 18/695 = 2.59 % [1.54, 4.06] | 1/1 = 100.00 % [2.50, 100.00] | 10/269 = 3.72 % [1.80, 6.73] |
| v2+clause | 251 | 350/385 = 90.91 % [87.58, 93.59] | 11/695 = 1.58 % [0.79, 2.81] | 0/1 = 0.00 % [0.00, 97.50] | 3/269 = 1.12 % [0.23, 3.22] |
| v2+subj | 233 | 348/385 = 90.39 % [87.00, 93.14] | 17/695 = 2.45 % [1.43, 3.89] | 1/1 = 100.00 % [2.50, 100.00] | 9/269 = 3.35 % [1.54, 6.26] |
| v2+by | 235 | 348/385 = 90.39 % [87.00, 93.14] | 16/695 = 2.30 % [1.32, 3.71] | 1/1 = 100.00 % [2.50, 100.00] | 8/269 = 2.97 % [1.29, 5.78] |
| AG v3 (all) | 266 | 350/385 = 90.91 % [87.58, 93.59] | 8/695 = 1.15 % [0.50, 2.26] | 0/1 = 0.00 % [0.00, 97.50] | 0/269 = 0.00 % [0.00, 1.36] |

| config | judged-correct rows AG rejects (MEASURED COST) | of them: flip an accept into a rejection | new firings vs v2 | v2 firings dropped |
| --- | --- | --- | --- | --- |
| AG v2 | 3 | 3 | 0 | 0 |
| v2+clause | 1 | 1 | 31 | 6 |
| v2+subj | 3 | 3 | 10 | 3 |
| v2+by | 3 | 3 | 9 | 0 |
| AG v3 (all) | 1 | 1 | 46 | 6 |

### MEASURED COST - every judged-correct item AG v3 rejects

| iid | Slovak | answer | flips an accept? | why |
| --- | --- | --- | --- | --- |
| C:170081:c3 | Ak Marek dostane tú prácu, kúpi rodičom novú práčku. | If Marek gets that job, a new washing machine will be bought for his parents. | YES | agentless passive in clause 1 against the Slovak clause 'kúpi rodičom novú práčku.' that names the agent: Marek (inherited) |

### JUDGE-VERIFIED cost - judged-correct packet items AG v3 rejects

| group | iid | Slovak | answer |
| --- | --- | --- | --- |
| agentless judged CORRECT | C:170081:c3 | Ak Marek dostane tú prácu, kúpi rodičom novú práčku. | If Marek gets that job, a new washing machine will be bought for his parents. |

### new catches of AG v3 that AG v2 did not fire on (46)

| iid | answer | RUL' label |
| --- | --- | --- |
| C:170019:c2 | A whole glass of milk was drunk. | wrong |
| W:170019:w1 | A whole glass of milk will be drunk. | wrong |
| W:170019:w2 | A whole glass of water was drunk. | wrong |
| C:170057:c2 | The old newspapers were thrown in the bin. | wrong |
| W:170057:w1 | The old magazines were thrown in the bin. | wrong |
| W:170057:w2 | The old newspapers were thrown away. | wrong |
| C:170061:c3 | When we got home, all the glasses from the party had already been washed. | wrong |
| W:170061:w2 | When we get home, all the glasses from the party will already have been washed. | wrong |
| W:170061:w3 | When we got home, all the plates from the party had already been washed. | wrong |
| C:170062:c3 | A colleague says that the list of orders is sent to the warehouse every week. | wrong |
| W:170062:w3 | A colleague says that the list of orders is sent to the office every week. | wrong |
| C:170063:c3 | If it doesn't stop raining tomorrow, the whole match will be cancelled. | wrong |
| W:170063:w2 | If it doesn't stop raining tomorrow, the whole match was cancelled. | wrong |
| W:170063:w3 | If it doesn't stop raining tomorrow, the whole tournament will be cancelled. | wrong |
| C:170071:c3 | When she gets back from Vienna, the photos from the exhibition will be brought to us. | wrong |
| W:170071:w3 | When she gets back from Vienna, the photos from the wedding will be brought to us. | wrong |
| C:170074:c3 | My father told me that the garage had been locked before lunch. | wrong |
| W:170074:w3 | My father told me that the gate had been locked before lunch. | wrong |
| ... | +28 more - full list in AG_V3_REGRESSION.json | |

### v2 firings AG v3 drops (6)

| iid | answer | RUL' label | why v3 abstains |
| --- | --- | --- | --- |
| C:170092:c4 | Obviously somebody swapped those labels, because all the boxes are mixed up. | correct | c1: the Slovak counterpart clause is itself passive |
| C:170114:c1 | Since the new system was introduced, employees have been reporting far fewer errors. | correct | c0: the Slovak counterpart clause has no overt agent and none precedes it (subjectless / 3pl pro-drop) |
| C:170114:c2 | Since a new system was introduced, the employees report far fewer errors. | correct | c0: the Slovak counterpart clause has no overt agent and none precedes it (subjectless / 3pl pro-drop) |
| W:170114:w1 | Once the new system is introduced, employees will report far fewer errors. | wrong | c0: the Slovak counterpart clause has no overt agent and none precedes it (subjectless / 3pl pro-drop) |
| W:170114:w2 | Since the new system was introduced, employees will report far fewer errors. | wrong | c0: the Slovak counterpart clause has no overt agent and none precedes it (subjectless / 3pl pro-drop) |
| W:170114:w5 | Since the new system was introduced, employees have been reporting far less errors. | wrong | c0: the Slovak counterpart clause has no overt agent and none precedes it (subjectless / 3pl pro-drop) |

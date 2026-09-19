# Phase 1N — PROBE of the new prompt line (design readout, CLOSED set)

**This is a design readout on a CLOSED set, not a measurement.** The 120 items come from the closed Phase 1M fresh set (writer intent `V`, L3-eligible), whose labels and whose old-prompt verdicts were already seen in 1M. No target may be claimed from these numbers and no number here may be quoted as coverage or FA. One run, no prompt iteration: the prompt text is the owner's, fixed before the run.

| setting | value |
|---|---|
| command | `python3 runner_1n.py --probe` (once) |
| model | gemini-3.1-flash-lite, temperature 0, thinkingBudget 0 |
| old prompt | `P-FROZEN` (verdicts reused from the 1M ledger, 0 calls) |
| new prompt | `P-FROZEN-1N` (the one inserted VOICE line) |
| pool | intent-V L3-eligible 191, sampled 120 (seeded) |
| counted calls | 120 (cap 1200, 1080 left) |
| failures | http200 120, empty-200 0, non-200 attempts 0, quota wall False |

The inserted line, verbatim:

> Voice: if the Slovak names an agent in the nominative and the learner sentence moves that agent out of subject position or drops it (an active Slovak sentence turned into an English passive), that is SAME, provided the meaning is preserved. Where the Slovak is itself impersonal or passive, an English passive is SAME.

## Accept rate old versus new

"Accept" = verdict `SAME` (the checker accepts the learner answer); `DIFF` = reject; `TIP` = the tip path, counted as a rejection under the frozen config (`tip_reject true`).

| verdict | old prompt | new prompt |
|---|---|---|
| SAME | 54 | 62 |
| DIFF | 60 | 56 |
| TIP | 6 | 2 |
| **accept rate (SAME)** | **54/120 = 45.00 %** | **62/120 = 51.67 %** |

Agreement old vs new: **108/120 = 90.00 % [83.18, 94.73]** — 12 items changed verdict.

Transitions: `{"DIFF->DIFF": 54, "DIFF->SAME": 6, "SAME->SAME": 53, "SAME->TIP": 1, "TIP->DIFF": 2, "TIP->SAME": 3, "TIP->TIP": 1}`

Accept rate split by the OLD judge label (diagnostic only, the labels are 1M-closed):

| judged | n | old accepts | new accepts |
|---|---|---|---|
| correct | 18 | 8 (44.4 %) | 8 (44.4 %) |
| wrong | 102 | 46 (45.1 %) | 54 (52.9 %) |

The 12 verdict changes by judged label and direction:

| judged | transition | n |
|---|---|---|
| correct | TIP -> DIFF | 1 |
| wrong | DIFF -> SAME | 6 |
| wrong | SAME -> TIP | 1 |
| wrong | TIP -> DIFF | 1 |
| wrong | TIP -> SAME | 3 |

By writer form: `{"cleft TIP->DIFF": 2, "dropped DIFF->SAME": 4, "dropped SAME->TIP": 1, "passive DIFF->SAME": 2, "passive TIP->SAME": 2, "reported TIP->SAME": 1}`

## The 12 changed items, verbatim

| item_id | form | judged | old | new | Slovak | learner answer |
|---|---|---|---|---|---|---|
| `W:150002:1328557373` | passive | wrong/V | DIFF | SAME | Učiteľka povedala, že my sme tú písomku písali celú hodinu. | The teacher said that the test had been written by us for the whole hour. |
| `W:150026:2435303869` | dropped | wrong/V | DIFF | SAME | Ja každý večer umývam riad a utieram stôl. | Every evening the dishes get washed and the table wiped. |
| `W:150028:3005108295` | reported | wrong/V | TIP | SAME | Kolegyňa mi celé popoludnie vysvetľovala ten nový účtovný systém. | I was taken through the new accounting system all afternoon. |
| `W:150042:3907820027` | dropped | wrong/V | DIFF | SAME | Ona tú kolekciu navrhla ešte počas štúdia v zahraničí. | That collection got designed while she was still studying abroad. |
| `W:150052:889472901` | dropped | wrong/V | DIFF | SAME | Oni každú jar sadia pri plote nové stromčeky. | Every spring new little trees get planted by the fence. |
| `W:150061:2328538810` | cleft | correct | TIP | DIFF | Ty dnes umývaš okná v celej obývačke. | It is you who are cleaning the windows in the whole living room today. |
| `W:150078:2842394043` | passive | wrong/V | DIFF | SAME | Ona sa ho spýtala, prečo on meškal na tú skúšku. | He was asked by her why he had been late for the exam. |
| `W:150089:915346680` | passive | wrong/V | TIP | SAME | Oni na tabuli oznámili, že oni ten výlet presunuli na jún. | It was announced on the noticeboard that they had moved the trip to June. |
| `W:150110:4001346192` | dropped | wrong/V | DIFF | SAME | Vodič autobusu vysadil turistov hneď pri hrade. | The tourists got dropped off right by the castle. |
| `W:150113:1692206539` | passive | wrong/V | TIP | SAME | Ja som sa jej spýtal, či ona tú knihu už dočítala. | I asked her whether the book had already been finished by her. |
| `W:150115:515712522` | cleft | wrong/V | TIP | DIFF | Ministerstvo zverejnilo tie výsledky až po polnoci. | It was the ministry that the results were published by, only after midnight. |
| `W:150125:3592231523` | dropped | wrong/V | SAME | TIP | Pošta doručila tú zásielku o celý týždeň neskôr. | The parcel arrived a whole week later. |

## All 120 probed items

| item_id | sid | form | judged | old | new | agree |
|---|---|---|---|---|---|---|
| `W:150001:168829870` | 150001 | cleft | correct | SAME | SAME | yes |
| `W:150001:825494265` | 150001 | dropped | wrong/V | DIFF | DIFF | yes |
| `W:150002:1328557373` | 150002 | passive | wrong/V | DIFF | SAME | NO |
| `W:150004:334432156` | 150004 | dropped | wrong/V | DIFF | DIFF | yes |
| `W:150004:3453654004` | 150004 | cleft | correct | DIFF | DIFF | yes |
| `W:150005:1781718779` | 150005 | dropped | wrong/V | DIFF | DIFF | yes |
| `W:150005:1989704614` | 150005 | cleft | correct | SAME | SAME | yes |
| `W:150005:2236991858` | 150005 | passive | wrong/V | SAME | SAME | yes |
| `W:150007:1883778449` | 150007 | dropped | wrong/V | DIFF | DIFF | yes |
| `W:150008:2587640877` | 150008 | reported | wrong/V | DIFF | DIFF | yes |
| `W:150010:598363861` | 150010 | passive | wrong/V | SAME | SAME | yes |
| `W:150013:816334031` | 150013 | reported | wrong/V | DIFF | DIFF | yes |
| `W:150014:3619959625` | 150014 | passive | wrong/V | SAME | SAME | yes |
| `W:150016:3330974851` | 150016 | dropped | wrong/V | DIFF | DIFF | yes |
| `W:150017:1365983468` | 150017 | passive | wrong/V | SAME | SAME | yes |
| `W:150019:2296116549` | 150019 | cleft | correct | DIFF | DIFF | yes |
| `W:150019:3252552891` | 150019 | passive | wrong/V | SAME | SAME | yes |
| `W:150020:2029729448` | 150020 | cleft | correct | SAME | SAME | yes |
| `W:150023:3346400173` | 150023 | passive | wrong/V | DIFF | DIFF | yes |
| `W:150023:439651469` | 150023 | cleft | correct | TIP | TIP | yes |
| `W:150023:749737719` | 150023 | dropped | wrong/V | DIFF | DIFF | yes |
| `W:150025:3416167737` | 150025 | dropped | wrong/V | DIFF | DIFF | yes |
| `W:150025:3429444882` | 150025 | reported | wrong/V | SAME | SAME | yes |
| `W:150025:707441286` | 150025 | passive | wrong/V | SAME | SAME | yes |
| `W:150026:2435303869` | 150026 | dropped | wrong/V | DIFF | SAME | NO |
| `W:150028:3005108295` | 150028 | reported | wrong/V | TIP | SAME | NO |
| `W:150029:4147431312` | 150029 | dropped | wrong/V | DIFF | DIFF | yes |
| `W:150029:636390549` | 150029 | reported | wrong/V | DIFF | DIFF | yes |
| `W:150031:3582321646` | 150031 | dropped | wrong/V | SAME | SAME | yes |
| `W:150036:1474753250` | 150036 | dropped | wrong/V | DIFF | DIFF | yes |
| `W:150036:3558481883` | 150036 | cleft | correct | SAME | SAME | yes |
| `W:150037:1991402156` | 150037 | dropped | wrong/W | DIFF | DIFF | yes |
| `W:150040:2150966800` | 150040 | cleft | correct | SAME | SAME | yes |
| `W:150040:3143089433` | 150040 | dropped | wrong/V | DIFF | DIFF | yes |
| `W:150042:3907820027` | 150042 | dropped | wrong/V | DIFF | SAME | NO |
| `W:150043:2120767092` | 150043 | cleft | correct | DIFF | DIFF | yes |
| `W:150043:3146717365` | 150043 | reported | wrong/V | DIFF | DIFF | yes |
| `W:150045:2206218273` | 150045 | reported | wrong/V | SAME | SAME | yes |
| `W:150046:2639017536` | 150046 | passive | wrong/V | SAME | SAME | yes |
| `W:150046:2758253816` | 150046 | dropped | wrong/V | DIFF | DIFF | yes |
| `W:150048:1297954659` | 150048 | reported | wrong/V | DIFF | DIFF | yes |
| `W:150048:4197112059` | 150048 | cleft | correct | DIFF | DIFF | yes |
| `W:150049:459742325` | 150049 | dropped | wrong/V | DIFF | DIFF | yes |
| `W:150049:796916908` | 150049 | passive | wrong/V | SAME | SAME | yes |
| `W:150051:3986601262` | 150051 | dropped | wrong/V | SAME | SAME | yes |
| `W:150051:754910220` | 150051 | passive | wrong/V | SAME | SAME | yes |
| `W:150052:889472901` | 150052 | dropped | wrong/V | DIFF | SAME | NO |
| `W:150055:196200580` | 150055 | passive | wrong/V | SAME | SAME | yes |
| `W:150058:1688612944` | 150058 | dropped | correct | DIFF | DIFF | yes |
| `W:150058:2801785851` | 150058 | passive | wrong/V | SAME | SAME | yes |
| `W:150060:144375501` | 150060 | cleft | correct | DIFF | DIFF | yes |
| `W:150061:2328538810` | 150061 | cleft | correct | TIP | DIFF | NO |
| `W:150061:3846227511` | 150061 | passive | wrong/V | SAME | SAME | yes |
| `W:150063:261736019` | 150063 | passive | wrong/V | SAME | SAME | yes |
| `W:150063:2962823344` | 150063 | cleft | correct | SAME | SAME | yes |
| `W:150066:3443590089` | 150066 | dropped | wrong/V | SAME | SAME | yes |
| `W:150071:2363984631` | 150071 | cleft | correct | DIFF | DIFF | yes |
| `W:150071:3413646462` | 150071 | passive | wrong/V | SAME | SAME | yes |
| `W:150071:4022443984` | 150071 | reported | wrong/V | SAME | SAME | yes |
| `W:150072:1266263209` | 150072 | cleft | correct | SAME | SAME | yes |
| `W:150074:1057493295` | 150074 | dropped | wrong/V | DIFF | DIFF | yes |
| `W:150074:2104861162` | 150074 | passive | wrong/V | SAME | SAME | yes |
| `W:150075:1159509963` | 150075 | passive | wrong/V | SAME | SAME | yes |
| `W:150075:801634234` | 150075 | cleft | correct | SAME | SAME | yes |
| `W:150077:2044919300` | 150077 | passive | wrong/V | SAME | SAME | yes |
| `W:150077:2554650535` | 150077 | reported | wrong/V | SAME | SAME | yes |
| `W:150077:3857607628` | 150077 | dropped | wrong/V | SAME | SAME | yes |
| `W:150078:1040946620` | 150078 | dropped | wrong/V | DIFF | DIFF | yes |
| `W:150078:2842394043` | 150078 | passive | wrong/V | DIFF | SAME | NO |
| `W:150081:3710757197` | 150081 | dropped | wrong/V | DIFF | DIFF | yes |
| `W:150084:1437856065` | 150084 | dropped | wrong/W | DIFF | DIFF | yes |
| `W:150084:261024190` | 150084 | cleft | correct | DIFF | DIFF | yes |
| `W:150086:237936824` | 150086 | passive | wrong/V | SAME | SAME | yes |
| `W:150086:3382762100` | 150086 | dropped | wrong/V | DIFF | DIFF | yes |
| `W:150087:2433194994` | 150087 | reported | wrong/V | SAME | SAME | yes |
| `W:150087:3402866932` | 150087 | passive | wrong/V | SAME | SAME | yes |
| `W:150089:579572383` | 150089 | reported | wrong/V | SAME | SAME | yes |
| `W:150089:915346680` | 150089 | passive | wrong/V | TIP | SAME | NO |
| `W:150090:1273528014` | 150090 | passive | wrong/V | SAME | SAME | yes |
| `W:150090:3733526245` | 150090 | dropped | wrong/V | SAME | SAME | yes |
| `W:150093:1629533700` | 150093 | dropped | wrong/V | DIFF | DIFF | yes |
| `W:150095:1491484926` | 150095 | passive | wrong/V | SAME | SAME | yes |
| `W:150096:499034233` | 150096 | reported | wrong/V | SAME | SAME | yes |
| `W:150098:3068777907` | 150098 | passive | wrong/V | SAME | SAME | yes |
| `W:150098:888621127` | 150098 | dropped | wrong/V | DIFF | DIFF | yes |
| `W:150099:1192995843` | 150099 | reported | wrong/V | SAME | SAME | yes |
| `W:150101:1276336797` | 150101 | dropped | wrong/V | SAME | SAME | yes |
| `W:150102:1582925269` | 150102 | dropped | wrong/W | DIFF | DIFF | yes |
| `W:150106:3315869736` | 150106 | dropped | wrong/V | DIFF | DIFF | yes |
| `W:150106:3347403383` | 150106 | passive | wrong/V | SAME | SAME | yes |
| `W:150109:3619876717` | 150109 | dropped | wrong/V | DIFF | DIFF | yes |
| `W:150109:521522753` | 150109 | passive | wrong/V | SAME | SAME | yes |
| `W:150110:4001346192` | 150110 | dropped | wrong/V | DIFF | SAME | NO |
| `W:150110:593166976` | 150110 | passive | wrong/V | SAME | SAME | yes |
| `W:150112:2428404286` | 150112 | dropped | wrong/V | DIFF | DIFF | yes |
| `W:150113:1692206539` | 150113 | passive | wrong/V | TIP | SAME | NO |
| `W:150113:2110518473` | 150113 | reported | wrong/V | DIFF | DIFF | yes |
| `W:150115:1129180123` | 150115 | passive | wrong/V | SAME | SAME | yes |
| `W:150115:515712522` | 150115 | cleft | wrong/V | TIP | DIFF | NO |
| `W:150116:2553064627` | 150116 | cleft | wrong/V | DIFF | DIFF | yes |
| `W:150116:770749499` | 150116 | dropped | wrong/V | DIFF | DIFF | yes |
| `W:150118:1718304670` | 150118 | dropped | wrong/V | DIFF | DIFF | yes |
| `W:150119:2239318030` | 150119 | dropped | wrong/W | DIFF | DIFF | yes |
| `W:150119:2635263983` | 150119 | passive | wrong/V | SAME | SAME | yes |
| `W:150119:3560412446` | 150119 | cleft | wrong/V | DIFF | DIFF | yes |
| `W:150121:116124357` | 150121 | passive | wrong/V | SAME | SAME | yes |
| `W:150121:782091048` | 150121 | dropped | wrong/W | DIFF | DIFF | yes |
| `W:150122:3948596667` | 150122 | dropped | wrong/V | DIFF | DIFF | yes |
| `W:150124:1452885164` | 150124 | cleft | wrong/V | DIFF | DIFF | yes |
| `W:150125:3592231523` | 150125 | dropped | wrong/V | SAME | TIP | NO |
| `W:150125:606191824` | 150125 | cleft | wrong/V | DIFF | DIFF | yes |
| `W:150128:2357036701` | 150128 | dropped | wrong/V | DIFF | DIFF | yes |
| `W:150130:2442407700` | 150130 | dropped | wrong/V | DIFF | DIFF | yes |
| `W:150133:149259560` | 150133 | dropped | wrong/V | DIFF | DIFF | yes |
| `W:150133:2433312371` | 150133 | passive | wrong/V | SAME | SAME | yes |
| `W:150133:3748382003` | 150133 | cleft | wrong/V | DIFF | DIFF | yes |
| `W:150136:2394497310` | 150136 | dropped | wrong/V | SAME | SAME | yes |
| `W:150136:405495784` | 150136 | cleft | wrong/V | DIFF | DIFF | yes |
| `W:150137:3351802829` | 150137 | reported | wrong/V | DIFF | DIFF | yes |
| `W:150137:59736284` | 150137 | dropped | wrong/V | SAME | SAME | yes |

## Reading

* The new line moves the prompt in the intended direction: it converts `DIFF -> SAME` 6 times and `TIP -> SAME` 3 times, against 3 moves away from accept (`SAME -> TIP` 1, `TIP -> DIFF` 2). Accept rate rises 45.00 -> 51.67 percentage points on this closed pool.

* 90 % of the pool is stable under the change, so the line is not a rewrite of the checker.

* Whether those new accepts are right or wrong CANNOT be settled here: the labels are the closed 1M labels the prompt was designed against. The fresh 1N set decides it, once.


# Phase 1N — TASK A: the re-judge movement (label `rescore-1m`)

0 model calls. Sources: `taskA/blind_map.json`, `taskA/out_part1.json`, `taskA/out_part2.json` (merged by `rescore_1m.py`; every read is in `access_log.jsonl`).

**Judge files: both OK** — parsable, every jid known, no jid missing, no wrong without a type in T/W/M/S. `bad_parts = []`.

## 1. Movement of the 221 non-filler items

| cell | n |
|---|---|
| old wrong -> new correct | 153 |
| old wrong -> still wrong | 24 |
| old correct -> new wrong | 0 |
| old correct -> still correct | 44 |
| **old wrong (total)** | 177 |
| **old correct (total)** | 44 |
| **new wrong (total)** | 24 |

Rehabilitation rate of the old-wrong items: 153/177 = 86.44% [80.50, 91.12].
Opposite direction, old-correct items now called wrong: 0/44 = 0.00% [0.00, 8.04].

New wrong-type histogram (non-fillers): `{"M": 11, "W": 13}`.

## 2. The same, by 1M form

| form | n | w->c | w->w | c->w | c->c | old-wrong rehabilitated |
|---|---|---|---|---|---|---|
| passive | 66 | 66 | 0 | 0 | 0 | 66/66 = 100.00% [94.56, 100.00] |
| cleft | 54 | 11 | 1 | 0 | 42 | 11/12 = 91.67% [61.52, 99.79] |
| reported | 32 | 30 | 1 | 0 | 1 | 30/31 = 96.77% [83.30, 99.92] |
| dropped | 68 | 45 | 22 | 0 | 1 | 45/67 = 67.16% [54.60, 78.15] |
| (other/none) | 1 | 1 | 0 | 0 | 0 | 1/1 = 100.00% [2.50, 100.00] |

## 3. Old wrong -> STILL wrong, item by item

The reason is the judge's note, i.e. the ground other than voice on which the item stays wrong.

| jid | item_id | form | old type | new type | passive | reason (judge note) |
|---|---|---|---|---|---|---|
| A001 | W:150121:782091048 | dropped | W | W | - | 'Someone' replaces the explicit subject I |
| A010 | W:150011:2096040593 | dropped | V | W | - | 'Someone' replaces the explicit subject you |
| A016 | W:150086:3382762100 | dropped | V | W | - | 'Someone' replaces the explicit subject we |
| A049 | W:150133:149259560 | dropped | V | W | - | 'Someone' replaces the town as repairer |
| A071 | W:150119:2239318030 | dropped | W | W | - | 'Someone' replaces named subject Katka |
| A072 | W:150078:1040946620 | dropped | V | W | - | 'Someone' replaces the explicit subject she |
| A076 | W:150127:121127838 | cleft | V | M | by | beneficiary 'for you' dropped |
| A088 | W:150113:1825792639 | dropped | V | W | - | 'Someone' replaces the explicit subject I |
| A122 | W:150130:2442407700 | dropped | V | W | - | 'Someone' replaces the explicit subject they |
| A133 | W:150080:3181878629 | dropped | V | W | - | 'They' replaces the named architect |
| A134 | W:150084:1437856065 | dropped | W | W | - | 'Someone' replaces dad as parker |
| A136 | W:150093:1629533700 | dropped | V | W | - | 'They' replaces the new colleague |
| A149 | W:150102:1582925269 | dropped | W | W | - | 'Someone' replaces the explicit subject you |
| A150 | W:150098:888621127 | dropped | V | W | - | 'They' replaces the baker |
| A153 | W:150112:2428404286 | dropped | V | M | - | identified 'they' replaced by unidentified 'someone' |
| A155 | W:150037:1991402156 | dropped | W | M | - | 'she' replaced by unidentified 'someone' |
| A167 | W:150002:2014087699 | dropped | W | M | - | teacher replaced by unidentified 'someone' |
| A184 | W:150118:1718304670 | dropped | V | M | agentless | coach replaced by unidentified 'somebody' |
| A186 | W:150049:459742325 | dropped | V | M | - | friend replaced by 'someone'; 'his' camera dropped |
| A188 | W:150106:3315869736 | dropped | V | M | - | grandpa replaced by unidentified 'someone' |
| A195 | W:150081:3710757197 | dropped | V | M | - | 'we' replaced by unidentified 'someone' |
| A208 | W:150124:2120438885 | reported | V | M | agentless | her admission dropped, replaced by 'it came out' |
| A219 | W:150116:770749499 | dropped | V | M | - | 'she' replaced by unidentified 'somebody' |
| A265 | W:150025:3416167737 | dropped | V | M | - | 'I think' replaced by hearsay 'apparently' |

## 4. The other direction: old correct -> new wrong

_none._

## 5. Old wrong -> new correct (the released items)

| jid | item_id | form | old type | passive |
|---|---|---|---|---|
| A003 | W:150074:1057493295 | dropped | V | agentless |
| A006 | W:150016:3330974851 | dropped | V | agentless |
| A008 | W:150017:3282275393 | dropped | V | agentless |
| A009 | W:150081:2186357679 | passive | V | agentless |
| A011 | W:150043:3146717365 | reported | V | agentless |
| A012 | W:150115:515712522 | cleft | V | by |
| A014 | W:150067:1995447870 | reported | V | agentless |
| A015 | W:150067:2928349087 | passive | V | by |
| A017 | W:150133:3748382003 | cleft | V | by |
| A021 | W:150029:4147431312 | dropped | V | agentless |
| A023 | W:150022:1914778343 | passive | V | by |
| A025 | W:150022:1824463829 | dropped | V | agentless |
| A029 | W:150008:2587640877 | reported | V | agentless |
| A030 | W:150101:1276336797 | dropped | V | agentless |
| A034 | W:150045:2207757270 | passive | V | by |
| A036 | W:150127:3341844202 | passive | V | by |
| A038 | W:150037:2631626927 | passive | V | by |
| A039 | W:150026:2435303869 | dropped | V | agentless |
| A040 | W:150005:1781718779 | dropped | V | agentless |
| A042 | W:150045:2206218273 | reported | V | - |
| A043 | W:150130:2099279997 | passive | V | agentless |
| A044 | W:150090:1273528014 | passive | V | by |
| A047 | W:150122:1084790222 | passive | V | by |
| A048 | W:150075:1159509963 | passive | V | by |
| A050 | W:150116:2553064627 | cleft | V | by |
| A056 | W:150077:2044919300 | passive | V | by |
| A057 | W:150107:1357263160 | passive | V | by |
| A058 | W:150049:3975592346 | reported | V | agentless |
| A059 | W:150098:3068777907 | passive | V | by |
| A060 | W:150054:3313325310 | dropped | V | agentless |
| A061 | W:150131:1435571480 | cleft | V | by |
| A062 | W:150051:3986601262 | dropped | V | agentless |
| A063 | W:150055:1422911619 | dropped | V | - |
| A064 | W:150095:1491484926 | passive | V | by |
| A065 | W:150032:3156470445 | reported | V | agentless |
| A067 | W:150071:3413646462 | passive | V | by |
| A070 | W:150042:3907820027 | dropped | V | agentless |
| A073 | W:150115:2771702179 | dropped | V | - |
| A074 | W:150095:1246691562 | reported | V | - |
| A075 | W:150023:3346400173 | passive | V | by |
| A077 | W:150001:825494265 | dropped | V | agentless |
| A079 | W:150010:2731739077 | dropped | V | agentless |
| A081 | W:150131:35193125 | passive | V | by |
| A090 | W:150057:1819726682 | dropped | V | agentless |
| A093 | W:150125:3592231523 | dropped | V | - |
| A094 | W:150013:4105166619 | passive | V | by |
| A099 | W:150007:1651911941 | passive | V | by |
| A100 | W:150014:1441258093 | dropped | V | agentless |
| A102 | W:150039:696790370 | dropped | V | agentless |
| A107 | W:150046:2639017536 | passive | V | by |
| A110 | W:150078:2842394043 | passive | V | by |
| A111 | W:150099:1192995843 | reported | V | - |
| A114 | W:150057:2210713267 | passive | V | by |
| A115 | W:150119:3560412446 | cleft | V | by |
| A116 | W:150115:1129180123 | passive | V | by |
| A118 | W:150133:2433312371 | passive | V | by |
| A126 | W:150077:2554650535 | reported | V | - |
| A127 | W:150075:3060416600 | reported | V | agentless |
| A131 | W:150093:871304538 | passive | V | by |
| A132 | W:150011:67241041 | passive | V | by |
| A135 | W:150026:181640577 | passive | V | by |
| A139 | W:150125:271837076 | passive | V | by |
| A141 | W:150025:3429444882 | reported | V | - |
| A144 | W:150087:2433194994 | reported | V | - |
| A145 | W:150102:1478031877 | passive | V | agentless |
| A147 | W:150042:1470509509 | passive | V | by |
| A148 | W:150125:606191824 | cleft | V | by |
| A151 | W:150061:3846227511 | passive | V | by |
| A156 | W:150039:1290265141 | passive | V | by |
| A157 | W:150109:521522753 | passive | V | by |
| A158 | W:150128:1170012679 | cleft | V | by |
| A159 | W:150134:3668949353 | dropped | V | agentless |
| A161 | W:150051:754910220 | passive | V | by |
| A162 | W:150054:1315505146 | passive | V | by |
| A163 | W:150066:3443590089 | dropped | V | agentless |
| A165 | W:150101:3819736691 | reported | V | - |
| A166 | W:150107:774143465 | reported | V | agentless |
| A169 | W:150131:690317222 | dropped | V | agentless |
| A170 | W:150002:1328557373 | passive | V | by |
| A171 | W:150089:3856161558 | dropped | V | agentless |
| A172 | W:150060:541897264 | reported | V | agentless |
| A174 | W:150043:2981417085 | passive | V | by |
| A175 | W:150074:2104861162 | passive | V | by |
| A176 | W:150063:261736019 | passive | V | by |
| A177 | W:150061:1135852382 | dropped | V | agentless |
| A178 | W:150109:3619876717 | dropped | V | agentless |
| A179 | W:150046:2758253816 | dropped | V | agentless |
| A180 | C:150123:3416772860 | None | V | by |
| A181 | W:150109:524090275 | cleft | V | agentless |
| A183 | W:150113:2110518473 | reported | V | agentless |
| A189 | W:150014:3619959625 | passive | V | by |
| A190 | W:150055:196200580 | passive | V | by |
| A193 | W:150029:2827682207 | passive | V | by |
| A196 | W:150121:2232976007 | cleft | V | by |
| A197 | W:150063:1085385892 | dropped | V | agentless |
| A200 | W:150048:1297954659 | reported | V | agentless |
| A201 | W:150023:749737719 | dropped | V | agentless |
| A202 | W:150064:2721351684 | reported | V | agentless |
| A204 | W:150010:598363861 | passive | V | by |
| A205 | W:150058:2801785851 | passive | V | by |
| A206 | W:150134:624654404 | passive | V | by |
| A211 | W:150096:499034233 | reported | V | - |
| A215 | W:150127:3559368588 | dropped | V | agentless |
| A216 | W:150013:816334031 | reported | V | agentless |
| A217 | W:150019:3252552891 | passive | V | by |
| A221 | W:150005:2236991858 | passive | V | by |
| A222 | W:150071:4022443984 | reported | V | - |
| A228 | W:150093:2343897934 | reported | V | - |
| A229 | W:150087:3402866932 | passive | V | by |
| A232 | W:150122:3948596667 | dropped | V | agentless |
| A233 | W:150137:3798492049 | passive | V | by |
| A234 | W:150089:579572383 | reported | V | - |
| A235 | W:150028:3005108295 | reported | V | agentless |
| A236 | W:150137:3351802829 | reported | V | agentless |
| A238 | W:150077:3857607628 | dropped | V | agentless |
| A239 | W:150118:858940622 | passive | V | by |
| A240 | W:150092:3656452801 | reported | V | - |
| A241 | W:150089:915346680 | passive | V | agentless |
| A243 | W:150110:593166976 | passive | V | by |
| A247 | W:150121:116124357 | passive | V | by |
| A251 | W:150036:1474753250 | dropped | V | agentless |
| A254 | W:150013:1574855049 | dropped | V | agentless |
| A255 | W:150099:2073308736 | passive | V | agentless |
| A256 | W:150020:3944356144 | dropped | V | agentless |
| A257 | W:150031:3582321646 | dropped | V | agentless |
| A258 | W:150072:2079221943 | reported | V | agentless |
| A259 | W:150136:2394497310 | dropped | V | agentless |
| A260 | W:150136:405495784 | cleft | V | by |
| A262 | W:150083:1963002460 | passive | V | by |
| A263 | W:150119:2635263983 | passive | V | by |
| A266 | W:150049:796916908 | passive | V | by |
| A267 | W:150083:2391353014 | reported | V | - |
| A268 | W:150066:2537125926 | passive | V | by |
| A269 | W:150004:334432156 | dropped | V | agentless |
| A271 | W:150025:707441286 | passive | V | by |
| A275 | W:150106:3347403383 | passive | V | by |
| A276 | W:150040:3143089433 | dropped | V | agentless |
| A277 | W:150052:889472901 | dropped | V | agentless |
| A279 | W:150086:237936824 | passive | V | by |
| A285 | W:150001:2599243042 | passive | V | by |
| A286 | W:150124:1452885164 | cleft | V | agentless |
| A287 | W:150007:1883778449 | dropped | V | agentless |
| A288 | W:150101:187052484 | passive | V | by |
| A291 | W:150029:636390549 | reported | V | agentless |
| A292 | W:150137:59736284 | dropped | V | - |
| A293 | W:150019:2436277438 | reported | V | - |
| A294 | W:150017:1365983468 | passive | V | by |
| A295 | W:150090:3733526245 | dropped | V | agentless |
| A297 | W:150128:2357036701 | dropped | V | agentless |
| A298 | W:150110:4001346192 | dropped | V | agentless |
| A299 | W:150045:3608276551 | dropped | V | - |
| A300 | W:150113:1692206539 | passive | V | by |
| A301 | W:150031:3491199111 | passive | V | by |

## 6. Filler agreement — the judge-drift diagnostic

80 fillers, re-judged blind alongside the real items. Old versus new verdict:

| cell | value |
|---|---|
| agreements | 78 / 80 |
| **agreement, exact 95 % CP** | 78/80 = 97.50% [91.26, 99.70] |
| old correct -> new wrong | 1 |
| old wrong -> new correct | 1 |

The disagreeing fillers:

| jid | item_id | old | new | new type | note |
|---|---|---|---|---|---|
| A098 | W:150139:1359368488 | wrong | correct | - | - |
| A246 | W:150035:3103579073 | correct | wrong | S | 'from morning' should be 'since morning' |

Read it as drift of the judging instrument, not as a result: the fillers were meant to be re-confirmed, so every disagreement here is noise that also sits inside the movement table above.


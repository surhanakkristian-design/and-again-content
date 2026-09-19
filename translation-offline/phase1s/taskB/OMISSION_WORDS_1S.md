# Phase 1S / Task B2 - omission word list (report only, no bucket changed)

- Source = phase1r/taskA/judge/verdicts.json `dropped` (119 judged items: 116 M2 + 3 M1), joined to iids via _key.json.
- Each dropped entry is split on "=" / "->"; the LEFT side is the Slovak material. It is lowercased and tokenised on Slovak letters.
- A token counts only if its de-accented form occurs in the item Slovak sentence (phase1p/data/sentences.json). 1 matched token = word-level, 2-4 = phrase-level, otherwise (0 matched, >4, or the text says clause/whole/sentence) = clause-level, listed separately, never guessed.
- No bucket was changed. POS column left blank; the only derived flag is membership in the owner-named disputed particle/adverb list.

## Counts
{"items_judged": 119, "dropped_entries_word_level": 46, "dropped_entries_phrase_level": 91, "dropped_entries_clause_level": 10, "distinct_words": 188}

## (i) Word table
| word | freq | bucket(s) | POS | disputed | example iid |
|---|---|---|---|---|---|
| v | 13 | {"M2": 13} |  |  | W:170026:w3 |
| na | 11 | {"M2": 11} |  |  | W:170118:w4 |
| do | 10 | {"M2": 10} |  |  | W:170057:w2 |
| pred | 8 | {"M2": 8} |  |  | W:170074:w4 |
| celú | 5 | {"M2": 5} |  | yes | W:170091:w4 |
| celý | 4 | {"M2": 4} |  | yes | W:170019:w3 |
| ešte | 4 | {"M2": 4} |  | yes | W:170074:w4 |
| o | 4 | {"M2": 4} |  |  | W:170014:w3 |
| pre | 4 | {"M2": 4} |  |  | W:170039:w2 |
| až | 3 | {"M1": 1, "M2": 2} |  | yes | W:170107:w4 |
| konca | 3 | {"M2": 3} |  |  | W:170117:w4 |
| môj | 3 | {"M2": 3} |  |  | W:170051:w2 |
| ona | 3 | {"M2": 3} |  |  | W:170054:w2 |
| po | 3 | {"M2": 3} |  |  | W:170061:w4 |
| s | 3 | {"M2": 3} |  |  | W:170025:w3 |
| z | 3 | {"M2": 3} |  |  | W:170038:w3 |
| zajtra | 3 | {"M2": 3} |  |  | W:170063:w4 |
| a | 2 | {"M2": 2} |  |  | W:170120:w4 |
| budúci | 2 | {"M2": 2} |  |  | W:170067:w4 |
| cez | 2 | {"M2": 2} |  |  | W:170053:w3 |
| domom | 2 | {"M2": 2} |  |  | W:170048:w2 |
| dva | 2 | {"M2": 2} |  |  | W:170120:w4 |
| ja | 2 | {"M2": 2} |  |  | W:170012:w2 |
| každý | 2 | {"M2": 2} |  |  | W:170062:w4 |
| lebo | 2 | {"M2": 2} |  |  | W:170065:w4 |
| malý | 2 | {"M2": 2} |  |  | W:170032:w3 |
| mesta | 2 | {"M2": 2} |  |  | W:170040:w3 |
| minulý | 2 | {"M2": 2} |  |  | W:170006:w2 |
| otec | 2 | {"M2": 2} |  |  | W:170051:w2 |
| rodinu | 2 | {"M2": 2} |  |  | W:170007:w3 |
| rok | 2 | {"M2": 2} |  |  | W:170056:w3 |
| roka | 2 | {"M2": 2} |  |  | W:170098:w4 |
| svojej | 2 | {"M2": 2} |  |  | W:170051:w2 |
| ten | 2 | {"M2": 2} |  |  | W:170032:w3 |
| týždeň | 2 | {"M2": 2} |  |  | W:170062:w4 |
| už | 2 | {"M2": 2} |  | yes | W:170094:w4 |
| večer | 2 | {"M2": 2} |  |  | W:170014:w3 |
| vlani | 2 | {"M2": 2} |  |  | W:170083:w4 |
| vo | 2 | {"M2": 2} |  |  | W:170051:w2 |
| za | 2 | {"M2": 2} |  |  | W:170032:w3 |
| aj | 1 | {"M1": 1} |  | yes | W:170116:w4 |
| ako | 1 | {"M2": 1} |  |  | W:170083:w4 |
| bez | 1 | {"M2": 1} |  |  | W:170105:w4 |
| bicykli | 1 | {"M2": 1} |  |  | W:170077:w4 |
| brat | 1 | {"M2": 1} |  |  | W:170003:w2 |
| byt | 1 | {"M2": 1} |  |  | W:170032:w3 |
| bytu | 1 | {"M2": 1} |  |  | W:170022:w3 |
| centre | 1 | {"M2": 1} |  |  | W:170093:w4 |
| chodník | 1 | {"M2": 1} |  |  | W:170009:w2 |
| chýbali | 1 | {"M2": 1} |  |  | W:170087:w4 |
| dedko | 1 | {"M2": 1} |  |  | W:170021:w2 |
| desiatej | 1 | {"M2": 1} |  |  | W:170076:w4 |
| deti | 1 | {"M2": 1} |  |  | W:170009:w2 |
| deň | 1 | {"M2": 1} |  |  | W:170050:w3 |
| dielni | 1 | {"M2": 1} |  |  | W:170051:w2 |
| dlhý | 1 | {"M2": 1} |  |  | W:170016:w3 |
| dnes | 1 | {"M2": 1} |  |  | W:170119:w4 |
| doklady | 1 | {"M2": 1} |  |  | W:170084:w4 |
| dvadsať | 1 | {"M2": 1} |  |  | W:170082:w4 |
| dve | 1 | {"M2": 1} |  |  | W:170087:w4 |
| dvora | 1 | {"M2": 1} |  |  | W:170038:w3 |
| futbalovou | 1 | {"M2": 1} |  |  | W:170068:w4 |
| garáži | 1 | {"M2": 1} |  |  | W:170011:w3 |
| hlavného | 1 | {"M2": 1} |  |  | W:170058:w3 |
| horách | 1 | {"M2": 1} |  |  | W:170070:w4 |
| hostí | 1 | {"M2": 1} |  |  | W:170039:w2 |
| hradoch | 1 | {"M2": 1} |  |  | W:170073:w4 |
| hrubou | 1 | {"M2": 1} |  |  | W:170025:w3 |
| hrubé | 1 | {"M2": 1} |  |  | W:170044:w3 |
| iba | 1 | {"M2": 1} |  |  | W:170088:w4 |
| internet | 1 | {"M2": 1} |  |  | W:170053:w3 |
| izbe | 1 | {"M2": 1} |  |  | W:170020:w3 |
| jar | 1 | {"M2": 1} |  |  | W:170101:w4 |
| jari | 1 | {"M2": 1} |  |  | W:170075:w4 |
| jazera | 1 | {"M2": 1} |  |  | W:170010:w3 |
| jazykový | 1 | {"M2": 1} |  |  | W:170066:w4 |
| jeden | 1 | {"M2": 1} |  |  | W:170088:w4 |
| kamarátkou | 1 | {"M2": 1} |  |  | W:170005:w3 |
| kancelárii | 1 | {"M2": 1} |  |  | W:170036:w2 |
| kaviarňou | 1 | {"M2": 1} |  |  | W:170015:w3 |
| každú | 1 | {"M2": 1} |  |  | W:170078:w4 |
| knihou | 1 | {"M2": 1} |  |  | W:170025:w3 |
| kolegovia | 1 | {"M2": 1} |  |  | W:170102:w4 |
| konci | 1 | {"M2": 1} |  |  | W:170103:w4 |
| koncom | 1 | {"M2": 1} |  |  | W:170106:w4 |
| konečne | 1 | {"M1": 1} |  | yes | W:170107:w4 |
| kopci | 1 | {"M2": 1} |  |  | W:170035:w3 |
| koša | 1 | {"M2": 1} |  |  | W:170057:w2 |
| košiciach | 1 | {"M2": 1} |  |  | W:170046:w3 |
| ktorú | 1 | {"M2": 1} |  |  | W:170102:w4 |
| kuchár | 1 | {"M2": 1} |  |  | W:170039:w2 |
| kurz | 1 | {"M2": 1} |  |  | W:170066:w4 |
| kúpeľni | 1 | {"M2": 1} |  |  | W:170042:w2 |
| loptou | 1 | {"M2": 1} |  |  | W:170068:w4 |
| menšieho | 1 | {"M2": 1} |  |  | W:170040:w3 |
| mesiac | 1 | {"M2": 1} |  |  | W:170067:w4 |
| mesiaca | 1 | {"M2": 1} |  |  | W:170103:w4 |
| minút | 1 | {"M2": 1} |  |  | W:170082:w4 |
| mnohé | 1 | {"M2": 1} |  |  | W:170119:w4 |
| my | 1 | {"M2": 1} |  |  | W:170008:w2 |
| nad | 1 | {"M2": 1} |  |  | W:170015:w3 |
| napriek | 1 | {"M2": 1} |  |  | W:170115:w4 |
| naším | 1 | {"M2": 1} |  |  | W:170048:w2 |
| nemeckým | 1 | {"M2": 1} |  |  | W:170099:w4 |
| novej | 1 | {"M2": 1} |  |  | W:170013:w3 |
| nový | 1 | {"M2": 1} |  |  | W:170114:w4 |
| nám | 1 | {"M2": 1} |  |  | W:170102:w4 |
| obedom | 1 | {"M2": 1} |  |  | W:170074:w4 |
| ochladilo | 1 | {"M2": 1} |  |  | W:170070:w4 |
| od | 1 | {"M2": 1} |  |  | W:170022:w3 |
| odchodom | 1 | {"M2": 1} |  |  | W:170047:w3 |
| odkedy | 1 | {"M2": 1} |  |  | W:170114:w4 |
| odporučili | 1 | {"M2": 1} |  |  | W:170102:w4 |
| okolo | 1 | {"M2": 1} |  |  | W:170010:w3 |
| oni | 1 | {"M2": 1} |  |  | W:170027:w2 |
| oslave | 1 | {"M2": 1} |  |  | W:170061:w4 |
| otvorením | 1 | {"M2": 1} |  |  | W:170112:w4 |
| parkovania | 1 | {"M2": 1} |  |  | W:170093:w4 |
| partnerom | 1 | {"M2": 1} |  |  | W:170099:w4 |
| pekárni | 1 | {"M2": 1} |  |  | W:170013:w3 |
| pes | 1 | {"M2": 1} |  |  | W:170024:w2 |
| plánu | 1 | {"M2": 1} |  |  | W:170105:w4 |
| podrobného | 1 | {"M2": 1} |  |  | W:170105:w4 |
| pondelok | 1 | {"M2": 1} |  |  | W:170094:w4 |
| popoludní | 1 | {"M2": 1} |  |  | W:170052:w3 |
| počasiu | 1 | {"M2": 1} |  |  | W:170115:w4 |
| prezentáciu | 1 | {"M2": 1} |  |  | W:170118:w4 |
| pripomienkach | 1 | {"M2": 1} |  |  | W:170096:w4 |
| profesorovi | 1 | {"M2": 1} |  |  | W:170037:w3 |
| práce | 1 | {"M2": 1} |  |  | W:170047:w3 |
| práve | 1 | {"M1": 1} |  | yes | W:170116:w4 |
| príliš | 1 | {"M2": 1} |  |  | W:170111:w4 |
| prílohy | 1 | {"M2": 1} |  |  | W:170087:w4 |
| riaditeľ | 1 | {"M2": 1} |  |  | W:170036:w2 |
| rieku | 1 | {"M2": 1} |  |  | W:170027:w2 |
| robotníci | 1 | {"M2": 1} |  |  | W:170033:w2 |
| rodičom | 1 | {"M2": 1} |  |  | W:170081:w4 |
| ráno | 1 | {"M2": 1} |  |  | W:170065:w4 |
| sa | 1 | {"M2": 1} |  |  | W:170070:w4 |
| schodoch | 1 | {"M2": 1} |  |  | W:170017:w3 |
| semester | 1 | {"M2": 1} |  |  | W:170088:w4 |
| septembra | 1 | {"M2": 1} |  |  | W:170117:w4 |
| sestre | 1 | {"M2": 1} |  |  | W:170018:w2 |
| skleníku | 1 | {"M2": 1} |  |  | W:170021:w2 |
| skontroloval | 1 | {"M2": 1} |  |  | W:170084:w4 |
| slovenských | 1 | {"M2": 1} |  |  | W:170073:w4 |
| sobotu | 1 | {"M2": 1} |  |  | W:170078:w4 |
| sotva | 1 | {"M2": 1} |  |  | W:170065:w4 |
| spaním | 1 | {"M2": 1} |  |  | W:170043:w3 |
| stanicu | 1 | {"M2": 1} |  |  | W:170030:w3 |
| starý | 1 | {"M2": 1} |  |  | W:170034:w3 |
| stola | 1 | {"M2": 1} |  |  | W:170024:w2 |
| stole | 1 | {"M2": 1} |  |  | W:170059:w3 |
| stromy | 1 | {"M2": 1} |  |  | W:170120:w4 |
| susedov | 1 | {"M2": 1} |  |  | W:170002:w2 |
| susedovi | 1 | {"M2": 1} |  |  | W:170038:w3 |
| systém | 1 | {"M2": 1} |  |  | W:170114:w4 |
| technik | 1 | {"M2": 1} |  |  | W:170042:w2 |
| tridsať | 1 | {"M2": 1} |  |  | W:170039:w2 |
| triede | 1 | {"M2": 1} |  |  | W:170004:w3 |
| tú | 1 | {"M2": 1} |  |  | W:170118:w4 |
| týždne | 1 | {"M2": 1} |  |  | W:170095:w4 |
| týždňa | 1 | {"M2": 1} |  |  | W:170089:w4 |
| večera | 1 | {"M2": 1} |  |  | W:170055:w3 |
| večeru | 1 | {"M2": 1} |  |  | W:170064:w4 |
| veľa | 1 | {"M2": 1} |  |  | W:170111:w4 |
| veľkej | 1 | {"M2": 1} |  |  | W:170020:w3 |
| veľký | 1 | {"M2": 1} |  |  | W:170029:w3 |
| viedne | 1 | {"M2": 1} |  |  | W:170071:w4 |
| vstávaš | 1 | {"M2": 1} |  |  | W:170065:w4 |
| vtedy | 1 | {"M1": 1} |  | yes | W:170110:w4 |
| vyvrátila | 1 | {"M2": 1} |  |  | W:170120:w4 |
| väčšina | 1 | {"M2": 1} |  |  | W:170079:w4 |
| vždy | 1 | {"M2": 1} |  |  | W:170103:w4 |
| zahraniční | 1 | {"M2": 1} |  |  | W:170108:w4 |
| zaviedli | 1 | {"M2": 1} |  |  | W:170114:w4 |
| zlému | 1 | {"M2": 1} |  |  | W:170115:w4 |
| zo | 1 | {"M2": 1} |  |  | W:170024:w2 |
| zvieratách | 1 | {"M2": 1} |  |  | W:170012:w2 |
| záhrade | 1 | {"M2": 1} |  |  | W:170026:w3 |
| záhradník | 1 | {"M2": 1} |  |  | W:170048:w2 |
| zľave | 1 | {"M2": 1} |  |  | W:170054:w2 |
| úplne | 1 | {"M2": 1} |  |  | W:170075:w4 |
| úradu | 1 | {"M2": 1} |  |  | W:170096:w4 |
| čakárni | 1 | {"M2": 1} |  |  | W:170045:w3 |
| šiestej | 1 | {"M2": 1} |  |  | W:170014:w3 |
| školou | 1 | {"M2": 1} |  |  | W:170033:w2 |
| školy | 1 | {"M2": 1} |  |  | W:170028:w3 |

## (ii) Disputed class (adverbs/particles) - pulled out for visibility only
| word | freq | bucket(s) | example iid |
|---|---|---|---|
| celú | 5 | {"M2": 5} | W:170091:w4 |
| celý | 4 | {"M2": 4} | W:170019:w3 |
| ešte | 4 | {"M2": 4} | W:170074:w4 |
| až | 3 | {"M1": 1, "M2": 2} | W:170107:w4 |
| už | 2 | {"M2": 2} | W:170094:w4 |
| aj | 1 | {"M1": 1} | W:170116:w4 |
| konečne | 1 | {"M1": 1} | W:170107:w4 |
| práve | 1 | {"M1": 1} | W:170116:w4 |
| vtedy | 1 | {"M1": 1} | W:170110:w4 |

## (iii) Borderline movers (7)

- J007 W:170091:w4 bucket=M2 dropped=['celú = whole'] verdict=wrong class=content
- J016 W:170023:w3 bucket=M2 dropped=['celú = whole'] verdict=wrong class=content
- J023 W:170019:w3 bucket=M2 dropped=['celý = whole'] verdict=wrong class=content
- J038 W:170043:w3 bucket=M2 dropped=['pred spaním = before bed'] verdict=wrong class=content
- J040 W:170031:w3 bucket=M2 dropped=['celý = whole'] verdict=wrong class=content
- J087 W:170030:w3 bucket=M2 dropped=['na stanicu = at the station'] verdict=wrong class=content
- J098 W:170041:w3 bucket=M2 dropped=['celý = whole'] verdict=wrong class=content

## (iv) Clause-level omissions (listed, not tokenised into the table)

- W:170097:w4 [M2] `Hoci firma sľubuje rýchle dodanie = although the company promises fast delivery`
- W:170113:w4 [M2] `Ak vláda schváli tú novelu = if the government approves that amendment`
- W:170104:w4 [M2] `Kým my sme čakali na verdikt = while we waited for the verdict`
- W:170109:w4 [M2] `Hneď ako komisia vyhodnotí prihlášky = as soon as the committee evaluates the applications`
- W:170060:w3 [M2] `k nám do novej chaty = to us at the new cottage`
- W:170090:w4 [M2] `a dva dni netiekla voda = and there was no water for two days`
- W:170092:w4 [M2] `pretože všetky škatule sú pomiešané = because all the boxes are mixed up`
- W:170086:w4 [M2] `Keďže mechanik nestihne opravu dnes = since the mechanic won't finish the repair today`
- W:170085:w4 [M2] `a je z toho dosť nervózna = and she is quite nervous about it`
- W:170069:w4 [M2] `vždy až v nedeľu večer = always only on Sunday evening`
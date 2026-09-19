# Phase 1Q Task A - type-M triage (0 model calls)

Source: 129 writer-intended type-M items from Phase 1P (intent=="M" in phase1p/data/items.json), joined to the blind judge verdicts in phase1p/judge/out_part1.json via blind_map.json. Counts assert clean: 119 judged correct + 10 judged wrong = 129.

Buckets: M1 function word/particle dropped; M2 content word dropped; M3 content ADDED that the Slovak does not contain; M4 anything else.

## (a) bucket x judged

| bucket | judged correct | judged wrong | total |
|---|---|---|---|
| M1 | 3 | 0 | 3 |
| M2 | 116 | 0 | 116 |
| M3 | 0 | 9 | 9 |
| M4 | 0 | 1 | 1 |
| **total** | **119** | **10** | **129** |

## (b) bucket x level

| bucket | A1 | A2 | B1 | B2 | total |
|---|---|---|---|---|---|
| M1 | 0 | 0 | 0 | 3 | 3 |
| M2 | 30 | 30 | 30 | 26 | 116 |
| M3 | 5 | 4 | 0 | 0 | 9 |
| M4 | 0 | 0 | 0 | 1 | 1 |
| **total** | 35 | 34 | 30 | 30 | 129 |

## (c) judged-CORRECT side, up to 5 examples per bucket

### M1 (judged correct, n=3)

| sid | level | Slovak | answer | dropped / added | reference |
|---|---|---|---|---|---|
| 170107 | B2 | Až keď technici vymenili server, stránka konečne prestala padať. | When the technicians replaced the server, the website stopped crashing. | az (only when); konecne (finally) - focus particle + stance adverb; propositional content intact | PENDING |
| 170110 | B2 | Vtedy sme si my ani neuvedomili, ako veľmi nám tá zmena pomohla. | We did not even realise how much that change had helped us. | vtedy (back then) - deictic time adverb; the past tense keeps the anchor | PENDING |
| 170116 | B2 | Práve táto poisťovňa pokrýva aj škody spôsobené vetrom. | This insurance company covers damage caused by wind. | prave (it is precisely this); aj (also) - two focus particles | PENDING |

### M2 (judged correct, n=116)

| sid | level | Slovak | answer | dropped / added | reference |
|---|---|---|---|---|---|
| 170001 | A1 | Marek každý večer zamyká bránu do záhrady. | Marek locks the garden gate. | kazdy vecer (every evening) | PENDING |
| 170002 | A1 | Ona včera upiekla jablkový koláč pre susedov. | An apple pie was baked yesterday. | ona (she, agent); pre susedov (for the neighbours) - agentless passive | PENDING |
| 170003 | A1 | Môj brat zajtra umyje naše auto pred domom. | Our car will be washed tomorrow. | moj brat (my brother, agent); pred domom (in front of the house) - agentless passive | PENDING |
| 170004 | A1 | Učiteľka teraz opravuje naše písomky v triede. | The teacher is correcting our tests now. | v triede (in the classroom) | PENDING |
| 170005 | A1 | Ja každú nedeľu chodím do parku s kamarátkou. | I go to the park every Sunday. | s kamaratkou (with my friend) | PENDING |

### M3 (judged correct, n=0)

_(none)_

### M4 (judged correct, n=0)

_(none)_

## (d) ALL 10 judged-WRONG items

### judged wrong (n=10)

| sid | level | Slovak | answer | dropped / added | reference |
|---|---|---|---|---|---|
| 170006 | A1 | Otec minulý týždeň natrel plot na zeleno. | Last week my dad carefully painted the whole new fence green. | ADDED: carefully, whole, new | PENDING |
| 170009 | A1 | Deti včera nakreslili veľký obrázok na chodník. | The children drew a big picture on the pavement in front of the school yesterday. | ADDED: in front of the school | PENDING |
| 170012 | A1 | Ja teraz čítam novú knihu o zvieratách. | I am reading an interesting new book about wild animals in my room now. | ADDED: interesting, wild, in my room | PENDING |
| 170021 | A1 | Môj dedko pestuje paradajky v skleníku. | My grandfather grows tomatoes and peppers in the greenhouse. | ADDED: and peppers | PENDING |
| 170024 | A1 | Pes zjedol moju večeru zo stola. | The hungry dog quickly ate my whole dinner off the kitchen table. | ADDED: hungry, quickly, whole, kitchen (table) | PENDING |
| 170033 | A2 | Robotníci budúci týždeň opravia cestu pred školou. | The workers will quickly repair the whole road in front of the new school next week. | ADDED: quickly, whole, new | PENDING |
| 170048 | A2 | Záhradník pokosil trávnik pred naším domom. | This morning the gardener mowed the big lawn in front of our new house. | ADDED: this morning, big, new | PENDING |
| 170054 | A2 | Ona si kúpila nový kabát v zľave. | Yesterday she bought a beautiful new winter coat on sale. | ADDED: beautiful, winter, yesterday | PENDING |
| 170057 | A2 | Ona vyhodila staré noviny do koša. | She angrily threw all the old newspapers into the bin in the kitchen. | ADDED: angrily, all, in the kitchen | PENDING |
| 170100 | B2 | Čím dlhšie o tom ja rozmýšľam, tým menej sa mi ten nápad pozdáva. | The less I like the idea. | DROPPED: Cim dlhsie o tom rozmyslam (the longer I think about it) - ungrammatical fragment: the correlative 'the less ...' is left dangling, not a clean omission | PENDING |

## (e) tie rule and hard cases

**Tie rule (applied):** if an answer both drops something and ADDS content, it is **M3**, with the drop recorded in `note`. In this set no judged-wrong addition item also dropped content, so the rule never had to break a tie; it is stated for the later steps.

**Secondary convention (stated because it moves 30 items):** the "w2" writer edits turn the sentence into an agentless passive AND delete the agent noun plus one more phrase. The voice change alone would be M4, but a content noun (the agent) is genuinely gone, so they are filed as **M2** with `note: "agentless passive"`. If the owner wants voice changes separated, they are exactly the 30 items whose note is "agentless passive".

**Hard to place:**
- `1P019 / 1P023 / 1P031 / 1P041 / 1P091` - only "cely/celu" (whole) is dropped. A quantifying adjective: M1 by feel, M2 by the letter of the definition. Filed **M2**, flagged `quantifying adjective, M1/M2 border`.
- `1P079` ("vacsina" / most) and `1P119` ("mnohe" / many) - quantifiers that do change the claim's scope. Filed **M2**.
- `1P111` ("prilis vela" / too much) - the evaluative load is lost but no noun is. Filed **M2**.
- `1P107` - drops "az" (only when) and "konecne" (finally); both are focus/stance items, propositional content intact. Filed **M1**.
- `1P110` - drops "vtedy" (back then), a deictic the past tense already implies. Filed **M1**.
- `1P100` (judged wrong) - "The less I like the idea." is not an omission, it is a broken correlative fragment. Filed **M4**, the only non-addition on the wrong side.
- `1P017` ("po schodoch" / up the stairs) - "up" appears in the M1 definition, but here the dropped unit is a PP with a content noun. Filed **M2**.


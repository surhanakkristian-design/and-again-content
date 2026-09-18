# Supplementary pass §4.5 — rejections of the independent (fix-split) translations
[STEP: supp] One read (this file), one write: `phase1c/review/supp.json` (under ~/Projects/and-again-content/translation-offline/).
Budget: no other reads, no tools besides the one Write.

Scope: the fix-pass split `phase1c/inputs/supp_fix.json` (90 translations of the supp ids) was run through checker v2 with the
Phase 1c annotations: 25 accepted, 65 rejected (all listed below as R1…R65). The held-out coverage
translations (step 3) are NOT in this split by design, so none of their rejections appear here.

## What to do — per rejection R<n>
1. Is the translation really a correct rendering of the Slovak (same meaning, grammatical, practised structure kept or acceptable)?
2. If NO: record it as "correctly rejected".
3. If YES: give the fix, preferring in this order: `synonym_table` (add a member / group — generalises to other sentences),
   `annotation` (d/g/o/p/s entry for this sentence), `new_variant` (a structurally different variant + its lock). Give the EXACT change
   in the change format below. One fix may cover several rejections — list all their R numbers.
NOTE: the Slovak of id 103 does not match its English (annotated from the English only) — do not "fix" 103 to the Slovak.

## Output format (write exactly this JSON)
{"verdicts":[{"r":"R1","really_correct":true|false,"fix_type":"synonym_table|annotation|new_variant|null","change_idx":[0],"reason":"…"}, ...],
 "changes":[ <change objects as below; referenced by index from verdicts> ],
 "unchanged": <number of rejections judged correctly rejected>}

{"changes":[ <change>, ... ], "unchanged": <int>, "notes": "<optional, one line>"}
Every change carries "target", "op" and a one-line "reason". Allowed changes:
- {"target":"syn","op":"set","group":"<id>","set":{"m":[...],"pos":"v|n|a|x","head":0,"irr":{...},"ok":"…","bad":"…"}}  (only the fields you change)
- {"target":"syn","op":"add_members","group":"<id>","members":["lemma", ...]}
- {"target":"syn","op":"remove_members","group":"<id>","members":["lemma", ...]}
- {"target":"syn","op":"remove_group","group":"<id>"}   (annotation anchors pointing to it are dropped)
- {"target":"syn","op":"merge_into","group":"<ng id>","into":"<existing id>"}   (anchors repointed; add members first if needed)
- {"target":"syn","op":"add_group","group":{"id":"<new id>","kind":"contextual","pos":"v|n|a|x","m":[...],"ok":"…","bad":"…"}}
- {"target":"lib","op":"set_item","item":"<libId>","set":{"verdict":"wrong|correct_with_tip","pattern":"…","sk":"…","cz":"…","en":"…","kind":"…","slots":[...]}}
- {"target":"lib","op":"remove_item","item":"<libId>"}
- {"target":"lib","op":"add_item","type_id":<int>,"item":{full item as in the library}}
- {"target":"ann","op":"set","id":<exercise id>,"key":"v|lk|s|g|o|d|p|m","value":<full new value>}
- {"target":"ann","op":"merge","id":<id>,"key":"s|o|d","value":{"anchor":"…"}}   (adds/overwrites entries)
- {"target":"ann","op":"append","id":<id>,"key":"g|p|m","value":[<entries>]}
- {"target":"ann","op":"delete","id":<id>,"key":"s|o|d|g|p|m","entry":"<anchor, or libId for m, or the p string>"}
- {"target":"ann","op":"add_variant","id":<id>,"variant":"<full sentence>","lock":"<locked span in it>"}
- {"target":"ann","op":"remove_variant","id":<id>,"index":<int ≥1>}
Members are LEMMAS (base form) for pos v/n/a; pos x = fixed surface strings (no inflection).
"unchanged" = number of reviewed units (groups / items / sentences / rejections) you left as they are.

## Format rules (condensed from FORMAT_SPEC.md)
- Synonym group: `kind` safe (swapped everywhere, ~30 groups, do not grow) or contextual (only where an annotation's `s` points to it; needs `ok` = valid example "A = B" and `bad` = invalid example "A ≠ B"). `m` = lemmas; forms are generated (v: base/3sg/past/pp/-ing; n: sg/pl; a: base/-er/-est), a swap keeps the form. pos x = invariant surface strings.
- Library item: verdict `wrong` or `correct_with_tip` (grammatical, same meaning, but not the practised structure / clearly more natural). Feedback: only what is wrong, no praise, English tense names, gender-neutral sk/cz, never the whole reference sentence, ≤150 chars after filling; `{right}`/`{wrong}` filled automatically.
- Annotation: `v` variants (v[0] = reference; ≤3 more, each STRUCTURALLY different — never only a word/determiner/pronoun/optional-word swap), `lk` locked span per variant (the practised grammar; nothing changes inside it), `s` anchor→group, `g` gender chains (only when the Slovak does not fix gender), `o` pronoun alternatives, `d` determiner freedom (A = the|a/an|this|that, P = the|these|those|∅, Z = the|∅, or explicit list; only where the Slovak has no article/demonstrative), `p` optional words (+w insert / -anchor drop; meaning-neutral only), `m` library mistakes [libId, wrongText(, anchor)]. `alt` = the annotator's free-text alternatives (mapped by script into `s`).

## Rejections (65 in 41 sentences)


### 29691 [S A1] EN: He drops his guidebook on the church steps! Total disaster! | SK: Pustí svojho sprievodcu na kostolné schody! Úplná katastrofa!
annotation: {"v": ["He drops his guidebook on the church steps! Total disaster!"], "lk": ["his"], "s": {"drops": "ng1c_3", "guidebook": "ng1c_4", "church steps": "ng1c_5", "Total": "total_complete_absolute", "disaster": "disaster_catastrophe"}}
groups: {"ng1c_3": ["drops", "lets go of", "lets fall"], "ng1c_4": ["guidebook", "guide", "guide book"], "ng1c_5": ["church steps", "steps of the church"], "total_complete_absolute": ["total", "complete", "absolute", "utter"], "disaster_catastrophe": ["disaster", "catastrophe"]}
- R1: “She drops her guidebook on the church stairs! Total disaster!” → checker: Namiesto „she“ patrí „he“. Namiesto „her“ patrí „his“. (step auto)
- R2: “She drops her guide onto the church steps! An absolute disaster!” → checker: Porovnaj svoju vetu so správnym prekladom. (step auto)

### 25921 [S A1] EN: They watch a volcano from the grassy ridge. | SK: Z trávnatého hrebeňa pozorujú sopku
annotation: {"v": ["They watch a volcano from the grassy ridge.", "From the grassy ridge they watch a volcano."], "lk": ["a volcano", "a volcano"], "s": {"watch": "observe_watch", "grassy": "ng1c_6", "ridge": "ng1c_7"}, "d": {"the": "the|a"}}
groups: {"observe_watch": ["watch", "observe"], "ng1c_6": ["grassy", "grass-covered"], "ng1c_7": ["ridge", "crest"]}
- R3: “They are watching the volcano from a grassy ridge.” → checker: Namiesto „are watching the“ patrí „watch a“. (step auto)
- R4: “They're watching a volcano from the grassy ridge.” → checker: Namiesto „are watching“ patrí „watch“. (step auto)

### 27097 [S A2] EN: Of course this square has many advertisements, exactly what we needed. | SK: Jasné, toto námestie má veľa reklám, presne to sme potrebovali.
annotation: {"v": ["Of course this square has many advertisements, exactly what we needed.", "Of course this square has many advertisements, that's exactly what we needed."], "lk": ["many", "many"], "s": {"Of course": "ng1c_9", "square": "ng1c_10", "advertisements": "advertisement_ad", "exactly": "exactly_just_right"}}
groups: {"ng1c_9": ["of course", "sure", "obviously", "clearly"], "ng1c_10": ["square", "plaza"], "advertisement_ad": ["advertisement", "ad", "advert", "commercial"], "exactly_just_right": ["exactly", "just", "right"]}
- R5: “Of course, this square has lots of advertisements, exactly what we needed.” → checker: Namiesto „lots of“ patrí „many“. (step auto)
- R6: “Right, this square has plenty of ads, just what we needed.” → checker: Namiesto „right“ patrí „sure“. Namiesto „plenty of“ patrí „many“. (step auto)

### 9992 [S B1] EN: The ankle that swelled up was the left one. | SK: Členok, ktorý opuchol, bol ten ľavý.
annotation: {"v": ["The ankle that swelled up was the left one.", "The ankle which swelled up was the left one."], "lk": ["that", "which"], "s": {"swelled up": "ng1c_17"}}
groups: {"ng1c_17": ["swell up", "swell", "get swollen"]}
- R7: “The ankle that had swollen up was the left one.” → checker: Namiesto „had swollen“ patrí „swelled“. (step auto)

### 7716 [S B1] EN: She managed to stay completely still until the dragonfly settled. | SK: Podarilo sa jej vydržať úplne nehybne, kým sa vážka usadila.
annotation: {"v": ["She managed to stay completely still until the dragonfly settled."], "lk": ["to stay"], "s": {"completely": "ng1c_18", "still": "still_motionless", "settled": "ng1c_19"}}
groups: {"ng1c_18": ["completely", "totally", "perfectly"], "still_motionless": ["still", "motionless"], "ng1c_19": ["settle", "land", "settle down"]}
- R8: “She managed to keep perfectly still until the dragonfly landed.” → checker: Namiesto „keep“ patrí „stay“. (step auto)
- R9: “She managed to remain completely motionless until the dragonfly settled.” → checker: Namiesto „remain“ patrí „stay“. (step auto)

### 8756 [S B1] EN: He said the puck travelled faster on cold ice. | SK: Povedal, že puk letí rýchlejšie na studenom ľade.
annotation: {"v": ["He said the puck travelled faster on cold ice."], "lk": ["travelled"], "s": {"faster": "ng1c_20"}, "p": ["+that@said"]}
groups: {"ng1c_20": ["faster", "more quickly", "quicker"]}
- R10: “He said the puck flew faster on cold ice.” → checker: Namiesto „flew“ patrí „travelled“. (step auto)
- R11: “He said the puck moves faster on cold ice.” → checker: Namiesto „moves“ patrí „travelled“. (step auto)

### 10959 [S B2] EN: If she had bought thicker paper, the bouquet would be perfect now. | SK: Keby bola kúpila hrubší papier, kytica by bola teraz dokonalá.
annotation: {"v": ["If she had bought thicker paper, the bouquet would be perfect now."], "lk": ["would be"], "s": {"bought": "buy_get", "perfect": "ng1c_26"}}
groups: {"buy_get": ["buy", "get"], "ng1c_26": ["perfect", "flawless"]}
- R12: “If she'd bought thicker paper, the bouquet would now be perfect.” → checker: Pozor na poradie slov: „be perfect now“. (step auto)
- R13: “The bouquet would be perfect now if she had bought thicker paper.” → checker: Pozor na poradie slov. (step auto)

### 7687 [S B2] EN: They had the kitchen filmed while they built the rainbow plate. | SK: Kuchyňu si dali natočiť, kým skladali ten dúhový tanier.
annotation: {"v": ["They had the kitchen filmed while they built the rainbow plate.", "They got the kitchen filmed while they built the rainbow plate."], "lk": ["had .. filmed", "got .. filmed"], "s": {"built": "ng1c_27", "plate": "plate_dish"}, "d": {"the": "the|their", "the#2": "the|that"}}
groups: {"ng1c_27": ["built", "were building", "put together", "assembled", "made"], "plate_dish": ["plate", "dish"]}
- R14: “They got the kitchen filmed while they were putting together the rainbow plate.” → checker: Namiesto „were putting“ patrí „put“. (step auto)

### 9607 [S B2] EN: She is said to have trained at altitude all winter. | SK: Hovorí sa, že celú zimu trénovala vo výške.
annotation: {"v": ["She is said to have trained at altitude all winter.", "It is said that she trained at altitude all winter."], "lk": ["is said", "is said"], "s": {"at altitude": "ng1c_28", "all winter": "all_winter"}}
groups: {"ng1c_28": ["at altitude", "at high altitude"], "all_winter": ["all winter", "all winter long", "the whole winter", "throughout the winter"]}
- R15: “She is said to have been training at altitude all winter long.” → checker: Namiesto „been training“ patrí „trained“. (step auto)

### 10043 [S B2] EN: He asked how long the swelling had been sitting on her foot. | SK: Spýtal sa, ako dlho ten opuch na jej nohe je
annotation: {"v": ["He asked how long the swelling had been sitting on her foot.", "He asked how long the swelling had been on her foot."], "lk": ["had been sitting", "had been"], "s": {"foot": "ng1c_29"}, "d": {"the": "the|that"}}
groups: {"ng1c_29": ["foot", "leg"]}
- R16: “He asked how long the swelling on her leg had been there.” → checker: Chýba „had been“. „had been there“ tu nepatrí. (step auto)
- R17: “He asked her how long she'd had the swelling on her leg.” → checker: „her“ tu nepatrí. Namiesto „she would“ patrí „the swelling“. (step auto)

### 27628 [L A1] EN: The children awake at seven in the morning. | SK: Deti sa zobudia o siedmej ráno.
annotation: {"v": ["The children awake at seven in the morning."], "lk": ["at"], "s": {"awake": "ng1c_30", "seven": "ng1c_31"}, "d": {"The": "Z"}}
groups: {"ng1c_30": ["awake", "wake up", "wake"], "ng1c_31": ["seven", "seven o'clock"]}
- R18: “The kids wake up at seven a.m.” → checker: Namiesto „kids“ patrí „children“. Namiesto „a m“ patrí „in the morning“. (step auto)
- R19: “The kids wake up at 7 in the morning.” → checker: Namiesto „kids“ patrí „children“. (step auto)

### 20298 [L A1] EN: He needs a pill for his bad headache. | SK: Na tú silnú bolesť hlavy potrebuje jednu tabletku.
annotation: {"v": ["He needs a pill for his bad headache."], "lk": ["a pill"], "s": {"bad": "bad_terrible_awful", "needs": "ng1c_34"}, "g": [["He", "his"]], "d": {"his": "his|that|the"}}
groups: {"bad_terrible_awful": ["bad", "terrible", "awful", "severe"], "ng1c_34": ["needs", "needs to take"]}
- R20: “She needs a tablet for that strong headache.” → checker: Namiesto „she“ patrí „he“. Namiesto „tablet“ patrí „pill“. (step auto)
- R21: “She needs one pill for that severe headache.” → checker: Namiesto „she“ patrí „he“. Namiesto „one“ patrí „a“. (step auto)

### 25981 [L A1] EN: The waiter carries ten hot plates at once. | SK: Čašník nesie naraz desať horúcich tanierov.
annotation: {"v": ["The waiter carries ten hot plates at once."], "lk": ["ten"], "s": {"carries": "ng1c_35", "at once": "ng1c_36"}}
groups: {"ng1c_35": ["carries", "is carrying"], "ng1c_36": ["at once", "at the same time", "at one time"]}
- R22: “A waiter is carrying ten hot plates at once.” → checker: Namiesto „a“ patrí „the“. (step auto)

### 26084 [L A1] EN: He can find her before she gets home. | SK: Dokáže ju nájsť skôr, než príde domov.
annotation: {"v": ["He can find her before she gets home."], "lk": ["can"], "s": {"gets": "arrive_come", "find": "ng1c_37"}, "g": [["He"]]}
groups: {"arrive_come": ["arrive", "come", "get"], "ng1c_37": ["find", "track down"]}
- R23: “She can find it before she comes home.” → checker: Namiesto „it“ patrí „her“. (step auto)

### 23669 [L A1] EN: The galaxy moves slowly above their heads. | SK: Galaxia sa pomaly pohybuje nad ich hlavami.
annotation: {"v": ["The galaxy moves slowly above their heads.", "The galaxy slowly moves above their heads."], "lk": ["above", "above"], "s": {"moves": "ng1c_38"}}
groups: {"ng1c_38": ["moves", "is moving", "drifts"]}
- R24: “The galaxy is slowly moving above their heads.” → checker: Pozor na poradie slov: „moving slowly“. (step auto)
- R25: “Slowly, the galaxy moves over their heads.” → checker: „slowly“ tu nepatrí. Namiesto „over“ patrí „slowly above“. (step auto)

### 14806 [L A2] EN: A moment ago she stopped the globe with her hand. | SK: Pred chvíľou zastavila glóbus rukou.
annotation: {"v": ["A moment ago she stopped the globe with her hand.", "She stopped the globe with her hand a moment ago."], "lk": ["stopped", "stopped"], "s": {"A moment ago": "ng1c_40"}}
groups: {"ng1c_40": ["a moment ago", "a minute ago", "just now"]}
- R26: “She stopped the globe with her hand a little while ago.” → checker: Namiesto „little while“ patrí „minute“. (step auto)

### 20702 [L A2] EN: Look! He is lifting the jug higher and higher now. | SK: Pozri! Teraz dvíha džbán vyššie a vyššie.
annotation: {"v": ["Look! He is lifting the jug higher and higher now.", "Look! Now he is lifting the jug higher and higher."], "lk": ["is lifting", "is lifting"], "s": {"jug": "jug_pitcher", "now": "now_right_now"}, "g": [["He"]]}
groups: {"jug_pitcher": ["jug", "pitcher"], "now_right_now": ["now", "right now"]}
- R27: “Look! She's raising the jug higher and higher now.” → checker: Namiesto „raising“ patrí „lifting“. (step auto)

### 11216 [L A2] EN: If you hate the answer, you should not ask the cards. | SK: Ak sa ti odpoveď nepáči, nemal by si sa kariet pýtať.
annotation: {"v": ["If you hate the answer, you should not ask the cards."], "lk": ["should"], "s": {"hate": "ng1c_48"}}
groups: {"ng1c_48": ["hate", "don't like", "do not like", "dislike"]}
- R28: “If the answer doesn't please you, you shouldn't ask the cards.” → checker: Porovnaj svoju vetu so správnym prekladom. (step auto)

### 13395 [L A2] EN: She usually draws hearts, but today she drew a circle. | SK: Zvyčajne kreslí srdcia, ale dnes nakreslila kruh.
annotation: {"v": ["She usually draws hearts, but today she drew a circle."], "lk": ["drew"]}
groups: {}
- R29: “Usually she draws hearts, but today she drew a circle.” → checker: Pozor na poradie slov: „she usually“. (step auto)
- R30: “She usually draws hearts; today, though, she drew a circle.” → checker: Namiesto „today though“ patrí „but today“. (step auto)

### 16009 [L A2] EN: It usually sits still, but now it is croaking loudly. | SK: Zvyčajne sedí ticho, ale teraz hlasno kváka
annotation: {"v": ["It usually sits still, but now it is croaking loudly."], "lk": ["is croaking"], "s": {"sits still": "ng1c_49", "loudly": "ng1c_50"}}
groups: {"ng1c_49": ["sits still", "sits quietly", "sits in silence", "is quiet"], "ng1c_50": ["loudly", "noisily"]}
- R31: “He usually sits quietly, but right now he is croaking loudly.” → checker: Namiesto „he“ patrí „it“. „right“ tu nepatrí. (step auto)
- R32: “She usually sits in silence, but now she's croaking loudly.” → checker: Namiesto „she“ patrí „it“. (step auto)

### 18966 [L A2] EN: There are two people in the empty meadow. | SK: Na prázdnej lúke sú dvaja ľudia.
annotation: {"v": ["There are two people in the empty meadow.", "In the empty meadow there are two people."], "lk": ["are", "are"], "s": {"empty": "empty_deserted", "meadow": "meadow_field"}}
groups: {"empty_deserted": ["empty", "deserted"], "meadow_field": ["meadow", "field"]}
- R33: “There are two people in an empty meadow.” → checker: Namiesto „an“ patrí „the“. (step auto)

### 21467 [L A2] EN: The water is cold, so you should wear boots. | SK: Voda je studená, mal by si si obuť čižmy.
annotation: {"v": ["The water is cold, so you should wear boots."], "lk": ["should"], "s": {"wear": "wear_put_on", "boots": "ng1c_51"}, "d": {"boots": "your|some"}}
groups: {"wear_put_on": ["wear", "put on"], "ng1c_51": ["boots", "rubber boots", "wellies"]}
- R34: “The water is cold. You should put on your wellies.” → checker: Chýba „so“. (step auto)

### 6365 [L B1] EN: The director said they would film the office scene before lunch. | SK: Režisér povedal, že kancelársku scénu natočia pred obedom.
annotation: {"v": ["The director said they would film the office scene before lunch."], "lk": ["would film"], "s": {"office scene": "ng1c_61"}, "p": ["+that@said"]}
groups: {"ng1c_61": ["office scene", "scene in the office"]}
- R35: “The director said the office scene would be shot before lunch.” → checker: Porovnaj svoju vetu so správnym prekladom. (step auto)

### 9498 [L B1] EN: The podium that she is standing behind is older than the school. | SK: Pult, za ktorým stojí, je starší než celá škola.
annotation: {"v": ["The podium that she is standing behind is older than the school.", "The podium which she is standing behind is older than the school.", "The podium behind which she is standing is older than the school."], "lk": ["that", "which", "behind which"], "s": {"podium": "ng1c_67", "is standing": "ng1c_68"}, "g": [["she"]], "p": ["+whole@the#2"]}
groups: {"ng1c_67": ["podium", "lectern", "desk", "counter"], "ng1c_68": ["is standing", "stands"]}
- R36: “The counter behind which she stands is older than the entire school.” → checker: „entire“ tu nepatrí. (step auto)

### 9495 [L B1] EN: Her speech was rewritten twice before she ever walked onto that stage. | SK: Jej prejav bol prepísaný dvakrát, ešte než vôbec vyšla na to pódium.
annotation: {"v": ["Her speech was rewritten twice before she ever walked onto that stage."], "lk": ["was rewritten"], "s": {"speech": "ng1c_69", "ever": "ng1c_70", "walked onto": "ng1c_71"}, "p": ["-ever"]}
groups: {"ng1c_69": ["speech", "talk", "address"], "ng1c_70": ["ever", "even"], "ng1c_71": ["walk onto", "go onto", "steppe onto", "get onto", "go up on"]}
- R37: “Her speech had been rewritten twice before she even went out on that stage.” → checker: Namiesto „had been“ patrí „was“. Namiesto „out“ patrí „up“. (step auto)
- R38: “Her speech was rewritten twice, even before she came out onto that stage.” → checker: „even“ tu nepatrí. Namiesto „came out“ patrí „ever got“. (step auto)

### 2929 [L B1] EN: The eerie light has faded completely, and the yard is dark again. | SK: Desivé svetlo úplne zhaslo a nádražie je zase tmavé.
annotation: {"v": ["The eerie light has faded completely, and the yard is dark again.", "The eerie light has gone out completely, and the yard is dark again."], "lk": ["has faded", "has gone out"], "s": {"eerie": "eerie_creepy_spooky", "completely": "completely_totally", "yard": "ng1c_73", "again": "once_more"}}
groups: {"eerie_creepy_spooky": ["eerie", "creepy", "spooky", "scary"], "completely_totally": ["completely", "totally", "entirely", "fully"], "ng1c_73": ["yard", "station", "station yard", "railway yard"], "once_more": ["once more", "one more time", "again"]}
- R39: “The creepy light has gone out completely, and the railway station is dark again.” → checker: „railway“ tu nepatrí. (step auto)
- R40: “The eerie light has gone out entirely and the train station is dark again.” → checker: „train“ tu nepatrí. (step auto)

### 8017 [L B1] EN: The keeper was standing on his line when the referee pointed to the spot. | SK: Brankár práve stál na čiare, keď rozhodca ukázal na biely bod.
annotation: {"v": ["The keeper was standing on his line when the referee pointed to the spot."], "lk": ["was standing"], "s": {"keeper": "keeper_goalkeeper", "his line": "ng1c_75", "pointed to": "ng1c_76", "the spot": "ng1c_77"}, "p": ["+just@keeper"]}
groups: {"keeper_goalkeeper": ["keeper", "goalkeeper", "goalie"], "ng1c_75": ["his line", "the line", "the goal line"], "ng1c_76": ["pointed to", "pointed at"], "ng1c_77": ["the spot", "the penalty spot", "the white spot"]}
- R41: “The goalie was just standing on the line when the referee pointed at the penalty spot.” → checker: „just“ tu nepatrí. (step auto)
- R42: “The goalkeeper was standing right on the line when the referee pointed to the white mark.” → checker: „right“ tu nepatrí. Namiesto „mark“ patrí „spot“. (step auto)

### 8920 [L B1] EN: The fastest sequence is shown in slow motion at the end. | SK: Najrýchlejšia akcia je ukázaná na konci v spomalenom zábere.
annotation: {"v": ["The fastest sequence is shown in slow motion at the end.", "At the end the fastest sequence is shown in slow motion."], "lk": ["is shown", "is shown"], "s": {"sequence": "ng1c_82"}}
groups: {"ng1c_82": ["sequence", "action", "scene"]}
- R43: “The fastest move is shown in slow motion at the end.” → checker: Namiesto „move“ patrí „sequence“. (step auto)
- R44: “The quickest action is shown at the end in slow motion.” → checker: Porovnaj svoju vetu so správnym prekladom. (step auto)

### 8062 [L B1] EN: She moved to the drum kit while the camera was still rolling. | SK: K bicím prešla, kým kamera ešte bežala.
annotation: {"v": ["She moved to the drum kit while the camera was still rolling.", "While the camera was still rolling, she moved to the drum kit."], "lk": ["moved", "moved"], "s": {"drum kit": "drums_drum_kit", "rolling": "roll_record"}}
groups: {"drums_drum_kit": ["drum kit", "drums"], "roll_record": ["roll", "run", "record"]}
- R45: “She went over to the drums while the camera was still rolling.” → checker: Namiesto „went over“ patrí „moved“. (step auto)
- R46: “While the camera was still running, she moved over to the drums.” → checker: „over“ tu nepatrí. (step auto)

### 10167 [L B1] EN: His mouth is that dry, so the thirst must be real. | SK: Ústa má také suché, že smäd musí byť skutočný.
annotation: {"v": ["His mouth is that dry, so the thirst must be real.", "His mouth is so dry that the thirst must be real."], "lk": ["must", "must"], "s": {"that dry": "ng1c_83", "real": "real_genuine"}, "g": [["His"]]}
groups: {"ng1c_83": ["that dry", "so dry"], "real_genuine": ["real", "genuine"]}
- R47: “Her mouth is so dry that her thirst must be genuine.” → checker: Namiesto „her“ patrí „the“. (step auto)

### 8293 [L B1] EN: She never shares food, so this one must be special. | SK: Jedlo nikdy nedelí, takže tento croissant musí byť výnimočný.
annotation: {"v": ["She never shares food, so this one must be special."], "lk": ["must"], "s": {"this one": "ng1c_84", "special": "special_exceptional", "shares": "share_split"}, "g": [["She"]]}
groups: {"ng1c_84": ["this one", "this croissant"], "special_exceptional": ["special", "exceptional"], "share_split": ["share", "split"]}
- R48: “She never shares her food, so this croissant must be extraordinary.” → checker: „her“ tu nepatrí. Namiesto „extraordinary“ patrí „special“. (step auto)

### 8812 [L B2] EN: Her trainer wishes his pads were a bit thicker. | SK: Tréner by si prial, aby jeho lapy boli trochu hrubšie.
annotation: {"v": ["Her trainer wishes his pads were a bit thicker."], "lk": ["were"], "s": {"trainer": "trainer_coach", "pads": "pad_mitt", "a bit": "a_bit_a_little"}}
groups: {"trainer_coach": ["trainer", "coach"], "pad_mitt": ["pad", "mitt", "focus pad", "focus mitt"], "a_bit_a_little": ["a bit", "a little", "slightly"]}
- R49: “The trainer wishes his mitts were a bit thicker.” → checker: Namiesto „the“ patrí „her“. (step auto)
- R50: “The coach wishes his focus mitts were a little thicker.” → checker: Namiesto „the“ patrí „her“. (step auto)

### 10013 [L B2] EN: Right now he is holding a blue ice pack against the lump. | SK: Práve teraz tlačí modrý obklad na hrču.
annotation: {"v": ["Right now he is holding a blue ice pack against the lump.", "Right now he is pressing a blue ice pack against the lump."], "lk": ["is holding", "is pressing"], "s": {"ice pack": "ng1c_96", "against": "ng1c_79", "lump": "lump_bump"}, "g": [["he"]]}
groups: {"ng1c_96": ["ice pack", "cold pack", "compress", "cold compress"], "ng1c_79": ["on", "against", "to"], "lump_bump": ["bump", "lump"]}
- R51: “She is pressing a blue ice pack on the lump right now.” → checker: Pozor na poradie slov. (step auto)
- R52: “Right now, she's pressing a blue cold pack onto the lump.” → checker: Namiesto „onto“ patrí „against“. (step auto)

### 10866 [L B2] EN: He had been waiting for two hours before his number finally appeared. | SK: Čakal dve hodiny, kým sa konečne objavilo jeho číslo.
annotation: {"v": ["He had been waiting for two hours before his number finally appeared."], "lk": ["had been waiting"], "s": {"before": "ng1c_57", "appeared": "appear_show_up"}}
groups: {"ng1c_57": ["before", "until"], "appear_show_up": ["appear", "show up", "come up", "turn up"]}
- R53: “He'd been waiting two hours when his number finally came up.” → checker: Chýba „for“. Namiesto „when“ patrí „before“. (step auto)
- R54: “By the time his number finally appeared, he had been waiting for two hours.” → checker: Porovnaj svoju vetu so správnym prekladom. (step auto)

### 7998 [L B2] EN: The veranda, where she now spends every morning, faces the sunrise. | SK: Veranda, na ktorej teraz trávi každé ráno, je otočená na východ slnka.
annotation: {"v": ["The veranda, where she now spends every morning, faces the sunrise.", "The veranda, on which she now spends every morning, faces the sunrise.", "The veranda, where she spends every morning now, faces the sunrise."], "lk": ["where", "on which", "where"], "s": {"veranda": "porch_veranda", "faces": "ng1c_101", "the sunrise": "ng1c_102"}, "g": [["she"]]}
groups: {"porch_veranda": ["porch", "veranda"], "ng1c_101": ["faces", "looks towards", "faces towards", "is turned towards"], "ng1c_102": ["the sunrise", "the east", "the rising sun"]}
- R55: “The porch where he spends each morning these days faces the rising sun.” → checker: Namiesto „each“ patrí „every“. Namiesto „these days“ patrí „now“. (step auto)

### 10574 [L B2] EN: He had been training for hours before the light was finally right. | SK: Trénoval hodiny, kým bolo svetlo konečne správne.
annotation: {"v": ["He had been training for hours before the light was finally right."], "lk": ["had been training"], "s": {"before": "ng1c_57", "right": "ng1c_103"}}
groups: {"ng1c_57": ["before", "until"], "ng1c_103": ["right", "good"]}
- R56: “He'd been rehearsing for hours until the lighting was finally right.” → checker: Namiesto „rehearsing“ patrí „training“. Namiesto „lighting“ patrí „light“. (step auto)
- R57: “He had been practicing for hours by the time the light was finally right.” → checker: Namiesto „practicing“ patrí „training“. Namiesto „by the time“ patrí „before“. (step auto)

### 9038 [L B2] EN: Right now he is scribbling a note while the laptop screen glows. | SK: Práve teraz čmára poznámku, kým obrazovka notebooku svieti.
annotation: {"v": ["Right now he is scribbling a note while the laptop screen glows."], "lk": ["is scribbling"], "s": {"glows": "ng1c_104"}, "g": [["he"]]}
groups: {"ng1c_104": ["glows", "shines", "is glowing", "is shining", "is on"]}
- R58: “She is scribbling a note right now while the laptop screen is shining.” → checker: Pozor na poradie slov. (step auto)
- R59: “Right now she's jotting down a note while the laptop's screen glows.” → checker: Namiesto „jotting down“ patrí „scribbling“. Namiesto „laptop's“ patrí „laptop“. (step auto)

### 10107 [L B2] EN: The terminal was empty; even so, she felt watched. | SK: Terminál bol prázdny; aj tak mala pocit, že ju niekto sleduje.
annotation: {"v": ["The terminal was empty; even so, she felt watched.", "The terminal was empty. Even so, she felt watched."], "lk": ["even so", "Even so"], "s": {"empty": "empty_deserted", "felt watched": "ng1c_105"}}
groups: {"empty_deserted": ["empty", "deserted"], "ng1c_105": ["felt watched", "felt that someone was watching her", "felt like someone was watching her", "felt she was being watched"]}
- R60: “The terminal was empty; still, she had the feeling someone was watching her.” → checker: Namiesto „still she had the feeling“ patrí „even so she felt like“. (step auto)
- R61: “The terminal was deserted; all the same, she had a feeling that someone was watching her.” → checker: Namiesto „all the same“ patrí „even so“. Namiesto „had a feeling“ patrí „felt“. (step auto)

### 9913 [L B2] EN: She had her boots dyed purple last summer. | SK: Vlani si dala čižmy zafarbiť na fialovo.
annotation: {"v": ["She had her boots dyed purple last summer.", "Last summer she had her boots dyed purple.", "She got her boots dyed purple last summer."], "lk": ["had", "had", "got"], "s": {"last summer": "ng1c_106"}}
groups: {"ng1c_106": ["last summer", "last year"]}
- R62: “She got her boots coloured purple last year.” → checker: Namiesto „coloured“ patrí „dyed“. (step auto)

### 9966 [L B2] EN: Right now they are shaking hands on the sunny rooftop. | SK: Práve teraz si na slnečnej streche podávajú ruky.
annotation: {"v": ["Right now they are shaking hands on the sunny rooftop.", "They are shaking hands on the sunny rooftop right now."], "lk": ["are shaking", "are shaking"], "s": {"rooftop": "roof_rooftop"}}
groups: {"roof_rooftop": ["roof", "rooftop"]}
- R63: “Right now, on the sunny roof, they're shaking hands.” → checker: Porovnaj svoju vetu so správnym prekladom. (step auto)

### 6884 [L B2] EN: If he had started earlier, he would have missed the mist. | SK: Keby vyrazil skôr, hmlu by bol minul.
annotation: {"v": ["If he had started earlier, he would have missed the mist.", "If he had set off earlier, he would have missed the mist.", "If he had left earlier, he would have missed the mist."], "lk": ["had started", "had set off", "had left"], "s": {"earlier": "ng1c_107", "missed": "ng1c_108"}}
groups: {"ng1c_107": ["early", "soon"], "ng1c_108": ["miss", "avoid"]}
- R64: “If he'd left earlier, he'd have avoided the fog.” → checker: Namiesto „fog“ patrí „mist“. (step auto)
- R65: “If he had left sooner, he would have missed the fog.” → checker: Namiesto „fog“ patrí „mist“. (step auto)

Write the JSON to `phase1c/review/supp.json` now.

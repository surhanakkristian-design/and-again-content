# Review task §4.1 — synonym groups used or proposed by the 80 Phase 1c sentences
[STEP: review-syn] One read (this file), one write: `phase1c/review/syn_1.json` (under ~/Projects/and-again-content/translation-offline/).
Budget: no other reads, no tools besides the one Write.

## What to do
For every group below decide: keep, change or remove. A group is WRONG when a member is not interchangeable with the others in
the sentences that use it (see `ok`/`bad`), when a member changes the meaning, or when a lemma/pos is wrong (pos x ng groups hold
raw surfaces — convert to lemma + pos v/n/a when they inflect, so the checker generates the forms; keep x for invariant phrases).
For the ng proposals (section B): accept only real everyday alternatives for the anchor in THAT sentence; write `ok`/`bad`; merge into
the nearest existing group when it fits; remove members that change the meaning. Be strict: a wrong member causes false acceptances.
NOTE: the Slovak of id 103 does not match its English (annotated from the English only) — do not "fix" 103 to the Slovak.

## Format rules (condensed from FORMAT_SPEC.md)
- Synonym group: `kind` safe (swapped everywhere, ~30 groups, do not grow) or contextual (only where an annotation's `s` points to it; needs `ok` = valid example "A = B" and `bad` = invalid example "A ≠ B"). `m` = lemmas; forms are generated (v: base/3sg/past/pp/-ing; n: sg/pl; a: base/-er/-est), a swap keeps the form. pos x = invariant surface strings.
- Library item: verdict `wrong` or `correct_with_tip` (grammatical, same meaning, but not the practised structure / clearly more natural). Feedback: only what is wrong, no praise, English tense names, gender-neutral sk/cz, never the whole reference sentence, ≤150 chars after filling; `{right}`/`{wrong}` filled automatically.
- Annotation: `v` variants (v[0] = reference; ≤3 more, each STRUCTURALLY different — never only a word/determiner/pronoun/optional-word swap), `lk` locked span per variant (the practised grammar; nothing changes inside it), `s` anchor→group, `g` gender chains (only when the Slovak does not fix gender), `o` pronoun alternatives, `d` determiner freedom (A = the|a/an|this|that, P = the|these|those|∅, Z = the|∅, or explicit list; only where the Slovak has no article/demonstrative), `p` optional words (+w insert / -anchor drop; meaning-neutral only), `m` library mistakes [libId, wrongText(, anchor)]. `alt` = the annotator's free-text alternatives (mapped by script into `s`).

## Output format (write exactly this JSON, nothing else in the file)
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

## Units (56 existing groups + 108 ng proposals = 164)
### A. Existing groups used by these sentences

**Part 1 of 2** — review only the units in this file; write `phase1c/review/syn_1.json`.

- {"id": "a_bit_a_little", "kind": "contextual", "pos": "x", "m": ["a bit", "a little", "slightly"], "ok": "I'm a bit tired. = I'm a little tired.", "bad": "I'd like a little milk. ≠ I'd like slightly milk."}
  used by: 8812 “a bit”
- {"id": "a_lot_of_lots_of", "kind": "contextual", "pos": "x", "m": ["a lot of", "lots of", "plenty of"], "ok": "There were a lot of people. = There were lots of people.", "bad": "I have a lot of work, too much in fact. ≠ I have plenty of work, too much in fact."}
  used by: 13175 “a lot of”
- {"id": "advertisement_ad", "kind": "contextual", "pos": "n", "m": ["advertisement", "ad", "advert", "commercial"], "ok": "I saw an advertisement for this phone. = I saw an ad for this phone.", "bad": "We watched a commercial flight take off. ≠ We watched a ad flight take off."}
  used by: 27097 “advertisements”
- {"id": "all_winter", "kind": "contextual", "pos": "x", "m": ["all winter", "all winter long", "the whole winter", "throughout the winter"], "ok": "The pond was frozen all winter. = The pond was frozen the whole winter.", "bad": "She packed away all winter clothes. ≠ She packed away throughout the winter clothes."}
  used by: 9607 “all winter”
- {"id": "appear_show_up", "kind": "contextual", "pos": "v", "m": ["appear", "show up", "come up", "turn up"], "ok": "The sun finally appeared. = The sun finally came up.", "bad": "It appears that you're right. ≠ It shows up that you're right."}
  used by: 10866 “appeared”
- {"id": "appointment_session_slot", "kind": "contextual", "pos": "n", "m": ["appointment", "slot", "session"], "ok": "She booked an appointment at the gym. = She booked an slot at the gym.", "bad": "Put a coin in the slot. ≠ Put a coin in the appointment."}
  used by: 8209 “appointment”
- {"id": "arrive_come", "kind": "contextual", "pos": "v", "m": ["arrive", "come", "get"], "ok": "When did you arrive? = When did you come?", "bad": "Come here, please. ≠ Arrive here, please."}
  used by: 26084 “gets”
- {"id": "bad_terrible_awful", "kind": "contextual", "pos": "x", "m": ["bad", "terrible", "awful", "severe"], "ok": "She has a bad headache. = She has a terrible headache.", "bad": "Smoking is bad for you, just a bit. ≠ Smoking is terrible for you, just a bit."}
  used by: 20298 “bad”
- {"id": "bag_sack", "kind": "contextual", "pos": "n", "m": ["bag", "sack"], "ok": "A bag of potatoes = A sack of potatoes", "bad": "He got the sack for being late. ≠ He got the bag for being late."}
  used by: 8824 “bag”
- {"id": "barely_hardly", "kind": "contextual", "pos": "x", "m": ["barely", "hardly", "scarcely"], "ok": "She barely lifted her eyes. = She hardly lifted her eyes.", "bad": "It's hardly surprising that he left. ≠ It's barely surprising that he left."}
  used by: 2874 “hardly”
- {"id": "big_large", "kind": "contextual", "pos": "a", "m": ["big", "large"], "ok": "They live in a big house. = They live in a large house.", "bad": "She is my big sister. ≠ She is my large sister."}
  used by: 20435 “big”
- {"id": "buy_get", "kind": "contextual", "pos": "v", "m": ["buy", "get"], "ok": "I bought a new phone. = I got a new phone.", "bad": "I don't buy it — explain again. ≠ I don't get it — explain again."}
  used by: 10959 “bought”
- {"id": "charm_pendant", "kind": "contextual", "pos": "n", "m": ["charm", "pendant"], "ok": "She wore a silver charm on a chain. = She wore a silver pendant on a chain.", "bad": "He won her over with his charm. ≠ He won her over with his pendant."}
  used by: 3937 “charm”
- {"id": "children_kids", "kind": "contextual", "pos": "n", "m": ["child", "kid"], "ok": "The children are asleep. = The kids are asleep.", "bad": "The goat had two kids. ≠ The goat had two children."}
  used by: 6830 “kids”
- {"id": "chopping_board", "kind": "contextual", "pos": "n", "m": ["chopping board", "cutting board", "board"], "ok": "Put the onion on the chopping board. = Put the onion on the cutting board.", "bad": "The board of directors met today. ≠ The cutting board of directors met today."}
  used by: 13175 “board”
- {"id": "combination_combo", "kind": "contextual", "pos": "n", "m": ["combination", "combo"], "ok": "She threw a fast combination. = She threw a fast combo.", "bad": "What's the combination of the safe? ≠ What's the combo of the safe?"}
  used by: 8799 “combination”
- {"id": "completely_totally", "kind": "contextual", "pos": "x", "m": ["completely", "totally", "entirely", "fully"], "ok": "I completely forgot. = I totally forgot.", "bad": "I'm not entirely sure. ≠ I'm not totally sure."}
  used by: 1018 “completely”; 2929 “completely”
- {"id": "disaster_catastrophe", "kind": "contextual", "pos": "n", "m": ["disaster", "catastrophe"], "ok": "The party was a disaster. = The party was a catastrophe.", "bad": "Natural disasters relief fund. ≠ Natural catastrophes relief fund."}
  used by: 29691 “disaster”
- {"id": "drums_drum_kit", "kind": "contextual", "pos": "n", "m": ["drum kit", "drums"], "ok": "She plays the drums. = She plays the drum kit.", "bad": "Oil is stored in drums. ≠ Oil is stored in drum kits."}
  used by: 8062 “drum kit”
- {"id": "eerie_creepy_spooky", "kind": "contextual", "pos": "x", "m": ["eerie", "creepy", "spooky", "scary"], "ok": "The empty station was eerie. = The empty station was creepy.", "bad": "That guy keeps staring at me, he's creepy. ≠ That guy keeps staring at me, he's eerie."}
  used by: 2929 “eerie”
- {"id": "empty_deserted", "kind": "contextual", "pos": "x", "m": ["empty", "deserted"], "ok": "The streets were empty. = The streets were deserted.", "bad": "The bottle is empty. ≠ The bottle is deserted."}
  used by: 10107 “empty”; 18966 “empty”
- {"id": "evidence_proof", "kind": "contextual", "pos": "n", "m": ["evidence", "proof"], "ok": "There is no evidence that he did it. = There is no proof that he did it.", "bad": "This drink is 80 proof. ≠ This drink is 80 evidence."}
  used by: 32342 “evidence”
- {"id": "exactly_just_right", "kind": "contextual", "pos": "x", "m": ["exactly", "just", "right"], "ok": "She arrived exactly at noon. = She arrived just at noon.", "bad": "I just want to sleep. ≠ I exactly want to sleep."}
  used by: 27097 “exactly”
- {"id": "floor_ground", "kind": "contextual", "pos": "n", "m": ["floor", "ground"], "ok": "The book fell to the floor. = The book fell to the ground.", "bad": "Our flat is on the second floor. ≠ Our flat is on the second ground."}
  used by: 4612 “floor”
- {"id": "hold_stay_still", "kind": "contextual", "pos": "v", "m": ["stay", "hold", "keep", "remain"], "ok": "If she stays perfectly still, it won't fly. = If she keeps perfectly still, it won't fly.", "bad": "We stayed at a small hotel. ≠ We held at a small hotel."}
  used by: 7238 “stay”
- {"id": "huge_gigantic", "kind": "contextual", "pos": "x", "m": ["huge", "enormous", "gigantic", "giant", "massive", "vast"], "ok": "Her lashes look huge. = Her lashes look gigantic.", "bad": "Thanks, that's a huge help. ≠ Thanks, that's a giant help."}
  used by: 7037 “huge”
- {"id": "into_in", "kind": "contextual", "pos": "x", "m": ["into", "in"], "ok": "She jumped into the pool. = She jumped in the pool.", "bad": "She is in jazz. ≠ She is into jazz."}
  used by: 1018 “into”
- {"id": "jug_pitcher", "kind": "contextual", "pos": "n", "m": ["jug", "pitcher"], "ok": "A jug of lemonade = A pitcher of lemonade", "bad": "The pitcher threw a fast ball. ≠ The jug threw a fast ball."}
  used by: 20702 “jug”
- {"id": "keeper_goalkeeper", "kind": "contextual", "pos": "n", "m": ["keeper", "goalkeeper", "goalie"], "ok": "The keeper saved the penalty. = The goalkeeper saved the penalty.", "bad": "The zoo keeper fed the lions. ≠ The zoo goalkeeper fed the lions."}
  used by: 8017 “keeper”
- {"id": "lump_bump", "kind": "contextual", "pos": "n", "m": ["bump", "lump"], "ok": "She pressed ice on the bump. = She pressed ice on the lump.", "bad": "We drove over a bump in the road. ≠ We drove over a lump in the road."}
  used by: 10013 “lump”
- {"id": "meadow_field", "kind": "contextual", "pos": "n", "m": ["meadow", "field"], "ok": "Cows grazed in the meadow. = Cows grazed in the field.", "bad": "Physics is not my field. ≠ Physics is not my meadow."}
  used by: 18966 “meadow”
- {"id": "noticeboard", "kind": "contextual", "pos": "n", "m": ["noticeboard", "notice board", "cork board", "corkboard", "pinboard", "bulletin board"], "ok": "The evidence is on the noticeboard. = The evidence is on the pinboard.", "bad": "Sam posted the ad on an online bulletin board. ≠ Sam posted the ad on an online cork board."}
  used by: 32342 “cork board”
- {"id": "now_right_now", "kind": "contextual", "pos": "x", "m": ["now", "right now"], "ok": "She is working now. = She is working right now.", "bad": "Now, where was I? ≠ Right now, where was I?"}
  used by: 20702 “now”
- {"id": "observe_watch", "kind": "contextual", "pos": "v", "m": ["watch", "observe"], "ok": "The scientists watched the birds. = The scientists observed the birds.", "bad": "Watch out for cars! ≠ Observe out for cars!"}
  used by: 25921 “watch”
- {"id": "once_more", "kind": "contextual", "pos": "x", "m": ["once more", "one more time", "again"], "ok": "Try it once more. = Try it one more time.", "bad": "Can you say that again? What was his name? ≠ Can you say that once more? What was his name?"}
  used by: 2929 “again”; 5959 “once more”
- {"id": "pad_mitt", "kind": "contextual", "pos": "n", "m": ["pad", "mitt", "focus pad", "focus mitt"], "ok": "The coach held the pads. = The coach held the mitts.", "bad": "Write it on a pad of paper. ≠ Write it on a mitt of paper."}
  used by: 8812 “pads”
- {"id": "plate_dish", "kind": "contextual", "pos": "n", "m": ["plate", "dish"], "ok": "Put it on a plate. = Put it on a dish.", "bad": "A licence plate. ≠ A licence dish."}
  used by: 7687 “plate”
- {"id": "porch_veranda", "kind": "contextual", "pos": "n", "m": ["porch", "veranda"], "ok": "They sat on the porch. = They sat on the veranda.", "bad": "Take your shoes off in the porch of the church. ≠ Take your shoes off in the veranda of the church."}
  used by: 7998 “veranda”
- {"id": "precisely_exactly", "kind": "contextual", "pos": "x", "m": ["precisely", "exactly"], "ok": "She said she wanted exactly the same one. = She said she wanted precisely the same one.", "bad": "\"Is it far?\" \"Not exactly, about ten minutes.\" ≠ \"Is it far?\" \"Not precisely, about ten minutes.\""}
  used by: 7238 “exactly”
- {"id": "push_shove", "kind": "contextual", "pos": "v", "m": ["push", "shove"], "ok": "Someone pushed me in the queue. = Someone shoved me in the queue.", "bad": "Push the button to start. ≠ Shove the button to start."}
  used by: 8824 “pushed”
- {"id": "quick_fast", "kind": "contextual", "pos": "a", "m": ["quick", "fast"], "ok": "She is a quick runner. = She is a fast runner.", "bad": "Is your watch fast? It says ten past. ≠ Is your watch quick? It says ten past."}
  used by: 24741 “fast”
- {"id": "real_genuine", "kind": "contextual", "pos": "x", "m": ["real", "genuine"], "ok": "Is that a real diamond? = Is that a genuine diamond?", "bad": "It was a real mess. ≠ It was a genuine mess."}
  used by: 10167 “real”
- {"id": "return_come_back", "kind": "contextual", "pos": "v", "m": ["come back", "return", "be back", "go back"], "ok": "She will come back to this market. = She will return to this market.", "bad": "Please return the book to the library. ≠ Please come back the book to the library."}
  used by: 16403 “come back”
- {"id": "roll_record", "kind": "contextual", "pos": "v", "m": ["roll", "run", "record"], "ok": "The cameras were rolling. = The cameras were running.", "bad": "The ball rolled under the sofa. ≠ The ball ran under the sofa."}
  used by: 8062 “rolling”
- {"id": "roof_rooftop", "kind": "contextual", "pos": "n", "m": ["roof", "rooftop"], "ok": "They had a party on the roof. = They had a party on the rooftop.", "bad": "The roof of my mouth is burning. ≠ The rooftop of my mouth is burning."}
  used by: 9966 “rooftop”
- {"id": "share_split", "kind": "contextual", "pos": "v", "m": ["share", "split"], "ok": "We shared the bill. = We split the bill.", "bad": "The wood split in two. ≠ The wood shared in two."}
  used by: 8293 “shares”
- {"id": "special_exceptional", "kind": "contextual", "pos": "x", "m": ["special", "exceptional"], "ok": "Her cooking is special. = Her cooking is exceptional.", "bad": "Today's special is fish soup. ≠ Today's exceptional is fish soup."}
  used by: 8293 “special”
- {"id": "stag_deer", "kind": "contextual", "pos": "n", "m": ["stag", "deer"], "ok": "A stag stood in the clearing. = A deer stood in the clearing.", "bad": "His stag party was in Prague. ≠ His deer party was in Prague."}
  used by: 7037 “stag”
- {"id": "still_motionless", "kind": "contextual", "pos": "x", "m": ["still", "motionless"], "ok": "She managed to remain totally still. = She managed to remain totally motionless.", "bad": "Is it still raining? ≠ Is it motionless raining?"}
  used by: 7716 “still”
- {"id": "tall_high", "kind": "contextual", "pos": "a", "m": ["tall", "high"], "ok": "A tall building = A high building", "bad": "A tall fever. ≠ A high fever."}
  used by: 1018 “tall”
- {"id": "total_complete_absolute", "kind": "contextual", "pos": "x", "m": ["total", "complete", "absolute", "utter"], "ok": "It was a total disaster. = It was a complete disaster.", "bad": "What's the total cost? ≠ What's the complete cost?"}
  used by: 29691 “Total”
- {"id": "trainer_coach", "kind": "contextual", "pos": "n", "m": ["trainer", "coach"], "ok": "Her trainer made her run ten laps. = Her coach made her run ten laps.", "bad": "I need new trainers for running. ≠ I need new coaches for running."}
  used by: 8812 “trainer”
- {"id": "very_really", "kind": "contextual", "pos": "x", "m": ["very", "really"], "ok": "It's very cold. = It's really cold.", "bad": "Do you really think so? ≠ Do you very think so?"}
  used by: 24741 “very”
- {"id": "wear_put_on", "kind": "contextual", "pos": "v", "m": ["wear", "put on"], "ok": "She wore her boots. = She put on her boots.", "bad": "She wears glasses every day. ≠ She puts on glasses every day."}
  used by: 21467 “wear”
- {"id": "whole_entire", "kind": "contextual", "pos": "x", "m": ["whole", "entire", "all"], "ok": "The whole group watched it. = The entire group watched it.", "bad": "He ate the cake whole without chewing. ≠ He ate the cake entire without chewing."}
  used by: 103 “whole”; 4571 “whole”
- {"id": "wrong_incorrect", "kind": "contextual", "pos": "a", "m": ["wrong", "incorrect"], "ok": "That answer is wrong. = That answer is incorrect.", "bad": "What's wrong? You look sad. ≠ What's incorrect? You look sad."}
  used by: 119 “wrong”

### B. Proposed NEW groups (ng) — ok/bad are EMPTY; accept (set ok+bad, fix m/pos), merge_into an existing group, or remove

- {"id": "ng1c_1", "pos": "n", "m": ["in", "to"], "anchor": "in"}
  nearest existing group: {"id": "into_in", "kind": "contextual", "pos": "x", "m": ["into", "in"], "ok": "She jumped into the pool. = She jumped in the pool.", "bad": "She is in jazz. ≠ She is into jazz."}
  sentence(s): 23026 [S A1] EN: She wears the skirt in the park every Sunday. | SK: Túto sukňu nosí do parku každú nedeľu.
  annotator alt: {"23026": {"in": ["to"], "every Sunday": ["on Sundays"]}}
- {"id": "ng1c_2", "pos": "x", "m": ["every sunday", "on sundays"], "anchor": "every sunday"}
  sentence(s): 23026 [S A1] EN: She wears the skirt in the park every Sunday. | SK: Túto sukňu nosí do parku každú nedeľu.
  annotator alt: {"23026": {"in": ["to"], "every Sunday": ["on Sundays"]}}
- {"id": "ng1c_3", "pos": "x", "m": ["drops", "lets go of", "lets fall"], "anchor": "drops"}
  nearest existing group: {"id": "drop_off", "kind": "contextual", "pos": "v", "m": ["drop off", "drop"], "ok": "Can you drop me off at the station? = Can you drop me at the station?", "bad": "I dropped off during the film. ≠ I dropped during the film."}
  sentence(s): 29691 [S A1] EN: He drops his guidebook on the church steps! Total disaster! | SK: Pustí svojho sprievodcu na kostolné schody! Úplná katastrofa!
  annotator alt: {"29691": {"drops": ["lets go of", "lets fall"], "guidebook": ["guide", "guide book"], "church steps": ["steps of the church"], "Total": ["Complete", "Utter"], "disaster": ["catastrophe"]}}
- {"id": "ng1c_4", "pos": "n", "m": ["guidebook", "guide", "guide book"], "anchor": "guidebook"}
  nearest existing group: {"id": "guidebook_guide", "kind": "contextual", "pos": "n", "m": ["guidebook", "guide", "travel guide"], "ok": "The guidebook says the museum closes at five. = The guide says the museum closes at five.", "bad": "Our guide spoke three languages. ≠ Our guidebook spoke three languages."}
  sentence(s): 29691 [S A1] EN: He drops his guidebook on the church steps! Total disaster! | SK: Pustí svojho sprievodcu na kostolné schody! Úplná katastrofa!
  annotator alt: {"29691": {"drops": ["lets go of", "lets fall"], "guidebook": ["guide", "guide book"], "church steps": ["steps of the church"], "Total": ["Complete", "Utter"], "disaster": ["catastrophe"]}}
- {"id": "ng1c_5", "pos": "x", "m": ["church steps", "steps of the church"], "anchor": "church steps"}
  sentence(s): 29691 [S A1] EN: He drops his guidebook on the church steps! Total disaster! | SK: Pustí svojho sprievodcu na kostolné schody! Úplná katastrofa!
  annotator alt: {"29691": {"drops": ["lets go of", "lets fall"], "guidebook": ["guide", "guide book"], "church steps": ["steps of the church"], "Total": ["Complete", "Utter"], "disaster": ["catastrophe"]}}
- {"id": "ng1c_6", "pos": "x", "m": ["grassy", "grass-covered"], "anchor": "grassy"}
  sentence(s): 25921 [S A1] EN: They watch a volcano from the grassy ridge. | SK: Z trávnatého hrebeňa pozorujú sopku
  annotator alt: {"25921": {"watch": ["observe"], "grassy": ["grass-covered"], "ridge": ["crest"]}}
- {"id": "ng1c_7", "pos": "n", "m": ["ridge", "crest"], "anchor": "ridge"}
  sentence(s): 25921 [S A1] EN: They watch a volcano from the grassy ridge. | SK: Z trávnatého hrebeňa pozorujú sopku
  annotator alt: {"25921": {"watch": ["observe"], "grassy": ["grass-covered"], "ridge": ["crest"]}}
- {"id": "ng1c_8", "pos": "v", "m": ["walk", "take", "see"], "anchor": "walk"}
  nearest existing group: {"id": "hike_walk", "kind": "contextual", "pos": "v", "m": ["hike", "walk"], "ok": "We hiked in the mountains. = We walked in the mountains.", "bad": "I walk the dog every morning. ≠ I hike the dog every morning."}
  sentence(s): 16261 [S A2] EN: He has a plan. He is going to walk her home. | SK: Má plán. Chystá sa odprevadiť ju domov.
  annotator alt: {"16261": {"walk": ["take", "see"]}}
- {"id": "ng1c_9", "pos": "x", "m": ["of course", "sure", "obviously", "clearly"], "anchor": "of course"}
  nearest existing group: {"id": "of_course_sure", "kind": "contextual", "pos": "x", "m": ["of course", "sure"], "ok": "\"Can I sit here?\" \"Of course.\" = \"Can I sit here?\" \"Sure.\"", "bad": "I'm not sure about that. ≠ I'm not of course about that."}
  sentence(s): 27097 [S A2] EN: Of course this square has many advertisements, exactly what we needed. | SK: Jasné, toto námestie má veľa reklám, presne to sme potrebovali.
  annotator alt: {"27097": {"Of course": ["Sure", "Obviously", "Clearly"], "square": ["plaza"], "advertisements": ["ads", "adverts"], "exactly": ["just"]}}
- {"id": "ng1c_10", "pos": "n", "m": ["square", "plaza"], "anchor": "square"}
  sentence(s): 27097 [S A2] EN: Of course this square has many advertisements, exactly what we needed. | SK: Jasné, toto námestie má veľa reklám, presne to sme potrebovali.
  annotator alt: {"27097": {"Of course": ["Sure", "Obviously", "Clearly"], "square": ["plaza"], "advertisements": ["ads", "adverts"], "exactly": ["just"]}}
- {"id": "ng1c_11", "pos": "x", "m": ["say bye", "say goodbye"], "anchor": "say bye"}
  sentence(s): 16403 [S A2] EN: Say bye now and she will come back in an hour. | SK: Rozlúč sa a o hodinu sa vráti naspäť.
  annotator alt: {"16403": {"Say bye": ["Say goodbye"], "come back": ["return", "be back"]}}
- {"id": "ng1c_12", "pos": "n", "m": ["blender", "mixer"], "anchor": "blender"}
  sentence(s): 1018 [S B1] EN: He has poured the smoothie into the tall glass, so the blender is completely empty now. | SK: Smoothie prelial do vysokého pohára, takže mixér je teraz úplne prázdny.
  annotator alt: {"1018": {"into": ["in"], "tall": ["high"], "blender": ["mixer"], "completely": ["totally", "entirely"]}}
- {"id": "ng1c_13", "pos": "x", "m": ["race car", "racing car"], "anchor": "race car"}
  sentence(s): 3603 [S B1] EN: The engineer asked him when he was bringing the race car back into the garage. | SK: Inžinier sa ho spýtal, kedy privezie pretekárske auto späť do garáže.
  annotator alt: {"3603": {"race car": ["racing car"], "into": ["to"]}}
- {"id": "ng1c_14", "pos": "n", "m": ["into", "to"], "anchor": "into"}
  nearest existing group: {"id": "into_in", "kind": "contextual", "pos": "x", "m": ["into", "in"], "ok": "She jumped into the pool. = She jumped in the pool.", "bad": "She is in jazz. ≠ She is into jazz."}
  sentence(s): 3603 [S B1] EN: The engineer asked him when he was bringing the race car back into the garage. | SK: Inžinier sa ho spýtal, kedy privezie pretekárske auto späť do garáže.
  annotator alt: {"3603": {"race car": ["racing car"], "into": ["to"]}}
- {"id": "ng1c_15", "pos": "x", "m": ["kept", "kept on"], "anchor": "kept"}
  nearest existing group: {"id": "keep_hold", "kind": "contextual", "pos": "v", "m": ["keep", "hold"], "ok": "Keep still. = Hold still.", "bad": "Keep the change. ≠ Hold the change."}
  sentence(s): 8799 [S B1] EN: She kept throwing the same combination until it felt smooth. | SK: Stále hádzala tú istú kombináciu, kým nešla hladko.
  annotator alt: {"8799": {"kept": ["kept on"], "combination": ["combo"], "felt": ["was"]}}
- {"id": "ng1c_16", "pos": "v", "m": ["felt", "was"], "anchor": "felt"}
  nearest existing group: {"id": "feel_sense", "kind": "contextual", "pos": "v", "m": ["feel", "sense"], "ok": "She felt danger. = She sensed danger.", "bad": "Feel the fabric, it's soft. ≠ Sense the fabric, it's soft."}
  sentence(s): 8799 [S B1] EN: She kept throwing the same combination until it felt smooth. | SK: Stále hádzala tú istú kombináciu, kým nešla hladko.
  annotator alt: {"8799": {"kept": ["kept on"], "combination": ["combo"], "felt": ["was"]}}
- {"id": "ng1c_17", "pos": "v", "m": ["swell up", "swell", "get swollen"], "anchor": "swelled up"}
  nearest existing group: {"id": "swell_swollen", "kind": "contextual", "pos": "v", "m": ["swell", "swell up"], "ok": "Her ankle swelled. = Her ankle swelled up.", "bad": "The music swelled to a climax. ≠ The music swelled up to a climax."}
  sentence(s): 9992 [S B1] EN: The ankle that swelled up was the left one. | SK: Členok, ktorý opuchol, bol ten ľavý.
  annotator alt: {"9992": {"swelled up": ["swelled", "got swollen"]}}
- {"id": "ng1c_18", "pos": "n", "m": ["completely", "totally", "perfectly"], "anchor": "completely"}
  nearest existing group: {"id": "completely_totally", "kind": "contextual", "pos": "x", "m": ["completely", "totally", "entirely", "fully"], "ok": "I completely forgot. = I totally forgot.", "bad": "I'm not entirely sure. ≠ I'm not totally sure."}
  sentence(s): 7716 [S B1] EN: She managed to stay completely still until the dragonfly settled. | SK: Podarilo sa jej vydržať úplne nehybne, kým sa vážka usadila. || 7238 [L B1] EN: If you step exactly where Mira steps, your feet stay completely dry. | SK: Ak stúpaš presne tam, kam stúpa Mira, nohy ti zostanú úplne suché.
  annotator alt: {"7716": {"completely": ["totally", "perfectly"], "still": ["motionless"], "settled": ["landed", "settled down"]}, "7238": {"If": ["When"], "exactly": ["precisely"], "stay": ["remain", "keep"], "completely": ["totally", "perfectly"]}}
- {"id": "ng1c_19", "pos": "v", "m": ["settle", "land", "settle down"], "anchor": "settled"}
  nearest existing group: {"id": "settle_land", "kind": "contextual", "pos": "v", "m": ["settle", "land"], "ok": "The dragonfly settled on the reed. = The dragonfly landed on the reed.", "bad": "They settled the argument. ≠ They landed the argument."}
  sentence(s): 7716 [S B1] EN: She managed to stay completely still until the dragonfly settled. | SK: Podarilo sa jej vydržať úplne nehybne, kým sa vážka usadila.
  annotator alt: {"7716": {"completely": ["totally", "perfectly"], "still": ["motionless"], "settled": ["landed", "settled down"]}}
- {"id": "ng1c_20", "pos": "x", "m": ["faster", "more quickly", "quicker"], "anchor": "faster"}
  nearest existing group: {"id": "quick_fast", "kind": "contextual", "pos": "a", "m": ["quick", "fast"], "ok": "She is a quick runner. = She is a fast runner.", "bad": "Is your watch fast? It says ten past. ≠ Is your watch quick? It says ten past."}
  sentence(s): 8756 [S B1] EN: He said the puck travelled faster on cold ice. | SK: Povedal, že puk letí rýchlejšie na studenom ľade.
  annotator alt: {"8756": {"faster": ["more quickly", "quicker"]}}
- {"id": "ng1c_21", "pos": "n", "m": ["jacket", "coat"], "anchor": "jacket"}
  sentence(s): 9907 [S B2] EN: If she had taken the beige jacket, this look would never have happened. | SK: Keby si bola vzala béžovú bundu, tento look by nikdy nevznikol.
  annotator alt: {"9907": {"jacket": ["coat"], "look": ["outfit"], "happened": ["come about", "come to be"]}}
- {"id": "ng1c_22", "pos": "n", "m": ["look", "outfit"], "anchor": "look"}
  nearest existing group: {"id": "look_style", "kind": "contextual", "pos": "n", "m": ["look", "style"], "ok": "She copied her look. = She copied her style.", "bad": "Have a look at this. ≠ Have a style at this."}
  sentence(s): 9907 [S B2] EN: If she had taken the beige jacket, this look would never have happened. | SK: Keby si bola vzala béžovú bundu, tento look by nikdy nevznikol.
  annotator alt: {"9907": {"jacket": ["coat"], "look": ["outfit"], "happened": ["come about", "come to be"]}}
- {"id": "ng1c_23", "pos": "x", "m": ["happened", "come about", "come to be"], "anchor": "happened"}
  nearest existing group: {"id": "go_on_happen", "kind": "contextual", "pos": "v", "m": ["go on", "happen"], "ok": "What's going on? = What's happening?", "bad": "Go on, tell me! ≠ Happen, tell me!"}
  sentence(s): 9907 [S B2] EN: If she had taken the beige jacket, this look would never have happened. | SK: Keby si bola vzala béžovú bundu, tento look by nikdy nevznikol.
  annotator alt: {"9907": {"jacket": ["coat"], "look": ["outfit"], "happened": ["come about", "come to be"]}}
- {"id": "ng1c_24", "pos": "x", "m": ["a group this quiet", "such a quiet group", "so quiet a group"], "anchor": "a group this quiet"}
  sentence(s): 7558 [S B2] EN: Never had we seen a group this quiet at sunset. | SK: Nikdy predtým sme nevideli takú tichú skupinu pri západe slnka.
  annotator alt: {"7558": {"a group this quiet": ["such a quiet group", "so quiet a group"], "at sunset": ["during sunset"]}}
- {"id": "ng1c_25", "pos": "x", "m": ["at sunset", "during sunset"], "anchor": "at sunset"}
  sentence(s): 7558 [S B2] EN: Never had we seen a group this quiet at sunset. | SK: Nikdy predtým sme nevideli takú tichú skupinu pri západe slnka.
  annotator alt: {"7558": {"a group this quiet": ["such a quiet group", "so quiet a group"], "at sunset": ["during sunset"]}}
- {"id": "ng1c_26", "pos": "v", "m": ["perfect", "flawless"], "anchor": "perfect"}
  sentence(s): 10959 [S B2] EN: If she had bought thicker paper, the bouquet would be perfect now. | SK: Keby bola kúpila hrubší papier, kytica by bola teraz dokonalá.
  annotator alt: {"10959": {"bought": ["got"], "perfect": ["flawless"]}}
- {"id": "ng1c_27", "pos": "x", "m": ["built", "were building", "put together", "assembled", "made"], "anchor": "built"}
  nearest existing group: {"id": "build_assemble", "kind": "contextual", "pos": "v", "m": ["build", "assemble", "put together"], "ok": "They built the wardrobe. = They assembled the wardrobe.", "bad": "The class assembled in the hall. ≠ The class put together in the hall."}
  sentence(s): 7687 [S B2] EN: They had the kitchen filmed while they built the rainbow plate. | SK: Kuchyňu si dali natočiť, kým skladali ten dúhový tanier.
  annotator alt: {"7687": {"built": ["were building", "put together", "assembled", "made"], "plate": ["dish"]}}
- {"id": "ng1c_28", "pos": "x", "m": ["at altitude", "at high altitude"], "anchor": "at altitude"}
  sentence(s): 9607 [S B2] EN: She is said to have trained at altitude all winter. | SK: Hovorí sa, že celú zimu trénovala vo výške.
  annotator alt: {"9607": {"at altitude": ["at high altitude"], "all winter": ["the whole winter", "all winter long"]}}
- {"id": "ng1c_29", "pos": "n", "m": ["foot", "leg"], "anchor": "foot"}
  sentence(s): 10043 [S B2] EN: He asked how long the swelling had been sitting on her foot. | SK: Spýtal sa, ako dlho ten opuch na jej nohe je
  annotator alt: {"10043": {"foot": ["leg"]}}
- {"id": "ng1c_30", "pos": "x", "m": ["awake", "wake up", "wake"], "anchor": "awake"}
  sentence(s): 27628 [L A1] EN: The children awake at seven in the morning. | SK: Deti sa zobudia o siedmej ráno.
  annotator alt: {"27628": {"awake": ["wake up", "wake"], "seven": ["seven o'clock", "7"]}}
- {"id": "ng1c_31", "pos": "x", "m": ["seven", "seven o'clock"], "anchor": "seven"}
  sentence(s): 27628 [L A1] EN: The children awake at seven in the morning. | SK: Deti sa zobudia o siedmej ráno.
  annotator alt: {"27628": {"awake": ["wake up", "wake"], "seven": ["seven o'clock", "7"]}}
- {"id": "ng1c_32", "pos": "n", "m": ["very", "completely", "totally", "really", "perfectly"], "anchor": "very"}
  nearest existing group: {"id": "very_really", "kind": "contextual", "pos": "x", "m": ["very", "really"], "ok": "It's very cold. = It's really cold.", "bad": "Do you really think so? ≠ Do you very think so?"}
  sentence(s): 20435 [L A1] EN: The big plate is white and very clean. | SK: Ten veľký tanier je biely a úplne čistý.
  annotator alt: {"20435": {"very": ["completely", "totally", "really", "perfectly"], "big": ["large"]}}
- {"id": "ng1c_33", "pos": "x", "m": ["rowing team", "rowing crew", "crew"], "anchor": "rowing team"}
  sentence(s): 24741 [L A1] EN: The rowing team is fast and very strong. | SK: Veslársky tím je rýchly a veľmi silný.
  annotator alt: {"24741": {"rowing team": ["rowing crew", "crew"], "fast": ["quick"], "very": ["really"]}}
- {"id": "ng1c_34", "pos": "x", "m": ["needs", "needs to take"], "anchor": "needs"}
  nearest existing group: {"id": "need_require", "kind": "contextual", "pos": "v", "m": ["need", "require"], "ok": "You need a passport. = You require a passport.", "bad": "I need a hug. ≠ I require a hug."}
  sentence(s): 20298 [L A1] EN: He needs a pill for his bad headache. | SK: Na tú silnú bolesť hlavy potrebuje jednu tabletku.
  annotator alt: {"20298": {"bad": ["terrible", "severe", "awful"], "needs": ["needs to take"]}}
- {"id": "ng1c_35", "pos": "x", "m": ["carries", "is carrying"], "anchor": "carries"}
  nearest existing group: {"id": "hold_carry", "kind": "contextual", "pos": "v", "m": ["hold", "carry"], "ok": "She is holding a baby. = She is carrying a baby.", "bad": "The hall holds 500 people. ≠ The hall carries 500 people."}
  sentence(s): 25981 [L A1] EN: The waiter carries ten hot plates at once. | SK: Čašník nesie naraz desať horúcich tanierov.
  annotator alt: {"25981": {"carries": ["is carrying"], "at once": ["at the same time", "at one time"]}}
- {"id": "ng1c_36", "pos": "x", "m": ["at once", "at the same time", "at one time"], "anchor": "at once"}
  nearest existing group: {"id": "immediately_at_once", "kind": "contextual", "pos": "x", "m": ["immediately", "at once", "right away", "straight away"], "ok": "Come here immediately! = Come here at once!", "bad": "They all spoke at once. ≠ They all spoke immediately."}
  sentence(s): 25981 [L A1] EN: The waiter carries ten hot plates at once. | SK: Čašník nesie naraz desať horúcich tanierov.
  annotator alt: {"25981": {"carries": ["is carrying"], "at once": ["at the same time", "at one time"]}}
- {"id": "ng1c_37", "pos": "x", "m": ["find", "track down"], "anchor": "find"}
  nearest existing group: {"id": "find_discover", "kind": "contextual", "pos": "v", "m": ["find", "discover"], "ok": "They found a cave. = They discovered a cave.", "bad": "I find him boring. ≠ I discover him boring."}
  sentence(s): 26084 [L A1] EN: He can find her before she gets home. | SK: Dokáže ju nájsť skôr, než príde domov.
  annotator alt: {"26084": {"gets": ["comes", "arrives"], "find": ["track down"]}}
- {"id": "ng1c_38", "pos": "x", "m": ["moves", "is moving", "drifts"], "anchor": "moves"}
  nearest existing group: {"id": "move_budge", "kind": "contextual", "pos": "v", "m": ["move", "budge"], "ok": "The pile didn't move at all. = The pile didn't budge at all.", "bad": "We moved to Leeds last year. ≠ We budged to Leeds last year."}
  sentence(s): 23669 [L A1] EN: The galaxy moves slowly above their heads. | SK: Galaxia sa pomaly pohybuje nad ich hlavami.
  annotator alt: {"23669": {"moves": ["is moving", "drifts"]}}
- {"id": "ng1c_39", "pos": "x", "m": ["right now", "at the moment", "just now"], "anchor": "right now"}
  nearest existing group: {"id": "right_now_at_the_moment", "kind": "contextual", "pos": "x", "m": ["right now", "at the moment", "at present", "currently"], "ok": "She is right now in a meeting. = She is at the moment in a meeting.", "bad": "Do it right now! ≠ Do it at the moment!"}
  sentence(s): 13034 [L A2] EN: Right now the girl is blowing out the candles. | SK: Práve teraz dievča sfukuje sviečky.
  annotator alt: {"13034": {"Right now": ["At the moment", "Just now"]}}
- {"id": "ng1c_40", "pos": "x", "m": ["a moment ago", "a minute ago", "just now"], "anchor": "a moment ago"}
  sentence(s): 14806 [L A2] EN: A moment ago she stopped the globe with her hand. | SK: Pred chvíľou zastavila glóbus rukou.
  annotator alt: {"14806": {"A moment ago": ["A minute ago", "Just now"]}}
- {"id": "ng1c_41", "pos": "n", "m": ["glass", "cup"], "anchor": "glass"}
  nearest existing group: {"id": "glass_tumbler", "kind": "contextual", "pos": "n", "m": ["glass", "tumbler"], "ok": "A glass of water = A tumbler of water", "bad": "The tumbler did five backflips. ≠ The glass did five backflips."}
  sentence(s): 24733 [L A2] EN: The glass is hot, so you must hold it carefully. | SK: Pohárik je horúci, tak ho musíš držať opatrne.
  annotator alt: {"24733": {"glass": ["cup"], "hold": ["handle"]}}
- {"id": "ng1c_42", "pos": "v", "m": ["hold", "handle"], "anchor": "hold"}
  nearest existing group: {"id": "hold_carry", "kind": "contextual", "pos": "v", "m": ["hold", "carry"], "ok": "She is holding a baby. = She is carrying a baby.", "bad": "The hall holds 500 people. ≠ The hall carries 500 people."}
  sentence(s): 24733 [L A2] EN: The glass is hot, so you must hold it carefully. | SK: Pohárik je horúci, tak ho musíš držať opatrne.
  annotator alt: {"24733": {"glass": ["cup"], "hold": ["handle"]}}
- {"id": "ng1c_43", "pos": "x", "m": ["reflector", "reflector board", "reflective board"], "anchor": "reflector"}
  sentence(s): 11348 [L A2] EN: Look! The assistant is holding the reflector up now. | SK: Pozri! Asistent práve drží odrazovú dosku hore.
  annotator alt: {"11348": {"reflector": ["reflector board", "reflective board"], "now": ["right now", "at the moment"]}}
- {"id": "ng1c_44", "pos": "x", "m": ["now", "right now", "at the moment"], "anchor": "now"}
  nearest existing group: {"id": "now_right_now", "kind": "contextual", "pos": "x", "m": ["now", "right now"], "ok": "She is working now. = She is working right now.", "bad": "Now, where was I? ≠ Right now, where was I?"}
  sentence(s): 11348 [L A2] EN: Look! The assistant is holding the reflector up now. | SK: Pozri! Asistent práve drží odrazovú dosku hore.
  annotator alt: {"11348": {"reflector": ["reflector board", "reflective board"], "now": ["right now", "at the moment"]}}
- {"id": "ng1c_45", "pos": "x", "m": ["stays dry", "stays under a roof", "stays indoors", "stays inside", "stays under cover"], "anchor": "stays dry"}
  sentence(s): 21124 [L A2] EN: She usually stays dry, but today she is dancing in the rain. | SK: Zvyčajne ostáva pod strechou, ale dnes tancuje v daždi.
  annotator alt: {"21124": {"stays dry": ["stays under a roof", "stays indoors", "stays inside", "stays under cover"]}}
- {"id": "ng1c_46", "pos": "x", "m": ["a minute", "a moment", "a second"], "anchor": "a minute"}
  sentence(s): 11980 [L A2] EN: Wait a minute and the water will boil! | SK: Počkaj chvíľu a voda zovrie!
  annotator alt: {"11980": {"a minute": ["a moment", "a second"], "boil": ["start boiling", "come to the boil"]}}
- {"id": "ng1c_47", "pos": "v", "m": ["boil", "start boiling", "come to the boil"], "anchor": "boil"}
  nearest existing group: {"id": "boil_come_to_boil", "kind": "contextual", "pos": "v", "m": ["boil", "come to the boil", "come to a boil"], "ok": "Wait for the water to boil. = Wait for the water to come to the boil.", "bad": "Boil the potatoes for twenty minutes. ≠ Come to the boil the potatoes for twenty minutes."}
  sentence(s): 11980 [L A2] EN: Wait a minute and the water will boil! | SK: Počkaj chvíľu a voda zovrie!
  annotator alt: {"11980": {"a minute": ["a moment", "a second"], "boil": ["start boiling", "come to the boil"]}}
- {"id": "ng1c_48", "pos": "x", "m": ["hate", "don't like", "do not like", "dislike"], "anchor": "hate"}
  nearest existing group: {"id": "hate_dislike", "kind": "contextual", "pos": "v", "m": ["hate", "dislike", "not like"], "ok": "She hates broccoli. = She dislikes broccoli.", "bad": "I hate to say it, but you're wrong. ≠ I dislike to say it, but you're wrong."}
  sentence(s): 11216 [L A2] EN: If you hate the answer, you should not ask the cards. | SK: Ak sa ti odpoveď nepáči, nemal by si sa kariet pýtať.
  annotator alt: {"11216": {"hate": ["don't like", "do not like", "dislike"]}}
- {"id": "ng1c_49", "pos": "x", "m": ["sits still", "sits quietly", "sits in silence", "is quiet"], "anchor": "sits still"}
  sentence(s): 16009 [L A2] EN: It usually sits still, but now it is croaking loudly. | SK: Zvyčajne sedí ticho, ale teraz hlasno kváka
  annotator alt: {"16009": {"sits still": ["sits quietly", "sits in silence", "is quiet"], "loudly": ["noisily"]}}
- {"id": "ng1c_50", "pos": "n", "m": ["loudly", "noisily"], "anchor": "loudly"}
  sentence(s): 16009 [L A2] EN: It usually sits still, but now it is croaking loudly. | SK: Zvyčajne sedí ticho, ale teraz hlasno kváka
  annotator alt: {"16009": {"sits still": ["sits quietly", "sits in silence", "is quiet"], "loudly": ["noisily"]}}
- {"id": "ng1c_51", "pos": "x", "m": ["boots", "rubber boots", "wellies"], "anchor": "boots"}
  nearest existing group: {"id": "kick_boot", "kind": "contextual", "pos": "v", "m": ["kick", "boot"], "ok": "He kicked the ball away. = He booted the ball away.", "bad": "Boot up the laptop. ≠ Kick up the laptop."}
  sentence(s): 21467 [L A2] EN: The water is cold, so you should wear boots. | SK: Voda je studená, mal by si si obuť čižmy.
  annotator alt: {"21467": {"wear": ["put on"], "boots": ["rubber boots", "wellies"]}}
- {"id": "ng1c_52", "pos": "x", "m": ["the moment", "the instant", "as soon as", "just as"], "anchor": "the moment"}
  sentence(s): 3084 [L B1] EN: The moment her friend made her laugh, her hand slipped and the line went crooked. | SK: V momente, keď ju kamarátka rozosmiala, jej ruka sa šmykla a čiara išla nakrivo.
  annotator alt: {"3084": {"The moment": ["The instant", "As soon as", "Just as"], "made her laugh": ["got her laughing"], "went crooked": ["came out crooked", "got crooked"]}}
- {"id": "ng1c_53", "pos": "x", "m": ["made her laugh", "got her laughing"], "anchor": "made her laugh"}
  sentence(s): 3084 [L B1] EN: The moment her friend made her laugh, her hand slipped and the line went crooked. | SK: V momente, keď ju kamarátka rozosmiala, jej ruka sa šmykla a čiara išla nakrivo.
  annotator alt: {"3084": {"The moment": ["The instant", "As soon as", "Just as"], "made her laugh": ["got her laughing"], "went crooked": ["came out crooked", "got crooked"]}}
- {"id": "ng1c_54", "pos": "x", "m": ["went crooked", "came out crooked", "got crooked"], "anchor": "went crooked"}
  sentence(s): 3084 [L B1] EN: The moment her friend made her laugh, her hand slipped and the line went crooked. | SK: V momente, keď ju kamarátka rozosmiala, jej ruka sa šmykla a čiara išla nakrivo.
  annotator alt: {"3084": {"The moment": ["The instant", "As soon as", "Just as"], "made her laugh": ["got her laughing"], "went crooked": ["came out crooked", "got crooked"]}}
- {"id": "ng1c_55", "pos": "x", "m": ["altogether", "in total", "in all"], "anchor": "altogether"}
  sentence(s): 4449 [L B1] EN: Altogether she lowered the basket three times before the man had all his oranges. | SK: Celkovo spustila kôš trikrát, kým mal muž všetky svoje pomaranče.
  annotator alt: {"4449": {"Altogether": ["In total", "In all"], "had": ["got", "received"], "before": ["until"]}}
- {"id": "ng1c_56", "pos": "v", "m": ["have", "get", "receive"], "anchor": "had"}
  nearest existing group: {"id": "eat_have", "kind": "contextual", "pos": "v", "m": ["eat", "have"], "ok": "She ate a banana. = She had a banana.", "bad": "She had a shower. ≠ She ate a shower."}
  sentence(s): 4449 [L B1] EN: Altogether she lowered the basket three times before the man had all his oranges. | SK: Celkovo spustila kôš trikrát, kým mal muž všetky svoje pomaranče.
  annotator alt: {"4449": {"Altogether": ["In total", "In all"], "had": ["got", "received"], "before": ["until"]}}
- {"id": "ng1c_57", "pos": "n", "m": ["before", "until"], "anchor": "before"}
  nearest existing group: {"id": "in_front_of_before", "kind": "contextual", "pos": "x", "m": ["in front of", "before"], "ok": "She stood in front of the judge. = She stood before the judge.", "bad": "Wash your hands before dinner. ≠ Wash your hands in front of dinner."}
  sentence(s): 4449 [L B1] EN: Altogether she lowered the basket three times before the man had all his oranges. | SK: Celkovo spustila kôš trikrát, kým mal muž všetky svoje pomaranče. || 10866 [L B2] EN: He had been waiting for two hours before his number finally appeared. | SK: Čakal dve hodiny, kým sa konečne objavilo jeho číslo. || 10574 [L B2] EN: He had been training for hours before the light was finally right. | SK: Trénoval hodiny, kým bolo svetlo konečne správne.
  annotator alt: {"4449": {"Altogether": ["In total", "In all"], "had": ["got", "received"], "before": ["until"]}, "10866": {"before": ["until"], "appeared": ["came up", "showed up"]}, "10574": {"before": ["until"], "right": ["good"]}}
- {"id": "ng1c_58", "pos": "n", "m": ["spine", "thorn", "needle"], "anchor": "spines"}
  sentence(s): 1452 [L B1] EN: If he touches that cactus, he will spend the evening pulling spines out of his finger. | SK: Ak sa dotkne toho kaktusa, strávi večer vyťahovaním tŕňov z prsta.
  annotator alt: {"1452": {"spines": ["thorns", "needles"], "pulling": ["taking", "getting"]}}
- {"id": "ng1c_59", "pos": "v", "m": ["pull", "take", "get"], "anchor": "pulling"}
  nearest existing group: {"id": "pull_drag", "kind": "contextual", "pos": "v", "m": ["pull", "drag"], "ok": "She was pulling a heavy suitcase. = She was dragging a heavy suitcase.", "bad": "He pulled a muscle. ≠ He dragged a muscle."}
  sentence(s): 1452 [L B1] EN: If he touches that cactus, he will spend the evening pulling spines out of his finger. | SK: Ak sa dotkne toho kaktusa, strávi večer vyťahovaním tŕňov z prsta.
  annotator alt: {"1452": {"spines": ["thorns", "needles"], "pulling": ["taking", "getting"]}}
- {"id": "ng1c_60", "pos": "x", "m": ["did not move a whisker", "did not move at all", "did not twitch a whisker", "did not even twitch a whisker"], "anchor": "did not move a whisker"}
  sentence(s): 9244 [L B1] EN: While the waves were rolling in, the black cat did not move a whisker. | SK: Kým sa vlny valili, čierna mačka nepohla ani fúzom.
  annotator alt: {"9244": {"did not move a whisker": ["did not move at all", "did not twitch a whisker", "did not even twitch a whisker"]}}
- {"id": "ng1c_61", "pos": "x", "m": ["office scene", "scene in the office"], "anchor": "office scene"}
  sentence(s): 6365 [L B1] EN: The director said they would film the office scene before lunch. | SK: Režisér povedal, že kancelársku scénu natočia pred obedom.
  annotator alt: {"6365": {"office scene": ["scene in the office"]}}
- {"id": "ng1c_62", "pos": "n", "m": ["if", "when"], "anchor": "if"}
  sentence(s): 4571 [L B1] EN: If you leave one screw loose, the whole chair wobbles. | SK: Keď necháš jednu skrutku uvoľnenú, celá stolička sa kýve. || 7238 [L B1] EN: If you step exactly where Mira steps, your feet stay completely dry. | SK: Ak stúpaš presne tam, kam stúpa Mira, nohy ti zostanú úplne suché.
  annotator alt: {"4571": {"If": ["When"], "one": ["a", "a single"], "loose": ["unscrewed", "undone"], "whole": ["entire"], "wobbles": ["shakes", "rocks"]}, "7238": {"If": ["When"], "exactly": ["precisely"], "stay": ["remain", "keep"], "completely": ["totally", "perfectly"]}}
- {"id": "ng1c_63", "pos": "x", "m": ["one", "a", "a single"], "anchor": "one"}
  sentence(s): 4571 [L B1] EN: If you leave one screw loose, the whole chair wobbles. | SK: Keď necháš jednu skrutku uvoľnenú, celá stolička sa kýve.
  annotator alt: {"4571": {"If": ["When"], "one": ["a", "a single"], "loose": ["unscrewed", "undone"], "whole": ["entire"], "wobbles": ["shakes", "rocks"]}}
- {"id": "ng1c_64", "pos": "n", "m": ["loose", "unscrewed", "undone"], "anchor": "loose"}
  sentence(s): 4571 [L B1] EN: If you leave one screw loose, the whole chair wobbles. | SK: Keď necháš jednu skrutku uvoľnenú, celá stolička sa kýve.
  annotator alt: {"4571": {"If": ["When"], "one": ["a", "a single"], "loose": ["unscrewed", "undone"], "whole": ["entire"], "wobbles": ["shakes", "rocks"]}}
- {"id": "ng1c_65", "pos": "v", "m": ["wobble", "shake", "rock"], "anchor": "wobbles"}
  nearest existing group: {"id": "wobble_shake", "kind": "contextual", "pos": "v", "m": ["wobble", "shake"], "ok": "The table wobbles. = The table shakes.", "bad": "Let's shake hands. ≠ Let's wobble hands."}
  sentence(s): 4571 [L B1] EN: If you leave one screw loose, the whole chair wobbles. | SK: Keď necháš jednu skrutku uvoľnenú, celá stolička sa kýve.
  annotator alt: {"4571": {"If": ["When"], "one": ["a", "a single"], "loose": ["unscrewed", "undone"], "whole": ["entire"], "wobbles": ["shakes", "rocks"]}}
- {"id": "ng1c_66", "pos": "x", "m": ["makes that face", "pulls that face", "makes that grimace"], "anchor": "makes that face"}
  sentence(s): 7458 [L B1] EN: Everyone makes that face, don't they? | SK: Tú grimasu robí každý, však?
  annotator alt: {"7458": {"makes that face": ["pulls that face", "makes that grimace"]}}
- {"id": "ng1c_67", "pos": "n", "m": ["podium", "lectern", "desk", "counter"], "anchor": "podium"}
  nearest existing group: {"id": "podium_lectern", "kind": "contextual", "pos": "n", "m": ["podium", "lectern"], "ok": "She stood at the podium. = She stood at the lectern.", "bad": "She finished third and stood on the podium. ≠ She finished third and stood on the lectern."}
  sentence(s): 9498 [L B1] EN: The podium that she is standing behind is older than the school. | SK: Pult, za ktorým stojí, je starší než celá škola.
  annotator alt: {"9498": {"podium": ["lectern", "desk", "counter"], "is standing": ["stands"]}}
- {"id": "ng1c_68", "pos": "x", "m": ["is standing", "stands"], "anchor": "is standing"}
  sentence(s): 9498 [L B1] EN: The podium that she is standing behind is older than the school. | SK: Pult, za ktorým stojí, je starší než celá škola.
  annotator alt: {"9498": {"podium": ["lectern", "desk", "counter"], "is standing": ["stands"]}}
- {"id": "ng1c_69", "pos": "n", "m": ["speech", "talk", "address"], "anchor": "speech"}
  sentence(s): 9495 [L B1] EN: Her speech was rewritten twice before she ever walked onto that stage. | SK: Jej prejav bol prepísaný dvakrát, ešte než vôbec vyšla na to pódium.
  annotator alt: {"9495": {"speech": ["talk", "address"], "ever": ["even"], "walked onto": ["went onto", "stepped onto", "got onto", "went up on"]}}
- {"id": "ng1c_70", "pos": "v", "m": ["ever", "even"], "anchor": "ever"}
  sentence(s): 9495 [L B1] EN: Her speech was rewritten twice before she ever walked onto that stage. | SK: Jej prejav bol prepísaný dvakrát, ešte než vôbec vyšla na to pódium.
  annotator alt: {"9495": {"speech": ["talk", "address"], "ever": ["even"], "walked onto": ["went onto", "stepped onto", "got onto", "went up on"]}}
- {"id": "ng1c_71", "pos": "v", "m": ["walk onto", "go onto", "steppe onto", "get onto", "go up on"], "anchor": "walked onto"}
  nearest existing group: {"id": "walk_onto_step_onto", "kind": "contextual", "pos": "v", "m": ["walk onto", "step onto", "go onto", "get on"], "ok": "She walked onto the stage. = She stepped onto the stage.", "bad": "She got on well with her boss. ≠ She stepped onto well with her boss."}
  sentence(s): 9495 [L B1] EN: Her speech was rewritten twice before she ever walked onto that stage. | SK: Jej prejav bol prepísaný dvakrát, ešte než vôbec vyšla na to pódium.
  annotator alt: {"9495": {"speech": ["talk", "address"], "ever": ["even"], "walked onto": ["went onto", "stepped onto", "got onto", "went up on"]}}
- {"id": "ng1c_72", "pos": "x", "m": ["into place", "into position"], "anchor": "into place"}
  sentence(s): 8824 [L B1] EN: While the chain was swinging, he pushed the bag into place. | SK: Kým sa reťaz kývala, dotlačil vrece na miesto.
  annotator alt: {"8824": {"pushed": ["shoved"], "bag": ["sack"], "into place": ["into position"]}}
- {"id": "ng1c_73", "pos": "x", "m": ["yard", "station", "station yard", "railway yard"], "anchor": "yard"}
  nearest existing group: {"id": "garden_yard", "kind": "contextual", "pos": "n", "m": ["garden", "yard", "backyard"], "ok": "The kids play in the garden. = The kids play in the yard.", "bad": "The table is one yard long. ≠ The table is one garden long."}
  sentence(s): 2929 [L B1] EN: The eerie light has faded completely, and the yard is dark again. | SK: Desivé svetlo úplne zhaslo a nádražie je zase tmavé.
  annotator alt: {"2929": {"eerie": ["creepy", "spooky", "scary"], "completely": ["fully", "entirely"], "yard": ["station", "station yard", "railway yard"], "again": ["once more"]}}
- {"id": "ng1c_74", "pos": "x", "m": ["jar", "glass jar"], "anchor": "jar"}
  sentence(s): 6830 [L B1] EN: As kids they would buy dried herbs in a jar. | SK: Ako deti kupovali sušené bylinky v pohári.
  annotator alt: {"6830": {"kids": ["children"], "jar": ["glass jar"]}}
- {"id": "ng1c_75", "pos": "x", "m": ["his line", "the line", "the goal line"], "anchor": "his line"}
  sentence(s): 8017 [L B1] EN: The keeper was standing on his line when the referee pointed to the spot. | SK: Brankár práve stál na čiare, keď rozhodca ukázal na biely bod.
  annotator alt: {"8017": {"keeper": ["goalkeeper", "goalie"], "his line": ["the line", "the goal line"], "pointed to": ["pointed at"], "the spot": ["the penalty spot", "the white spot"]}}
- {"id": "ng1c_76", "pos": "x", "m": ["pointed to", "pointed at"], "anchor": "pointed to"}
  sentence(s): 8017 [L B1] EN: The keeper was standing on his line when the referee pointed to the spot. | SK: Brankár práve stál na čiare, keď rozhodca ukázal na biely bod.
  annotator alt: {"8017": {"keeper": ["goalkeeper", "goalie"], "his line": ["the line", "the goal line"], "pointed to": ["pointed at"], "the spot": ["the penalty spot", "the white spot"]}}
- {"id": "ng1c_77", "pos": "x", "m": ["the spot", "the penalty spot", "the white spot"], "anchor": "the spot"}
  sentence(s): 8017 [L B1] EN: The keeper was standing on his line when the referee pointed to the spot. | SK: Brankár práve stál na čiare, keď rozhodca ukázal na biely bod.
  annotator alt: {"8017": {"keeper": ["goalkeeper", "goalie"], "his line": ["the line", "the goal line"], "pointed to": ["pointed at"], "the spot": ["the penalty spot", "the white spot"]}}
- {"id": "ng1c_78", "pos": "x", "m": ["keycard", "card", "key card"], "anchor": "keycard"}
  sentence(s): 119 [L B1] EN: How long has she been tapping that keycard on the wrong door? | SK: Ako dlho prikladá tou kartou na nesprávne dvere?
  annotator alt: {"119": {"keycard": ["card", "key card"], "on": ["against", "to"], "wrong": ["incorrect"]}}
- {"id": "ng1c_79", "pos": "n", "m": ["on", "against", "to"], "anchor": "on"}
  nearest existing group: {"id": "on_against", "kind": "contextual", "pos": "x", "m": ["on", "against"], "ok": "She pressed the pack on the bump. = She pressed the pack against the bump.", "bad": "She voted against the plan. ≠ She voted on the plan."}
  sentence(s): 119 [L B1] EN: How long has she been tapping that keycard on the wrong door? | SK: Ako dlho prikladá tou kartou na nesprávne dvere? || 10013 [L B2] EN: Right now he is holding a blue ice pack against the lump. | SK: Práve teraz tlačí modrý obklad na hrču.
  annotator alt: {"119": {"keycard": ["card", "key card"], "on": ["against", "to"], "wrong": ["incorrect"]}, "10013": {"ice pack": ["cold pack", "compress", "cold compress"], "against": ["on", "to"], "lump": ["bump"]}}
- {"id": "ng1c_80", "pos": "v", "m": ["turn", "twist", "rotate"], "anchor": "turns"}
  nearest existing group: {"id": "turn_spin_rotate", "kind": "contextual", "pos": "v", "m": ["turn", "spin", "rotate"], "ok": "The wheel turned. = The wheel spun.", "bad": "Turn left at the lights. ≠ Spin left at the lights."}
  sentence(s): 5959 [L B1] EN: If he turns the ring once more, she will drop the price again. | SK: Ak prsteň otočí ešte raz, zníži cenu znova.
  annotator alt: {"5959": {"turns": ["twists", "rotates"], "once more": ["one more time"], "again": ["once again"]}}
- {"id": "ng1c_81", "pos": "x", "m": ["again", "once again"], "anchor": "again"}
  nearest existing group: {"id": "once_more", "kind": "contextual", "pos": "x", "m": ["once more", "one more time", "again"], "ok": "Try it once more. = Try it one more time.", "bad": "Can you say that again? What was his name? ≠ Can you say that once more? What was his name?"}
  sentence(s): 5959 [L B1] EN: If he turns the ring once more, she will drop the price again. | SK: Ak prsteň otočí ešte raz, zníži cenu znova.
  annotator alt: {"5959": {"turns": ["twists", "rotates"], "once more": ["one more time"], "again": ["once again"]}}
- {"id": "ng1c_82", "pos": "n", "m": ["sequence", "action", "scene"], "anchor": "sequence"}
  sentence(s): 8920 [L B1] EN: The fastest sequence is shown in slow motion at the end. | SK: Najrýchlejšia akcia je ukázaná na konci v spomalenom zábere.
  annotator alt: {"8920": {"sequence": ["action", "scene"]}}
- {"id": "ng1c_83", "pos": "x", "m": ["that dry", "so dry"], "anchor": "that dry"}
  sentence(s): 10167 [L B1] EN: His mouth is that dry, so the thirst must be real. | SK: Ústa má také suché, že smäd musí byť skutočný.
  annotator alt: {"10167": {"that dry": ["so dry"], "real": ["genuine"]}}
- {"id": "ng1c_84", "pos": "x", "m": ["this one", "this croissant"], "anchor": "this one"}
  sentence(s): 8293 [L B1] EN: She never shares food, so this one must be special. | SK: Jedlo nikdy nedelí, takže tento croissant musí byť výnimočný.
  annotator alt: {"8293": {"this one": ["this croissant"], "special": ["exceptional"], "shares": ["splits"]}}
- {"id": "ng1c_85", "pos": "x", "m": ["ball", "little ball"], "anchor": "ball"}
  sentence(s): 3494 [L B2] EN: If the ball had landed in black, she would have gone home with empty pockets. | SK: Keby bola guľôčka padla na čiernej, išla by domov s prázdnymi vreckami.
  annotator alt: {"3494": {"ball": ["little ball"], "in black": ["on black", "on the black", "in the black"]}}
- {"id": "ng1c_86", "pos": "x", "m": ["in black", "on black", "on the black", "in the black"], "anchor": "in black"}
  sentence(s): 3494 [L B2] EN: If the ball had landed in black, she would have gone home with empty pockets. | SK: Keby bola guľôčka padla na čiernej, išla by domov s prázdnymi vreckami.
  annotator alt: {"3494": {"ball": ["little ball"], "in black": ["on black", "on the black", "in the black"]}}
- {"id": "ng1c_87", "pos": "x", "m": ["guard", "security guard", "watchman"], "anchor": "guard"}
  nearest existing group: {"id": "protect_guard", "kind": "contextual", "pos": "v", "m": ["protect", "guard", "defend"], "ok": "Dogs guard the house. = Dogs protect the house.", "bad": "Sunscreen protects your skin. ≠ Sunscreen guards your skin."}
  sentence(s): 2955 [L B2] EN: The guard wishes he had turned the camera towards the horizon a minute earlier. | SK: Strážnik ľutuje - kiežby bol otočil kameru k obzoru o minútu skôr.
  annotator alt: {"2955": {"guard": ["security guard", "watchman"], "towards": ["toward", "to", "at"], "a minute earlier": ["a minute sooner"]}}
- {"id": "ng1c_88", "pos": "n", "m": ["towards", "toward", "to", "at"], "anchor": "towards"}
  sentence(s): 2955 [L B2] EN: The guard wishes he had turned the camera towards the horizon a minute earlier. | SK: Strážnik ľutuje - kiežby bol otočil kameru k obzoru o minútu skôr.
  annotator alt: {"2955": {"guard": ["security guard", "watchman"], "towards": ["toward", "to", "at"], "a minute earlier": ["a minute sooner"]}}
- {"id": "ng1c_89", "pos": "x", "m": ["a minute earlier", "a minute sooner"], "anchor": "a minute earlier"}
  sentence(s): 2955 [L B2] EN: The guard wishes he had turned the camera towards the horizon a minute earlier. | SK: Strážnik ľutuje - kiežby bol otočil kameru k obzoru o minútu skôr.
  annotator alt: {"2955": {"guard": ["security guard", "watchman"], "towards": ["toward", "to", "at"], "a minute earlier": ["a minute sooner"]}}
- {"id": "ng1c_90", "pos": "x", "m": ["days ago", "a few days ago", "several days ago"], "anchor": "days ago"}
  sentence(s): 2874 [L B2] EN: He should have seen a doctor days ago, but he waited until he could hardly stand. | SK: Mal ísť k lekárovi už pred pár dňami, ale čakal, kým sa sotva udržal na nohách.
  annotator alt: {"2874": {"days ago": ["a few days ago", "several days ago"], "hardly": ["barely", "scarcely"], "stand": ["stand up", "stay on his feet", "keep on his feet"]}}
- {"id": "ng1c_91", "pos": "x", "m": ["stand", "stand up", "stay on his feet", "keep on his feet"], "anchor": "stand"}
  nearest existing group: {"id": "pedestal_stand_base", "kind": "contextual", "pos": "n", "m": ["pedestal", "stand", "base"], "ok": "Their old globe has got a wooden stand. = Their old globe has got a wooden pedestal.", "bad": "The fans cheered from the stand. ≠ The fans cheered from the pedestal."}
  sentence(s): 2874 [L B2] EN: He should have seen a doctor days ago, but he waited until he could hardly stand. | SK: Mal ísť k lekárovi už pred pár dňami, ale čakal, kým sa sotva udržal na nohách.
  annotator alt: {"2874": {"days ago": ["a few days ago", "several days ago"], "hardly": ["barely", "scarcely"], "stand": ["stand up", "stay on his feet", "keep on his feet"]}}
- {"id": "ng1c_92", "pos": "n", "m": ["diploma", "degree"], "anchor": "diploma"}
  sentence(s): 103 [L B2] EN: He was handed his diploma in front of the whole stadium, and the confetti came down. | SK: O jeho promócii sa hovorí, že bola najhlučnejšia v histórii univerzity.
  annotator alt: {"103": {"diploma": ["degree"], "whole": ["entire"], "came down": ["fell", "rained down"]}}
- {"id": "ng1c_93", "pos": "x", "m": ["came down", "fell", "rained down"], "anchor": "came down"}
  sentence(s): 103 [L B2] EN: He was handed his diploma in front of the whole stadium, and the confetti came down. | SK: O jeho promócii sa hovorí, že bola najhlučnejšia v histórii univerzity.
  annotator alt: {"103": {"diploma": ["degree"], "whole": ["entire"], "came down": ["fell", "rained down"]}}
- {"id": "ng1c_94", "pos": "x", "m": ["a fifth", "her fifth", "the fifth"], "anchor": "a fifth"}
  sentence(s): 8209 [L B2] EN: By Friday she will have booked a fifth appointment at the studio. | SK: Do piatku si zarezervuje piaty termín v štúdiu.
  annotator alt: {"8209": {"a fifth": ["her fifth", "the fifth"], "appointment": ["session", "slot"]}}
- {"id": "ng1c_95", "pos": "n", "m": ["leaves", "foliage"], "anchor": "leaves"}
  nearest existing group: {"id": "forget_leave", "kind": "contextual", "pos": "v", "m": ["forget", "leave"], "ok": "I forgot my keys at home. = I left my keys at home.", "bad": "I forgot his name. ≠ I left his name."}
  sentence(s): 7037 [L B2] EN: The stag, whose antlers were huge, stood among the leaves. | SK: Jeleň, ktorého parohy boli obrovské, stál medzi lístím.
  annotator alt: {"7037": {"stag": ["deer"], "huge": ["enormous", "massive"], "leaves": ["foliage"]}}
- {"id": "ng1c_96", "pos": "n", "m": ["ice pack", "cold pack", "compress", "cold compress"], "anchor": "ice pack"}
  nearest existing group: {"id": "compress_ice_pack", "kind": "contextual", "pos": "n", "m": ["ice pack", "cold compress", "compress"], "ok": "She is pressing a blue ice pack on the bump. = She is pressing a blue cold compress on the bump.", "bad": "Put the ice pack in the software to shrink the file. ≠ Put the compress in the software to shrink the file."}
  sentence(s): 10013 [L B2] EN: Right now he is holding a blue ice pack against the lump. | SK: Práve teraz tlačí modrý obklad na hrču.
  annotator alt: {"10013": {"ice pack": ["cold pack", "compress", "cold compress"], "against": ["on", "to"], "lump": ["bump"]}}
- {"id": "ng1c_97", "pos": "x", "m": ["ten", "ten o'clock"], "anchor": "ten"}
  sentence(s): 10366 [L B2] EN: By ten he will have been reheating noodles for two hours straight. | SK: Do desiatej už bude zohrievať rezance dve hodiny v kuse.
  annotator alt: {"10366": {"ten": ["ten o'clock", "10"], "noodles": ["the noodles"], "straight": ["in a row", "non-stop"]}}
- {"id": "ng1c_98", "pos": "x", "m": ["noodles", "the noodles"], "anchor": "noodles"}
  sentence(s): 10366 [L B2] EN: By ten he will have been reheating noodles for two hours straight. | SK: Do desiatej už bude zohrievať rezance dve hodiny v kuse.
  annotator alt: {"10366": {"ten": ["ten o'clock", "10"], "noodles": ["the noodles"], "straight": ["in a row", "non-stop"]}}
- {"id": "ng1c_99", "pos": "x", "m": ["straight", "in a row", "non-stop"], "anchor": "straight"}
  nearest existing group: {"id": "in_a_row", "kind": "contextual", "pos": "x", "m": ["in a row", "straight", "running"], "ok": "Three days in a row = Three days running", "bad": "Put them in a row. ≠ Put them running."}
  sentence(s): 10366 [L B2] EN: By ten he will have been reheating noodles for two hours straight. | SK: Do desiatej už bude zohrievať rezance dve hodiny v kuse.
  annotator alt: {"10366": {"ten": ["ten o'clock", "10"], "noodles": ["the noodles"], "straight": ["in a row", "non-stop"]}}

Write the JSON to `phase1c/review/syn_1.json` now. "unchanged" counts groups left as they are.

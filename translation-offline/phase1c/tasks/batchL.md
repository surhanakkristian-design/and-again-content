# Task: annotate batch L (60 sentences) — Phase 1c

Budget: ONE read (this file, already done) and ONE write. Do not open any other file, do not search, do not run code.
Write `/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase1c/annotated/batchL.json`: a JSON array, one compact object per line, one per sentence below, same order. Nothing else.

## What an annotation is
For each English reference sentence (`en`, a translation of the Slovak `sk`), describe every English sentence a learner may
correctly write for `sk`, compactly. The checker matches patterns; it never expands rows.

## Output schema (omit a key when empty; all anchors case-insensitive whole words/phrases)
```
{"id":10860,"t":44,"lv":"B1",
 "v":["The officer who stamped his passport barely raised her eyes.","The officer that stamped his passport barely raised her eyes."],
 "lk":["who stamped","that stamped"],
 "alt":{"raised":["lifted"],"barely":["hardly","scarcely"],"stamped":["checked"]},
 "g":[["his"],["her"]],
 "o":{},
 "d":{"The":"A"},
 "p":["+even","-barely"],
 "m":[["44.01","which stamped"],["44.03","who he stamped"],["44.07","stamped","who stamped"]]}
```
- `id`,`t`,`lv`: copy from the input.
- `v` — `v[0]` = `en` EXACTLY. At most 3 more variants, each STRUCTURALLY different (another construction or word order a
  learner would write for `sk`: when/if, passive/active, "would already be"/"would be … by now", relative clause with/without
  pronoun, reported-speech alternatives…). NEVER a variant that differs only by a word swap, article, pronoun or optional word —
  those go in alt/d/g/o/p.
- `lk` — the LOCKED span per variant (same order as `v`): the practised grammar = the exercise answer `ans` located in that
  variant (and its counterpart in the other variants). Must occur verbatim in the variant. Discontinuous: pieces joined with
  ` .. ` ("would .. have been"). Nothing inside a lock may vary.
- Anchors (keys of alt/o/d, entries of g, `-` entries of p, 3rd element of m): a word or phrase that occurs in the variants,
  written exactly as there; `word#2` = its second occurrence. An anchor applies in every variant containing it. An anchor must
  NEVER lie inside a locked span.
- `alt` — THE MAIN JOB. For EVERY content word or phrase outside the lock that a learner could plausibly render differently
  from `sk` (nouns, verbs, adjectives, adverbs, phrasal verbs, set phrases), list the alternatives a learner would really write,
  as SHORT FREE TEXT, in the SAME grammatical form as the anchor so each can replace it in place ("dropped" → ["lowered","reduced"],
  "spines" → ["thorns"], "grin" → ["smirk"], "cancelled" → ["called off"], "whole" → ["entire"], "muddy" → ["covered in mud"]).
  Same meaning in THIS sentence only. Think of the Slovak word and every common English rendering of it. A phrase may replace a
  word and vice versa. Be generous with real everyday alternatives, strict about meaning: nothing that changes the meaning
  (drop ≠ lower when it means letting fall; interrupt ≠ cancel). Do not list pure BrE/AmE spelling variants (colour/color,
  cancelled/canceled — handled automatically), nor someone/somebody-type pairs. Words inside the lock are never keys.
- `g` — gender chains: each inner list = anchors that switch masculine↔feminine together (he↔she, him↔her, his↔her,
  himself↔herself). ONLY when `sk` does NOT fix the gender (no pronoun, verb form not gendered, e.g. "tlačí", "premenila" IS
  gendered → fixed). Omit when fixed. Put pronouns that must flip together in ONE chain.
- `o` — single pronoun alternatives: anchor → "her|it" (sk "ju", thing or person), "him|it" (sk "ho"), "them|it".
- `d` — determiner freedom where `sk` has no demonstrative/possessive for that noun: anchor → `A` (the|a/an|this|that),
  `P` (plural: the|these|those|∅), `Z` (the|∅) or an explicit list "the|her|his". Anchor = the determiner itself ("The"), or
  the bare noun when the reference has none (a determiner may then be inserted before it).
- `p` — small meaning-neutral optional words: `+w` may be inserted anywhere outside the lock (at most once), `+w@anchor` only
  right after anchor, `-anchor` may be dropped. Multi-word allowed ("+of them", "-for"). Only words like already, just, even,
  ever, really, up, of them, at all, for, then, so, right, now.
- `m` — 3–8 library mistakes from the LIBRARY INDEX below (only this sentence's topic `t`) that a learner of this sentence
  would plausibly make, with the concrete wrong text: `[libId, wrongText]` replaces the locked span in every variant;
  `[libId, wrongText, anchor]` replaces the anchor text instead; optional 4th element `{"slot":"value"}` for every extra slot
  listed after `slots:` in the index (e.g. `{"base":"stamp"}`). `[libId, "=full wrong sentence"]` when a replacement cannot
  express it. `[tip]` items are correct-but-not-practised (verdict correct_with_tip); `[wrong]` items are errors. The wrong
  text must really be wrong for the item's kind (never a correct sentence under a [wrong] item).
- Be terse; do not deliberate at length per sentence. Output only the file.

## Sentences (one JSON object per line; `long` = 13–16-word sentence)
{"id": 14266, "t": 9, "topic": "Wh- questions", "lv": "A1", "long": false, "en": "What do they dance? — Salsa.", "ans": "What", "sk": "Čo tancujú? — Salsu."}
{"id": 27628, "t": 10, "topic": "Prepositions of place/time", "lv": "A1", "long": false, "en": "The children awake at seven in the morning.", "ans": "at", "sk": "Deti sa zobudia o siedmej ráno."}
{"id": 20435, "t": 1, "topic": "TO BE", "lv": "A1", "long": false, "en": "The big plate is white and very clean.", "ans": "is", "sk": "Ten veľký tanier je biely a úplne čistý."}
{"id": 32342, "t": 1, "topic": "TO BE", "lv": "A1", "long": false, "en": "The evidence is on the cork board.", "ans": "is", "sk": "Dôkaz je na korkovej tabuli."}
{"id": 24741, "t": 1, "topic": "TO BE", "lv": "A1", "long": false, "en": "The rowing team is fast and very strong.", "ans": "is", "sk": "Veslársky tím je rýchly a veľmi silný."}
{"id": 20298, "t": 6, "topic": "A, AN, THE", "lv": "A1", "long": false, "en": "He needs a pill for his bad headache.", "ans": "a pill", "sk": "Na tú silnú bolesť hlavy potrebuje jednu tabletku."}
{"id": 25981, "t": 11, "topic": "Cardinal numbers", "lv": "A1", "long": false, "en": "The waiter carries ten hot plates at once.", "ans": "ten", "sk": "Čašník nesie naraz desať horúcich tanierov."}
{"id": 26084, "t": 4, "topic": "Modal verb CAN", "lv": "A1", "long": false, "en": "He can find her before she gets home.", "ans": "can", "sk": "Dokáže ju nájsť skôr, než príde domov."}
{"id": 23669, "t": 10, "topic": "Prepositions of place/time", "lv": "A1", "long": false, "en": "The galaxy moves slowly above their heads.", "ans": "above", "sk": "Galaxia sa pomaly pohybuje nad ich hlavami."}
{"id": 13034, "t": 14, "topic": "Present Continuous", "lv": "A2", "long": false, "en": "Right now the girl is blowing out the candles.", "ans": "is blowing", "sk": "Práve teraz dievča sfukuje sviečky."}
{"id": 14806, "t": 12, "topic": "Past Simple", "lv": "A2", "long": false, "en": "A moment ago she stopped the globe with her hand.", "ans": "stopped", "sk": "Pred chvíľou zastavila glóbus rukou."}
{"id": 24733, "t": 23, "topic": "Must, Have to...", "lv": "A2", "long": false, "en": "The glass is hot, so you must hold it carefully.", "ans": "must", "sk": "Pohárik je horúci, tak ho musíš držať opatrne."}
{"id": 11348, "t": 14, "topic": "Present Continuous", "lv": "A2", "long": false, "en": "Look! The assistant is holding the reflector up now.", "ans": "is holding", "sk": "Pozri! Asistent práve drží odrazovú dosku hore."}
{"id": 21124, "t": 15, "topic": "Present Continuous or Simple", "lv": "A2", "long": false, "en": "She usually stays dry, but today she is dancing in the rain.", "ans": "is dancing", "sk": "Zvyčajne ostáva pod strechou, ale dnes tancuje v daždi."}
{"id": 20702, "t": 14, "topic": "Present Continuous", "lv": "A2", "long": false, "en": "Look! He is lifting the jug higher and higher now.", "ans": "is lifting", "sk": "Pozri! Teraz dvíha džbán vyššie a vyššie."}
{"id": 11980, "t": 16, "topic": "Future with WILL", "lv": "A2", "long": false, "en": "Wait a minute and the water will boil!", "ans": "will", "sk": "Počkaj chvíľu a voda zovrie!"}
{"id": 11216, "t": 24, "topic": "Modal verb SHOULD", "lv": "A2", "long": false, "en": "If you hate the answer, you should not ask the cards.", "ans": "should", "sk": "Ak sa ti odpoveď nepáči, nemal by si sa kariet pýtať."}
{"id": 13395, "t": 13, "topic": "Present or Past Simple", "lv": "A2", "long": false, "en": "She usually draws hearts, but today she drew a circle.", "ans": "drew", "sk": "Zvyčajne kreslí srdcia, ale dnes nakreslila kruh."}
{"id": 16009, "t": 15, "topic": "Present Continuous or Simple", "lv": "A2", "long": false, "en": "It usually sits still, but now it is croaking loudly.", "ans": "is croaking", "sk": "Zvyčajne sedí ticho, ale teraz hlasno kváka"}
{"id": 18966, "t": 21, "topic": "There is, are", "lv": "A2", "long": false, "en": "There are two people in the empty meadow.", "ans": "are", "sk": "Na prázdnej lúke sú dvaja ľudia."}
{"id": 21467, "t": 24, "topic": "Modal verb SHOULD", "lv": "A2", "long": false, "en": "The water is cold, so you should wear boots.", "ans": "should", "sk": "Voda je studená, mal by si si obuť čižmy."}
{"id": 3084, "t": 33, "topic": "Past Simple or Continuos", "lv": "B1", "long": true, "en": "The moment her friend made her laugh, her hand slipped and the line went crooked.", "ans": "slipped", "sk": "V momente, keď ju kamarátka rozosmiala, jej ruka sa šmykla a čiara išla nakrivo."}
{"id": 4449, "t": 33, "topic": "Past Simple or Continuos", "lv": "B1", "long": true, "en": "Altogether she lowered the basket three times before the man had all his oranges.", "ans": "lowered", "sk": "Celkovo spustila kôš trikrát, kým mal muž všetky svoje pomaranče."}
{"id": 1452, "t": 39, "topic": "1. Conditional", "lv": "B1", "long": true, "en": "If he touches that cactus, he will spend the evening pulling spines out of his finger.", "ans": "touches", "sk": "Ak sa dotkne toho kaktusa, strávi večer vyťahovaním tŕňov z prsta."}
{"id": 5595, "t": 34, "topic": "Present Perfect Simple or Continuos", "lv": "B1", "long": true, "en": "He has stamped the document at last, so she can finally go home.", "ans": "has stamped", "sk": "Konečne dokument opečiatkoval, takže môže ísť domov."}
{"id": 9244, "t": 33, "topic": "Past Simple or Continuos", "lv": "B1", "long": true, "en": "While the waves were rolling in, the black cat did not move a whisker.", "ans": "were rolling", "sk": "Kým sa vlny valili, čierna mačka nepohla ani fúzom."}
{"id": 6365, "t": 45, "topic": "Reported speech", "lv": "B1", "long": false, "en": "The director said they would film the office scene before lunch.", "ans": "would film", "sk": "Režisér povedal, že kancelársku scénu natočia pred obedom."}
{"id": 4571, "t": 38, "topic": "0 Conditional", "lv": "B1", "long": false, "en": "If you leave one screw loose, the whole chair wobbles.", "ans": "leave", "sk": "Keď necháš jednu skrutku uvoľnenú, celá stolička sa kýve."}
{"id": 7458, "t": 48, "topic": "Question tags", "lv": "B1", "long": false, "en": "Everyone makes that face, don't they?", "ans": "don't they", "sk": "Tú grimasu robí každý, však?"}
{"id": 7238, "t": 38, "topic": "0 Conditional", "lv": "B1", "long": false, "en": "If you step exactly where Mira steps, your feet stay completely dry.", "ans": "step", "sk": "Ak stúpaš presne tam, kam stúpa Mira, nohy ti zostanú úplne suché."}
{"id": 9498, "t": 44, "topic": "Relative clauses", "lv": "B1", "long": false, "en": "The podium that she is standing behind is older than the school.", "ans": "that", "sk": "Pult, za ktorým stojí, je starší než celá škola."}
{"id": 9495, "t": 41, "topic": "Passive", "lv": "B1", "long": false, "en": "Her speech was rewritten twice before she ever walked onto that stage.", "ans": "was rewritten", "sk": "Jej prejav bol prepísaný dvakrát, ešte než vôbec vyšla na to pódium."}
{"id": 8824, "t": 33, "topic": "Past Simple or Continuos", "lv": "B1", "long": false, "en": "While the chain was swinging, he pushed the bag into place.", "ans": "was swinging", "sk": "Kým sa reťaz kývala, dotlačil vrece na miesto."}
{"id": 2929, "t": 34, "topic": "Present Perfect Simple or Continuos", "lv": "B1", "long": false, "en": "The eerie light has faded completely, and the yard is dark again.", "ans": "has faded", "sk": "Desivé svetlo úplne zhaslo a nádražie je zase tmavé."}
{"id": 6830, "t": 46, "topic": "Used to, Would", "lv": "B1", "long": false, "en": "As kids they would buy dried herbs in a jar.", "ans": "would", "sk": "Ako deti kupovali sušené bylinky v pohári."}
{"id": 8017, "t": 31, "topic": "Past Continuous", "lv": "B1", "long": false, "en": "The keeper was standing on his line when the referee pointed to the spot.", "ans": "was standing", "sk": "Brankár práve stál na čiare, keď rozhodca ukázal na biely bod."}
{"id": 119, "t": 32, "topic": "Present Perfect Continuous", "lv": "B1", "long": false, "en": "How long has she been tapping that keycard on the wrong door?", "ans": "has she been tapping", "sk": "Ako dlho prikladá tou kartou na nesprávne dvere?"}
{"id": 5959, "t": 39, "topic": "1. Conditional", "lv": "B1", "long": false, "en": "If he turns the ring once more, she will drop the price again.", "ans": "will drop", "sk": "Ak prsteň otočí ešte raz, zníži cenu znova."}
{"id": 8920, "t": 41, "topic": "Passive", "lv": "B1", "long": false, "en": "The fastest sequence is shown in slow motion at the end.", "ans": "is shown", "sk": "Najrýchlejšia akcia je ukázaná na konci v spomalenom zábere."}
{"id": 8062, "t": 33, "topic": "Past Simple or Continuos", "lv": "B1", "long": false, "en": "She moved to the drum kit while the camera was still rolling.", "ans": "moved", "sk": "K bicím prešla, kým kamera ešte bežala."}
{"id": 10167, "t": 43, "topic": "Modal verbs Probability", "lv": "B1", "long": false, "en": "His mouth is that dry, so the thirst must be real.", "ans": "must", "sk": "Ústa má také suché, že smäd musí byť skutočný."}
{"id": 8293, "t": 43, "topic": "Modal verbs Probability", "lv": "B1", "long": false, "en": "She never shares food, so this one must be special.", "ans": "must", "sk": "Jedlo nikdy nedelí, takže tento croissant musí byť výnimočný."}
{"id": 3494, "t": 53, "topic": "3. Conditional", "lv": "B2", "long": true, "en": "If the ball had landed in black, she would have gone home with empty pockets.", "ans": "had landed", "sk": "Keby bola guľôčka padla na čiernej, išla by domov s prázdnymi vreckami."}
{"id": 2955, "t": 60, "topic": "Wish clauses", "lv": "B2", "long": true, "en": "The guard wishes he had turned the camera towards the horizon a minute earlier.", "ans": "had turned", "sk": "Strážnik ľutuje - kiežby bol otočil kameru k obzoru o minútu skôr."}
{"id": 2874, "t": 57, "topic": "Modals in past", "lv": "B2", "long": true, "en": "He should have seen a doctor days ago, but he waited until he could hardly stand.", "ans": "should have seen", "sk": "Mal ísť k lekárovi už pred pár dňami, ale čakal, kým sa sotva udržal na nohách."}
{"id": 103, "t": 55, "topic": "Advanced Passive Voice", "lv": "B2", "long": true, "en": "He was handed his diploma in front of the whole stadium, and the confetti came down.", "ans": "was handed", "sk": "O jeho promócii sa hovorí, že bola najhlučnejšia v histórii univerzity."}
{"id": 8812, "t": 60, "topic": "Wish clauses", "lv": "B2", "long": false, "en": "Her trainer wishes his pads were a bit thicker.", "ans": "were", "sk": "Tréner by si prial, aby jeho lapy boli trochu hrubšie."}
{"id": 8209, "t": 51, "topic": "Future Perfect Simple", "lv": "B2", "long": false, "en": "By Friday she will have booked a fifth appointment at the studio.", "ans": "will have booked", "sk": "Do piatku si zarezervuje piaty termín v štúdiu."}
{"id": 7037, "t": 61, "topic": "Relative clauses", "lv": "B2", "long": false, "en": "The stag, whose antlers were huge, stood among the leaves.", "ans": "whose", "sk": "Jeleň, ktorého parohy boli obrovské, stál medzi lístím."}
{"id": 10013, "t": 65, "topic": "All Present Tenses", "lv": "B2", "long": false, "en": "Right now he is holding a blue ice pack against the lump.", "ans": "is holding", "sk": "Práve teraz tlačí modrý obklad na hrču."}
{"id": 10366, "t": 52, "topic": "Future Perfect Continuous", "lv": "B2", "long": false, "en": "By ten he will have been reheating noodles for two hours straight.", "ans": "will have been reheating", "sk": "Do desiatej už bude zohrievať rezance dve hodiny v kuse."}
{"id": 10866, "t": 50, "topic": "Past Perfect Continuous", "lv": "B2", "long": false, "en": "He had been waiting for two hours before his number finally appeared.", "ans": "had been waiting", "sk": "Čakal dve hodiny, kým sa konečne objavilo jeho číslo."}
{"id": 3937, "t": 67, "topic": "All Future Tenses", "lv": "B2", "long": false, "en": "She will buy another charm when she comes to this market again.", "ans": "comes", "sk": "Kúpi si ďalší prívesok, keď príde na tento trh znova."}
{"id": 7998, "t": 61, "topic": "Relative clauses", "lv": "B2", "long": false, "en": "The veranda, where she now spends every morning, faces the sunrise.", "ans": "where", "sk": "Veranda, na ktorej teraz trávi každé ráno, je otočená na východ slnka."}
{"id": 10574, "t": 50, "topic": "Past Perfect Continuous", "lv": "B2", "long": false, "en": "He had been training for hours before the light was finally right.", "ans": "had been training", "sk": "Trénoval hodiny, kým bolo svetlo konečne správne."}
{"id": 9038, "t": 65, "topic": "All Present Tenses", "lv": "B2", "long": false, "en": "Right now he is scribbling a note while the laptop screen glows.", "ans": "is scribbling", "sk": "Práve teraz čmára poznámku, kým obrazovka notebooku svieti."}
{"id": 10107, "t": 63, "topic": "Advanced linkers", "lv": "B2", "long": false, "en": "The terminal was empty; even so, she felt watched.", "ans": "even so", "sk": "Terminál bol prázdny; aj tak mala pocit, že ju niekto sleduje."}
{"id": 9913, "t": 59, "topic": "Causative HAVE/GET", "lv": "B2", "long": false, "en": "She had her boots dyed purple last summer.", "ans": "had", "sk": "Vlani si dala čižmy zafarbiť na fialovo."}
{"id": 9966, "t": 65, "topic": "All Present Tenses", "lv": "B2", "long": false, "en": "Right now they are shaking hands on the sunny rooftop.", "ans": "are shaking", "sk": "Práve teraz si na slnečnej streche podávajú ruky."}
{"id": 6884, "t": 53, "topic": "3. Conditional", "lv": "B2", "long": false, "en": "If he had started earlier, he would have missed the mist.", "ans": "had started", "sk": "Keby vyrazil skôr, hmlu by bol minul."}

## LIBRARY INDEX (topics of this batch only): id [wrong|tip] pattern (slots: extra slots to fill)
## 1 TO BE
1.01 [wrong] drop am/is/are (SK/CZ-like verbless sentence)
1.02 [wrong] is/was with a plural subject
1.03 [wrong] are/were with a singular or uncountable subject
1.04 [wrong] is/are after I instead of am
1.05 [wrong] is/am after you instead of are
1.06 [wrong] be instead of am/is/are
1.07 [wrong] move is/are to the end or after the adverb (The carrot is in the bed big)
1.08 [wrong] statement order with a question mark (You are tired?)
1.09 [wrong] invert subject and be in a statement (Is the plate white.)
1.10 [wrong] don't/doesn't with be (He doesn't be, I don't am)
1.11 [wrong] not in front of am/is/are (He not is)
1.12 [wrong] have/has (got) + years for age (calque of mať rokov)
1.13 [wrong] have + noun for a state expressed with be (I have cold, She has hunger)
1.14 [wrong] drop the dummy subject it (Is cold today)
1.15 [wrong] add -s to evidence, information, advice, money, furniture
1.16 [wrong] much before a plain adjective (much strong)
1.17 [wrong] drop a/an/the before a noun
1.18 [wrong] singular noun where the plural is needed (after two, many)
1.19 [wrong] replace the preposition with a typical SK/CZ calque (in/on/at/to/for)
1.20 [wrong] a different word whose meaning does not fit (carry for wear, listen for hear)
## 4 Modal verb CAN
4.01 [wrong] insert to after can/must/should/will
4.02 [wrong] verb with -s after can (can finds)
4.03 [wrong] verb with -ing after can (can swimming)
4.04 [wrong] can with -s after he/she/it (She cans)
4.05 [wrong] Do/Does + can in a question (Do you can…?)
4.06 [wrong] statement order with a question mark (You can help me?)
4.07 [wrong] Can you… where the sentence is a statement
4.08 [wrong] don't/doesn't + can (I don't can)
4.09 [wrong] not in front of can (She not can)
4.10 [tip] is able to / are able to instead of can
4.11 [tip] could in a polite request or present ability
4.12 [wrong] will can for future ability
4.13 [wrong] know/knows (to) + verb for ability (calque of vie plávať)
4.14 [wrong] object pronoun right after the verb for mi/me (hold me the nail)
4.15 [wrong] put will into an if/when/before/until clause
4.16 [wrong] drop -s/-es from a he/she/it verb
4.17 [tip] understandable but unusual order (time phrase in the middle)
4.18 [wrong] a different word whose meaning does not fit (carry for wear, listen for hear)
4.19 [wrong] replace the preposition with a typical SK/CZ calque (in/on/at/to/for)
4.20 [wrong] drop a/an/the before a noun
## 6 A, AN, THE
6.01 [wrong] drop a/an before a singular countable noun
6.02 [wrong] drop the before a known or specific noun
6.03 [wrong] a before a vowel sound or an before a consonant sound
6.04 [wrong] a/an where the thing is specific or already known
6.05 [wrong] the where the thing is mentioned for the first time
6.06 [wrong] a/an before a plural noun (a books)
6.07 [wrong] a/an before an uncountable noun (a sugar, a water)
6.08 [wrong] the before a plural or uncountable noun meant in general (I like the cats)
6.09 [wrong] play the football, have the breakfast, speak the English
6.10 [wrong] sun, moon, sky, world without the
6.11 [wrong] She is doctor / He works as teacher
6.12 [wrong] the before a person's name or most countries/cities
6.13 [tip] one where plain a/an is meant
6.14 [wrong] the/a together with my/his/her (the my bag)
6.15 [wrong] the instead of my/his/her/its before a body part
6.16 [wrong] drop -s/-es from a he/she/it verb
6.17 [wrong] subject form instead of object form or vice versa (he/him, she/her)
6.18 [tip] grammatical, same meaning, but a clumsy calque (strong headache, on the meadow)
6.19 [wrong] replace the preposition with a typical SK/CZ calque (in/on/at/to/for)
6.20 [wrong] a different word whose meaning does not fit (carry for wear, listen for hear)
## 9 Wh- questions
9.01 [wrong] question word + subject + verb with no do/does (Why they wait?)
9.02 [wrong] does with I/you/we/they
9.03 [wrong] do with he/she/it
9.04 [wrong] verb with -s or -ing after do/does (do they falls, does she sleeping)
9.05 [wrong] question word + verb + subject (Where fall they?)
9.06 [wrong] be at the end of a question (Where her card is?)
9.07 [wrong] drop is/are in a be-question (Where her card?)
9.08 [wrong] what/where/how/who/when swapped
9.09 [wrong] Who does live… / What does happen… when asking about the subject
9.10 [wrong] how much with a plural noun or how many with an uncountable one
9.11 [wrong] who/who's where whose (owner) is asked
9.12 [wrong] How many years has/is… for How old
9.13 [tip] About what… / With who… instead of the preposition at the end
9.14 [wrong] did/was in a present question
9.15 [wrong] insert to after can/must/should/will
9.16 [wrong] an SK/CZ look-alike word (automat, reklama, control)
9.17 [wrong] replace the preposition with a typical SK/CZ calque (in/on/at/to/for)
9.18 [wrong] a different word whose meaning does not fit (carry for wear, listen for hear)
9.19 [wrong] drop a/an/the before a noun
## 10 Prepositions of place/time
10.01 [wrong] in/on + clock time (in seven)
10.02 [wrong] in/at + day or date (in Monday, at 5 May)
10.03 [wrong] on/at + month, year or season (on June)
10.04 [wrong] at the morning / in the night / on the evening
10.05 [wrong] in for something lying on a surface (in the table, in a bench)
10.06 [wrong] on for something inside (on the box, on the bay)
10.07 [wrong] on/in for at a point or place (on the door, in the bus stop)
10.08 [wrong] in/to for movement into something
10.09 [wrong] on for something above and not touching (on their heads)
10.10 [wrong] under/above, in front of/behind swapped
10.11 [wrong] drop part of a two-word preposition (next the, in front the)
10.12 [wrong] at London / at Slovakia
10.13 [wrong] after an hour for in an hour (from now)
10.14 [wrong] calque před/pred + time instead of … ago
10.15 [wrong] insert a preposition English does not use (go to home, enter into)
10.16 [wrong] drop a/an/the before a noun
10.17 [wrong] translate sa/se as himself/herself/itself/you
10.18 [wrong] drop -s/-es from a he/she/it verb
10.19 [wrong] add -s to people/children/men/women
10.20 [wrong] keep SK/CZ word order (object first, verb after the place phrase)
10.21 [wrong] a different word whose meaning does not fit (carry for wear, listen for hear)
## 11 Cardinal numbers
11.01 [wrong] noun without -s after two, ten, twenty…
11.02 [wrong] one + plural noun
11.03 [wrong] tenth/third for ten/three
11.04 [wrong] three/ten for third/tenth
11.05 [wrong] two hundreds, three thousands, five millions
11.06 [wrong] fifteen/fifty, thirteen/thirty swapped
11.07 [wrong] fourty, nineth, twelf, fivety
11.08 [wrong] hundred people without a/one
11.09 [wrong] five of apples, ten of people
11.10 [wrong] 2,5 for 2.5
11.11 [wrong] is/was with a plural subject
11.12 [wrong] have/has (got) + years for age (calque of mať rokov)
11.13 [wrong] add -s to an adjective before a plural noun (olds books)
11.14 [wrong] drop -s/-es from a he/she/it verb
11.15 [tip] understandable but unusual order (time phrase in the middle)
11.16 [wrong] drop a/an/the before a noun
11.17 [wrong] replace the preposition with a typical SK/CZ calque (in/on/at/to/for)
11.18 [tip] persons after a number
11.19 [wrong] a different word whose meaning does not fit (carry for wear, listen for hear)
## 12 Past Simple
12.01 [wrong] present form for a finished past action (yesterday, ago, last…)
12.02 [wrong] has/have + past participle with yesterday/ago/last…
12.03 [wrong] base form instead of the past form
12.04 [wrong] buyed, leaved, drawed, teached
12.05 [wrong] seen, done, gone, drunk used alone as the past
12.06 [wrong] stoped, studyed, plaied, planed
12.07 [wrong] were with I/he/she/it or was with you/we/they
12.08 [wrong] did/didn't + past form (didn't went, did she saw)
12.09 [wrong] not/no + past verb (She not went, He no stopped)
12.10 [wrong] statement order with a question mark in the past (You saw it?)
12.11 [wrong] was/were + verb (was burned, was went) for the plain past
12.12 [tip] was/were + -ing for a simple finished action
12.13 [wrong] the second past verb left in the present
12.14 [wrong] had + past participle for a single past action
12.15 [wrong] calque před/pred + time instead of … ago
12.16 [wrong] an SK/CZ look-alike word (automat, reklama, control)
12.17 [wrong] keep SK/CZ word order (object first, verb after the place phrase)
12.18 [wrong] replace the preposition with a typical SK/CZ calque (in/on/at/to/for)
12.19 [wrong] drop a/an/the before a noun
12.20 [wrong] a different word whose meaning does not fit (carry for wear, listen for hear)
## 13 Present or Past Simple
13.01 [wrong] present form for a finished past action (yesterday, ago, last…)
13.02 [wrong] past form for something that still happens usually/always
13.03 [wrong] has/have + past participle with yesterday/ago/last…
13.04 [tip] has/have + past participle for a finished action today
13.05 [tip] was/were + -ing for a simple finished action
13.06 [wrong] is/are + -ing with usually/always/every…
13.07 [wrong] is/are + -ing for something already done
13.08 [wrong] drop -s/-es from a he/she/it verb
13.09 [wrong] base form instead of the past form
13.10 [wrong] buyed, leaved, drawed, teached
13.11 [wrong] seen, done, gone, drunk used alone as the past
13.12 [wrong] did/didn't + past form (didn't went, did she saw)
13.13 [wrong] does/doesn't in a past question or negative
13.14 [wrong] did/didn't in a present question or negative
13.15 [wrong] always/usually/often after the verb
13.16 [wrong] were with I/he/she/it or was with you/we/they
13.17 [wrong] stoped, studyed, plaied, planed
13.18 [wrong] drop a/an/the before a noun
13.19 [wrong] insert a preposition English does not use (go to home, enter into)
13.20 [wrong] a different word whose meaning does not fit (carry for wear, listen for hear)
## 14 Present Continuous
14.01 [wrong] Present Simple for an action happening now (Look!, now, right now)
14.02 [wrong] drop am/is/are before the -ing verb
14.03 [wrong] am/is/are + base verb (is hold)
14.04 [wrong] am/is/are not matching the subject (they is, he are)
14.05 [wrong] siting, makeing, lieing, runing
14.06 [wrong] was/were + -ing for an action happening now
14.07 [wrong] being + -ing, or is + -ing twice (is being lowering)
14.08 [wrong] don't/doesn't + -ing (She doesn't dancing)
14.09 [wrong] statement order with a question mark, or do + -ing (Does she sleeping?)
14.10 [wrong] am knowing, is liking, is wanting, are needing
14.11 [wrong] more + short adjective (more high, more big)
14.12 [wrong] drop a needed small word (of, out, on, it, to)
14.13 [wrong] the instead of my/his/her/its before a body part
14.14 [wrong] drop the subject pronoun (SK/CZ pro-drop)
14.15 [wrong] drop a/an/the before a noun
14.16 [wrong] replace the preposition with a typical SK/CZ calque (in/on/at/to/for)
14.17 [wrong] an SK/CZ look-alike word (automat, reklama, control)
14.18 [wrong] a different word whose meaning does not fit (carry for wear, listen for hear)
14.19 [tip] drop the where it is optional but more natural
## 15 Present Continuous or Simple
15.01 [wrong] Present Simple for today/now in contrast with a habit
15.02 [wrong] is/are + -ing with usually/always/every…
15.03 [wrong] past form for what is happening now/today
15.04 [wrong] drop -s/-es from a he/she/it verb
15.05 [wrong] drop am/is/are before the -ing verb
15.06 [wrong] am/is/are + base verb (is hold)
15.07 [wrong] am knowing, is liking, is wanting, are needing
15.08 [tip] Present Simple for a temporary situation (She lives with us this month)
15.09 [wrong] is/are + -ing for a permanent fact (The river is flowing into the sea)
15.10 [wrong] always/usually/often after the verb
15.11 [wrong] am/is/are not matching the subject (they is, he are)
15.12 [wrong] siting, makeing, lieing, runing
15.13 [wrong] don't/doesn't + -ing (She doesn't dancing)
15.14 [wrong] isn't + base verb for a habit (She isn't eat meat)
15.15 [wrong] translate sa/se as himself/herself/itself/you
15.16 [wrong] drop the subject pronoun (SK/CZ pro-drop)
15.17 [tip] adjective where the -ly adverb is needed (slow for slowly)
15.18 [wrong] drop a/an/the before a noun
15.19 [wrong] replace the preposition with a typical SK/CZ calque (in/on/at/to/for)
15.20 [wrong] a different word whose meaning does not fit (carry for wear, listen for hear)
## 16 Future with WILL
16.01 [tip] Present Simple for a future prediction or promise
16.02 [tip] be going to where the sentence practises will
16.03 [wrong] will + verb with -s
16.04 [wrong] insert to after can/must/should/will
16.05 [wrong] will + verb with -ing
16.06 [wrong] will + adjective/noun without be (will empty)
16.07 [wrong] will is / will are
16.08 [wrong] is/are for a future state (tomorrow)
16.09 [wrong] don't will / will don't / not will
16.10 [wrong] statement order with a question mark, or Do you will…?
16.11 [wrong] would for a plain future
16.12 [wrong] put will into an if/when/before/until clause
16.13 [wrong] after an hour for in an hour (from now)
16.14 [wrong] Not worry / No worry for Do not worry
16.15 [wrong] translate sa/se as himself/herself/itself/you
16.16 [wrong] a before a vowel sound or an before a consonant sound
16.17 [wrong] add a word English does not use here (shake their hands, return back)
16.18 [wrong] keep SK/CZ word order (object first, verb after the place phrase)
16.19 [wrong] drop a/an/the before a noun
16.20 [wrong] a different word whose meaning does not fit (carry for wear, listen for hear)
## 21 There is, are
21.01 [wrong] There are + a singular or uncountable noun (first noun decides)
21.02 [wrong] There is + a plural noun
21.03 [wrong] start with the place phrase and drop there (On the bench is a bag)
21.04 [tip] place phrase first with a full verb (On the bench lies a bandage)
21.05 [wrong] It is / It's for There is
21.06 [wrong] They are for There are
21.07 [wrong] There has / It has for There is (calque of má)
21.08 [wrong] There are no any / There isn't no
21.09 [wrong] There is …? with a question mark
21.10 [wrong] There + noun without is/are
21.11 [wrong] their/they're for there
21.12 [wrong] There was + plural or There were + singular
21.13 [wrong] singular noun where the plural is needed (after two, many)
21.14 [wrong] add -s to people/children/men/women
21.15 [tip] persons as the everyday plural
21.16 [wrong] replace the preposition with a typical SK/CZ calque (in/on/at/to/for)
21.17 [tip] grammatical, same meaning, but a clumsy calque (strong headache, on the meadow)
21.18 [wrong] drop a/an/the before a noun
21.19 [wrong] a different word whose meaning does not fit (carry for wear, listen for hear)
## 23 Must, Have to...
23.01 [wrong] insert to after can/must/should/will
23.02 [wrong] must + verb with -s
23.03 [wrong] must + verb with -ing
23.04 [wrong] should where the sentence says musieť/muset
23.05 [wrong] must for a past obligation (yesterday I must)
23.06 [wrong] have to after he/she/it
23.07 [wrong] have/has + verb without to
23.08 [wrong] mustn't where nemusieť/nemuset (no need) is meant, or the reverse
23.09 [wrong] don't must / not must
23.10 [wrong] Do I must…? / I must…?
23.11 [wrong] need + verb without to
23.12 [wrong] adjective where the -ly adverb is needed (slow for slowly)
23.13 [wrong] him/her for an object (SK/CZ grammatical gender)
23.14 [wrong] adverb between verb and object (hold carefully it)
23.15 [wrong] much before a plain adjective (much strong)
23.16 [wrong] a/an before an uncountable noun (a sugar, a water)
23.17 [wrong] replace the preposition with a typical SK/CZ calque (in/on/at/to/for)
23.18 [wrong] a different word whose meaning does not fit (carry for wear, listen for hear)
23.19 [wrong] drop a/an/the before a noun
## 24 Modal verb SHOULD
24.01 [wrong] insert to after can/must/should/will
24.02 [wrong] should + verb with -ing or -s
24.03 [wrong] must/have to where the sentence gives advice
24.04 [wrong] not should / don't should
24.05 [wrong] Do I should…? / I should…?
24.06 [wrong] would for advice (calque of mal by / měl by)
24.07 [tip] had better / ought to where the sentence practises should
24.08 [wrong] should + past form (should went)
24.09 [wrong] should + verb for something in the past (should buy yesterday)
24.10 [wrong] put will into an if/when/before/until clause
24.11 [wrong] the thing as subject for páčiť sa/líbit se (The answer does not like you)
24.12 [wrong] drop a needed small word (of, out, on, it, to)
24.13 [wrong] translate sa/se as himself/herself/itself/you
24.14 [wrong] drop -s/-es from a he/she/it verb
24.15 [wrong] him/her for an object (SK/CZ grammatical gender)
24.16 [wrong] drop a/an/the before a noun
24.17 [wrong] replace the preposition with a typical SK/CZ calque (in/on/at/to/for)
24.18 [wrong] a different word whose meaning does not fit (carry for wear, listen for hear)
## 31 Past Continuous
31.01 [wrong] Past Simple (tilted) for the longer action that was in progress when something happened
31.02 [tip] Past Simple of a position/state-like verb (stood, sat, lay, held) instead of was + -ing
31.03 [wrong] was/were + base verb without -ing (was tilt)
31.04 [wrong] -ing form without was/were (She tilting)
31.05 [wrong] was with a plural subject or you, were with a singular one (the lights was)
31.06 [wrong] was + past participle (was tilted) instead of was + -ing — turns it into Passive
31.07 [wrong] long background action in Past Simple and the short interrupting action in Past Continuous (use =full sentence)
31.08 [wrong] the short interrupting action also in Past Continuous (when the referee was pointing)
31.09 [wrong] am/is/are + -ing instead of was/were + -ing in a past story
31.10 [tip] had been + -ing instead of was/were + -ing (same moment, extra duration meaning)
31.11 [wrong] misspelt -ing form that is a spelling rule error (siting, lieing, makeing, stoping)
31.12 [wrong] while used before the short interrupting action instead of when (while the session started)
31.13 [wrong] Slovak/Czech reflexive verb (sa/se) turned into be + participle (was started, is opened)
31.14 [wrong] state verb (know, want, believe, own) put into was/were + -ing
31.15 [tip] still/already/always put before was/were (still was rolling)
31.16 [wrong] Present Simple in the when-clause of a past story (when the sun moves)
31.17 [wrong] -ed added to an irregular verb (striked, bursted, flied)
31.18 [wrong] was/were left after the subject in a question (What she was doing?)
31.19 [wrong] didn't + -ing or wasn't + base verb (didn't sleeping, wasn't sleep)
31.20 [wrong] article dropped before a singular countable noun (pillow for a pillow)
31.21 [wrong] wrong, extra or missing preposition copied from Slovak/Czech (struck into, on place)
## 32 Present Perfect Continuous
32.01 [wrong] Present Simple (sprints, does she tap) for an action going on since/for a time
32.02 [wrong] am/is/are + -ing with since/for/how long (is sprinting since)
32.03 [wrong] was/were + -ing for an action that still continues (was working since spring)
32.04 [tip] has + past participle (has worked) for a long action still in progress
32.05 [wrong] have/has + -ing without been (has sprinting)
32.06 [wrong] have/has been + base verb or past participle (has been work, has been worked)
32.07 [wrong] have with he/she/it or has with I/you/we/they
32.08 [wrong] is/was been + -ing instead of has been + -ing
32.09 [wrong] since with a length of time or for with a starting point (since two hours, for Monday)
32.10 [wrong] from used for the starting point (from the spring)
32.11 [wrong] Present Perfect in the since-clause (since the gun has gone off)
32.12 [wrong] How long + subject + has been (How long she has been tapping?)
32.13 [wrong] state verb (know, own, like) in have/has been + -ing
32.14 [wrong] ago added to the time phrase (for two years ago, since two years ago)
32.15 [wrong] didn't/isn't been + -ing instead of hasn't been + -ing
32.16 [tip] until now / till now added as a literal translation of doteraz (has been working until now)
32.17 [wrong] for long time / since long time without a (for a long time)
32.18 [wrong] phrase translated word for word from Slovak/Czech (today morning, this night, there where)
32.19 [wrong] article dropped before a singular countable noun (pillow for a pillow)
32.20 [wrong] wrong, extra or missing preposition copied from Slovak/Czech (struck into, on place)
## 33 Past Simple or Continuos
33.01 [wrong] was/were + -ing for a short completed action (was shouting, was pushing into place)
33.02 [wrong] Past Simple for the action in progress in the background (the lights still warmed up)
33.03 [tip] Past Simple for the longer action after while (while the chain swung)
33.04 [wrong] the interrupting action also in Past Continuous (someone was striking)
33.05 [wrong] long action in Past Simple, short one in Past Continuous (use =full sentence)
33.06 [wrong] Past Continuous for actions that happen one after another (the moment … were collapsing)
33.07 [wrong] was/were + -ing for a sudden action (suddenly/the moment … was bursting)
33.08 [wrong] Present Simple for a past event (when the director shouts)
33.09 [wrong] has/have + past participle for a finished event in a past story (has moved)
33.10 [wrong] had + past participle for the second of two consecutive actions (changes the order)
33.11 [wrong] was with a plural subject or were with a singular one (the lights was)
33.12 [wrong] -ing form without was/were (While the group settling)
33.13 [wrong] state verb (know, want, belong) in was/were + -ing
33.14 [tip] still/already put before was/were (still was rolling)
33.15 [wrong] during used before a clause instead of while (During the group was settling)
33.16 [wrong] -ed added to an irregular verb (striked, bursted, flied)
33.17 [wrong] past form kept after did/didn't (didn't saw, did she went)
33.18 [wrong] article dropped before a singular countable noun (pillow for a pillow)
33.19 [wrong] wrong, extra or missing preposition copied from Slovak/Czech (struck into, on place)
33.20 [wrong] phrase translated word for word from Slovak/Czech (today morning, this night, there where)
## 34 Present Perfect Simple or Continuos
34.01 [wrong] has been + -ing with a count of finished actions (has been scoring three penalties)
34.02 [wrong] has been + -ing for a completed result (has been fading completely)
34.03 [tip] has + past participle for a long activity still in progress (has worked all day)
34.04 [tip] Past Simple with this morning/today/this season/tonight (nudged … this morning)
34.05 [tip] Past Simple where the result is visible now (faded completely, and the yard is dark)
34.06 [wrong] Present Simple for a state/action lasting from the past until now (lives here since)
34.07 [wrong] have/has + base verb (has fade)
34.08 [wrong] have/has + Past Simple form of an irregular verb (has went, has took)
34.09 [wrong] -ed added to an irregular verb (striked, bursted, flied)
34.10 [wrong] is/are + past participle instead of has/have (is faded)
34.11 [wrong] have with he/she/it or has with I/you/we/they (She have scored)
34.12 [wrong] state verb (know, own, believe) in has been + -ing
34.13 [wrong] has been + adjective for a state described now (has been dark again)
34.14 [wrong] Present Simple for a change happening now (the pile still grows)
34.15 [wrong] yet used in a positive statement instead of already (has checked six sources yet)
34.16 [wrong] since with a length of time or for with a starting point
34.17 [wrong] adverb after look/feel/seem instead of an adjective (look hugely)
34.18 [wrong] second negative added (didn't … nothing, never doesn't, neither isn't)
34.19 [wrong] phrase translated word for word from Slovak/Czech (today morning, this night, there where)
34.20 [wrong] article dropped before a singular countable noun (pillow for a pillow)
## 38 0 Conditional
38.01 [tip] will + verb in the result of a general rule (the chair will wobble)
38.02 [wrong] will added in the if-clause (If you will leave)
38.03 [wrong] would + verb in the result of a general rule (the chair would wobble)
38.04 [wrong] am/is/are + -ing in a general rule (is wobbling, is opening)
38.05 [wrong] Past Simple in the if-clause of a general rule (If you left one screw loose)
38.06 [wrong] Present Simple verb without -s after he/she/it or a singular noun
38.07 [wrong] -s added after a plural subject (your feet stays)
38.08 [wrong] not/no + verb instead of don't/doesn't (If you not water it)
38.09 [wrong] doesn't + verb with -s (doesn't opens)
38.10 [wrong] unless followed by a negative verb (unless you don't score it)
38.11 [wrong] adjective used to describe the verb (opens easy)
38.12 [wrong] all + singular noun for celý/celá (all chair)
38.13 [wrong] Slovak/Czech reflexive verb (sa/se) turned into be + participle (was started, is opened)
38.14 [wrong] adverb put between the verb and its object (score first the skin)
38.15 [wrong] phrase translated word for word from Slovak/Czech (today morning, this night, there where)
38.16 [tip] correct near-synonym or phrasing that sounds less natural (legs for feet, two times for twice)
38.17 [wrong] false friend or near-synonym with a different meaning (work for job, true for real, quiet for still)
38.18 [wrong] article dropped before a singular countable noun (pillow for a pillow)
38.19 [wrong] wrong, extra or missing preposition copied from Slovak/Czech (struck into, on place)
## 39 1. Conditional
39.01 [wrong] will added in the if-clause (If she will report him)
39.02 [wrong] Present Simple in the result where a one-off future consequence needs will (he loses his job by Monday)
39.03 [tip] Present Simple in the result where it still reads as a plan/rule (the dragonfly stays)
39.04 [wrong] would + verb in the result of a real condition (the border would open)
39.05 [wrong] whole sentence in Second Conditional (If he turned …, she would drop …) — use =full sentence
39.06 [wrong] Past Simple in the if-clause with will in the result (If both states signed …, will open)
39.07 [wrong] when used for ak/pokud (When she reports him) — makes the condition certain
39.08 [wrong] Present Simple verb without -s after he/she/it or a singular noun
39.09 [wrong] -s added after a plural subject (If both states signs)
39.10 [wrong] verb with -s or -ed after will (will continues)
39.11 [wrong] will + can (will can come) instead of will be able to
39.12 [tip] am/is/are going to in the result
39.13 [wrong] unless followed by a negative verb (unless she doesn't report him)
39.14 [wrong] until for a deadline (do pondelka = by Monday)
39.15 [wrong] in/on/at before next/last/this + time (in next month)
39.16 [wrong] other + singular noun for ďalší/další (other hour)
39.17 [wrong] possessive chosen by the subject instead of the owner (svoju → her when it is his)
39.18 [wrong] article added where English has none (the next week, the nature)
39.19 [wrong] adverb put between the verb and its object (score first the skin)
39.20 [wrong] false friend or near-synonym with a different meaning (work for job, true for real, quiet for still)
39.21 [wrong] article dropped before a singular countable noun (pillow for a pillow)
## 41 Passive
41.01 [wrong] past participle without was/is (The knot checked twice)
41.02 [wrong] be + base verb (was check)
41.03 [wrong] be + Past Simple form of an irregular verb (was rewrote, is showed)
41.04 [wrong] -ed added to an irregular verb (striked, bursted, flied)
41.05 [wrong] is/are for a past event or was/were for a present one (is checked … leaned)
41.06 [wrong] was with a plural subject or were with a singular one (the boxes was checked)
41.07 [tip] sentence turned active with someone/they as the subject
41.08 [wrong] was/is + -ing (The knot was checking) — active meaning
41.09 [wrong] has/have + past participle without been (has checked for has been checked)
41.10 [wrong] is/was + past participle where being is needed (is cleaned now for is being cleaned)
41.11 [wrong] modal + past participle without be (must checked)
41.12 [wrong] from/of instead of by for the doer (checked from the instructor)
41.13 [tip] by someone/by people/by them added to a passive
41.14 [tip] get + past participle instead of be + past participle (got checked)
41.15 [wrong] it + passive + the real subject after it (It was checked the knot)
41.16 [tip] correct near-synonym or phrasing that sounds less natural (legs for feet, two times for twice)
41.17 [wrong] phrase translated word for word from Slovak/Czech (today morning, this night, there where)
41.18 [wrong] article dropped before a singular countable noun (pillow for a pillow)
41.19 [wrong] wrong, extra or missing preposition copied from Slovak/Czech (struck into, on place)
## 43 Modal verbs Probability
43.01 [wrong] can/could/might/may instead of must for a sure conclusion
43.02 [wrong] must to be / must is / must + -s
43.03 [tip] has to / have to for a logical conclusion
43.04 [tip] plain is/are instead of must be where the evidence makes the fact nearly certain
43.05 [wrong] plain is/are instead of must be where the deduction is the point of the sentence
43.06 [wrong] mustn't be for a negative deduction (it mustn't be real)
43.07 [wrong] might not/may not/can for a sure negative conclusion
43.08 [wrong] must be / must was for a conclusion about the past
43.09 [wrong] must have + Past Simple or base form, or must had (must have went, must had gone)
43.10 [wrong] must + base verb for something happening now (he must joke)
43.11 [tip] maybe/perhaps + verb instead of might/could + verb
43.12 [wrong] might to / could to + verb
43.13 [wrong] are/were after a singular noun that is plural in Slovak/Czech (his mouth are)
43.14 [wrong] Present Simple verb without -s after he/she/it or a singular noun
43.15 [wrong] second negative added (didn't … nothing, never doesn't, neither isn't)
43.16 [wrong] false friend or near-synonym with a different meaning (work for job, true for real, quiet for still)
43.17 [wrong] phrase translated word for word from Slovak/Czech (today morning, this night, there where)
43.18 [wrong] article dropped before a singular countable noun (pillow for a pillow)
## 44 Relative clauses
44.01 [wrong] who/that/which left out when it is the subject of the clause (The ankle swelled up was …)
44.02 [wrong] who/what referring to a thing or animal (The ball who/what)
44.03 [wrong] which/what referring to a person (The officer which)
44.04 [wrong] object repeated as it/him/her inside the relative clause (which the dog fetched it)
44.05 [wrong] verb put before the subject of an object clause (which fetched the dog)
44.06 [wrong] preposition + that (behind that she is standing)
44.07 [wrong] preposition both before which and at the end (on which she sat on)
44.08 [wrong] where combined with a preposition at the end (where she is standing behind)
44.09 [wrong] where used when the place is the object of the clause (the town where she visited)
44.10 [wrong] who's/who his/which his instead of whose (the man who his car)
44.11 [wrong] verb in the clause not agreeing with the noun before who/that (the people who lives)
44.12 [wrong] different tense inside the relative clause (who stamps his passport … looked up)
44.13 [tip] adjective or separate sentence instead of the relative clause (The swollen ankle …)
44.14 [wrong] one dropped after an adjective (was the left, was left one)
44.15 [wrong] second negative added (didn't … nothing, never doesn't, neither isn't)
44.16 [wrong] the/you instead of a possessive with a body part (burn you the fingers, above the head)
44.17 [wrong] phrase translated word for word from Slovak/Czech (today morning, this night, there where)
44.18 [wrong] article dropped before a singular countable noun (pillow for a pillow)
44.19 [wrong] wrong, extra or missing preposition copied from Slovak/Czech (struck into, on place)
## 45 Reported speech
45.01 [tip] Present Simple kept after said/asked (She said she wants)
45.02 [tip] will kept after said (said they will film)
45.03 [wrong] question inversion or do/did kept in a reported question (asked why did he spend)
45.04 [wrong] direct question copied after asked (asked him why do you spend)
45.05 [tip] direct statement copied after said (She said I want one)
45.06 [wrong] pronoun of the original speaker kept so the meaning changes (She said I wanted)
45.07 [wrong] yes/no question reported without if/whether (asked her she was ready)
45.08 [wrong] told with no person after it (She told that)
45.09 [wrong] said + person without to (She said me)
45.10 [wrong] Past Simple for a reported future plan (said they filmed the scene)
45.11 [wrong] past form or -ing after would (would filmed, would filming)
45.12 [tip] was/were going to instead of would
45.13 [wrong] told/asked + don't/imperative instead of (not) to + verb (told him don't touch)
45.14 [wrong] preposition after ask before the person (asked to him, asked from him)
45.15 [tip] tomorrow/today/here kept from the direct speech where the report is later
45.16 [wrong] for + -ing for purpose (just for sitting)
45.17 [wrong] more + short adjective or double comparative (more fast, more faster)
45.18 [wrong] -ed added to an irregular verb (striked, bursted, flied)
45.19 [wrong] phrase translated word for word from Slovak/Czech (today morning, this night, there where)
45.20 [wrong] article dropped before a singular countable noun (pillow for a pillow)
45.21 [wrong] wrong, extra or missing preposition copied from Slovak/Czech (struck into, on place)
## 46 Used to, Would
46.01 [tip] plain Past Simple for a repeated past habit or past state (they bought, he believed)
46.02 [wrong] past form or -ing after would (would bought, would buying)
46.03 [wrong] was/were + -ing for a repeated past habit (they were buying)
46.04 [wrong] use to in a positive statement (he use to believe)
46.05 [wrong] used with -d after did/didn't (didn't used to, did you used to)
46.06 [wrong] past form after used to (used to believed)
46.07 [wrong] -ing after used to for a past habit (used to buying)
46.08 [wrong] was used to + verb/-ing for a past habit (he was used to believe)
46.09 [wrong] got used to for a past habit (they got used to buy)
46.10 [wrong] would + state verb (would believe, would have, would live)
46.11 [wrong] would/used to for one single past event (one day he would find)
46.12 [wrong] usually + Present Simple for a past habit (As kids they usually buy)
46.13 [wrong] would to + verb
46.14 [wrong] like for ako (v úlohe/v čase) (Like kids they would buy)
46.15 [wrong] preposition added after a verb that takes a direct object (believe to every story)
46.16 [wrong] -ed added to an irregular verb (striked, bursted, flied)
46.17 [wrong] phrase translated word for word from Slovak/Czech (today morning, this night, there where)
46.18 [wrong] article dropped before a singular countable noun (pillow for a pillow)
46.19 [wrong] wrong, extra or missing preposition copied from Slovak/Czech (struck into, on place)
## 48 Question tags
48.01 [wrong] he/she/it in the tag after everyone/everybody/nobody (doesn't he?)
48.02 [wrong] isn't it? used as a fixed tag whatever the verb
48.03 [wrong] positive tag after a positive sentence (makes that face, do they?)
48.04 [wrong] negative tag after a negative sentence (doesn't smile, doesn't she?)
48.05 [wrong] negative tag after never/hardly/nobody (never smiles, doesn't she?)
48.06 [wrong] tag uses a different auxiliary from the sentence (is tired, doesn't she?)
48.07 [wrong] tag in a different tense (made that face, don't they?)
48.08 [wrong] noun repeated in the tag instead of a pronoun (doesn't the dog?)
48.09 [wrong] this/that kept in the tag instead of it (That's odd, isn't that?)
48.10 [wrong] amn't I / am I not / isn't I after I am
48.11 [wrong] isn't it? after there is/are (There's time, isn't it?)
48.12 [wrong] don't we?/won't we? after Let's (Let's go, don't we?)
48.13 [wrong] does not they? / do not they? instead of don't they?
48.14 [wrong] pronoun before the verb in the tag (, they don't?)
48.15 [wrong] no?/yes?/not? as a calque of že?/nie? instead of a Question tag
48.16 [tip] right?/correct?/true? instead of the Question tag
48.17 [wrong] plural verb after everyone/everybody (Everyone make)
48.18 [wrong] object first, subject after the verb, copying Slovak/Czech order (That face makes everyone)
48.19 [wrong] Present Simple verb without -s after he/she/it or a singular noun
48.20 [wrong] article dropped before a singular countable noun (pillow for a pillow)
## 50 Past Perfect Continuous
50.01 [wrong] was/were + -ing instead of had been + -ing for duration up to a past point
50.02 [tip] had + past participle instead of had been + -ing (duration stressed)
50.03 [tip] Past Simple instead of had been + -ing before another past event
50.04 [wrong] has/have been + -ing in a past story
50.05 [wrong] has/have + past participle in a past story
50.06 [wrong] is/are + -ing in a past story
50.07 [wrong] had been + base form
50.08 [wrong] had + -ing (been dropped)
50.09 [wrong] been + -ing without had
50.10 [wrong] had being + -ing
50.11 [wrong] had be + -ing
50.12 [wrong] was been + -ing
50.13 [wrong] the later short event (before/when clause) also put into had been + -ing or had + participle
50.14 [wrong] since + length of time
50.15 [wrong] for dropped before a length of time where it is required
50.16 [wrong] during + length of time
50.17 [wrong] 'for months' replaced by 'months ago'
50.18 [wrong] state verb (know, own, believe) in had been + -ing
50.19 [wrong] irregular verb given a regular -ed form elsewhere in the sentence
50.20 [wrong] the later event put into Present Simple/Perfect instead of Past Simple
## 51 Future Perfect Simple
51.01 [wrong] will + base form after a 'by …' deadline
51.02 [wrong] will have + base form
51.03 [wrong] will have + Past Simple form (will have took)
51.04 [wrong] irregular verb with a regular -ed participle (will have writed)
51.05 [wrong] until/till instead of by before the deadline
51.06 [wrong] to, in or on instead of by before the deadline
51.07 [wrong] will be + -ing instead of will have + participle
51.08 [wrong] Present Simple instead of will have + participle
51.09 [wrong] has/have + participle for a future deadline
51.10 [wrong] will has + participle
51.11 [wrong] will had + participle
51.12 [wrong] will + participle (have dropped)
51.13 [wrong] will be + participle followed by an object (she will be finished every exercise)
51.14 [wrong] will have to + base form
51.15 [wrong] be going to + base after a 'by …' deadline
51.16 [wrong] will have been + -ing with a finished result or count
51.17 [tip] 'will be done/finished with' + noun instead of will have + participle
51.18 [wrong] the added before a day of the week or 'closing time'
51.19 [wrong] a/an or the dropped before a singular countable noun
51.20 [wrong] every + plural noun
## 52 Future Perfect Continuous
52.01 [wrong] will be + -ing instead of will have been + -ing
52.02 [tip] will have + participle where the duration is stressed
52.03 [wrong] will + base form with 'by …' and a duration
52.04 [wrong] is/are + -ing instead of will have been + -ing
52.05 [wrong] has/have been + -ing for a future point
52.06 [wrong] will have been + base form
52.07 [wrong] will have + -ing
52.08 [wrong] will been + -ing
52.09 [wrong] will has been + -ing
52.10 [wrong] will have being + -ing
52.11 [wrong] will be been + -ing
52.12 [wrong] be going to + base with 'by …' and a duration
52.13 [wrong] since + length of time
52.14 [wrong] for dropped before a length of time where it is required (not with 'straight')
52.15 [wrong] during + length of time
52.16 [wrong] until/till instead of by before the future point
52.17 [wrong] 'for + time' moved between will have been and the verb
52.18 [wrong] state verb (know, own, belong) in will have been + -ing
52.19 [tip] rephrased as 'it will be X years since …' or similar
52.20 [wrong] this/that with a plural noun
## 53 3. Conditional
53.01 [wrong] Past Simple + would + base for an unreal past
53.02 [wrong] would (have) + verb after if
53.03 [wrong] Past Simple instead of Past Perfect after if (result clause kept)
53.04 [wrong] has/have + participle after if
53.05 [wrong] would + base where the result is clearly over (event finished)
53.06 [tip] would + base where a present result still makes sense
53.07 [tip] would have + participle where the result is true now (Mixed)
53.08 [wrong] would had + participle
53.09 [wrong] would of / could of instead of would have
53.10 [wrong] would + participle (have dropped)
53.11 [wrong] would have + base form
53.12 [wrong] if + had + base form
53.13 [wrong] had/have + Past Simple form (would have went)
53.14 [wrong] will have + participle in the result clause
53.15 [wrong] had + participle in the result clause instead of would have
53.16 [wrong] when instead of if for an unreal condition
53.17 [wrong] unless used for 'if … not' with an unreal past
53.18 [wrong] two negatives in one clause (wouldn't … no)
53.19 [wrong] still placed after be before an adverb/adjective (would be still here)
53.20 [tip] still placed after be before an -ing form (would be still crying)
53.21 [wrong] more + short adjective/adverb (more early, more thick)
## 55 Advanced Passive Voice
55.01 [wrong] is said to + base for an earlier action
55.02 [wrong] is said to have + participle for something true now
55.03 [wrong] subject + is said + that-clause (mixing personal and impersonal passive)
55.04 [tip] People say / They say + clause instead of the passive
55.05 [tip] is supposed to / is believed to instead of the practised is said to
55.06 [wrong] to have + Past Simple form (to have took)
55.07 [wrong] to have + base form
55.08 [wrong] is said + -ing
55.09 [wrong] is said + base form without to
55.10 [wrong] It says (that) … for 'hovorí sa'
55.11 [wrong] About X is said (that) … word-for-word from 'o … sa hovorí'
55.12 [wrong] Is said that … without It
55.13 [wrong] thing + says/believes (This mascara says to …)
55.14 [wrong] passive without a form of be (The treaty said to …)
55.15 [wrong] was said / has been said instead of present is said
55.16 [tip] passive + by people / by everyone
55.17 [wrong] verb + -ing where being + participle is needed (likes rushing)
55.18 [wrong] verb + been + participle instead of being + participle
55.19 [wrong] is + participle for an action in progress (is repaired now)
55.20 [wrong] irregular verb with a regular -ed participle in the passive
55.21 [wrong] take + time + for + -ing instead of to + verb
## 57 Modals in past
57.01 [wrong] could/should/might + base form instead of modal + have + participle
57.02 [wrong] should/could have + base form
57.03 [wrong] modal have + Past Simple form (should have drew)
57.04 [wrong] irregular verb with a regular -ed participle (drawed)
57.05 [wrong] modal + had + participle (should had)
57.06 [wrong] should of / could of / would of
57.07 [wrong] modal + participle (have dropped)
57.08 [wrong] was able to + verb for an unused possibility
57.09 [wrong] had to + verb for a reproach about the past
57.10 [wrong] would have instead of could have for a possibility
57.11 [wrong] must have + participle (deduction) instead of should have
57.12 [wrong] must have where the sense is 'surely not' (opposite meaning)
57.13 [wrong] mustn't have for a negative deduction
57.14 [tip] might have for an unused possibility
57.15 [tip] ought to have + participle
57.16 [tip] was supposed to + verb instead of should have + participle
57.17 [tip] didn't need to + verb for something done unnecessarily
57.18 [tip] should have not / could have not + participle
57.19 [wrong] second clause in present instead of Past Simple
57.20 [wrong] ask to/at + person
57.21 [wrong] body part without his/her/their
## 59 Causative HAVE/GET
59.01 [wrong] subject does the action itself (She dyed her boots) instead of have/get + object + participle
59.02 [tip] object + was/were + participle (Her boots were dyed)
59.03 [wrong] have/get + object + base form
59.04 [wrong] have/get + object + Past Simple form (got it took)
59.05 [wrong] irregular verb with a regular -ed participle
59.06 [wrong] have/get + participle + object (got checked her slides)
59.07 [wrong] had + participle + object (had dyed her boots)
59.08 [wrong] have + object + to + verb (had the kitchen to film)
59.09 [wrong] have + person + to + verb
59.10 [wrong] get + person + base form without to
59.11 [wrong] gave + object + to + verb for 'dať urobiť'
59.12 [wrong] let + object + verb for 'nechať si urobiť'
59.13 [wrong] made + object + participle
59.14 [wrong] extra reflexive pronoun (had herself her hair cut) from 'dala si'
59.15 [wrong] has/gets for a past event (last summer, the night before)
59.16 [wrong] has had + object + participle with a finished past time
59.17 [wrong] from/of instead of by before the person who does it
59.18 [wrong] preposition added before the colour (dyed on purple)
59.19 [wrong] her/his/their dropped before the object or agent
59.20 [wrong] until instead of while for 'kým' (= during)
## 60 Wish clauses
60.01 [wrong] wish + Present Simple (is/are/have) about the present
60.02 [wrong] wish + can
60.03 [wrong] wish + will
60.04 [tip] wish + I/he/she/it was
60.05 [tip] wish + would be for a state
60.06 [wrong] I wish I would … about one's own ability/action
60.07 [wrong] wish + had + participle about the present
60.08 [wrong] wish + Past Simple about a past event
60.09 [wrong] wish + would have + participle
60.10 [wrong] wish + could to + verb
60.11 [wrong] not added because the native sentence has 'škoda, že ne…'
60.12 [wrong] hope + past form for an unreal wish
60.13 [wrong] wish + person/thing + to + verb (I wish my cat to be)
60.14 [wrong] he/she/it + wish
60.15 [tip] would wish that … from 'by si prial/a'
60.16 [tip] It's a pity / would like / too bad instead of wish
60.17 [wrong] so … as in a positive comparison
60.18 [wrong] as + adjective + like
60.19 [wrong] more + short adjective (more thick)
60.20 [wrong] present tense in a clause about a past time (last spring)
## 61 Relative clauses
61.01 [wrong] which + noun for possession
61.02 [wrong] who + noun for possession
61.03 [wrong] whose + his/her/its + noun
61.04 [wrong] whose + the + noun
61.05 [wrong] comma + its/his/her + noun instead of whose (run-on)
61.06 [wrong] extra him/her/it/there inside the relative clause
61.07 [wrong] which referring to a person
61.08 [wrong] who referring to a thing
61.09 [wrong] what instead of which/that after a noun
61.10 [wrong] , what … referring to the whole previous clause
61.11 [wrong] that after a comma (non-defining clause)
61.12 [wrong] which alone for a place where 'where/on which' is needed
61.13 [wrong] where for a thing that is not a place
61.14 [wrong] where + … + on/in at the end
61.15 [wrong] preposition both before which and at the end
61.16 [wrong] verb in the relative clause does not agree with its subject
61.17 [wrong] adverb (now, often) placed between verb and object
61.18 [wrong] the instead of her/his with a body part
61.19 [tip] with + noun or another phrase instead of the relative clause
61.20 [tip] which/who had + noun instead of whose + noun
61.21 [tip] literal calque that is grammatical but unidiomatic (is turned to)
## 63 Advanced linkers
63.01 [wrong] even though/even if standing alone after a semicolon
63.02 [wrong] although standing alone after a semicolon/full stop
63.03 [wrong] although at the end of a sentence
63.04 [wrong] although … , but … (calque of 'hoci …, ale')
63.05 [wrong] despite of + noun
63.06 [wrong] in spite + noun
63.07 [wrong] although/even though + noun phrase without a verb
63.08 [wrong] despite/in spite of + full clause with a verb
63.09 [wrong] despite/in spite of standing alone as a sentence linker
63.10 [tip] although + clause instead of the practised despite + noun
63.11 [tip] however instead of even so / nevertheless
63.12 [tip] simple but instead of the practised linker
63.13 [tip] still/yet as the linker instead of the practised one
63.14 [wrong] even without so for 'aj tak'
63.15 [wrong] so (result) instead of a contrast linker
63.16 [wrong] therefore/thus instead of a contrast linker
63.17 [wrong] moreover/furthermore instead of a contrast linker
63.18 [wrong] because of instead of despite
63.19 [wrong] on the contrary for simple contrast between two facts
63.20 [wrong] otherwise for 'aj tak/napriek tomu'
63.21 [wrong] active -ing instead of past participle after feel/seem (felt watching)
## 65 All Present Tenses
65.01 [wrong] Present Simple for an action happening now
65.02 [wrong] is/are + -ing for a habit or permanent fact
65.03 [wrong] subject + -ing without am/is/are
65.04 [wrong] am/is/are + base form
65.05 [wrong] state verb (know, like, want, belong) in the -ing form
65.06 [wrong] he/she/it (or a singular noun) + verb without -s
65.07 [wrong] -s on the verb with I/you/we/they or a plural noun
65.08 [wrong] does/doesn't + verb with -s
65.09 [wrong] Present Simple/Continuous with for/since for duration up to now
65.10 [wrong] has/have + participle with yesterday/ago/last …
65.11 [wrong] since + length of time
65.12 [wrong] has/have been + -ing with a number of finished items
65.13 [tip] has/have + participle where the ongoing duration is stressed
65.14 [wrong] has/have been + base form
65.15 [wrong] have with he/she/it or has with I/you/we/they
65.16 [wrong] possessive added to a fixed phrase (shaking their hands)
65.17 [wrong] literal verb in a fixed phrase (give hands, make a photo)
65.18 [wrong] SK/CZ look-alike word with another English meaning (notebook for laptop)
65.19 [wrong] a/an or the dropped before a singular countable noun
65.20 [wrong] in front + noun without of
65.21 [tip] before for place instead of in front of
## 67 All Future Tenses
67.01 [wrong] will + base with a 'by …' deadline
67.02 [wrong] will be + -ing for an action finished by a deadline
67.03 [wrong] will have + base form
67.04 [wrong] will have + Past Simple form (will have took)
67.05 [wrong] until/till instead of by before a deadline
67.06 [wrong] will in a time clause after when/as soon as/before/after/if
67.07 [wrong] is/are + -ing in a time clause about one future event
67.08 [wrong] he/she/it + verb without -s in the time clause
67.09 [wrong] Present Simple in the main clause for a single future action
67.10 [wrong] Present Simple for a spontaneous offer/decision (I help you)
67.11 [tip] will + base for a fixed arrangement
67.12 [wrong] will + base for an action in progress at a future moment
67.13 [tip] will have been + -ing for a finished result
67.14 [wrong] will + to + verb
67.15 [wrong] will be + base form
67.16 [wrong] am/is/are going + base form
67.17 [wrong] will + going to / will be going to for a plan
67.18 [wrong] would + base for a real future
67.19 [wrong] other / an other for 'ďalší' with a singular noun

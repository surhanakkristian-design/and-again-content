# Task: annotate batch S (20 sentences) — Phase 1c

Budget: ONE read (this file, already done) and ONE write. Do not open any other file, do not search, do not run code.
Write `/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase1c/annotated/batchS.json`: a JSON array, one compact object per line, one per sentence below, same order. Nothing else.

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
{"id": 23026, "t": 3, "topic": "Present Simple", "lv": "A1", "long": false, "en": "She wears the skirt in the park every Sunday.", "ans": "wears", "sk": "Túto sukňu nosí do parku každú nedeľu."}
{"id": 29691, "t": 8, "topic": "My, Your, His,...", "lv": "A1", "long": false, "en": "He drops his guidebook on the church steps! Total disaster!", "ans": "his", "sk": "Pustí svojho sprievodcu na kostolné schody! Úplná katastrofa!"}
{"id": 25921, "t": 6, "topic": "A, AN, THE", "lv": "A1", "long": false, "en": "They watch a volcano from the grassy ridge.", "ans": "a volcano", "sk": "Z trávnatého hrebeňa pozorujú sopku"}
{"id": 16261, "t": 17, "topic": "Future BE GOING TO", "lv": "A2", "long": false, "en": "He has a plan. He is going to walk her home.", "ans": "is going to", "sk": "Má plán. Chystá sa odprevadiť ju domov."}
{"id": 27097, "t": 20, "topic": "Much, Many, Some...", "lv": "A2", "long": false, "en": "Of course this square has many advertisements, exactly what we needed.", "ans": "many", "sk": "Jasné, toto námestie má veľa reklám, presne to sme potrebovali."}
{"id": 16403, "t": 16, "topic": "Future with WILL", "lv": "A2", "long": false, "en": "Say bye now and she will come back in an hour.", "ans": "will", "sk": "Rozlúč sa a o hodinu sa vráti naspäť."}
{"id": 13175, "t": 19, "topic": "Countable and uncountable", "lv": "A2", "long": false, "en": "There is a lot of yellow cheese on the board.", "ans": "cheese", "sk": "Na doske je veľa žltého syra"}
{"id": 1018, "t": 34, "topic": "Present Perfect Simple or Continuos", "lv": "B1", "long": true, "en": "He has poured the smoothie into the tall glass, so the blender is completely empty now.", "ans": "has poured", "sk": "Smoothie prelial do vysokého pohára, takže mixér je teraz úplne prázdny."}
{"id": 3603, "t": 45, "topic": "Reported speech", "lv": "B1", "long": true, "en": "The engineer asked him when he was bringing the race car back into the garage.", "ans": "was bringing", "sk": "Inžinier sa ho spýtal, kedy privezie pretekárske auto späť do garáže."}
{"id": 8799, "t": 47, "topic": "Gerund vs Infinitive", "lv": "B1", "long": false, "en": "She kept throwing the same combination until it felt smooth.", "ans": "throwing", "sk": "Stále hádzala tú istú kombináciu, kým nešla hladko."}
{"id": 4612, "t": 40, "topic": "2. Conditional", "lv": "B1", "long": false, "en": "If he held the screwdriver, that shelf would be on the floor by now.", "ans": "held", "sk": "Keby skrutkovač držal on, tá polica by už dávno bola na zemi."}
{"id": 9992, "t": 44, "topic": "Relative clauses", "lv": "B1", "long": false, "en": "The ankle that swelled up was the left one.", "ans": "that", "sk": "Členok, ktorý opuchol, bol ten ľavý."}
{"id": 7716, "t": 47, "topic": "Gerund vs Infinitive", "lv": "B1", "long": false, "en": "She managed to stay completely still until the dragonfly settled.", "ans": "to stay", "sk": "Podarilo sa jej vydržať úplne nehybne, kým sa vážka usadila."}
{"id": 8756, "t": 45, "topic": "Reported speech", "lv": "B1", "long": false, "en": "He said the puck travelled faster on cold ice.", "ans": "travelled", "sk": "Povedal, že puk letí rýchlejšie na studenom ľade."}
{"id": 9907, "t": 53, "topic": "3. Conditional", "lv": "B2", "long": true, "en": "If she had taken the beige jacket, this look would never have happened.", "ans": "had taken", "sk": "Keby si bola vzala béžovú bundu, tento look by nikdy nevznikol."}
{"id": 7558, "t": 58, "topic": "Inversion basic", "lv": "B2", "long": false, "en": "Never had we seen a group this quiet at sunset.", "ans": "had we seen", "sk": "Nikdy predtým sme nevideli takú tichú skupinu pri západe slnka."}
{"id": 10959, "t": 54, "topic": "Mixed Conditional", "lv": "B2", "long": false, "en": "If she had bought thicker paper, the bouquet would be perfect now.", "ans": "would be", "sk": "Keby bola kúpila hrubší papier, kytica by bola teraz dokonalá."}
{"id": 7687, "t": 59, "topic": "Causative HAVE/GET", "lv": "B2", "long": false, "en": "They had the kitchen filmed while they built the rainbow plate.", "ans": "had", "sk": "Kuchyňu si dali natočiť, kým skladali ten dúhový tanier."}
{"id": 9607, "t": 55, "topic": "Advanced Passive Voice", "lv": "B2", "long": false, "en": "She is said to have trained at altitude all winter.", "ans": "is said", "sk": "Hovorí sa, že celú zimu trénovala vo výške."}
{"id": 10043, "t": 56, "topic": "Reported speech", "lv": "B2", "long": false, "en": "He asked how long the swelling had been sitting on her foot.", "ans": "had been sitting", "sk": "Spýtal sa, ako dlho ten opuch na jej nohe je"}

## LIBRARY INDEX (topics of this batch only): id [wrong|tip] pattern (slots: extra slots to fill)
## 3 Present Simple
3.01 [wrong] drop -s/-es from a he/she/it verb
3.02 [wrong] add -s after I/you/we/they or a plural subject
3.03 [wrong] watchs, gos, washs, fixs
3.04 [wrong] studys, carrys, flys
3.05 [wrong] haves / have for has
3.06 [wrong] is/are + -ing with every day/usually/always
3.07 [tip] is/are + -ing with no habit word in the sentence
3.08 [wrong] not/no before the verb (She not likes, He no works)
3.09 [wrong] doesn't/does + verb with -s
3.10 [wrong] don't after he/she/it
3.11 [wrong] doesn't after I/you/we/they
3.12 [wrong] statement order with a question mark, or inverted verb (Likes she tea?)
3.13 [wrong] always/usually/often after the verb or at the end
3.14 [tip] every day/every winter between verb and object or place
3.15 [wrong] noun with -s after every/each
3.16 [wrong] adjective where the -ly adverb is needed (slow for slowly)
3.17 [wrong] drop the subject pronoun (SK/CZ pro-drop)
3.18 [wrong] drop a/an/the before a noun
3.19 [wrong] replace the preposition with a typical SK/CZ calque (in/on/at/to/for)
3.20 [wrong] a different word whose meaning does not fit (carry for wear, listen for hear)
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
## 8 My, Your, His,...
8.01 [wrong] him/her/them/me before a noun instead of his/her/their/my
8.02 [wrong] he/she/they/I before a noun instead of his/her/their/my
8.03 [wrong] his for a female owner or her for a male owner
8.04 [wrong] it's (or its') where the possessive its belongs
8.05 [wrong] there or they're for their
8.06 [wrong] you're for your
8.07 [wrong] my/your where svoj/svůj refers to he/she/they
8.08 [tip] the/a where the native sentence has jeho/jej/svoj
8.09 [wrong] drop my/his/her before the noun
8.10 [wrong] the/a together with my/his/her (the my bag)
8.11 [wrong] possessive written twice (her her coat)
8.12 [wrong] mine/yours/hers/ours before a noun
8.13 [wrong] my/your/her at the end without a noun (It is my.)
8.14 [wrong] name + noun without 's (Peter car)
8.15 [tip] the car of Peter for Peter's car
8.16 [tip] his money where vlastné/vlastní asks for his own
8.17 [wrong] the instead of my/his/her/its before a body part
8.18 [wrong] drop -s/-es from a he/she/it verb
8.19 [wrong] replace the preposition with a typical SK/CZ calque (in/on/at/to/for)
8.20 [wrong] add -s to evidence, information, advice, money, furniture
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
## 17 Future BE GOING TO
17.01 [tip] will for a plan or intention already made
17.02 [wrong] goes to / go to + verb (calque of ide urobiť)
17.03 [wrong] drop am/is/are before going to
17.04 [wrong] going + verb without to
17.05 [wrong] going to + verb-ing
17.06 [wrong] going to + verb with -s
17.07 [wrong] Present Simple for a plan
17.08 [tip] is/are + -ing for an arranged plan
17.09 [wrong] am/is/are not matching the subject (they is, he are)
17.10 [wrong] statement order with a question mark, or Do you going to…?
17.11 [wrong] don't going to / not is going to
17.12 [tip] gonna in a neutral, non-slang sentence
17.13 [wrong] go/walk/take … to home
17.14 [wrong] drop a needed small word (of, out, on, it, to)
17.15 [wrong] him/her for an object (SK/CZ grammatical gender)
17.16 [wrong] add -s to a noun that must stay singular (after one, every)
17.17 [wrong] drop a/an/the before a noun
17.18 [wrong] replace the preposition with a typical SK/CZ calque (in/on/at/to/for)
17.19 [wrong] a different word whose meaning does not fit (carry for wear, listen for hear)
## 19 Countable and uncountable
19.01 [wrong] There are / are with an uncountable noun
19.02 [wrong] add -s to evidence, information, advice, money, furniture
19.03 [wrong] a/an before an uncountable noun (a sugar, a water)
19.04 [wrong] many before an uncountable noun (many water)
19.05 [wrong] much before a plural countable noun
19.06 [wrong] a few / few before an uncountable noun
19.07 [wrong] a little / little before a plural countable noun
19.08 [wrong] little/few (almost none) for a little/a few (some)
19.09 [tip] much in a plain positive sentence
19.10 [wrong] a lot + noun without of
19.11 [wrong] number + uncountable noun (two breads, three waters)
19.12 [wrong] some in a negative sentence or open question
19.13 [wrong] how much with a plural noun or how many with an uncountable one
19.14 [wrong] singular countable noun without a/an
19.15 [wrong] these/those/many before an uncountable noun
19.16 [wrong] start with the place phrase and drop there (On the bench is a bag)
19.17 [wrong] replace the preposition with a typical SK/CZ calque (in/on/at/to/for)
19.18 [wrong] a different word whose meaning does not fit (carry for wear, listen for hear)
19.19 [wrong] drop a/an/the before a noun
## 20 Much, Many, Some...
20.01 [wrong] much before a plural countable noun
20.02 [wrong] many before an uncountable noun (many water)
20.03 [wrong] is/was with a plural subject
20.04 [wrong] are/were with a singular or uncountable subject
20.05 [wrong] many + noun without -s
20.06 [wrong] no many / no much for not many / not much
20.07 [tip] a lot of / lots of where the sentence practises many/much
20.08 [tip] much in a plain positive sentence
20.09 [wrong] some in a negative sentence or open question
20.10 [wrong] any in a plain positive sentence
20.11 [wrong] two negatives in one clause (don't … nothing, isn't no)
20.12 [wrong] a lot + noun without of
20.13 [wrong] a lots of / lot of
20.14 [wrong] a few / few before an uncountable noun
20.15 [wrong] a little / little before a plural countable noun
20.16 [wrong] little/few (almost none) for a little/a few (some)
20.17 [wrong] add -s to people/children/men/women
20.18 [wrong] add -s to a verb after I/you/we/they or a plural noun
20.19 [wrong] start with the place phrase and drop there (On the bench is a bag)
20.20 [wrong] change the tense of a verb outside the practised span
20.21 [wrong] an SK/CZ look-alike word (automat, reklama, control)
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
## 40 2. Conditional
40.01 [wrong] Present Simple or is/are in the if-clause of an unreal situation (If durians don't smell)
40.02 [wrong] would added in the if-clause (If she would be a robot)
40.03 [wrong] will/won't in the result of an unreal condition
40.04 [wrong] whole sentence in First Conditional (If the beam is weaker, he will …) — use =full sentence
40.05 [tip] If I/he/she/it was instead of were
40.06 [wrong] base verb in the if-clause (If he hold)
40.07 [wrong] had + past participle in the if-clause (If he had held) — refers to the past
40.08 [wrong] would have + past participle in the result (would have let them through)
40.09 [wrong] would + can (would still can blink)
40.10 [wrong] could + verb for by + verb where no ability is meant (customs could let them through)
40.11 [wrong] past form, -s or to after would (would held, would to let)
40.12 [wrong] Past Simple + not instead of didn't + verb (smelled not)
40.13 [wrong] subject before would in a question (What you would do if …?)
40.14 [wrong] object pronoun after the particle of a phrasal verb (let through them)
40.15 [wrong] more + short adjective (more weak)
40.16 [wrong] until now for už (do tejto chvíle) (would be on the floor until now)
40.17 [wrong] phrase translated word for word from Slovak/Czech (today morning, this night, there where)
40.18 [wrong] article dropped before a singular countable noun (pillow for a pillow)
40.19 [wrong] wrong, extra or missing preposition copied from Slovak/Czech (struck into, on place)
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
## 47 Gerund vs Infinitive
47.01 [wrong] to + verb after keep/enjoy/avoid/finish/mind/suggest (kept to throw)
47.02 [wrong] base verb after keep/enjoy/finish (kept throw)
47.03 [wrong] -ing after refuse/manage/decide/want/hope/promise (refused leaving)
47.04 [wrong] base verb without to after refuse/manage/decide (managed stay)
47.05 [wrong] past form after to (to left, to stayed)
47.06 [wrong] preposition + to/base verb (before to leave, interested in learn)
47.07 [wrong] look forward to / be used to + base verb (look forward to see)
47.08 [wrong] with/of added after finish/stop/start (finished with wrapping)
47.09 [wrong] -ing and to swapped after stop/remember/forget/try, changing the meaning
47.10 [wrong] let/make + person + to + verb (made her to wait)
47.11 [wrong] want + that-clause copied from chcieť, aby (wanted that she stays)
47.12 [wrong] succeeded to + verb for podarilo sa (succeeded to stay)
47.13 [wrong] still + verb for kept doing (She still threw)
47.14 [wrong] stopped for finished/completed (She stopped wrapping)
47.15 [tip] was able to / could for podarilo sa
47.16 [tip] didn't want to instead of refused to (weaker meaning, same structure type)
47.17 [wrong] negative verb after until copied from Slovak/Czech (until it didn't feel smooth)
47.18 [wrong] adverb after feel/look/seem (felt smoothly)
47.19 [wrong] article dropped before a singular countable noun (pillow for a pillow)
47.20 [wrong] wrong, extra or missing preposition copied from Slovak/Czech (struck into, on place)
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
## 54 Mixed Conditional
54.01 [tip] if + had been for a condition that is still true (permanent trait)
54.02 [wrong] would + base where the result would already have happened
54.03 [wrong] would have + participle for a result true now
54.04 [wrong] would + verb after if
54.05 [wrong] Present Simple after if for an unreal present condition
54.06 [wrong] Past Simple after if for a past cause
54.07 [wrong] has/have + participle after if
54.08 [tip] if + I/he/she/it was instead of were
54.09 [wrong] will instead of would in the result clause
54.10 [wrong] real condition (is/will) instead of an unreal one
54.11 [wrong] result clause in plain present/past without would
54.12 [wrong] would had + participle
54.13 [wrong] if + had + base form
54.14 [wrong] unless used for 'if … not' in an unreal condition
54.15 [wrong] when instead of if for an unreal condition
54.16 [wrong] yet in a positive clause for 'already'
54.17 [wrong] such + adjective without a noun
54.18 [wrong] more + short adjective (more thick)
54.19 [wrong] a/an before an uncountable noun (a paper, an advice)
54.20 [wrong] 'all them' instead of 'them all' / 'all of them'
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
## 56 Reported speech
56.01 [tip] reported earlier action in Past Simple instead of had + participle
56.02 [wrong] auxiliary before the subject in a reported question
56.03 [wrong] did + base kept in a reported question
56.04 [wrong] direct question form (is/are/do + subject) after asked
56.05 [wrong] has/have + participle kept after a past reporting verb when the situation is clearly over
56.06 [tip] present tense kept after a past reporting verb when it may still be true
56.07 [wrong] Past Simple for an action that was in progress (meaning: finished)
56.08 [wrong] Present Simple for an action in progress after a past verb
56.09 [wrong] will kept after a past reporting verb
56.10 [wrong] can kept after a past reporting verb
56.11 [wrong] how long + Past Simple instead of had been
56.12 [wrong] asked (me) that … for a yes/no question
56.13 [wrong] asked + clause without if/whether
56.14 [wrong] said me / said him (person directly after say)
56.15 [wrong] told that … without a person
56.16 [wrong] possessive/personal pronoun not adapted to the reporter's view
56.17 [tip] tomorrow/yesterday/now kept after a past reporting verb
56.18 [wrong] insisted on + -ing instead of insisted that …
56.19 [tip] quoted direct speech instead of reported speech
56.20 [wrong] asked about whether/if
## 58 Inversion basic
58.01 [wrong] negative adverbial first, then normal subject-verb order
58.02 [tip] ordinary word order with never/rarely inside the sentence
58.03 [wrong] not added after the negative adverbial
58.04 [wrong] had + subject + Past Simple form (had we saw)
58.05 [tip] did-inversion instead of had-inversion for experience up to a past point
58.06 [wrong] did + subject + Past Simple form (did we saw)
58.07 [wrong] full verb inverted in a simple tense (Rarely saw we)
58.08 [wrong] subject placed before the auxiliary after the adverbial (Not only he did)
58.09 [wrong] have/has instead of had (or vice versa) in the inversion
58.10 [wrong] auxiliary does not agree with the subject (Never has they)
58.11 [wrong] second clause after but/when also inverted
58.12 [wrong] inversion right after 'only when/after' instead of in the main clause
58.13 [wrong] than after hardly/scarcely instead of when
58.14 [wrong] when after no sooner instead of than
58.15 [wrong] second clause after than/when also in Past Perfect
58.16 [wrong] inversion after a non-negative adverb (Often had we seen)
58.17 [wrong] main verb (not auxiliary) moved before the subject in a perfect tense
58.18 [wrong] so + adjective + noun (so quiet group)
58.19 [wrong] such + adjective + singular noun without a
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

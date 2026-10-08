# A66 "write your own story" phrases (exercise 5 page 2) - writer brief

RUN = ~/Projects/and-again-content/runs/a66_20261008/. Input: RUN/content/source.json = the 8 lab items exactly as the
learner meets them (ex1 tap phrases, ex2 nouns, ex3 carousel captions + scene descriptions of the 3 carousel pictures,
ex4 mind map captions/chips + rows with a [gap], ex5 story in 3 parts + b) models). Pictures:
~/Projects/and-again-content/runs/a65_20261007/stills/<id>.png (all 8), frames/<id>_NN.png (videos 62, 236, 7071, 8039),
carousel/ (carousel pictures, if present). Look at the still of each item before you choose.

Exercise 5 page 2 asks the learner to write their OWN short story about the VIDEO (the still for the pilots 900001,
900002). Above the field the app shows exactly 4 helpful phrases. For each item choose the 4 MOST USEFUL phrases for
writing a story about this video, TAKEN FROM THIS ITEM'S EXERCISES (tap phrases, ex4 rows, mind-map / carousel captions,
the story). Rules:
- Exactly 4 phrases per item. Phrase 1 should hold the key word.
- Prefer phrases that describe what actually happens in the video (the action, the doer, the funny point) over phrases
  that only fit a carousel picture. Carousel / mind-map options of the SAME pattern may be grouped with "or", written
  like "blind, dream or double date" / "beach or gym bag" (at most 3 options) - only when the options really are
  alternatives a story could use.
- Keep the wording of the exercise (verb phrases in the infinitive with "to": "to ride a quad bike"; nouns / short
  phrases as in the captions). You may shorten a phrase (drop a part) but not invent new words.
- Natural US English (the owner's examples: "to have a date", "to impress her with his self-confidence", "to laugh about
  the jokes", "blind, dream or double date").
- No two phrases that say the same thing.

For each phrase also write `match` = how the app decides that the learner used it in their story:
- one or more alternatives, one per option of a grouped phrase: "blind, dream or double date" ->
  [["blind","date"],["dream","date"],["double","date"]];
- each alternative = the BASE forms (lemmas: lowercase, singular, infinitive) of the words that must appear in the
  learner's story IN THIS ORDER, each within 4 words of the previous one;
- leave out "to", articles, possessives and anything a natural retelling may drop or change. The owner counts "had a
  date", "laughed about the jokes", "impressed her" as uses of "to have a date", "to laugh about the jokes", "to impress
  her with his self-confidence". So pick the SMALLEST set that still means THIS phrase: usually the verb + its key noun
  (["have","date"], ["laugh","joke"]) or just a distinctive verb (["impress"]). Never require a preposition or a
  pronoun. Do not pick a set so loose that any story matches (e.g. just ["king"] for "to bow to the king" is too loose -
  ["bow","king"] is right; "the king bowed" would NOT match since "king" comes before "bow" - consider whether the
  natural retelling keeps the order; if a natural retelling may flip it, choose the distinctive word alone, e.g. ["bow"]).
- Multi-word nouns: each word ("water","bottle"). Hyphenated words are one token ("thumbs-up"). The matcher lemmatises
  the learner's words (regular -s/-es/-ed/-ing/-ied, doubled consonants, common irregular verbs and plurals), so lemmas
  are enough; a lemma must be a real base form (irregular: "ride" not "rode", "fly" not "flew").

Output RUN/content/phrases_writer.json:
{"<id>": [{"text": "...", "match": [["...", "..."]], "from": "ex1|ex3|ex4|ex5 and which entry", "why": "short"}, ... 4]}
Reply with one line.

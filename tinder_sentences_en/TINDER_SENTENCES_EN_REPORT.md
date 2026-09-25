Media done: 3658 of 3664; media left: 6; TRUE sentences of 30 characters or less: A-level 1643/1918 = 85.7 %, B-level 1481/1740 = 85.1 % (floor 70 %).

# Tinder texts, English: all media, four texts each

Written 25 Sept 2026 (owner decisions 120-122). Every media with an asset description got a TRUE sentence, a FALSE sentence, a TRUE short phrase and a FALSE short phrase, written by an Opus writer from `media.asset_description` (plus the transcript where there is one) and checked by an independent Opus verifier plus a deterministic checker (`check.py`). Only rows both accepted are stored.

## Where it is

- Table `public.tinder_sentences` (migration `supabase/migrations/20260925150000_tinder_sentences.sql`, applied live): media_id, language_code, true_sentence, false_sentence, true_phrase, false_phrase, tone, device, created_at; unique (media_id, language_code); RLS on with the read policy of exercise_localizations; anon and authenticated have SELECT only.
- English rows live: **3658** (language_code `en`). The database writes were not refused; every slice was upserted as soon as it was agreed.
- Working files: `~/Projects/and-again-content/tinder_sentences_en/` (RULES.md, task files, check.py, pipeline.py, write_slice.sh, slices/sNN_*.jsonl, tokens.tsv).
- Review page: `TINDER_SENTENCES_EN.html` (same Drive folder as this report).

## Scope

- Live media with an asset description: 3664 (A-level 1924, B-level 1740). 3 media without a description were out of scope. Level group = A or B from the media's exercise types.
- 25 slices ordered by level group, then category, then id: 13 A slices of 148 and 12 B slices of 145.

## Length: the 70/30 rule

- TRUE sentence 30 characters or less: A 1643/1918 = 85.7 %, B 1481/1740 = 85.1 %. Both above the 70 % floor.
- FALSE sentences follow the TRUE sentence's length class (checked for every row).
- Longest TRUE sentence 59 characters; median 28. Phrases: longest 30 characters.
- Sentences the verifier marked as stretched past 30 characters only for a joke: 319 of 3658 (8.7 %; limit 20 %).

## Tense of the TRUE sentence

- A: present_simple 1104 (57.6 %), present_continuous 617 (32.2 %), past 184 (9.6 %), future 13 (0.7 %)
- B: present_simple 1005 (57.8 %), present_continuous 548 (31.5 %), past 180 (10.3 %), future 7 (0.4 %)
- Present simple is the largest group because most TRUE sentences state what is visible with a stative verb (is, has, looks, wants) rather than an action. Actions going on in the media use the present continuous; the verifier rejected 39 rows in round 1 for a wrong tense (mostly present simple for an ongoing action), all rewritten.
- The first draft of slice s01 (discarded before verification) used the present simple for ongoing actions in 138 of 148 rows; the rules were tightened and s01 was rewritten. Its tokens are in the total.

## Humour devices and tones

- Devices, A: none 908 (47.3 %), exclamation 462 (24.1 %), exaggeration 238 (12.4 %), guessing 133 (6.9 %), understatement 77 (4.0 %), cliche 55 (2.9 %), blaming_someone 17 (0.9 %), cheap_quality 14 (0.7 %), banter 9 (0.5 %), bad_excuse 5 (0.3 %)
- Devices, B: none 1029 (59.1 %), exclamation 323 (18.6 %), exaggeration 160 (9.2 %), guessing 76 (4.4 %), understatement 68 (3.9 %), cliche 41 (2.4 %), blaming_someone 21 (1.2 %), banter 9 (0.5 %), cheap_quality 8 (0.5 %), bad_excuse 5 (0.3 %)
- Tones, A: chill 699 (36.4 %), dramatic 513 (26.7 %), slang 234 (12.2 %), business 150 (7.8 %), gossip 88 (4.6 %), ironic 82 (4.3 %), low_iq 79 (4.1 %), flirt 73 (3.8 %)
- Tones, B: chill 617 (35.5 %), dramatic 357 (20.5 %), gossip 155 (8.9 %), slang 141 (8.1 %), ironic 133 (7.6 %), nerd 128 (7.4 %), business 105 (6.0 %), low_iq 53 (3.0 %), flirt 51 (2.9 %)
- Rows with a humour device: 1721 of 3658 (47.0 %). The rest are plain factual sentences, which the brief ranks above a forced joke.
- 57 rows were accepted after the verifier's only objection was the tone LABEL (a plain sentence labelled business/gossip/flirt etc.); their label was changed to chill, the text is unchanged.

## Pop culture

- 22 rows use a pop-culture name (0.6 %). Most used: Ronaldo 2, LeBron 2, Batman 2, Messi 2, Harry Potter 2, Jack Sparrow 1, Mona Lisa 1, Santa Claus 1, Oscar 1, Spider-Man 1, Star Wars 1, Indiana Jones 1, Frozen (Elsa) 1, Sherlock Holmes 1, Lego 1.
- Pop culture is rare because the writers used it only where a name genuinely fits the scene and the brief forbids inventing; it can be raised in a later pass if the owner wants more.

## Verifier rejections by reason

- Round 1: 198 of 3664 rows rejected. Reasons (a row can have several): tone 82, tense 39, false_sentence_unclear 20, grammar 16, false_phrase_weak 15, not_true 9, word_missing 7, translatability 7, false_phrase_bad 6, register 5, false_sentence_true 5, other 3, phrase_not_label 1, invented 1.
- Round 2 (the rejected rows rewritten once and re-checked by the verifier): 7 of 142 rejected again. Reasons: false_sentence_unclear 2, register 1, false_sentence_true 1, not_true 1, other 1, tense 1.

| slice | level | media | stored | round-1 rejects | retried | round-2 rejects |
|---|---|---|---|---|---|---|
| s01 | A | 148 | 148 | 28 | 1 | 0 |
| s02 | A | 148 | 147 | 19 | 19 | 2 |
| s03 | A | 148 | 147 | 22 | 22 | 1 |
| s04 | A | 148 | 148 | 3 | 3 | 0 |
| s05 | A | 148 | 147 | 7 | 7 | 1 |
| s06 | A | 148 | 148 | 13 | 8 | 0 |
| s07 | A | 148 | 147 | 4 | 4 | 1 |
| s08 | A | 148 | 147 | 3 | 3 | 1 |
| s09 | A | 148 | 148 | 3 | 3 | 0 |
| s10 | A | 148 | 147 | 5 | 5 | 1 |
| s11 | A | 148 | 148 | 13 | 6 | 0 |
| s12 | A | 148 | 148 | 5 | 5 | 0 |
| s13 | A | 148 | 148 | 2 | 2 | 0 |
| s14 | B | 145 | 145 | 1 | 1 | 0 |
| s15 | B | 145 | 145 | 4 | 4 | 0 |
| s16 | B | 145 | 145 | 7 | 6 | 0 |
| s17 | B | 145 | 145 | 6 | 5 | 0 |
| s18 | B | 145 | 145 | 2 | 2 | 0 |
| s19 | B | 145 | 145 | 4 | 4 | 0 |
| s20 | B | 145 | 145 | 4 | 4 | 0 |
| s21 | B | 145 | 145 | 25 | 10 | 0 |
| s22 | B | 145 | 145 | 1 | 1 | 0 |
| s23 | B | 145 | 145 | 8 | 8 | 0 |
| s24 | B | 145 | 145 | 6 | 6 | 0 |
| s25 | B | 145 | 145 | 3 | 3 | 0 |

## 20 examples, A-level

| id | word | TRUE sentence | FALSE sentence | TRUE phrase | FALSE phrase | tone / device |
|---|---|---|---|---|---|---|
| 67 | banana | He learned a new banana trick. (30) | He learned a new apple trick. (29) | peeling a banana | a banana in a smoothie | chill / none |
| 262 | elephant | Free shower for the elephant. (29) | Free shower for the giraffe. (28) | an elephant at a waterhole | an elephant in a circus | slang / cheap_quality |
| 285 | family | Family photo time. Say cheese! (30) | Family swim time. Say cheese! (29) | a family photo outside | a family photo album | dramatic / exclamation |
| 370 | helmet | The red helmet did its job. (27) | The blue helmet did its job. (28) | a red skate helmet | a helmet on a motorbike | chill / understatement |
| 514 | oven | The oven is their new TV. (25) | The fridge is their new TV. (27) | bread rising in the oven | pizza in the oven | slang / exaggeration |
| 582 | proud | She is proud of her chair. (26) | She is proud of her table. (26) | proud of her work | proud of her car | chill / none |
| 601 | razor | He is shaving with a razor. (27) | He is shaving with a knife. (27) | an electric razor | a razor blade | chill / none |
| 668 | shoes | Shoes laced. Ready to go. (25) | Boots laced. Ready to go. (25) | lacing up brown shoes | polishing brown shoes | business / none |
| 1163 | lady | The lady has white gloves on. (29) | The lady has black gloves on. (29) | a lady on the stairs | a lady at the bar | chill / none |
| 2656 | bus | Two red buses. Very London. (27) | Two red trams. Very London. (27) | a red double-decker bus | a red double-decker tram | slang / cliche |
| 2788 | blow | She is blowing petals. (22) | She is blowing out candles. (27) | blowing petals and butterflies | blowing out candles | chill / none |
| 4116 | small | His car is so small! (20) | His car is so big! (18) | a small red bubble car | a small red boat | dramatic / exclamation |
| 4243 | pay | Someone is paying by card. (26) | Someone is paying with cash. (28) | paying for a hot dog | paying for a pizza | chill / none |
| 4315 | price | The price keeps going up! (25) | The price keeps going down! (27) | the price of a flat | the price of a car | dramatic / exclamation |
| 4320 | plan | He is drawing a plan. (21) | He is drawing a face. (21) | drawing a house plan | making a holiday plan | chill / none |
| 4588 | traffic | The traffic is stopped. (23) | The traffic is moving. (22) | stopped traffic at night | heavy traffic in the day | business / none |
| 4856 | teacher | The teacher is behind a wall of paper. (38) | The teacher is behind a wall of books. (38) | a teacher marking papers | a teacher reading a book | dramatic / exaggeration |
| 4957 | hotel | Hotel prices range from cheap to 2,000 EUR. (43) | Hotel prices range from cheap to 20 EUR. (40) | three kinds of hotel | a hotel by the sea | business / cheap_quality |
| 4977 | hand | A hand is leading the way. (26) | A dog is leading the way. (25) | an outstretched open hand | a hand full of rice | chill / none |
| 5141 | doctor | The doctor has a stethoscope. (29) | The doctor has a camera. (24) | a doctor with a stethoscope | a doctor in an ambulance | chill / none |

## 20 examples, B-level

| id | word | TRUE sentence | FALSE sentence | TRUE phrase | FALSE phrase | tone / device |
|---|---|---|---|---|---|---|
| 398 | hygiene | Hygiene first, then thumbs up. (30) | Hygiene first, then high five. (30) | good hygiene in the bathroom | good hygiene in the kitchen | chill / none |
| 1576 | dream | In her dream, she swings from the moon. (39) | In her dream, she swings from a tree. (37) | a dream about the moon | a dream about the sea | chill / guessing |
| 1597 | underwater | Oops, his face is underwater! (29) | Oops, his face is in the sand! (30) | a dog underwater | a dog above the water | dramatic / exclamation |
| 1644 | armor | The knight wears full armor. (28) | The knight wears no armor. (26) | a knight in metal armor | a knight without armor | chill / none |
| 1908 | heron | Bro, the heron is chilling. (27) | Bro, the swan is chilling. (26) | a heron on a branch | a heron in the water | slang / none |
| 2034 | poppy | This poppy is red. Very red. (28) | This poppy is blue. Very blue. (30) | a red poppy bloom | a field of poppies | low_iq / none |
| 2359 | traditional | They wear traditional dress. (28) | They wear modern dress. (23) | traditional Indian dress | a traditional wedding cake | chill / none |
| 2415 | garland | The god wears flower garlands. (30) | The god wears paper garlands. (29) | garlands of red flowers | garlands on a Christmas tree | chill / none |
| 2603 | sheet music | The sheet music is handwritten. (31) | The sheet music is printed out. (31) | old handwritten sheet music | new printed sheet music | nerd / none |
| 2723 | furious | He is absolutely furious! (25) | She is absolutely furious! (26) | a furious warrior | a furious dragon | dramatic / exclamation |
| 4318 | applause | His applause is growing. (24) | His laughter is growing. (24) | applause for the performer | applause for the team | chill / none |
| 4348 | athletic | She looks so athletic! (22) | He looks so athletic! (21) | an athletic surfer | an athletic club meeting | flirt / exclamation |
| 4622 | sigh | She is sighing at the ceiling. (30) | She is sighing at the window. (29) | sighing at the gate | sighing with relief | chill / none |
| 4893 | crowded | Crowded to the very top! (24) | Crowded only at the bottom! (27) | a crowded baseball stadium | a crowded bus at night | dramatic / exclamation |
| 5070 | mattress | She's testing every mattress. (29) | She's testing every pillow. (27) | lying back on a mattress | carrying a mattress | chill / none |
| 5284 | metal | Love the metal armour, knight. (30) | Love the metal crown, knight. (29) | a full metal suit | a full metal band | flirt / none |
| 5350 | creek | Mid-air over the creek. Brave! (30) | Mid-air over the lake. Brave! (29) | jumping across a creek | swimming in a creek | dramatic / exclamation |
| 5373 | expand | Everything is expanding! (24) | Everything is shrinking! (24) | a bouncy castle expanding | a business expanding abroad | dramatic / exclamation |
| 5446 | misty | The hills are misty. (20) | The hills are sunny. (20) | misty hills over a lake | misty eyes at a wedding | chill / none |
| 5479 | robe | A robe and a "tiny" wardrobe. (29) | A robe and a "tiny" kitchen. (28) | a long satin robe | a hotel spa robe | ironic / understatement |

## Tokens

- Subagent tokens (writers, verifiers, retries): 5,105,907. The orchestrating session is not included in this figure.
- Per slice, cumulative:

| slice / step group | tokens | cumulative |
|---|---|---|
| s01 | 279,590 | 279,590 |
| s02 | 234,220 | 513,810 |
| s05 | 161,257 | 675,067 |
| s06 | 169,453 | 844,520 |
| s04 | 163,912 | 1,008,432 |
| s03 | 240,389 | 1,248,821 |
| s01+s04+s05+s06 | 69,703 | 1,318,524 |
| s07 | 158,381 | 1,476,905 |
| s08 | 171,631 | 1,648,536 |
| s09 | 176,011 | 1,824,547 |
| s07+s08 | 56,299 | 1,880,846 |
| s11 | 179,183 | 2,060,029 |
| s10 | 180,060 | 2,240,089 |
| s13 | 163,318 | 2,403,407 |
| s09+s11 | 56,144 | 2,459,551 |
| s12 | 173,084 | 2,632,635 |
| s14 | 172,660 | 2,805,295 |
| s10+s13 | 55,314 | 2,860,609 |
| s16 | 171,773 | 3,032,382 |
| s15 | 181,129 | 3,213,511 |
| s12+s14+s16 | 61,075 | 3,274,586 |
| s17 | 180,896 | 3,455,482 |
| s18 | 172,553 | 3,628,035 |
| s19 | 167,240 | 3,795,275 |
| s20 | 169,257 | 3,964,532 |
| s15+s17 | 56,213 | 4,020,745 |
| s21 | 170,843 | 4,191,588 |
| s18+s19 | 52,501 | 4,244,089 |
| s23 | 161,631 | 4,405,720 |
| s22 | 166,217 | 4,571,937 |
| s20+s21 | 61,362 | 4,633,299 |
| s24 | 170,644 | 4,803,943 |
| s22+s23+s24 | 63,536 | 4,867,479 |
| s25 | 238,428 | 5,105,907 |

## What remains

- 6 media have no stored texts: they failed the verifier twice (rewritten once, rejected again). Resume: `python3 pipeline.py retry_in <slice>` is already built for them; a fresh writer + verifier pass on these ids, then `bash write_slice.sh <slice>`.

| id | slice | word | round-1 reasons | round-2 reasons |
|---|---|---|---|---|
| 277 | s05 | exercise | false_sentence_unclear fs: 'does homework every day' not contradicted by the media | false_sentence_true fs: every day implies every week, so FALSE is logically true |
| 302 | s02 | flour | tone, translatability ts gossip not visible; fp flour/flowers homophone | false_sentence_unclear fs: sugar vs flour not visible at a glance |
| 1424 | s08 | colleague | false_sentence_unclear fs: 'his colleague' is ambiguous, the young man's colleague IS sitting from the other view | other ts/fs: 'old colleague' reads as long-time/former colleague; age label, use 'older man' |
| 2500 | s07 | laptop | not_true ts/fs: yes/no question, not a true/false statement | not_true ts: walls of glowing code also light the room, laptop not the only light |
| 4909 | s10 | famous | not_true, grammar ts 'famous on the lamppost' unnatural, not the definition sense | tense ts/fs: filming is happening now, needs 'People are filming her' |
| 5119 | s03 | entrance | tense ts: 'The entrance opens' ongoing | false_sentence_unclear fs: entrance vs exit not visible at a glance |

- Translations into the 8 other languages (decision 120) are not started.
- The app still reads Tinder sentences from the grammar exercises; switching it to `tinder_sentences` is app work (no app code was touched here).
- 4870 (foam): the stored definition is foam on waves, the media shows shaving foam; the texts follow the media. The concept's definition should be corrected.

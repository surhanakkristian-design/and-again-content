# Phase 1f — human-judgement pass (notes for the report writer)

Judged: the 18 wrong-set items that are accepted in at least one of the 32 flag×prompt rows and carry
no Phase 1e judgement (union over all 32 rows). Written to `judgements_1f.json`.
**17 real / 1 not real.** Verdict rule used: the Slovak is the ground truth; an answer that omits a
content element of the Slovak, or swaps the subject the Slovak verb ending fixes, is not an acceptable
translation — strict, doubt resolved as "real".

Effect on the headline rows (script counts real/105):

| row | raw FA | real before (unjudged = real) | real after this file | % of 105 | ≤ 2 % candidate? |
|---|---|---|---|---|---|
| all four × P-B | 15 | 7 | **6** | 5.7 % | no |
| all four × P-C | 17 | 9 | **8** | 7.6 % | no |
| F1+F2 × P-B | 24 | 15 | **14** | 13.3 % | no |

Only `W:3603:1489926651` flips to not-real, so no row moves near 2 %. Reported as fact, not tuned.

## a. Wrong-set items still accepted

Type key: T tense, W wrong word, M missing/deleted content, S wrong subject.
"src" = judgement source: **1e** = frozen `fa_class` (tip-accept / valid reading, counted not-real by
`NOT_REAL_FA_CLASSES`), **1f** = this pass. Model column: verdict of the L3 call, or `—` when the item
was accepted before the model layer (L1 checker-accept / veto dropped by F1-F2).

### (i) all four × P-B — 15 raw / 6 real

| item_id | T | sk | reference | answer | model | raw/real | src | reason |
|---|---|---|---|---|---|---|---|---|
| W:3603:1489926651 | W | Inžinier sa ho spýtal, kedy privezie pretekárske auto späť do garáže. | The engineer asked him when he was bringing the race car back into the garage. | …when he was **taking** the race car back into the garage. | — | raw | 1f | not real: "take it back to the garage" is an ordinary rendering of *privezie späť*; reported-speech backshift intact |
| W:4612:586139873 | M | Keby skrutkovač držal on, tá polica by už dávno bola na zemi. | …that shelf would be on the floor **by now**. | …that shelf would be on the floor. | — | REAL | 1f | drops *už dávno*, the time reference that carries the counterfactual |
| W:9907:325819033 | M | Keby si bola vzala béžovú bundu, tento **look** by nikdy nevznikol. | …this **look** would never have happened. | …this would never have happened. | — | REAL | 1f | drops the subject noun of the result clause |
| W:11348:2987233244 | M | Pozri! Asistent práve drží odrazovú dosku **hore**. | Look! The assistant is holding the reflector **up now**. | Look! The assistant is holding the reflector. | — | REAL | 1f | drops *hore* and *práve* |
| W:1452:1471817457 | W | Ak sa **dotkne** toho kaktusa… | If he **touches** that cactus… | If he **grabs** that cactus… | — | REAL | 1f | grabbing ≠ touching, different event in the conditional |
| W:7238:1943930546 | M | …nohy ti zostanú **úplne** suché. | …your feet stay **completely** dry. | …your feet stay dry. | — | REAL | 1f | intensifier omitted |
| W:8824:1740944184 | M | Kým sa reťaz kývala, dotlačil vrece **na miesto**. | …he pushed the bag **into place**. | …he pushed the bag. | — | REAL | 1f | result of *dotlačil* gone |
| W:16403:624976382 | M | Rozlúč sa a o hodinu sa vráti naspäť. | …and she **will come** back in an hour. | …and she **comes** back in an hour. | — | raw | 1e (tip-accept) | see "disagreement" below |
| W:1018:1251085634 | T | Smoothie prelial…, takže mixér je prázdny. | He **has poured**… | He **poured**… | — | raw | 1e (tip-accept) | |
| W:14266:664063167 | T | Čo tancujú? — Salsu. | What **do they dance**? — Salsa. | What **are they dancing**? — Salsa. | — | raw | 1e (valid reading) | |
| W:1452:3166274700 | S | Ak sa dotkne toho kaktusa… | If **he** touches… | If **she** touches…her finger. | — | raw | 1e (valid reading) | agree: Slovak 3sg has no gender here |
| W:5595:3623849236 | T | Konečne dokument opečiatkoval… | He **has stamped**…at last | He **stamped**…at last | — | raw | 1e (tip-accept) | |
| W:9244:3038274947 | T | Kým sa vlny valili… | While the waves **were rolling in**… | While the waves **rolled in**… | — | raw | 1e (tip-accept) | |
| W:8824:241327957 | T | Kým sa reťaz kývala… | While the chain **was swinging**… | While the chain **swung**… | — | raw | 1e (tip-accept) | |
| W:10366:3357618811 | T | Do desiatej už **bude zohrievať** rezance dve hodiny v kuse. | …he **will have been reheating**… | …he **will have reheated**… | — | raw | 1e (tip-accept) | see "disagreement" |

(The ninth 1e not-real item, `W:5595:1942575047` "He has stamped the document" — *konečne* dropped — is
killed by F3 in this row, which is why 15 and not 16 raw.)

### (ii) all four × P-C — 17 raw / 8 real
Same 15 as above **plus**:

| item_id | T | sk | reference | answer | model | raw/real | src | reason |
|---|---|---|---|---|---|---|---|---|
| W:14266:2043261128 | M | Čo tancujú? — **Salsu**. | What do they dance? — **Salsa**. | What do they dance? | DIFF at P-B, accepted at P-C | REAL | 1f | the short answer is untranslated |
| W:10366:36005249 | S | Do desiatej už bude zohrievať rezance… | By ten **he** will have been reheating… | By ten **they** will have been reheating… | DIFF at P-B, SAME at P-C | REAL | 1f | *bude* is singular; *they* is impossible |

P-C's "judge against the Slovak, not the reference" line is what loosens these two: it buys +5 correct
answers and pays with exactly these 2 real false acceptances.

### (iii) F1+F2 × P-B — 24 raw / 14 real
All nine 1e not-real items + the 15 1f-judged ones: the 7 from (i) plus
`W:11980:982093953` (M, drops *chvíľu*), `W:1452:2457679986` (M, drops *z prsta*),
`W:9244:3534999071` (M, drops *ani fúzom*), `W:4571:2387652990` (M, drops *celá*),
`W:4571:4142535241` (S, *I* for *you*), `W:3494:2082147100` (M, drops *s prázdnymi vreckami*),
`W:3494:4150910632` (S, *they* for *she*), `W:8209:2200603079` (M, drops *v štúdiu*) — all REAL (1f).
These 9 are precisely what F3+F4 remove, hence 24/14 → 15/6.

### Why the offline guards missed the remaining real FAs (all four × P-B)

| item | guard that should own it | why it did not fire |
|---|---|---|
| W:4612:586139873 | F3 deletion | the deleted tokens *by now* are both in the function/adverb table, so the deletion is not a content-word deletion by F3's test |
| W:11348:2987233244 | F3 deletion | deleted *up* (particle) + *now* (adverb) — again function-class only |
| W:7238:1943930546 | F3 deletion | deleted *completely* is in the ADVERBS table, i.e. function class |
| W:9907:325819033 | F3 deletion | content noun *look* deleted mid-sentence, the determiner *this* survives; the surviving determiner keeps the pattern out of F3's trailing-content-deletion shape |
| W:8824:1740944184 | F3 deletion | *into place* deleted at the tail and *place* is a content word, so this looks like an F3 gap worth re-reading in code (real deletion, still accepted) |
| W:1452:1471817457 | none | lexical substitution *touches → grabs*: no deletion, no subject change; an offline guard would need a content-verb-substitution test, which F1/F2 deliberately allow (different-verb paraphrase is the main F1/F2 gain) |
| plus at P-C: W:14266:2043261128 | F3 deletion | the missing chunk is a whole second unit after the dash, not a token deletion inside one sentence |
| plus at P-C: W:10366:36005249 | F4 subject | the Slovak drops the pronoun (person/number only in *bude*), so F4 could not confidently determine the subject and abstained |

## b. Correct-set items still REJECTED

All four × P-B rejects **21/235**; all four × P-C rejects **16/235** (the 5 marked P-C-RESCUE).
No item is lost by P-C (P-C-only rejects: none).

| item_id | lvl | killed by | P-C | sk | reference | answer | judgement |
|---|---|---|---|---|---|---|---|
| C:16261:2683737001 | A2 | model DIFF | — | Má plán. Chystá sa odprevadiť ju domov. | He has a plan. He is going to walk her home. | She's got a plan. She is going to accompany her home. | defensible: learner makes the walker female and then *her* has no distinct referent |
| C:16403:2761099319 | A2 | model DIFF | — | Rozlúč sa a o hodinu sa vráti naspäť. | Say bye now and she will come back in an hour. | Say goodbye - he will return in an hour. | defensible: *o hodinu* (in an hour) dropped |
| C:21124:681157260 | A2 | model DIFF | RESCUE | Zvyčajne ostáva pod strechou, ale dnes tancuje v daždi. | She usually stays dry, but today she is dancing in the rain. | He usually stays under the roof, but today he is dancing in the rain. | true miss: closer to the Slovak than the reference is |
| C:23669:2842578131 | A1 | L2 veto kept (lock *above*) | — | Galaxia sa pomaly pohybuje nad ich hlavami. | The galaxy moves slowly above their heads. | The galaxy is moving slowly over their heads. | true miss on wording, defensible on aspect: *over* is fine, present continuous for a habitual/stative reading is the questionable part |
| C:26084:1225655220 | A1 | model DIFF | — | Dokáže ju nájsť skôr, než príde domov. | He can find her before she gets home. | He can find her before he gets home. | defensible: subject of the *before* clause changed |
| C:26084:2889436188 | A1 | L2 veto kept (lock *can*) | — | Dokáže ju nájsť… | He can find her before she gets home. | He is able to find her before he arrives home. | defensible: *be able to* avoids the practised *can*, plus the same subject slip |
| C:26084:3073504942 | A1 | model DIFF | — | Dokáže ju nájsť… | He can find her before she gets home. | He can find it before he comes home. | defensible: *ju* is feminine animate, *it* is wrong |
| C:27628:2910266109 | A1 | model DIFF | RESCUE | Deti sa zobudia o siedmej ráno. | The children awake at seven in the morning. | The children will wake up at seven o'clock in the morning. | true miss: *zobudia sa* is perfective, future reading is licensed |
| C:27628:3492027817 | A1 | model DIFF | — | Deti sa zobudia o siedmej ráno. | The children awake at seven in the morning. | The children will wake up at seven in the morning. | true miss, and it is the *same* answer as the rescued one minus "o'clock" — P-C rescues one and not the other, i.e. model noise |
| C:29691:2402977996 | A1 | model DIFF | — | Pustí svojho sprievodcu na kostolné schody! | He drops his guidebook on the church steps! | He's going to drop his guide on the church steps! | defensible: *going to* is a prediction, the item practises the dramatic present |
| C:29691:455389026 | A1 | model DIFF | RESCUE | (same) | He drops his guidebook… | He will drop his guidebook on the church steps! | true miss: *pustí* is perfective present = future |
| C:5595:3589927967 | B1 | L2 veto kept (lock *has stamped*) | — | Konečne dokument opečiatkoval, takže môže ísť domov. | He has stamped the document at last, so she can finally go home. | He has finally stamped the document, so he can go home. | true miss: the present perfect is there; the lock string *has stamped* is broken only by the inserted *finally* |
| C:5595:3701842021 | B1 | L2 veto kept (lock *has stamped*) | — | (same) | (same) | He has finally put a stamp on the document, so he can go home. | true miss on grammar (present perfect present), defensible on lexis (*put a stamp on* is a paraphrase of the practised verb) |
| C:5959:1797630685 | B1 | L2 veto kept (lock *will drop*) | RESCUE | Ak prsteň otočí ešte raz, zníži cenu znova. | If he turns the ring once more, she will drop the price again. | If he turns the ring once more, he will lower the price again. | true miss: first conditional intact, *lower* = *zníži* |
| C:5959:378048785 | B1 | L2 veto kept (lock *will drop*) | — | (same) | (same) | If he turns the ring again, he will reduce the price once more. | true miss: same structure, only synonyms differ |
| C:7558:2926388663 | B2 | L2 veto kept (mistake-library: auxiliary tense) | — | Nikdy predtým sme nevideli takú tichú skupinu pri západe slnka. | Never had we seen a group this quiet at sunset. | Never before have we seen such a quiet group at sunset. | defensible-to-true-miss: inversion is practised and present; the perfect vs past perfect choice is acceptable for a bare Slovak past, so the library rule is too hard here |
| C:8293:1872525904 | B1 | model DIFF | RESCUE | Jedlo nikdy nedelí, takže tento croissant musí byť výnimočný. | She never shares food, so this one must be special. | He never shares food, so this particular croissant must be exceptional. | true miss: the Slovak gives no gender; the answer is nearer the Slovak (*croissant*) than the reference |
| C:9244:3137708535 | B1 | L2 veto kept (lock *were rolling*) | — | Kým sa vlny valili… | While the waves were rolling in, the black cat did not move a whisker. | While the waves rolled in, the black cat didn't move a single whisker. | defensible: the practised past continuous is genuinely replaced by a past simple |
| C:9498:3533979063 | B1 | **F4** | — | Pult, za ktorým stojí, je starší než celá škola. | The podium that she is standing behind is older than the school. | The counter he is standing behind is older than the whole school. | true miss: Slovak *stojí* is 3sg with no gender, *he* is legitimate → F4 is wrong here |
| C:9498:362699013 | B1 | **F4** | — | (same) | (same) | The counter that he's standing behind is older than the whole school. | true miss, same reason (this is also the only `lost_correct` vs the F1+F2 row) |
| C:9498:582627860 | B1 | **F4** | — | (same) | (same) | The counter he stands behind is older than the entire school. | defensible on aspect (*stands* for the practised continuous), but the F4 kill is for the wrong reason (gender) |

Pattern: 7 of the 21 are L2 vetoes F1/F2 kept (all of them lock-string or mistake-library artefacts on
answers whose grammar is actually present), 11 are model DIFF at L3, 3 are F4. The A1 *perfective
present → will* family (C:27628, C:29691) is the single biggest true-miss cluster and P-C only half-fixes
it, which is model noise rather than a rule difference.

## c. What F3 and F4 cost on the 235

**F3 (deletion guard): cost on the 235 = 0.** No correct item is rejected by F3 in any row
(`f3_f4_offline.F3.cost_on_235.total = 0`; `layers_correct` for the all-four rows contains no F3 bucket).
Its gain: 14 wrong-set kills, 7 of which were being accepted
(W:11980:982093953, W:1452:2457679986, W:5595:1942575047, W:9244:3534999071, W:4571:2387652990,
W:3494:2082147100, W:8209:2200603079 — all M, all real by this pass except W:5595:1942575047 which 1e
had already classed "valid reading"). Verdict: F3 is free and its only questionable kill is the one item
1e considered acceptable.

**F4 (subject guard): cost on the 235 = 3, all three wrong kills, all one exercise.**

| item | answer vs reference | kill wrong? |
|---|---|---|
| C:9498:3533979063 | *he is standing behind* vs *she is standing behind* | yes — Slovak *za ktorým stojí* marks 3sg only, no gender; F4's claim that the Slovak fixes "3/sg/f" is read off the English reference, not the Slovak |
| C:9498:362699013 | *that he's standing behind* vs *that she is standing behind* | yes — same |
| C:9498:582627860 | *he stands behind* vs *she is standing behind* | kill is wrong for the gender reason; the answer is separately weak (simple for continuous) |

F4's gain: 13 S-type kills, 2 of which were being accepted (W:4571:4142535241 *I* for *you*,
W:3494:4150910632 *they* for *she*) — both real. So F4 trades 2 real FA saves for 3 wrong rejections and
is net-negative on this sample as implemented; its abstention logic must read person/number/gender off
the Slovak verb morphology, never off the reference pronoun.

## d. Five lines: what the remaining real FAs share, and the one rule to test next

1. Eleven of the 14 real FAs in the F1+F2 row and 5 of the 6 in the all-four row are **omissions of a
   single adjunct** (*by now, up, completely, into place, a minute, at the studio, with empty pockets*) —
   the learner's answer is a strict subsequence of a correct translation, so every semantic layer reads it
   as "same, just shorter".
2. F3 misses them almost exclusively because the omitted token is in the function/adverb table
   (*by, now, up, completely*), i.e. the guard's content-word test, not its subsequence test, is the leak.
3. The S-type leak is a different shape: subjectless Slovak clauses where person/number lives in the verb
   ending (*bude*, *hádzala*), so F4 abstains and the model shrugs.
4. The W-type leak (*touches → grabs*) is the price of F1/F2 allowing different-verb paraphrase and cannot
   be closed offline without also re-breaking the 38 gains.
5. Worth testing next (describe only): an **adjunct-deletion rule** — if the normalised answer is a pure
   subsequence of the reference and the deleted span contains any token carrying the sentence's stated
   time / place / manner / measure information (including function-class adverbs and particles such as
   *by now, up, completely, into place*, and any dropped clause after a dash), reject regardless of word
   class; pair it with an F4 variant that derives person/number/gender from the Slovak verb ending and
   stays silent when the ending is ambiguous.

# Review task §4.3 — 10 % annotation sample (8 sentences)
[STEP: review-sample] One read (this file), one write: `phase1c/review/sample.json` (under ~/Projects/and-again-content/translation-offline/).
Budget: no other reads, no tools besides the one Write.

## What to do
For each sentence check the full annotation against the Slovak: missing or wrong variants (a correct learner answer the checker would
reject), wrong locks, missing/wrong gender (`g` only when the Slovak does not fix gender), determiner freedom (`d` only where the Slovak has
no article/demonstrative), optional words, synonym anchors (wrong group = false acceptance), and whether the `m` mistakes are real and
correctly placed. Output ann changes (or syn changes when a group is wrong). Sampling: seed 20260920, stratified by batch and level
(2 from S, 6 from L; id 103 excluded — its Slovak does not match).

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

## Units (8 sentences: 7716, 25921, 25981, 13034, 8293, 2955, 119, 7037)


### 7716 [S B1] topic Gerund vs Infinitive — answer span “to stay”
EN: She managed to stay completely still until the dragonfly settled.
SK: Podarilo sa jej vydržať úplne nehybne, kým sa vážka usadila.
annotation: {"id": 7716, "t": 47, "lv": "B1", "v": ["She managed to stay completely still until the dragonfly settled."], "lk": ["to stay"], "s": {"completely": "ng1c_18", "still": "still_motionless", "settled": "ng1c_19"}, "m": [["47.03", "staying"], ["47.04", "stay"], ["47.05", "to stayed"], ["47.12", "=She succeeded to stay completely still until the dragonfly settled."], ["47.15", "=She was able to stay completely still until the dragonfly settled."], ["47.17", "didn't settle", "settled"]], "alt": {"completely": ["totally", "perfectly"], "still": ["motionless"], "settled": ["landed", "settled down"]}}
synonym groups (members): {"ng1c_18": ["completely", "totally", "perfectly"], "still_motionless": ["still", "motionless"], "ng1c_19": ["settle", "land", "settle down"]}
mistake items used (kind / verdict): {"47.03": "gerund after to-verb / wrong", "47.04": "missing to / wrong", "47.05": "past form after to / wrong", "47.12": "succeed plus to / wrong", "47.15": "was able instead of managed / correct_with_tip", "47.17": "negative after until / wrong"}

### 25921 [S A1] topic A, AN, THE — answer span “a volcano”
EN: They watch a volcano from the grassy ridge.
SK: Z trávnatého hrebeňa pozorujú sopku
annotation: {"id": 25921, "t": 6, "lv": "A1", "v": ["They watch a volcano from the grassy ridge.", "From the grassy ridge they watch a volcano."], "lk": ["a volcano", "a volcano"], "s": {"watch": "observe_watch", "grassy": "ng1c_6", "ridge": "ng1c_7"}, "d": {"the": "the|a"}, "m": [["6.01", "volcano"], ["6.03", "an volcano"], ["6.20", "look", "watch"], ["6.19", "of", "from"], ["6.02", "=They watch a volcano from grassy ridge."]], "alt": {"watch": ["observe"], "grassy": ["grass-covered"], "ridge": ["crest"]}}
synonym groups (members): {"observe_watch": ["watch", "observe"], "ng1c_6": ["grassy", "grass-covered"], "ng1c_7": ["ridge", "crest"]}
mistake items used (kind / verdict): {"6.01": "missing a / wrong", "6.03": "a/an mixed up / wrong", "6.20": "wrong word / wrong", "6.19": "wrong preposition / wrong", "6.02": "missing the / wrong"}

### 25981 [L A1] topic Cardinal numbers — answer span “ten”
EN: The waiter carries ten hot plates at once.
SK: Čašník nesie naraz desať horúcich tanierov.
annotation: {"id": 25981, "t": 11, "lv": "A1", "v": ["The waiter carries ten hot plates at once."], "lk": ["ten"], "s": {"carries": "ng1c_35", "at once": "ng1c_36"}, "m": [["11.03", "tenth"], ["11.01", "plate", "plates"], ["11.14", "carry", "carries"], ["11.13", "hots", "hot"], ["11.09", "ten of"], ["11.15", "=The waiter carries at once ten hot plates."]], "alt": {"carries": ["is carrying"], "at once": ["at the same time", "at one time"]}}
synonym groups (members): {"ng1c_35": ["carries", "is carrying"], "ng1c_36": ["at once", "at the same time", "at one time"]}
mistake items used (kind / verdict): {"11.03": "ordinal instead of cardinal / wrong", "11.01": "singular after a number / wrong", "11.14": "missing 3rd person -s / wrong", "11.13": "-s on adjective / wrong", "11.09": "of after a number / wrong", "11.15": "unusual word order / correct_with_tip"}

### 13034 [L A2] topic Present Continuous — answer span “is blowing”
EN: Right now the girl is blowing out the candles.
SK: Práve teraz dievča sfukuje sviečky.
annotation: {"id": 13034, "t": 14, "lv": "A2", "v": ["Right now the girl is blowing out the candles.", "Right now the girl is blowing the candles out.", "The girl is blowing out the candles right now."], "lk": ["is blowing", "is blowing", "is blowing"], "s": {"Right now": "ng1c_39"}, "m": [["14.01", "blows"], ["14.02", "blowing"], ["14.03", "is blow"], ["14.06", "was blowing"], ["14.15", "girl", "the girl"], ["14.12", "=Right now the girl is blowing the candles."]], "alt": {"Right now": ["At the moment", "Just now"]}}
synonym groups (members): {"ng1c_39": ["right now", "at the moment", "just now"]}
mistake items used (kind / verdict): {"14.01": "Present Simple instead of Present Continuous / wrong", "14.02": "missing is / wrong", "14.03": "missing -ing / wrong", "14.06": "Past Continuous instead of Present Continuous / wrong", "14.15": "missing article / wrong", "14.12": "missing small word / wrong"}

### 8293 [L B1] topic Modal verbs Probability — answer span “must”
EN: She never shares food, so this one must be special.
SK: Jedlo nikdy nedelí, takže tento croissant musí byť výnimočný.
annotation: {"id": 8293, "t": 43, "lv": "B1", "v": ["She never shares food, so this one must be special."], "lk": ["must"], "s": {"this one": "ng1c_84", "special": "special_exceptional", "shares": "share_split"}, "g": [["She"]], "m": [["43.01", "can"], ["43.02", "=She never shares food, so this one must is special."], ["43.14", "share", "shares"], ["43.05", "=She never shares food, so this one is special."], ["43.03", "has to"], ["43.15", "=She never doesn't share food, so this one must be special."]], "alt": {"this one": ["this croissant"], "special": ["exceptional"], "shares": ["splits"]}}
synonym groups (members): {"ng1c_84": ["this one", "this croissant"], "special_exceptional": ["special", "exceptional"], "share_split": ["share", "split"]}
mistake items used (kind / verdict): {"43.01": "possibility instead of certainty / wrong", "43.02": "must plus to or is / wrong", "43.14": "missing third person -s / wrong", "43.05": "no modal, meaning lost / wrong", "43.03": "has to instead of must / correct_with_tip", "43.15": "double negation / wrong"}

### 2955 [L B2 long] topic Wish clauses — answer span “had turned”
EN: The guard wishes he had turned the camera towards the horizon a minute earlier.
SK: Strážnik ľutuje - kiežby bol otočil kameru k obzoru o minútu skôr.
annotation: {"id": 2955, "t": 60, "lv": "B2", "v": ["The guard wishes he had turned the camera towards the horizon a minute earlier."], "lk": ["had turned"], "s": {"guard": "ng1c_87", "towards": "ng1c_88", "a minute earlier": "ng1c_89"}, "m": [["60.08", "turned"], ["60.09", "would have turned"], ["60.14", "=The guard wish he had turned the camera towards the horizon a minute earlier."], ["60.03", "will turn"]], "alt": {"guard": ["security guard", "watchman"], "towards": ["toward", "to", "at"], "a minute earlier": ["a minute sooner"]}}
synonym groups (members): {"ng1c_87": ["guard", "security guard", "watchman"], "ng1c_88": ["towards", "toward", "to", "at"], "ng1c_89": ["a minute earlier", "a minute sooner"]}
mistake items used (kind / verdict): {"60.08": "Past Simple for past regret / wrong", "60.09": "would have for past regret / wrong", "60.14": "missing -s on wishes / wrong", "60.03": "will instead of would / wrong"}

### 119 [L B1] topic Present Perfect Continuous — answer span “has she been tapping”
EN: How long has she been tapping that keycard on the wrong door?
SK: Ako dlho prikladá tou kartou na nesprávne dvere?
annotation: {"id": 119, "t": 32, "lv": "B1", "v": ["How long has she been tapping that keycard on the wrong door?"], "lk": ["has she been tapping"], "s": {"keycard": "ng1c_78", "on": "ng1c_79", "wrong": "wrong_incorrect"}, "m": [["32.01", "does she tap"], ["32.02", "is she tapping"], ["32.12", "=How long she has been tapping that keycard on the wrong door?"], ["32.05", "has she tapping"], ["32.06", "has she been tap"], ["32.08", "is she been tapping"], ["32.07", "have she been tapping"]], "alt": {"keycard": ["card", "key card"], "on": ["against", "to"], "wrong": ["incorrect"]}}
synonym groups (members): {"ng1c_78": ["keycard", "card", "key card"], "ng1c_79": ["on", "against", "to"], "wrong_incorrect": ["wrong", "incorrect"]}
mistake items used (kind / verdict): {"32.01": "Present Simple instead of PPC / wrong", "32.02": "Present Continuous instead of PPC / wrong", "32.12": "statement word order in question / wrong", "32.05": "missing been / wrong", "32.06": "no -ing after been / wrong", "32.08": "is/was instead of has / wrong", "32.07": "have/has agreement / wrong"}

### 7037 [L B2] topic Relative clauses — answer span “whose”
EN: The stag, whose antlers were huge, stood among the leaves.
SK: Jeleň, ktorého parohy boli obrovské, stál medzi lístím.
annotation: {"id": 7037, "t": 61, "lv": "B2", "v": ["The stag, whose antlers were huge, stood among the leaves."], "lk": ["whose"], "s": {"stag": "stag_deer", "huge": "huge_gigantic", "leaves": "ng1c_95"}, "m": [["61.01", "which"], ["61.02", "who"], ["61.03", "whose his"], ["61.04", "whose the"], ["61.05", "=The stag, its antlers were huge, stood among the leaves."], ["61.20", "=The stag, which had huge antlers, stood among the leaves."], ["61.19", "=The stag with huge antlers stood among the leaves."]], "alt": {"stag": ["deer"], "huge": ["enormous", "massive"], "leaves": ["foliage"]}}
synonym groups (members): {"stag_deer": ["stag", "deer"], "huge_gigantic": ["huge", "enormous", "gigantic", "giant", "massive", "vast"], "ng1c_95": ["leaves", "foliage"]}
mistake items used (kind / verdict): {"61.01": "which instead of whose / wrong", "61.02": "who instead of whose / wrong", "61.03": "double possessive / wrong", "61.04": "article after whose / wrong", "61.05": "pronoun instead of relative / wrong", "61.20": "which had instead of whose / correct_with_tip", "61.19": "avoids the relative clause / correct_with_tip"}

Write the JSON to `phase1c/review/sample.json` now. "unchanged" counts SENTENCES needing no change.

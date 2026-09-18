# Review task §4.1 — synonym groups used or proposed by the 80 Phase 1c sentences
[STEP: review-syn] One read (this file), one write: `phase1c/review/syn_2.json` (under ~/Projects/and-again-content/translation-offline/).
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

**Part 2 of 2** — review only the units in this file; write `phase1c/review/syn_2.json`.

- {"id": "ng1c_100", "pos": "x", "m": ["another", "one more"], "anchor": "another"}
  sentence(s): 3937 [L B2] EN: She will buy another charm when she comes to this market again. | SK: Kúpi si ďalší prívesok, keď príde na tento trh znova.
  annotator alt: {"3937": {"another": ["one more"], "charm": ["pendant"]}}
- {"id": "ng1c_101", "pos": "x", "m": ["faces", "looks towards", "faces towards", "is turned towards"], "anchor": "faces"}
  nearest existing group: {"id": "face_expression", "kind": "contextual", "pos": "n", "m": ["face", "expression"], "ok": "Did you see his face? = Did you see his expression?", "bad": "She faced the problem. ≠ She expressed the problem."}
  sentence(s): 7998 [L B2] EN: The veranda, where she now spends every morning, faces the sunrise. | SK: Veranda, na ktorej teraz trávi každé ráno, je otočená na východ slnka.
  annotator alt: {"7998": {"veranda": ["porch"], "faces": ["looks towards", "faces towards", "is turned towards"], "the sunrise": ["the east", "the rising sun"]}}
- {"id": "ng1c_102", "pos": "x", "m": ["the sunrise", "the east", "the rising sun"], "anchor": "the sunrise"}
  sentence(s): 7998 [L B2] EN: The veranda, where she now spends every morning, faces the sunrise. | SK: Veranda, na ktorej teraz trávi každé ráno, je otočená na východ slnka.
  annotator alt: {"7998": {"veranda": ["porch"], "faces": ["looks towards", "faces towards", "is turned towards"], "the sunrise": ["the east", "the rising sun"]}}
- {"id": "ng1c_103", "pos": "n", "m": ["right", "good"], "anchor": "right"}
  nearest existing group: {"id": "right_correct", "kind": "contextual", "pos": "x", "m": ["right", "correct"], "ok": "That's the right answer. = That's the correct answer.", "bad": "Turn right at the lights. ≠ Turn correct at the lights."}
  sentence(s): 10574 [L B2] EN: He had been training for hours before the light was finally right. | SK: Trénoval hodiny, kým bolo svetlo konečne správne.
  annotator alt: {"10574": {"before": ["until"], "right": ["good"]}}
- {"id": "ng1c_104", "pos": "x", "m": ["glows", "shines", "is glowing", "is shining", "is on"], "anchor": "glows"}
  nearest existing group: {"id": "glow_shine", "kind": "contextual", "pos": "v", "m": ["glow", "shine"], "ok": "The laptop screen is glowing. = The laptop screen is shining.", "bad": "She shines at maths. ≠ She glows at maths."}
  sentence(s): 9038 [L B2] EN: Right now he is scribbling a note while the laptop screen glows. | SK: Práve teraz čmára poznámku, kým obrazovka notebooku svieti.
  annotator alt: {"9038": {"glows": ["shines", "is glowing", "is shining", "is on"]}}
- {"id": "ng1c_105", "pos": "x", "m": ["felt watched", "felt that someone was watching her", "felt like someone was watching her", "felt she was being watched"], "anchor": "felt watched"}
  sentence(s): 10107 [L B2] EN: The terminal was empty; even so, she felt watched. | SK: Terminál bol prázdny; aj tak mala pocit, že ju niekto sleduje.
  annotator alt: {"10107": {"empty": ["deserted"], "felt watched": ["felt that someone was watching her", "felt like someone was watching her", "felt she was being watched"]}}
- {"id": "ng1c_106", "pos": "x", "m": ["last summer", "last year"], "anchor": "last summer"}
  sentence(s): 9913 [L B2] EN: She had her boots dyed purple last summer. | SK: Vlani si dala čižmy zafarbiť na fialovo.
  annotator alt: {"9913": {"last summer": ["last year"]}}
- {"id": "ng1c_107", "pos": "a", "m": ["early", "soon"], "anchor": "earlier"}
  sentence(s): 6884 [L B2] EN: If he had started earlier, he would have missed the mist. | SK: Keby vyrazil skôr, hmlu by bol minul.
  annotator alt: {"6884": {"earlier": ["sooner"], "missed": ["avoided"]}}
- {"id": "ng1c_108", "pos": "v", "m": ["miss", "avoid"], "anchor": "missed"}
  sentence(s): 6884 [L B2] EN: If he had started earlier, he would have missed the mist. | SK: Keby vyrazil skôr, hmlu by bol minul.
  annotator alt: {"6884": {"earlier": ["sooner"], "missed": ["avoided"]}}

Write the JSON to `phase1c/review/syn_2.json` now. "unchanged" counts groups left as they are.

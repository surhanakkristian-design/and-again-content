# A32 second look on the Body Parts lists

The Body Parts group has 36 videos (16 at level A, 20 at level B), fewer than the 40 of the brief, so the
second look covered ALL of them, not a sample. A separate agent got only `packets/bp_audit_in.json`
(video, key word, description, transcript, candidate words) and judged every word ok / doubt / fit.

Result: 1,117 judgments: 1,107 ok, 10 doubt, 0 fit. All 10 doubts were removed.

| media | key word | removed word | why (second reviewer) |
|---|---|---|---|
| 94 | blink | dive (3102) | A shabby diner or bar is called a dive in everyday English, and the scene is set in a diner. |
| 642 | scar | warehouse (3640) | Crates stacked on a pier suggest a dockside storage setting, so a warehouse may be in the background. |
| 4202 | belly | umbrella (2103) | A sunny patio very often has a patio umbrella that the description does not rule out. |
| 4460 | palm | pyramid (149) | The sticks are stacked as a teepee, which is a pyramid shape at the centre of the shot. |
| 4592 | foot | paddle (625) | To paddle also means to walk barefoot in shallow liquid, close to bare feet treading in grape juice. |
| 4963 | finger | corkscrew (297) | Screws lie on the floor during furniture assembly, and corkscrew contains and resembles screw. |
| 5016 | knee | train (2081) | To train means to exercise, and he drops into a deep squat. |
| 5346 | stomach | wolf (970) | To wolf (down) means to eat greedily, and he forks up a huge mouthful of spaghetti. |
| 5346 | stomach | drum (1258) | He pats his middle with both hands, which reads as drumming on his belly. |
| 7268 | joint | barbecue (192) | Joint has everyday senses tied to this word (a barbecue joint, a joint of meat). |

Patterns the second reviewer named: nouns that are also everyday verbs or slang (train, wolf, drum, paddle,
dive); shape words (pyramid for a teepee of sticks); lookalike words (corkscrew next to screws); typical
background objects the description does not rule out (umbrella on a sunny patio, warehouse near crates on a
pier); other senses of the key word (joint -> barbecue). These became rules 7-11 in `BODY_PARTS_RULES.md`.

After the removal I went over all 36 lists once more with rules 7-11 in hand and found no further case.
The lists were then cut to at most 25 words each (the brief's target), so the stored lists are a subset of
what both looks approved.

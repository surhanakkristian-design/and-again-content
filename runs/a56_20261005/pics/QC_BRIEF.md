# A56 picture QC - HARD FAILS ONLY (owner decision 370)
For each picture listed in your task: open it (Read the PNG; it is an edit of a video still), and give a verdict.
HARD FAIL (only these): (1) any text, letters, digits or number-like marks anywhere (signs, clothes, objects, sandbags, roofs);
(2) the caption is not readable at first glance (the picture does not clearly show the caption, or it would equally fit a
sibling caption named in the task; for tense captions the time - centuries ago / far future / now - must be obvious);
(3) broken anatomy or physics (extra / missing / fused fingers or limbs, duplicated person or animal, floating things, melted objects);
(4) violence, gore or gross details.
NOT a fail: a face resembling a real person, logos carried over from the source, framing differences, imperfect eyelines,
small deviations from the prompt, style differences. Tiny leftovers that a local retouch could remove (a small mark in a corner):
say "RETOUCH" with the place.
Write `qc/<task name>.json`: [{"file": "...", "caption": "...", "verdict": "PASS"|"FAIL"|"RETOUCH", "reason": "one sentence", "zoom_checked": "what you zoomed on"}]
Zoom in on hands, faces and any surface that could carry text (crop with python3 + PIL into the scratch folder you are given, then Read the crop).
Reply with one line per picture: file, verdict, reason. Nothing else.

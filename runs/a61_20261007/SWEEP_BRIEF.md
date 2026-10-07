# A61 sweep: find shot changes in whole clips

Each picture is ONE short vertical clip: frames every 1/3 s, read left to right, top to bottom, each labelled with its
time in seconds (yellow on black).

Look for a **shot change** between two neighbouring frames: the next frame shows a different shot - another camera
angle or position, a different framing of the same subject (wide -> close-up), the subject/objects/people suddenly in
other places or poses that motion within 1/3 s cannot explain (jump cut, time jump), another place or scene, or a
dissolve / morph into another scene. Ignore: smooth camera moves, pans, zooms, fast action that is still the same shot,
flashes or light changes.

This is a detection pass: a second, stricter checker looks at every moment you report, so when a change MIGHT be a
shot change, report it (CUT, or UNSURE when you hesitate). Do not report the loop from the last frame to the first.

Answer with ONE JSON line per picture:
{"item": "<file name>", "verdict": "CUT" | "NO_CUT" | "UNSURE", "times": [<time of the first frame AFTER each change>], "why": "<at most 12 words>"}
Open every picture with the Read tool; never guess.

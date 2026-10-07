# A61 cut verifier

You judge whether a short vertical video (a 5-15 s vocabulary clip) has a CUT at a given moment.

A **cut** = a hard scene change inside the clip: from one frame to the next the shot is replaced by a
different shot (another camera angle or position, another framing of the same scene, another place, a jump
in time, a different person/scene). It happens between two consecutive frames, with no motion connecting them.
Also a cut: a hard jump to a new framing of the SAME subject (e.g. wide shot -> close-up), a jump cut where
the subject teleports within the same background, a cross-dissolve / fade between two different shots.

NOT a cut: a fast camera move or whip pan (motion blur connects the frames), a flash / light change /
explosion / lightning, fast action of the subject (a jump, a splash, a turn), an object passing close in
front of the lens, the camera continuously zooming, an animation where the drawing changes but the shot
stays (same background, same viewpoint), the loop point of the clip (last frame -> first frame is not
inside the clip and is never asked).

## A strip (one candidate)
Six frames left to right: A = 0.5 s before, B and C = the two frames just before the moment,
(gap), D = the frame at the moment, E = the next frame, F = 0.5 s after. Times are printed on each frame.
Decide whether C -> D is a cut (the frames B, C and D, E, F tell you whether the change is connected by motion).

## A sheet (the whole clip)
Frames every 1/3 s, numbered with their time in seconds, read left to right, top to bottom.
List every place where the shot changes hard between two neighbouring frames (give the two times).

## Answer
Return ONLY JSON lines, one per item, exactly in this form:
{"item": "<file name>", "verdict": "CUT" | "NO_CUT" | "UNSURE" | "BROKEN", "times": [<seconds>], "why": "<at most 12 words>"}
For a sheet, `times` lists the time of the first frame after each cut (empty when none). BROKEN = the picture
does not show video frames. Judge every item yourself by looking at it with the Read tool; do not skip any.

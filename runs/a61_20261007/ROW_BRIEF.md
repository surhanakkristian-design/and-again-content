# A61 cut verifier (rows)

Each picture belongs to ONE short vertical video clip and holds 1-6 ROWS. Each row is one candidate moment:
six frames left to right, labelled `<row><letter> <time s>`:
A = 0.5 s before, B and C = the two frames just before the moment, (red bar), D = the frame at the moment,
E = the next frame, F = 0.5 s after. The question for each row: is C -> D a CUT?

**CUT** = a hard scene change: from C to D the shot is replaced by a different shot - another camera angle or
position, another framing of the same subject (wide -> close-up), the subject or objects teleport / a jump in time
(jump cut, e.g. a tutorial step skipped), another place or scene. Also a cut: a fast dissolve / morph where D already
shows a different shot than C. A cut has no motion connecting C and D (B -> C and D -> E look smooth, C -> D does not).

**NO** = the same continuous shot: fast camera move or whip pan (motion blur, the scene slides), a flash, light or
colour change, an explosion, fast action of the subject (jump, splash, turn), something passing close in front of the
lens, a smooth zoom, an animation where the drawing moves but the viewpoint stays. Look at A..F: if C -> D is just
a bigger step of a movement that also happens across A -> B -> C and D -> E -> F, it is NO.

UNSURE only when you truly cannot tell. BROKEN when the row shows no video frames.

Answer with ONE JSON line per picture, exactly:
{"item": "<file name>", "rows": {"1": "CUT"|"NO"|"UNSURE"|"BROKEN", "2": ...}, "why": "<at most 12 words about the cut rows>"}
Every row of the picture gets a verdict. Open every picture with the Read tool and look carefully; never guess.

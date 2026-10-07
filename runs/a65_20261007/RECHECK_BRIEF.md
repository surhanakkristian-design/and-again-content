# A65 naturalness RE-CHECK (owner rule 7: "unnatural items are rewritten and checked again")

You wrote none of this. Folder `~/Projects/and-again-content/runs/a65_20261007`.
Inputs: `content/source.json` (live content), `content/writer.json` (new content), `verify/natural_review.json`
(a first reviewer's rewrites `changes` and open `flags`), `NATURAL_BRIEF.md` (the rules and the mechanics every rewrite
must keep - read it). Pictures: `stills/<id>.png`, `carousel/<id>_<n>.png`, and for the videos 62, 236, 7071, 8039
one frame per second `frames/<id>_NN.png` (the tap exercise plays the VIDEO, so a thing may be visible in a later frame
even if not in the still).

Tasks:
1. For EVERY change in `natural_review.json`: is the `after` text exactly what a native US-English speaker would say,
   true to the picture, and does it keep the mechanics? Verdict `ok` or `fix` (with your better text).
2. For EVERY flag: look at the frames. Is it a real problem? If real, propose the smallest fix that keeps the
   mechanics (a phrase whose thing is visible, its noun, the matching ex4 row). If a fix needs a NEW ex2 noun, give its
   point as shares of the still (x, y from the top-left, 0-1) on a visible part of the thing, and the tap target
   (who / what does it). If a flag is not a real problem, say why.
3. Anything else in the final content (source + writer + accepted changes) that is still unnatural.

Write `verify/natural_recheck.json`:
```json
{"changes": [{"id":..., "field":"...", "verdict":"ok"|"fix", "after":"final text", "why":"..."}],
 "flags": [{"id":..., "what":"...", "real": true|false, "fix": [{"field":"...", "before":"...", "after":"...", "x":0.5, "y":0.5, "target":"the man"}] , "why":"..."}],
 "more": [{"id":..., "field":"...", "before":"...", "after":"...", "why":"..."}]}
```
No chat output; reply with one line (path + counts).

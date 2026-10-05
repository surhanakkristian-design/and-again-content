# A51 free pre-check of edit prompts (no credits are spent here)

You are the separate prompt verifier. For your word, read:
- the still (the image every picture is an EDIT of): path given below (if it is large, make a small JPEG copy with `sips -Z 900 <in> --out /private/tmp/claude-501/a51_pre/<name>.jpg -s format jpeg` and Read that),
- the rules: /Users/kristiansurhanak/Projects/and-again-content/runs/a49_20261005/pics/RULES.md (R1-R10 + decision 370),
- each prompt file listed below.

A51 rules on top: the carousel has exactly 3 pictures = 3 captions (listed below, the original still is NOT shown);
each picture must read its OWN caption at first glance and must not read as a sibling caption; at most one past,
one present, one future per word; never deliberately depict a recognisable celebrity or add a large famous brand
logo; no text/letters/digits; no broken anatomy/physics; no violence or gross details; children only in normal,
safe, everyday situations.

For every prompt: predict how Nano Banana Pro (an image EDIT model) will fail on THIS still (mirrored sides, things
that cannot fit the framing, leftover original elements that would duplicate, unclear eyelines, hands, lettering,
weak caption cue, sibling confusion, the tense not readable). Then FIX the prompt file in place (keep its structure:
keep-block, "CHANGE ONLY THIS:", Must NOT appear, Look, the strict block). Do not make it longer than needed.
Write `precheck_<id>.md` next to this file: per prompt "Before:" (problems found), "Changed:", "Remaining risk: low/medium/high".
Reply with one line per prompt: caption, remaining risk.

# A31 representatives (curator)

Each group of videos gets one representative video per level: the tile a NEW learner sees on the
Training wall for that group. Rules (the starter-wall rules):
- clear: the picture shows one strong, easy to read subject; the key word is obvious from the clip;
- attractive: bright, well composed, fun or beautiful; something a 15-25 year old would tap;
- nothing sensitive: no violence, weapons, blood, injury, illness close-ups, medical distress, death, fear or horror imagery, alcohol, smoking, drugs, gambling, nudity or sexual content, politics, religion, police / prison / arrest, disasters, crying or humiliation, anything disgusting;
- the thumbnail itself (the still the wall shows first) must look good and not be dark, blurry or mid-blink.

Each packet `packets/rep/<name>.json` has the group, the level and every candidate: `m` (media id), `word`, `desc`, `thumb` (thumbnail URL).
For each packet:
1. read all descriptions; shortlist the 5 best candidates by the rules;
2. download their thumbnails with curl into `packets/rep_thumbs/<m>.webp`; convert with `python3 -c "from PIL import Image; Image.open('X.webp').convert('RGB').save('X.jpg')"` if the Read tool cannot open webp; look at each one with the Read tool;
3. pick the best one and one runner-up.
Write `packets/rep_out/<name>.json`: {"packet": "<name>", "pick": <m>, "runner_up": <m>, "why": "<one line>", "shortlist": [m, ...], "rejected": {"<m>": "<reason>"}}.
For groups whose topic is itself delicate (Health, Stress & Fear, Law & Power, Win & Lose, Grab & Break) pick the lightest, friendliest clip (cartoon or funny is good).
Reply with one line per packet: name, pick, word.

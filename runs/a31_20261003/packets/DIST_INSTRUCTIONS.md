# A31 distractor look (one-word Tinder cards)

The app shows a short video and ONE word on top. The learner swipes right if the word fits the
video, left if not. The correct card shows the video's key word. A wrong card shows another key
word of the same group and level. A wrong word must be CLEARLY wrong for that video: a learner
(or a strict reviewer who reads the video's description) must never be able to say
"but that word fits too".

Each packet file `packets/dist/<name>.json` has:
- `words`: every key word of this group and level: `c` (concept id), `w` (word), `pos`, `d` (definition).
- `videos`: `m` (media id), `key` (concept id of its key word), `word`, `desc` (what the video shows), `said` (what is spoken).

For EVERY video decide which words of `words` must NOT be used as a wrong word for it. Exclude a word when any of these holds:
1. it is a synonym or near-synonym of the key word, or a broader / narrower word for the same thing (dog - puppy - pet - animal), or the same idea in another part of speech (cook - cooking - chef in a cooking video);
2. the thing, action, quality, feeling, place or person it names is visible, done, heard, said or clearly implied in the video (desc + said), even as a side detail;
3. it could reasonably describe the scene, mood or topic of the video as a whole (e.g. "funny", "busy", "outside", "together" when that is plainly true);
4. you are in doubt. Doubt = exclude. A too-long exclude list costs nothing; one wrong card that fits is a failure.
Keep a word (do not exclude) only when it is plainly not in the video and not about it.
Never list the video's own key concept (it is excluded anyway).

Also give `generic`: words of the list that are so broad that they fit a large share of this group's videos (e.g. "animal" in Animals, "food" in Food & Drink, "person", "thing", "do"). They will never be used as wrong words in this group and level.

Write for each packet ONE file `packets/dist_out/<name>.json` (same name), valid JSON, exactly:
{"packet": "<name>", "generic": [concept ids], "exclude": {"<media id>": [concept ids], ...}}
`exclude` must have an entry for EVERY video of the packet (an empty list is allowed only when truly nothing fits). Use only concept ids that are in the packet's `words`.
Work video by video against the whole word list; do not write a script that guesses from string matching - read and judge. After writing, re-open each output and check: valid JSON, every media id present, ids are numbers from `words`.
Reply with one line per packet: name, number of videos, average excluded words per video.

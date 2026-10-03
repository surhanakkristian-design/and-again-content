# A37: split one old group of videos into smaller topic groups (writer)

The app's Training wall shows one tile per group of vocabulary videos (learners aged 15-25). Today there are 35
broad groups; we split them into about 100 smaller ones by topic (examples: Animals -> Pets, Wildlife, Farm, Sea;
Food -> Fruit, Snacks, Drinks).

For each file `packets/split_<id>.tsv` you are given: line 1 = the old group, its video counts at level A and B, and
the target number of new groups (with the allowed range). Then one line per video: media id, level (A or B),
key word, part of speech, description of the clip (cut).

Rules
1. Every video of the file goes into exactly ONE new group. A video is placed by what its KEY WORD means and what
   the clip shows (read the description: the key word alone can mislead, e.g. "bat" the animal vs the sports bat).
2. Every new group must have at least 7 videos at level A AND at least 7 at level B (hard floor 6 and 6). Count both
   levels yourself before you finish. If a topic cannot reach that at one level, make the topic broader or merge it.
3. Number of new groups: inside the allowed range of line 1. A target of 1 means the group stays whole (still give
   it a name). Prefer groups of similar size; no group should hold more than about half of the videos unless the target is 2.
4. Topics must be clear to a teenager at a glance, distinct from each other inside the old group, and concrete
   (things / places / activities), not grammatical (never "Verbs", "Adjectives", "Other", "Misc", "More").
   The leftover videos must also sit in a group whose name truly covers them: choose the cut so that nothing is left over.
5. Name: ONE English word (no spaces, no "&", no hyphen), title case, a common word (e.g. Pets, Wildlife, Farm, Sea,
   Fruit, Snacks, Drinks, Airport, Hotel). It will be translated into 8 other languages as one word, so prefer
   concrete nouns. Do not reuse the names in `packets/taken_names.txt` unless the group is the unsplit old group of that name,
   and give 2 alternative one-word names per group (other groups elsewhere may have taken your first choice).
6. Nothing sensitive as a topic name (no Death, Drugs, Weapons, Crime as a name; Law / Safety are fine).

Output: write `out/split_<id>.json` (one file per old group), exactly:
{"old_group": <id>, "groups": [{"en": "Pets", "alt": ["Companions", "Petcare"], "about": "one line: what belongs here", "media": [<media ids>]}, ...]}
Then run `python3 check_split.py <id>` in the run folder; it must print OK (it checks: every video once, floors, name form).
Fix and re-run until OK. Work only in this run folder; write nothing else; no database access.
Final answer: one line per old group: the new groups with their A/B counts.

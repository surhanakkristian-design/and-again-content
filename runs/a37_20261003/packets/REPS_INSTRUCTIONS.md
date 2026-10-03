# A37: pick the representative video of a group (curator)

Each group of vocabulary videos has a tile on the app's wall (learners aged 15-25). The tile shows one video's
thumbnail with the GROUP's name on it. `packets/reps_need.json` lists the slots (group id, English name, what
belongs in the group, level, 8 or fewer candidate videos with key word and description). For each slot there is a
contact sheet `reps/sheets/<group>_<level>.jpg`: the candidates' thumbnails left to right in the order of the list,
each labelled with media id and key word. LOOK at every sheet of your slots (Read the image).

Pick ONE candidate per slot:
1. it clearly shows what the group's NAME says (a tile named "Drinks" shows a drink, "Dogs" a dog);
2. clear and attractive as a small tile: one obvious subject, bright, sharp, not cluttered, no big text;
3. nothing sensitive: no weapons, blood, injuries, needles, alcohol or smoking in focus, no underwear / revealing
   clothing, no religious or political symbols, no scary or sad picture, nobody who looks like a minor in an
   awkward situation;
4. if no candidate is good, pick the least bad and say so in "note".

Output: {"<group>_<level>": {"media": <id>, "why": "short", "note": ""}, ...} to the file named in your task.
Work only in this run folder (helper files in your own subfolder). No database access. Do not show images in your final answer.

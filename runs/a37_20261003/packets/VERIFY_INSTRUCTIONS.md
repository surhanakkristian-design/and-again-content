# A37: verify the split of an old group into smaller topic groups (verifier, fresh eyes)

`packets/verify_<id>.md` shows one old group cut into new groups: per new group its id, English name, counts at
level A / B, what belongs there, then its videos (media id, level, key word, part of speech, description, cut).
A video belongs where its KEY WORD's meaning and the clip fit best. You did not make this cut: judge it.

For each file:
1. Read every video. Find videos that CLEARLY sit better in another new group of the SAME old group (a real
   misplacement a teenager would notice on a tile named like that), not matters of taste. No move across old groups.
2. A move must not push the group it leaves below 6 videos at that video's level. If a wrong video cannot move for
   that reason, list it under "stuck".
3. Judge each name: does the one English word cover the group's videos? If not, propose a better ONE-word name.
   Old groups that were not split (one new group) need no moves; only judge the name.
4. If the old group has only one new group and you see a clean split into two with at least 7 videos at A and at B
   each, say so under "notes" (do not do it).

Output `out/verify_<id>.json`:
{"old_group": <id>, "moves": [{"media": 123, "from": 101, "to": 103, "why": "..."}], "stuck": [{"media": 1, "why": ""}],
 "names": [{"id": 101, "ok": true, "better": null, "why": ""}], "notes": ""}
Work only in this run folder; use your own private subfolder of the scratchpad for helper files; no database access.
Final answer: per old group the number of moves and any name you would change.

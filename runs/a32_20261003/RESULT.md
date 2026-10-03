**Body-part concepts: 69 (64 human, 5 animal-only); (video, word) pairs removed: 1,523 on 892 videos (1,134 on 856 videos outside the Body Parts group, 389 on its 36 videos, whose lists were rebuilt); classes: 2,870 person / 131 animal only / 33 none; Body Parts group: 36 videos, 24 / 25.0 / 25 options (min / avg / max), all from other groups; second look on all 36: 1,107 ok / 10 doubt / 0 fit (10 removed); below 5 on the list alone: 33 videos, below 5 with list + fallback: 5, with none at all: 0; written live: yes (893 rows, one guarded transaction); re-select: 3,034 rows, 0 differ from the out files.**

# A32 part 1 (data) - result, 3 October 2026

Run folder `runs/a32_20261003`. No app change, no deploy, no Gemini, nothing committed.

## Start state
Fresh snapshot of the live `tinder_word_distractors` (3,034 rows): equal to A31's `out/distractors.json` and `out/fallback.json` in every row. Media (descriptions, transcripts), concepts, concept_media, the 74/75 exercises and the localizations were re-snapshotted and are unchanged since A31. Before-state: `backup/tinder_word_distractors_before.json` (all rows), `backup/changed_rows_before.json` (the 893 changed rows).

## 1. Body-part concepts: 69
`out/body_part_concepts.md` / `.json` (id, word, definition, kind, why). I read the word, part of speech and definition of all 2,987 key words.
- 64 human parts. 53 by definition (arm, leg, nose, ..., also lid = eyelid, middle = the front of the body, left = the left hand, feature = a part of the face). 8 by the bare word although the concept is defined otherwise: back (3 further concepts), bottom (sea bottom), face (verb), hand (farm worker), brain (clever person), butt (end of a handle). 3 by doubt: figure (2 concepts, "the shape of a human body" / a small model of a person), temple (the building; also the side of the head).
- 5 animal-only parts: fur, wing (2 concepts), scale (2 concepts, the weighing device / to weigh; also what covers a fish).
- Read and not counted, listed in the same file for you to overrule: hairstyles (braid, bun, ponytail, haircut, hairstyle, wig), marks on the skin (scar, wrinkle, tattoo, piercing), fluids (tears, sweat), materials (ivory, leather, wool), adjectives (cardiac, dental, fat), rare animal senses (bill, comb, coat, hide).

## 2. Removal: 1,523 pairs on 892 videos
- Class per video in `out/video_classes.json`: person 2,870 (723 of them also show an animal), animal only 131, none 33.
- How the class was set: clear person words by a keyword rule; I read every description without a clear person word (143) and every one with only a weak one (69, e.g. "legs", "face", "figure"). All 33 "none" videos were read by me: 189, 259, 4017, 4090, 4093, 4152, 4153, 4160, 4164, 4193, 4233, 4748, 4826, 4906, 5538, 6888, 6890, 6891, 6910, 6942, 6958, 6997, 7102, 7121, 7203, 7236, 7237, 7293, 7300, 7425, 7492, 7806, 7996. A hand that must be doing the action without being named (4037 cook, 4053 corn, 5176 mug), a first-person rider (369, 4167) and a figure built of stones (4119) count as person.
- Person: all 64 human parts removed; the 5 animal-only parts removed only when an animal is in the description. Animal only: all 69 removed (I did not decide part by part which animal has what; doubt = remove). None: nothing removed (8 of the 33 keep a body-part word: lap, brain, back, scale, forehead).
- Both columns were cleaned. No fallback list held a body-part word, so the fallback column did not change by this step.
- Most removed: breast 97, jaw 87, bottom 84, wing 74, butt 74, mouth 58, back 55, brain 52, back 49, figure 49, kidney 44, bone 43, left 43, temple 37, flesh 36. Full count per word: `out/stats.json`.
- Outside the Body Parts group this is 1,134 pairs on 856 videos; the average list goes from 39.8 to 39.6 options.

## 3. Body Parts group: 36 videos, 24 / 25.0 / 25 options
- The group has 36 videos (16 A, 20 B), not 40 or more, so both looks covered every video; there was no "rest" to build by rules.
- First look (me): for each video I picked the words one by one from a pool of 302 concrete nouns and 12 verbs of other groups (`bp_pool.py`, `bp_first.py`), then the script applied same level, other group, no body part, R1-R5 (1 word dropped by R4). 1,117 words, 25-36 per video.
- Second look (a separate agent that got only `packets/bp_audit_in.json`): 1,107 ok, 10 doubt, 0 fit. All 10 removed (`out/body_parts_audit.md`): dive, warehouse, umbrella, pyramid, paddle, corkscrew, train, wolf, drum, barbecue. Its findings are rules 7-11 in `out/BODY_PARTS_RULES.md`.
- Then cut to at most 25 per video (the brief's target). Final lists: `out/body_parts_lists.md`. Same part of speech first (all key words are nouns except blink, which gets 8 verbs first).
- No word of the Body Parts group and no body-part concept is in any of these lists.

## 4. Thin lists (decision 4)
- Below 5 on the same-level list alone: 33 videos (31 after A31; new: 6828 alarm and 8048 hesitate, Stress & Fear B, which lost "figure").
- 29 of them already had a fallback list from A31 (unchanged). For the other four I did A31's fallback look (other level of the same group, R1-R5, first look): 7302 lock the door gets underground, chains, jimmy; 196 courage, 6828 alarm and 8048 hesitate get nothing, because all level-A words of Stress & Fear (brave, dangerous, nervous, safe, scare, danger, alarm) fit or are arguable on those clips.
- Below 5 with list + fallback together: 5 videos: 196 courage (3), 214 dangerous (4), 4729 afraid (4), 6828 alarm (4), 8048 hesitate (4). With none at all: 0.

| media | group | level | key word | options (same level) | fallback | together |
|---|---|---|---|---|---|---|
| 112 | Stress & Fear | A | brave | 0:  | 6 | 6 |
| 196 | Stress & Fear | B | courage | 3: shock, distraction, desperate | 0 | 3 |
| 214 | Stress & Fear | A | dangerous | 0:  | 4 | 4 |
| 381 | Stress & Fear | A | scare | 4: brave, dangerous, safe, danger | 9 | 13 |
| 473 | Win & Lose | A | medal | 3: favourite, start, fail an exam | 17 | 20 |
| 498 | Stress & Fear | A | nervous | 4: dangerous, safe, scare, danger | 6 | 10 |
| 596 | Win & Lose | A | race | 4: medal, trophy, fortune, fail an exam | 13 | 17 |
| 610 | Win & Lose | A | ribbon | 4: race, finish, start, fail an exam | 23 | 27 |
| 629 | Stress & Fear | A | safe | 1: alarm | 9 | 10 |
| 644 | Stress & Fear | A | scared | 1: safe | 5 | 6 |
| 654 | Best Friends | A | secret | 2: cola, anxious | 17 | 19 |
| 811 | Win & Lose | A | trophy | 3: fortune, start, fail an exam | 18 | 21 |
| 872 | Best Friends | A | whistling | 4: secret, cola, share, admit | 15 | 19 |
| 877 | Win & Lose | A | winner | 3: fortune, start, fail an exam | 13 | 16 |
| 4057 | Best Friends | A | cola | 3: whistling, share, admit | 20 | 23 |
| 4075 | Stress & Fear | A | danger | 0:  | 7 | 7 |
| 4100 | Grab & Break | A | hole | 3: trap, to pull, easy | 13 | 16 |
| 4209 | Daily Routine | B | sleep | 4: suds, dirt, pot, soaked | 37 | 41 |
| 4515 | Win & Lose | A | to win | 2: start, fail an exam | 16 | 18 |
| 4729 | Stress & Fear | A | afraid | 0:  | 4 | 4 |
| 4862 | Mind & Ideas | A | choose | 4: dream, remember, word, plan | 20 | 24 |
| 5049 | Doors & Locks | A | close | 3: reveal, address, window | 6 | 9 |
| 5206 | Mind & Ideas | A | evidence | 4: rating, choose, dream, easy | 15 | 19 |
| 5401 | Mind & Ideas | A | wonder | 3: easy, evidence, rating | 12 | 15 |
| 5530 | Best Friends | A | admit | 4: share, whistling, cola, anxious | 16 | 20 |
| 5541 | Stress & Fear | A | alarm | 2: brave, safe | 6 | 8 |
| 5556 | Best Friends | A | anxious | 4: secret, whistling, cola, admit | 16 | 20 |
| 5609 | Stress & Fear | A | be afraid of | 2: dangerous, danger | 6 | 8 |
| 5637 | Daily Routine | B | be used to | 3: suds, soaked, dirt | 35 | 38 |
| 6828 | Stress & Fear | B | alarm | 4: haven, distraction, desperate, be willing to | 0 | 4 |
| 7104 | Win & Lose | A | favourite | 4: medal, trophy, finish, fail an exam | 22 | 26 |
| 7302 | Doors & Locks | A | lock the door | 4: chain, pass, address, window | 3 | 7 |
| 8048 | Stress & Fear | B | hesitate | 4: desperate, alarm, haven, distraction | 0 | 4 |

## 5. Write
- `out/a32_data.sql`: one transaction; guard: each of the 893 rows still has exactly the snapshot values in both columns, else it raises and changes nothing; assertions after the update: 3,034 rows; no human body-part concept in any list of a video outside the 33 "none" videos; no animal-part concept on a video with an animal; every Body Parts video has at least 10 options and none from its own group; no list holds a concept linked to the same media; every id exists in word_concepts; no list holds its own key word.
- Dry run in a rolled-back transaction: clean (3,034 rows, 893 changed rows equal to the new values, 120,023 options, 409 fallback words; the same sums as the local build).
- Live write: done by the session with `db query --linked --file out/a32_data.sql`, first try, not refused. No owner script was needed, so there is no `apply_a32.sh`.
- Rollback, NOT run: `out/a32_rollback.sql` (guarded the same way; restores the 893 rows).

## 6. Re-select
`verify_live.sh` after the write: 3,034 live rows, 0 differ from `out/distractors.json` and `out/fallback.json`.

## Files for the app tests
`out/distractors.json` (media id -> concept ids, all 3,034) and `out/fallback.json` (media id -> concept ids, the 30 videos with a fallback list). Also `out/video_classes.json`, `out/body_part_concepts.json`.

## For you to decide
1. **figure and temple count as body parts by doubt.** "figure" (the shape of a body) was on 61 lists, "temple" on 37. Removing "figure" is what pushed 6828 and 8048 from 5 to 4 options. Say if they should go back.
2. **scale counts as an animal part** (fish), although both concepts are about weighing; it was removed only from 19 videos with an animal.
3. **Hairstyles, scars, tattoos, tears, sweat are not counted.** "ponytail" or "scar" can still be a wrong word on a person video. A31's looks already removed them where the clip shows one.
4. **Animal-only videos lose every body-part word**, also parts the animal does not have (thumb on a dog video). It costs little and avoids deciding animal by animal.
5. **Five videos stay below 5 even with the fallback** (196, 214, 4729, 6828, 8048, all Stress & Fear). With a minimum of 5 they would get only correct cards, or the app accepts 3-4 options there.
6. **The looks read the description and transcript, not the picture**, as in A31. The keyword rule for "person" errs to the safe side: a video wrongly taken as showing a person only loses words.
7. **Body Parts videos now show unrelated concrete words** (penguin, toaster, lighthouse). They are clearly wrong, so these cards are easier than in other groups.

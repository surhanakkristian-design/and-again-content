# Phase 1Q Task B2/B3 part 2 - F6 hand gold on the 120 NEW sentences, F5 measured on 1N

0 model calls, 0 DB. `f6.py` was NOT touched (VARIANT C, as frozen).

## PART 1 - F6 hand gold, 120 new sentences (sids 170001-170120)

Source of the gold: `phase1p/data/sentences.json` + `phase1p/data/annotations_src.json`
(the blind reference annotation: `v`, `lk`, `alt`). No `items.json`, no writer answers, no
labels were opened; both reads are logged in `phase1p/access_log.jsonl`.
The flat 1P record is wrapped as `{"hygienised": {...}}` in this script, mirroring the 1N
container that `f6._ann` unwraps.

`faithful` = a correct natural English answer, not identical to `v[0]`; gold = must NOT be
rejected. `added` = the same answer plus exactly one content addition the Slovak lacks; gold
= should be rejected. agree = addition rejected. conservative = addition not rejected
(harmless miss). ERROR = a faithful answer rejected.

| variant | agree | conservative | ERROR |
|---|---|---|---|
| C (selected) | 58/120 | 62 | 0 |
| A | 115/120 | 5 | 0 |
| B | 39/120 | 81 | 0 |

### Variant C - every ERROR (faithful answer rejected)

none.

### Variant C - conservative items (planted addition NOT rejected)

- 170002 - added "in the new oven" -> abstain (content overlap 0.71 below 0.80 - free paraphrase, not judged)
- 170004 - added "with a red pen" -> abstain (content overlap 0.75 below 0.80 - free paraphrase, not judged)
- 170006 - added "in the garden" -> abstain (only a bare extra modifier - not rejected under this variant)
- 170007 - added "in a big pot" -> abstain (content overlap 0.71 below 0.80 - free paraphrase, not judged)
- 170009 - added "with chalk" -> abstain (only a bare extra modifier - not rejected under this variant)
- 170013 - added "on the way home" -> abstain (content overlap 0.75 below 0.80 - free paraphrase, not judged)
- 170015 - added "in the city centre" -> abstain (content overlap 0.71 below 0.80 - free paraphrase, not judged)
- 170016 - added "on thin paper" -> abstain (content overlap 0.67 below 0.80 - free paraphrase, not judged)
- 170017 - added "to the second floor" -> abstain (content overlap 0.75 below 0.80 - free paraphrase, not judged)
- 170018 - added "from the post office" -> abstain (extra content is not an anchored phrase (no preposition / determiner))
- 170020 - added "with the window open" -> abstain (content overlap 0.71 below 0.80 - free paraphrase, not judged)
- 170021 - added "every summer" -> abstain (extra content is not an anchored phrase (no preposition / determiner))
- 170023 - added "before the guests arrive" -> abstain (content overlap 0.67 below 0.80 - free paraphrase, not judged)
- 170026 - added "with a new camera" -> abstain (content overlap 0.71 below 0.80 - free paraphrase, not judged)
- 170027 - added "last year" -> abstain (content overlap 0.67 below 0.80 - free paraphrase, not judged)
- 170028 - added "for my classmates" -> abstain (extra content is not an anchored phrase (no preposition / determiner))
- 170030 - added "from Vienna" -> abstain (only a bare extra modifier - not rejected under this variant)
- 170031 - added "in one evening" -> abstain (extra content is not an anchored phrase (no preposition / determiner))
- 170033 - added "with new asphalt" -> abstain (content overlap 0.78 below 0.80 - free paraphrase, not judged)
- 170034 - added "for a hundred euros" -> abstain (content overlap 0.75 below 0.80 - free paraphrase, not judged)
- 170036 - added "with a fountain pen" -> abstain (content overlap 0.71 below 0.80 - free paraphrase, not judged)
- 170037 - added "by email" -> abstain (only a bare extra modifier - not rejected under this variant)
- 170038 - added "through the open gate" -> abstain (content overlap 0.78 below 0.80 - free paraphrase, not judged)
- 170039 - added "in the hotel kitchen" -> abstain (content overlap 0.71 below 0.80 - free paraphrase, not judged)
- 170042 - added "for a new model" -> abstain (content overlap 0.78 below 0.80 - free paraphrase, not judged)
- 170043 - added "in their room" -> abstain (extra content is not an anchored phrase (no preposition / determiner))
- 170044 - added "in the library" -> abstain (only a bare extra modifier - not rejected under this variant)
- 170048 - added "on Saturday morning" -> abstain (content overlap 0.71 below 0.80 - free paraphrase, not judged)
- 170049 - added "to her new flat" -> abstain (content overlap 0.71 below 0.80 - free paraphrase, not judged)
- 170052 - added "to our door" -> abstain (extra content is not an anchored phrase (no preposition / determiner))
- 170053 - added "from my phone" -> abstain (extra content is not an anchored phrase (no preposition / determiner))
- 170054 - added "in the shopping centre" -> abstain (content overlap 0.67 below 0.80 - free paraphrase, not judged)
- 170056 - added "with a wooden deck" -> abstain (content overlap 0.78 below 0.80 - free paraphrase, not judged)
- 170058 - added "for the older pupils" -> abstain (content overlap 0.75 below 0.80 - free paraphrase, not judged)
- 170059 - added "this morning" -> abstain (extra content is not an anchored phrase (no preposition / determiner))
- 170060 - added "by car" -> abstain (only a bare extra modifier - not rejected under this variant)
- 170061 - added "in the kitchen sink" -> abstain (content overlap 0.75 below 0.80 - free paraphrase, not judged)
- 170067 - added "next to the bank" -> abstain (only a bare extra modifier - not rejected under this variant)
- 170068 - added "yesterday afternoon" -> abstain (content overlap 0.78 below 0.80 - free paraphrase, not judged)
- 170070 - added "for three days" -> abstain (content overlap 0.78 below 0.80 - free paraphrase, not judged)
- 170071 - added "in a big album" -> abstain (content overlap 0.71 below 0.80 - free paraphrase, not judged)
- 170072 - added "in the whole house" -> abstain (content overlap 0.78 below 0.80 - free paraphrase, not judged)
- 170073 - added "for her history class" -> abstain (content overlap 0.75 below 0.80 - free paraphrase, not judged)
- 170074 - added "with the new key" -> abstain (content overlap 0.71 below 0.80 - free paraphrase, not judged)
- 170077 - added "in a rucksack" -> abstain (only a bare extra modifier - not rejected under this variant)
- 170078 - added "in a wood stove" -> abstain (content overlap 0.67 below 0.80 - free paraphrase, not judged)
- 170080 - added "on the third floor" -> abstain (content overlap 0.75 below 0.80 - free paraphrase, not judged)
- 170083 - added "in the gym" -> abstain (only a bare extra modifier - not rejected under this variant)
- 170085 - added "every evening" -> abstain (extra content is not an anchored phrase (no preposition / determiner))
- 170087 - added "at yesterday's meeting" -> abstain (content overlap 0.75 below 0.80 - free paraphrase, not judged)
- 170091 - added "with one click" -> abstain (extra content is not an anchored phrase (no preposition / determiner))
- 170094 - added "by registered post" -> abstain (content overlap 0.75 below 0.80 - free paraphrase, not judged)
- 170096 - added "in two weeks" -> abstain (content overlap 0.75 below 0.80 - free paraphrase, not judged)
- 170103 - added "on the last page" -> abstain (content overlap 0.78 below 0.80 - free paraphrase, not judged)
- 170104 - added "in his office" -> abstain (extra content is not an anchored phrase (no preposition / determiner))
- 170107 - added "last month" -> abstain (content overlap 0.75 below 0.80 - free paraphrase, not judged)
- 170110 - added "in our lives" -> abstain (content overlap 0.75 below 0.80 - free paraphrase, not judged)
- 170113 - added "from next year" -> abstain (content overlap 0.75 below 0.80 - free paraphrase, not judged)
- 170116 - added "on old houses" -> abstain (content overlap 0.71 below 0.80 - free paraphrase, not judged)
- 170117 - added "on its website" -> abstain (extra content is not an anchored phrase (no preposition / determiner))
- 170119 - added "in the first grades" -> abstain (content overlap 0.78 below 0.80 - free paraphrase, not judged)
- 170120 - added "in the park" -> abstain (only a bare extra modifier - not rejected under this variant)

### 1N gold (closed set, reported separately - never pooled with the 120)

| set | agree | conservative | ERROR |
|---|---|---|---|
| 1N (100 sentences) | 63/100 | 37 | 0 |
| 1P new (120 sentences) | 58/120 | 62 | 0 |

No measured cost on the 1P items is reported here: the 1P answers and labels stay unopened.

## PART 2 - F5 (frozen omission guard) on the CLOSED 1N set

The earlier attempt called `phase1i/checker_1i.f5_adjunct_deletion` with a hand-rolled dict;
every call raised `KeyError: exercise_id` and its 0/426 figure is VOID. Here the 1N records
are built by `phase1n/runner_1n.build_side_1n(...)` (the real builder: `item_id`,
`exercise_id`, refs, chk, the HYGIENE registry) and F5 is called on those records.

- record shape handed to F5: `+exercise_id=sid(int)`
- records built: 900; call failures: 0

| | k/n | %% |
|---|---|---|
| **F5 cost** (judged-CORRECT answers F5 rejects) | 13/426 | 3.05 |
| **F5 catches** (judged-WRONG answers F5 rejects) | 13/474 | 2.74 |

Catches by wrong type:

| wrong type | F5 rejects |
|---|---|
| M | 12/474 |
| T | 1/474 |

### F5 cost items (judged CORRECT, F5 rejected)

- `C:160013:2559106042` - "The tinsmith has been polishing the copper cauldron since early morning." -> (True, {'fired': True, 'variant': 'The tinsmith has been polishing the copper cauldron since early in the morning.', 'spans': [{'deleted': 'in', 'why': 'verb pa
- `C:160015:3892272793` - "Despite the strong wind, Viktor brought the seedlings all the way to the upper terrace." -> (True, {'fired': True, 'variant': 'Despite the strong wind, Viktor brought those seedlings all the way up to the upper terrace.', 'spans': [{'deleted': 'up', 'w
- `W:160015:3861351230` - "Despite the strong wind, Viktor brought the seedlings to the upper terrace." -> (True, {'fired': True, 'variant': 'Despite the strong wind, Viktor brought those seedlings all the way up to the upper terrace.', 'spans': [{'deleted': 'all way
- `W:160020:81015253` - "When we arrived, Janka had set up the whole stall." -> (True, {'fired': True, 'variant': 'When we arrived, Janka had already set up the whole stall.', 'spans': [{'deleted': 'already', 'why': 'adjunct adverb already'
- `W:160021:356150325` - "You will clean the clogged gutter after the first rain." -> (True, {'fired': True, 'variant': 'You will clean that clogged gutter only after the first rain.', 'spans': [{'deleted': 'only', 'why': 'adjunct adverb only', '
- `C:160028:1479798515` - "You have to take the empty bottles to the container in front of the house." -> (True, {'fired': True, 'variant': 'You have to take the empty bottles out to the container in front of the house.', 'spans': [{'deleted': 'out', 'why': 'verb pa
- `C:160038:3120993943` - "What are you drawing on the big paper right now?" -> (True, {'fired': True, 'variant': 'What are you drawing on that big sheet of paper right now?', 'spans': [{'deleted': 'sheet of', 'why': 'content word(s) sheet'
- `C:160038:4030922795` - "What are you drawing on that big sheet of paper?" -> (True, {'fired': True, 'variant': 'What are you drawing on that big sheet of paper right now?', 'spans': [{'deleted': 'right now', 'why': 'content word(s) right
- `C:160045:3626274490` - "She confirmed that she photographed the entire platform before the train left." -> (True, {'fired': True, 'variant': 'She confirmed to us that she photographed the entire platform before the train left.', 'spans': [{'deleted': 'to us', 'why': 
- `C:160050:968854585` - "The restorer explained that she removed three layers of varnish from the canvas." -> (True, {'fired': True, 'variant': 'The restorer explained to us that she had removed three layers of varnish from that canvas.', 'spans': [{'deleted': 'to us', 
- `C:160053:703629798` - "By evening, he will have been sanding the floor for eight hours straight." -> (True, {'fired': True, 'variant': 'By the evening he will have been sanding that parquet floor for eight hours straight.', 'spans': [{'deleted': 'that parquet',
- `W:160053:337807729` - "By evening, he will have been sanding the floor for eight hours." -> (True, {'fired': True, 'variant': 'By the evening he will have been sanding that parquet floor for eight hours straight.', 'spans': [{'deleted': 'that parquet',
- `C:160095:3693460798` - "You claimed that your colleague installed the new server." -> (True, {'fired': True, 'variant': 'You claimed to us that your colleague had installed the new server.', 'spans': [{'deleted': 'to us', 'why': 'content word(s) 

### F5 catches (judged WRONG, F5 rejected)

- [M] `W:160002:2138001426` - "A classmate wrote to me that he had read three chapters of the manual." -> (True, {'fired': True, 'variant': 'A classmate wrote to me that he had read three chapters of that manual in a single evening.', 'spans': [{'deleted': 'in singl
- [M] `W:160003:3268213061` - "We are going to lend you the big tent." -> (True, {'fired': True, 'variant': 'We are going to lend you that big tent for the whole weekend.', 'spans': [{'deleted': 'for whole weekend', 'why': 'content wo
- [M] `W:160005:1078273903` - "He is gluing the broken bowl right now." -> (True, {'fired': True, 'variant': 'He is gluing the broken bowl on the kitchen counter right now.', 'spans': [{'deleted': 'on kitchen counter', 'why': 'content 
- [M] `W:160009:547121764` - "The boatman told us that he had pulled up the anchor." -> (True, {'fired': True, 'variant': 'The boatman told us that he had pulled up the anchor before the storm.', 'spans': [{'deleted': 'before storm', 'why': 'conten
- [M] `W:160013:1152761632` - "The tinsmith has been polishing the copper cauldron." -> (True, {'fired': True, 'variant': 'The tinsmith has been polishing the copper cauldron since early in the morning.', 'spans': [{'deleted': 'since early in morni
- [M] `W:160019:1553120931` - "She is hanging the two maps above the desk." -> (True, {'fired': True, 'variant': 'She is hanging those two maps above the desk in the small study.', 'spans': [{'deleted': 'in small study', 'why': 'content wo
- [M] `W:160022:3493255559` - "If only she had read the contract." -> (True, {'fired': True, 'variant': 'If only she had read the contract more carefully.', 'spans': [{'deleted': 'more carefully', 'why': 'adjunct adverb more caref
- [M] `W:160023:1673437210` - "You can open the stuck drawer." -> (True, {'fired': True, 'variant': 'You can open that stuck drawer with one movement.', 'spans': [{'deleted': 'with one movement', 'why': 'content word(s) moveme
- [M] `W:160024:826788507` - "Klára told us that she had brought the old viola to the rehearsal." -> (True, {'fired': True, 'variant': 'Klára told us that she had brought that old viola to the rehearsal herself.', 'spans': [{'deleted': 'herself', 'why': 'conten
- [M] `W:160025:1471429802` - "There aren't many free shelves." -> (True, {'fired': True, 'variant': 'There are not many free shelves in that old warehouse.', 'spans': [{'deleted': 'in that old warehouse', 'why': 'content word(
- [M] `W:160055:746872208` - "The new suitcase is light and spacious." -> (True, {'fired': True, 'variant': 'That new suitcase is light and surprisingly spacious.', 'spans': [{'deleted': 'surprisingly', 'why': 'content word(s) surpris
- [M] `W:160061:1158872455` - "You will be putting the new chairs into the hall." -> (True, {'fired': True, 'variant': 'You will be putting those new chairs into the hall all morning.', 'spans': [{'deleted': 'all morning', 'why': 'content word(s
- [T] `W:160003:3275266210` - "We lend you the big tent for the whole weekend." -> (True, {'fired': True, 'variant': 'We are going to lend you that big tent for the whole weekend.', 'spans': [{'deleted': 'are going to', 'why': 'content word(s)

### Overlap F5 / F6[C] on 1N

F5 and F6 numbers are NEVER added together. Items both guards reject: **0**.

## Files

- `phase1q/f6_gold_1p.json` - the 120 x 2 hand gold (new sentences)
- `phase1q/f6_gold_eval_1p.py` - this measurement (re-runnable, 0 calls)
- `phase1q/f6_gold_1p_eval.json` - raw numbers
- `phase1q/F6_VALIDATION_1N.md` - earlier file; its F5 lines are VOID (notice appended there)

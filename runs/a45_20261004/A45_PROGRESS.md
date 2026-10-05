# A45 progress

Updated: 5 Oct 2026 21:23. All batches done and in the database (5 Oct 2026).

**Videos with content: 3044 / 3044 (A 1457 / 1457, B 1587 / 1587); failed: 0; audio files recorded: 24055 (Samantha female, Daniel male); batches in the database: 32 of 32 (3044 rows, read 5 Oct 2026 21:23).**

## Owner script to run
`bash ~/Projects/and-again-content/runs/a45_20261004/apply_a45.sh`
Batches not in the database yet: none. The script applies the migrations if missing (table `media_exercise_sets`; columns width / height), then per batch not in the database: audio upload (missing files are sent again up to 5 rounds with pauses after a network error), read-back of every object, guarded rows (only when all audio reads back), and the picture shape of every batch. `--check` only checks the files. Safe to run again; a batch already written is skipped.

## Notes (resumed run, 5 Oct 2026)
- The owner's first run of the script (from 09:22) wrote b001-b004, b007-b009 and b011; b005, b006 and b010 stopped on network errors during the audio upload (504 Gateway Time-out, transport error); nothing of them was written. The script now retries (see above). The resumed session ran it itself (allowed): b005, b006, b010 written; b012 and lab10 were written by the owner's run; all 13 earlier batches (1,210 rows) are in the database with their picture shape (5 Oct 2026). All later batches (b013-b031) were written by the session the same way; at 21:23 the table holds all 3,044 videos with their shape. Nothing is left for the owner script.
- Migration 20261004230000 recorded in the migration history (supabase migration repair) and checked: table, columns, constraints, RLS read policy, grants (anon / authenticated select only), index, bucket `audio` (public, audio/mpeg + audio/mp4) as in the migration.
- Migration 20261005100000 (columns `width`, `height` = the video's pixel size; aspect = width / height) applied and recorded by the session; the guarded shape updates (`out/<batch>_shape.sql`) fill them for every batch.

## Batches
| batch | videos | done | failed | audio files | in the database |
|---|---|---|---|---|---|
| lab10 | 10 | 10 | 0 | 80 | yes (10 rows, shape) |
| b001 | 100 | 100 | 0 | 790 | yes (100 rows, shape) |
| b002 | 100 | 100 | 0 | 793 | yes (100 rows, shape) |
| b003 | 100 | 100 | 0 | 788 | yes (100 rows, shape) |
| b004 | 100 | 100 | 0 | 786 | yes (100 rows, shape) |
| b005 | 100 | 100 | 0 | 780 | yes (100 rows, shape) |
| b006 | 100 | 100 | 0 | 783 | yes (100 rows, shape) |
| b007 | 100 | 100 | 0 | 787 | yes (100 rows, shape) |
| b008 | 100 | 100 | 0 | 792 | yes (100 rows, shape) |
| b009 | 100 | 100 | 0 | 790 | yes (100 rows, shape) |
| b010 | 100 | 100 | 0 | 790 | yes (100 rows, shape) |
| b011 | 100 | 100 | 0 | 775 | yes (100 rows, shape) |
| b012 | 100 | 100 | 0 | 784 | yes (100 rows, shape) |
| b013 | 100 | 100 | 0 | 789 | yes (100 rows, shape) |
| b014 | 100 | 100 | 0 | 792 | yes (100 rows, shape) |
| b015 | 100 | 100 | 0 | 785 | yes (100 rows, shape) |
| b016 | 100 | 100 | 0 | 786 | yes (100 rows, shape) |
| b017 | 100 | 100 | 0 | 784 | yes (100 rows, shape) |
| b018 | 100 | 100 | 0 | 791 | yes (100 rows, shape) |
| b019 | 100 | 100 | 0 | 790 | yes (100 rows, shape) |
| b020 | 100 | 100 | 0 | 789 | yes (100 rows, shape) |
| b021 | 100 | 100 | 0 | 793 | yes (100 rows, shape) |
| b022 | 100 | 100 | 0 | 793 | yes (100 rows, shape) |
| b023 | 100 | 100 | 0 | 794 | yes (100 rows, shape) |
| b024 | 100 | 100 | 0 | 797 | yes (100 rows, shape) |
| b025 | 100 | 100 | 0 | 797 | yes (100 rows, shape) |
| b026 | 100 | 100 | 0 | 797 | yes (100 rows, shape) |
| b027 | 100 | 100 | 0 | 799 | yes (100 rows, shape) |
| b028 | 100 | 100 | 0 | 794 | yes (100 rows, shape) |
| b029 | 100 | 100 | 0 | 799 | yes (100 rows, shape) |
| b030 | 100 | 100 | 0 | 798 | yes (100 rows, shape) |
| b031 | 34 | 34 | 0 | 270 | yes (34 rows, shape) |

## Failed videos
none

## Voices
Samantha (female), Daniel (male). Checked 5 Oct 2026 (`say -v '?'`): no Ava / Zoe (Premium) and no Evan / Nathan (Enhanced) installed, so no re-recording. To get them: System Settings > Accessibility > Spoken Content > System voice > Manage voices.

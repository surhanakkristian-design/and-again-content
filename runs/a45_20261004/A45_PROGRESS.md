# A45 progress

Updated: 5 Oct 2026 08:42. Stopped for the handoff after batch b012; see A45_HANDOFF.md.

**Videos with content: 1210 / 3044 (A 764 / 1457, B 446 / 1587); failed: 0; audio files recorded: 9518 (Samantha female, Daniel male); batches in the database: 0 of 13.**

## Owner script to run
`bash ~/Projects/and-again-content/runs/a45_20261004/apply_a45.sh`
The migration (table `media_exercise_sets`; the bucket `audio` also takes audio/mp4) if it is missing, then every batch that is not in the database yet: audio upload, read-back, guarded rows. `--check` only checks the files. Safe to run again after every new batch; a batch already written is skipped.

## Batches
| batch | videos | done | failed | audio files | in the database |
|---|---|---|---|---|---|
| lab10 | 10 | 10 | 0 | 80 | waits for the owner script |
| b001 | 100 | 100 | 0 | 790 | waits for the owner script |
| b002 | 100 | 100 | 0 | 793 | waits for the owner script |
| b003 | 100 | 100 | 0 | 788 | waits for the owner script |
| b004 | 100 | 100 | 0 | 786 | waits for the owner script |
| b005 | 100 | 100 | 0 | 780 | waits for the owner script |
| b006 | 100 | 100 | 0 | 783 | waits for the owner script |
| b007 | 100 | 100 | 0 | 787 | waits for the owner script |
| b008 | 100 | 100 | 0 | 792 | waits for the owner script |
| b009 | 100 | 100 | 0 | 790 | waits for the owner script |
| b010 | 100 | 100 | 0 | 790 | waits for the owner script |
| b011 | 100 | 100 | 0 | 775 | waits for the owner script |
| b012 | 100 | 100 | 0 | 784 | waits for the owner script |

## Failed videos
none

## Voices
Samantha (female), Daniel (male): no Premium / Enhanced English voice is installed. Better: download Ava (Premium) or Zoe (Premium), and Evan (Enhanced) or Nathan (Enhanced) in System Settings > Accessibility > Spoken Content > System voice > Manage voices, then say so.

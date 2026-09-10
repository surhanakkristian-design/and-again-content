# and-again-content

Content pipeline for the And Again app: the Brief 19/20 chunking and grammar
scripts and prompts, the SQL data repairs, Claude output workbooks, and the
Claude Code skills that drive the exercise and vocabulary workbook fills.

The app itself lives in the `and-again` repo
(git@github.com:surhanakkristian-design/and-again.git).

## Layout

- `scripts/brief19/` — pipeline scripts and prompts (chunking, grammar sweep, repairs)
- `scripts/repairs_9.9.2026/` — SQL data repairs and notes
- `Claude outputs/` — workbooks and previews produced by Claude sessions
- `skills/` — Claude Code skills (`ugc-exercise-fill`, `ugc-vocab-sheet-fill-level-ab`)

## Skills

Claude Code loads skills from `~/.claude/skills/<name>/SKILL.md`. Symlink each
skill directory from this repo into that folder:

```bash
ln -s ~/Projects/and-again-content/skills/ugc-exercise-fill ~/.claude/skills/ugc-exercise-fill
ln -s ~/Projects/and-again-content/skills/ugc-vocab-sheet-fill-level-ab ~/.claude/skills/ugc-vocab-sheet-fill-level-ab
```

## Run outputs

Pipeline run outputs (`runs/` anywhere in the tree) are ignored. Finished run
logs are archived on Drive only.

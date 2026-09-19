# Phase 1V — Track A, A4 set build (TASK_A_SET) — status: NEED_SPAWN

**Stopped at the spawn step, as the task instructs.** The `claude` CLI at `/opt/homebrew/bin/claude`
cannot run: `Error: claude native binary not installed. Either postinstall did not run (--ignore-scripts, some pnpm configs)`.
This happened on both `claude --version` and `claude -p ... --model sonnet`. No writer and no judge ran. There are 0 sentences and 0 items, and no floor has been checked.

## Items
- **A4 set build: done up to the spawn.** The briefs, tooling and declarations are written. Writers, assembly, packets, judging and the floor check are **not done** because nothing could be spawned.
- **Overlap reference: 770 sentences**, verified by running `assemble_1v.earlier_slovak()`. The sources are phase1n/existing_350 (350), phase1n/data (100), phase1p/data (120), phase1t/set/data (100) and phase1u/data (100). Collisions are checked on the exact normalised text and on Jaccard similarity, as in 1U. Sentences from phase1v's own folders are never used as the reference.
- **SIDs:** 200001–200100 (public ids 1V001–1V100, level blocks as in 1U). **Shuffle seed:** 20260923 (1U used 20260920). There are 80 hidden duplicates, 20 per level, in 4 packets. The script moves to 5 packets only if the token budget forces it.
- **Writer brief:** `WRITER_SPEC_1V.md` is the 1U spec with one addition. In every FR, MC and MN sentence, `c2` must be a determiner-only difference: a / an / the / zero article. The Slovak noun phrase must have no demonstrative (ten/tá/to/tie/tieto…) and no possessive, and the variant must not use this/that or a possessive. In addition, at least 3 SKP `c4` answers carry the tags `skp-passive` + `determiner`. That gives about 92 written items for F6 (floor 60). The 1U example that used "that new bridge" now uses "a new bridge".
- **Judge brief:** `judge/JUDGE_BRIEF_1V.md` is the 1U brief plus the owner's determiner rule, labelled as restated from the 1V brief.
- **Floors** (`FLOORS_DECLARED_1V.json`, enforced by `floors_1v.py`): F1 ≥120, F1a ≥40, F1b ≥30, F2 ≥100, F3 ≥60, F4 ≥40, F5 ≥40, and the **new F6 ≥60** (determiner-difference answers judged correct). The script also reports `determiner_judged_wrong`. `floors_1v.json` and `FLOOR_CHECK_1V.json` are **not done**: they need judged labels.
- **Sensitivities** (`SENSITIVITIES_1V.json`): S1–S6 as in 1U, plus **S7** = determiner-difference items judged correct, rescored as wrong. S7 has n ≥ 60 by floor F6. The run agent's scorer must implement S7.
- **Top-up round:** not needed yet (no floor has been checked).
- **Tooling self-test:** `selftest_1v.py` → SELFTEST OK, 0 failures (synthetic data, 0 model calls).
- All scripts are the 1U scripts adapted: 1u→1v, sid 190→200, new seed, and F6 added to the floor script and the assembler counts. The mirror writes that 1U sent to `phase1u/data/` now go to `trackA_set/data/`, so nothing is written outside this track.

## What the main session must run (in order)
1. Spawn 4 blind writers in parallel (Read+Write only). Each task file is its whole prompt:
   `briefs/WRITER_TASK_A1.md`, `…_A2.md`, `…_B1.md`, `…_B2.md`. Each writer writes
   `writers/writer_<L>_part1.json` and `writers/writer_<L>_part2.json`.
2. `python3 assemble_1v.py`, then `python3 build_packets_1v.py`. This writes `judge/packet_partK.jsonl`,
   `judge/JUDGE_TASK_1V.md` and `packet_key_1v.json`.
3. Spawn ONE blind judge (Read+Write) on `judge/JUDGE_TASK_1V.md`. It writes `judge/verdicts_partK.json`.
4. `python3 join_labels_1v.py`, then `python3 floors_1v.py`. Exit code 2 means a floor failed: allow one top-up round, then STOP.

All paths are under `/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase1v/trackA_set/`.

## Budget
Model calls: 0 counted, 0 failed, 0 retried. Spend: $0. Own harness tool calls: 9 of 12. No STOP rule was triggered, apart from the NEED_SPAWN stop.

## Execution attempt, 19 Sept 2026 (set-execution agent): STOPPED because headless auth failed
- **Binary:** `/opt/homebrew/bin/claude` is broken ("native binary not installed"). There is a working binary at
  `~/Library/Application Support/Claude/claude-code/2.1.275/claude.app/Contents/MacOS/claude`, and it reports `2.1.275 (Claude Code)`.
  (`claude-code-vm/2.1.275/claude` is the VM build, which is not for macOS. `npx @anthropic-ai/claude-code` fails the same way as Homebrew.)
- **Auth blocker:** `-p "say ok" --model sonnet --output-format json` returns `is_error: true`,
  `"Failed to authenticate: OAuth session expired and could not be refreshed"`. This happens with the inherited desktop env and with a clean `env -i` env.
  `claude auth status` gives `loggedIn: false, authMethod: none`. The Desktop app's sessions authenticate through the host
  (CLAUDE_CODE_SDK_HAS_HOST_AUTH_REFRESH), and a spawned headless child does not get that refresh.
- **Not done:** writers, assemble, packets, judge, join, floors, top-up. The counts are still 0 sentences / 0 items / 0 judged.
  No floor was checked, and `floors_1v.json` / `FLOOR_CHECK_1V.json` do not exist.
- **Claude-session tokens:** 0 (both test sessions failed before inference). Model calls: 0. Spend: $0.
- **To unblock (user action):** run `"<that binary>" auth login` once in a terminal (or `claude setup-token` and export
  `CLAUDE_CODE_OAUTH_TOKEN`). After that, the driver in the spawn order above can run unchanged. The alternative is for the main session to spawn the 5 sessions as Agents
  (brief paths in "What the main session must run").
- **Deviations:** none. No system software was installed or modified.

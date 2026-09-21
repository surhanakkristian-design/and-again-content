# SHA incident S2 (resolved 21.9.2026 by stage 2b)

Finding: NO real write to any earlier phase. The 122-line SHA_diff_S2.txt is a generator mismatch, not a change.

- S1 built SHA_before.txt with phase2i/sha_tree.sh (prunes phase2i) with phase2j lines removed -> 3,256 files, 0 phase2i and 0 phase2j lines.
- s2_chain.sh used its own `find` that prunes only phase2j, so it ADDED the 121 phase2i files (diff = header + 121 `>` lines,
  every one under phase2i/; no `<` line, no changed hash).
- Re-run of the S1 generator (`zsh phase2i/sha_tree.sh | grep -v '  phase2j/'`) at stage 2b start: 3,256 files, diff vs SHA_before EMPTY.
- phase2i itself (not covered by the baseline): `git status -- translation-offline/phase2i` clean (0 entries), so byte-identical to its commit.
- No __pycache__ anywhere outside phase2j; no file outside phase2j newer than SHA_before.txt. Nothing to restore.
- phase1p access_log.jsonl / run_1p.log show as modified in git: that is the dirty pair that is part of the baseline (unchanged hashes).

Fix: s2_chain.sh now uses the S1 generator (sha_tree.sh | grep -v phase2j) and literal `git -C /Users/kristiansurhanak/Projects/and-again-content` calls.

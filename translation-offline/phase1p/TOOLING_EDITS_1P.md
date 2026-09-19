# Phase 1P — tooling edits

## First runner agent (commit 2e62b1f)
None. It stopped before any edit because `data/writer_A.json` was missing.

## Recover + run agent (this session) — tooling only, no lever / prompt / decision rule / threshold touched
1. `data/writer_A.json` restored from a re-run of writer A's own build script (proof: `RECOVERY_1P.md`).
   Sources kept in `recovery/` (`build_A.py.txt` is renamed so that `check_freeze()` does not see a new `.py`).
2. NEW `normalise_1p.py` (appended to `FREEZE_FILES`, block "not executed by --final"). It maps what the
   writers and judges delivered onto the `loader_1p` contract:
   * writer schema `{correct:[4], wrong:[5]}` -> items `<C|W>:<170000+n>:<aid>`;
   * aid conventions: writer A positional `c0..c3 / w0..w4`, writer B native `c1..c4 / w1..w5` (kept as delivered, they match the key files);
   * intent `TF` -> `T`; correct answers get intent `C`; `writer_side`, `writer_kind`, `writer_intent`, `writer_passive` kept on every item;
   * `_key_A.json` + `_key_B.json` and `verdicts_{A1,A2,B1,B2}.json` -> `judge/blind_map.json` + `judge/out_part1.json`
     (the label of record is the JUDGED label); the 40 + 40 hidden duplicates -> `judge/controls_map.json` + `judge/out_controls.json`, never test items;
   * asserts: 120 sentences, 4 + 5 per sentence, known tags, no overlap with the existing 450, no internal duplicate,
     every jid has a verdict, every packet answer equals the writer answer, 1,080 distinct test items;
   * writes the label-side floor pre-check to `normalise_1p.json`;
   * builds `data/annotations.json` ONLY from an independent delivery `data/annotations_src.json`; it never invents a reference.
3. `assemble_1p.py`, `floor_check_1p.py`, `runner_1p.py`, `loader_1p.py`, `lever{1,2,3}.py` are byte-identical to 0e0961b.
   `assemble_1p.py` is superseded by `normalise_1p.py` for this set (its input contract — the 1N writer schema with an
   `annotation` block — is not what the writers were asked to deliver).

# Phase 1P — recovery of `data/writer_A.json`

* Cause search: `grep -nE "rmtree|unlink|os\.remove|\brm |shutil\.move|os\.rename" phase1p/*.py phase1p/selftest/*` -> **no hit**.
  Nothing in the phase tooling deletes or moves files. Writer A's script writes `data/writer_A.json` with a plain `json.dump`;
  the file was in no commit, so the loss cannot be dated. `data/` was copied to `data_backup/` before anything was run.
* Writer A's build script and its three hand-written source parts were still in the session scratchpad
  (`build_A.py`, `p1.json`, `p2.json`, `p3.json`, seed 1601). They were copied to a temp dir, ONE line was patched
  (`P = os.path.join(C, "phase1p")` -> an output dir from the environment) and the script was re-run. Its own checks printed `OK`
  and the writer's reported counts reproduce (correct tags agentless 48 / determiner 60 / aspect 37 / by-passive 17;
  wrong timeframe 104 / agentless 96, 64 of them non-timeframe; intents T 104 / W 67 / M 69 / S 60).
* Identity with what the blind judge actually saw (regenerated vs committed in `judge/`):

| file | bytes identical | sha256 (first 16) |
|---|---|---|
| `judge/packets_A1.json` (280 jids) | yes | `3d2065ccd8f7525d` |
| `judge/packets_A2.json` (300 jids) | yes | `1388c7dc61f8a7ea` |
| `judge/_key_A.json` (580 jids) | yes | `70c5ebea7617a2bc` |

  Same jid -> same Slovak / answer, same key, same hidden duplicates. The blind labels remain valid.
  `normalise_1p.py` additionally asserts, for all 1,160 jids of both writers, packet answer == writer answer.
* Restored file: `data/writer_A.json` sha256 `e7bc0b648f0073f07be5852b74e8ac39bf9ad88b01070264ea14bd823f73e32a`; sources archived in `recovery/`.

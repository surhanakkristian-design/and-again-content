# Phase 2I run - access log, verbatim

Every open of `set/items.jsonl` by run_2i.py, copied byte-for-byte from `run/access_log.jsonl` (2 lines).

```
{"argv": ["--set", "phase2i/set/items.jsonl", "--run-dir", "phase2i/run", "--purpose", "Phase 2I stage 5 final run (set opened once)"], "bytes": 2594863, "path": "/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2i/set/items.jsonl", "pid": 20166, "purpose": "Phase 2I stage 5 final run (set opened once)", "sha256": "45f0abc7afb8ab0d63fbc997cb71127cf5c096c6ff356eb015b203dccd387ce7", "ts": "2026-09-21T09:13:10+00:00"}
{"argv": ["--set", "/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2i/set/items.jsonl", "--run-dir", "/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2i/run", "--purpose", "Phase 2I stage 5 final run, re-launch after attempt 1 crashed at stack prepare (relative --run-dir vs stack cwd), 0 calls made"], "bytes": 2594863, "path": "/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2i/set/items.jsonl", "pid": 20343, "purpose": "Phase 2I stage 5 final run, re-launch after attempt 1 crashed at stack prepare (relative --run-dir vs stack cwd), 0 calls made", "sha256": "45f0abc7afb8ab0d63fbc997cb71127cf5c096c6ff356eb015b203dccd387ce7", "ts": "2026-09-21T09:22:49+00:00"}
```

Open 1 crashed before any model call (relative-path bug, see FINAL_RUN_DONE); open 2 is the resume/re-launch that ran the set. No other open.

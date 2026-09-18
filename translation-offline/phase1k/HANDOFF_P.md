# Phase 1k — HANDOFF from agent P (prep)

Read `phase1k/CONTEXT_1K.md` first (it carries the owner's §0 verbatim). Everything below is
produced by `phase1k/fresh/make_fresh.py` (deterministic, 0 model calls, 0 DB reads).

## 1 The 70 fresh sentences — counts

sids **140001..140070** (max existing sid 32539 + >100000), `side:"fresh"`, arm-B form (explicit subject
pronoun wherever Slovak would drop it; noun subjects untouched), `g` = null everywhere.

| metric | got | target | |
|---|---|---|---|
| level A1/A2/B1/B2 | 6/16/25/23 | 6/16/25/23 (= DEV 70 of 1j) | OK |
| tf_gold | past 21 · future 20 · present 19 · conditional 8 · mixed 2 | spread | OK |
| voice_sk | active_agent 59 · impersonal 6 · passive 5 | impersonal+passive >= 10 | OK |
| agent_nom (nom. agent + transitive) | 43 | >= 42 | OK |
| perfective_present futures | 13 | >= 12 | OK |
| bude + infinitive futures | 6 | >= 6 | OK |
| conditionals (by) | 8 | >= 8 | OK |
| plain present | 19 | >= 15 | OK |
| past total | 21 | >= 20 | OK |
| past imperfective (tense_open) | 10 | >= 10 | OK |
| Slovak length 6-18 words | 6-11 | 6-18 | OK |
| overlap with the existing 140 | sk dup 0, en dup 0, max content Jaccard 0.27 | 0 / 0 / < 0.50 | OK |

Closest existing sentences by content-word Jaccard (sid (score)): 140051 (0.27), 140058 (0.22), 140017 (0.22) — no normalised Slovak
sentence and no English reference equals an existing one (original or arm-B rewritten).

`tf_gold`/`voice_sk`/`agent_nom`/`perfective_present`/`tense_open` are **gold metadata for
reporting only** — no checker layer, guard or prompt may read them. `agent_nom:true` means the
Slovak names a nominative agent AND the verb is transitive, i.e. an English passive recast is
possible and, per §0 B1, WRONG.

## 2 Schema notes

- Fresh records use the Phase 1j `sentences_all.jsonl` keys plus `annotation`
  (`{hygienised, raw}`, the `$J/*/annotations.json` shape: `id, t, lv, v, lk, alt`) plus the five
  gold fields. `annotations_fresh.json` is the same annotation keyed by `"<sid>"`, so existing
  checker code can be seeded exactly as in `baseline_dev_1j.py`.
- `lk` is parallel to `v` (one lock per accepted reference) and is the **practised structure** —
  under §0 it may only produce a TIP, never a rejection.
- `t` is synthetic (9000+) and carries no `m` mistake patterns, so no pattern lookup can fire on a
  fresh sentence. `n_items` is null until the answer writer has run.
- `band` is the Slovak word-count bucket, the same convention as Phase 1j.
- Item ids: `C:<sid>:<crc32(text)>` for intent C, `W:<sid>:<crc32(text)>` otherwise.

## 3 How to read data (always through the loader)

```python
import os, sys
K = os.path.expanduser('~/Projects/and-again-content/translation-offline/phase1k')
sys.path.insert(0, K)
from loader_1k import (load_dev_items, load_dev_annotations, load_holdout1j_items,
                       load_fresh_sentences, load_fresh_annotations, load_fresh_items)
dev  = load_dev_items(purpose='…')             # 490, arm-B sk/reference/refs
ann  = load_dev_annotations(purpose='…')       # arm-B annotations (g removed)
hol  = load_holdout1j_items(purpose='…')       # 490, labelled replay
frs  = load_fresh_sentences(purpose='…')       # 70, answer-free, always readable
itm  = load_fresh_items(purpose='…')           # GATED: needs PHASE1K_OPEN_FRESH=1
```

Every call appends `{ts, side, what, caller, n, purpose}` to `phase1k/access_log.jsonl`.
`$J` is `chmod -R a-w`: `loader_1k` neuters `loader_1j._log` and logs into `$K` instead, and sets
`sys.dont_write_bytecode` — still run python with `PYTHONDONTWRITEBYTECODE=1`.

## 4 The answer writer → the judge input

1. The writer reads ONLY `phase1k/fresh/writer_input.jsonl` (`{wid, slovak, level, topic}`) and
   writes `phase1k/fresh/writer_output.jsonl`, one line per sentence:
   `{"wid": 140001, "answers": [{"text": "…", "intent": "C|T|W|M|S|V|TF"}, …]}`
   Quotas enforced by the builder: per sentence **>= 3 C and >= 4 wrong**, overall **>= 30 V**
   (active→passive recast, the §0 B1 probe) and **>= 30 TF** (time-frame shift, the B2 probe).
   Exact duplicate texts inside one sentence are dropped before the quota check.
2. Then, exactly:

```
cd ~/Projects/and-again-content/translation-offline
PYTHONDONTWRITEBYTECODE=1 python3 phase1k/judge/build_judge_input.py
```

   It prints counts only and writes `fresh/items_fresh.jsonl`, `judge/in_1..in_4.jsonl`
   (Phase 1j DEV 490 + fresh + 60 control duplicates, shuffled with seed `phase1k-judge`, equal
   sizes, each control in a different chunk than its original), `judge/in_5.jsonl` (the 490
   Phase 1j HOLDOUT items) and `judge/key.jsonl` (j → {id, sid, source, dup_of}; forbidden to the
   judge). Judge lines carry **only** `{j, sk, en}`. A malformed writer_output fails loudly with a
   `WRITER_OUTPUT ERROR:` message. `python3 phase1k/judge/build_judge_input.py --selftest` runs the
   whole build on a fabricated writer_output in a temp dir.

## 5 Agent P self-count

11 tool calls (3 recon/inspect Bash, 4 Write, 2 Edit, 2 Bash build+selftest+lock+verify) — cap was 12.

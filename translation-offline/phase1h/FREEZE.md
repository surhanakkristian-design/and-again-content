# Phase 1h — FREEZE

18 Sept 2026. The checker, the rules, the tables, the thresholds, the two
prompts and the hygiene script are frozen at this commit and were NOT touched afterwards.
The only things produced after the tag are `fresh/new_sentences_60.jsonl`,
`fresh/writer_input_140.jsonl` (mechanical selection, seed 20260919) and STATE.md.

- freeze commit: `0abfafd40a6a768cfa1c3c69cfc43482e0d9979b`
- tag: `translation-offline-phase1h-FROZEN`

| file | sha256 |
|---|---|
| `phase1h/checker_1h.py` | `49fa087bf2ecb511a960315e1c1e25a6f01ffbbb40fd285fc3157168af556f19` |
| `phase1h/lib_prev.py` | `c9e19245ee48888eb2ea5033e6bad7890fa7fa0abdb70ec2f0cb8d99d911067a` |
| `phase1h/reference_hygiene.py` | `7380f3142f8980c15ec9c43528642e59437b7131a930e2115447ba68db605d36` |
| `phase1h/select_new_sentences.py` | `93a8623df8a328510204eb5d95744b9875fd4dde5c3ed7ff45597a0ee9b2dad6` |
| `phase1h/FRESH_SCHEMA.md` | `9128781ffa412f8a70ade3767553289de97002f14d4d29897077460d0c4b199f` |

Frozen inputs (all made read-only by this phase): `phase1c/`, `phase1e/`, `phase1f/`, `phase1g/`.

# Phase 1m — DATA HANDOFF (label: recon-data)

Everything below is recovered from Phase 1k materials so that a NEW 140-sentence set can be written,
annotated and judged under exactly the Phase 1k conventions. Companion files, all in `phase1m/tasks/`:
`ACCEPTANCE_RULE.md` (the §0 rule verbatim), `TYPE_DEFS.md` (T/W/M/S/V/E and the intents V, TF),
`ARM_B.md` (the Slovak subject convention). Those three are the blind-side files: they contain nothing
about checkers, layers, locks, guards or prompts.

## (a) The annotation schema of the Phase 1k fresh sentences

Two files carry it:

- `phase1k/fresh/sentences_fresh.jsonl` — one full record per sentence, 23 keys.
- `phase1k/fresh/annotations_fresh.json` — `{"<sid>": {"hygienised": {…}, "raw": {…}}}`, the same
  annotation keyed by sid as a string. In all 70 fresh sentences `hygienised` and `raw` are identical
  (the sentences were authored clean, so hygienisation was a no-op).

### Annotation object (inside `annotation.hygienised` / `annotation.raw`)

| key | meaning | written by |
|---|---|---|
| `id` | = the sid (int) | annotator (agent P) |
| `t` | topic id; **synthetic 9000+** for a hand-written set, so it is not a live topic id and carries no mistake patterns | annotator |
| `lv` | CEFR level string: `A1` / `A2` / `B1` / `B2` | annotator |
| `v` | list of ACCEPTED English reference translations (the first is the primary reference) | annotator |
| `lk` | list of grammar locks, **parallel to `v`** (one per accepted reference) = the practised structure of that reference. Under the §0 rule it may only produce a tip, never a rejection | annotator |
| `alt` | per-word alternatives: `{"<word in the reference>": ["<accepted variant>", …]}` | annotator |
| `s` | optional synonym groups (absent in all 70 fresh records) | annotator |
| `d` | optional tokens (null in the fresh records) | annotator |
| `p` | optional (null in the fresh records) | annotator |
| `m` | mistake patterns (absent for hand-written sentences — their `t` is synthetic) | annotator |
| `g` | gender chain — **absent / null everywhere under arm B**, because the subject pronoun is stated | annotator |

### Full sentence record (`sentences_fresh.jsonl`), all 23 keys

`sid`, `side` (`"fresh"`), `level`, `band` (Slovak word-count bucket `1-6 / 7-9 / 10-12 / 13-16 / 17+`),
`topic` (the human topic name, e.g. "Present Simple"), `half` (`"NEW"`), `sk` (the Slovak sentence, arm-B
form), `reference` (primary English reference), `refs` (all accepted references), `annotation_v`,
`annotation_alt`, `annotation_d`, `annotation_p`, `g`, `g_raw`, `locks` (= `lk`), `n_items` (null until
answers exist), `annotation` (`{hygienised, raw}`), plus the five **gold metadata** fields, which are
hand-checked by the annotator and **for reporting only — no checker layer, guard or prompt may read
them** (`phase1k/CONTEXT_1K.md` lines 68-75, `HANDOFF_P.md` §1):

| field | values / meaning |
|---|---|
| `tf_gold` | `present \| past \| future \| conditional \| mixed` — the time frame the Slovak fixes |
| `voice_sk` | `active_agent \| impersonal \| passive` |
| `agent_nom` | `true` = the Slovak names a nominative agent **and** the verb is transitive, so an English passive recast is possible — and per B1 **wrong** |
| `perfective_present` | `true` = perfective present form with future meaning ("dokončí") |
| `tense_open` | `true` = the Slovak leaves the English tense choice open inside the frame (B3), e.g. past imperfective |

### Three full example annotations (verbatim from `phase1k/fresh/annotations_fresh.json`)

```json
"140001": {"hygienised": {"id": 140001, "t": 9000, "lv": "A1", "v": ["She drinks green tea with honey every morning."], "lk": ["drinks"], "alt": {"drinks": ["has"]}}, "raw": {"id": 140001, "t": 9000, "lv": "A1", "v": ["She drinks green tea with honey every morning."], "lk": ["drinks"], "alt": {"drinks": ["has"]}}}
"140002": {"hygienised": {"id": 140002, "t": 9001, "lv": "A1", "v": ["He is washing his old trainers in the sink right now."], "lk": ["is washing"], "alt": {"trainers": ["sneakers", "trainers"], "sink": ["basin"]}}, "raw": {… identical …}}
"140003": {"hygienised": {"id": 140003, "t": 9002, "lv": "A1", "v": ["My sister only wears glasses when she reads.", "My sister wears glasses only for reading."], "lk": ["wears", "wears"], "alt": {"glasses": ["spectacles"]}}, "raw": {… identical …}}
```

Their sentence records (sid 140001) show how the two halves fit together: `sk` "Ona každé ráno pije
zelený čaj s medom.", `reference` = `v[0]`, `locks` = `lk`, `annotation_alt` = `alt`, `g`/`g_raw` null,
`tf_gold` "present", `voice_sk` "active_agent", `agent_nom` true, `perfective_present` false,
`tense_open` false.

### The instructions the Phase 1k annotator (agent P) worked to

There is **no standalone annotator prompt file on disk**. The instructions are stated in three places,
essential text quoted:

1. `phase1k/fresh/make_fresh.py` lines 1-15 (the annotator's own program header):
   > Phase 1k — the 70 NEW Slovak holdout sentences (agent P, authored by hand). Emits,
   > deterministically and with 0 model calls: `fresh/sentences_fresh.jsonl` full records
   > (1j sentence schema + annotation + gold metadata); `fresh/annotations_fresh.json`
   > `{"<sid>": {"hygienised":…, "raw":…}}`; `fresh/writer_input.jsonl` `{wid, slovak, level, topic}`
   > ONLY; `HANDOFF_P.md` counts + overlap check.
   > Arm-B convention: an explicit subject pronoun wherever Slovak would drop the subject; noun
   > subjects stay as they are; no `g` chain anywhere (the pronoun states the gender).
   > Row = (level, topic, sk, [refs], [locks parallel to refs], alt, tf_gold, voice_sk, agent_nom,
   >        perfective_present, tense_open)
2. `phase1k/HANDOFF_P.md` §2 "Schema notes": `lk` is parallel to `v` (one lock per accepted reference)
   and is the practised structure; `t` is synthetic (9000+) and carries no `m` mistake patterns;
   `band` is the Slovak word-count bucket; item ids are `C:<sid>:<crc32(text)>` for intent C and
   `W:<sid>:<crc32(text)>` otherwise, with `crc32 = zlib.crc32(text.encode('utf-8')) & 0xffffffff`.
3. `phase1k/HANDOFF_P.md` §1 and report §2.1 — the composition targets the annotator had to hit
   (see (c) below), plus the overlap rule: **0 duplicate Slovak sentences, 0 duplicate English
   references, max content-word Jaccard < 0.50 against every existing sentence** (achieved: 0 / 0 / 0.27).
   sids started at 140001 = max existing sid 32539 + more than 100000.

## (b) The judge-label schema

- Judge input, one JSON object per line (`phase1k/judge/in_1..in_5.jsonl`): **only**
  `{"j": "<6-char opaque id>", "sk": "<Slovak>", "en": "<answer>"}`. In Phase 1k the judge saw no
  reference, no intent, no source side and no annotation — §0 makes the Slovak the sole ground truth.
- Judge output, TSV, one row per judged item (`phase1k/judge/out_1..out_5.tsv`), verbatim shapes:
  - correct: `<j>\tC`
  - wrong:   `<j>\tW\t<TYPE>` with TYPE in `T | W | M | S | V | E`
  Observed rows: `952852\tW\tT`, `180f61\tC`, `cb67ad\tW\tM`.
- Key file, forbidden to the judge (`phase1k/judge/key.jsonl`):
  `{"j": "72300f", "id": "C:10013:204106987", "sid": 10013, "source": "dev|fresh|control|holdout1j", "dup_of": <j or null>}`.
- Item record (`phase1k/fresh/items_fresh.jsonl`): `{id, sid, text, intent}`.
- Writer input (`phase1k/fresh/writer_input.jsonl`): `{wid, slovak, level, topic}` and nothing else.
- Writer output (`phase1k/fresh/writer_output.jsonl`): one line per sentence,
  `{"wid": 140001, "answers": [{"text": "…", "intent": "C|T|W|M|S|V|TF"}, …]}`.
- **Judge noise controls**: N = 60 duplicate items, drawn with a fixed seed, given a SECOND opaque id
  and forced into a different chunk than their original; chunking = 4 equal shuffled chunks with seed
  `phase1k-judge` (control seed `phase1k-control`). The 1k judge agreed 60/60 on the controls; the
  report records the caveat that same-session controls bound within-session inconsistency only.
- Judge protocol inherited from `phase1j/CONTEXT_1J.md` §6: blind, per item, the pass must be recorded
  **before any checker verdict for those items exists**, doubts marked and resolved explicitly.
  No standalone verbatim judge-instruction file exists on disk in 1j or 1k; the judge was given the
  §0 rule verbatim (report §2.3) plus the type list.

## (c) How the sentences were stratified over A1 / A2 / B1 / B2

**The Phase 1c stratification rule itself is nowhere stated in the Phase 1k materials.** What 1k states
is only that it inherited the proportions:

- `phase1k/HANDOFF_P.md` §1: `level A1/A2/B1/B2 | 6/16/25/23 | 6/16/25/23 (= DEV 70 of 1j)`
- report §2.1: `| level A1/A2/B1/B2 | 6/16/25/23 | = the 1j DEV proportions |`

So for 70 sentences the target is A1 6, A2 16, B1 25, B2 23 (≈ 8.6 % / 22.9 % / 35.7 % / 32.9 %). For a
**140-sentence** set the same proportions give A1 12, A2 32, B1 50, B2 46. The other composition
targets the 1k annotator had to hit, scale the same way (1k actuals in brackets):

| dimension | 1k target over 70 (actual) |
|---|---|
| `tf_gold` spread | past 21 · future 20 · present 19 · conditional 8 · mixed 2 |
| `voice_sk` | impersonal + passive >= 10 (impersonal 6, passive 5; active 59) |
| `agent_nom` (nominative agent + transitive) | >= 42 (43) |
| perfective-present futures | >= 12 (13, 5 of them without a time adverbial) |
| `bude` + infinitive futures | >= 6 (6) |
| conditionals (`by`) | >= 8 (8) |
| plain present | >= 15 (19) |
| past total | >= 20 (21) |
| past imperfective (`tense_open`) | >= 10 (10) |
| Slovak length | 6-18 words (actual 6-11) |
| overlap with existing sentences | 0 sk dups / 0 en dups / max Jaccard < 0.50 (0 / 0 / 0.27) |

If Phase 1m wants the real Phase 1c rule (and not just these inherited proportions), someone with a
phase1c read permission has to fetch it; this recon did not open phase1c.

## Gaps worth knowing

- No verbatim, standalone prompt file exists on disk for the sentence writer, the answer writer or the
  judge in Phase 1k — only the §0 rule text, the schemas and the quota code. The blind-side files in
  `phase1m/tasks/` are the reconstruction, quoting verbatim wherever verbatim text exists.
- Type **E** has no definition anywhere (see `TYPE_DEFS.md`).
- The Phase 1k report's writer-intent table labels intent `S` "subject recast"; the canonical S
  definition is the small-slip family from `phase1j/CONTEXT_1J.md` §6.

# Phase 1V / Track B — annotation cost of production sentences (0 Gemini calls, DB read-only)

Files: `trackb.py` (gold + arm-B rewrite + annotation tables + measurement), `sample_raw.json` (DB pull),
`trackb_results.json` (all rows, both states, every error). Model calls: **0 planned, 0 counted, 0 failed,
0 retried, $0.00.** Harness tool calls: 10.

## Finding that shapes everything below
The "unchanged 1N/1M pipeline" contains **no Gemini stage**. The arm-B rewrite is hand-authored agent work
(`phase1j/taskB/apply_rewrite.py` header: "The decision table below is agent B's own linguistic work"),
and so is the 1M/1N annotation (`phase1m/make_annotations_part2.py`: "Hand-written, 0 model calls").
So there is no `usageMetadata` to read. Tokens below are the size of the AUTHORED ARTEFACTS (JSON per
sentence, tiktoken absent -> UTF-8 bytes / 4). They are OUTPUT tokens only; the authoring agent's input,
context re-reads and reasoning are not observable from inside the agent and are NOT included.

## Sample
SELECT only (Supabase CLI, `--linked`): `exercise_localizations` sk + en `full_sentence`, level from
`exercise_types.level`, 15 per level A1/A2/B1/B2 (legacy level `B` excluded), deterministic order
`md5(exercise_id || 'phase1v-B')`. 60 real sentences, none invented.

## B1 — rewrite need and token cost
- Needed an arm-B rewrite: **30/60 = 50.0 % [36.81, 63.19]** (1J: 91/140 = 65.0 %; Fisher p = 0.058).
  By level A1 3/15, A2 6/15, B1 10/15, B2 11/15 — production A1/A2 sentences mostly already name the subject.
  Untouched: 29 explicit subject, 1 impersonal. 5 of the 30 insertions are in an embedded clause (21, 31, 42, 44, 52).
  Every rewrite passed the 1J machine check (old tokens + exactly the pronoun).
- Tokens/sentence, REWRITE: **28.3** over all 60 (34.7 per rewritten sentence); total 1,699.
- Tokens/sentence, ANNOTATION (1M/1N schema: v, lk, alt, tf_gold, voice_sk, agent_nom,
  perfective_present, tense_open): **84.0**; total 5,039. By level A1 81.0 / A2 78.1 / B1 85.5 / B2 91.3.
- Gold (if production needs it as well): 50.0 tok/sentence.

## B2 — deterministic guards, gold validation BEFORE (raw DB) and AFTER (rewrite + annotation)
Method = `phase1t/taskB/cz_validate.py` g1-g4 + e2e executed UNCHANGED (body exec'd from the file), same
AGREE / CONSERVATIVE / ERROR definitions. Readers are text-only as in 1T; e2e = AG v3 `decide` fed the EN
reference as the answer (ann = {} before; ann = my annotation after).
Gold: written by THIS agent from the Slovak alone to `GOLD_SPEC_SK.md`, before any guard ran. **Deviation
from 1T:** 1T used blind separate annotators (two, cz + sk); this is ONE annotator who also did the rewrite
and the annotation, so annotation-vs-gold agreement is circular and not reported as a result. AFTER gold =
BEFORE gold with the inserted pronoun as main subject (voice -> active_agent, agent_nom true) or appended to
embedded_agents.

| guard (n = 60) | BEFORE ERROR [95 % CP] | AFTER ERROR [95 % CP] | AGREE b/a | CONS b/a |
|---|---|---|---|---|
| g1 F9 time frame | 2 = 3.33 % [0.41, 11.53] | 3 = 5.00 % [1.04, 13.92] | 41/41 | 17/16 |
| g2 F4v2 person/number | 2 = 3.33 % [0.41, 11.53] | 2 = 3.33 % [0.41, 11.53] | 12/36 | 46/22 |
| g3 AG agent reader v2 (= v3) | 30 = 50.00 % [36.81, 63.19] | 20 = 33.33 % [21.69, 46.69] | 23/26 | 7/14 |
| g4 voice v2 (SK_REFLEX) | 8 = 13.33 % [5.94, 24.59] | 15 = 25.00 % [14.72, 37.86] | 52/45 | — |
| g4 voice v3 | 10 = 16.67 % [8.29, 28.52] | 19 = 31.67 % [20.26, 44.96] | 50/41 | — |
| e2e AG v3 rejects the correct EN reference | 0 | 0 (ann empty and ann used) | | |

- **AG reader vs 1T:** 30/60 = 50.0 % [36.81, 63.19] on raw production vs 1T's 47/120 = 39.17 % [30.4, 48.5]
  (Fisher p = 0.20, not different). v3 = v2 on every row, as in 1T. Mechanism: the reader returns the
  sentence-initial token as "agent" (`Pod`, `Na`, `V`, `Pozri`, `Hádaj`, `Ak`, `Do` ...). The rewrite fixes
  it only where the pronoun lands sentence-first (10 fixed); where the pronoun follows a fronted phrase
  (22, 25, 28, 35, 46, 47, 49, 50) the error remains with a different gold; 12 untouched explicit-subject
  sentences keep their error. Arm-B does not repair this reader; it is a reader bug.
- **g4 rise is a gold-definition artefact, not a reader change:** SK_REFLEX is a text regex and the pronoun
  adds no `sa/si`. 1T's ERROR_as_passive counts only gold active_agent; the rewrite turns 7 (v2) / 9 (v3)
  prodrop sentences that already carried an ordinary reflexive `si/sa` (6, 17, 39, 51, 53, 55, 60; v3 also
  50, 57) into active_agent. Like-for-like the reader errs on 15 (v2) / 19 (v3) of 60 in both states.
- g1: before 35, 47; after 31 (new: pronoun in the relative clause), 35, 47. Cause of 31 not inspected (budget).
- g2: 54 fixed; 21 new (embedded `oni tancujú` read as main-clause 3pl, gold 3sg `Jedlo`); 56 in both.
  AGREE rises 12 -> 36: the rewrite converts abstentions into correct person readings.

## B3 — extrapolation to 5,895 sentences
Model: **linear**. No saturation signal: each sentence is authored independently, per-sentence annotation
size rises with level (81 -> 91) and rewrite need rises with level (3 -> 11 of 15); nothing is reused.
- Rewrites expected: 2,948 [2,170, 3,725] (CP band scaled).
- Authored output tokens: rewrite 166,927 + annotation 495,082 = **662,008** (+ 294,750 if gold is also needed).
- Gemini checking calls for the preparation: **0**; Gemini wall-clock: 0 (no tier rate applies).
- Agent wall-clock (assumption, not measured): at ~50 output tok/s effective, 662k tok ≈ 3.7 h pure
  generation; in batches of 60 that is ~99 agent batches, each paying its own context/input tokens, which
  dominate and are unmeasured here.
Assumptions: level mix of the 5,895 = equal quarter per A1-B2 (unknown; rewrite need is level-driven, so a
B-heavy mix raises it); artefact size of this sample is representative; bytes/4 ≈ tokens for Slovak/English
JSON (tokeniser absent); a single agent annotator's quality is acceptable (not verified blind here).

## Items not done
- usageMetadata-based token counts: not possible — the pipeline has no Gemini call (see top).
- Blind second annotator for the gold: not done (no sub-agent available within the 12-call limit).

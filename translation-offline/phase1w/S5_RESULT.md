# Phase 1W §5 Track B result (0 Gemini calls, DB read-only)

Model: claude-opus-5 (`--model opus`); 1V's annotation/rewrite were hand-authored by a Claude Code sub-agent on the session model (Opus), so Opus is the consistent choice.
Harness: bundled claude 2.1.275, `-p --output-format json --max-turns 12`, prompt carries the batch inline, answer = JSON array, no tools used (num_turns 1 each).
Sample: 60 fresh production SK sentences, 15/level A1-B2, order md5(exercise_id||'phase1w-B'), 1V's 60 ids excluded (overlap 0); ids in trackB/sample_raw.json.
Batch N = 30 sentences per session; sessions: 2 rewrite + 2 annotation + 2 blind gold = 6; durations 28.2-69.2 s each, sum 376.9 s, driver wall 118.1 s (parallel).

## 5.1 Harness tokens per session
gold_b1: input 2 / cache_creation 11110 / cache_read 20777 / output 3056 / turns 1 / $0.1979 / 28.2 s
gold_b2: input 2 / cache_creation 11416 / cache_read 20777 / output 3360 / turns 1 / $0.2086 / 29.2 s
rewrite_b1: input 2 / cache_creation 11676 / cache_read 20777 / output 3923 / turns 1 / $0.2252 / 36.9 s
rewrite_b2: input 2 / cache_creation 12191 / cache_read 20777 / output 4483 / turns 1 / $0.2444 / 38.2 s
annot_b1: input 2 / cache_creation 10206 / cache_read 22462 / output 6925 / turns 1 / $0.2864 / 58.1 s
annot_b2: input 2 / cache_creation 10717 / cache_read 22462 / output 8325 / turns 1 / $0.3265 / 69.2 s

Rewrite tok/sentence incl cache reads: 1230.5
Rewrite tok/sentence excl cache reads: 538.0
Rewrite output tok/sentence: 140.1 (1V bytes/4: 28.3)
Rewrite $/sentence: 0.00783
Annotation tok/sentence incl cache reads: 1351.7
Annotation tok/sentence excl cache reads: 603.0
Annotation output tok/sentence: 254.2 (1V bytes/4: 84.0)
Annotation $/sentence: 0.01022
Gold tok/sentence incl cache reads: 1175.0 (excl 482.4)
Fixed context per session: ~20.8k cache_read + ~10-12k cache_creation (Claude Code system prompt + tools + prompt); ~1.07k tok/sentence of it at N=30
Rewrites: 30/60 = 50.0 %; machine-check failures: 0
1V's 662,008 was off by: x22.99 (all harness tokens), x10.16 (excl cache reads), x3.51 (output only incl thinking)

## 5.2 Annotation vs blind gold (separate session, Slovak only), n = 60
tf: 59/60 = 98.33 %
person: 60/60 = 100.0 %
voice: 60/60 = 100.0 %
agent_nom: 60/60 = 100.0 %
subject_exact: 60/60 = 100.0 %
subject_lenient: 60/60 = 100.0 %
Exact match per sentence (tf, person, voice, agent_nom, subject): 59/60 = 98.33 %
Exact match on the 30 unrewritten sentences (no pronoun hint): 29/30
Rewrite decision (main-clause insert) vs gold active_prodrop: 57/60 = 95.0 %
Caveat: gold and annotation are the SAME model with the SAME definitions, blind to each other but not independent annotators; on the 30 rewritten sentences the subject is the inserted pronoun, which makes subject/voice agreement easy. This is model self-consistency, not human-verified accuracy.
Disagreements (annotation vs gold):
- n29 (19046, A2) Počkaj päť minút a podlaha bude suchá. | tf: ann='future' gold='present'
Disagreements (rewrite decision vs gold):
- n24 (33609, A2) Počuj, povedal mi, že on sa chystá púšťať šarkana na každej streche v meste. | rewrite=U/None/None gold voice=active_prodrop subj=None
- n29 (19046, A2) Počkaj päť minút a podlaha bude suchá. | rewrite=U/None/None gold voice=active_prodrop subj=None
- n30 (14080, A2) Svieti červená. Mal by si počkať na chodníku. | rewrite=R/main/ty gold voice=active_agent subj='červená'

## 5.3 Re-extrapolation to 5,895 sentences
Assumptions: linear in sentences; batches of N = 30 (197 sessions per stage); same level mix as the stratified sample (equal quarters); per-session fixed context as measured (cache warm for the 20.8k prefix); Opus list prices as reported by total_cost_usd; no retries; gold not needed in production (shown separately).
Rewrite: 7,253,896 tok incl cache reads / 3,171,215 excl / $46.14
Annotation: 7,968,173 tok incl cache reads / 3,554,390 excl / $60.22
Rewrite + annotation total: 15,222,069 tok incl cache reads / 6,725,605 excl / 2,324,202 output
Rewrite + annotation dollars: $106.36
Blind gold (if wanted): 6,926,625 tok / $39.93
Batch count: 394 sessions (197 rewrite + 197 annotation), +197 if gold
Wall-clock serial: 5.52 h; at 4 parallel sessions ~1.4 h (measured 4-way parallel ran without error)
Larger N lowers the ~32k fixed context share (at N = 30 it is ~80 % of all tokens); not measured beyond N = 30.
Gemini calls: 0. DB: SELECT only. Files: trackB/run_s5.py, sample_raw.json, session_*.json, s5_results.json, s5_rows.json, run_s5.log.

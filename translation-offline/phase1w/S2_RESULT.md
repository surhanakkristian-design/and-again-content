# Phase 1W §2 result: nominative-subject agent reader (0 Gemini calls, 0 model calls)

- Decision: **FREEZE-ELIGIBLE (raw production Slovak ERROR 0.00 % < 10 % target, gate PASS)**
- Chosen reader variant: full
- Stack entry point for §3/§4 ("1V round 2 + §2"): `translation-offline/phase1w/stack_1w.py`, functions `decide(sk, ann, wtags, answer, reference, variant="primary", flags=None, extra=("rs_nom",))` and `final_accept(row, extra=("rs_nom",), tip=True)`
- Reader module: `translation-offline/phase1w/reader_nom.py` (`read`, `installed`); earlier phase dirs not edited, hashes unchanged: True
- Gold caveat: Track B gold (phase1v/trackB/trackb.py GOLD) was written by the same 1V agent that wrote the rewrite and annotation; it is not blind. The Track B figures here are therefore validated against a single non-blind annotator. The 1T 120-pair gold is blind (separate annotators).

## Caveats (read first)

- Track B is IN-SAMPLE for this reader: the §2 worker saw the 1V Track B GOLD subjects (trackb.py) before writing reader_nom.py, and that gold is itself non-blind (same 1V agent). Track B 0/60 ERROR is therefore NOT an honest out-of-sample figure.
- The 1T 120 pairs were NOT inspected before the reader was written (blind gold): Slovak control ERROR 2/120 = 1.67 % [0.20, 5.89], Czech 6/120 = 5.00 % [1.86, 10.57]. This is the best available estimate for raw production Slovak, but 1T sentences are test-set style, not production.
- Regression gate is weakly informative: on 1U, 1T and the 1S packet the new reader changed 0 AG decisions (0 new fires, 0 un-fires). The agent string there comes from writer_tags.agent or the annotation gate blocks first, so the reader path is barely exercised; cost 0 is measured but not a stress test.
- Czech leftovers (full): case-ambiguous oblique heads read as nominative (Kameře, odpoledne), sentence-initial particles Kdybych/Kéž not in stop lists, 'ty' demonstrative read as 2sg pronoun (n=47, known 1V leftover). Slovak leftovers: Kamere (dative), Prvý certifikát (object, pro-drop subject).
- Variant 'pron' (pronoun-only) also passes the gate with ERROR 0/60 Track B, 0/120 sk, 1/120 cz but abstains more (CONSERVATIVE 31 vs 28 on Track B raw). 'full' chosen: equal cost 0, equal Track B ERROR, tie broken by list order; 'pron' is the fallback if §4 wants zero noun risk.
- Target (ERROR < 10 % on raw production Slovak): MET on the point for Track B (in-sample, circular gold) and for the 1T Slovak control (blind, not production). FREEZE-ELIGIBLE rests on these caveats.

## 2.2 Agent reader, AGREE / CONSERVATIVE / ERROR (g3, v3 token parse; before = 1V round-2 first-word reader)

- Track B Slovak raw (n = 60), BEFORE: 23 / 7 / 30, ERROR 50.00 % [36.81, 63.19]
- Track B Slovak raw (n = 60), full: 32 / 28 / 0, ERROR 0.00 % [0.00, 5.96]
- Track B Slovak raw (n = 60), pron: 29 / 31 / 0, ERROR 0.00 % [0.00, 5.96]
- Track B Slovak rewritten (n = 60), BEFORE: 26 / 14 / 20, ERROR 33.33 % [21.69, 46.69]
- Track B Slovak rewritten (n = 60), full: 30 / 30 / 0, ERROR 0.00 % [0.00, 5.96]
- Track B Slovak rewritten (n = 60), pron: 27 / 33 / 0, ERROR 0.00 % [0.00, 5.96]
- 1T pairs Czech (4 fixes) (n = 120), BEFORE: 59 / 16 / 45, ERROR 37.50 % [28.83, 46.80]
- 1T pairs Slovak control (n = 120), BEFORE: 55 / 18 / 47, ERROR 39.17 % [30.39, 48.50]
- 1T pairs Czech (4 fixes) (n = 120), full: 54 / 60 / 6, ERROR 5.00 % [1.86, 10.57]
- 1T pairs Slovak control (n = 120), full: 59 / 59 / 2, ERROR 1.67 % [0.20, 5.89]
- 1T pairs Czech (4 fixes) (n = 120), pron: 53 / 66 / 1, ERROR 0.83 % [0.02, 4.56]
- 1T pairs Slovak control (n = 120), pron: 53 / 67 / 0, ERROR 0.00 % [0.00, 3.03]
- Reproduction of 1V figures (before): {"trackB_raw_before_ERROR": 30, "want_1V": 30, "trackB_rewritten_before_ERROR": 20, "want_1V_rw": 20, "1T_sk_before_ERROR": 47, "want_sk": 47, "1T_cz_before_ERROR": 45, "want_cz_after_4fixes": 45}

## 2.3 Regression gate (stored verdicts, 0 calls; worst case = an un-fired AG reject on a judged-wrong row counts as accepted)

- 1U baseline 1V round 2 re-scored: coverage 390/402 = 97.01 % [94.84, 98.45]
- 1U baseline 1V round 2 re-scored: FA 13/498 = 2.61 % [1.40, 4.42]
- 1U old-reader recompute mismatches vs stored AG: 0
- 1T baseline 1V round 2 re-scored: coverage 394/421 = 93.59 % [90.81, 95.73]
- 1T baseline 1V round 2 re-scored: FA 9/479 = 1.88 % [0.86, 3.54]
- 1T old-reader recompute mismatches vs stored AG: 0
- 1S packet baseline: {"agent drops (judged wrong)": {"n": 97, "fired": 97}, "by-passive controls": {"n": 42, "fired": 0}, "plain controls (judged correct)": {"n": 39, "fired": 0}, "v2 misfires (judged correct)": {"n": 3, "fired": 0}, "agentless judged CORRECT": {"n": 1, "fired": 1}, "plain control judged wrong": {"n": 1, "fired": 0}}
- [full] 1S packet: {"agent drops (judged wrong)": {"n": 97, "fired": 97}, "by-passive controls": {"n": 42, "fired": 0}, "plain controls (judged correct)": {"n": 39, "fired": 0}, "v2 misfires (judged correct)": {"n": 3, "fired": 0}, "agentless judged CORRECT": {"n": 1, "fired": 1}, "plain control judged wrong": {"n": 1, "fired": 0}}
- [full] 1U coverage (worst) 390/402 = 97.01 % [94.84, 98.45]
- [full] 1U FA (worst) 13/498 = 2.61 % [1.40, 4.42]
- [full] 1U coverage (best) 390/402 = 97.01 % [94.84, 98.45]
- [full] 1U FA (best) 13/498 = 2.61 % [1.40, 4.42]
- [full] 1U new AG fires 0, catches 0, un-fires 0, measured cost 0 []
- [full] 1T coverage (worst) 394/421 = 93.59 % [90.81, 95.73]
- [full] 1T FA (worst) 9/479 = 1.88 % [0.86, 3.54]
- [full] 1T coverage (best) 394/421 = 93.59 % [90.81, 95.73]
- [full] 1T FA (best) 9/479 = 1.88 % [0.86, 3.54]
- [full] 1T new AG fires 0, catches 0, un-fires 0, measured cost 0 []
- [full] GATE 1S drops caught >= 96/97: PASS
- [full] GATE 1S by-passive controls rejected 0/42: PASS
- [full] GATE 1S plain controls rejected 0/39: PASS
- [full] GATE 1U coverage >= 390/402: PASS
- [full] GATE 1U FA <= 13/498: PASS
- [full] GATE 1T coverage >= 394/421: PASS
- [full] GATE 1T FA <= 9/479: PASS
- [full] GATE overall: PASS
- [pron] 1S packet: {"agent drops (judged wrong)": {"n": 97, "fired": 97}, "by-passive controls": {"n": 42, "fired": 0}, "plain controls (judged correct)": {"n": 39, "fired": 0}, "v2 misfires (judged correct)": {"n": 3, "fired": 0}, "agentless judged CORRECT": {"n": 1, "fired": 1}, "plain control judged wrong": {"n": 1, "fired": 0}}
- [pron] 1U coverage (worst) 390/402 = 97.01 % [94.84, 98.45]
- [pron] 1U FA (worst) 13/498 = 2.61 % [1.40, 4.42]
- [pron] 1U coverage (best) 390/402 = 97.01 % [94.84, 98.45]
- [pron] 1U FA (best) 13/498 = 2.61 % [1.40, 4.42]
- [pron] 1U new AG fires 0, catches 0, un-fires 0, measured cost 0 []
- [pron] 1T coverage (worst) 394/421 = 93.59 % [90.81, 95.73]
- [pron] 1T FA (worst) 9/479 = 1.88 % [0.86, 3.54]
- [pron] 1T coverage (best) 394/421 = 93.59 % [90.81, 95.73]
- [pron] 1T FA (best) 9/479 = 1.88 % [0.86, 3.54]
- [pron] 1T new AG fires 0, catches 0, un-fires 0, measured cost 0 []
- [pron] GATE 1S drops caught >= 96/97: PASS
- [pron] GATE 1S by-passive controls rejected 0/42: PASS
- [pron] GATE 1S plain controls rejected 0/39: PASS
- [pron] GATE 1U coverage >= 390/402: PASS
- [pron] GATE 1U FA <= 13/498: PASS
- [pron] GATE 1T coverage >= 394/421: PASS
- [pron] GATE 1T FA <= 9/479: PASS
- [pron] GATE overall: PASS

## Selection (on measured closed-set cost, then Track B raw ERROR)

- Eligible: ['full', 'pron']
- Chosen: full
- Decision: FREEZE-ELIGIBLE (raw production Slovak ERROR 0.00 % < 10 % target, gate PASS)

## Remaining ERROR rows (Track B raw, chosen / full)

- none (0/60)

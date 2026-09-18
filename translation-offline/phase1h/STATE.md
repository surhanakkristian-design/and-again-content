# Phase 1h — builder state (18 Sept 2026)

## Done (all before the freeze, in this order)

1. **Frozen data protected.** Every regular file in `phase1c/ phase1e/ phase1f/ phase1g/` is now `a-w`;
   `git status --short -- translation-offline` shows nothing modified there. No previous-phase runner is
   imported: `phase1h/lib_prev.py` is a byte copy of `phase1g/lib_prev.py` (its `HERE` resolves to
   `phase1h/`), `phase1h/checker_1h.py` is `phase1g/run_phase1g.py` with every path constant moved to
   `phase1h/` (own `calls.jsonl`, `decisions.jsonl`, `call_log.jsonl`, own results). The 1e/1f/1g ledgers
   are opened read-only as byte-identical seeds and are used **only for the OLD sets**. The module is
   import-safe.
2. **§2.1 L2 lock, non-verb spans.** `lock_equivalent_ok()` releases a lock when an *equivalent preposition
   or linker* is present. Only for locks that are prepositions/relativisers/linkers (never a verb pattern),
   only through groups that already exist (`phase1c/synonyms/{table,ng_phase1c,review_added}.json` and the
   item's own `alt`), and the equivalent must itself be a preposition/linker. No new word table.
   Effect on the 80: 2 items released — `C:23669:2842578131` ("over" vs lock "above", the case in the
   brief) and `C:10107:4080641578`.
3. **§2.2 F2B span match.** `en_span_tokens(it)` extends `EN_SPAN` with the renderings this item's own
   annotation already accepts (`p` "+word" insertions, `alt` members of a span that contains an EN_SPAN
   word, co-members of the existing synonym groups). `C:9498:582627860` ("entire school" for "celá") is no
   longer downgraded; `W:10366:3357618811` is still caught. General, not id-specific.
4. **§2.3 reference hygiene** — `phase1h/reference_hygiene.py`, deterministic, zero model tokens, runs on
   any annotation file in the Phase 1c format, writes only into `phase1h/`.
   (a) Reference-only content is marked OPTIONAL in the annotation's `d` (which the checker already reads):
       from the annotators' own `p:"-span"` entries and from an `alt` member that is a strict token
       subsequence of the span with particle/adverb-only remainder. **8 of 80** sentences touched
       (1018, 10866, 16403, 21467, 5595, 9244, 9495, 9992). F5 stops killing `C:9244` ("rolling in") and
       `C:9992` ("up").
   (b) The `g` gender chain is added when F4v2's Slovak reader leaves person/gender open. Tightened before
       the freeze: the reader *abstains* on an l-participle without a past marker, so a gender-shaped word
       in the Slovak (`_gender_signal`) blocks the chain. Otherwise 22 of 80 got a chain and one of them
       turned a wrong answer into an acceptance. **1 of 80** touched after the tightening.
       `gender_variants()` then expands the accepted variants for F3/F5/F2B.
   Report: `phase1h/hygiene_report_old.json` (counts, every touched id, 10 examples per half with
   before/after). Hygiene output: `phase1h/hygiene/annotated/*.json` (in-memory at run time as well).
5. **Harness** in `checker_1h.py`: `--selftest --hygiene <file|dir> --plan --calls --tabulate --all`.
   Two configurations only: row 7 = F1F2F3F4v2F5F2B × P-B, row 8 = same × P-C. Prompts byte-identical to
   Phase 1g (`base.prompt` + the P-C line). `gemini-3.1-flash-lite`, no thinking, 24 output tokens,
   SAME/TIP/DIFF; an unparsable reply is a FAILED call (counted, never guessed, never retried into a
   guess). `CAP = 1500` in code, 7 threads, 429 backoff inherited from `lib_prev.call_model`, ledger-locked
   writes, resumable, per-call latency and token usage recorded. Priority fresh P-B → fresh P-C → old P-B →
   old P-C; reuse of the 1e/1f/1g ledgers only for OLD items (`verdict_map_own` for fresh). Items left
   without a verdict at the cap are written to `call_counts.json` as `not_measured`.
6. **Regression on the 80 (offline, 0 model calls).** `results_1h_20260918T155021Z.json`:
   | row | coverage /235 | 95 % CP | strict FA | raw FA | false rejections |
   |---|---|---|---|---|---|
   | 7 (P-B) | **216** (was 213) | 87.7–95.1 % | 2 (`W:16403:624976382`, `W:1452:1471817457`) | 10 | L3 16 · L2 2 · F5 1 |
   | 8 (P-C) | **221** (was 218) | 90.2–96.7 % | 3 (+ `W:10366:36005249`) | 11 | L3 11 · L2 2 · F5 1 |
   Strict FA is unchanged against Phase 1g (same ids). **7 newly accepted wrong-set items were never
   judged by Phase 1f** (`W:1018:1251085634, W:14266:664063167, W:1452:3166274700, W:5595:3623849236,
   W:5595:1942575047, W:9244:3038274947, W:8824:241327957`); they are reported as
   `accepted_but_unjudged`, never counted as FA. **A judge must rule on these 7** — most of them are
   exactly the "reference added content" family that hygiene (a) unblocked, so several are probably not
   real errors, but that is a judgement, not a measurement.
   **Prompt bytes: the prompt contains only Slovak / reference / learner / topic — it does NOT include the
   annotations, so hygiene changed 0 prompts.** §2.1 sends 1 previously L2-vetoed item to L3, i.e.
   **2 new calls** (1 × P-B, 1 × P-C) are needed on the old sets; `--plan` prints exactly that.
7. **FREEZE**: commit `0abfafd40a6a768cfa1c3c69cfc43482e0d9979b`, tag `translation-offline-phase1h-FROZEN`,
   hashes in `phase1h/FREEZE.md`.
8. **After the tag**: `select_new_sentences.py` (seed 20260919) wrote `fresh/new_sentences_60.jsonl` and
   `fresh/writer_input_140.jsonl` (80 old + 60 new, only sid/sk/level/topic). Pool 132 unused sentences
   from the same local source Phase 1c drew from (`measurements/selection.json`, `pilot/coverage_input.json`);
   99 of them carry a tier-1 topic (the topic set of the 80). Levels 9 A1 / 12 A2 / 21 B1 / 18 B2 = the
   Phase 1c proportion (12/16/28/24 of 80). Zero overlap by id and by Slovak text.

## Left / not done
- **Only 2 sentences of 13–16 Slovak words** could be selected: the whole unused pool contains just two.
  The 13–16 band is still tabulated (on the 80 it is 6/6), but it will stay thin. Nothing can be done
  without a new sentence source, which would be a DB read Phase 1c did not do either.
- No model call was made in this task; `phase1h/calls.jsonl` is empty and `call_counts.json` unwritten.
- Cost per L3 call and per active user per month: `tabulate_1h()` records tokens and latency and points at
  `lib_prev.PRICE` and the Phase 1e usage assumption; **the per-user monthly figure must be restated by
  hand in the report from `phase1e/REPORT_PHASE1E.md`** — it is not re-derived in code.
- Errors noticed and deliberately NOT fixed (no rule invented for them): the `si` clitic still blocks every
  person signal (Phase 1g §3a); F5 still fires on `C:11348:1001085647` ("now"/"práve", defensible);
  the L3 model still rejects faithful answers that use the other gender even where the Slovak leaves it
  open — the `g` chain only reaches F3/F5/F2B, not the prompt (that would need a prompt change, which §2
  does not allow).

## Exact next commands

**(a) Annotator — the 60 new annotations.**
Template: `phase1c/annotated_after/10013.json` (fields `id,t,lv,v,lk,s,d,g,p,m,alt`).
Spec: `translation-offline/GENERATION_SPEC.md` + `phase1c/BRIEF.md` §4, task prompts
`phase1c/tasks/batchS.md` and `phase1c/tasks/batchL.md` (they produced the 80). Write one file per
sentence to `phase1h/fresh/annotations_new_60/<sid>.json`. Do NOT pre-apply hygiene — it is applied at
load time. Input list: `phase1h/fresh/new_sentences_60.jsonl`.
Then check it loads:

    python3 phase1h/reference_hygiene.py phase1h/fresh/annotations_new_60 phase1h/hygiene_new

**(b) Writers / judges.** Blind input is `phase1h/fresh/writer_input_140.jsonl` only. Answers go to
`phase1h/fresh/correct_part*.jsonl` and `wrong_part*.jsonl`, judgements to
`phase1h/fresh/judgements.jsonl`. Schema and the REQUIRED `chk` block (the existing offline checker's
verdict per answer, without which fresh items can never be accepted at L1): `phase1h/FRESH_SCHEMA.md`.

**(c) Measuring agent.**

    cd /Users/kristiansurhanak/Projects/and-again-content/translation-offline
    python3 phase1h/checker_1h.py --selftest
    python3 phase1h/checker_1h.py --hygiene phase1h/fresh/annotations_new_60
    python3 phase1h/checker_1h.py --plan          # must stay under 1500
    python3 phase1h/checker_1h.py --calls         # GEMINI_API_KEY from ~/Projects/and-again/.env.local
    python3 phase1h/checker_1h.py --tabulate

Add in a SEPARATE non-checker file (do not touch the frozen ones): the side-by-side in-sample vs
out-of-sample table, FA split by wrong-type with CP intervals on the fresh set, the grouping of the false
rejections by cause (the raw dump with `cause` and the asserted totals is already in
`results_1h_*.json`), and the cost paragraph.

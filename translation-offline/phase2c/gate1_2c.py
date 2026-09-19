#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phase 2C GATE 1 SCORE (0 model calls, 0 DB, 0 new gold).

Re-validates the three reader patches of derive_2c.py on 2B's frozen 200-sentence sample
(phase2b/sample_2b.json, sk 1..100 / cz 101..200) against 2B's EXISTING blind gold
(phase2b/run_2b_results.json -> outputs.gold_sk / gold_cz = run 2, the run results_2b.json scored).

Per language (sk, cz) and pooled, per field: n AGREE / n CONSERVATIVE (script abstains) / n ERROR and
ERROR-of-decided = ERROR/(AGREE+ERROR) with EXACT 95 % Clopper-Pearson intervals, BEFORE and AFTER,
plus three single-patch ablations for attribution.  Classification logic is copied verbatim from
phase2b/score_2b.py §2.3 so that "before" must reproduce results_2b.json (asserted).

Writes: gate1_2c.json, GATE1.md, derived_2c.json (after rows)."""
import os, re, sys, json, math, collections
sys.dont_write_bytecode = True
BASE = os.path.expanduser("~/Projects/and-again-content/translation-offline")
HERE = os.path.join(BASE, "phase2c")
sys.path.insert(0, HERE)
import derive_2c as D                                     # noqa: E402

WORD = re.compile(r"[a-záäčďéěíĺľňóôöŕřšťúůüýž]+", re.I)   # verbatim from score_2b.py
words = lambda s: set(WORD.findall((s or "").lower()))
nrm = lambda x: None if x is None else str(x).strip().lower()


def cp(k, n, a=0.05):                                      # verbatim from score_2b.py (exact Clopper-Pearson)
    if n == 0:
        return [None, None]
    def cdf(x, p): return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(x + 1))
    def bis(f):
        lo, hi = 0.0, 1.0
        for _ in range(60):
            mid = (lo + hi) / 2
            if f(mid): lo = mid
            else: hi = mid
        return (lo + hi) / 2
    lo = 0.0 if k == 0 else bis(lambda p: 1 - cdf(k - 1, p) < a / 2)
    hi = 1.0 if k == n else bis(lambda p: cdf(k, p) > a / 2)
    return [round(100 * lo, 2), round(100 * hi, 2)]


def rate(k, n): return {"k": k, "n": n, "pct": round(100 * k / n, 2) if n else None, "cp95": cp(k, n)}

FIELDS = {"voice_sk": "voice", "agent_nom": "subject", "person": "person", "number": "number",
          "gender": "gender", "tf": "tf", "tense_open": "tense_open", "perfective_present": "perfective_present"}
ORDER = ["voice_sk", "agent_nom", "person", "number", "gender", "tense_open", "perfective_present", "tf"]
EXPECT_2B = {"voice_sk": 17.2, "agent_nom": 26.1, "tf": 14.1, "gender": 14.9, "tense_open": 32.4,
             "number": 3.5, "perfective_present": 6.0}          # pooled ERROR_of_decided quoted in the brief


def classify(f, dvv, g):
    gk = FIELDS[f]
    if dvv is None:
        return "CONSERVATIVE"
    if f == "agent_nom":
        return "AGREE" if (words(dvv) & words(g.get("subject"))) else "ERROR"
    if f in ("tense_open", "perfective_present"):
        return "AGREE" if bool(dvv) == bool(g.get(gk)) else "ERROR"
    return "AGREE" if nrm(dvv) == nrm(g.get(gk)) else "ERROR"


ROWS = json.load(open(f"{BASE}/phase2b/sample_2b.json", encoding="utf-8"))["rows"]
BY = {r["n"]: r for r in ROWS}
RUN = json.load(open(f"{BASE}/phase2b/run_2b_results.json", encoding="utf-8"))["outputs"]
GOLD = {**{int(k): v for k, v in RUN["gold_sk"].items()}, **{int(k): v for k, v in RUN["gold_cz"].items()}}
REF = json.load(open(f"{BASE}/phase2b/results_2b.json", encoding="utf-8"))["2.3_fields"]
OLD = {r["n"]: r for r in json.load(open(f"{BASE}/phase2b/derived_2b.json", encoding="utf-8"))["rows"]}

CFGS = ["before", "tok", "verbish", "agent", "after"]
DER = {c: {r["n"]: D.derive(r, mode=c) for r in ROWS} for c in CFGS}

# ---------------------------------------------------------------- sanity: "before" == 2B, byte for byte
mismatch = [[n, f] for c in ["before"] for n in OLD for f in FIELDS
            if DER[c][n]["derived"][f]["value"] != OLD[n]["derived"][f]["value"]]
res = {}
for c in CFGS:
    blk = {}
    for f in FIELDS:
        cls = {r["n"]: classify(f, DER[c][r["n"]]["derived"][f]["value"], GOLD[r["n"]])
               for r in ROWS if r["n"] in GOLD}
        per = {}
        for tag in ("pooled", "sk", "cz"):
            ns = [n for n in cls if tag == "pooled" or BY[n]["lang"] == tag]
            cnt = collections.Counter(cls[n] for n in ns)
            dec = cnt["AGREE"] + cnt["ERROR"]
            per[tag] = {"agree": cnt["AGREE"], "conservative": cnt["CONSERVATIVE"], "error": cnt["ERROR"],
                        "n": len(ns), "ERROR_of_decided": rate(cnt["ERROR"], dec),
                        "coverage_decided": rate(dec, len(ns)), "ERROR_of_all": rate(cnt["ERROR"], len(ns))}
        blk[f] = per
        if c in ("before", "after"):
            blk[f]["errors"] = [[n, BY[n]["lang"], BY[n]["src"][:70], DER[c][n]["derived"][f]["value"],
                                 GOLD[n].get(FIELDS[f])] for n in sorted(cls) if cls[n] == "ERROR"][:20]
    res[c] = blk
sanity = {"before_vs_derived_2b_field_mismatches": len(mismatch), "examples": mismatch[:10],
          "before_vs_results_2b_pooled": {f: [res["before"][f]["pooled"]["ERROR_of_decided"]["pct"],
                                              REF[f]["pooled"]["ERROR_of_decided"]["pct"]] for f in FIELDS},
          "brief_quoted_pooled": {f: [res["before"][f]["pooled"]["ERROR_of_decided"]["pct"], EXPECT_2B[f]]
                                  for f in EXPECT_2B}}
sanity["ok"] = (len(mismatch) == 0 and
                all(abs(a - b) < 1e-9 for a, b in sanity["before_vs_results_2b_pooled"].values()) and
                all(abs(a - b) <= 0.06 for a, b in sanity["brief_quoted_pooled"].values()))
if not sanity["ok"]:
    print(json.dumps(sanity, ensure_ascii=False, indent=1)); sys.exit("SANITY FAILED - scorer suspect, stopping")

# ---------------------------------------------------------------- GATE 1 + attribution
passed = [f for f in ORDER
          if all(res["after"][f][L]["ERROR_of_decided"]["n"] > 0 and
                 res["after"][f][L]["ERROR_of_decided"]["pct"] < 10.0 for L in ("sk", "cz"))]
attr = {f: {c: {L: res[c][f][L]["ERROR_of_decided"]["pct"] for L in ("pooled", "sk", "cz")} for c in CFGS}
        for f in ORDER}
moved = {c: [f for f in ORDER if any(res[c][f][L]["ERROR_of_decided"] != res["before"][f][L]["ERROR_of_decided"]
                                     or res[c][f][L]["conservative"] != res["before"][f][L]["conservative"]
                                     for L in ("sk", "cz"))] for c in ("tok", "verbish", "agent")}
OUT = {"generated_by": "phase2c/gate1_2c.py", "model_calls": 0, "db_calls": 0, "new_gold": 0,
       "sample": "phase2b/sample_2b.json (200 rows: sk 1-100, cz 101-200)",
       "gold": "phase2b/run_2b_results.json outputs.gold_sk/gold_cz (2B blind gold, run 2)",
       "entry_point": "derive_2c.derive(row, lang=None, mode='after')",
       "fields": ORDER, "gate_rule": "AFTER ERROR-of-decided point estimate < 10 % on BOTH sk and cz",
       "passed": passed, "sanity": sanity, "attribution_error_of_decided_pct": attr, "fixes_that_moved": moved,
       "caveat": "the three fixes were designed from defect examples drawn from THIS same 200-row sample; "
                 "the AFTER figures are optimistic in-sample numbers, not a fresh-set measurement",
       "results": res}
json.dump(OUT, open(f"{HERE}/gate1_2c.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# ---------------------------------------------------------------- GATE1.md
def row_md(f, L):
    b, a = res["before"][f][L], res["after"][f][L]
    return "| %s | %s | %d/%d/%d | %s %% %s | %d/%d/%d | %s %% %s | %s |" % (
        f, L, b["agree"], b["conservative"], b["error"], b["ERROR_of_decided"]["pct"], b["ERROR_of_decided"]["cp95"],
        a["agree"], a["conservative"], a["error"], a["ERROR_of_decided"]["pct"], a["ERROR_of_decided"]["cp95"],
        "PASS" if (f in passed) else "-")

tbl = ["| field | lang | BEFORE A/C/E | BEFORE ERR-of-decided | AFTER A/C/E | AFTER ERR-of-decided | gate |",
       "|---|---|---|---|---|---|---|"]
for f in ORDER:
    for L in ("sk", "cz", "pooled"):
        tbl.append(row_md(f, L))
att = ["| field | before | +tok | +verbish | +agent | after (all three) |", "|---|---|---|---|---|---|"] + [
    "| %s | %s | %s | %s | %s | %s |" % (f, *["%s / %s" % (attr[f][c]["sk"], attr[f][c]["cz"]) for c in CFGS])
    for f in ORDER]
md = open(f"{HERE}/GATE1.md", "w", encoding="utf-8")
md.write(f"""# Phase 2C GATE 1 - three reader fixes, re-validated on 2B's frozen sample

0 Gemini calls, 0 headless sessions, 0 DB access, 0 new gold. Sample = `phase2b/sample_2b.json`
(200 rows, sk 1-100 / cz 101-200); gold = 2B's blind gold `phase2b/run_2b_results.json`
`outputs.gold_sk` / `outputs.gold_cz` (run 2 - the run `results_2b.json` scored).

## Entry point (for the production runner)

    import derive_2c
    out = derive_2c.derive(row, lang=None, mode="after")

`row` = {{"n": int, "lang": "sk"|"cz", "src": str, "en": str, "level": str}} (`lang=` fills/overrides
`row["lang"]`). `mode`: `"after"` (all three patches, the production setting), `"before"` (byte-identical
2B behaviour), or `"tok"`/`"verbish"`/`"agent"` (single-patch ablation), or a dict
`{{"tok":bool,"verbish":bool,"agent":bool}}`.

Output schema = **exactly** `phase2b/derive_2b.derive()`'s, so everything `run_2b.py` consumed keeps working:

* `reader`: `agent`, `why`, `clause`, `feats`, `agent_on_fallback_clause`
* `derived`: `agent_nom`, `finite_verb`, `person`, `number`, `gender`, `tf` (+`frames`), `tense_open`,
  `perfective_present`, `voice_sk` - each `{{"value": ..., "source": str}}`, `value is None` = abstain
* `voice_paths`: `g4_v2_sk_reflex`, `g4_v3_passive_or_reflex`, `g4_cz_se_missed`, `agv4_sk_clause_passive`,
  `agv4_sk_clause_reflex`, `agv4_main_passive`, `agv4_main_reflex`, `agv4_en_passive`,
  `agv4_en_passive_span`, `reader_nom_full_agent` - the AG v4 + reader_nom paths
* `rewrite`: `action` (`U`/`R`/`ABSTAIN`), `new`, `pronoun`, `where`, `reason`, `check` - the arm-B script
  rewrite. `derive_2c.main()` renames `new` -> `sk_new`/`cz_new` exactly as `derive_2b.main()` did.

Frozen code is never edited: `phase1*/`, `checker/` and `phase2b/` are imported and monkeypatched in
memory by `derive_2c.patches()`; the patched `_decide_clause` copy lives in `phase2c/derive_2c.py`.

## The three fixes

1. **P3 / DERIVE #3 `agent`** - `reader_nom._decide_clause` returned non-nominatives. Patched copy:
   a pronoun form that is also a determiner and stands before a noun (adjectives skipped) is a determiner,
   not the pronoun (cz `ty rybky`); NP heads are rejected when they are closed-class adverbs, particles,
   conjunctions or subordinators (incl. the generated `kdyby-`/`aby-` conditional paradigm and the
   "stem + `ze`" conjunction rule), deictic obliques in `-hle`, preposition-governed forms, or bare
   long-form adjectives without a head noun. Nothing survives -> abstain (frozen behaviour).
2. **P1 / DERIVE #1 `tok`** - `f9.WORD` is replaced by `[a-z + the full Czech+Slovak diacritic set]`
   (adds r-hacek and u-kroucek, plus o/u-umlaut), on BOTH f9 module objects (Slovak `f9_1n` and the
   `cz_reader.build()` copy), so `tok`, `_is_l_part`, `sk_frame`, the CZ_PERF aspect lexicon and
   `reader_nom._lpset` all see whole Czech words. Verified: `Rekne mu domu` -> `['řekne','mu','domů']`.
3. **P2 / DERIVE #2 `verbish`** - `reader_nom._verbish` wrapper: a token that is not a byt-copula, a modal
   or an l-participle loses its verb reading when it is preposition-governed in the sentence
   (`po pobreznej ceste`), capitalised but not sentence-initial, or ends in `-s` without a real 2sg
   present ending (`Kamos`).

Not touched, by instruction: **`tense_open`** (2B DEFECTS_score #3 - a definition mismatch, not a reader
bug: the script reports the f9 frame-set size, the gold reports "more than one English tense acceptable",
and the gold itself flips on 13/100 sk rows). It stays a model field. The `tf` "conditional" emission
(DEFECTS_score #2 - the gold schema only has past/present/future) was also left alone; see below.

## Before / after (ERROR-of-decided = ERROR / (AGREE + ERROR), exact 95 % Clopper-Pearson)

A/C/E = AGREE / CONSERVATIVE (script abstains) / ERROR.

{chr(10).join(tbl)}

## GATE 1

Rule: a field may be script-derived in production only if its AFTER ERROR-of-decided **point estimate is
under 10 % on BOTH sk and cz**.

**Passed: {', '.join(passed) if passed else 'NONE'}**

## Per-fix attribution (ERROR-of-decided %, sk / cz)

{chr(10).join(att)}

Fields moved by each single fix (counts or rates changed vs before):
{json.dumps(moved, ensure_ascii=False)}

## Caveat (important)

The three fixes were designed from the defect examples in `phase2b/DEFECTS_derive.md`, and those examples
were drawn from **this same 200-row sample**. The AFTER column is therefore an optimistic **in-sample**
number: it is a regression check that the fixes do what they claim, not a fresh-set measurement of the
patched reader. A production decision at the 10 % bar should be confirmed on rows this sample never saw.

## Defects recorded, not fixed

* `tf` emits `"conditional"`; the gold schema is past/present/future only (2B rows n30, n34) - every
  conditional reading is scored ERROR by construction. Not one of the three named fixes; left as is.
* `tense_open` definition mismatch (see above) - left to the model.
* `phase1t/taskB/cz_validate.py` has its **own** `WORD` regex inside the g1..g4 slice, independent of
  `f9.WORD`; the P1 fix does not reach it. It only feeds `voice_paths` (g4 raw readings), not a scored
  field, so it was left untouched. Recorded in `DEFECTS_gate1.md`.
""")
md.close()
D.main("after")
print("SANITY", json.dumps(sanity["brief_quoted_pooled"]))
print("PASSED", passed)
for f in ORDER:
    print("F", f, *["%s b=%s%s a=%s%s A/C/E b=%d/%d/%d a=%d/%d/%d" % (
        L, res["before"][f][L]["ERROR_of_decided"]["pct"], res["before"][f][L]["ERROR_of_decided"]["cp95"],
        res["after"][f][L]["ERROR_of_decided"]["pct"], res["after"][f][L]["ERROR_of_decided"]["cp95"],
        res["before"][f][L]["agree"], res["before"][f][L]["conservative"], res["before"][f][L]["error"],
        res["after"][f][L]["agree"], res["after"][f][L]["conservative"], res["after"][f][L]["error"])
        for L in ("sk", "cz")])
print("MOVED", json.dumps(moved))

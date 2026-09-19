# Phase 1M — carry-check 1: was the Phase 1L fresh reference-hygiene null genuine?

Label `carry`. Generated 2026-09-19T07:10:26Z by `phase1m/hygiene_null_check.py`. **0 model calls.**

## Verdict

**GENUINE.** The Phase 1L §4 "UNDETERMINED for the non-displayed variants" caveat is now closed: the fresh null is a real property of the data, not an artefact of a shared annotation object.

## 1. The two copies are provably independent

Two separate `loader_1l.load_fresh_annotations()` calls, each then `copy.deepcopy`-ed:

```json
{
 "loader_returned_same_top_object": false,
 "loader_returned_same_nested_object_140022": false,
 "deepcopies_share_top_object": false,
 "deepcopies_share_nested_object_140022": false,
 "recs_share_any_object": false,
 "n_items": 600
}
```

This reproduces `CACHING_CHECK.md` at runtime on the *1L* loader path: `load_fresh_annotations` has no memo, so the two calls already returned distinct top-level and nested objects (`False` on both identity tests); the deep copies make that structural rather than incidental. The 600 record dicts are distinct objects too (`recs_share_any_object = False`).

## 2. `v` before and after the patch — the unpatched copy really is unpatched

Patch files: `out_fresh_1.json`; sids 140022, 140024, 140032.

**Before `apply_hygiene`:**

| copy | sid | v (accepted variants beyond the displayed reference) |
|---|---|---|
| A (stays unpatched) | 140022 | ["You were waiting on the platform when it started raining.", "You waited on the platform when it started raining."] |
| A (stays unpatched) | 140024 | ["He was fixing that lawnmower all afternoon and in the end he gave up.", "He fixed that lawnmower all afternoon and in the end he gave up."] |
| A (stays unpatched) | 140032 | ["She asked me whether I could use that program.", "She asked me if I knew that program."] |
| copy | sid | v (accepted variants beyond the displayed reference) |
|---|---|---|
| B (about to be patched) | 140022 | ["You were waiting on the platform when it started raining.", "You waited on the platform when it started raining."] |
| B (about to be patched) | 140024 | ["He was fixing that lawnmower all afternoon and in the end he gave up.", "He fixed that lawnmower all afternoon and in the end he gave up."] |
| B (about to be patched) | 140032 | ["She asked me whether I could use that program.", "She asked me if I knew that program."] |

**After `apply_hygiene(recsB, annB, patches)`:**

| copy | sid | v (accepted variants beyond the displayed reference) |
|---|---|---|
| A (unpatched) | 140022 | ["You were waiting on the platform when it started raining.", "You waited on the platform when it started raining."] |
| A (unpatched) | 140024 | ["He was fixing that lawnmower all afternoon and in the end he gave up.", "He fixed that lawnmower all afternoon and in the end he gave up."] |
| A (unpatched) | 140032 | ["She asked me whether I could use that program.", "She asked me if I knew that program."] |
| copy | sid | v (accepted variants beyond the displayed reference) |
|---|---|---|
| B (patched) | 140022 | ["You were waiting on the platform when it started raining."] |
| B (patched) | 140024 | ["He was fixing that lawnmower all afternoon and in the end he gave up."] |
| B (patched) | 140032 | ["She asked me whether I could use that program.", "She asked me if I knew how to use that program."] |

`apply_hygiene` stats on copy B:

```json
{
 "sids_touched": [
  140022,
  140024,
  140032
 ],
 "removed": 2,
 "replaced": 1,
 "ref_changed": 0,
 "ref_kept": []
}
```

Copy A still carries every removed string and none of the replacements: `A_untouched = True`.

## 3. `compute_chk` over all 600 fresh items, under each copy

| copy | match | mistake | auto |
|---|---|---|---|
| A (no hygiene) | 39 | 0 | 561 |
| B (hygiene)    | 39 | 0 | 561 |

**Items whose `chk` differs between the two copies: 0 / 600.**

## 4. Could any answer have matched a touched variant?

Under the checker's own `checker_1i.base.norm`, comparing all 600 answers with the 3 removed / replaced strings:

* *removed*: `You waited on the platform when it started raining.`
* *removed*: `He fixed that lawnmower all afternoon and in the end he gave up.`
* *replaced-from*: `She asked me if I knew that program.`

**Exact normalised hits: 0.** (26 of the 600 answers belong to the three touched sids at all, so even the candidate pool is small.)

## 5. Combined with `CACHING_CHECK.md`

`CACHING_CHECK.md` established statically and at runtime that `loader_1k.load_fresh_annotations` builds a fresh object on every call (no module memo, unlike `_rewrites`). The artefact hypothesis in the 1L report required the opposite: that the "before" column had silently been computed against already-hygienised annotations, because `apply_hygiene` mutates `hy['v']` in place. Three independent facts now rule that out:

1. no caching — the loader cannot leak a mutation from one `build_side` call into the next;
2. with the mutation *deliberately* confined to one of two deep copies, the unpatched copy demonstrably still contains the removed variants (§2), i.e. the "before" state is real;
3. with both copies scored side by side in one process, **0** of 600 items change `chk` (§3), and **0** answers can even reach a touched variant under `norm` (§4).

The zero in the 1L "after minus before" columns is therefore the true effect size on this fresh set: the two removed variants and the one replaced variant were simply never the string any learner answer matched, and (per 1L) `display_reference_changed = 0`, so the prompt text was identical as well — which is why the run produced 460 identical request hashes. The null measures the *set*, not the machinery.

Scope note: this settles the fresh side only. The DEV side moved 182 -> 172 under the same machinery, so hygiene is not inert in general; and the replay1j references were never hygienised at all (1L §4).


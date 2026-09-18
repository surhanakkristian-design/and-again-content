# Task B output — how agent R (and F) must wire the rewrite into the pipeline

Task B made the dropped Slovak subject pronoun explicit in **91 of 140** sentences (both sides).
Nothing here was derived from a checker verdict, a model reply or a learner answer: the rewrite is a
fixed linguistic rule applied to the answer-free `sentences_all.jsonl`, and the judge input was built
by `build_judge_input.py`, which only counts.

## Files

| file | what |
|---|---|
| `rewrites.jsonl` | one line per sid (140): `sid, side, status, untouched_reason, person, number, pronoun, old_sk, new_sk, refs_old, refs_new, g_old, g_new, g_removed, note`. **`person` / `number` / `pronoun` are LISTS**, one entry per inserted pronoun (3 sentences got two pronouns); empty lists for untouched sentences. |
| `sk_new.json` | `{"<sid>": "<new Slovak>"}` for the 91 rewritten sentences only — the lookup you need at run time |
| `annotations_b_dev.json`, `annotations_b_holdout.json` | drop-in replacements for `phase1j/<side>/annotations.json`: same shape `{"<sid>": {"hygienised": …, "raw": …}}`, with `g` set to `null` on every rewritten sid (`v[]` needed no trimming — the dropped references were all `g`-generated hygiene variants) |
| `TASK_B_REWRITE.md` | the counts and 10 DEV before/after examples |
| `judge_input.jsonl` (+ `part1/2/3`), `judge_keymap.json`, `JUDGE_TASK.md` | the blind re-judging pass. **`judge_keymap.json` is forbidden to the judge.** |

## Which fields carry the Slovak sentence — change all three

1. **`item['sk']`** in `phase1j/<side>/items.jsonl`. This is what `pipeline_1i.build_prompt` puts on the
   `Slovak: <sk>` line (`to_item(r)` copies it through). Override it:
   `if str(r['sid']) in SK_NEW: r['sk'] = SK_NEW[str(r['sid'])]` — **before** `to_item()` /
   `run_pipeline()` / `prompt_key()`.
2. **`checker_1i.SK_OF[sid]`**, the sid → Slovak map seeded in `pipeline_1i.setup()` /
   `baseline_dev_1j.py`. F4 / F4v2 / **F4v3** (the frozen Task-C guard) read the Slovak morphology from
   there; if you do not update it, the subject guard keeps deciding on the old, subject-less sentence
   and the whole point of Task B is lost.
3. **`item['refs']`** — the stored `refs` still contain the gender alternates that no longer agree.
   Replace them with `refs_new` from `rewrites.jsonl` (40 references dropped over 31 sentences), and use
   `annotations_b_<side>.json` instead of `<side>/annotations.json` so that `refs_of()` and the hygiene
   step regenerate nothing from `g`. `item['reference']` (the primary) never changes — the inserted
   pronoun always matches it.

## The gender licence line of the L3 prompt

The prompt line

> `Gender: the Slovak does not fix the gender here — the reference's "he" may equally be the other gender …`

**must be REMOVED for every rewritten sentence** (the Slovak now fixes the gender) and **KEPT for the
untouched ones**. If you load `annotations_b_<side>.json`, this happens by itself:
`pipeline_1i.gender_chain(st, sid)` returns empty when the annotation's `g` is `null`, and
`build_prompt` then emits no gender line (`has_gender=False`). Assert it: no rewritten sid may produce
a prompt containing `"Gender:"`. The 31 rewritten sentences that had a `g` are exactly the ones that
lose the line; the 18-1j-DEV/holdout sentences that keep a `g` are all untouched.

## Consequences for the ledger

Every stored P-E4b verdict of a **rewritten** sid is invalid (the prompt text changed): those items must
be re-called and counted against the 1,400-call cap. Untouched sids keep their cached verdicts, since
their prompt text is byte-identical. 637 items belong to rewritten sentences (dev 357, holdout 280);
only the subset that reaches L3 needs a call.

## The re-judged gold labels

`judge_output.jsonl` (written by the blind judge) + `judge_keymap.json` give the new ground truth per
item: join on `k`. 697 items were re-judged — 637 from rewritten sentences plus 60 controls drawn with
seed 1 from untouched DEV sentences whose Slovak did not change; the control set measures judge noise
against the old labels and must be excluded from any coverage / FA number reported for the rewrite.

# Phase 1U — the L3 prompt change, as a diff

## Where the 1T prompt text lives
The 1T L3 prompt is not one string in one file: it is assembled at call time.

| what | file | lines |
|---|---|---|
| prompt id selected by the 1T runner (`PROMPT = R1P.PROMPT_1P`, `'P-FROZEN-1P'`) | `phase1t/run/runner_1t.py` | 57 |
| the assembler — **the insertion point** | `phase1p/runner_1p.py` | 66–81 (`build_req_1p`) |
| `VOICE_SAME_LINE` (1N's one change, first element of `ins`) | `phase1n/runner_1n.py` | 78–82 |
| head / extra / tail layout, `P-FROZEN` body | `phase1k/runner_1k.py` | 76–90 (`build_req`) |
| `GENDER_TMPL`, `GROUND_LINE`, `WORDING_LINE`; `pb_lines()`, `sys_text()` | `phase1i/pipeline_1i.py` | 40–51, 154–179 |
| lever 2 lines (`DEF_LINE`, `ASPECT_TMPL`, `NUMBER_TMPL`) | `phase1p/lever2.py` | 19–31 |
| lever 3 line (`ALT_TMPL`, `CAP = 2`) | `phase1p/lever3.py` | 16–17 |

Resulting user-prompt order under `P-FROZEN-1P`:
`PB head lines` → `gender line?` → `GROUND_LINE` → `WORDING_LINE` → `VOICE_SAME_LINE` →
`lever 2 / lever 3 lines` → tail `SAME, TIP or DIFF?`.
(`build_req_1p` finds the single occurrence of `WORDING_LINE` and splices `ins` in right after it,
so `ins` lands between `WORDING_LINE` and the tail.)

## The change
Exactly ONE line is added, at the END of `ins` — i.e. **after** the lever lines, so that it
qualifies lever 2's `DEF_LINE` ("...chooses a different article is SAME on that point") whenever
that line fires, and **before** the frozen tail. Nothing else changes: not the system text, not the
P-B body, not the tail, not `GEN_CFG`, not the output vocabulary (SAME / TIP / DIFF), not the levers.

```diff
--- a/phase1p/runner_1p.py	(P-FROZEN-1P, as run in Phase 1T)
+++ b/phase1u/stack/  (P-FROZEN-1U)
@@ -63,6 +63,14 @@
+ARTICLE_LINE_1U = (
+    'Articles: the previous point is about the CHOICE of article. An article that English grammar '
+    'REQUIRES and the learner sentence simply leaves out ("Dad will buy new fridge.", "It is cold '
+    'in kitchen today.") is not acceptable English and is DIFF. An English article is a '
+    'grammatical requirement of the target language, and Slovak has no article to omit in the '
+    'first place, so nothing was dropped in translation: the sentence is simply not grammatical '
+    'English. Where more than one determiner is grammatical (a / the / a possessive / no article '
+    'where English allows it), the choice stays free and is SAME on that point.')
+
 def build_req_1p(st, r, prompt_id):
     """P-FROZEN-1P = the P-FROZEN body + VOICE_SAME_LINE (1N's one change) + this record's lever
     2 / lever 3 lines, inserted at the same place the gender chain is inserted."""
     if prompt_id != PROMPT_1P:
         return R1N.build_req_1n(st, r, prompt_id)
     sysx, user, gcfg, _h = R1N._ORIG_BUILD_REQ(st, r, 'P-FROZEN')
     lines = user.split('\n')
     at = [k for k, ln in enumerate(lines) if ln == P.WORDING_LINE]
     if len(at) != 1:
         raise SystemExit('REFUSED: WORDING_LINE occurs %d times in the P-FROZEN body' % len(at))
-    ins = [R1N.VOICE_SAME_LINE] + list(r.get('_extra') or [])
+    ins = [R1N.VOICE_SAME_LINE] + list(r.get('_extra') or []) + [ARTICLE_LINE_1U]
     lines = lines[:at[0] + 1] + ins + lines[at[0] + 1:]
     user = '\n'.join(lines)
     return sysx, user, gcfg, R.req_hash(sysx, user, gcfg)
```

## How the 1U runner must load the new text
The SPEC agent changes nothing outside `phase1u/`. The 1U runner tooling agent wires it as follows;
`phase1p/runner_1p.py` stays untouched on disk.

1. Put `ARTICLE_LINE_1U` in a new 1U-owned module, e.g. `phase1u/run/article_line_1u.py`, as a
   single module-level string. Its text is the block between the `>>>` markers in
   `phase1u/stack/L3_PROMPT_1U.txt` — one physical line, no leading/trailing whitespace, the
   straight-quote form shown in the diff above.
2. In the 1U runner, after `import runner_1p as R1P`, define a new prompt id
   `PROMPT_1U = 'P-FROZEN-1U'`, register it in `R1K.PROMPTS` exactly as 1P registers `P-FROZEN-1P`,
   and monkey-patch `R1K.build_req` with a `build_req_1u` that is `build_req_1p` verbatim except for
   the one `ins` line above, falling through to `R1P.build_req_1p` for any other prompt id.
   Set the runner's `PROMPT = PROMPT_1U`.
3. The new prompt id makes every `req_hash` differ from every 1T/1P hash, so no 1T reply can be
   replayed for a 1U item by accident. This is intended — 1U is a fresh measurement.
4. Assert in the preflight, on at least one built request: the user prompt contains
   `ARTICLE_LINE_1U` exactly once; `ARTICLE_LINE_1U` stands after every lever line and immediately
   before the tail line; the tail line is still `SAME, TIP or DIFF?`; and the system text is
   byte-identical to the 1T system text. Refuse to run if any of the four fails.
5. Record the prompt id, the sha256 of the assembled template and the sha256 of `ARTICLE_LINE_1U`
   in the frozen config, and freeze `phase1u/run/article_line_1u.py` in `FREEZE_FILES`.

## Caveat, disclosed
`{{PB_HEAD_LINES}}` and `{{SYS}}` were NOT opened (they live in the checker / `lib_prev`, one more
hop outside the permitted reading set, and the tool budget did not allow it). They are reproduced as
named placeholders and are carried through unchanged; the change above is purely additive and does
not depend on their content. The tooling agent must nevertheless run assertion 4 against a really
built request before the run.

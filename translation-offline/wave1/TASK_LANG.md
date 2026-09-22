# Wave 1 language agent task (one agent per language: de, ua or es)

You own ONE language, given in your prompt as LANG. Absolute paths only. Work under
`/Users/kristiansurhanak/Projects/and-again-content/translation-offline/wave1/` (below: `W1`).
Everything is already built and tested by the main session (`W1/common/test_w1.py` 13/13 PASS, model mocked):
`W1/common/{prompts_w1,stack_w1,pipeline_w1}.py`, `W1/common/chain_w1.sh`, `W1/spec/*`. Part A (SELECT only) is DONE:
`W1/LANG/partA/partA.md` + `partA.json` + `rows.jsonl`.

## What you do
1. Launch the chain for your language, detached, with nohup (NEVER setsid):
   `cd /tmp && nohup bash W1/common/chain_w1.sh LANG > W1/LANG/chain.log 2>&1 &`
   (write the absolute path). It runs: preflight tests (0 cost) -> [ua/es only: Part B rewrite pass 1 / pass 2 / final
   via headless opus sessions] -> token projection (stops the language BEFORE Part D if over budget) -> fresh set ->
   mock -> 4 blind writers -> 4 judges -> items -> freeze + commits -> ONE open of the set by the frozen stack (Gemini)
   -> analysis. It commits its own files. Expect 30-90 minutes.
2. Wait for it with few tool calls: one Bash call per wait of at most ~9 minutes, e.g.
   `for i in $(seq 1 54); do grep -q "CHAIN_DONE\|CHAIN FAIL" W1/LANG/chain.log && break; sleep 10; done; tail -4 W1/LANG/chain.log`
   Do not read big files while waiting. `W1/LANG/TOKENS.md` has the cumulative headless tokens after every stage.
3. If the chain fails: read `W1/LANG/CHAIN_FAIL.txt`, the tail of `chain.log` and any `W1/LANG/STOP_*.md`.
   - `STOP_quota.md` / a usage-limit or quota error of a headless Claude session: STOP this language for good (do not
     relaunch) and write the report part with what exists.
   - `STOP_D_budget.md` or `STOP_tokencap.md`: STOP for good, report.
   - Anything else (a code bug, invalid output after the retry, a transient failure): do NOT edit anything under
     `W1/common/` or `W1/spec/` (they are shared and frozen for all three languages). Relaunch the chain ONCE if the
     failure looks transient (finished sessions and stored Gemini replies resume at 0 cost). If it fails again, stop and
     describe the failure precisely in your final message (file, line, error) so the main session can fix it.
   - Never delete `W1/LANG/partD/run/` (the set is opened once; the gemini step refuses to reopen).
4. When the chain prints CHAIN_DONE, write `W1/LANG/REPORT_LANG.md` (English, plain sentences, tables where useful):
   - FIRST: coverage and FA, pooled and per level, with the exact 95 % Clopper-Pearson intervals, and MET / missed for
     coverage >= 90 % and FA < 5 % on the point AND on the interval (from `partD/analysis/HEADLINE.json`); then the L3-only
     diagnostic line and what the content check caught / cost.
   - Part A data findings (from `partA/partA.json`: counts per finding and every flagged row except the `empty` list,
     which you summarise by level).
   - ua/es: Part B rewrite counts (changed, unchanged, flagged, machine-check failures, second-pass disagreements, by
     level, pronouns) with 10 examples each for changed, changed+flagged, pass-2 disagreements and machine-check
     failures (from `partB/partB.json`).
   - Every false acceptance and every false rejection with its cause (layer, content-check word, writer type, judge
     reason), grouped by cause, plus a short reading of the causes (from `partD/analysis/HEADLINE.json`).
   - Judge noise (80 hidden duplicates: agree / disagree, each disagreement).
   - Gemini calls (HTTP 200 counted, failed-but-counted) and spend (from HEADLINE.json `gemini` + `GEMINI_LEDGER.json`).
   - Claude tokens: every headless session from `TOKENS.md` (rewrite, writers, judges) and your own estimate.
   - Freeze hash, FREEZE_COMMIT, RUN_COMMIT, access log (opened ONCE?).
   - Defects you noticed, recorded, NOT fixed.
   Then commit it: `python3 -B W1/common/gitc.py "Wave 1 LANG: report part" W1/LANG`.
5. Rules: NO database writes of any kind (no UPDATE/INSERT/DDL; you do not need the database at all). No deploy, no
   push. Do not touch earlier phase directories, `W1/common/`, `W1/spec/` or other languages' directories. Never print
   the OAuth token or the Gemini key. Keep your own tool calls few (about 20).
6. Final message (it goes to the main session, not the user), at most 15 lines: status (CHAIN_DONE / stopped why),
   pooled coverage and FA with CP intervals, both targets met on the point yes/no, the report path, headless tokens,
   Gemini calls and spend, anything the main session must fix.

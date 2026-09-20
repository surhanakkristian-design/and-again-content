# DEFECTS — phase 2F Czech run (run_2f_cz.py)

Same convention as 2E: one timestamped line per defect, appended by the runner itself (`defect()`), plus
anything found by hand. A defect recorded and NOT fixed says so explicitly.

2026-09-20 23:25 DEFECT (environment, WORKED AROUND): a `nohup ... &` background launch from this agent's
Bash tool does NOT survive the end of the tool call - the sandbox reaps the whole descendant tree, and a
double-fork + os.setsid() daemon (PPID 1, own session) was reaped too. Two in-flight headless sessions were
killed mid-call this way (their tokens are spent but unrecorded in any ledger, because the ledger is only
written when the session returns). Part 1 is therefore launched with run_in_terminal, in the user's own
login shell outside the sandbox, which persists. Anything long in 2F must be launched the same way.
2026-09-20 23:26 DEFECT (recorded, NOT fixed): session() charges retry tokens to `retry_tokens_not_counted_
as_session` only when the CLI returns; a session killed from outside (sandbox reap, SIGKILL) leaves its
tokens uncounted in ledger_2f_cz.json, so the tripwire under-reads real spend by that amount.

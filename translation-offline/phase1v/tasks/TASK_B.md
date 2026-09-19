Track B (B1, B2, B3). Dir: TO/phase1v/trackB. 0 checking calls; the rewrite and annotation calls are
LLM calls of the unchanged 1N/1M annotation pipeline and arm-B rewrite (as used for 1J/1T sets; find the
code from phase1t/taskB and the modules it imports). Count them separately and report them; keep them
small (60 sentences). They do NOT count as checking calls but DO count toward the phase's 1,200 cap
and $1 spend — print the planned count before running.
DB read-only: the Supabase CLI query recipe (memory: CLI binary path used for live reads; project ref
abyrutykpvmzkfbesire) — SELECT only. 60 real Slovak sentences stratified by level (15/level).
B1 tokens/sentence rewrite vs annotation (use usageMetadata from the API responses), how many needed rewrite.
B2 gold validation of the deterministic guards (phase1t/taskB method) BEFORE and AFTER; error rate per
guard in both states; compare with 1T's 47 agent-reader errors on 120 raw sentences.
  Gold labels: produce them the same way phase1t/taskB did (state how).
B3 extrapolation to 5,895 (saturation vs linear, justify), token total, wall-clock at the active tier's
rate, Gemini checking calls 0; list assumptions.

Track A, items A1, A2, A3 (closed sets only; loop budget 200 model calls). Dir: TO/phase1v/trackA_loop.
- A1: classify the 9 type-M false accepts of 1U (writer tags fronted 3 / main 3 / misaligned 3), fix the
  deterministic ones as agent_drop_v5 (copy of v4 + changes, new file). Regression gate on the 1S packet:
  >=96/97 catches, 0/42 by-passive and 0/39 plain controls rejected; cost on 1T and 1U closed sets must
  not exceed v4's (1 item W:190081:w2). Select on measured cost.
- A2: determiner-free rule where the Slovak has no demonstrative (ten/ta/tie/tieto and their forms):
  (a) one L3 PROMPT line, (b) a TIP-path rule. Measure each separately (cost + gain), on closed sets.
  The prompt line needs model calls: re-run only the L3-affected closed items, within the 200 budget.
- A3: bounded loop, max 3 rounds, each round = one fix applied + re-score 1T and 1U closed + record
  coverage, FA, FA by type, per-guard cost. Apply ALL stop rules of the brief literally; log reverted
  rounds too. Output rounds.json + a markdown table.
- Deliver the FINAL frozen candidate stack as a manifest TO/phase1v/trackA_loop/STACK_1V.json listing
  every module/prompt file the fresh run must use (1U frozen stack + the accepted fixes), and a
  self-contained scoring entry point the run agent can call. Do not freeze/commit; the run agent does.
- The fresh set of A4 is being built in parallel by another agent in TO/phase1v/trackA_set: never read it.

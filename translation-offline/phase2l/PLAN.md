# Phase 2L plan (22.9.2026)
Stage order A -> B -> C (safety stop) -> D -> E -> report. Claude budget 2,000,000 tokens; Gemini hard cap 3,500 calls, $1.00.
- S0 main: brief copy, SHA_before (earlier phase dirs), plan. ~40k tokens.
- S1 agent (tx-opus, <=12 tool calls): Part A (0 calls), Part B build + test suite (mocked, poison test) then B2 run on
  2I + 2J Part D accepted items (est. <=1,500 Gemini calls), Part C config table + SAFETY STOP decision + freeze. Projection ~250k.
- S2 agent: Part D Czech checker + tests + 1T gold validation + upload_cz_final.xlsx (0 calls). Projection ~250k.
- S3 agent: Part E set build (writers = headless sessions), judge (4 headless sessions, <=400k each). Projection ~900k.
- S4 agent: Part E frozen Gemini run (~900 L3 + ~800 B calls) + analysis. Projection ~150k.
- S5 agent: report + SHA after. Projection ~100k.
Token accounting after each stage in phase2l/TOKENS.md (harness-reported subagent totals).

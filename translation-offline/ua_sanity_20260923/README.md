# ua checker sanity check (owner decision 41, 23 Sept 2026) - DIAGNOSTIC, NOT a measurement

- run_stack.ts runs the DEPLOYED wave-1 ua stack (and-again supabase/functions/check-translation/sourceOnly/wave1.ts,
  unchanged) offline with the real Gemini transport. No prompt and no frozen file was changed.
- repro_1067_*: exercise 1067 (2 live answers + 4 probes). fresh30_*: 30 selected ua exercises outside the wave-1
  Part D set (excluded_ids.txt), 8 A1 / 8 A2 / 7 B1 / 7 B2, md5 order with seed 'ua-sanity-20260923'; one faithful
  answer each by an Opus subagent that saw only the Ukrainian sentence, level and topic.
- calls.jsonl = every model call verbatim (user text + reply). 68 calls, $0.0065.

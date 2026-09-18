Work dir: ~/Projects/and-again-content/translation-offline/phase1b (FORMAT_SPEC.md there is authoritative).
TOKEN BUDGET RULES (hard): every tool call re-reads your whole context, so minimise tool calls. Read what you need once,
in parallel calls where possible. Write each output file with ONE Write call (whole file). Never re-read a file you wrote.
Never print large files to stdout. Final message: at most 4 lines (what file(s) you wrote, counts, problems). No database
writes, no paid model APIs, no network, do not touch files outside the paths named in your task.

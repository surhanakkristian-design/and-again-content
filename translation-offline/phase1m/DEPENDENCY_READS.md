phase1k/loader_1k.py | full read, allowed by task step 3 (fresh-annotation loader + caching check) | recon-code
phase1k/taskB/runner_1k.py | grep -n + small sed range for configure_row signature/docstring only, allowed by task step 3 | recon-code
phase1j/taskC/runner_1j.py | grep -n + small sed range for load_side signature/docstring only, allowed by task step 3 | recon-code
phase1k/ (ls, incl. fresh/ judge/ taskA/ taskB/ taskD/) | named in my task: plain ls of phase1k and its task/prompt sub-directories | recon-data
phase1k/CONTEXT_1K.md | named in my task: §0 acceptance rule verbatim + schemas + arm-B convention + intents | recon-data
phase1k/HANDOFF_P.md | named in my task: annotator (agent P) task/prompt file | recon-data
phase1k/fresh/make_fresh.py (header + first rows) | the annotator's only written instruction set (arm-B convention, row schema) | recon-data
phase1k/judge/build_judge_input.py | the answer-writer's enforced quotas + judge-input/label file formats | recon-data
phase1k/HANDOFF_R.md, taskA/TASK_A_RELABEL.md, taskB/HANDOFF_G.md, taskD/TASK_D_DEV.md | locating the declared type set T/W/M/S/V/E and the judge-label conventions; none of it used in the blind-side files | recon-data
docs/features/reports/TRANSLATION_OFFLINE_PHASE1K_REPORT.md §2 (lines 119-240) + headings | my task allows §0 of this report; the report has no §0, and §2.1-2.4 are where the sentence-writer, blind-writer and blind-judge instructions are recorded | recon-data
phase1j/CONTEXT_1J.md §6 (lines 206-227) | the only place the T/W/M/S definitions exist verbatim; phase1k delegates to it explicitly ('keep their Phase 1c-1j definitions, $J/CONTEXT_1J.md §6'). Read-only, nothing written | recon-data
docs/features/reports/TRANSLATION_OFFLINE_PHASE1L_REPORT.md (grep for type E) | checked whether type E is defined anywhere; it is not | recon-data
| phase1k fresh sentences/items/annotations (via loader_1l -> loader_1k) | carry-check 1 names them: "load the 1k fresh annotations twice as independent deep copies" and compute_chk over the 600 fresh items; logged in access_log.jsonl | carry |
| phase1j dev items+annotations (via runner_1l.build_side('dev') -> runner_1j.load_side) | carry-check 2 names them: the 490 DEV records carrying the STORED production chk; logged in access_log.jsonl | carry |
| phase1m/runner_1m.py (import only, for l1_nearmiss) | carry-check 2 says "import it from runner_1m if present"; module import reads no data, nothing under data/ or judge/ opened | carry |

- phase1j/ + phase1k/ python modules (loader_1k, runner_1k) | imported by loader_1l/runner_1l; the phase1m code cannot run without them (code only, no data read) | smoke
- phase1j/ + phase1k/ python modules + their items/annotations/judge labels (via loader_1l/runner_1l/R1K.judge_labels), phase1l/hygiene | f8-union step 4 cannot evaluate f8u on dev/replay1j/fresh1l without them; read-only, 0 model calls, all logged in access_log.jsonl | f8-union

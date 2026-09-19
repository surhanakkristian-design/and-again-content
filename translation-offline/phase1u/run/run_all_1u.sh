#!/bin/bash
# Phase 1U - the three stages the RUN agent calls ONE BY ONE.  Nothing outside phase1u/ is written
# (stage3 only chmods earlier phase dirs read-only and commits phase1u).
#   ./run_all_1u.sh stage1     # 0 model calls: join, floors, AG gate, self-tests, preflight
#   ./run_all_1u.sh stage2     # design-only: the 1T probe under the new prompt (<= 80 calls)
#   ./run_all_1u.sh stage3     # freeze, RUN commit, --final, score
set -u
RUN="$(cd "$(dirname "$0")" && pwd)"
P1U="$(dirname "$RUN")"
TOFF="$(dirname "$P1U")"
REPO="$(cd "$TOFF/.." && pwd)"
export PYTHONDONTWRITEBYTECODE=1
cd "$RUN" || exit 1

sync_data() {                       # the assembler writes phase1u/data and phase1u/set/data
  for f in sentences.json annotations.json items.json labels.json; do
    if [ -f "$P1U/set/data/$f" ] && [ ! -f "$P1U/data/$f" ]; then
      mkdir -p "$P1U/data" && cp "$P1U/set/data/$f" "$P1U/data/$f"
    elif [ -f "$P1U/data/$f" ] && [ ! -f "$P1U/set/data/$f" ]; then
      mkdir -p "$P1U/set/data" && cp "$P1U/data/$f" "$P1U/set/data/$f"
    fi
  done
}

case "${1:-}" in
stage1)
  set -e
  python3 "$P1U/set/join_labels_1u.py"
  sync_data
  python3 "$P1U/set/floors_1u.py" --data-dir "$P1U/data" --out-dir "$P1U/set"
  python3 "$P1U/taskA/gate_v4.py"
  python3 "$RUN/selftest_1u_run.py"
  python3 "$RUN/score_1u.py" --selftest
  python3 "$RUN/runner_1u.py" --preflight --data-dir "$P1U/data"
  echo "STAGE1 OK - 0 model calls.  Read PREFLIGHT_1U.json (PLANNED_CALLS) before stage2."
  ;;
stage2)
  set -e
  python3 "$RUN/runner_1u.py" --probe1t 80
  echo "STAGE2 OK - PROBE_1T_1U.md written (design only; it does not change the ruling line)."
  ;;
stage3)
  set -e
  for d in "$TOFF"/phase1[a-t]*; do
    [ -d "$d" ] && chmod -R a-w "$d" && echo "read-only: $(basename "$d")"
  done
  python3 "$RUN/runner_1u.py" --preflight --data-dir "$P1U/data"     # regenerates MODULES_1U.txt
  { echo "# Phase 1U FREEZE_FILES - every .py the run imports, relative to the repository root."
    cat "$RUN/MODULES_1U.txt"
    echo "translation-offline/phase1u/run/score_1u.py"
    echo "translation-offline/phase1u/run/selftest_1u_run.py"; } | sort -u > "$RUN/FREEZE_FILES"
  cd "$REPO"
  git add "$P1U" && git commit -m "Phase 1U: RUN commit (frozen stack + AG v4 + ARTICLE_LINE_1U)"
  git rev-parse HEAD | tee "$RUN/RUN_COMMIT" > "$RUN/FREEZE_HASH"
  cp "$RUN/FREEZE_HASH" "$RUN/FREEZE_1U.txt"
  git rev-parse HEAD >> "$RUN/FREEZE_1U.txt"
  ( cd "$REPO" && while read -r f; do case "$f" in \#*) continue;; esac
      printf '%s %s\n' "$(git hash-object "$f")" "$f"; done < "$RUN/FREEZE_FILES" ) \
    >> "$RUN/FREEZE_1U.txt"
  cd "$RUN"
  python3 "$RUN/runner_1u.py" --final --data-dir "$P1U/data"
  python3 "$RUN/score_1u.py"
  echo "STAGE3 OK - FINAL_RUN_DONE, results_1u.json, SCORE_1U.md, score_1u.json written."
  ;;
*) echo "usage: $0 stage1|stage2|stage3"; exit 2;;
esac

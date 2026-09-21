#!/bin/zsh
# Phase 2K: SHA-256 of every file under translation-offline/phase*/ except phase2k (sorted, relative paths).
# Same find/sort/shasum pipeline as phase2i/sha_tree.sh; the prune is phase2k instead of phase2i (so phase2i and phase2j are covered).
cd "$(dirname "$0")/.." || exit 1
find . -path './phase2k' -prune -o -path './phase*' -type f -print0 | LC_ALL=C sort -z | xargs -0 shasum -a 256 | sed 's#  \./#  #'

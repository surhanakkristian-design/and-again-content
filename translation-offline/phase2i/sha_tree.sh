#!/bin/zsh
# Phase 2I: SHA-256 of every file under translation-offline/phase*/ except phase2i (sorted, relative paths).
# Usage: zsh phase2i/sha_tree.sh > phase2i/SHA_after.txt   (run from anywhere)
cd "$(dirname "$0")/.." || exit 1
find . -path './phase2i' -prune -o -path './phase*' -type f -print0 | LC_ALL=C sort -z | xargs -0 shasum -a 256 | sed 's#  \./#  #'

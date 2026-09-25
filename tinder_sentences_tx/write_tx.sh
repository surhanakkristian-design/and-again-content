#!/bin/bash
# Upsert one slice's agreed rows of one language into public.tinder_sentences (idempotent).
# usage: bash write_tx.sh sk t01     (or: bash write_tx.sh sk r1)
set -euo pipefail
cd "$(dirname "$0")"
source "$HOME/Projects/and-again/supabase/scripts/_sb.sh" >/dev/null
F="$PWD/slices/$1/$2_upsert.sql"
cd "$HOME/Projects/and-again"
for try in 1 2 3; do
  "$SB" db query --linked --file "$F" >/dev/null 2>&1 && break
  [ "$try" = 3 ] && "$SB" db query --linked --file "$F"
  sleep 5
done
sb_rows "select count(*) n from public.tinder_sentences where language_code='$1'"; echo

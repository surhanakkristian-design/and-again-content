#!/bin/bash
# Write one slice's agreed English rows into public.tinder_sentences (upsert, idempotent).
# usage: bash write_slice.sh s01
set -euo pipefail
cd "$(dirname "$0")"
source "$HOME/Projects/and-again/supabase/scripts/_sb.sh"
python3 pipeline.py sql "$1"
cd "$HOME/Projects/and-again"
for try in 1 2 3; do
  "$SB" db query --linked --file "$OLDPWD/slices/$1_upsert.sql" >/dev/null 2>&1 && break
  [ "$try" = 3 ] && "$SB" db query --linked --file "$OLDPWD/slices/$1_upsert.sql"
  sleep 5
done
sb_rows "select count(*) n from public.tinder_sentences where language_code='en'"; echo

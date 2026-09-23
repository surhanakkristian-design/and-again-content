#!/bin/bash
# q.sh "<sql>" -> JSON rows on stdout
cd ~/Projects/and-again && source supabase/scripts/_sb.sh && sb_rows "$1"

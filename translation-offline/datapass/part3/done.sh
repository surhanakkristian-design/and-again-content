#!/bin/bash
# done.sh translate|review <slice> <tokens>  -> ledger line, then review_input (translate) or apply --write (review)
cd "$(dirname "$0")/.." || exit 1
printf "p3\t%s_%s\t%s\n" "$1" "$2" "$3" >> token_ledger.tsv
if [ "$1" = translate ]; then python3 part3/run_slice.py review_input "$2"; else python3 part3/run_slice.py apply "$2" --write; fi
awk -F'\t' 'NR>1{s+=$3}END{print "cumulative tokens",s}' token_ledger.tsv
awk -F'\t' 'r{s+=$3} $2 ~ /^RESUME_START/{r=1} END{print "resume-run cumulative tokens",s}' token_ledger.tsv

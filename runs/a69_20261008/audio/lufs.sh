#!/bin/bash
# prints file \t integrated LUFS \t true peak dBTP \t LRA
for f in "$@"; do
  out=$(ffmpeg -nostats -hide_banner -i "$f" -af ebur128=peak=true -f null - 2>&1 | sed -n '/Summary/,$p')
  I=$(echo "$out" | awk '/I:/{print $2; exit}')
  TP=$(echo "$out" | awk '/Peak:/{print $2; exit}')
  LRA=$(echo "$out" | awk '/LRA:/{print $2; exit}')
  printf "%s\t%s\t%s\t%s\n" "$(basename "$f")" "$I" "$TP" "$LRA"
done

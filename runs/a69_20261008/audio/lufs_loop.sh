#!/bin/bash
# loudness WHILE a short sound sounds: the file looped back to back (an integrated value needs >= 400 ms blocks)
for f in "$@"; do
  out=$(ffmpeg -nostats -hide_banner -stream_loop 19 -i "$f" -af ebur128=peak=true -f null - 2>&1 | sed -n '/Summary/,$p')
  printf "%s\t%s\t%s\n" "$(basename "$f")" "$(echo "$out" | awk '/I:/{print $2; exit}')" "$(echo "$out" | awk '/Peak:/{print $2; exit}')"
done

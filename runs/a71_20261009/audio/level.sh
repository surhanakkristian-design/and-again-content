#!/bin/bash
# A71: encodes lab-correct.wav / lab-wrong.wav to mp3 (44.1 kHz mono 160 kbit/s, as the old files) at -22 LUFS measured
# WHILE they sound (looped, as A69's lufs_loop.sh): gain from a first measurement, then measured again (two passes).
set -euo pipefail
cd "$(dirname "$0")"
meas() { ffmpeg -nostats -hide_banner -stream_loop 19 -i "$1" -af ebur128=peak=true -f null - 2>&1 | sed -n '/Summary/,$p' | awk '/I:/{print $2; exit}'; }
for n in lab-correct lab-wrong; do
  gain=0
  for pass in 1 2 3; do
    ffmpeg -v error -y -i "$n.wav" -af "volume=${gain}dB" -ar 44100 -ac 1 -c:a libmp3lame -b:a 160k "$n.mp3"
    i=$(meas "$n.mp3")
    gain=$(python3 -c "print(round($gain + (-22.0 - ($i)), 2))")
  done
  printf "%s\t%s LUFS\t%s s\n" "$n.mp3" "$(meas "$n.mp3")" "$(ffprobe -v 0 -show_entries format=duration -of csv=p=0 "$n.mp3")"
done

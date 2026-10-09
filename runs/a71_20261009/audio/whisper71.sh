#!/bin/bash
# A71: every new recording transcribed with whisper large-v3 (two-model rule: small was a sample) -> audio/whisper71.tsv
cd "$(dirname "$0")"; : > whisper71.tsv
while IFS=$'\t' read -r vid fn lufs dur text; do
  ffmpeg -v error -y -i "tts/$vid/$fn" -af apad=pad_dur=1 -ar 16000 -ac 1 /tmp/claude-501/w71.wav
  heard=$(whisper-cli -m ~/.claude-video-vision/models/ggml-large-v3.bin -f /tmp/claude-501/w71.wav -nt 2>/dev/null | tr '\n' ' ' | sed 's/^ *//;s/ *$//')
  printf "%s\t%s\t%s\t%s\n" "$vid" "$fn" "$text" "$heard" >> whisper71.tsv
done < levels71.tsv
echo done

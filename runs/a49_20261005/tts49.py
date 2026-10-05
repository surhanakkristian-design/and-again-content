# A49: records the new texts of 7071 ("king"): the noun "a king" and the six carousel captions, with the A45 voice
# Daniel (7071's default voice). Same encoding as A45 / A48: AAC 64 kbit/s mono 44.1 kHz, silence trimmed, -19 LUFS.
#   python3 tts49.py -> audio/7071/<file> + audio/manifest.json (object = sets/7071/<file>, new names)
import json, os, subprocess, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
VOICES = json.load(open(f'{HERE}/voices.json'))
K = json.load(open(f'{HERE}/content/king_7071.verified.json'))
def render(text, gender, out):
    aiff = out + '.aiff'
    subprocess.run(['say', '-v', VOICES[gender], '-o', aiff, text], check=True, timeout=120)
    af = ('silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.03,areverse,'
          'silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.08,areverse,'
          'loudnorm=I=-19:TP=-2:LRA=11,aresample=44100')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', aiff, '-af', af, '-ac', '1', '-c:a', 'aac', '-b:a', '64k', '-movflags', '+faststart', out], check=True, timeout=60)
    os.remove(aiff)
    dur = float(subprocess.run(['ffprobe', '-v', '0', '-show_entries', 'format=duration', '-of', 'csv=p=0', out], capture_output=True, text=True, timeout=30).stdout.strip())
    if not (0.2 <= dur <= 12): raise SystemExit(f'{out}: duration {dur}')
    return dur
items = [('noun', 2, 'a king')] + [('caption', i + 1, c) for i, c in enumerate(K['captions_en'].values())]
d = f'{HERE}/audio/7071'; os.makedirs(d, exist_ok=True); man = []
for kind, i, text in items:
    h = hashlib.sha1(f'{text}|{VOICES["male"]}|a49'.encode()).hexdigest()[:8]
    f = f'a49_{kind}{i}_{VOICES["male"].lower()}_{h}.m4a'
    dur = render(text, 'male', f'{d}/{f}')
    man.append({'mediaId': 7071, 'kind': kind, 'text': text, 'voice': 'male', 'file': f, 'object': f'sets/7071/{f}', 'duration': round(dur, 2)})
json.dump(man, open(f'{HERE}/audio/manifest.json', 'w'), ensure_ascii=False, indent=1)
print(len(man), 'recordings')

# A51: records the new carousel captions with the set's voice (as A45 / A48: AAC 64 kbit/s mono 44.1 kHz,
# silence trimmed, -19 LUFS).   python3 tts51.py -> audio/<id>/<file> + audio/manifest.json (object = sets/<id>/<file>)
import json, os, subprocess, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
VOICES = json.load(open(f'{HERE}/voices.json'))
ITEMS = [(8039, 'narrow way', 'female'), (8039, 'to look for a way through', 'female'),
         (62, 'beach bag', 'male'), (62, 'sports bag', 'male'), (4265, 'to calm a crying baby', 'male')]
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
man = []
for vid, text, gender in ITEMS:
    d = f'{HERE}/audio/{vid}'; os.makedirs(d, exist_ok=True)
    h = hashlib.sha1(f'{text}|{VOICES[gender]}|a51'.encode()).hexdigest()[:8]
    slug = ''.join(c if c.isalnum() else '_' for c in text).strip('_')
    f = f'a51_caption_{slug}_{VOICES[gender].lower()}_{h}.m4a'
    dur = render(text, gender, f'{d}/{f}')
    man.append({'mediaId': vid, 'kind': 'caption', 'text': text, 'voice': gender, 'file': f, 'object': f'sets/{vid}/{f}', 'duration': round(dur, 2)})
json.dump(man, open(f'{HERE}/audio/manifest.json', 'w'), ensure_ascii=False, indent=1)
print(len(man), 'recordings', [(m['text'], m['duration']) for m in man])

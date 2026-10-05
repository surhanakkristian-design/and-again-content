# A48: records every carousel caption of the 10 lab videos and every changed model answer, with the A45 voices
# (voices.json: Samantha female, Daniel male; the video's default voice from content/<id>.json).
#   python3 tts48.py   -> audio/<id>/<kind><i>_<voice>_<hash>.m4a + audio/manifest.json (object = sets/<id>/<file>, new names)
# Same encoding as A45's tts.py: AAC 64 kbit/s mono 44.1 kHz, silence trimmed, loudness -19 LUFS.
import json, os, subprocess, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
VOICES = json.load(open(f'{HERE}/voices.json'))
IDS = [8055, 236, 624, 7071, 8056, 4265, 461, 62, 8039, 432]
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
for vid in IDS:
    c = json.load(open(f'{HERE}/content/{vid}.json'))
    gender = c.get('voices', {}).get('default', 'male')
    items = []
    car = c['carousel']
    for i, cap in enumerate([x['caption'] for x in car['vertical'] + car['horizontal']]):
        items.append(('caption', i + 1, cap))
    if c.get('answerChanged'):
        items.append(('answer', '', ' '.join(c['answer'])))
    d = f'{HERE}/audio/{vid}'; os.makedirs(d, exist_ok=True)
    for kind, i, text in items:
        h = hashlib.sha1(f'{text}|{VOICES[gender]}|a48'.encode()).hexdigest()[:8]
        f = f'a48_{kind}{i}_{VOICES[gender].lower()}_{h}.m4a'
        out = f'{d}/{f}'
        dur = render(text, gender, out)
        man.append({'mediaId': vid, 'kind': kind, 'text': text, 'voice': gender, 'file': f, 'object': f'sets/{vid}/{f}', 'duration': round(dur, 2)})
json.dump(man, open(f'{HERE}/audio/manifest.json', 'w'), ensure_ascii=False, indent=1)
print(len(man), 'recordings')

# A45: records every phrase, noun and model answer of content/<id>.json with the macOS voices.
#   python3 tts.py <id> [<id> ...]      -> audio/<id>/<item>_<voice>_<hash>.m4a + audio/<id>/manifest.json
# AAC (m4a) 64 kbit/s mono 44.1 kHz, silence trimmed at both ends, loudness -19 LUFS. Free local tools only (say, ffmpeg).
import json, os, sys, subprocess, hashlib, re
HERE = os.path.dirname(os.path.abspath(__file__))
VOICES = json.load(open(f'{HERE}/voices.json'))   # { "female": "Samantha", "male": "Daniel" }
def spoken(text):
    return text
def render(text, gender, out):
    voice = VOICES[gender]
    aiff = out + '.aiff'
    subprocess.run(['say', '-v', voice, '-o', aiff, spoken(text)], check=True, timeout=120)
    af = ('silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.03,areverse,'
          'silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.08,areverse,'
          'loudnorm=I=-19:TP=-2:LRA=11,aresample=44100')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', aiff, '-af', af, '-ac', '1', '-c:a', 'aac', '-b:a', '64k', '-movflags', '+faststart', out], check=True, timeout=60)
    os.remove(aiff)
    p = subprocess.run(['ffprobe', '-v', '0', '-show_entries', 'format=duration', '-of', 'csv=p=0', out], capture_output=True, text=True, timeout=30)
    dur = float(p.stdout.strip())
    if not (0.2 <= dur <= 12): raise SystemExit(f'{out}: duration {dur}')
    return dur
def name(kind, i, text, gender):
    h = hashlib.sha1(f'{text}|{VOICES[gender]}'.encode()).hexdigest()[:8]
    return f'{kind}{i}_{VOICES[gender].lower()}_{h}.m4a'
def one(vid):
    c = json.load(open(f'{HERE}/content/{vid}.json'))
    d = f'{HERE}/audio/{vid}'; os.makedirs(d, exist_ok=True)
    items = [('tap', i + 1, t['phrase'], t['voice']) for i, t in enumerate(c['taps'])]
    items += [('noun', i + 1, n['word'], n['voice']) for i, n in enumerate(c['nouns'])]
    items += [('answer', '', ' '.join(c['answer']), c['answerVoice'])]
    man = {'mediaId': c['mediaId'], 'voices': VOICES, 'items': []}
    for kind, i, text, gender in items:
        f = name(kind, i, text, gender); out = f'{d}/{f}'
        dur = render(text, gender, out) if not os.path.exists(out) else float(subprocess.run(['ffprobe', '-v', '0', '-show_entries', 'format=duration', '-of', 'csv=p=0', out], capture_output=True, text=True).stdout.strip())
        man['items'].append({'kind': kind, 'i': i, 'text': text, 'voice': gender, 'file': f, 'object': f'sets/{vid}/{f}', 'duration': round(dur, 2), 'bytes': os.path.getsize(out)})
    keep = {x['file'] for x in man['items']} | {'manifest.json'}
    for f in os.listdir(d):
        if f not in keep: os.remove(f'{d}/{f}')   # files of an earlier text version of this video (never uploaded names are simply dropped)
    json.dump(man, open(f'{d}/manifest.json', 'w'), ensure_ascii=False, indent=1)
    return f'{vid} {len(man["items"])}'
from concurrent.futures import ThreadPoolExecutor
def safe(vid):
    for attempt in range(3):
        try: return one(vid)
        except BaseException as x: err = x
    return f'{vid} FAILED {err}'
with ThreadPoolExecutor(4) as ex: res = list(ex.map(safe, sys.argv[1:]))
bad = [r for r in res if 'FAILED' in r]
print(len(res) - len(bad), 'videos recorded;', len(bad), 'failed', bad[:10])

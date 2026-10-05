# A55: records every phrase, noun, model answer and carousel caption of content/<lang>/<id>.json with the macOS voices of
# voices.json (by voice identifier, so the Premium / Enhanced voice is used and never the compact one of the same name).
#   python3 tts55.py <lang> <id> [<id> ...]  -> audio/<lang>/<id>/a55_<lang>_<item>_<voice>_<hash>.m4a + manifest.json
# AAC (m4a) 64 kbit/s mono 44.1 kHz, silence trimmed at both ends, loudness -19 LUFS (as A45). Free local tools only (say, ffmpeg).
import json, os, sys, subprocess, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
ALL = json.load(open(f'{HERE}/voices.json'))
def dur_of(f):
    return float(subprocess.run(['ffprobe', '-v', '0', '-show_entries', 'format=duration', '-of', 'csv=p=0', f], capture_output=True, text=True, timeout=30).stdout.strip())
def render(voice, text, out):
    aiff = out + '.aiff'
    subprocess.run(['say', '-v', voice['id'], '-o', aiff, text], check=True, timeout=120)
    af = ('silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.03,areverse,'
          'silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.08,areverse,'
          'loudnorm=I=-19:TP=-2:LRA=11,aresample=44100')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', aiff, '-af', af, '-ac', '1', '-c:a', 'aac', '-b:a', '64k', '-movflags', '+faststart', out], check=True, timeout=60)
    os.remove(aiff)
    d = dur_of(out)
    if not (0.2 <= d <= 12): raise SystemExit(f'{out}: duration {d}')
    return d
def one(lang, vid):
    V = ALL[lang]
    c = json.load(open(f'{HERE}/content/{lang}/{vid}.json')); src = json.load(open(f'{HERE}/src/{vid}.json'))
    d = f'{HERE}/audio/{lang}/{vid}'; os.makedirs(d, exist_ok=True)
    items = [('tap', i + 1, t['phrase'], t['voice']) for i, t in enumerate(c['taps'])]
    items += [('noun', i + 1, n['word'], n['voice']) for i, n in enumerate(c['nouns'])]
    items += [('answer', '', ' '.join(c['answer']), c['answerVoice'])]
    items += [('caption', i + 1, x['caption'], src['defaultVoice']) for i, x in enumerate(c['carousel'])]
    man = {'mediaId': vid, 'lang': lang, 'voices': {g: v['name'] for g, v in V.items()}, 'items': []}
    for kind, i, text, gender in items:
        v = V[gender]; h = hashlib.sha1(f'{text}|{v["id"]}'.encode()).hexdigest()[:8]
        f = f'a55_{lang}_{kind}{i}_{v["id"].split(".")[-1].lower()}_{h}.m4a'; out = f'{d}/{f}'
        dur = render(v, text, out) if not os.path.exists(out) else dur_of(out)
        man['items'].append({'kind': kind, 'i': i, 'text': text, 'voice': gender, 'file': f, 'object': f'sets/{vid}/{f}', 'duration': round(dur, 2), 'bytes': os.path.getsize(out)})
    keep = {x['file'] for x in man['items']} | {'manifest.json'}
    for f in os.listdir(d):
        if f not in keep: os.remove(f'{d}/{f}')
    json.dump(man, open(f'{d}/manifest.json', 'w'), ensure_ascii=False, indent=1)
    return f'{lang} {vid} {len(man["items"])}'
from concurrent.futures import ThreadPoolExecutor
def safe(job):
    err = None
    for attempt in range(3):
        try: return one(*job)
        except BaseException as x: err = x
    return f'{job} FAILED {err}'
lang = sys.argv[1]
with ThreadPoolExecutor(4) as ex: res = list(ex.map(safe, [(lang, int(v)) for v in sys.argv[2:]]))
bad = [r for r in res if 'FAILED' in r]
print(len(res) - len(bad), 'videos recorded;', len(bad), 'failed', bad[:10]); sys.exit(1 if bad else 0)

# A60 (from tts59): records ONLY changed / new texts: the 6 noun videos' new story sentences (each video keeps its A58 voice)
# and every text of the two lab-only pilots (phrases, nouns, carousel captions, story). Voices by identifier; a render equal to
# the default voice's render stops the run.  python3 tts60.py -> audio/<id>/a60_<item>_<voice>_<hash>.m4a + manifest.json
import json, os, sys, subprocess, hashlib, filecmp
HERE = os.path.dirname(os.path.abspath(__file__))
VOICE = {236: 'premium.en-US.Ava', 8039: 'premium.en-US.Ava', 62: 'enhanced.en-US.Evan', 7071: 'enhanced.en-US.Nathan',
         8055: 'enhanced.en-US.Evan', 8056: 'enhanced.en-US.Nathan', 900001: 'premium.en-US.Zoe', 900002: 'enhanced.en-US.Nathan'}
PILOT = {900001: 'select', 900002: 'classical'}
def dur_of(f):
    return float(subprocess.run(['ffprobe', '-v', '0', '-show_entries', 'format=duration', '-of', 'csv=p=0', f], capture_output=True, text=True, timeout=30).stdout.strip())
def render(vid, text, out):
    aiff = out + '.aiff'; ref = out + '.ref.aiff'
    subprocess.run(['say', '-v', 'com.apple.voice.' + VOICE[vid], '-o', aiff, text], check=True, timeout=120)
    subprocess.run(['say', '-o', ref, text], check=True, timeout=120)
    if filecmp.cmp(aiff, ref, shallow=False): raise SystemExit(f'{vid}: the voice {VOICE[vid]} fell back to the default')
    os.remove(ref)
    af = ('silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.03,areverse,'
          'silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.08,areverse,'
          'loudnorm=I=-19:TP=-2:LRA=11,aresample=44100')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', aiff, '-af', af, '-ac', '1', '-c:a', 'aac', '-b:a', '64k', '-movflags', '+faststart', out], check=True, timeout=60)
    os.remove(aiff)
    d = dur_of(out)
    if not (0.2 <= d <= 12): raise SystemExit(f'{out}: duration {d}')
    return d
def one(vid):
    st = json.load(open(f'{HERE}/content/stories.json'))
    if vid in PILOT:
        c = json.load(open(f'{HERE}/content/{PILOT[vid]}.json'))
        items = [('phrase', i + 1, t['phrase']) for i, t in enumerate(c['taps'])]
        items += [('noun', i + 1, n['word']) for i, n in enumerate(c['nouns'])]
        items += [('caption', i + 1, x['caption']) for i, x in enumerate(c['fill4']['nodes'])]
        items += [('story', i + 1, s) for i, s in enumerate(st[PILOT[vid]]['new'])]
    else:
        items = [('story', i + 1, s) for i, s in enumerate(st[str(vid)]['new'])]
    d = f'{HERE}/audio/{vid}'; os.makedirs(d, exist_ok=True)
    name = VOICE[vid].split('.')[-1].lower()
    man = {'mediaId': vid, 'voice': VOICE[vid], 'items': []}
    for kind, i, text in items:
        h = hashlib.sha1(f'{text}|{VOICE[vid]}'.encode()).hexdigest()[:8]
        f = f'a60_{kind}{i}_{name}_{h}.m4a'; out = f'{d}/{f}'
        dur = render(vid, text, out) if not os.path.exists(out) else dur_of(out)
        man['items'].append({'kind': kind, 'i': i, 'text': text, 'file': f, 'object': f'sets/{vid}/{f}', 'duration': round(dur, 2), 'bytes': os.path.getsize(out)})
    keep = {x['file'] for x in man['items']} | {'manifest.json'}
    for f in os.listdir(d):
        if f not in keep: os.remove(f'{d}/{f}')
    json.dump(man, open(f'{d}/manifest.json', 'w'), ensure_ascii=False, indent=1)
    return f'{vid} {len(man["items"])} files'
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(4) as ex: print(list(ex.map(one, list(VOICE))))

# A66 (from tts65): records every text of ~/Projects/and-again-a66/lib/lab58.json whose recording is null (changed phrases, nouns, rows,
# story parts) and every new carousel caption (no recording in voices.captions). Each item keeps its voice (by
# identifier); a render equal to the default voice's stops the run.
#   python3 tts66.py -> audio/<id>/a66_<kind><i>_<voice>_<hash>.m4a + audio/<id>/manifest.json
import json, os, subprocess, hashlib, filecmp
HERE = os.path.dirname(os.path.abspath(__file__))
VOICE = {236: 'premium.en-US.Ava', 8039: 'premium.en-US.Ava', 62: 'enhanced.en-US.Evan', 7071: 'enhanced.en-US.Nathan',
         8055: 'enhanced.en-US.Evan', 8056: 'enhanced.en-US.Nathan', 900001: 'premium.en-US.Zoe', 900002: 'enhanced.en-US.Nathan'}
SAY = {}
def dur_of(f):
    return float(subprocess.run(['ffprobe', '-v', '0', '-show_entries', 'format=duration', '-of', 'csv=p=0', f], capture_output=True, text=True, timeout=30).stdout.strip())
def render(vid, text, out):
    aiff = out + '.aiff'; ref = out + '.ref.aiff'
    subprocess.run(['say', '-v', 'com.apple.voice.' + VOICE[vid], '-o', aiff, SAY.get(text, text)], check=True, timeout=120)
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
lab = {c['mediaId']: c for c in json.load(open(os.path.expanduser('~/Projects/and-again-a66/lib/lab58.json')))}
def one(vid):
    c = lab[vid]; v = c['voices']
    items = [('phrase', i + 1, c['taps'][i]['phrase']) for i, u in enumerate(v['phrases']) if u is None]
    items += [('noun', i + 1, c['nouns'][i]['word']) for i, u in enumerate(v['nouns']) if u is None]
    items += [('story', i + 1, c['story'][i]) for i, u in enumerate(v['story']) if u is None]
    items += [('row', i + 1, ' '.join(p['text'] for p in c['rows'][i])) for i, u in enumerate(v.get('rows') or []) if u is None]
    items += [('caption', i + 1, cap) for i, cap in enumerate(c['captions']) if cap not in v['captions']]
    d = f'{HERE}/audio/{vid}'; os.makedirs(d, exist_ok=True)
    name = VOICE[vid].split('.')[-1].lower()
    man = {'mediaId': vid, 'voice': VOICE[vid], 'items': []}
    for kind, i, text in items:
        h = hashlib.sha1(f'{text}|{VOICE[vid]}'.encode()).hexdigest()[:8]
        fn = f'a66_{kind}{i}_{name}_{h}.m4a'; out = f'{d}/{fn}'
        dur = render(vid, text, out) if not os.path.exists(out) else dur_of(out)
        man['items'].append({'kind': kind, 'i': i, 'text': text, 'file': fn, 'object': f'sets/{vid}/{fn}', 'duration': round(dur, 2), 'bytes': os.path.getsize(out)})
    json.dump(man, open(f'{d}/manifest.json', 'w'), ensure_ascii=False, indent=1)
    return f'{vid} {len(man["items"])}'
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(4) as ex: print(list(ex.map(one, list(VOICE))))

# A64 (from tts62): records ONLY texts without a recording - the new story parts (exercise 5), a replaced noun and its
# phrase (exercise 2), exercise 4 rows that are
# not one of the item's phrases, and mind-map phrases that are neither a carousel caption nor a phrase. Each item keeps its
# voice (by identifier); a render equal to the default voice's stops the run.
#   python3 tts64.py -> audio/<id>/a64_<kind><i>_<voice>_<hash>.m4a + audio/<id>/manifest.json
import json, os, subprocess, hashlib, filecmp
HERE = os.path.dirname(os.path.abspath(__file__))
LAB = os.path.expanduser('~/Projects/and-again-a64/lib/lab58.json')
VOICE = {236: 'premium.en-US.Ava', 8039: 'premium.en-US.Ava', 62: 'enhanced.en-US.Evan', 7071: 'enhanced.en-US.Nathan',
         8055: 'enhanced.en-US.Evan', 8056: 'enhanced.en-US.Nathan', 900001: 'premium.en-US.Zoe', 900002: 'enhanced.en-US.Nathan'}
def dur_of(f):
    return float(subprocess.run(['ffprobe', '-v', '0', '-show_entries', 'format=duration', '-of', 'csv=p=0', f], capture_output=True, text=True, timeout=30).stdout.strip())
# what `say` is given where the plain text was misheard (whisper heard "while the way"); the shown text stays the same
SAY = {'He held on to the rope all the way to work.': 'He held on to the rope [[slnc 120]] all the way to work.'}
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
lab = {c['mediaId']: c for c in json.load(open(f'{HERE}/upload/lab58_before_a64.json'))}
final = json.load(open(f'{HERE}/content/a64_final.json'))
def row_text(parts): return ' '.join(p['text'] for p in parts)
def one(vid):
    c = lab[vid]; f = final[str(vid)]
    phrases = [t['phrase'] for t in c['taps']]
    items = [('story', i + 1, t) for i, t in enumerate(f['story']['parts']) if t not in c['story']]
    # exercise 2: a replaced noun changes its phrase - both are recorded
    for x in f.get('ex2', []):
        if x.get('replacement'):
            i = [n['word'] for n in c['nouns']].index(x['noun'])
            items += [('phrase', i + 1, x['replacement']['phrase']), ('noun', i + 1, x['replacement']['noun'])]
            phrases[i] = x['replacement']['phrase']
    if 'ex4' in f:
        items += [('row', i + 1, row_text(r)) for i, r in enumerate(f['ex4']['rows']) if row_text(r) not in phrases]
        items += [('node', i + 1, n['caption']) for i, n in enumerate(f['ex4']['mindMap']['nodes']) if n['caption'] not in c['voices']['captions'] and n['caption'] not in phrases]
    d = f'{HERE}/audio/{vid}'; os.makedirs(d, exist_ok=True)
    name = VOICE[vid].split('.')[-1].lower()
    man = {'mediaId': vid, 'voice': VOICE[vid], 'items': []}
    for kind, i, text in items:
        h = hashlib.sha1(f'{text}|{VOICE[vid]}'.encode()).hexdigest()[:8]
        fn = f'a64_{kind}{i}_{name}_{h}.m4a'; out = f'{d}/{fn}'
        dur = render(vid, text, out) if not os.path.exists(out) else dur_of(out)
        man['items'].append({'kind': kind, 'i': i, 'text': text, 'file': fn, 'object': f'sets/{vid}/{fn}', 'duration': round(dur, 2), 'bytes': os.path.getsize(out)})
    json.dump(man, open(f'{d}/manifest.json', 'w'), ensure_ascii=False, indent=1)
    return f'{vid} {len(man["items"])}'
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(4) as ex: print(list(ex.map(one, list(VOICE))))

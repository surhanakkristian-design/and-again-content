# A71 (from tts69): records every lab text of lib/lab58.json whose recording is null after build71.py - phrases, nouns,
# carousel captions, story parts and exercise 4 rows (a row that is the same text as a phrase / caption reuses that file).
# Each item keeps its voice (by identifier); a render equal to the default voice's stops the run. Loudness: loudnorm -19,
# then measured (ebur128 integrated; files outside -19 +- 0.5 LU are re-rendered with the measured offset).
#   python3 tts71.py -> audio/tts/<id>/a71_<kind><i>_<voice>_<hash>.m4a, audio/voices71.json (the public URLs), audio/levels71.tsv
import json, os, subprocess, hashlib, filecmp
HERE = os.path.dirname(os.path.abspath(__file__))
VOICE = {236: 'premium.en-US.Ava', 8039: 'premium.en-US.Ava', 62: 'enhanced.en-US.Evan', 7071: 'enhanced.en-US.Nathan',
         8055: 'enhanced.en-US.Evan', 8056: 'enhanced.en-US.Nathan', 900001: 'premium.en-US.Zoe', 900002: 'enhanced.en-US.Nathan'}
PUB = 'https://abyrutykpvmzkfbesire.supabase.co/storage/v1/object/public/audio/sets'
LAB = '/Users/kristiansurhanak/Projects/and-again/lib/lab58.json'

def dur_of(f):
    return float(subprocess.run(['ffprobe', '-v', '0', '-show_entries', 'format=duration', '-of', 'csv=p=0', f], capture_output=True, text=True, timeout=30).stdout.strip())

def lufs(f):
    out = subprocess.run(['ffmpeg', '-nostats', '-hide_banner', '-i', f, '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True, timeout=60).stderr
    tail = out[out.rfind('Summary'):]
    for line in tail.splitlines():
        if line.strip().startswith('I:'): return float(line.split()[1])
    return None

def render(vid, text, out, gain=0.0):
    aiff = out + '.aiff'; ref = out + '.ref.aiff'
    subprocess.run(['say', '-v', 'com.apple.voice.' + VOICE[vid], '-o', aiff, text], check=True, timeout=120)
    subprocess.run(['say', '-o', ref, text], check=True, timeout=120)
    if filecmp.cmp(aiff, ref, shallow=False): raise SystemExit(f'{vid}: the voice {VOICE[vid]} fell back to the default')
    os.remove(ref)
    af = ('silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.03,areverse,'
          'silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.08,areverse,'
          f'loudnorm=I=-19:TP=-2:LRA=11,volume={gain}dB,aresample=44100')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', aiff, '-af', af, '-ac', '1', '-c:a', 'aac', '-b:a', '64k', '-movflags', '+faststart', out], check=True, timeout=60)
    os.remove(aiff)
    d = dur_of(out)
    if not (0.2 <= d <= 12): raise SystemExit(f'{out}: duration {d}')

def record(vid, kind, i, text):
    name = VOICE[vid].split('.')[-1].lower()
    h = hashlib.sha1(f'{text}|{VOICE[vid]}'.encode()).hexdigest()[:8]
    d = f'{HERE}/audio/tts/{vid}'; os.makedirs(d, exist_ok=True)
    fn = f'a71_{kind}{i}_{name}_{h}.m4a'; out = f'{d}/{fn}'
    if not os.path.exists(out):
        render(vid, text, out)
        level = lufs(out)
        if level is not None and abs(level + 19) > 0.5:
            render(vid, text, out, round(-19 - level, 2))
    return fn, out

lab = [c for c in json.load(open(LAB)) if c['mediaId'] in VOICE]
urls, levels = {}, []
for c in lab:
    vid = c['mediaId']; v = c['voices']; mine = urls.setdefault(str(vid), {})
    same = {}
    for i, t in enumerate(c['taps']):
        if v['phrases'][i]: same[t['phrase']] = v['phrases'][i]
    for cap, u in v['captions'].items():
        if u: same[cap] = u
    todo = [('phrase', i + 1, t['phrase']) for i, t in enumerate(c['taps']) if not v['phrases'][i]]
    todo += [('noun', i + 1, n['word']) for i, n in enumerate(c['nouns']) if not v['nouns'][i]]
    todo += [('caption', c['captions'].index(cap) + 1, cap) for cap, u in v['captions'].items() if not u]
    todo += [('story', i + 1, s) for i, s in enumerate(c['story']) if not v['story'][i]]
    for kind, i, text in todo:
        fn, out = record(vid, kind, i, text)
        mine[f'{kind}{i}'] = f'{PUB}/{vid}/{fn}'; same.setdefault(text, mine[f'{kind}{i}'])
        levels.append(f'{vid}\t{fn}\t{lufs(out)}\t{dur_of(out):.2f}\t{text}')
    for i, r in enumerate(c['rows']):
        if (v.get('rows') or [None] * len(c['rows']))[i]: continue
        text = ' '.join(p['text'] for p in r)
        if text in same: mine[f'row{i + 1}'] = same[text]; continue
        fn, out = record(vid, 'row', i + 1, text)
        mine[f'row{i + 1}'] = f'{PUB}/{vid}/{fn}'
        levels.append(f'{vid}\t{fn}\t{lufs(out)}\t{dur_of(out):.2f}\t{text}')
json.dump(urls, open(f'{HERE}/audio/voices71.json', 'w'), ensure_ascii=False, indent=1)
open(f'{HERE}/audio/levels71.tsv', 'w').write('\n'.join(levels) + '\n')
print(f'{len(levels)} recordings; LUFS range', min(float(l.split("\t")[2]) for l in levels), max(float(l.split("\t")[2]) for l in levels))

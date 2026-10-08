# A66: what Whisper (whisper-cli, ggml-small.en) hears in every new recording (audio/<id>/manifest.json) -> verify/whisper.json
import json, os, glob, subprocess, re, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = os.path.expanduser('~/.cache/whisper/ggml-small.en.bin')
def norm(s): return re.sub(r"[^a-z0-9' ]", '', s.lower().replace('-', ' ')).split()
out = []
for m in sorted(glob.glob(f'{HERE}/audio/*/manifest.json')):
    man = json.load(open(m))
    for it in man['items']:
        f = os.path.join(os.path.dirname(m), it['file'])
        with tempfile.TemporaryDirectory() as t:
            wav = f'{t}/a.wav'
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', f, '-ar', '16000', '-ac', '1', wav], check=True, timeout=60)
            r = subprocess.run(['whisper-cli', '-m', MODEL, '-nt', '-np', '-f', wav], capture_output=True, text=True, timeout=180)
        heard = ' '.join(r.stdout.split())
        out.append({'id': man['mediaId'], 'file': it['file'], 'text': it['text'], 'heard': heard, 'same': norm(heard) == norm(it['text'])})
json.dump(out, open(f'{HERE}/verify/whisper.json', 'w'), ensure_ascii=False, indent=1)
for o in out: print(o['id'], o['same'], '|', o['text'], '|', o['heard'])

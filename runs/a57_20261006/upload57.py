# A57: uploads the audio objects of one or more batches ONE FILE AT A TIME (bucket `audio`, sets/<media id>/a57_<lang>_*), each
# with retries, and reads every object back (the public URL's bytes must equal the local file). The bulk `storage cp -r` of A55
# stopped at the first transport error. The project's service key is read from the Supabase CLI inside this process and is never
# printed or written to disk. New object names only (an existing object with the same bytes counts as uploaded; different
# bytes = an error, never overwritten).
#   python3 upload57.py <batch>_<lang> [...]        -> upload/<batch>_<lang>.ok (every object read back) or exit 1
import json, os, sys, subprocess, time, glob, hashlib, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__))
REF = 'abyrutykpvmzkfbesire'; API = f'https://{REF}.supabase.co/storage/v1'
PUB = f'{API}/object/public/audio'
def cli():
    c = sorted(glob.glob(os.path.expanduser('~/.npm/_npx/*/node_modules/@supabase/cli-darwin-arm64/bin/supabase')))
    return os.environ.get('SUPABASE_BIN') or (c[0] if c else 'supabase')
def service_key():
    out = subprocess.run([cli(), 'projects', 'api-keys', '--project-ref', REF, '-o', 'json'], capture_output=True, text=True, timeout=90, cwd=os.path.expanduser('~/Projects/and-again')).stdout
    d = json.loads(out); d = d.get('rows', d) if isinstance(d, dict) else d
    return next(k['api_key'] for k in d if k.get('name') == 'service_role')
KEY = None
def remote(obj):
    try:
        with urllib.request.urlopen(urllib.request.Request(f'{PUB}/{obj}', headers={'Cache-Control': 'no-cache'}), timeout=30) as r: return r.read()
    except urllib.error.HTTPError as x:
        if x.code in (400, 404): return None
        raise
def put(obj, data):
    req = urllib.request.Request(f'{API}/object/audio/{obj}', data=data, method='POST', headers={
        'Authorization': f'Bearer {KEY}', 'apikey': KEY, 'Content-Type': 'audio/mp4',
        'Cache-Control': 'public, max-age=31536000, immutable', 'x-upsert': 'false'})
    try:
        with urllib.request.urlopen(req, timeout=60) as r: return r.status
    except urllib.error.HTTPError as x:
        if x.code in (400, 409) and b'exists' in x.read().lower(): return 409
        raise
def one(lang, obj):
    local = open(f'{HERE}/audio/{lang}/{obj[len("sets/"):]}', 'rb').read()
    err = None
    for t in range(6):
        try:
            got = remote(obj)
            if got == local: return None
            if got is not None: return f'{obj}: a different object with this name is in storage (not overwritten)'
            put(obj, local)
            time.sleep(0.3)
            got = remote(obj)
            if got == local: return None
            err = 'read back differs' if got is not None else 'not readable after upload'
        except Exception as x: err = str(x)[:120]
        time.sleep(min(60, 3 * 2 ** t))
    return f'{obj}: {err}'
if __name__ == '__main__':
    KEY = service_key()
    bad_all = 0
    for name in sys.argv[1:]:
        b = json.load(open(f'{HERE}/batches/{name}.json')); lang = b['lang']
        with ThreadPoolExecutor(8) as ex: res = list(ex.map(lambda o: one(lang, o), b['objects']))
        bad = [r for r in res if r]
        os.makedirs(f'{HERE}/upload', exist_ok=True)
        if bad:
            bad_all += 1
            open(f'{HERE}/upload/{name}.errors', 'w').write('\n'.join(bad) + '\n')
            if os.path.exists(f'{HERE}/upload/{name}.ok'): os.remove(f'{HERE}/upload/{name}.ok')
            print(f'{name}: {len(bad)} of {len(res)} objects NOT read back: {bad[:3]}')
        else:
            open(f'{HERE}/upload/{name}.ok', 'w').write(f'{len(res)} objects read back {time.strftime("%Y-%m-%d %H:%M")}\n')
            print(f'{name}: all {len(res)} objects read back')
    sys.exit(1 if bad_all else 0)

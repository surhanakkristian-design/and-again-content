"""Shared helper: run SQL through the linked Supabase CLI and return rows (both JSON shapes)."""
import glob, json, os, subprocess

REPO = os.path.expanduser('~/Projects/and-again')  # a linked checkout (supabase/.temp/project-ref)
def _bin():
    if os.environ.get('SUPABASE_BIN'):
        return os.environ['SUPABASE_BIN']
    for c in [os.path.expanduser('~/.npm/_npx/aa8e5c70f9d8d161/node_modules/@supabase/cli-darwin-arm64/bin/supabase')] + glob.glob(os.path.expanduser('~/.npm/_npx/*/node_modules/@supabase/cli-darwin-arm64/bin/supabase')):
        if os.access(c, os.X_OK):
            return c
    raise SystemExit('No Supabase CLI binary found. Set SUPABASE_BIN=/path/to/supabase.')
SB = _bin()

def rows(sql, timeout=300):
    if len(sql) > 60_000:  # a long statement goes through a file (the argument list has a limit)
        import tempfile
        with tempfile.NamedTemporaryFile('w', suffix='.sql', delete=False) as f:
            f.write(sql); path = f.name
        try:
            r = subprocess.run([SB, 'db', 'query', '--linked', '-o', 'json', '-f', path], cwd=REPO, capture_output=True, text=True, timeout=timeout)
        finally:
            os.unlink(path)
    else:
        r = subprocess.run([SB, 'db', 'query', '--linked', '-o', 'json', sql], cwd=REPO, capture_output=True, text=True, timeout=timeout)
    if r.returncode != 0:
        raise RuntimeError('query failed: ' + sql[:200] + '\n' + '\n'.join(l for l in r.stderr.splitlines() if 'new version' not in l and 'recommend updating' not in l))
    d = json.loads(r.stdout)
    out = d.get('rows') if isinstance(d, dict) else d
    if not isinstance(out, list):
        raise RuntimeError('unexpected JSON from the CLI: ' + r.stdout[:300])
    return out

def scalar(sql):
    r = rows(sql)
    return list(r[0].values())[0] if r else None

"""Thin Supabase CLI wrapper for the data pass. Accepts both JSON shapes of `db query -o json`
({"rows": [...]} under agent detection, a bare list in a plain terminal)."""
import glob, json, os, subprocess, tempfile

REPO = os.path.expanduser("~/Projects/and-again")


def _bin():
    b = os.environ.get("SUPABASE_BIN")
    if b:
        return b
    cands = [os.path.expanduser("~/.npm/_npx/aa8e5c70f9d8d161/node_modules/@supabase/cli-darwin-arm64/bin/supabase")]
    cands += glob.glob(os.path.expanduser("~/.npm/_npx/*/node_modules/@supabase/cli-darwin-arm64/bin/supabase"))
    for c in cands:
        if os.access(c, os.X_OK):
            return c
    raise SystemExit("no supabase CLI binary")


def rows(sql):
    """Run SQL (read or write) and return the result rows."""
    with tempfile.NamedTemporaryFile("w", suffix=".sql", delete=False) as f:
        f.write(sql)
        path = f.name
    try:
        p = subprocess.run([_bin(), "db", "query", "--linked", "-o", "json", "--file", path],
                           cwd=REPO, capture_output=True, text=True)
    finally:
        os.unlink(path)
    if p.returncode != 0:
        raise RuntimeError("query failed: " + p.stderr[-2000:])
    d = json.loads(p.stdout) if p.stdout.strip() else []
    r = d.get("rows") if isinstance(d, dict) else d
    if not isinstance(r, list):
        raise RuntimeError("unexpected JSON: " + p.stdout[:300])
    return r


def q(s):
    """SQL string literal (dollar-free, standard quoting)."""
    if s is None:
        return "NULL"
    return "'" + s.replace("'", "''") + "'"

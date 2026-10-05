"""A50: restore the old cards' tables from this folder (backup.py made it).
  python3 restore.py                      every table into public (recreated from schema.sql)
  python3 restore.py --tables tinder_sentences listening_questions
  python3 restore.py --schema a50_restore_check   a test copy in another schema (columns + defaults
                                          + identity copied from schema.sql's columns, no FKs/policies)
Rows go in chunks (the SQL API takes about 2 MB per call). After loading, every restored table is
dumped again exactly as backup.py dumps it and its row count and sha256 must equal manifest.json,
else the script stops with a non-zero exit (nothing is dropped by this script)."""
import argparse, hashlib, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sb import rows, scalar

HERE = os.path.dirname(os.path.abspath(__file__))
CHUNK_BYTES = 1_200_000

def sections():
    text = open(os.path.join(HERE, 'schema.sql')).read()
    out = {}
    for part in re.split(r'^-- (\w+)\n', text, flags=re.M)[1:]:
        pass
    parts = re.split(r'^-- (\w+)\n', text, flags=re.M)
    for i in range(1, len(parts), 2):
        out[parts[i]] = parts[i + 1]
    return out

def statements(sql):
    # one statement per line group ending with ';' at end of line
    out, cur = [], []
    for line in sql.splitlines():
        cur.append(line)
        if line.rstrip().endswith(';'):
            out.append('\n'.join(cur).strip()); cur = []
    return [s for s in out if s]

def dump_sha(schema, t, pk):
    h = hashlib.sha256(); n = 0; off = 0
    while True:
        page = rows(f'select to_jsonb(t) as r from (select * from {schema}.{t} order by {pk} limit 5000 offset {off}) t')
        for r in page:
            line = json.dumps(r['r'], ensure_ascii=False, sort_keys=True) + '\n'
            h.update(line.encode()); n += 1
        if len(page) < 5000: return n, h.hexdigest()
        off += 5000

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--tables', nargs='*')
    ap.add_argument('--schema', default='public')
    a = ap.parse_args()
    manifest = json.load(open(os.path.join(HERE, 'manifest.json')))['tables']
    tables = a.tables or list(manifest)
    ddl = sections()
    for t in tables:
        m = manifest[t]
        if scalar(f"select to_regclass('{a.schema}.{t}') is not null"):
            sys.exit(f'{a.schema}.{t} exists already - nothing restored (drop or rename it first)')
        if a.schema == 'public':
            for st in statements(ddl[t]):
                rows(st)
        else:
            rows(f'create schema if not exists {a.schema}')
            create = statements(ddl[t])[0]
            cols = [l for l in create.splitlines()[1:-1] if not l.strip().startswith('constraint')]
            rows(f'create table {a.schema}.{t} (\n' + ',\n'.join(c.rstrip(',') for c in cols) + f',\n  primary key ("{m["pk"]}")\n);')
        has_identity = scalar(f"select count(*) from pg_attribute where attrelid = '{a.schema}.{t}'::regclass and attidentity <> ''") > 0
        overriding = ' overriding system value' if has_identity else ''
        buf, size, loaded = [], 0, 0
        def flush():
            nonlocal buf, size, loaded
            if not buf: return
            payload = '[' + ','.join(buf) + ']'
            tag = '$a50$'
            assert tag not in payload
            rows(f'insert into {a.schema}.{t}{overriding} select * from jsonb_populate_recordset(null::{a.schema}.{t}, {tag}{payload}{tag}::jsonb)')
            loaded += len(buf); buf, size = [], 0
        with open(os.path.join(HERE, f'{t}.jsonl')) as f:
            for line in f:
                line = line.rstrip('\n')
                if size + len(line.encode()) > CHUNK_BYTES: flush()
                buf.append(line); size += len(line.encode()) + 1
        flush()
        if has_identity:
            rows(f"select setval(pg_get_serial_sequence('{a.schema}.{t}', 'id'), (select max(id) from {a.schema}.{t}))")
        n, sha = dump_sha(a.schema, t, m['pk'])
        ok = n == m['file_rows'] and sha == m['sha256']
        print(f'{a.schema}.{t}: loaded {loaded}, now {n} rows, sha {"equal" if sha == m["sha256"] else "DIFFERENT"} -> {"OK" if ok else "FAILED"}')
        if not ok: sys.exit(1)

if __name__ == '__main__':
    main()

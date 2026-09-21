#!/usr/bin/env python3
"""Phase 2I stage 2b - write guard. Imported FIRST by stack_frozen.py and stack_tonly.py (before any 1W module).
Every write the chain attempts to a path inside the content repo but OUTSIDE phase2i/ (open in w/a/x/+ mode,
io.open, os.open with write flags, os.replace/rename, os.remove/unlink, os.makedirs/mkdir of a new dir) is
redirected to $P2I_RUN_DIR/_redirected/<repo-relative path> and logged to $P2I_RUN_DIR/_redirected/REDIRECTS.jsonl.
A later READ of such a path gets the redirected copy if one exists. Reads are otherwise untouched. No verdict
effect: the chain sees the same bytes it wrote. (DEFECTS 3: run in place the chain appends to phase1p/.)"""
import builtins, io, json, os, traceback
HERE = os.path.dirname(os.path.abspath(__file__))
TOFF = os.path.dirname(HERE)
REPO = os.path.dirname(TOFF)
_open, _os_open, _replace, _rename = builtins.open, os.open, os.replace, os.rename
_remove, _unlink, _makedirs, _mkdir = os.remove, os.unlink, os.makedirs, os.mkdir
WFLAGS = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND | os.O_TRUNC
COUNT = [0]


def _rd():
    return os.environ.get('P2I_RUN_DIR') or os.path.join(HERE, 'run')


def _abs(path):
    if isinstance(path, int):
        return None
    try:
        return os.path.abspath(os.fspath(path))
    except TypeError:
        return None


def _guarded(ap):
    return ap is not None and ap.startswith(REPO + os.sep) and not ap.startswith(HERE + os.sep)


def _mapped(ap):
    return os.path.join(_rd(), '_redirected', os.path.relpath(ap, REPO))


def target(path, op='write'):
    ap = _abs(path)
    if not _guarded(ap):
        return path
    new = _mapped(ap)
    _makedirs(os.path.dirname(new), exist_ok=True)
    COUNT[0] += 1
    try:
        with _open(os.path.join(_rd(), '_redirected', 'REDIRECTS.jsonl'), 'a', encoding='utf-8') as fh:
            fh.write(json.dumps({'op': op, 'from': os.path.relpath(ap, REPO), 'to': new,
                                 'where': ['%s:%d %s' % (f.filename, f.lineno, f.name)
                                           for f in traceback.extract_stack()[-5:-2]]}) + '\n')
    except Exception:
        pass
    return new


def _read_path(path):
    ap = _abs(path)
    if _guarded(ap) and os.path.exists(_mapped(ap)):
        return _mapped(ap)
    return path


def g_open(file, mode='r', *a, **k):
    if any(c in mode for c in 'wax+'):
        return _open(target(file, 'open:' + mode), mode, *a, **k)
    return _open(_read_path(file), mode, *a, **k)


def g_os_open(path, flags, *a, **k):
    if flags & WFLAGS:
        return _os_open(target(path, 'os.open'), flags, *a, **k)
    return _os_open(_read_path(path), flags, *a, **k)


def g_replace(s, d, *a, **k):
    return _replace(_read_path(s), target(d, 'replace'), *a, **k)


def g_rename(s, d, *a, **k):
    return _rename(_read_path(s), target(d, 'rename'), *a, **k)


def g_remove(p, *a, **k):
    return _remove(target(p, 'remove'), *a, **k)


def g_unlink(p, *a, **k):
    return _unlink(target(p, 'unlink'), *a, **k)


def g_makedirs(p, *a, **k):
    ap = _abs(p)
    if _guarded(ap) and os.path.isdir(ap):
        return None
    return _makedirs(target(p, 'makedirs'), *a, **k)


def g_mkdir(p, *a, **k):
    return _mkdir(target(p, 'mkdir'), *a, **k)


builtins.open = io.open = g_open
os.open, os.replace, os.rename = g_os_open, g_replace, g_rename
os.remove, os.unlink, os.makedirs, os.mkdir = g_remove, g_unlink, g_makedirs, g_mkdir

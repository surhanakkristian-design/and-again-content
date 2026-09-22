#!/usr/bin/env python3
"""Serialised git commit for the parallel wave-1 languages (fcntl lock on wave1/.commit.lock).
    python3 -B /abs/wave1/common/gitc.py "message" /abs/path [/abs/path ...]   -> commits ONLY those paths."""
import fcntl, os, subprocess, sys, time
REPO = '/Users/kristiansurhanak/Projects/and-again-content'
LOCK = REPO + '/translation-offline/wave1/.commit.lock'
TRAILER = '\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>'


def git(args, **kw):
    """index.lock held by another session (the data pass commits to this repo too): wait 30 s and retry."""
    for i in range(40):
        p = subprocess.run(args, capture_output=True, text=True)
        if p.returncode == 0 or 'index.lock' not in (p.stderr or ''):
            if kw.get('check') and p.returncode != 0:
                raise subprocess.CalledProcessError(p.returncode, args, p.stdout, p.stderr)
            return p
        time.sleep(30)
    raise SystemExit('index.lock persisted 20 minutes')


def commit(msg, paths):
    for p in paths:
        if not os.path.isabs(p):
            raise SystemExit('REFUSED: relative path %r' % p)
    with open(LOCK, 'w') as fh:
        fcntl.flock(fh, fcntl.LOCK_EX)
        g = ['git', '-C', REPO]
        git(g + ['add', '-A', '--'] + paths, check=True)
        st = git(g + ['diff', '--cached', '--quiet', '--'] + paths)
        if st.returncode == 0:
            return 'nothing to commit'
        git(g + ['commit', '-q', '-m', msg + TRAILER, '--'] + paths, check=True)
        return subprocess.run(g + ['rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()


if __name__ == '__main__':
    print(commit(sys.argv[1], sys.argv[2:]))

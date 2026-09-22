#!/usr/bin/env python3
"""Serialised git commit for the parallel wave-1 languages (fcntl lock on wave1/.commit.lock).
    python3 -B /abs/wave1/common/gitc.py "message" /abs/path [/abs/path ...]   -> commits ONLY those paths."""
import fcntl, os, subprocess, sys
REPO = '/Users/kristiansurhanak/Projects/and-again-content'
LOCK = REPO + '/translation-offline/wave1/.commit.lock'
TRAILER = '\n\nCo-Authored-By: Claude Opus 5 <noreply@anthropic.com>'


def commit(msg, paths):
    for p in paths:
        if not os.path.isabs(p):
            raise SystemExit('REFUSED: relative path %r' % p)
    with open(LOCK, 'w') as fh:
        fcntl.flock(fh, fcntl.LOCK_EX)
        g = ['git', '-C', REPO]
        subprocess.run(g + ['add', '-A', '--'] + paths, check=True, capture_output=True)
        st = subprocess.run(g + ['diff', '--cached', '--quiet', '--'] + paths)
        if st.returncode == 0:
            return 'nothing to commit'
        subprocess.run(g + ['commit', '-q', '-m', msg + TRAILER, '--'] + paths, check=True, capture_output=True)
        return subprocess.run(g + ['rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()


if __name__ == '__main__':
    print(commit(sys.argv[1], sys.argv[2:]))

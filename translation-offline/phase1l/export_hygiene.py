#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2.3 — reference-hygiene EXPORT (plumbing only; a separate blind agent does the judging).

    python3 -B phase1l/export_hygiene.py --side dev
    python3 -B phase1l/export_hygiene.py --side fresh        # AFTER the freeze only

Writes ONLY {sid, slovak, v} — the stored accepted reference list — into
phase1l/hygiene/in_<side>_<n>.json, pretty-printed, <= 1100 lines per file.
NEVER a judge label, NEVER a learner answer, NEVER an intent. Every read is logged in
phase1l/access_log.jsonl through loader_1l.

The blind agent answers with phase1l/hygiene/out_<side>_<n>.json:
  [{"sid": 140001, "remove": ["…"], "replace": [{"from": "…", "to": "…"}], "reason": "…"}]
"""
import argparse, json, os, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import loader_1l as L                                                      # noqa: E402
OUT = os.path.join(HERE, 'hygiene')
MAX_LINES = 1100


def records(side, purpose):
    if side == 'dev':
        rows = L.load_dev_sentences(purpose=purpose, arm_b=True)
        return [{'sid': int(r['sid']), 'slovak': r['sk'],
                 'v': list(r.get('annotation_v') or r.get('refs') or [])} for r in rows]
    if side == 'fresh':
        rows = L.load_fresh_sentences(purpose=purpose)
        out = []
        for r in rows:
            a = (r.get('annotation') or {})
            hy = a.get('hygienised', a) or {}
            out.append({'sid': int(r['sid']), 'slovak': r['sk'],
                        'v': list(hy.get('v') or r.get('annotation_v') or r.get('refs') or [])})
        return out
    raise ValueError(side)


def chunk(recs):
    files, cur = [], []
    for r in recs:
        trial = cur + [r]
        if cur and len(json.dumps(trial, ensure_ascii=False, indent=1).splitlines()) > MAX_LINES:
            files.append(cur); cur = [r]
        else:
            cur = trial
    if cur:
        files.append(cur)
    return files


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--side', choices=('dev', 'fresh'), required=True)
    a = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    purpose = ('Phase 1L reference-hygiene export, side %s: SLOVAK + stored reference list ONLY, '
               'no answers, no labels' % a.side)
    recs = sorted(records(a.side, purpose), key=lambda r: r['sid'])
    for n, part in enumerate(chunk(recs), 1):
        p = os.path.join(OUT, 'in_%s_%d.json' % (a.side, n))
        open(p, 'w', encoding='utf-8').write(json.dumps(part, ensure_ascii=False, indent=1) + '\n')
        print('%s  sids %d  lines %d' % (p, len(part), sum(1 for _ in open(p, encoding='utf-8'))))
    print('side=%s  sids %d  references %d' % (a.side, len(recs), sum(len(r['v']) for r in recs)))


if __name__ == '__main__':
    main()

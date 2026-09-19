#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phase 1M recon — (a) export the 210 EXISTING sentences (Slovak/level/topic only, no references,
answers or labels) for the new-set writers, (b) the brief-§4 caching check on
loader_1k.load_fresh_annotations.  Zero model calls.  Run:

    PYTHONDONTWRITEBYTECODE=1 python3 -B phase1m/export_existing_210.py
"""
import sys, os, json, datetime, collections
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import loader_1l as L          # noqa: E402  (patches loader_1k._log -> phase1m/access_log.jsonl)
import runner_1l as RL         # noqa: E402  (its HERE is phase1m: calls.jsonl/hygiene point here)
import loader_1k as LK         # noqa: E402  (same module object, _log already redirected)

OUT = os.path.join(HERE, 'existing_210.json')
ACCESS = os.path.join(HERE, 'access_log.jsonl')
PURPOSE = ('Phase 1M recon-code: export Slovak/level/topic of the 210 existing sentences so the '
           'new-set writers can avoid duplicating them; no references, answers or labels exported')


def alog(side, what, n, purpose=PURPOSE):
    rec = {'ts': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
           'side': side, 'what': what, 'caller': 'export_existing_210.py', 'n': n,
           'purpose': purpose}
    with open(ACCESS, 'a', encoding='utf-8') as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + '\n')


def meta(loader):
    m = {}
    for s in loader(purpose=PURPOSE, arm_b=True):
        m[int(s['sid'])] = {'level': s.get('level'), 'topic': s.get('topic'), 'sk': s['sk']}
    return m


rows = []
for side, tag, loader in (('dev', 'dev', LK.load_dev_sentences),
                          ('replay1j', 'holdout', LK.load_holdout1j_sentences)):
    m = meta(loader)
    st, recs, ann, by, info = RL.build_side(side, False, PURPOSE)
    alog('1j:%s' % tag, 'runner_1l.build_side records (sid + arm-B sk only used)', len(recs))
    seen = {}
    for r in recs:
        sid = int(r['sid'])
        if sid not in seen:
            mm = m.get(sid, {})
            seen[sid] = {'sid': sid, 'side': tag, 'slovak': r['sk'],
                         'level': r.get('level') or mm.get('level'),
                         'topic': r.get('topic') or mm.get('topic')}
    drift = sum(1 for sid, x in seen.items() if m.get(sid, {}).get('sk') != x['slovak'])
    print('[%s] %d sentences, sk drift vs loader arm-B sentences: %d' % (tag, len(seen), drift))
    rows += [seen[k] for k in sorted(seen)]

fs = L.load_fresh_sentences(purpose=PURPOSE)
alog('1k:fresh', 'sentences (sid/sk/level/topic only)', len(fs))
for s in fs:
    rows.append({'sid': int(s['sid']), 'side': 'fresh1k', 'slovak': s['sk'],
                 'level': s.get('level'), 'topic': s.get('topic')})

assert all(set(r) == {'sid', 'side', 'slovak', 'level', 'topic'} for r in rows)
json.dump(rows, open(OUT, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
lv = collections.Counter(r['level'] for r in rows)
sd = collections.Counter(r['side'] for r in rows)
print('TOTAL %d  sides %s  levels %s' % (len(rows), json.dumps(sd), json.dumps(lv)))

# ------------------------------------------------------------------ §4 caching check
a1 = LK.load_fresh_annotations(purpose=PURPOSE + ' | caching check call 1 of 2')
a2 = LK.load_fresh_annotations(purpose=PURPOSE + ' | caching check call 2 of 2')
alog('1k:fresh', 'annotations x2 (caching check, contents not inspected)', len(a1))
k0 = sorted(a1)[0]
same_top, same_nested = (a1 is a2), (a1[k0] is a2[k0])
verdict = 'cached' if (same_top or same_nested) else 'fresh-object-per-call'
print('CACHING top-level identical object: %s   nested per-sid object identical: %s   -> %s'
      % (same_top, same_nested, verdict))
open(os.path.join(HERE, 'CACHING_CHECK.md'), 'w', encoding='utf-8').write(
    '# Phase 1M — caching check on `loader_1k.load_fresh_annotations` (brief §4)\n\n'
    'The loader body (`phase1k/loader_1k.py` lines 196-199), verbatim:\n\n'
    '```python\n'
    "def load_fresh_annotations(purpose='', path=None):\n"
    "    a = json.load(open(path or os.path.join(FRESH, 'annotations_fresh.json'), encoding='utf-8'))\n"
    "    _log('1k:fresh', 'annotations', len(a), purpose)\n"
    '    return a\n'
    '```\n\n'
    'There is no module-level memo (contrast `loader_1k._rewrites`, which *does* cache into the\n'
    'global `_RW` and returns `dict(_RW)`). Every call re-opens the file and re-parses the JSON.\n\n'
    '## Runtime result (two consecutive calls in one process)\n\n'
    '* top-level dicts are the same object: **%s**\n'
    '* per-sid nested objects are the same object (sid `%s`): **%s**\n\n'
    '**Verdict: %s.** A mutation of the returned annotations (e.g. `apply_hygiene`, which rewrites\n'
    "`hy['v']` in place) therefore affects ONLY the copy held by the caller; the next loader call\n"
    'returns pristine annotations. Conversely, a caller that wants the hygienised annotations to\n'
    'persist across calls must keep its own reference.\n'
    % (same_top, k0, same_nested, verdict))
print('written', OUT, 'and CACHING_CHECK.md')

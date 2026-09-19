#!/usr/bin/env python3
"""Phase 1T loader — the ONLY door to phase1t/set/data and to its judge labels.

Same contract as loader_1p/loader_1n: every read appends one JSON line to
phase1t/run/access_log.jsonl in the 1N convention {ts, side, what, caller, n, purpose}.
Nothing is ever written into phase1t/set/ or into any earlier phase directory.

phase1t/set/data/sentences.json    [{sid, slovak, level, topic, tags{half, writer_tags{...}}}]
                                   sid 180001..180100  (SPLIT_1T.md: numeric sid = 180000 + n)
phase1t/set/data/annotations.json  {"<sid>": {hygienised{v,lk,alt,...}, voice_sk, agent_nom,
                                              tf_gold, tense_open, perfective_present}}
phase1t/set/data/items.json        [{id, sid, kind, intent, form, tags[], passive, answer}]
phase1t/set/data/labels.json       {"<item id>": {judged, type, passive, agent_drop, tip,
                                                  borderline, ...}}   <- LABELS, --final only
"""
import datetime
import json
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))              # phase1t/run
P1T = os.path.dirname(HERE)                                    # phase1t
SET = os.path.join(P1T, 'set')
DATA = os.path.join(SET, 'data')
LOG = os.path.join(HERE, 'access_log.jsonl')

TYPES = ('T', 'W', 'M', 'S')
SID_LO, SID_HI = 180001, 180100
TAGS = ('plain', 'determiner', 'aspect', 'by-passive', 'by-passive-embedded', 'skp-passive',
        'agentdrop-main', 'agentdrop-embedded', 'timeframe', 'number')
PASSIVE_TAGS = (None, 'by', 'agentless')
LEVELS = ('A1', 'A2', 'B1', 'B2')


# ------------------------------------------------------------------ access log
def _log(side, what, n, purpose, caller=None):
    rec = {'ts': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
           'side': side, 'what': what,
           'caller': caller or os.path.basename(sys.argv[0] or 'interactive'),
           'n': n, 'purpose': purpose or ''}
    d = os.path.dirname(LOG)
    if d and not os.path.isdir(d):
        os.makedirs(d, exist_ok=True)
    with open(LOG, 'a', encoding='utf-8') as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + '\n')
    return rec


def _json(path, side, what, purpose, caller):
    if not os.path.exists(path):
        raise SystemExit('REFUSED: %s does not exist (the set side has not delivered it yet)' % path)
    obj = json.load(open(path, encoding='utf-8'))
    _log(side, what, len(obj), purpose, caller or 'loader_1t.py')
    return obj


def _dirs(data_dir):
    if not data_dir or os.path.abspath(data_dir) == os.path.abspath(DATA):
        return DATA, '1t:fresh1t', False
    return (data_dir, '1t:ext:%s' % os.path.basename(os.path.dirname(os.path.abspath(data_dir))),
            True)


# ------------------------------------------------------------------ the set
def load_sentences(purpose, caller=None, data_dir=None):
    d, side, ext = _dirs(data_dir)
    rows = _json(os.path.join(d, 'sentences.json'), side, 'data/sentences.json', purpose, caller)
    if not isinstance(rows, list) or not rows:
        raise SystemExit('REFUSED: data/sentences.json is not a non-empty list')
    seen = set()
    for s in rows:
        sid = int(s['sid'])
        if sid in seen:
            raise SystemExit('REFUSED: duplicate sid %d in sentences.json' % sid)
        seen.add(sid)
        if not ext and not (SID_LO <= sid <= SID_HI):
            raise SystemExit('REFUSED: sid %d outside the agreed range %d..%d'
                             % (sid, SID_LO, SID_HI))
        for k in ('slovak', 'level', 'topic'):
            if not s.get(k):
                raise SystemExit('REFUSED: sid %d has no %r' % (sid, k))
        if s['level'] not in LEVELS:
            raise SystemExit('REFUSED: sid %d has level %r' % (sid, s['level']))
        s['tags'] = dict(s.get('tags') or {})
        s['tags']['writer_tags'] = dict(s['tags'].get('writer_tags') or {})
    return rows


def load_annotations(purpose, caller=None, data_dir=None):
    d, side, _ext = _dirs(data_dir)
    ann = _json(os.path.join(d, 'annotations.json'), side, 'data/annotations.json', purpose, caller)
    if not isinstance(ann, dict) or not ann:
        raise SystemExit('REFUSED: data/annotations.json is not a non-empty dict')
    for sid, a in ann.items():
        hy = a.get('hygienised', a)
        if not [x for x in (hy.get('v') or []) if isinstance(x, str) and x.strip()]:
            raise SystemExit('REFUSED: annotation %s carries no accepted reference in "v"' % sid)
    return ann


def load_items(purpose, caller=None, data_dir=None):
    d, side, ext = _dirs(data_dir)
    items = _json(os.path.join(d, 'items.json'), side, 'data/items.json', purpose, caller)
    if not isinstance(items, list) or not items:
        raise SystemExit('REFUSED: data/items.json is not a non-empty list')
    seen = set()
    for it in items:
        i = it['id']
        if i in seen:
            raise SystemExit('REFUSED: duplicate item id %s' % i)
        seen.add(i)
        if i.split(':')[0] not in ('C', 'W'):
            raise SystemExit('REFUSED: item id %s does not start with C: or W:' % i)
        if not it.get('answer'):
            raise SystemExit('REFUSED: item %s has no answer' % i)
        tg = it.get('tags')
        if not ext:
            if not isinstance(tg, list) or not tg:
                raise SystemExit('REFUSED: item %s has no tags list' % i)
            bad = [t for t in tg if t not in TAGS]
            if bad:
                raise SystemExit('REFUSED: item %s carries unknown tags %s' % (i, bad))
        if it.get('passive') not in PASSIVE_TAGS:
            it['passive'] = ('agentless' if ('agentdrop-main' in (tg or [])
                                             or 'agentdrop-embedded' in (tg or [])
                                             or 'skp-passive' in (tg or [])) else
                             'by' if ('by-passive' in (tg or [])
                                      or 'by-passive-embedded' in (tg or [])) else None)
    return items


# ------------------------------------------------------------------ labels (--final only)
def labels_path(data_dir=None):
    d, _side, _ext = _dirs(data_dir)
    return os.path.join(d, 'labels.json')


def have_labels(data_dir=None):
    return os.path.exists(labels_path(data_dir))


def load_labels(purpose, caller=None, data_dir=None):
    """-> (labels, meta).  labels: item id -> the judge record as assemble_1t.py joined it
    ({judged, type, passive, agent_drop, tip, borderline, ...}).  THE ONLY label read site."""
    d, side, ext = _dirs(data_dir)
    p = os.path.join(d, 'labels.json')
    lab = _json(p, side.replace('1t:', '1t:labels:'), 'data/labels.json', purpose, caller)
    if not isinstance(lab, dict) or not lab:
        raise SystemExit('REFUSED: data/labels.json is not a non-empty dict')
    bad = []
    for iid, r in lab.items():
        if not isinstance(r, dict) or r.get('judged') not in ('correct', 'wrong'):
            bad.append({'item': iid, 'why': 'judged=%r' % (r or {}).get('judged')})
            continue
        if r.get('judged') == 'correct':
            r['type'] = None
        elif r.get('type') not in TYPES:
            bad.append({'item': iid, 'why': 'wrong with type=%r' % r.get('type')})
            r['type'] = None
    meta = {'labels_path': p, 'items_labelled': len(lab), 'rejected_rows': bad,
            'external': ext,
            'judged': _count(r.get('judged') for r in lab.values()),
            'types': _count(r.get('type') for r in lab.values() if r.get('judged') == 'wrong')}
    join = os.path.join(SET, 'assemble_1t.json')
    if not ext and os.path.exists(join):
        try:
            obj = json.load(open(join, encoding='utf-8'))
            _log(side.replace('1t:', '1t:labels:'), 'set/assemble_1t.json', 1,
                 'judge-noise / duplicate-control statistics of the label join', caller)
            meta['label_join'] = obj.get('labels') if isinstance(obj, dict) else None
        except Exception as e:                                        # pragma: no cover
            meta['label_join_error'] = str(e)
    return lab, meta


def _count(it):
    out = {}
    for x in it:
        out[str(x)] = out.get(str(x), 0) + 1
    return out

#!/usr/bin/env python3
"""Phase 1U loader — the ONLY door to phase1u/data and to its judge labels.
Same contract as loader_1t: every read appends one JSON line to phase1u/run/access_log.jsonl
{ts, side, what, caller, n, purpose}.  Nothing outside phase1u/run/ is written.

phase1u/data/sentences.json    [{sid, slovak, level, topic, tags{...}}]   sid 190001..190100
phase1u/data/annotations.json  {"<sid>": {hygienised{v,lk,...}, voice_sk, agent_nom, tf_gold, ...}}
phase1u/data/items.json        [{id, sid, kind, intent, form, tags[], passive, answer}]
phase1u/data/labels.json       {"<item id>": {judged, type, passive, tip, borderline, confidence,
                                              dropped, packet_part, packet_position, qid}}
"""
import datetime
import json
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))              # phase1u/run
P1U = os.path.dirname(HERE)
DATA = os.path.join(P1U, 'data')
ALT_DATA = os.path.join(P1U, 'set', 'data')
SET = os.path.join(P1U, 'set')
LOG = os.path.join(HERE, 'access_log.jsonl')

TYPES = ('T', 'W', 'M', 'S')
SID_LO, SID_HI = 210001, 210100   # 2F Part 2: fresh Czech sids
LEVELS = ('A1', 'A2', 'B1', 'B2')
KNOWN_TAGS = ('plain', 'determiner', 'aspect', 'number', 'by-passive', 'by-passive-embedded',
              'skp-passive', 'drop-main', 'drop-fronted', 'drop-misaligned', 'drop-other',
              'time-frame', 'missing-article', 'timeframe', 'agentdrop-main', 'agentdrop-embedded')
PASSIVE_TAGS = (None, 'by', 'agentless')
UNKNOWN_TAGS = {}


def data_dir_default():
    """phase1u/data is the agreed dir; phase1u/set/data is the assembler's twin."""
    if os.path.exists(os.path.join(DATA, 'items.json')):
        return DATA
    if os.path.exists(os.path.join(ALT_DATA, 'items.json')):
        return ALT_DATA
    return DATA


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
    _log(side, what, len(obj), purpose, caller or 'loader_1u.py')
    return obj


def _dirs(data_dir):
    d = data_dir or data_dir_default()
    ext = os.path.abspath(d) not in (os.path.abspath(DATA), os.path.abspath(ALT_DATA))
    return d, ('1u:ext:%s' % os.path.basename(os.path.abspath(d)) if ext else '1u:fresh1u'), ext


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
        for k in ('slovak', 'level'):
            if not s.get(k):
                raise SystemExit('REFUSED: sid %d has no %r' % (sid, k))
        if s['level'] not in LEVELS:
            raise SystemExit('REFUSED: sid %d has level %r' % (sid, s['level']))
        s['tags'] = dict(s.get('tags') or {})
        s['tags']['writer_tags'] = dict(s['tags'].get('writer_tags') or {})
    return rows


def load_annotations(purpose, caller=None, data_dir=None):
    d, side, _e = _dirs(data_dir)
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
        if not ext and (not isinstance(tg, list) or not tg):
            raise SystemExit('REFUSED: item %s has no tags list' % i)
        for t in (tg or []):
            if t not in KNOWN_TAGS:                     # recorded, never a refusal (cosmetic only)
                UNKNOWN_TAGS[t] = UNKNOWN_TAGS.get(t, 0) + 1
        if it.get('passive') not in PASSIVE_TAGS:
            it['passive'] = ('agentless' if any(t in (tg or []) for t in
                                                ('drop-main', 'drop-fronted', 'drop-misaligned',
                                                 'drop-other', 'skp-passive', 'agentdrop-main',
                                                 'agentdrop-embedded'))
                             else 'by' if any(t in (tg or []) for t in
                                              ('by-passive', 'by-passive-embedded')) else None)
    return items


def labels_path(data_dir=None):
    d, _s, _e = _dirs(data_dir)
    return os.path.join(d, 'labels.json')


def have_labels(data_dir=None):
    return os.path.exists(labels_path(data_dir))


def load_labels(purpose, caller=None, data_dir=None):
    """THE ONLY label read site.  Read LAST, after every verdict exists."""
    d, side, ext = _dirs(data_dir)
    p = os.path.join(d, 'labels.json')
    lab = _json(p, side.replace('1u:', '1u:labels:'), 'data/labels.json', purpose, caller)
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
        c = r.get('confidence')
        if not (isinstance(c, int) and 1 <= c <= 5):
            bad.append({'item': iid, 'why': 'confidence=%r (S2/S3 top-up needs 1-5)' % c})
    meta = {'labels_path': p, 'items_labelled': len(lab), 'rejected_rows': bad, 'external': ext,
            'judged': _count(r.get('judged') for r in lab.values()),
            'types': _count(r.get('type') for r in lab.values() if r.get('judged') == 'wrong'),
            'confidence': _count(r.get('confidence') for r in lab.values()),
            'borderline': sum(1 for r in lab.values() if r.get('borderline')),
            'unknown_item_tags': dict(UNKNOWN_TAGS)}
    for name in ('join_labels_1u.json', 'LABEL_JOIN_1U.json', 'assemble_1u.json'):
        j = os.path.join(SET, name)
        if not ext and os.path.exists(j):
            try:
                obj = json.load(open(j, encoding='utf-8'))
                _log(side.replace('1u:', '1u:labels:'), 'set/' + name, 1,
                     'judge-noise / duplicate-control statistics of the label join', caller)
                meta.setdefault('label_join', {})[name] = obj.get('duplicates', obj.get('labels'))
            except Exception as e:                                       # pragma: no cover
                meta.setdefault('label_join_error', {})[name] = str(e)
    return lab, meta


def _count(it):
    out = {}
    for x in it:
        out[str(x)] = out.get(str(x), 0) + 1
    return out

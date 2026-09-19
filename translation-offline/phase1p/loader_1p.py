#!/usr/bin/env python3
"""Phase 1P loader — the ONLY door to the new 1P set, to its judge labels, and (read-only) to the
CLOSED earlier sets used by --dev.  Same contract as loader_1n; every read appends one JSON line to
phase1p/access_log.jsonl.  Nothing is ever written into a closed phase directory.

phase1p/data/sentences.json   [{sid, slovak, level, topic, tags{}}]                 sid 170001..170120
phase1p/data/annotations.json {"<sid>": {hygienised{v,lk,...}, voice_sk, agent_nom, tf_gold, ...}}
phase1p/data/items.json       [{id, sid, kind, intent, form, tags[], passive, answer}]
                              tags values: agentless | by-passive | determiner | aspect |
                                           timeframe | number | plain
phase1p/judge/blind_map.json  {"J...": "<item id>"}   judge/_key.json {"J...": {sid, aid}}
phase1p/judge/out_part*.json / out_controls.json + controls_map.json  (1N verdict schema)
"""
import datetime, glob, json, os, sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data')
JUDGE = os.path.join(HERE, 'judge')
LOG = os.path.join(HERE, 'access_log.jsonl')
TYPES = ('T', 'W', 'M', 'S')
SID_LO, SID_HI = 170001, 170120
PASSIVE_TAGS = (None, 'by', 'agentless')
TAGS = ('agentless', 'by-passive', 'determiner', 'aspect', 'timeframe', 'number', 'plain')


def _log(side, what, n, purpose, caller=None):
    rec = {'ts': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
           'side': side, 'what': what,
           'caller': caller or os.path.basename(sys.argv[0] or 'interactive'),
           'n': n, 'purpose': purpose or ''}
    with open(LOG, 'a', encoding='utf-8') as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + '\n')
    return rec


def _json(path, side, what, purpose, caller):
    if not os.path.exists(path):
        raise SystemExit('REFUSED: %s does not exist (the data side has not delivered it yet)' % path)
    obj = json.load(open(path, encoding='utf-8'))
    _log(side, what, len(obj), purpose, caller or 'loader_1p.py')
    return obj


def _dirs(data_dir):
    if not data_dir or os.path.abspath(data_dir) == os.path.abspath(DATA):
        return DATA, '1p:fresh1p', False
    return data_dir, '1p:ext:%s' % os.path.basename(os.path.dirname(os.path.abspath(data_dir))), True


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
            raise SystemExit('REFUSED: sid %d outside the agreed range %d..%d' % (sid, SID_LO, SID_HI))
        for k in ('slovak', 'level', 'topic'):
            if not s.get(k):
                raise SystemExit('REFUSED: sid %d has no %r' % (sid, k))
        if s['level'] not in ('A1', 'A2', 'B1', 'B2'):
            raise SystemExit('REFUSED: sid %d has level %r' % (sid, s['level']))
        s['tags'] = dict(s.get('tags') or {})
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
            # derive it from the tag list (1P schema); the 1N key stays authoritative when present
            it['passive'] = ('agentless' if 'agentless' in (tg or [])
                             else 'by' if 'by-passive' in (tg or []) else None)
    return items


def load_labels(purpose, caller=None, judge_dir=None, types=None):
    jd = judge_dir or JUDGE
    ext = os.path.abspath(jd) != os.path.abspath(JUDGE)
    side = '1p:judge' + (':ext' if ext else '')
    ty = tuple(types or TYPES)

    def rd(name):
        return _json(os.path.join(jd, name), side, 'judge/' + name, purpose, caller)

    blind = rd('blind_map.json')
    parts = sorted(glob.glob(os.path.join(jd, 'out_part*.json')))
    if not parts:
        raise SystemExit('REFUSED: no judge/out_part*.json — the judge has not delivered')
    labels, passive, dupes, bad, rows_n = {}, {}, [], [], 0
    for p in parts:
        rows = rd(os.path.basename(p))
        rows_n += len(rows)
        for r in rows:
            jid = r['jid']
            iid = blind.get(jid)
            if iid is None:
                bad.append({'jid': jid, 'why': 'not in blind_map.json'})
                continue
            judged, typ = r.get('judged'), r.get('type')
            if judged not in ('correct', 'wrong'):
                bad.append({'jid': jid, 'why': 'judged=%r' % judged})
                continue
            if judged == 'correct':
                typ = None
            elif typ not in ty:
                bad.append({'jid': jid, 'why': 'wrong with type=%r' % typ})
                typ = None
            if 'passive' in r and r.get('passive') in PASSIVE_TAGS:
                passive[iid] = r.get('passive')
            if iid in labels:
                dupes.append({'item': iid, 'a': labels[iid], 'b': (judged, typ)})
            labels[iid] = (judged, typ)
    controls = {}
    cpath, cmap_path = os.path.join(jd, 'out_controls.json'), os.path.join(jd, 'controls_map.json')
    if os.path.exists(cpath) and os.path.exists(cmap_path):
        cmap = rd('controls_map.json')
        for r in rd('out_controls.json'):
            iid = cmap.get(r['jid'])
            if iid is None:
                bad.append({'jid': r['jid'], 'why': 'not in controls_map.json'})
                continue
            typ = r.get('type') if r.get('judged') == 'wrong' else None
            controls.setdefault(iid, []).append((r.get('judged'), typ if typ in ty else None))
    meta = {'parts': [os.path.basename(p) for p in parts], 'rows_read': rows_n,
            'items_labelled': len(labels), 'controls': len(controls),
            'judge_dir': jd, 'types_accepted': list(ty), 'passive_tags_read': len(passive),
            'passive_by_item': passive, 'hidden_duplicate_rows': dupes, 'rejected_rows': bad}
    return labels, controls, meta

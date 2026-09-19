#!/usr/bin/env python3
"""Phase 1M loader — the ONLY door to the new 140-sentence set and to its judge labels.

Every read of sentence / item / annotation / label data appends one JSON line to
phase1m/access_log.jsonl in the format loader_1l._log writes
({ts, side, what, caller, n, purpose}).  Nothing outside phase1m is read here.

File formats (fixed by the orchestrator, see the task brief):
  data/sentences.json   list of {sid, slovak, level, topic, tags{nom_agent, agent,
                                 reported_speech, perfective_future, impersonal_or_passive}}
  data/annotations.json dict "<sid>" -> {"hygienised": {...}, "raw": {...}}   (Phase 1k schema)
  data/items.json       list of {id, sid, kind, intent, form, answer}
  judge/blind_map.json  {"J....": "<item id>"}      judge/controls_map.json {"K...": "<item id>"}
  judge/out_part1..6.json, judge/out_controls.json
                        list of {jid, judged: correct|wrong, type: null|T|W|M|S|V|E}
"""
import datetime, glob, json, os, sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data')
JUDGE = os.path.join(HERE, 'judge')
LOG = os.path.join(HERE, 'access_log.jsonl')
TYPES = ('T', 'W', 'M', 'S', 'V', 'E')
SID_LO, SID_HI = 150001, 150140


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
    _log(side, what, len(obj), purpose, caller or 'loader_1m.py')
    return obj


# ------------------------------------------------------------------ the new set
def load_sentences(purpose, caller=None):
    rows = _json(os.path.join(DATA, 'sentences.json'), '1m:fresh1m',
                 'data/sentences.json', purpose, caller)
    if not isinstance(rows, list) or not rows:
        raise SystemExit('REFUSED: data/sentences.json is not a non-empty list')
    seen = set()
    for s in rows:
        sid = int(s['sid'])
        if sid in seen:
            raise SystemExit('REFUSED: duplicate sid %d in sentences.json' % sid)
        seen.add(sid)
        if not (SID_LO <= sid <= SID_HI):
            raise SystemExit('REFUSED: sid %d outside the agreed range %d..%d' % (sid, SID_LO, SID_HI))
        for k in ('slovak', 'level', 'topic'):
            if not s.get(k):
                raise SystemExit('REFUSED: sid %d has no %r' % (sid, k))
        if s['level'] not in ('A1', 'A2', 'B1', 'B2'):
            raise SystemExit('REFUSED: sid %d has level %r' % (sid, s['level']))
        s['tags'] = dict(s.get('tags') or {})
    return rows


def load_annotations(purpose, caller=None):
    ann = _json(os.path.join(DATA, 'annotations.json'), '1m:fresh1m',
                'data/annotations.json', purpose, caller)
    if not isinstance(ann, dict) or not ann:
        raise SystemExit('REFUSED: data/annotations.json is not a non-empty dict')
    for sid, a in ann.items():
        hy = a.get('hygienised', a)
        v = [x for x in (hy.get('v') or []) if isinstance(x, str) and x.strip()]
        if not v:
            raise SystemExit('REFUSED: annotation %s carries no accepted reference in "v"' % sid)
    return ann


def load_items(purpose, caller=None):
    items = _json(os.path.join(DATA, 'items.json'), '1m:fresh1m',
                  'data/items.json', purpose, caller)
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
    return items


# ------------------------------------------------------------------ judge labels
def _map(name, purpose, caller):
    return _json(os.path.join(JUDGE, name), '1m:judge', 'judge/' + name, purpose, caller)


def load_labels(purpose, caller=None):
    """Merge judge/out_part*.json through blind_map.json -> {item_id: (judged, type)}.

    Returns (labels, controls, meta).  `controls` is {item_id: [(judged, type), ...]} from
    out_controls.json through controls_map.json (the judge-noise duplicates).  Read ONCE, after
    every model verdict exists.
    """
    blind = _map('blind_map.json', purpose, caller)
    parts = sorted(glob.glob(os.path.join(JUDGE, 'out_part*.json')))
    if not parts:
        raise SystemExit('REFUSED: no judge/out_part*.json — the judge has not delivered')
    labels, bad, rows_n = {}, [], 0
    for p in parts:
        rows = _json(p, '1m:judge', 'judge/' + os.path.basename(p), purpose, caller)
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
            elif typ not in TYPES:
                bad.append({'jid': jid, 'why': 'wrong with type=%r' % typ})
                typ = None
            if iid in labels and labels[iid] != (judged, typ):
                bad.append({'jid': jid, 'why': 'conflicting duplicate label for %s' % iid})
            labels[iid] = (judged, typ)
    controls = {}
    cpath = os.path.join(JUDGE, 'out_controls.json')
    cmap_path = os.path.join(JUDGE, 'controls_map.json')
    if os.path.exists(cpath) and os.path.exists(cmap_path):
        cmap = _map('controls_map.json', purpose, caller)
        for r in _json(cpath, '1m:judge', 'judge/out_controls.json', purpose, caller):
            iid = cmap.get(r['jid'])
            if iid is None:
                bad.append({'jid': r['jid'], 'why': 'not in controls_map.json'})
                continue
            typ = r.get('type') if r.get('judged') == 'wrong' else None
            controls.setdefault(iid, []).append((r.get('judged'), typ if typ in TYPES else None))
    meta = {'parts': [os.path.basename(p) for p in parts], 'rows_read': rows_n,
            'items_labelled': len(labels), 'controls': len(controls), 'rejected_rows': bad}
    return labels, controls, meta

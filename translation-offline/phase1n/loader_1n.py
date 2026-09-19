#!/usr/bin/env python3
"""Phase 1N loader — the ONLY door to the new set, to its judge labels, and (read-only) to the
CLOSED phase1m data used by --dev / --selftest-final / --probe.

Every read appends one JSON line to phase1n/access_log.jsonl ({ts, side, what, caller, n,
purpose}) — including the reads of phase1m/data and phase1m/judge, which are passed in through
`data_dir` / `judge_dir` so that NOTHING is ever logged into the closed phase1m directory.

File formats (phase1n/data, phase1n/judge)
  data/sentences.json   list of {sid, slovak, level, topic, tags{...}}
  data/annotations.json dict "<sid>" -> {"hygienised": {...}, "raw": {...}}   (Phase 1k schema)
  data/items.json       list of {id, sid, kind, intent, form, passive, answer}
                        passive: null | "by" | "agentless"   (writer tag)
  judge/blind_map.json  {"J....": "<item id>"}      judge/controls_map.json {"K...": "<item id>"}
  judge/out_part1..9.json, judge/out_controls.json
                        list of {jid, judged: correct|wrong, type: null|T|W|M|S, passive: ...}
Judge types are T / W / M / S only — V is retired; a row that still carries V (or E) lands in
meta['rejected_rows'] instead of being kept silently.
"""
import datetime, glob, json, os, sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data')
JUDGE = os.path.join(HERE, 'judge')
LOG = os.path.join(HERE, 'access_log.jsonl')
TYPES = ('T', 'W', 'M', 'S')
SID_LO, SID_HI = 160001, 160100
PASSIVE_TAGS = (None, 'by', 'agentless')


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
    _log(side, what, len(obj), purpose, caller or 'loader_1n.py')
    return obj


def _dirs(data_dir):
    """(directory, side tag, external?) — external = a closed earlier-phase directory."""
    if not data_dir or os.path.abspath(data_dir) == os.path.abspath(DATA):
        return DATA, '1n:fresh1n', False
    return data_dir, '1n:ext:%s' % os.path.basename(os.path.dirname(os.path.abspath(data_dir))), True


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
            raise SystemExit('REFUSED: sid %d outside the agreed range %d..%d' % (sid, SID_LO, SID_HI))
        for k in ('slovak', 'level', 'topic'):
            if not s.get(k):
                raise SystemExit('REFUSED: sid %d has no %r' % (sid, k))
        if s['level'] not in ('A1', 'A2', 'B1', 'B2'):
            raise SystemExit('REFUSED: sid %d has level %r' % (sid, s['level']))
        s['tags'] = dict(s.get('tags') or {})
    return rows


def load_annotations(purpose, caller=None, data_dir=None):
    d, side, ext = _dirs(data_dir)
    ann = _json(os.path.join(d, 'annotations.json'), side, 'data/annotations.json', purpose, caller)
    if not isinstance(ann, dict) or not ann:
        raise SystemExit('REFUSED: data/annotations.json is not a non-empty dict')
    for sid, a in ann.items():
        hy = a.get('hygienised', a)
        v = [x for x in (hy.get('v') or []) if isinstance(x, str) and x.strip()]
        if not v:
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
        if not ext and it.get('passive') not in PASSIVE_TAGS:
            raise SystemExit('REFUSED: item %s has passive=%r (null | by | agentless)'
                             % (i, it.get('passive')))
    return items


# ------------------------------------------------------------------ judge labels
def load_labels(purpose, caller=None, judge_dir=None, types=None):
    """Merge judge/out_part*.json through blind_map.json -> {item_id: (judged, type)}.

    Returns (labels, controls, meta). `controls` is {item_id: [(judged, type), ...]} from
    out_controls.json through controls_map.json (the judge-noise duplicates).  The judge's own
    `passive` key is carried in meta['passive_by_item'].  Read ONCE, after every model verdict
    exists.  `types` / `judge_dir` exist so the CLOSED 1M labels can be re-scored offline.
    """
    jd = judge_dir or JUDGE
    ext = os.path.abspath(jd) != os.path.abspath(JUDGE)
    side = '1n:judge' + (':ext' if ext else '')
    ty = tuple(types or TYPES)

    def rd(name):
        return _json(os.path.join(jd, name), side, 'judge/' + name, purpose, caller)

    blind = rd('blind_map.json')
    parts = sorted(glob.glob(os.path.join(jd, 'out_part*.json')))
    if not parts:
        raise SystemExit('REFUSED: no judge/out_part*.json — the judge has not delivered')
    labels, passive, bad, rows_n = {}, {}, [], 0
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
            if 'passive' in r:
                pv = r.get('passive')
                if pv not in PASSIVE_TAGS:
                    bad.append({'jid': jid, 'why': 'passive=%r' % pv})
                else:
                    passive[iid] = pv
            if iid in labels and labels[iid] != (judged, typ):
                bad.append({'jid': jid, 'why': 'conflicting duplicate label for %s' % iid})
            labels[iid] = (judged, typ)
    controls = {}
    cpath = os.path.join(jd, 'out_controls.json')
    cmap_path = os.path.join(jd, 'controls_map.json')
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
            'judge_dir': ('phase1m/judge (CLOSED, re-scored)' if ext else 'phase1n/judge'),
            'types_accepted': list(ty), 'passive_tags_read': len(passive),
            'passive_by_item': passive, 'rejected_rows': bad}
    return labels, controls, meta

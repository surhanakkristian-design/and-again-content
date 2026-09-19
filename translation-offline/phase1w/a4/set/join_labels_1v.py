#!/usr/bin/env python3
"""Phase 1V label join — 0 model calls.

    python3 phase1v/trackA_set/join_labels_1v.py

Reads set/judge/verdicts_part*.json + set/packet_key_1v.json + data/items.json,
refuses loudly unless ALL key entries (900 real + 80 duplicate controls) are present and
well formed, and writes data/labels.json (mirrored to phase1v/data/) in the schema the
frozen runner/scorer reads:

    {"<item id>": {"judged": "correct"|"wrong", "type": null|"T"|"W"|"M"|"S",
                   "passive": ..., "agent_drop": ..., "tip": bool, "borderline": bool,
                   "confidence": 1-5, "dropped": "...", "packet_part": K,
                   "packet_position": n, "qid": "Q0001"}}

Judge noise on the 80 hidden duplicates (label and type disagreement) goes into
set/join_labels_1v.json.
"""
import argparse, collections, glob, json, os, sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
PHASE = os.path.dirname(HERE)
TOFF = os.path.dirname(PHASE)
sys.path.insert(0, os.path.join(TOFF, 'phase1s'))
try:
    from safe_json import safe_dump                            # noqa: E402
except Exception:                                              # pragma: no cover
    def safe_dump(obj, path):
        tmp = path + '.tmp'
        with open(tmp, 'w', encoding='utf-8') as fh:
            json.dump(obj, fh, ensure_ascii=False, indent=1)
        os.replace(tmp, path)

LABELS = ('correct', 'wrong')
TYPES = ('T', 'W', 'M', 'S')


def join(data_dir=None, judge_dir=None, key_path=None, out_dirs=None, force=False):
    data_dir = data_dir or os.path.join(HERE, 'data')
    judge_dir = judge_dir or os.path.join(HERE, 'judge')
    key_path = key_path or os.path.join(HERE, 'packet_key_1v.json')
    out_dirs = out_dirs or [data_dir, os.path.join(HERE, 'data')]
    key = json.load(open(key_path, encoding='utf-8'))
    items = json.load(open(os.path.join(data_dir, 'items.json'), encoding='utf-8'))
    ids = {i['id'] for i in items}

    rows, files, errs = {}, [], []
    for p in sorted(glob.glob(os.path.join(judge_dir, 'verdicts_part*.json'))):
        files.append(p)
        try:
            obj = json.load(open(p, encoding='utf-8'))
        except Exception as e:
            errs.append({'file': os.path.basename(p), 'qid': '-', 'why': 'bad JSON: %s'
                         % str(e)[:120]})
            continue
        if isinstance(obj, dict):
            obj = obj.get('verdicts') or list(obj.values())
        if not isinstance(obj, list):
            errs.append({'file': os.path.basename(p), 'qid': '-', 'why': 'not a JSON list'})
            continue
        for r in obj:
            if not isinstance(r, dict) or not r.get('id'):
                errs.append({'file': os.path.basename(p), 'qid': '-', 'why': 'no id'})
                continue
            if r['id'] in rows:
                errs.append({'file': os.path.basename(p), 'qid': r['id'],
                             'why': 'verdict given twice'})
            rows[r['id']] = r

    def check(qid, r):
        bad = []
        if r.get('label') not in LABELS:
            bad.append('label %r' % r.get('label'))
        c = r.get('confidence')
        if isinstance(c, bool) or not isinstance(c, int) or not 1 <= c <= 5:
            bad.append('confidence %r' % c)
        if r.get('label') == 'wrong' and r.get('type') not in TYPES:
            bad.append('type %r on a wrong answer' % r.get('type'))
        if r.get('label') == 'correct' and r.get('type') not in (None, '', 'null'):
            bad.append('type %r on a correct answer' % r.get('type'))
        if not isinstance(r.get('borderline'), bool):
            bad.append('borderline %r' % r.get('borderline'))
        return bad

    missing, malformed = [], []
    for qid in sorted(key):
        r = rows.get(qid)
        if r is None:
            missing.append(qid)
            continue
        b = check(qid, r)
        if b:
            malformed.append({'qid': qid, 'why': '; '.join(b)})
    extra = sorted(set(rows) - set(key))

    labels, dup_pairs = {}, []
    for qid, k in sorted(key.items()):
        iid = k.get('item')
        r = rows.get(qid)
        if r is None or iid not in ids:
            continue
        if k.get('duplicate_of'):
            dup_pairs.append((k['duplicate_of'], qid, iid))
            continue
        labels[iid] = {
            'judged': r.get('label'),
            'type': r.get('type') if r.get('label') == 'wrong' else None,
            'passive': r.get('passive'), 'agent_drop': r.get('agent_drop'),
            'tip': bool(r.get('tip')), 'borderline': bool(r.get('borderline')),
            'confidence': r.get('confidence'), 'dropped': r.get('dropped') or '',
            'packet_part': k.get('part'), 'packet_position': k.get('position'), 'qid': qid}

    dis, type_dis, judged_dups = 0, 0, 0
    dis_rows = []
    for orig, dup, iid in dup_pairs:
        a, b = rows.get(orig), rows.get(dup)
        if not a or not b:
            continue
        judged_dups += 1
        if a.get('label') != b.get('label'):
            dis += 1
            dis_rows.append({'item': iid, 'a': a.get('label'), 'b': b.get('label')})
        elif a.get('label') == 'wrong' and a.get('type') != b.get('type'):
            type_dis += 1
            dis_rows.append({'item': iid, 'a': 'wrong/%s' % a.get('type'),
                             'b': 'wrong/%s' % b.get('type')})

    rep = {'key_entries': len(key), 'verdict_files': len(files),
           'verdict_rows': len(rows), 'items_labelled': len(labels),
           'unlabelled_items': len(ids) - len(labels),
           'missing_verdicts': missing, 'malformed_verdicts': malformed,
           'unknown_ids': extra, 'file_errors': errs,
           'duplicate_controls': len(dup_pairs), 'duplicate_controls_judged': judged_dups,
           'label_disagreements': dis,
           'judge_noise_pct': round(100.0 * dis / judged_dups, 2) if judged_dups else None,
           'type_only_disagreements': type_dis, 'disagreement_rows': dis_rows,
           'judged': dict(collections.Counter(v['judged'] for v in labels.values())),
           'types': dict(collections.Counter(v['type'] for v in labels.values()
                                             if v['judged'] == 'wrong')),
           'confidence': dict(collections.Counter(v['confidence']
                                                  for v in labels.values())),
           'borderline': sum(1 for v in labels.values() if v['borderline']),
           'written': False}
    fatal = bool(missing or malformed or errs or len(labels) != len(ids))
    if fatal and not force:
        rep['REFUSED'] = True
        safe_dump(rep, os.path.join(HERE, 'join_labels_1v.json'))
        print(json.dumps({k: rep[k] for k in
                          ('key_entries', 'verdict_rows', 'items_labelled',
                           'unlabelled_items', 'unknown_ids', 'file_errors')},
                         indent=1, sort_keys=True))
        print('MISSING VERDICTS (%d): %s' % (len(missing), ', '.join(missing[:40])))
        for m in malformed[:40]:
            print('MALFORMED %s: %s' % (m['qid'], m['why']))
        print('REFUSED: %d missing, %d malformed, %d file errors, %d items unlabelled'
              % (len(missing), len(malformed), len(errs), len(ids) - len(labels)))
        return 2
    for d in out_dirs:
        os.makedirs(d, exist_ok=True)
        safe_dump(labels, os.path.join(d, 'labels.json'))
    rep['written'] = True
    rep['out_dirs'] = out_dirs
    safe_dump(rep, os.path.join(HERE, 'join_labels_1v.json'))
    slim = {k: v for k, v in rep.items()
            if k not in ('missing_verdicts', 'malformed_verdicts', 'disagreement_rows')}
    print(json.dumps(slim, indent=1, sort_keys=True))
    return 0


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--data-dir')
    ap.add_argument('--judge-dir')
    ap.add_argument('--key')
    ap.add_argument('--force', action='store_true')
    a = ap.parse_args()
    raise SystemExit(join(a.data_dir, a.judge_dir, a.key, None, a.force))

"""Task B — backfill the `s` synonym-group ids into annotations from the EXISTING tables on disk.

Zero model tokens, zero new words: an alt pair (key, member) is mapped to a group only when BOTH sit in
that group already (phase1c/synonyms/table.json, ng_phase1c.json, review_added.json).  Phase 1h defect D4:
the 60 fresh annotations were written without `s`, so every alternative sits in `alt` only.

Use (identical on dev and holdout, nothing is printed but counts):

    import backfill_s_ids as B
    report = B.apply_to_checker(checker_module)                    # mutates checker_module._ANN in place
    new_ann, report = B.backfill_annotations(annotations, checker_module)   # pure, returns a copy
    python3 backfill_s_ids.py dev                                  # writes taskB/backfill_<side>.json

`annotations` is the loader's dict {"<sid>": {"hygienised": {...}, "raw": {...}}} or a plain
{"<sid>": <annotation>}; items from load_items() are not needed (the `s` ids are per sentence).
"""
import os
import sys
import json
import copy

HERE = os.path.dirname(os.path.abspath(__file__))
P1I = os.path.dirname(HERE)


def _groups(C):
    out = []
    for fn in getattr(C, 'SYN_FILES', ('table.json', 'ng_phase1c.json', 'review_added.json')):
        p = os.path.join(C.base.P1C, 'synonyms', fn)
        if os.path.exists(p):
            for g in (json.load(open(p)).get('groups') or []):
                m = [C.base.norm(x).strip() for x in (g.get('m') or [])]
                m = [x for x in m if x]
                if len(m) > 1 and g.get('id'):
                    out.append((str(g['id']), m))
    return out


def backfill_annotation(a, groups, norm):
    """-> (new annotation, rows). One sentence annotation; `s` entries already present are never changed."""
    a = copy.deepcopy(a or {})
    s = dict(a.get('s') or {})
    rows = []
    for k, vs in (a.get('alt') or {}).items():
        kn = norm(k)
        if k in s or kn in {norm(x) for x in s}:
            rows.append({'key': k, 'status': 'kept', 'gid': s.get(k)})
            continue
        want = {norm(v) for v in (vs or [])}
        best = None
        for gid, m in groups:
            if kn not in m:
                continue
            ov = len(want & set(m))
            if not ov:
                continue
            score = (ov, -len(m))
            if best is None or score > best[0]:
                best = (score, gid)
        if best:
            s[k] = best[1]
            rows.append({'key': k, 'status': 'added', 'gid': best[1]})
        else:
            rows.append({'key': k, 'status': 'no_group', 'gid': None})
    if s:
        a['s'] = s
    return a, rows


def backfill_annotations(annotations, C):
    groups = _groups(C)
    norm = lambda x: C.base.norm(x).strip()          # noqa: E731
    out, rep = {}, {'sentences': 0, 'added': 0, 'kept': 0, 'no_group': 0, 'per_sid': {}}
    for sid, v in annotations.items():
        a = v.get('hygienised') if isinstance(v, dict) and 'hygienised' in v else v
        na, rows = backfill_annotation(a, groups, norm)
        out[sid] = na
        rep['sentences'] += 1
        for r in rows:
            rep[r['status']] += 1
        rep['per_sid'][str(sid)] = rows
    return out, rep


def apply_to_checker(C, annotations=None):
    """Backfill the annotations the checker already holds in _ANN (or the given ones) IN PLACE."""
    src = annotations
    if src is None:
        src = {str(k): v for k, v in C._ANN.items()}
    new, rep = backfill_annotations(src, C)
    for sid, a in new.items():
        C._ANN[int(sid)] = a
    return rep


def main(side):
    sys.path.insert(0, P1I)
    import checker_1i as C
    from loader import load_annotations
    ann = load_annotations(side)
    new, rep = backfill_annotations(ann, C)
    json.dump(new, open(os.path.join(HERE, 'backfill_%s.json' % side), 'w'), ensure_ascii=False)
    rep_small = {k: v for k, v in rep.items() if k != 'per_sid'}
    json.dump(rep, open(os.path.join(HERE, 'backfill_%s_report.json' % side), 'w'), ensure_ascii=False)
    print(json.dumps(rep_small))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'dev')

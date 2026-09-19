#!/usr/bin/env python3
"""Phase 1U floor check on JUDGED counts (SPLIT_1U.md) — 0 model calls.

    python3 phase1u/set/floors_1u.py

Reads data/items.json (writer tags) + data/labels.json (judge labels) and writes
set/floors_1u.json — copied byte-identically to set/FLOOR_CHECK_1U.json, the name
SPLIT_1U.md uses — with EXACTLY these keys:

  F1_agent_drops_wrong  F1a_fronted_wrong  F1b_misaligned_wrong  F2_time_frame_wrong
  F3_by_passive_correct F4_skp_correct     F5_missing_article_wrong
      each {"n": int, "min": int, "pass": bool}
  missing_article_judged_correct   T_W_M_S_wrong   judged_correct   judged_wrong   all_pass

Exit 0 when all seven floors hold, 2 otherwise.  The run does not start on exit 2.
"""
import argparse, collections, json, os, shutil, sys

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

DROP_TAGS = ('drop-fronted', 'drop-misaligned', 'drop-main', 'drop-other')
MINS = {'F1_agent_drops_wrong': 120, 'F1a_fronted_wrong': 40, 'F1b_misaligned_wrong': 30,
        'F2_time_frame_wrong': 100, 'F3_by_passive_correct': 60, 'F4_skp_correct': 40,
        'F5_missing_article_wrong': 40}


def check(data_dir=None, out_dir=None):
    data_dir = data_dir or os.path.join(HERE, 'data')
    out_dir = out_dir or HERE
    items = json.load(open(os.path.join(data_dir, 'items.json'), encoding='utf-8'))
    labels = json.load(open(os.path.join(data_dir, 'labels.json'), encoding='utf-8'))

    def tag(i, t):
        return t in (i.get('tags') or [])

    def lab(i):
        return (labels.get(i['id']) or {}).get('judged')

    def n(pred):
        return sum(1 for i in items if pred(i))

    cnt = {
        'F1_agent_drops_wrong': n(lambda i: any(tag(i, t) for t in DROP_TAGS)
                                  and lab(i) == 'wrong'),
        'F1a_fronted_wrong': n(lambda i: tag(i, 'drop-fronted') and lab(i) == 'wrong'),
        'F1b_misaligned_wrong': n(lambda i: tag(i, 'drop-misaligned') and lab(i) == 'wrong'),
        'F2_time_frame_wrong': n(lambda i: tag(i, 'time-frame') and lab(i) == 'wrong'),
        'F3_by_passive_correct': n(lambda i: tag(i, 'by-passive') and lab(i) == 'correct'),
        'F4_skp_correct': n(lambda i: tag(i, 'skp-passive') and lab(i) == 'correct'),
        'F5_missing_article_wrong': n(lambda i: tag(i, 'missing-article')
                                      and lab(i) == 'wrong')}
    out = collections.OrderedDict()
    all_pass = True
    for k in ('F1_agent_drops_wrong', 'F1a_fronted_wrong', 'F1b_misaligned_wrong',
              'F2_time_frame_wrong', 'F3_by_passive_correct', 'F4_skp_correct',
              'F5_missing_article_wrong'):
        ok = cnt[k] >= MINS[k]
        all_pass = all_pass and ok
        out[k] = {'n': cnt[k], 'min': MINS[k], 'pass': ok}
    types = collections.Counter((labels.get(i['id']) or {}).get('type') for i in items
                                if lab(i) == 'wrong')
    out['missing_article_judged_correct'] = n(lambda i: tag(i, 'missing-article')
                                              and lab(i) == 'correct')
    out['T_W_M_S_wrong'] = {t: int(types.get(t, 0)) for t in ('T', 'W', 'M', 'S')}
    out['judged_correct'] = n(lambda i: lab(i) == 'correct')
    out['judged_wrong'] = n(lambda i: lab(i) == 'wrong')
    out['all_pass'] = all_pass
    out['items'] = len(items)
    out['items_labelled'] = sum(1 for i in items if lab(i) in ('correct', 'wrong'))
    out['drop_cells'] = {t: {'wrong': n(lambda i, t=t: tag(i, t) and lab(i) == 'wrong'),
                             'correct': n(lambda i, t=t: tag(i, t) and lab(i) == 'correct')}
                         for t in DROP_TAGS}
    p = os.path.join(out_dir, 'floors_1u.json')
    safe_dump(out, p)
    shutil.copyfile(p, os.path.join(out_dir, 'FLOOR_CHECK_1U.json'))
    print(json.dumps(out, indent=1))
    if not all_pass:
        print('FLOORS NOT MET: ' + ', '.join('%s %d < %d' % (k, out[k]['n'], out[k]['min'])
                                             for k in MINS if not out[k]['pass']))
    return 0 if all_pass else 2


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--data-dir')
    ap.add_argument('--out-dir')
    a = ap.parse_args()
    raise SystemExit(check(a.data_dir, a.out_dir))

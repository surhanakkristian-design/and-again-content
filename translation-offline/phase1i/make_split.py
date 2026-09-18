#!/usr/bin/env python3
"""Phase 1i — deterministic DEV/HOLDOUT split of the Phase 1h fresh set + DEV/HOLDOUT working data.

ZERO model calls. Reads only phase1h/ (read-only) and writes only into phase1i/.

Split rule:  side = int(sha256(item_id.encode('utf-8')).hexdigest(), 16) % 2   ->  0 = DEV, 1 = HOLDOUT
"Item" = one written+judged answer of the fresh set (correct and wrong alike), id `C:<sid>:<n>` /
`W:<sid>:<n>` as produced by checker_1h._iid (md5 of the English answer).

The Phase 1h per-item verdicts are NOT stored in results_1h_*.json (only aggregates), so they are
recomputed here offline: the frozen checker's decide() over the frozen row-7/row-8 flag sets with the
model verdicts taken from the frozen ledger phase1h/calls.jsonl. No call is made; if a verdict is
missing the item is 'failed' exactly as the frozen rule demands.

usage: python3 phase1i/make_split.py
"""
import hashlib
import json
import os
import stat
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
TO = os.path.dirname(HERE)
P1H = os.path.join(TO, 'phase1h')
sys.path.insert(0, P1H)

# fresh_io_fix patches only the BYTES checker_1h reads (D1/D2 of the 1h report). It monkeypatches
# C.jl / C._jl_glob at import time and writes nothing.
import fresh_io_fix as _F          # noqa: E402
import checker_1h as C             # noqa: E402  (import-safe: main_1h() only under __main__)

assert _F.C is C

ROW7_FLAGS = {'F1': 1, 'F2': 1, 'F3': 1, 'F4v2': 1, 'F5': 1, 'F2B': 1}      # row 7 = P-B  (headline)
ROW8_FLAGS = dict(ROW7_FLAGS)                                              # row 8 = P-C

DEV = os.path.join(HERE, 'dev')
HOLD = os.path.join(HERE, 'holdout')
SPLIT = os.path.join(HERE, 'split')
TASKA = os.path.join(HERE, 'taskA')


def side_of(item_id):
    return int(hashlib.sha256(item_id.encode('utf-8')).hexdigest(), 16) % 2


def unlock(d):
    """Re-open a previously chmod a-w output directory so this script stays re-runnable."""
    for root, dirs, files in os.walk(d):
        for n in dirs:
            p = os.path.join(root, n)
            os.chmod(p, os.stat(p).st_mode | stat.S_IWUSR)
        for n in files:
            p = os.path.join(root, n)
            os.chmod(p, os.stat(p).st_mode | stat.S_IWUSR)


for d in (DEV, HOLD, SPLIT, TASKA):
    os.makedirs(d, exist_ok=True)
    unlock(d)

# ---------------------------------------------------------------- load the fresh set, frozen semantics
oc, ow = C.load_items_1h()            # fills SK_OF for the 80 old sids and clears the annotation cache
fc, fw = C.load_fresh()               # the 980 fresh answers over all 140 sentences (patched loader)
bud = C.Bud1h()
vm = {'row7': C.verdict_map_own('P-B', bud), 'row8': C.verdict_map_own('P-C', bud)}
raw_rec = {}
for k, v in bud.own.items():
    if k[0] == C.MODEL:
        raw_rec[(k[1], k[2])] = v
failed = set()
for r in C.jl(os.path.join(P1H, 'calls.jsonl')):
    if r.get('counted') and r.get('verdict') not in ('SAME', 'TIP', 'DIFF'):
        failed.add((r.get('variant'), r.get('item_id')))

judged = C.judgements_fresh()
new_sids = {int(r['sid']) for r in C.jl(os.path.join(P1H, 'fresh', 'new_sentences_60.jsonl'))
            if 'source' in r or 'topic' in r}
# the patched loader merges 140 rows into new_sentences_60.jsonl; read the true 60 with the ORIGINAL reader
new_sids = {int(r['sid']) for r in _F._orig_jl(os.path.join(P1H, 'fresh', 'new_sentences_60.jsonl'))}

VARIANT = {'row7': 'P-B', 'row8': 'P-C'}
items, rows_out = [], []
ann = {}
for it in fc + fw:
    iid = it['item_id']
    sid = int(it['exercise_id'])
    rec = {'item_id': iid, 'side': 'dev' if side_of(iid) == 0 else 'holdout', 'kind': it['kind'],
           'sid': sid, 'n': it.get('n'), 'level': it.get('level'), 'topic': it.get('topic'),
           'sk': it.get('sk'), 'band': C.band(it.get('sk') or ''), 'reference': it.get('reference'),
           'refs': C.refs_of(it), 'answer': it['answer'], 'judged': judged.get(iid),
           'wrong_type': it.get('wrong_type'), 'half': 'NEW' if sid in new_sids else 'OLD',
           'chk': {'verdict': it['verdict'], 'step': it['step'], 'feedback': it.get('feedback')},
           'chk_missing': it.get('chk_missing'), 'locks': it.get('locks'), 'lock_ok': it.get('lock_ok'),
           'lock_released_2_1': it.get('lock_released_2_1'), 'rows': {}}
    srow = {k: rec[k] for k in ('item_id', 'side', 'kind', 'sid', 'judged', 'wrong_type', 'half',
                                'level', 'band')}
    for row, flags in (('row7', ROW7_FLAGS), ('row8', ROW8_FLAGS)):
        d = C.decide(it, flags, vm[row])
        var = VARIANT[row]
        mrec = raw_rec.get((var, iid))
        r = {'layer': d['layer'], 'accepted': bool(d['accepted']), 'verdict': d['verdict'],
             'tip': d.get('tip'), 'why': d.get('why'),
             'model': (mrec or {}).get('verdict'), 'reply': (mrec or {}).get('reply'),
             'call_made': mrec is not None or (var, iid) in failed,
             'failed_call': (var, iid) in failed and mrec is None}
        rec['rows'][row] = r
        srow[row] = {k: r[k] for k in ('layer', 'accepted', 'verdict', 'tip', 'model', 'failed_call')}
    items.append(rec)
    rows_out.append(srow)
    if sid not in ann:
        ann[sid] = {'hygienised': C.annot(sid), 'raw': C.raw_annot(sid)}

# ---------------------------------------------------------------- sanity: reproduce the 1h headline
def head(row):
    cov = [r for r in rows_out if r['kind'] == 'C' and r['judged'] == 'correct']
    fa = [r for r in rows_out if r['kind'] == 'W' and r['judged'] == 'wrong']
    return (sum(1 for r in cov if r[row]['accepted']), len(cov),
            sum(1 for r in fa if r[row]['accepted']), len(fa))

k7, n7, f7, m7 = head('row7')
print('reproduction check row7: coverage %d/%d (expect 345/420), real FA %d/%d (expect 66/550)'
      % (k7, n7, f7, m7))
assert (k7, n7, f7, m7) == (345, 420, 66, 550), 'row 7 join does not reproduce Phase 1h'
print('reproduction check row8: coverage %d/%d, real FA %d/%d' % head('row8'))

# ---------------------------------------------------------------- write the split
dev_ids = sorted(r['item_id'] for r in rows_out if r['side'] == 'dev')
hold_ids = sorted(r['item_id'] for r in rows_out if r['side'] == 'holdout')
json.dump(dev_ids, open(os.path.join(SPLIT, 'dev_ids.json'), 'w'), indent=0)
json.dump(hold_ids, open(os.path.join(SPLIT, 'holdout_ids.json'), 'w'), indent=0)


def counts(side):
    rs = [r for r in rows_out if r['side'] == side]
    c = [r for r in rs if r['kind'] == 'C']
    w = [r for r in rs if r['kind'] == 'W']
    return {'items': len(rs), 'correct_written': len(c), 'wrong_written': len(w),
            'correct_judged_correct': sum(1 for r in c if r['judged'] == 'correct'),
            'correct_judged_wrong': sum(1 for r in c if r['judged'] == 'wrong'),
            'wrong_judged_wrong': sum(1 for r in w if r['judged'] == 'wrong'),
            'wrong_judged_correct': sum(1 for r in w if r['judged'] == 'correct'),
            'unjudged': sum(1 for r in rs if r['judged'] is None),
            'by_wrong_type': dict(Counter(r['wrong_type'] for r in w)),
            'by_wrong_type_judged_wrong': dict(Counter(r['wrong_type'] for r in w
                                                       if r['judged'] == 'wrong')),
            'by_half': dict(Counter(r['half'] for r in rs)),
            'by_half_correct': dict(Counter(r['half'] for r in c)),
            'by_half_wrong': dict(Counter(r['half'] for r in w)),
            'sids': len({r['sid'] for r in rs})}


cnt = {'dev': counts('dev'), 'holdout': counts('holdout')}
sid_sides = defaultdict(set)
for r in rows_out:
    sid_sides[r['sid']].add(r['side'])
both = sorted(s for s, v in sid_sides.items() if len(v) == 2)
cnt['sids_total'] = len(sid_sides)
cnt['sids_on_both_sides'] = len(both)
cnt['sids_dev_only'] = sum(1 for v in sid_sides.values() if v == {'dev'})
cnt['sids_holdout_only'] = sum(1 for v in sid_sides.values() if v == {'holdout'})
json.dump(cnt, open(os.path.join(SPLIT, 'split_counts.json'), 'w'), indent=1)

L = ['# Phase 1i — DEV / HOLDOUT split of the Phase 1h fresh set\n',
     'Produced by `phase1i/make_split.py` (zero model calls). Source: the Phase 1h fresh set as read by',
     'the frozen loader through `phase1h/fresh_io_fix.py` — 420 correct + 560 wrong written answers over',
     '140 sentences (80 OLD in-sample sentences + 60 NEW), judgements from `phase1h/fresh/judgements.jsonl`.\n',
     '## Rule\n',
     '```\nside = int(sha256(item_id.encode("utf-8")).hexdigest(), 16) % 2      # 0 = DEV, 1 = HOLDOUT\n```\n',
     'Deterministic, id-only, no randomness, no stratification. `item_id` is the frozen Phase 1h id',
     '`C|W:<sid>:<int(md5(answer)[:8],16)>` (`checker_1h._iid`).\n',
     '## Counts\n',
     '| figure | DEV | HOLDOUT | total |', '|---|---|---|---|']
for k, lab in (('items', 'items'), ('correct_written', 'correct answers written'),
               ('wrong_written', 'wrong answers written'),
               ('correct_judged_correct', 'correct, judged really correct (coverage denominator)'),
               ('wrong_judged_wrong', 'wrong, judged really wrong (FA denominator)'),
               ('wrong_judged_correct', 'wrong, judged really CORRECT (excluded from FA)'),
               ('unjudged', 'unjudged')):
    L.append('| %s | %d | %d | %d |' % (lab, cnt['dev'][k], cnt['holdout'][k],
                                        cnt['dev'][k] + cnt['holdout'][k]))
L += ['', '### Wrong answers by type (written / judged really wrong)\n',
      '| type | DEV | HOLDOUT |', '|---|---|---|']
for t in ('T', 'W', 'M', 'S'):
    L.append('| %s | %d / %d | %d / %d |'
             % (t, cnt['dev']['by_wrong_type'].get(t, 0), cnt['dev']['by_wrong_type_judged_wrong'].get(t, 0),
                cnt['holdout']['by_wrong_type'].get(t, 0),
                cnt['holdout']['by_wrong_type_judged_wrong'].get(t, 0)))
L += ['', '### Old (the 80 in-sample sentences) vs new (the 60 fresh sentences)\n',
      '| half | DEV items (C / W) | HOLDOUT items (C / W) |', '|---|---|---|']
for h in ('OLD', 'NEW'):
    L.append('| %s | %d (%d / %d) | %d (%d / %d) |'
             % (h, cnt['dev']['by_half'].get(h, 0), cnt['dev']['by_half_correct'].get(h, 0),
                cnt['dev']['by_half_wrong'].get(h, 0), cnt['holdout']['by_half'].get(h, 0),
                cnt['holdout']['by_half_correct'].get(h, 0), cnt['holdout']['by_half_wrong'].get(h, 0)))
L += ['', '## Leakage caveat — RECORDED, NOT FIXED\n',
      'The split is per ANSWER, not per sentence. **%d of the %d Slovak sentences (sid) have items on '
      'both sides** (%d DEV-only, %d HOLDOUT-only).' % (cnt['sids_on_both_sides'], cnt['sids_total'],
                                                        cnt['sids_dev_only'], cnt['sids_holdout_only']),
      'Anything learned on DEV about a particular Slovak sentence, its reference wording or its annotation',
      'therefore transfers to HOLDOUT items of the same sentence. A per-sid split was not used because it',
      'would have made the per-type cells (T/W/M/S) too small to measure; the consequence is that the',
      'HOLDOUT number is an optimistic bound whenever a change is sentence-specific. Any change that is',
      'per-sentence (a hand edit of an annotation, a reference rewrite, a word list keyed to a sid) is',
      'therefore NOT measurable on this holdout and must be declared as such.\n',
      'sids on both sides: ' + ', '.join(str(s) for s in both) + '\n',
      '## Files\n',
      '- `split/dev_ids.json`, `split/holdout_ids.json` — sorted id lists',
      '- `split/split_counts.json` — every count above as JSON',
      '- `dev/items.jsonl`, `holdout/items.jsonl` — one line per item (schema in `phase1i/CONTEXT.md`)',
      '- `dev/annotations.json`, `holdout/annotations.json` — sid -> {hygienised, raw} annotation',
      '- `dev/l2_false_rejections.json`, `dev/false_acceptances.json` — row-7 error lists on DEV',
      '- `taskA/scoring_rows.jsonl` — verdict-only rows for both sides (no Slovak, no answers)\n']
open(os.path.join(SPLIT, 'SPLIT.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')

# ---------------------------------------------------------------- materialise dev/ and holdout/
for side, d in (('dev', DEV), ('holdout', HOLD)):
    sub = [r for r in items if r['side'] == side]
    with open(os.path.join(d, 'items.jsonl'), 'w', encoding='utf-8') as fh:
        for r in sorted(sub, key=lambda x: x['item_id']):
            fh.write(json.dumps(r, ensure_ascii=False) + '\n')
    sids = sorted({r['sid'] for r in sub})
    json.dump({str(s): ann[s] for s in sids}, open(os.path.join(d, 'annotations.json'), 'w'),
              ensure_ascii=False, indent=1)
    l2fr = sorted(r['item_id'] for r in sub if r['kind'] == 'C' and r['judged'] == 'correct'
                  and not r['rows']['row7']['accepted'] and r['rows']['row7']['layer'] == 'L2')
    fa = sorted(r['item_id'] for r in sub if r['kind'] == 'W' and r['judged'] == 'wrong'
                and r['rows']['row7']['accepted'])
    json.dump(l2fr, open(os.path.join(d, 'l2_false_rejections.json'), 'w'), indent=0)
    json.dump(fa, open(os.path.join(d, 'false_acceptances.json'), 'w'), indent=0)
    if side == 'dev':
        print('DEV: %d items, %d L2 false rejections (row 7), %d real false acceptances (row 7)'
              % (len(sub), len(l2fr), len(fa)))
    else:
        print('HOLDOUT: %d items written, derived lists written WITHOUT inspection' % len(sub))

with open(os.path.join(TASKA, 'scoring_rows.jsonl'), 'w', encoding='utf-8') as fh:
    for r in sorted(rows_out, key=lambda x: x['item_id']):
        fh.write(json.dumps(r, ensure_ascii=False) + '\n')

# ---------------------------------------------------------------- the guarded loader
LOADER = r'''#!/usr/bin/env python3
"""Phase 1i — the ONLY sanctioned way to read the split data. Every load is logged.

    from loader import load_items
    items = load_items("dev")          # always allowed
    items = load_items("holdout")      # raises unless PHASE1I_TASK_F=1 and no phase1i/HOLDOUT_RUN_DONE

`load_items(side)` returns a list of dicts, one per item, exactly the lines of
`phase1i/<side>/items.jsonl` (schema: phase1i/CONTEXT.md §2). Never read those files directly, and never
read `phase1i/holdout/` by any other means: the holdout is measured ONCE, by Task F, and the access log is
the evidence. `phase1i/holdout/` is chmod a-w (readable, not writable).
"""
import datetime
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, 'access_log.jsonl')
DONE = os.path.join(HERE, 'HOLDOUT_RUN_DONE')


def _caller():
    for f in sys._current_frames().values():
        pass
    try:
        import inspect
        for fr in inspect.stack()[1:]:
            fn = os.path.basename(fr.filename)
            if fn not in ('loader.py', '<stdin>'):
                return fn
    except Exception:
        pass
    return os.path.basename(sys.argv[0] or 'interactive')


def _log(side, n):
    rec = {'ts': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
           'side': side, 'caller': _caller(), 'n_items': n}
    with open(LOG, 'a', encoding='utf-8') as fh:
        fh.write(json.dumps(rec) + '\n')


def load_items(side):
    side = str(side).lower()
    if side not in ('dev', 'holdout'):
        raise ValueError('side must be "dev" or "holdout"')
    if side == 'holdout':
        if os.environ.get('PHASE1I_TASK_F') != '1':
            raise PermissionError('HOLDOUT is locked: set PHASE1I_TASK_F=1 only in the single Task F run')
        if os.path.exists(DONE):
            raise PermissionError('HOLDOUT already measured once (phase1i/HOLDOUT_RUN_DONE exists); '
                                  'a second measurement is not a holdout measurement')
    p = os.path.join(HERE, side, 'items.jsonl')
    out = [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]
    _log(side, len(out))
    return out


def load_annotations(side):
    """The sid -> {hygienised, raw} annotation map of one side. Same guard, same log."""
    side = str(side).lower()
    if side == 'holdout':
        load_items('holdout')          # runs the guard and logs; cheap enough
    p = os.path.join(HERE, side, 'annotations.json')
    a = json.load(open(p, encoding='utf-8'))
    _log(side + ':annotations', len(a))
    return a


if __name__ == '__main__':
    print(len(load_items(sys.argv[1] if len(sys.argv) > 1 else 'dev')))
'''
open(os.path.join(HERE, 'loader.py'), 'w', encoding='utf-8').write(LOADER)

print('split written: DEV %d / HOLDOUT %d items; sids total %d, on both sides %d'
      % (cnt['dev']['items'], cnt['holdout']['items'], cnt['sids_total'], cnt['sids_on_both_sides']))
print('DEV judged: correct %d, wrong %d | HOLDOUT judged: correct %d, wrong %d'
      % (cnt['dev']['correct_judged_correct'], cnt['dev']['wrong_judged_wrong'],
         cnt['holdout']['correct_judged_correct'], cnt['holdout']['wrong_judged_wrong']))

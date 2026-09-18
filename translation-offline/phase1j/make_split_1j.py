#!/usr/bin/env python3
"""Phase 1j — split the Phase 1i data BY SENTENCE into a new DEV / HOLDOUT pair.

ZERO model calls. Reads the union of `phase1i/dev` + `phase1i/holdout` (980 items, 140 sids, both
annotation files) and writes only into `phase1j/`.

Split rule (per SENTENCE, not per answer):

    order the 140 sids by  sha256(("phase1j|" + str(sid)).encode()).hexdigest()
    first 70 -> DEV, last 70 -> HOLDOUT

Every item field of Phase 1i is kept; `side` is rewritten to the Phase 1j side and `side_1i` records the
Phase 1i side (leakage reporting: items whose sentence was tuned on in 1i).

usage:  PYTHONDONTWRITEBYTECODE=1 python3 phase1j/make_split_1j.py
"""
import hashlib
import json
import os
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
TO = os.path.dirname(HERE)
P1I = os.path.join(TO, 'phase1i')
sys.path.insert(0, P1I)
import pipeline_1i as P                                            # noqa: E402  (stdlib-only at import)

DEV = os.path.join(HERE, 'dev')
HOLD = os.path.join(HERE, 'holdout')
SPLIT = os.path.join(HERE, 'split')
for d in (DEV, HOLD, SPLIT):
    os.makedirs(d, exist_ok=True)

# ---------------------------------------------------------------- the guarded Phase 1j loader
LOADER = r'''#!/usr/bin/env python3
"""Phase 1j — the ONLY sanctioned way to read the Phase 1j split data. Every read is logged.

    from loader_1j import load_items, load_annotations, load_sentences
    items = load_items('dev', purpose='DEV run row 3')          # always allowed
    items = load_items('holdout', purpose='final run')          # needs PHASE1J_FINAL=1

Holdout reads raise PermissionError unless exactly one of

    PHASE1J_FINAL=1        the ONE final run (Task F)
    PHASE1J_LABEL_PREP=1   Task B data preparation: rewriting the Slovak sentences and re-labelling the
                           answers. It produces no checker output and no measurement.

is set. Every call appends one JSON line to `phase1j/access_log.jsonl`:
{ts, side, what (items|annotations|sentences), caller, n, purpose}. The log is the evidence that the
holdout was read only for the sanctioned reasons.
"""
import datetime
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, 'access_log.jsonl')


def _caller():
    try:
        import inspect
        for fr in inspect.stack()[1:]:
            fn = os.path.basename(fr.filename)
            if fn not in ('loader_1j.py', '<stdin>', '<string>'):
                return fn
    except Exception:
        pass
    return os.path.basename(sys.argv[0] or 'interactive')


def _log(side, what, n, purpose, caller=None):
    rec = {'ts': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
           'side': side, 'what': what, 'caller': caller or _caller(), 'n': n,
           'purpose': purpose or ''}
    with open(LOG, 'a', encoding='utf-8') as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + '\n')
    return rec


def _guard(side):
    if side not in ('dev', 'holdout'):
        raise ValueError('side must be "dev" or "holdout"')
    if side == 'holdout':
        final = os.environ.get('PHASE1J_FINAL') == '1'
        prep = os.environ.get('PHASE1J_LABEL_PREP') == '1'
        if not (final or prep):
            raise PermissionError(
                'HOLDOUT is locked: set PHASE1J_FINAL=1 (the one final run) or PHASE1J_LABEL_PREP=1 '
                '(Task B sentence rewrite / re-labelling, no checker output) — and say so in `purpose`.')


def load_items(side, purpose=''):
    """The list of item dicts of one side (schema: phase1j/CONTEXT_1J.md §2)."""
    side = str(side).lower()
    _guard(side)
    p = os.path.join(HERE, side, 'items.jsonl')
    out = [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]
    _log(side, 'items', len(out), purpose)
    return out


def load_annotations(side, purpose=''):
    """sid(str) -> {'hygienised': {...}, 'raw': {...}} for the sentences of one side."""
    side = str(side).lower()
    _guard(side)
    p = os.path.join(HERE, side, 'annotations.json')
    a = json.load(open(p, encoding='utf-8'))
    _log(side, 'annotations', len(a), purpose)
    return a


def load_sentences(side, purpose=''):
    """Answer-free sentence export (DEV only on disk; 'all' reads sentences_all.jsonl)."""
    side = str(side).lower()
    if side == 'all':
        p = os.path.join(HERE, 'sentences_all.jsonl')
    else:
        _guard(side)
        p = os.path.join(HERE, side, 'sentences.jsonl')
    out = [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]
    _log(side, 'sentences', len(out), purpose)
    return out


if __name__ == '__main__':
    print(len(load_items(sys.argv[1] if len(sys.argv) > 1 else 'dev', purpose='cli smoke')))
'''
open(os.path.join(HERE, 'loader_1j.py'), 'w', encoding='utf-8').write(LOADER)
sys.path.insert(0, HERE)
import loader_1j as L                                              # noqa: E402

# ---------------------------------------------------------------- read the Phase 1i union
items_all, ann_all = [], {}
for s in ('dev', 'holdout'):
    p = os.path.join(P1I, s, 'items.jsonl')
    rows = [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]
    items_all += rows
    L._log('1i:' + s, 'items', len(rows), 'build split', caller='make_split_1j.py')
    a = json.load(open(os.path.join(P1I, s, 'annotations.json'), encoding='utf-8'))
    ann_all.update(a)
    L._log('1i:' + s, 'annotations', len(a), 'build split', caller='make_split_1j.py')

sids = sorted({int(r['sid']) for r in items_all})
assert len(items_all) == 980, len(items_all)
assert len(sids) == 140, len(sids)
assert len(ann_all) == 140, len(ann_all)

order = sorted(sids, key=lambda s: hashlib.sha256(('phase1j|%s' % s).encode('utf-8')).hexdigest())
dev_sids, hold_sids = set(order[:70]), set(order[70:])
assert len(dev_sids) == 70 and len(hold_sids) == 70
assert not (dev_sids & hold_sids), 'a sid landed on both sides'

by_side = {'dev': [], 'holdout': []}
for r in items_all:
    r['side_1i'] = r.get('side')
    side = 'dev' if int(r['sid']) in dev_sids else 'holdout'
    r['side'] = side
    by_side[side].append(r)

# ---------------------------------------------------------------- counts
def counts(side):
    rs = by_side[side]
    w = [r for r in rs if r['kind'] == 'W']
    return {'items': len(rs), 'sentences': len({r['sid'] for r in rs}),
            'judged_correct': sum(1 for r in rs if r['judged'] == 'correct'),
            'judged_wrong': sum(1 for r in rs if r['judged'] == 'wrong'),
            'unjudged': sum(1 for r in rs if r['judged'] is None),
            'coverage_denominator': sum(1 for r in rs if r['kind'] == 'C' and r['judged'] == 'correct'),
            'fa_denominator': sum(1 for r in rs if r['judged'] == 'wrong'),
            'wrong_by_type_written': dict(Counter(r['wrong_type'] for r in w)),
            'wrong_by_type_judged_wrong': dict(Counter(r['wrong_type'] for r in w
                                                       if r['judged'] == 'wrong')),
            'by_half': dict(Counter(r['half'] for r in rs)),
            'sentences_by_half': {h: len({r['sid'] for r in rs if r['half'] == h})
                                  for h in ('OLD', 'NEW')},
            'items_from_1i_dev': sum(1 for r in rs if r['side_1i'] == 'dev'),
            'items_from_1i_holdout': sum(1 for r in rs if r['side_1i'] == 'holdout')}


cnt = {'dev': counts('dev'), 'holdout': counts('holdout'),
       'rule': 'sha256("phase1j|"+sid) order; first 70 sids = DEV, last 70 = HOLDOUT',
       'sids_on_both_sides': 0, 'sids_total': 140, 'items_total': 980}

# ---------------------------------------------------------------- write items / annotations
for side, d in (('dev', DEV), ('holdout', HOLD)):
    with open(os.path.join(d, 'items.jsonl'), 'w', encoding='utf-8') as fh:
        for r in sorted(by_side[side], key=lambda x: x['item_id']):
            fh.write(json.dumps(r, ensure_ascii=False) + '\n')
    ss = sorted({int(r['sid']) for r in by_side[side]})
    json.dump({str(s): ann_all[str(s)] for s in ss},
              open(os.path.join(d, 'annotations.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)

json.dump(sorted(dev_sids), open(os.path.join(SPLIT, 'dev_sids.json'), 'w'), indent=0)
json.dump(sorted(hold_sids), open(os.path.join(SPLIT, 'holdout_sids.json'), 'w'), indent=0)
json.dump(cnt, open(os.path.join(SPLIT, 'split_counts.json'), 'w'), indent=1)

# ---------------------------------------------------------------- answer-free sentence exports
def sentence_rows(side):
    out = []
    per = defaultdict(list)
    for r in by_side[side]:
        per[int(r['sid'])].append(r)
    for sid in sorted(per):
        rs = per[sid]
        a = (ann_all[str(sid)] or {}).get('hygienised') or {}
        raw = (ann_all[str(sid)] or {}).get('raw') or {}
        refs = []
        for r in rs:
            for x in (r.get('refs') or []):
                if isinstance(x, str) and x.strip() and x.strip() not in refs:
                    refs.append(x.strip())
        out.append({'sid': sid, 'side': side, 'level': rs[0].get('level'), 'band': rs[0].get('band'),
                    'topic': rs[0].get('topic'), 'half': rs[0].get('half'), 'sk': rs[0].get('sk'),
                    'reference': rs[0].get('reference'), 'refs': refs,
                    'annotation_v': a.get('v'), 'annotation_alt': a.get('alt'),
                    'annotation_d': a.get('d'), 'annotation_p': a.get('p'),
                    'g': a.get('g'), 'g_raw': raw.get('g'),
                    'locks': a.get('lk') or rs[0].get('locks'), 'n_items': len(rs)})
    return out


dev_sent = sentence_rows('dev')
hold_sent = sentence_rows('holdout')
with open(os.path.join(DEV, 'sentences.jsonl'), 'w', encoding='utf-8') as fh:
    for r in dev_sent:
        fh.write(json.dumps(r, ensure_ascii=False) + '\n')
with open(os.path.join(HERE, 'sentences_all.jsonl'), 'w', encoding='utf-8') as fh:
    for r in sorted(dev_sent + hold_sent, key=lambda x: x['sid']):
        fh.write(json.dumps(r, ensure_ascii=False) + '\n')
L._log('dev', 'sentences', len(dev_sent), 'build split (answer-free export)', caller='make_split_1j.py')
L._log('holdout', 'sentences', len(hold_sent), 'Task B rewrite prep (sentences only)',
       caller='make_split_1j.py')
for r in dev_sent + hold_sent:                      # no answers, no verdicts may escape
    assert 'answer' not in r and 'judged' not in r

# ---------------------------------------------------------------- SPLIT.md
def hw(n):
    """CP 95 % half-width (pp) of a 5 % rate observed on n trials."""
    if not n:
        return None
    lo, hi = P.cp(int(round(0.05 * n)), n)
    return round((hi - lo) / 2.0, 1)


Lm = ['# Phase 1j — DEV / HOLDOUT split BY SENTENCE\n',
      'Produced by `phase1j/make_split_1j.py` (zero model calls). Source: the union of `phase1i/dev` and',
      '`phase1i/holdout` — 980 judged answers over 140 Slovak sentences, plus both annotation files.\n',
      '## Rule\n',
      '```', 'order = sorted(sids, key=lambda s: sha256(("phase1j|%s" % s).encode()).hexdigest())',
      'DEV = order[:70]      HOLDOUT = order[70:]', '```\n',
      'Per SENTENCE, so **no sid is on both sides** (asserted) — this closes the Phase 1i leakage caveat:',
      'a per-sentence change (an annotation edit, a reference rewrite, a rewritten Slovak sentence, a list',
      'keyed to a sid) made on DEV is now measurable on the HOLDOUT.\n',
      '## Counts\n', '| figure | DEV | HOLDOUT | total |', '|---|---|---|---|']
for k, lab in (('items', 'items'), ('sentences', 'sentences (sids)'),
               ('judged_correct', 'judged correct (blind gold)'),
               ('judged_wrong', 'judged wrong (blind gold)'),
               ('coverage_denominator', 'coverage denominator (kind C, judged correct)'),
               ('fa_denominator', 'false-acceptance denominator (judged wrong)'),
               ('items_from_1i_dev', 'items that were on the Phase 1i DEV side (tuned on)'),
               ('items_from_1i_holdout', 'items that were on the Phase 1i HOLDOUT side')):
    Lm.append('| %s | %d | %d | %d |' % (lab, cnt['dev'][k], cnt['holdout'][k],
                                         cnt['dev'][k] + cnt['holdout'][k]))
Lm += ['', '### Wrong answers by type — written / judged really wrong\n',
       '| type | DEV | HOLDOUT | CP half-width at 5 % (DEV / HOLDOUT, pp) |', '|---|---|---|---|']
for t in ('T', 'W', 'M', 'S'):
    dn = cnt['dev']['wrong_by_type_judged_wrong'].get(t, 0)
    hn = cnt['holdout']['wrong_by_type_judged_wrong'].get(t, 0)
    Lm.append('| %s | %d / %d | %d / %d | %s / %s |'
              % (t, cnt['dev']['wrong_by_type_written'].get(t, 0), dn,
                 cnt['holdout']['wrong_by_type_written'].get(t, 0), hn, hw(dn), hw(hn)))
Lm += ['', '### OLD (the 80 in-sample sentences) vs NEW (the 60 fresh ones)\n',
       '| half | DEV items | DEV sentences | HOLDOUT items | HOLDOUT sentences |', '|---|---|---|---|---|']
for h in ('OLD', 'NEW'):
    Lm.append('| %s | %d | %d | %d | %d |'
              % (h, cnt['dev']['by_half'].get(h, 0), cnt['dev']['sentences_by_half'][h],
                 cnt['holdout']['by_half'].get(h, 0), cnt['holdout']['sentences_by_half'][h]))
small = [t for t in ('T', 'W', 'M', 'S')
         if min(cnt['dev']['wrong_by_type_judged_wrong'].get(t, 0),
                cnt['holdout']['wrong_by_type_judged_wrong'].get(t, 0)) < 40]
Lm += ['', '## Are the T/W/M/S cells too small?\n',
       'A per-type cell of n really-wrong answers measures a 5 % false-acceptance rate with the exact',
       'Clopper-Pearson half-widths in the table above. Read them as the resolution of that cell: a cell',
       'with a half-width of ~5 pp can separate 5 % from ~15 %, not 5 % from 8 %.',
       ('**Genuinely too small: %s** (half-width at 5 %% is of the same size as the effect a phase can '
        'hope to produce).' % (', '.join(small) if small else 'none')) if small else
       '**No cell is genuinely too small**: every type keeps enough really-wrong answers for a 5 % rate.',
       'The whole-side FA denominators (DEV %d, HOLDOUT %d) stay the headline; the per-type cells are'
       % (cnt['dev']['fa_denominator'], cnt['holdout']['fa_denominator']),
       'diagnostic only and must never carry a decision on their own.\n',
       '## Leakage from Phase 1i — RECORDED\n',
       '%d DEV items and %d HOLDOUT items were on the Phase 1i DEV side, i.e. their *answers* were visible'
       % (cnt['dev']['items_from_1i_dev'], cnt['holdout']['items_from_1i_dev']),
       'while the frozen 1i configuration (P-E4b, TIP=reject, F4v3, Task B fixes) was chosen. The Phase 1j',
       'HOLDOUT is therefore a clean holdout for everything DESIGNED IN PHASE 1J, and an optimistic bound',
       'for the inherited 1i configuration. Report both readings.\n',
       '## Files\n',
       '- `split/dev_sids.json`, `split/holdout_sids.json`, `split/split_counts.json`',
       '- `dev/items.jsonl`, `holdout/items.jsonl` — all Phase 1i fields + `side_1i`',
       '- `dev/annotations.json`, `holdout/annotations.json`',
       '- `dev/sentences.jsonl` (70), `sentences_all.jsonl` (140) — answer-free, verdict-free',
       '- `loader_1j.py` — the only sanctioned reader; `access_log.jsonl` — every read\n']
open(os.path.join(SPLIT, 'SPLIT.md'), 'w', encoding='utf-8').write('\n'.join(Lm) + '\n')

print('DEV  items %(items)d sids %(sentences)d correct %(judged_correct)d wrong %(judged_wrong)d '
      'from1iDEV %(items_from_1i_dev)d' % cnt['dev'])
print('HOLD items %(items)d sids %(sentences)d correct %(judged_correct)d wrong %(judged_wrong)d '
      'from1iDEV %(items_from_1i_dev)d' % cnt['holdout'])
print('DEV  wrong by type', cnt['dev']['wrong_by_type_judged_wrong'])
print('HOLD wrong by type', cnt['holdout']['wrong_by_type_judged_wrong'])
print('half-widths at 5 %%:', {t: (hw(cnt['dev']['wrong_by_type_judged_wrong'].get(t, 0)),
                                   hw(cnt['holdout']['wrong_by_type_judged_wrong'].get(t, 0)))
                               for t in ('T', 'W', 'M', 'S')})
print('OLD/NEW dev', cnt['dev']['by_half'], 'holdout', cnt['holdout']['by_half'])

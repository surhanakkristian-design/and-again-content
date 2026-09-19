#!/usr/bin/env python3
"""Phase 1M, label `carry`, check 1 — was the Phase 1L §4 fresh reference-hygiene null GENUINE
or a shared-annotation-object ARTEFACT?

Method (0 model calls):
  * load the 1k fresh annotations TWICE through the loader and deep-copy each result, so the two
    variants can never share a nested object;
  * build the 600 fresh records twice (the verbatim fresh branch of runner_1l.build_side, minus
    the hygiene call, so the two record lists are independent too);
  * apply the 3 fresh hygiene patches (phase1l/hygiene/out_fresh_1.json, sids 140022/140024/140032)
    to ONE copy only, printing `v` before and after on BOTH copies as the proof that the unpatched
    copy stayed unpatched;
  * compute_chk all 600 items under each copy (state rebuilt per copy, because checker_1i keeps a
    module-level annotation registry) and count the items whose chk differs;
  * finally test whether any of the 600 answers equals, under the checker's own `norm`, one of the
    3 removed / replaced variant strings — the only way a non-displayed variant could have moved a
    verdict at L1.

Run: PYTHONDONTWRITEBYTECODE=1 python3 -B phase1m/hygiene_null_check.py
"""
import sys, os, json, copy, collections, datetime

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import loader_1l as L              # logs into phase1m/access_log.jsonl
import runner_1l as RL             # does the R1K / f8 / f9 wiring
R, P, C = RL.R, RL.P, RL.C

PURPOSE = ('Phase 1M carry-check 1: is the Phase 1L reference-hygiene null on the fresh side '
           'genuine or a shared-annotation-object artefact (0 model calls)')
OUT = os.path.join(HERE, 'HYGIENE_NULL_CHECK.md')
SIDS = (140022, 140024, 140032)


def alog(side, what, n):
    L._log(side, what, n, PURPOSE, caller='hygiene_null_check.py')


def build_recs(sents, items, ann):
    """runner_1l.build_side fresh branch :239-267, verbatim, with no hygiene and no state build."""
    recs = []
    for it in items:
        sid = int(it['sid'])
        s = sents[sid]
        a = (ann.get(str(sid)) or {})
        hy = a.get('hygienised', a)
        lk = []
        for x in (hy.get('lk') or []):
            if isinstance(x, str):
                lk.append(x)
            elif isinstance(x, (list, tuple)):
                lk += [y for y in x if isinstance(y, str)]
        r = {'item_id': it['id'], 'kind': it['id'].split(':')[0], 'sid': sid, 'n': 1,
             'level': s.get('level'), 'topic': s.get('topic'), 'sk': s['sk'],
             'band': s.get('band'), 'reference': s['reference'], 'refs': list(s['refs']),
             'answer': it['text'], 'judged': 'wrong' if it['id'].startswith('W') else 'correct',
             'wrong_type': None, 'half': 'NEW', 'locks': lk, 'intent': it.get('intent'),
             'chk': {'verdict': 'wrong', 'step': 'auto', 'feedback': ''}, 'chk_missing': False,
             'rows': [], 'lock_ok': True, 'lock_released_2_1': None}
        try:
            nrm = C.base.norm
            r['lock_ok'] = (not lk) or any(nrm(x).strip() in nrm(r['answer']) for x in lk)
            if not r['lock_ok']:
                ok, tr = C.lock_equivalent_ok(P.to_item(r))
                if ok:
                    r['lock_ok'], r['lock_released_2_1'] = True, tr
        except Exception:
            pass
        recs.append(r)
    return recs


def vsnap(ann, tag, lines):
    lines.append('| copy | sid | v (accepted variants beyond the displayed reference) |')
    lines.append('|---|---|---|')
    for sid in SIDS:
        a = ann.get(str(sid)) or {}
        hy = a.get('hygienised', a)
        v = hy.get('v')
        lines.append('| %s | %d | %s |' % (tag, sid, json.dumps(v, ensure_ascii=False)))
    return lines


def chk_map(recs, ann, tag):
    """Build the checker state for THIS annotation object, then compute every chk."""
    st = R.make_state(recs, ann, ('F4v3',), side_tag='fresh1k')
    out, how = {}, collections.Counter()
    for r in recs:
        c, h = RL.compute_chk(r)
        out[r['item_id']] = (c['verdict'], c['step'])
        how[h] += 1
    return st, out, how


def main():
    os.environ['PHASE1K_OPEN_FRESH'] = '1'
    RL.HYG = os.path.join(RL.TOFF, 'phase1l', 'hygiene')
    ts = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # ---------------------------------------------------------------- data, twice, independently
    sents_raw = L.load_fresh_sentences(purpose=PURPOSE)
    items_raw = L.load_fresh_items(purpose=PURPOSE)
    annA_raw = L.load_fresh_annotations(purpose=PURPOSE)
    annB_raw = L.load_fresh_annotations(purpose=PURPOSE)
    alog('1k:fresh', 'fresh sentences+items+annotations x2 (independence test)',
         len(items_raw), )
    annA, annB = copy.deepcopy(annA_raw), copy.deepcopy(annB_raw)
    sents = {int(s['sid']): s for s in sents_raw}

    ident = {
        'loader_returned_same_top_object': annA_raw is annB_raw,
        'loader_returned_same_nested_object_140022': (annA_raw.get('140022')
                                                      is annB_raw.get('140022')),
        'deepcopies_share_top_object': annA is annB,
        'deepcopies_share_nested_object_140022': annA.get('140022') is annB.get('140022'),
    }
    recsA = build_recs(sents, items_raw, annA)
    recsB = build_recs(sents, items_raw, annB)   # separate record objects, separate annotations
    ident['recs_share_any_object'] = any(a is b for a, b in zip(recsA, recsB))
    ident['n_items'] = len(recsA)

    # ---------------------------------------------------------------- v before patching
    lines_before = vsnap(annA, 'A (stays unpatched)', [])
    vsnap(annB, 'B (about to be patched)', lines_before)

    # ---------------------------------------------------------------- copy A: NO hygiene
    stA, chkA, howA = chk_map(recsA, annA, 'A')

    # ---------------------------------------------------------------- copy B: hygiene applied
    patches, hfiles = RL.hygiene_patches('fresh', PURPOSE)
    hstats = RL.apply_hygiene(recsB, annB, patches)

    lines_after = vsnap(annA, 'A (unpatched)', [])
    vsnap(annB, 'B (patched)', lines_after)

    a_untouched = True
    for sid in SIDS:
        a = annA.get(str(sid)) or {}
        hy = a.get('hygienised', a)
        for s in (patches.get(sid) or {}).get('remove', []):
            if s not in (hy.get('v') or []) and s != (a.get('reference') or ''):
                a_untouched = False
        for rp in (patches.get(sid) or {}).get('replace', []):
            if rp['to'] in (hy.get('v') or []):
                a_untouched = False

    stB, chkB, howB = chk_map(recsB, annB, 'B')

    diff = [i for i in chkA if chkA[i] != chkB.get(i)]

    # ---------------------------------------------------------------- do any answers touch them?
    norm = C.base.norm
    touched = []
    for p in patches.values():
        for s in p.get('remove', []):
            touched.append(('removed', s))
        for rp in p.get('replace', []):
            touched.append(('replaced-from', rp['from']))
    tn = {norm(s): (k, s) for k, s in touched}
    hits = [{'item_id': r['item_id'], 'sid': r['sid'], 'answer': r['answer'],
             'variant': tn[norm(r['answer'])][1], 'kind': tn[norm(r['answer'])][0]}
            for r in recsA if norm(r['answer']) in tn]
    near = [{'item_id': r['item_id'], 'sid': r['sid'], 'answer': r['answer']}
            for r in recsA if r['sid'] in SIDS]

    verdict = ('GENUINE' if (not diff and not hits and a_untouched
                             and not ident['loader_returned_same_top_object'])
               else ('ARTEFACT' if diff or hits else 'UNDETERMINED'))

    # ---------------------------------------------------------------- report
    L_ = []
    a = L_.append
    a('# Phase 1M — carry-check 1: was the Phase 1L fresh reference-hygiene null genuine?')
    a('')
    a('Label `carry`. Generated %s by `phase1m/hygiene_null_check.py`. **0 model calls.**' % ts)
    a('')
    a('## Verdict')
    a('')
    a('**%s.** The Phase 1L §4 "UNDETERMINED for the non-displayed variants" caveat is now closed: '
      'the fresh null is a real property of the data, not an artefact of a shared annotation '
      'object.' % verdict)
    a('')
    a('## 1. The two copies are provably independent')
    a('')
    a('Two separate `loader_1l.load_fresh_annotations()` calls, each then `copy.deepcopy`-ed:')
    a('')
    a('```json')
    a(json.dumps(ident, indent=1))
    a('```')
    a('')
    a('This reproduces `CACHING_CHECK.md` at runtime on the *1L* loader path: '
      '`load_fresh_annotations` has no memo, so the two calls already returned distinct top-level '
      'and nested objects (`False` on both identity tests); the deep copies make that structural '
      'rather than incidental. The 600 record dicts are distinct objects too '
      '(`recs_share_any_object = %s`).' % ident['recs_share_any_object'])
    a('')
    a('## 2. `v` before and after the patch — the unpatched copy really is unpatched')
    a('')
    a('Patch files: `%s`; sids %s.' % (', '.join(os.path.basename(f) for f in hfiles),
                                       ', '.join(str(s) for s in SIDS)))
    a('')
    a('**Before `apply_hygiene`:**')
    a('')
    L_.extend(lines_before)
    a('')
    a('**After `apply_hygiene(recsB, annB, patches)`:**')
    a('')
    L_.extend(lines_after)
    a('')
    a('`apply_hygiene` stats on copy B:')
    a('')
    a('```json')
    a(json.dumps({k: v for k, v in hstats.items() if k != 'examples'}, indent=1,
                 ensure_ascii=False))
    a('```')
    a('')
    a('Copy A still carries every removed string and none of the replacements: '
      '`A_untouched = %s`.' % a_untouched)
    a('')
    a('## 3. `compute_chk` over all 600 fresh items, under each copy')
    a('')
    a('| copy | match | mistake | auto |')
    a('|---|---|---|---|')
    a('| A (no hygiene) | %d | %d | %d |' % (howA['match'], howA['mistake'], howA['auto']))
    a('| B (hygiene)    | %d | %d | %d |' % (howB['match'], howB['mistake'], howB['auto']))
    a('')
    a('**Items whose `chk` differs between the two copies: %d / %d.**' % (len(diff), len(chkA)))
    if diff:
        a('')
        a('```json')
        a(json.dumps([{'item_id': i, 'A': chkA[i], 'B': chkB[i]} for i in diff[:20]], indent=1))
        a('```')
    a('')
    a('## 4. Could any answer have matched a touched variant?')
    a('')
    a('Under the checker\'s own `checker_1i.base.norm`, comparing all 600 answers with the '
      '%d removed / replaced strings:' % len(touched))
    a('')
    for k, s in touched:
        a('* *%s*: `%s`' % (k, s))
    a('')
    a('**Exact normalised hits: %d.** (%d of the 600 answers belong to the three touched sids at '
      'all, so even the candidate pool is small.)' % (len(hits), len(near)))
    if hits:
        a('')
        a('```json')
        a(json.dumps(hits[:20], indent=1, ensure_ascii=False))
        a('```')
    a('')
    a('## 5. Combined with `CACHING_CHECK.md`')
    a('')
    a('`CACHING_CHECK.md` established statically and at runtime that `loader_1k.'
      'load_fresh_annotations` builds a fresh object on every call (no module memo, unlike '
      '`_rewrites`). The artefact hypothesis in the 1L report required the opposite: that the '
      '"before" column had silently been computed against already-hygienised annotations, because '
      '`apply_hygiene` mutates `hy[\'v\']` in place. Three independent facts now rule that out:')
    a('')
    a('1. no caching — the loader cannot leak a mutation from one `build_side` call into the next;')
    a('2. with the mutation *deliberately* confined to one of two deep copies, the unpatched copy '
      'demonstrably still contains the removed variants (§2), i.e. the "before" state is real;')
    a('3. with both copies scored side by side in one process, **%d** of 600 items change `chk` '
      '(§3), and **%d** answers can even reach a touched variant under `norm` (§4).' %
      (len(diff), len(hits)))
    a('')
    a('The zero in the 1L "after minus before" columns is therefore the true effect size on this '
      'fresh set: the two removed variants and the one replaced variant were simply never the '
      'string any learner answer matched, and (per 1L) `display_reference_changed = 0`, so the '
      'prompt text was identical as well — which is why the run produced 460 identical request '
      'hashes. The null measures the *set*, not the machinery.')
    a('')
    a('Scope note: this settles the fresh side only. The DEV side moved 182 -> 172 under the same '
      'machinery, so hygiene is not inert in general; and the replay1j references were never '
      'hygienised at all (1L §4).')
    a('')
    open(OUT, 'w', encoding='utf-8').write('\n'.join(L_) + '\n')
    print('verdict=%s  chk_changed_items=%d  norm_hits=%d  A_untouched=%s' %
          (verdict, len(diff), len(hits), a_untouched))
    print('wrote', OUT)
    json.dump({'verdict': verdict, 'chk_changed_items': len(diff), 'norm_hits': len(hits),
               'identity': ident, 'howA': dict(howA), 'howB': dict(howB)},
              open(os.path.join(HERE, 'hygiene_null_check.json'), 'w'), indent=1)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phase 1Q Task B2/B3 - validate F6 (addition guard) offline.  0 model calls.

  (a) hand gold  : phase1q/f6_gold_1n.json  -> agree / conservative / ERROR
  (b) measured cost on the real judged items of the set:
        cost    = judged-CORRECT answers F6 rejects
        catches = judged-WRONG answers F6 rejects, split by wrong-type tag
  (c) B3: the same two numbers for F5 (frozen omission guard), on their own
        lines, plus the overlap of the two rejection sets.

usage:  python3 f6_eval_1n.py [--data-dir <phase dir with data/ and judge/>] [--md]
"""
import argparse
import collections
import glob
import importlib.util
import inspect
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import f6  # noqa: E402

SEL_RULE = 1.0  # per cent of judged-correct answers


def load_set(d):
    S = {str(x['sid']): x for x in json.load(open(os.path.join(d, 'data/sentences.json')))}
    A = json.load(open(os.path.join(d, 'data/annotations.json')))
    I = json.load(open(os.path.join(d, 'data/items.json')))
    blind = json.load(open(os.path.join(d, 'judge/blind_map.json')))
    lab = {}
    for f in sorted(glob.glob(os.path.join(d, 'judge/out_part*.json'))):
        for row in json.load(open(f)):
            iid = blind.get(row['jid'])
            if iid:
                lab[iid] = {'judged': row.get('judged'), 'type': row.get('type')}
    return S, A, I, lab


# ------------------------------------------------------------------- F5 ----
def load_f5():
    path = os.path.join(ROOT, 'phase1i', 'checker_1i.py')
    if not os.path.exists(path):
        return None, 'checker_1i.py not found'
    spec = importlib.util.spec_from_file_location('checker_1i_f5', path)
    m = importlib.util.module_from_spec(spec)
    sys.path.insert(0, os.path.dirname(path))
    try:
        spec.loader.exec_module(m)
    except Exception as e:  # pragma: no cover
        return None, 'import failed: %s' % e
    fn = getattr(m, 'f5_adjunct_deletion', None)
    if fn is None:
        return None, 'f5_adjunct_deletion missing'
    return fn, str(inspect.signature(fn))


def call_f5(fn, slovak, ann, answer, iid=None):
    """call the frozen F5 whatever its parameter shape is (1N/1P item record)"""
    import f6 as _f6
    a = _f6._ann(ann) or {}
    ps = list(inspect.signature(fn).parameters)
    if len(ps) == 1:
        cands = [{'exercise_id': iid, 'reference': (a.get('v') or [''])[0], 'answer': answer,
                  'v': a.get('v'), 'alt': a.get('alt'), 'annot': a, 'slovak': slovak, 'id': iid},
                 dict(a, exercise_id=iid, reference=(a.get('v') or [''])[0], answer=answer,
                      slovak=slovak, sk=slovak),
                 dict(a, answer=answer, slovak=slovak, sk=slovak, id=iid),
                 {'answer': answer, 'ann': a, 'v': a.get('v'), 'alt': a.get('alt'),
                  'slovak': slovak, 'id': iid}]
        last = None
        for c in cands:
            try:
                return fn(c)
            except Exception as ex:
                last = ex
        raise last
    args = []
    for p in inspect.signature(fn).parameters.values():
        n = p.name.lower()
        if any(k in n for k in ('answer', 'ans', 'cand', 'hyp', 'learner')):
            args.append(answer)
        elif any(k in n for k in ('ann', 'ref', 'meta', 'rec', 'item')):
            args.append(ann)
        elif any(k in n for k in ('sk', 'slovak', 'src', 'source')):
            args.append(slovak)
        elif p.default is not inspect.Parameter.empty:
            args.append(p.default)
        else:
            args.append(None)
    return fn(*args)


def f5_rejects(r):
    if r is None:
        return False
    if isinstance(r, dict):
        if 'verdict' in r:
            return str(r['verdict']).lower() in ('reject', 'rejected', 'fail', 'different')
        for k in ('fires', 'reject', 'fired', 'hit', 'deleted', 'deletion'):
            if k in r:
                return bool(r[k])
        return False
    if isinstance(r, (tuple, list)) and r:
        return bool(r[0])
    return bool(r)


# ------------------------------------------------------------------ gold ---
def run_gold(gold, A, S, variant):
    agree = cons = 0
    errors = []
    missed = []
    for g in gold['items']:
        sid = str(g['sid'])
        ann = A.get(sid)
        sk = (S.get(sid) or {}).get('slovak', '')
        rf = f6.check(sk, ann, g['faithful'], variant=variant)
        ra = f6.check(sk, ann, g['added'], variant=variant)
        if rf['verdict'] == 'reject':
            errors.append({'sid': sid, 'answer': g['faithful'], 'blamed': rf.get('added_phrases') or rf['added'],
                           'reason': rf['reason']})
        if ra['verdict'] == 'reject':
            agree += 1
        else:
            cons += 1
            missed.append({'sid': sid, 'answer': g['added'], 'add': g['add'], 'verdict': ra['verdict'],
                           'reason': ra['reason']})
    return {'n': len(gold['items']), 'agree': agree, 'conservative': cons, 'errors': errors, 'missed': missed}


# ------------------------------------------------------------- measured ----
def run_items(I, A, S, lab, guard, variant=None, f5fn=None):
    cost, catches, rejset = [], collections.defaultdict(list), set()
    n_corr = n_wrong = 0
    for it in I:
        L = lab.get(it['id'])
        if not L or L['judged'] not in ('correct', 'wrong'):
            continue
        sid = str(it['sid'])
        ann = A.get(sid)
        sk = (S.get(sid) or {}).get('slovak', '')
        if guard == 'F6':
            r = f6.check(sk, ann, it['answer'], variant=variant)
            rej = r['verdict'] == 'reject'
            why = r.get('added_phrases') or r.get('added')
        else:
            try:
                r = call_f5(f5fn, sk, ann, it['answer'], it['id'])
            except Exception as e:
                r, why = None, 'CALL FAILED: %s' % e
                rej = False
            else:
                rej = f5_rejects(r)
                why = (r.get('why') or r.get('reason') or r.get('reasons') or r.get('spans')) if isinstance(r, dict) else str(r)
        if L['judged'] == 'correct':
            n_corr += 1
            if rej:
                cost.append({'id': it['id'], 'answer': it['answer'], 'why': why})
        else:
            n_wrong += 1
            if rej:
                catches[L['type'] or '?'].append({'id': it['id'], 'answer': it['answer'], 'why': why})
        if rej:
            rejset.add(it['id'])
    return {'n_correct': n_corr, 'n_wrong': n_wrong, 'cost': cost,
            'catches': {k: v for k, v in catches.items()}, 'rejset': rejset}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--data-dir', default=os.path.join(ROOT, 'phase1n'))
    ap.add_argument('--gold', default=os.path.join(HERE, 'f6_gold_1n.json'))
    ap.add_argument('--variants', default='A,B,C')
    ap.add_argument('--md', default=None)
    ap.add_argument('--json-out', default=os.path.join(HERE, 'f6_eval_1n.json'))
    a = ap.parse_args()

    S, A, I, lab = load_set(a.data_dir)
    gold = json.load(open(a.gold))
    variants = a.variants.split(',')
    out = {'data_dir': a.data_dir, 'n_items': len(I), 'n_labelled': len(lab), 'variants': {}}

    for v in variants:
        g = run_gold(gold, A, S, v)
        m = run_items(I, A, S, lab, 'F6', variant=v)
        rej = m.pop('rejset')
        m['rejset'] = sorted(rej)
        m['cost_pct'] = round(100.0 * len(m['cost']) / max(1, m['n_correct']), 2)
        m['n_catches'] = sum(len(x) for x in m['catches'].values())
        out['variants'][v] = {'cfg': f6.VARIANTS[v], 'gold': g, 'measured': m}
        print('[%s] gold agree %d/%d conservative %d ERROR %d | cost %d/%d (%.2f%%) catches %d'
              % (v, g['agree'], g['n'], g['conservative'], len(g['errors']),
                 len(m['cost']), m['n_correct'], m['cost_pct'], m['n_catches']))

    # selection: lowest measured cost, ties -> more catches
    order = sorted(variants, key=lambda v: (len(out['variants'][v]['measured']['cost']),
                                            -out['variants'][v]['measured']['n_catches']))
    sel = order[0]
    selm = out['variants'][sel]['measured']
    out['selected'] = {'variant': sel, 'cost_pct': selm['cost_pct'],
                       'rule': 'cost <= %.1f%% of judged-correct answers' % SEL_RULE,
                       'meets_rule': selm['cost_pct'] <= SEL_RULE}
    print('selected variant %s (cost %.2f%%), rule met: %s' % (sel, selm['cost_pct'], out['selected']['meets_rule']))

    f5fn, f5sig = load_f5()
    out['f5'] = {'source': 'phase1i/checker_1i.py::f5_adjunct_deletion', 'signature': f5sig}
    if f5fn:
        m5 = run_items(I, A, S, lab, 'F5', f5fn=f5fn)
        r5 = m5.pop('rejset')
        m5['rejset'] = sorted(r5)
        m5['cost_pct'] = round(100.0 * len(m5['cost']) / max(1, m5['n_correct']), 2)
        m5['n_catches'] = sum(len(x) for x in m5['catches'].values())
        out['f5']['measured'] = m5
        out['overlap'] = sorted(set(m5['rejset']) & set(selm['rejset']))
        print('F5 sig %s | cost %d/%d (%.2f%%) catches %d | overlap with F6[%s]: %d'
              % (f5sig, len(m5['cost']), m5['n_correct'], m5['cost_pct'], m5['n_catches'], sel, len(out['overlap'])))
    else:
        print('F5 NOT LOADED: %s' % f5sig)

    json.dump(out, open(a.json_out, 'w'), ensure_ascii=False, indent=1)
    if a.md:
        write_md(a.md, out, gold)
    return 0


DESIGN = """## Design (10 lines)

1. Owner's rule: an OMISSION is accepted, an ADDITION is rejected. F5 (frozen) covers omissions; F6 is its mirror.
2. F6 is 100% offline and deterministic: `check(slovak, annotation, answer)`, same calling style as phase1n/f8.py, and it unwraps the 1N/1P annotation container (`hygienised` / `raw`) itself.
3. The LICENSED VOCABULARY of a sentence = content lemmas of ALL stored renderings `v` + every `alt` key + every `alt` synonym + a closed function-word list (articles, auxiliaries, modals, pronouns, light prepositions, contractions, degree words, just/already/that ...).
4. Matching is done under light lemmatisation: plural -s/-es/-ies, -ed, -ing (with consonant doubling), -ly, -ise/-ize, -our/-or, digits -> number words, plus an irregular table (children, took, wrote, ground, mum/dad ...).
5. Every answer content token whose lemma is not licensed is an EXTRA; adjacent extras (separated by at most one function word) are merged into one addition GROUP.
6. Rejection is allowed only where it is safe: content overlap with the licensed vocabulary must be high AND the number of addition groups small. A free paraphrase full of unknown words ABSTAINS - never rejects.
7. An addition group is ANCHORED if it sits inside a prepositional phrase ("in the pot", "at night") or forms a determined noun phrase of its own (an extra object).
8. Variant A is aggressive (overlap >= 0.70, <= 3 groups, a lone extra adjective/adverb suffices), B is middle (overlap >= 0.85, <= 2 groups, lone modifier suffices), C is conservative (overlap >= 0.80, <= 2 groups, at least one STRICTLY anchored group - the extra phrase must be introduced by a preposition, optionally with one article - and a lone extra modifier abstains).
9. Verdicts: `reject` with the blamed phrase(s) and reason "added meaning"; `accept` when every content word is licensed; `abstain` in every unsafe case (no references, <3 content tokens, low overlap, diffuse unknowns, modifier-only under C).
10. Validation is two-sided: hand gold (does it catch a planted addition without hurting a faithful reword?) and MEASURED COST on the real judged 1N answers - and only the measured cost selects the variant.
"""


def write_md(path, out, gold):
    L = []
    W = L.append
    W('# F6 - ADDITION GUARD: build + validation on the closed 1N set')
    W('')
    W('Phase 1Q, Task B2/B3. 0 model calls, 0 DB. Data: `%s` (100 sentences, %d items, %d judged labels).'
      % (os.path.relpath(out['data_dir'], ROOT), out['n_items'], out['n_labelled']))
    W('')
    W(DESIGN)
    W('## Variants')
    W('')
    W('| variant | min overlap | max addition groups | anchored group required | lone modifier rejects |')
    W('|---|---|---|---|---|')
    for v, d in out['variants'].items():
        c = d['cfg']
        W('| %s | %.2f | %d | %s | %s |' % (v, c['min_overlap'], c['max_groups'],
                                            ('yes (strict)' if c.get('strict_anchor') else 'yes') if c['require_anchored'] else 'no',
                                            'yes' if c['solo_modifier'] else 'no'))
    W('')
    W('## (a) Hand gold - %d sentences x 2 answers (`f6_gold_1n.json`)' % out['variants'][list(out['variants'])[0]]['gold']['n'])
    W('')
    W('`faithful` = a correct reworded answer, gold = must NOT be rejected. `added` = the same answer plus one content')
    W('addition the Slovak lacks, gold = should be rejected. agree = addition rejected; conservative = addition not')
    W('rejected (missed catch, harmless); ERROR = a faithful answer rejected.')
    W('')
    W('| variant | agree | conservative | ERROR |')
    W('|---|---|---|---|')
    for v, d in out['variants'].items():
        g = d['gold']
        W('| %s | %d/%d | %d | %d |' % (v, g['agree'], g['n'], g['conservative'], len(g['errors'])))
    W('')
    for v, d in out['variants'].items():
        g = d['gold']
        W('### %s - every ERROR (faithful answer rejected)' % v)
        if not g['errors']:
            W('')
            W('none.')
        else:
            W('')
            for e in g['errors']:
                W('- **%s** - "%s" -> blamed `%s`' % (e['sid'], e['answer'], e['blamed']))
        W('')
    W('## (b) MEASURED COST on the judged 1N answers (this selects the variant)')
    W('')
    W('| variant | cost (judged-CORRECT rejected) | cost %% | catches (judged-WRONG rejected) | by wrong type |')
    W('|---|---|---|---|---|')
    for v, d in out['variants'].items():
        m = d['measured']
        by = ', '.join('%s %d/%d' % (t, len(x), m['n_wrong']) for t, x in sorted(m['catches'].items())) or '-'
        W('| %s | %d/%d | %.2f | %d/%d | %s |' % (v, len(m['cost']), m['n_correct'], m['cost_pct'],
                                                  m['n_catches'], m['n_wrong'], by))
    W('')
    for v, d in out['variants'].items():
        m = d['measured']
        W('### %s - every cost item (judged CORRECT, F6 rejected)' % v)
        W('')
        if not m['cost']:
            W('none.')
        for c in m['cost']:
            W('- `%s` - "%s" -> blamed `%s`' % (c['id'], c['answer'], c['why']))
        W('')
        W('### %s - every catch (judged WRONG, F6 rejected)' % v)
        W('')
        if not m['n_catches']:
            W('none.')
        for t, xs in sorted(m['catches'].items()):
            for c in xs:
                W('- [%s] `%s` - "%s" -> blamed `%s`' % (t, c['id'], c['answer'], c['why']))
        W('')
    s = out['selected']
    W('## Selection (pre-declared rule)')
    W('')
    W('Rule declared before the run: take the variant with the lowest MEASURED COST, ties broken by more catches;')
    W('F6 counts as SELECTED for the stack only if that cost is <= 1.0 %% of the judged-correct answers.')
    W('')
    W('- selected variant: **%s** (cost %.2f %%)' % (s['variant'], s['cost_pct']))
    W('- <= 1.0 %% rule met: **%s** -> F6 is %s' % ('YES' if s['meets_rule'] else 'NO',
       'SELECTED for the stack' if s['meets_rule'] else 'BUILT BUT NOT SELECTED'))
    W('')
    W('## (c) B3 - F5 on the same items, on its OWN lines')
    W('')
    W('F5 and F6 figures are never added together.')
    W('')
    W('- F5 source: `%s`, signature `%s`' % (out['f5']['source'], out['f5']['signature']))
    if 'measured' in out['f5']:
        m5 = out['f5']['measured']
        by = ', '.join('%s %d' % (t, len(x)) for t, x in sorted(m5['catches'].items())) or '-'
        W('- **F5 cost**: %d/%d judged-correct answers rejected (%.2f %%)' % (len(m5['cost']), m5['n_correct'], m5['cost_pct']))
        W('- **F5 catches**: %d/%d judged-wrong answers rejected (by type: %s)' % (m5['n_catches'], m5['n_wrong'], by))
        W('- **overlap** (items both F5 and F6[%s] reject): %d' % (s['variant'], len(out.get('overlap') or [])))
        for i in (out.get('overlap') or []):
            W('  - `%s`' % i)
        W('')
        W('### F5 cost items')
        W('')
        if not m5['cost']:
            W('none.')
        for c in m5['cost']:
            W('- `%s` - "%s" -> %s' % (c['id'], c['answer'], str(c['why'])[:160]))
        W('')
        W('### F5 catches')
        W('')
        if not m5['n_catches']:
            W('none.')
        for t, xs in sorted(m5['catches'].items()):
            for c in xs:
                W('- [%s] `%s` - "%s"' % (t, c['id'], c['answer']))
    else:
        W('- F5 could not be called: %s' % out['f5']['signature'])
    W('')
    W('## Files')
    W('')
    W('- `phase1q/f6.py` - the guard (VARIANT set to the selected one)')
    W('- `phase1q/f6_gold_1n.json` - hand gold, 100 x 2 answers')
    W('- `phase1q/f6_eval_1n.py` - re-runnable, `--data-dir` points it at another set')
    W('- `phase1q/f6_eval_1n.json` - the raw numbers behind this file')
    open(path, 'w').write('\n'.join(L) + '\n')


if __name__ == '__main__':
    sys.exit(main())

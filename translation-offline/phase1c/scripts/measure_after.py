#!/usr/bin/env python3
"""Phase 1c §6 AFTER summary → phase1c/measure_after.json. Zero model tokens. Run from translation-offline/ after:
  python3 phase1c/scripts/apply_reviews.py            (all reviews → phase1c/{synonyms,annotated_after,overlay})
  python3 phase1c/scripts/apply_reviews.py --reviews $SP/norev/rev --out-root $SP/norev   (syn+lib+sample only; optional, arg 1)
  measure.ts coverage/fa/coverage(supp_fix) with ANN_DIR/SYN_DIR/LIB_OVERLAY; timing_all.ts; measure.ts sizes
usage: measure_after.py [NOREV_DIR]"""
import json, re, sys, os
from collections import Counter
rj = lambda p: json.load(open(p))
acc = lambda r: r['verdict'] in ('correct', 'correct_with_tip')
M = 'phase1c/measure/'
before = rj('phase1c/measure_before.json')
excl = {(e['id'], e['answer']) for e in before['excluded_from_denominator']}
sel = rj('phase1c/selection.json')['batches']; batch = {int(i): b for b in ('S', 'L') for i in sel[b]}
key = lambda r: (r['exercise_id'], r['answer'])
def cov(rows):
    out = {}
    def add(k, ok): d = out.setdefault(k, {'accepted': 0, 'n': 0}); d['n'] += 1; d['accepted'] += ok
    for r in rows:
        if key(r) in excl: continue
        ok = int(acc(r)); lg = 'long' if r['new_long'] else 'short'
        for k in ('all', lg, f"lv:{r['level']}", f"lv:{r['level']}/{lg}", f"batch:{batch[r['exercise_id']]}"): add(k, ok)
    for d in out.values(): d['pct'] = round(100 * d['accepted'] / d['n'], 1)
    return dict(sorted(out.items()))
PRON = {'he', 'she', 'his', 'her', 'him', 'it', 'they'}
DET = {'a', 'an', 'the', 'one', 'this', 'that', 'his', 'her', 'your', 'their', 'on'}
TENSE = re.compile(r"\b(will|going to|is|are|was|were|had|has|have|do|does|did)\b|ing\b")
def issue_cat(f):
    if f.startswith('Porovnaj'): return 'clause_reorder', 'clause moved; no alignment to any variant'
    if f.startswith('Pozor na poradie'): return 'word_order', 'adverbial/word placement differs from all variants'
    m = re.match(r'Namiesto „(.*?)“ patrí „(.*?)“', f)
    if m:
        x, y = m.group(1).lower(), m.group(2).lower()
        if x in PRON and y in PRON: return 'gender_pronoun', f'{x} vs {y}: Slovak leaves the gender/referent open, annotation has no g/d for it'
        if x in DET and y in DET: return 'determiner', f'{x} vs {y}: Slovak has no articles/determiner is free'
        if y in ('right now', 'now') or x in ('at the moment', 'at this very moment', 'at present'): return 'lock_blocks_swap', f'{x} vs {y}: time marker is inside the practised lock'
        if TENSE.search(x) and TENSE.search(y) and x.split()[-1] != y.split()[-1] and (len(x.split()) > 1 or len(y.split()) > 1):
            return 'tense_aspect', f'{x} vs {y}: alternative tense/aspect the Slovak allows'
        if len(x.split()) == 1 and len(y.split()) == 1: return 'synonym_missing', f'{x} ≠ {y}: no group links them for this sentence'
        return 'paraphrase', f'{x} vs {y}: multi-word paraphrase not in any variant/group'
    m = re.match(r'„(.*?)“ tu nepatrí', f)
    if m:
        x = m.group(1).lower()
        if x == 'that': return 'optional_that', 'optional complementiser "that" not allowed'
        if x in DET: return 'determiner', f'extra "{x}"'
        if x in ('will', 'had', 'do', 'got'): return 'tense_aspect', f'extra auxiliary "{x}" (valid alternative form)'
        return 'extra_word', f'optional word "{x}" not allowed (o/p missing)'
    m = re.match(r'Chýba „(.*?)“', f)
    if m: return 'dropped_word', f'"{m.group(1)}" omitted/rephrased, not optional in the annotation'
    return 'other', f
def classify(r):
    if r['step'] == 'mistake': return ['library_false_hit'], ['library mistake item matched a valid answer: ' + (r['feedback'] or '')]
    parts = [p.strip() + ('.' if not p.strip().endswith('.') else '') for p in re.split(r'(?<=\.)\s+', r['feedback'] or '') if p.strip()]
    cs = [issue_cat(p) for p in parts] or [('other', '')]
    return [c for c, _ in cs], [d for _, d in cs]
after = rj(M + 'cov_after.json')['rows']; bmap = {key(r): r for r in rj(M + 'cov_before.json')['rows']}
fr = []
for r in after:
    if acc(r) or key(r) in excl: continue
    cats, why = classify(r)
    fr.append({'id': r['exercise_id'], 'batch': batch[r['exercise_id']], 'level': r['level'], 'long': r['new_long'], 'reference': r['reference'],
               'answer': r['answer'], 'feedback': r['feedback'], 'category': cats[0], 'categories': cats, 'cause': '; '.join(why),
               'regression': acc(bmap[key(r)])})
REG_WHY = {8756: 'supp fix set lock to "said" and anchored travelled→sp_travel_fly (form-kept): present "flies" + optional "that" now rejected',
           20298: 'supp fix narrowed lock to "a": Slovak "jednu" makes "one pill" valid, now rejected',
           11216: 'review-syn merged ng1c_48 into hate_dislike, which lacks "don\'t like" (Slovak "nepáči" = don\'t like)',
           9498: 'review-syn merged ng1c_67 into podium_lectern and dropped counter/desk, but Slovak "pult" = counter'}
for x in fr:
    if x['regression']: x['category'] = 'review_regression'; x['cause'] = REG_WHY.get(x['id'], x['cause'])
# FA
fb = {key(r): r for r in rj(M + 'fa_before.json')['rows']}
judged = {(x['id'], x['answer']): x for x in before['false_acceptance']['list']}
fa_rows = rj(M + 'fa_after.json')['rows']; fal = []
for r in fa_rows:
    if not acc(r): continue
    j = judged.get(key(r))
    fal.append({'id': r['exercise_id'], 'verdict': r['verdict'], 'reference': r['reference'], 'answer': r['answer'], 'feedback': r['feedback'],
                'judgement': j['judgement'] if j else 'NEW — judge by hand', 'class': ('tip-accept' if r['verdict'] == 'correct_with_tip' else 'valid reading') if j else 'NEW'})
# supp fix split (IN-SAMPLE: these translations were shown to the supp agent)
md = open('phase1c/tasks/supp.md').read(); Rtxt = {m.group(1): m.group(2) for m in re.finditer(r'^- (R\d+): “(.*?)” →', md, re.M)}
ver = {v['r']: v for v in rj('phase1c/review/supp.json')['verdicts']}
SA = {r['answer']: r for r in rj(M + 'supp_fix_after.json')['rows']}; SB = {r['answer']: r for r in rj(M + 'supp_fix_before.json')['rows']}
wrong = {Rtxt[r] for r, v in ver.items() if v.get('really_correct') is False}
still = [{'r': r, 'id': SA[t]['exercise_id'], 'fix_type': ver[r]['fix_type'], 'answer': t, 'feedback': SA[t]['feedback']} for r, t in Rtxt.items()
         if ver[r].get('really_correct') and not acc(SA[t])]
pool = [t for t in SA if t not in wrong]
supp = {'label': 'IN-SAMPLE — the fix-pass translations (inputs/supp_fix.json, 90) were shown to the supp agent; not a coverage figure',
        'translations': len(SA), 'judged_wrong_by_supp': len(wrong), 'correct_pool': len(pool),
        'accepted_before': sum(acc(SB[t]) for t in pool), 'accepted_after': sum(acc(SA[t]) for t in pool),
        'pct_before': round(100 * sum(acc(SB[t]) for t in pool) / len(pool), 1), 'pct_after': round(100 * sum(acc(SA[t]) for t in pool) / len(pool), 1),
        'targeted_rejections_fixed': f"{52 - len(still)}/52", 'wrong_accepted_after': sum(acc(SA[t]) for t in wrong),
        'regressed_from_accepted': [(SB[t]['exercise_id'], t, SA[t]['feedback']) for t in pool if acc(SB[t]) and not acc(SA[t])],
        'still_rejected': still}
res = {'note': '§6 AFTER all four reviews (syn_1/2, lib_1..6, sample, supp) applied to phase1c copies; checker v2 unchanged. Same split and '
               'denominator as measure_before.json (held-out cov_heldout.json 240 − 5 excluded = 235; FA fa.json 105).',
       'coverage_before': before['coverage'], 'coverage_after': cov(after),
       'false_acceptance': {'total_wrong': len(fa_rows), 'accepted': len(fal), 'silent_correct': sum(x['verdict'] == 'correct' for x in fal),
                            'tip_accepts': sum(x['verdict'] == 'correct_with_tip' for x in fal), 'new_vs_before': sum(x['class'] == 'NEW' for x in fal), 'real': 0,
                            'real_note': 'same 9 rows as before, same judgements: 3 silent = valid readings of the Slovak, 6 tip-accepts via library soft items; 0 real (1b convention), 6/105 if tip-accepts count',
                            'list': fal},
       'false_rejections': {'count': len(fr), 'by_category': dict(Counter(x['category'] for x in fr).most_common()),
                            'all_issue_categories': dict(Counter(c for x in fr for c in x['categories']).most_common()),
                            'regressions_vs_before': [x for x in fr if x['regression']], 'list': fr},
       'supp_fix_split': supp,
       'apply_log': {k: v for k, v in rj('phase1c/review/applied.json').items() if k in ('by_target_op', 'errors', 'irr_normalised', 'groups')}}
if len(sys.argv) > 1:
    nd = sys.argv[1]; nr = rj(os.path.join(nd, 'cov.json'))['rows']; ns = {r['answer']: r for r in rj(os.path.join(nd, 'supp_fix.json'))['rows']}
    res['effect_split'] = {'note': 'syn+lib+sample reviews only (no supp.json) vs all four; held-out coverage and in-sample fix split',
                           'heldout_review_only': cov(nr)['all'], 'heldout_all_four': res['coverage_after']['all'], 'heldout_before': before['coverage']['all'],
                           'fix_split_review_only': sum(acc(ns[t]) for t in pool), 'fix_split_all_four': supp['accepted_after'], 'fix_split_before': supp['accepted_before'],
                           'fa_accepted_review_only': sum(acc(r) for r in rj(os.path.join(nd, 'fa.json'))['rows'])}
t = rj(M + 'timing_after.json'); s = rj(M + 'sizes_after.json')
res['timing'] = {k: t[k] for k in ('exercises', 'answers_per_exercise', 'runs', 'checks', 'ms_all', 'ms_warm_runs', 'compile_ms', 'worst', 'largest_graph')}
res['timing']['script'] = 'phase1c/scripts/timing_all.ts'
res['download_per_exercise'] = {**s['per_exercise_download'], 'note': 'bytes of {annotation, library_sk items, forms of used groups, neighbours} per exercise (measure.ts sizes, AFTER data)'}
res['raw_files'] = [M + f for f in ('cov_after.json', 'fa_after.json', 'supp_fix_after.json', 'timing_after.json', 'sizes_after.json')]
json.dump(res, open('phase1c/measure_after.json', 'w'), ensure_ascii=False, indent=1)
print(json.dumps({'after': res['coverage_after'], 'fa': len(fal), 'fr': res['false_rejections']['by_category'], 'supp': {k: supp[k] for k in ('pct_before', 'pct_after', 'targeted_rejections_fixed', 'wrong_accepted_after')}, 'split': res.get('effect_split')}, ensure_ascii=False))

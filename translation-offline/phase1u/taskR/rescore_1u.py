#!/usr/bin/env python3
"""Phase 1U task R: A re-score of the closed 1T set (article omission = ERROR), B sensitivity
reconciliation from the RAW verdict files, C minimal-pair probe of the 18 article answers."""
import json, os, sys, math, time, copy, shutil, traceback, collections

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
P1T  = os.path.join(ROOT, 'phase1t'); RUN = os.path.join(P1T, 'run'); SET = os.path.join(P1T, 'set')
TASKR = os.path.join(ROOT, 'phase1u', 'taskR'); os.makedirs(TASKR, exist_ok=True)
LEDGER = os.path.join(ROOT, 'phase1u', 'ledger_dev.jsonl')
DO_C = '--noc' not in sys.argv

# ---------- exact stats, no scipy ----------
def bincdf(k, n, p):                       # P(X<=k)
    return sum(math.comb(n, i) * p**i * (1-p)**(n-i) for i in range(0, k+1))
def cp(k, n, a=0.05):
    if n == 0: return (0.0, 0.0)
    def bis(f, lo, hi):
        for _ in range(200):
            m = (lo+hi)/2
            if f(m) > 0: hi = m
            else: lo = m
        return (lo+hi)/2
    lo = 0.0 if k == 0 else bis(lambda p: (1 - bincdf(k-1, n, p)) - a/2, 0.0, 1.0)
    hi = 1.0 if k == n else bis(lambda p: -(bincdf(k, n, p) - a/2), 0.0, 1.0)
    return (100*lo, 100*hi)
def fisher(a, b, c, d):                    # 2x2 two-sided
    n = a+b+c+d; r1 = a+b; c1 = a+c
    def pr(x): return math.comb(r1, x)*math.comb(n-r1, c1-x)/math.comb(n, c1)
    p0 = pr(a); lo = max(0, c1-(n-r1)); hi = min(r1, c1)
    return sum(pr(x) for x in range(lo, hi+1) if pr(x) <= p0*(1+1e-9))
def fig(k, n):
    l, h = cp(k, n); return '%d/%d = %.2f %% [%.2f, %.2f]' % (k, n, 100*k/n if n else 0, l, h)

# ---------- raw data ----------
rows  = json.load(open(os.path.join(RUN, 'results_1t.json')))['rows']
items = {i['id']: i for i in json.load(open(os.path.join(SET, 'data', 'items.json')))}
sents = {s['sid']: s for s in json.load(open(os.path.join(SET, 'data', 'sentences.json')))}
key   = json.load(open(os.path.join(SET, 'judge', '_private', '_key.json')))
Vprim, Vany, vrowsall = {}, {}, []
for p in 'P1 P2 P3 P4'.split():
    for v in json.load(open(os.path.join(SET, 'judge', 'verdicts_%s.json' % p))):
        k = key[v['jid']]; vrowsall.append((v, k))
        Vany.setdefault(k['item'], v)
        if not k.get('duplicate_of') or k['item'] not in Vprim: Vprim[k['item']] = v
R = {r['item_id']: r for r in rows}
lab = [r for r in rows if r.get('judged') in ('correct', 'wrong')]
acc = lambda r: bool(r['final_accept'])
half = lambda r: r['half']
art = [r['item_id'] for r in rows if 'article' in (Vprim[r['item_id']].get('note') or '').lower()]

def covfa(judfn, pool=None):
    pool = pool if pool is not None else lab
    c = [r for r in pool if judfn(r) == 'correct']; w = [r for r in pool if judfn(r) == 'wrong']
    return sum(map(acc, c)), len(c), sum(map(acc, w)), len(w)
def block(name, judfn, pool=None, out=None):
    a = covfa(judfn, pool); out.append('| %s | %s | %s |' % (name, fig(a[0], a[1]), fig(a[2], a[3]))); return a

O = []; P = O.append
P('# RESCORE_1U (Phase 1U, task R) — re-score of a CLOSED set\n')
P('Source: phase1t/run/results_1t.json + phase1t/set/judge/verdicts_P{1..4}.json + _key.json (raw).')
P('Intervals: exact Clopper-Pearson 95 %% (own implementation). Fisher: two-sided exact.\n')

# ================= A =================
P('## A. Article omission scored WRONG (owner ruling, brief §1.2) — re-score of a closed set\n')
prim = lambda r: r['judged']
ART = set(art)
sart = lambda r: 'wrong' if r['item_id'] in ART else r['judged']
P('| scoring | coverage | FA |'); P('|---|---|---|')
ap = block('1T primary (published)', prim, out=O)
bp = block('A: S-art re-score (18 article answers = WRONG)', sart, out=O)
for h in ('P1', 'P2'):
    pool = [r for r in lab if r['half'] == h]
    block('A: %s (%s sid)' % (h, 'odd' if h == 'P1' else 'even'), sart, pool, O)
    block('1T primary %s' % h, prim, pool, O)
p1 = [r for r in lab if r['half'] == 'P1']; p2 = [r for r in lab if r['half'] == 'P2']
a1 = covfa(sart, p1); a2 = covfa(sart, p2)
P('')
P('Fisher (A re-score) coverage P1 vs P2: accepted %d/%d vs %d/%d, p = %.4f'
  % (a1[0], a1[1], a2[0], a2[1], fisher(a1[0], a1[1]-a1[0], a2[0], a2[1]-a2[0])))
P('Fisher (A re-score) FA P1 vs P2: %d/%d vs %d/%d, p = %.4f'
  % (a1[2], a1[3], a2[2], a2[3], fisher(a1[2], a1[3]-a1[2], a2[2], a2[3]-a2[2])))
P('\nBrief expectation: coverage 388/403 = 96.28 %% [93.94, 97.90], FA 17/497 = 3.42 %% [2.00, 5.42].')
P('ACTUAL from the raw files: coverage %s, FA %s.' % (fig(bp[0], bp[1]), fig(bp[2], bp[3])))
P('\n### the 18 "article omission only" items (judge note match, raw verdicts)\n')
P('| # | id | level/half | stack layer | model verdict | accepted | Slovak | answer |')
P('|---|---|---|---|---|---|---|---|')
for n, iid in enumerate(sorted(ART), 1):
    r = R[iid]
    P('| %d | %s | %s %s | %s | %s | %s | %s | %s |' % (n, iid, r['level'], r['half'],
      r['layers']['main_layer'], r['layers'].get('model'), 'YES' if acc(r) else 'no',
      sents[r['sid']]['slovak'], items[iid]['answer']))
lc = collections.Counter(R[i]['layers']['main_layer'] for i in ART)
P('\nlayer breakdown: %s · accepted by the stack: %d · rejected: %d'
  % (dict(lc), sum(acc(R[i]) for i in ART), sum(not acc(R[i]) for i in ART)))

# ================= B =================
P('\n## B. Sensitivity table reconciled from the RAW files (brief §3)\n')
bl_prim = {i: bool(Vprim[i].get('borderline')) for i in R}
bl_row  = {i: bool(R[i].get('borderline')) for i in R}
bl_any  = {i: any(v.get('borderline') for v, k in vrowsall if k['item'] == i) for i in R}
jc_b = [i for i in R if R[i]['judged'] == 'correct' and bl_prim[i]]
jw_b = [i for i in R if R[i]['judged'] == 'wrong' and bl_prim[i]]
nrows_b = sum(1 for v, k in vrowsall if v.get('borderline'))
dupdiff = [i for i in R if bl_prim[i] != bl_any[i]]
rowdiff = [i for i in R if bl_prim[i] != bl_row[i]]
P('true borderline counts (primary verdict per item, duplicates dropped):')
P('- judged-correct borderline: **%d**' % len(jc_b))
P('- judged-wrong borderline:   **%d**' % len(jw_b))
P('- total unique borderline items: **%d**' % (len(jc_b)+len(jw_b)))
P('- borderline verdict ROWS incl. duplicate judgements: **%d** (duplicate jids in the key: %d)'
  % (nrows_b, sum(1 for k in key.values() if k.get('duplicate_of'))))
P('- items whose duplicate judgement disagrees on the borderline flag: %d %s'
  % (len(dupdiff), sorted(dupdiff)))
P('- items where results_1t.json row["borderline"] != primary verdict borderline: %d %s'
  % (len(rowdiff), sorted(rowdiff)))
P('')
P('| scenario | coverage | FA |'); P('|---|---|---|')
block('primary', prim, out=O)
s2 = block('S2-wide (judged-wrong borderline -> correct)',
           lambda r: 'correct' if (r['judged'] == 'wrong' and bl_prim[r['item_id']]) else r['judged'], out=O)
block('S-art (A)', sart, out=O)
s3 = block('S3 (judged-correct borderline -> wrong)',
           lambda r: 'wrong' if (r['judged'] == 'correct' and bl_prim[r['item_id']]) else r['judged'], out=O)
nb = [r for r in lab if not bl_prim[r['item_id']]]
s5 = block('S5 (borderline excluded)', prim, nb, O)
P('')
P('published 1T: S2-wide 390/436 & 15/464 · S3 and S5 coverage denominator 384')
P('recomputed:   S2-wide %d/%d & %d/%d · S3 coverage n=%d · S5 coverage n=%d'
  % (s2[0], s2[1], s2[2], s2[3], s3[1], s5[1]))
P('arithmetic check: 421 + %d judged-wrong borderline = %d; 479 - %d = %d; 421 - %d judged-correct '
  'borderline = %d' % (len(jw_b), 421+len(jw_b), len(jw_b), 479-len(jw_b), len(jc_b), 421-len(jc_b)))

# ================= C =================
P('\n### cause\n\nThe published 1T sensitivity NUMBERS are correct: S2-wide 390/436 and 15/464, S3 and S5 coverage\nn = 384 all reproduce exactly from the raw verdict files. What is wrong is the prose borderline\nCOUNTS the report and analysis_1t.py put on them: the true figures are 37 judged-correct and\n15 judged-wrong borderline items, 52 unique borderline items in all — not 38 / 17 / 55.\n\n* analysis_1t.py **line 37** — `P(\'S2-wide (all 17 judged-wrong borderline items scored correct)...\')`\n  — the label says 17 while the very computation on that line (`bw`, line 36) moves 15. The number\n  17 was carried over from the "21 S-intent answers judged correct" narrative, not counted.\n* The 55 in "55 borderline flags" counts borderline VERDICT ROWS across verdicts_P1..P4\n  (55 rows), i.e. duplicate judgements included: the key holds 80 duplicate jids. The de-duplication\n  at analysis_1t.py **line 14** (`if not k.get(\'duplicate_of\') or k[\'item\'] not in V`) is itself\n  sound — 0 items disagree between their primary and duplicate borderline flag, and 0 items\n  disagree with `results_1t.json` row["borderline"] — so only the counting of the flags, done\n  before the de-duplication, is off. 52 unique items carry the flag.\n* 421 - 37 = 384 (S3 / S5 coverage denominator, as published) and 421 + 15 = 436, 479 - 15 = 464\n  (S2-wide, as published). There is no off-by-one and no double count in the figures themselves.\n')
P('\n## C. Minimal pairs: is the article the reason the stack rejects? (brief §1.3)\n')
pairs = json.load(open(os.path.join(TASKR, 'article_pairs.json')))['pairs']
cinfo = {'made': 0, 'failed': 0, 'tin': 0, 'tout': 0, 'mode': None, 'error': None, 'res': {}}
def led(item, http, counted, reply, tin, tout, extra=None):
    rec = {'ts': time.time(), 'agent': 'rescore', 'item': item, 'http': http, 'counted': counted,
           'reply': reply, 'tokens_in': tin, 'tokens_out': tout}
    if extra: rec.update(extra)
    with open(LEDGER, 'a', encoding='utf-8') as f: f.write(json.dumps(rec, ensure_ascii=False)+'\n')
if DO_C:
  try:
    wd = os.path.join(TASKR, 'rundir'); os.makedirs(wd, exist_ok=True)
    for f in ('FROZEN_CONFIG_1T.json', 'FREEZE_HASH', 'FREEZE_FILES'):
        if not os.path.exists(os.path.join(wd, f)): shutil.copy(os.path.join(RUN, f), wd)
    data2 = os.path.join(TASKR, 'data_restored')
    if os.path.exists(data2): shutil.rmtree(data2)
    shutil.copytree(os.path.join(SET, 'data'), data2)
    it2 = json.load(open(os.path.join(data2, 'items.json')))
    pm = {p['id']: p for p in pairs}
    for i in it2:
        if i['id'] in pm:
            assert i['answer'] == pm[i['id']]['bare'], (i['id'], i['answer'])
            i['answer'] = pm[i['id']]['restored']
    json.dump(it2, open(os.path.join(data2, 'items.json'), 'w'), ensure_ascii=False, indent=1)
    sys.path.insert(0, RUN)
    import runner_1t as R1T
    R1T.set_run_dir(wd)
    sel = R1T.load_cfg()
    res = R1T.build(data2, R1T.SIDE_TAG, 'Phase 1U taskR minimal pairs')
    if not isinstance(res, (tuple, list)): res = (res,)
    recs = [x for x in res if isinstance(x, list) and x and isinstance(x[0], dict)
            and 'item_id' in x[0]][0]
    cands = [x for x in res if isinstance(x, dict) and 'C' in x]
    if not cands:
        raise SystemExit('build() returned %s ; dict keys: %s' % ([type(x).__name__ for x in res],
                         [sorted(x)[:12] for x in res if isinstance(x, dict)]))
    st = cands[0]
    R1P = R1T.R1P; RL = R1T.RL
    ids = [p['id'] for p in pairs]
    req, hmap = R1P.plan(st, recs, ids, R1T.PROMPT)
    cinfo['mode'] = 'rebuilt from restored answers through the frozen 1T build_req'
    keys = RL.load_keys(); k0 = keys[0]
    streak = 0
    for iid in ids:
        if cinfo['made'] >= 40 or streak >= 5: break
        row = RL.call_one(req[hmap[iid]], k0)
        http = row.get('http'); rep = (row.get('reply') or '').strip()
        counted = (http == 200)
        tin = row.get('prompt_tokens') or 0; tout = row.get('candidates_tokens') or 0
        if counted:
            cinfo['made'] += 1; cinfo['tin'] += tin; cinfo['tout'] += tout; streak = 0
            if not rep: cinfo['failed'] += 1
        else:
            streak += 1
        led(iid, http, counted, rep, tin, tout, {'verdict': row.get('verdict'), 'try': row.get('try')})
        cinfo['res'][iid] = {'http': http, 'reply': rep, 'verdict': row.get('verdict')}
  except Exception as e:
    cinfo['error'] = traceback.format_exc()[-1500:]
    P('```\nC FAILED: %s\n```' % cinfo['error'])
P('mode: %s · model calls counted (http 200): %d · failed (empty/unparsable 200): %d · '
  'tokens in %d / out %d\n' % (cinfo['mode'], cinfo['made'], cinfo['failed'], cinfo['tin'], cinfo['tout']))
P('| id | bare answer verdict (1T, stored) | stack layer | restored answer verdict (new call) | article is the cause? | added |')
P('|---|---|---|---|---|---|')
cause = 0
for p in pairs:
    r = R[p['id']]; bare = r['layers'].get('model'); res = cinfo['res'].get(p['id'], {})
    new = res.get('verdict') or res.get('reply') or '(no call)'
    is_cause = (bare in ('TIP', 'DIFF')) and new == 'SAME'
    cause += bool(is_cause)
    P('| %s | %s | %s | %s | %s | %s |' % (p['id'], bare, r['layers']['main_layer'], new,
      'YES' if is_cause else ('n/a (bare SAME)' if bare == 'SAME' else 'NO'), p['added']))
P('\n**the article is the cause in %d of %d.**' % (cause, len(pairs)))
still = [p['id'] for p in pairs if (cinfo['res'].get(p['id'], {}).get('verdict') not in (None, 'SAME'))
         and R[p['id']]['layers'].get('model') in ('TIP', 'DIFF')]
P('restored answer still TIP/DIFF: %s' % (still or 'none'))
P('\n### the 21 S-intent answers judged CORRECT — the 3 the stack ACCEPTED\n')
s21 = [r for r in lab if r.get('intent') == 'S' and r['judged'] == 'correct']
P('n = %d, accepted %d' % (len(s21), sum(map(acc, s21))))
P('| id | layer | model | Slovak | answer | judge note |'); P('|---|---|---|---|---|---|')
for r in s21:
    if acc(r):
        P('| %s | %s | %s | %s | %s | %s |' % (r['item_id'], r['layers']['main_layer'],
          r['layers'].get('model'), sents[r['sid']]['slovak'], items[r['item_id']]['answer'],
          Vprim[r['item_id']].get('note')))
open(os.path.join(TASKR, 'RESCORE_1U.md'), 'w', encoding='utf-8').write('\n'.join(O)+'\n')
print('\n'.join(O))

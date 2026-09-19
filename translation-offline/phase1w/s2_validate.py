#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phase 1W §2.2 + §2.3: reader validation (Track B 60, 1T 120 pairs) and the regression gate
(1S packet, closed 1U/1T re-scored from STORED verdicts). 0 model calls. Writes S2_RESULT.md + s2_result.json."""
import os, re, sys, json, hashlib, contextlib
sys.dont_write_bytecode = True
BASE = os.path.expanduser("~/Projects/and-again-content/translation-offline")
HERE = os.path.join(BASE, 'phase1w')
WATCH = ['phase1s/taskC/agent_drop_v2.py', 'phase1t/taskA/agent_drop_v3.py', 'phase1u/taskA/agent_drop_v4.py',
         'phase1u/taskA/gate_v4.py', 'phase1v/trackA_loop/stack_1v.py', 'phase1v/trackA_loop/loop_1v.py',
         'phase1n/f9.py', 'phase1i/checker_1i.py', 'phase1v/trackC/cz_reader.py',
         'phase1v/trackB/trackb_results.json', 'phase1u/run/results_1u.json', 'phase1t/taskB/cz_gold.json',
         'phase1t/taskB/sk_gold.json', 'phase1s/taskC/judge/verdicts.json']
sha = lambda r: hashlib.sha256(open(os.path.join(BASE, r), 'rb').read()).hexdigest()
H0 = {r: sha(r) for r in WATCH}
sys.path.insert(0, os.path.join(BASE, 'phase1v', 'trackA_loop'))
import loop_1v as L1V                                                          # noqa: E402
S, G = L1V.S, L1V.G
V2, V3 = G.V2, G.V3
sys.path.insert(0, HERE)
import reader_nom as R                                                         # noqa: E402
sys.path.insert(0, os.path.join(BASE, 'phase1v', 'trackC'))
import cz_reader as CZR                                                        # noqa: E402
OLD_SA = V2.slovak_agent
VARIANTS = ('full', 'pron')
cp = L1V.cp
WORD = re.compile(r"[a-záäčďéěíĺľňóôöŕřšťúůüýž]+", re.I)
words = lambda s: set(WORD.findall((s or '').lower()))


def g3cls(agent, g, v3m):
    toks_ = v3m.parse_agent_tokens(agent)[0] if agent else []
    gm = words(g.get('subject'))
    ga = set(gm)
    for e in (g.get('embedded_agents') or []):
        ga |= words(e)
    low = {x.lower().strip(".,!?;:„“\"'") for x in toks_ if x}
    if not agent:
        return 'CONSERVATIVE' if gm else 'AGREE'
    if not ga:
        return 'ERROR'
    return 'AGREE' if low & gm else 'ERROR'


def cnt(lst):
    c = {'AGREE': 0, 'CONSERVATIVE': 0, 'ERROR': 0}
    for x in lst:
        c[x] += 1
    n = len(lst)
    c['n'] = n; c['ERROR_pct'] = round(100.0 * c['ERROR'] / n, 2); c['ERROR_ci'] = cp(c['ERROR'], n)
    return c


OUT = {'phase': '1W §2', 'gemini_calls': 0, 'model_calls': 0}
# ------------------------------------------------------------------ 2.2a Track B 60 production sentences
tb = json.load(open(os.path.join(BASE, 'phase1v/trackB/trackb_results.json'), encoding='utf-8'))['rows']
TB, TBERR = {}, {}
for state, tk, gk in (('raw', 'sk_raw', 'gold_before'), ('rewritten', 'sk_new', 'gold_after')):
    rec = {'before': []}; rec.update({v: [] for v in VARIANTS}); TBERR[state] = {k: [] for k in rec}
    for r in tb:
        text, g = r[tk], r[gk]
        a0 = OLD_SA(text, {}, {})[0]
        c0 = g3cls(a0, g, V3); rec['before'].append(c0)
        if c0 == 'ERROR':
            TBERR[state]['before'].append([r['n'], a0])
        for v in VARIANTS:
            a, info = R.read(text, 'sk', v)
            c = g3cls(a, g, V3); rec[v].append(c)
            if c == 'ERROR':
                TBERR[state][v].append([r['n'], text[:100], a, g.get('subject'), g.get('embedded_agents'), info.get('why')])
    TB[state] = {k: cnt(v) for k, v in rec.items()}
OUT['trackB'] = TB; OUT['trackB_errors'] = TBERR
# ------------------------------------------------------------------ 2.2b 1T 120 Czech/Slovak pairs
cz = CZR.build(CZR.ALL_FIXES)
rows1t = json.load(open(os.path.join(BASE, 'phase1t/taskB/cz_sample_numbered.json'), encoding='utf-8'))
gold = {'cz': {g['n']: g for g in json.load(open(os.path.join(BASE, 'phase1t/taskB/cz_gold.json'), encoding='utf-8'))},
        'sk': {g['n']: g for g in json.load(open(os.path.join(BASE, 'phase1t/taskB/sk_gold.json'), encoding='utf-8'))}}
T1, T1ERR = {}, {}
for lang, oldsa, v3m, mods in (('cz', cz['V2'].slovak_agent, cz['V3'], cz), ('sk', OLD_SA, V3, None)):
    rec = {'before': []}; rec.update({v: [] for v in VARIANTS}); T1ERR[lang] = {v: [] for v in VARIANTS}
    for r in rows1t:
        text, g = r[lang], gold[lang][r['n']]
        rec['before'].append(g3cls(oldsa(text, {}, {})[0], g, v3m))
        for v in VARIANTS:
            a, info = R.read(text, lang, v, mods)
            c = g3cls(a, g, v3m); rec[v].append(c)
            if c == 'ERROR':
                T1ERR[lang][v].append([r['n'], text[:100], a, g.get('subject'), info.get('why')])
    T1[lang] = {k: cnt(v) for k, v in rec.items()}
OUT['pairs_1T'] = T1; OUT['pairs_1T_errors'] = T1ERR
OUT['reproduction'] = {'trackB_raw_before_ERROR': TB['raw']['before']['ERROR'], 'want_1V': 30,
                       'trackB_rewritten_before_ERROR': TB['rewritten']['before']['ERROR'], 'want_1V_rw': 20,
                       '1T_sk_before_ERROR': T1['sk']['before']['ERROR'], 'want_sk': 47,
                       '1T_cz_before_ERROR': T1['cz']['before']['ERROR'], 'want_cz_after_4fixes': 45}
# ------------------------------------------------------------------ 2.3 closed sets from stored verdicts
u = L1V.load_1u()
t, tnotes, _ = L1V.load_1t()
raw_u = {r['item_id']: r for r in json.load(open(os.path.join(BASE, 'phase1u/run/results_1u.json')))['rows']}


def _idx(x, key):
    return {str(e.get(key)): e for e in x} if isinstance(x, list) else {str(k): v for k, v in x.items()}


udata = None
for d in ('phase1u/set/data', 'phase1u/data', 'phase1u/taskR/data_restored'):
    p = os.path.join(BASE, d)
    try:
        items = _idx(json.load(open(os.path.join(p, 'items.json'))), 'id')
        sents = _idx(json.load(open(os.path.join(p, 'sentences.json'))), 'sid')
        ann = json.load(open(os.path.join(p, 'annotations.json'))) if os.path.exists(os.path.join(p, 'annotations.json')) else {}
    except Exception:
        continue
    if sum(1 for r in u if str(r['id']) in items) >= 0.9 * len(u):
        udata = (d, items, sents, ann); break
for r in u:
    r['ann'], r['wt'] = {}, {}
    if udata:
        d, items, sents, ann = udata
        it = items.get(str(r['id'])) or {}
        sid = raw_u[r['id']].get('sid') or it.get('sid')
        s = sents.get(str(sid)) or {}
        r['ann'] = (ann.get(str(sid)) or {}) if isinstance(ann, dict) else {}
        r['wt'] = (s.get('tags') or {}).get('writer_tags') or {}
OUT['closed_1U_ann_source'] = udata[0] if udata else 'none (ann={} production mode)'
SETS = {'1U': u, '1T': t}


def fires(rows, variant):
    out = {}
    ctx = R.installed(V2, 'sk', variant) if variant else contextlib.nullcontext()
    with ctx:
        for r in rows:
            try:
                out[r['id']] = bool(S.ORIG_V4_DECIDE(r['sk'], r['ann'] or {}, r['wt'] or {}, r['answer'],
                                                     r['reference'])['fired'])
            except Exception:
                out[r['id']] = None
    return out


def rescore(rows, old_re, new_re, worst=True):
    res, newf, unf = [], [], []
    for r in rows:
        o, nn = old_re[r['id']], new_re[r['id']]
        eff = r['v4'] if (nn is None or o is None or nn == o) else nn
        acc, lay = r['acc0'], r['layer0']
        if eff and not r['v4'] and acc:
            acc, lay = False, 'AGv6'; newf.append(r)
        if r['v4'] and not eff and not acc and 'AG' in str(lay):
            unf.append(r)
            if (worst and r['judged'] == 'wrong') or (not worst and r['judged'] == 'correct'):
                acc, lay = True, 'AGv6-unfire'
        if acc and not eff and S.refsubj(r['sk'], r['answer'], r['reference'], ('rs_nom',)):
            acc, lay = False, 'AGv5'
        if (not acc) and S.tip_det_rule(r['sk'], r['answer'], r['reference'], lay):
            acc, lay = True, 'TIPdet'
        res.append(dict(r, acc=acc, layer=lay))
    return res, newf, unf


def fig(m):
    return '%d/%d = %.2f %% [%.2f, %.2f]' % (m['k'], m['n'], m['pct'], m['ci'][0], m['ci'][1])


CL = {'baseline_1V_round2': {}}
old = {k: fires(v, None) for k, v in SETS.items()}
for k, v in SETS.items():
    m = L1V.metrics(L1V.apply(v, ('rs_nom',), True)[0])
    CL['baseline_1V_round2'][k] = {'coverage': m['coverage'], 'FA': m['FA'],
                                   'recompute_mismatch_vs_stored_v4': sum(1 for r in v if old[k][r['id']] != r['v4'])}
WANT = {'1U': ((390, 402), (13, 498)), '1T': ((394, 421), (9, 479))}
PK = {'baseline_1V_round2': L1V.packet(('rs_nom',))}
for var in VARIANTS:
    CL[var] = {}
    for k, v in SETS.items():
        nw = fires(v, var)
        resw, newf, unf = rescore(v, old[k], nw, True)
        resb, _, _ = rescore(v, old[k], nw, False)
        mw, mb = L1V.metrics(resw), L1V.metrics(resb)
        cost = [r['id'] for r in newf if r['judged'] == 'correct'] + [r['id'] for r in unf if r['judged'] == 'wrong']
        (ck, cn), (fk, fn) = WANT[k]
        cov_ok = mw['coverage']['k'] * cn >= ck * mw['coverage']['n']
        fa_ok = mw['FA']['k'] * fn <= fk * mw['FA']['n']
        CL[var][k] = {'coverage_worst': mw['coverage'], 'FA_worst': mw['FA'], 'coverage_best': mb['coverage'],
                      'FA_best': mb['FA'], 'new_fires': len(newf),
                      'new_catches': [r['id'] for r in newf if r['judged'] == 'wrong'],
                      'unfires': len(unf), 'unfire_ids': [(r['id'], r['judged']) for r in unf],
                      'measured_cost': len(cost), 'cost_ids': cost,
                      'cost_detail': [(r['id'], r['sk'], r['answer']) for r in newf if r['judged'] == 'correct'],
                      'gate_coverage': cov_ok, 'gate_FA': fa_ok}
    with R.installed(V2, 'sk', var):
        PK[var] = L1V.packet(('rs_nom',))
OUT['closed'] = CL; OUT['packet_1S'] = {k: {'gate_pass': v[0], 'counts': v[1]} for k, v in PK.items()}
# ------------------------------------------------------------------ selection + decision
DK, BK, PL = 'agent drops (judged wrong)', 'by-passive controls', 'plain controls (judged correct)'
SEL = {}
for var in VARIANTS:
    pc = PK[var][1]
    lines = {'1S drops caught >= 96/97': pc.get(DK, {}).get('fired', 0) >= 96,
             '1S by-passive controls rejected 0/42': pc.get(BK, {}).get('fired', 1) == 0,
             '1S plain controls rejected 0/39': pc.get(PL, {}).get('fired', 1) == 0,
             '1U coverage >= 390/402': CL[var]['1U']['gate_coverage'], '1U FA <= 13/498': CL[var]['1U']['gate_FA'],
             '1T coverage >= 394/421': CL[var]['1T']['gate_coverage'], '1T FA <= 9/479': CL[var]['1T']['gate_FA']}
    SEL[var] = {'gate_lines': lines, 'gate_pass': all(lines.values()),
                'closed_cost': CL[var]['1U']['measured_cost'] + CL[var]['1T']['measured_cost'],
                'trackB_raw_ERROR': TB['raw'][var]['ERROR'], 'trackB_raw_ERROR_pct': TB['raw'][var]['ERROR_pct']}
elig = [v for v in VARIANTS if SEL[v]['gate_pass']]
chosen = min(elig, key=lambda v: (SEL[v]['closed_cost'], SEL[v]['trackB_raw_ERROR'])) if elig else None
if chosen is None:
    decision = 'NOT FREEZE-ELIGIBLE (no reader variant passes the regression gate; stack stays on the 1V reader)'
elif SEL[chosen]['trackB_raw_ERROR_pct'] > 15:
    decision = 'NOT FREEZE-ELIGIBLE (NOT FROZEN: raw production Slovak ERROR %.2f %% > 15 %%)' % SEL[chosen]['trackB_raw_ERROR_pct']
elif SEL[chosen]['trackB_raw_ERROR_pct'] >= 10:
    decision = 'FREEZE-ELIGIBLE, target MISSED (raw production Slovak ERROR %.2f %%, target < 10 %%, above-15 %% stop not hit)' % SEL[chosen]['trackB_raw_ERROR_pct']
else:
    decision = 'FREEZE-ELIGIBLE (raw production Slovak ERROR %.2f %% < 10 %% target, gate PASS)' % SEL[chosen]['trackB_raw_ERROR_pct']
OUT['selection'] = SEL; OUT['chosen_variant'] = chosen; OUT['decision'] = decision
OUT['stack_entry_point'] = {'file': 'translation-offline/phase1w/stack_1w.py',
                            'decide': 'stack_1w.decide(sk, ann, wtags, answer, reference, variant="primary", flags=None, extra=("rs_nom",))',
                            'final_accept': 'stack_1w.final_accept(row, extra=("rs_nom",), tip=True)',
                            'reader': 'phase1w/reader_nom.py installed(v2mod, lang, variant) / read(sk, lang, variant, mods)'}
H1 = {r: sha(r) for r in WATCH}
OUT['earlier_phase_files_unchanged'] = H0 == H1
OUT['gold_circularity'] = ('Track B gold (phase1v/trackB/trackb.py GOLD) was written by the same 1V agent that wrote the '
                           'rewrite and annotation; it is not blind. The Track B figures here are therefore validated '
                           'against a single non-blind annotator. The 1T 120-pair gold is blind (separate annotators).')
json.dump(OUT, open(os.path.join(HERE, 's2_result.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1, default=str)
# ------------------------------------------------------------------ markdown
c3 = lambda c: '%d / %d / %d, ERROR %.2f %% [%.2f, %.2f]' % (c['AGREE'], c['CONSERVATIVE'], c['ERROR'], c['ERROR_pct'], c['ERROR_ci'][0], c['ERROR_ci'][1])
md = ['# Phase 1W §2 result: nominative-subject agent reader (0 Gemini calls, 0 model calls)', '',
      '- Decision: **%s**' % decision,
      '- Chosen reader variant: %s' % chosen,
      '- Stack entry point for §3/§4 ("1V round 2 + §2"): `translation-offline/phase1w/stack_1w.py`, functions `decide(sk, ann, wtags, answer, reference, variant="primary", flags=None, extra=("rs_nom",))` and `final_accept(row, extra=("rs_nom",), tip=True)`',
      '- Reader module: `translation-offline/phase1w/reader_nom.py` (`read`, `installed`); earlier phase dirs not edited, hashes unchanged: %s' % OUT['earlier_phase_files_unchanged'],
      '- Gold caveat: %s' % OUT['gold_circularity'], '',
      '## 2.2 Agent reader, AGREE / CONSERVATIVE / ERROR (g3, v3 token parse; before = 1V round-2 first-word reader)', '']
for state in ('raw', 'rewritten'):
    for k in ('before',) + VARIANTS:
        md.append('- Track B Slovak %s (n = 60), %s: %s' % (state, k if k != 'before' else 'BEFORE', c3(TB[state][k])))
for k in ('before',) + VARIANTS:
    for lang in ('cz', 'sk'):
        md.append('- 1T pairs %s (n = 120), %s: %s' % ('Czech (4 fixes)' if lang == 'cz' else 'Slovak control', k if k != 'before' else 'BEFORE', c3(T1[lang][k])))
md.append('- Reproduction of 1V figures (before): %s' % json.dumps(OUT['reproduction']))
md += ['', '## 2.3 Regression gate (stored verdicts, 0 calls; worst case = an un-fired AG reject on a judged-wrong row counts as accepted)', '']
b = CL['baseline_1V_round2']
for k in ('1U', '1T'):
    md.append('- %s baseline 1V round 2 re-scored: coverage %s' % (k, fig(b[k]['coverage'])))
    md.append('- %s baseline 1V round 2 re-scored: FA %s' % (k, fig(b[k]['FA'])))
    md.append('- %s old-reader recompute mismatches vs stored AG: %d' % (k, b[k]['recompute_mismatch_vs_stored_v4']))
md.append('- 1S packet baseline: %s' % json.dumps(PK['baseline_1V_round2'][1]))
for var in VARIANTS:
    md.append('- [%s] 1S packet: %s' % (var, json.dumps(PK[var][1])))
    for k in ('1U', '1T'):
        c = CL[var][k]
        md.append('- [%s] %s coverage (worst) %s' % (var, k, fig(c['coverage_worst'])))
        md.append('- [%s] %s FA (worst) %s' % (var, k, fig(c['FA_worst'])))
        md.append('- [%s] %s coverage (best) %s' % (var, k, fig(c['coverage_best'])))
        md.append('- [%s] %s FA (best) %s' % (var, k, fig(c['FA_best'])))
        md.append('- [%s] %s new AG fires %d, catches %d, un-fires %d, measured cost %d %s' % (var, k, c['new_fires'], len(c['new_catches']), c['unfires'], c['measured_cost'], c['cost_ids']))
    for ln, ok in SEL[var]['gate_lines'].items():
        md.append('- [%s] GATE %s: %s' % (var, ln, 'PASS' if ok else 'FAIL'))
    md.append('- [%s] GATE overall: %s' % (var, 'PASS' if SEL[var]['gate_pass'] else 'FAIL'))
md += ['', '## Selection (on measured closed-set cost, then Track B raw ERROR)', '',
       '- Eligible: %s' % elig, '- Chosen: %s' % chosen, '- Decision: %s' % decision, '',
       '## Remaining ERROR rows (Track B raw, chosen / full)', '']
for e in TBERR['raw'][chosen or 'full']:
    md.append('- n=%s | %s | read %r | gold %r emb %r | %s' % tuple(e))
open(os.path.join(HERE, 'S2_RESULT.md'), 'w', encoding='utf-8').write('\n'.join(md) + '\n')
print('\n'.join(md[:80]))
print('ERR_T1', json.dumps(T1ERR, ensure_ascii=False)[:3000])
print('ERR_TB_rw', json.dumps(TBERR['rewritten'].get('full'), ensure_ascii=False)[:1500])
print('COSTDETAIL', json.dumps({v: {k: CL[v][k]['cost_detail'] for k in SETS} for v in VARIANTS}, ensure_ascii=False)[:2000])

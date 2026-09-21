#!/usr/bin/env python3
"""Phase 2I stage 6 - deterministic analysis of run/results.jsonl (0 model calls).

Numbers are computed from the stored files. The CAUSE assignments (FR_CAUSE, FA_CAUSE, P2F_CAUSE) are the
stage-6 agent's own categorisation, written down here verbatim so the tables are reproducible.
Writes analysis/ANALYSIS.md and analysis/numbers.json.
"""
import json, os, math
from collections import Counter, defaultdict

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))          # phase2i
TO = os.path.dirname(BASE)                                                  # translation-offline
P2F = os.path.join(TO, 'phase2f/p3/probe')
LEVELS = ['A1', 'A2', 'B1', 'B2']


def jl(p):
    return [json.loads(l) for l in open(p) if l.strip()]


# ------------------------------------------------------------------ exact Clopper-Pearson
def _bcdf(k, n, p):
    return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k + 1))


def cp(k, n, a=0.05):
    try:
        from scipy.stats import beta
        lo = 0.0 if k == 0 else float(beta.ppf(a / 2, k, n - k + 1))
        hi = 1.0 if k == n else float(beta.ppf(1 - a / 2, k + 1, n - k))
        return lo, hi, 'scipy.stats.beta'
    except ImportError:
        def bis(f):
            lo, hi = 0.0, 1.0
            for _ in range(200):
                m = (lo + hi) / 2
                if f(m):
                    lo = m
                else:
                    hi = m
            return (lo + hi) / 2
        lo = 0.0 if k == 0 else bis(lambda p: 1 - _bcdf(k - 1, n, p) < a / 2)
        hi = 1.0 if k == n else bis(lambda p: _bcdf(k, n, p) > a / 2)
        return lo, hi, 'exact binomial bisection'


def pct(k, n):
    return 100.0 * k / n if n else float('nan')


def esc(s):
    return str(s if s is not None else '-').replace('|', '/').replace('\n', ' ')


# ------------------------------------------------------------------ load
R = {(x['stack'], x['jid']): x for x in jl(f'{BASE}/run/results.jsonl')}
ITEMS = jl(f'{BASE}/set/items.jsonl')
LAB = {x['aid']: x for x in jl(f'{BASE}/judge/labels.jsonl')}
CTRL = json.load(open(f'{BASE}/judge/controls.json'))
INTENT = json.load(open(f'{BASE}/judge/intent_agreement.json'))
assert len(ITEMS) == 900 and len(R) == 1800
for it in ITEMS:
    assert LAB[it['aid']]['label'] == it['judge_label'], it['aid']
    assert ('tonly', it['jid']) in R and ('frozen', it['jid']) in R
BYJ = {it['jid']: it for it in ITEMS}
lock_layers = [k for k, x in R.items() if k[0] == 'frozen' and str(x['layer']).startswith('L2')]

# ------------------------------------------------------------------ causes (stage-6 categorisation)
C_DET = 'determiner or article CHOICE'
C_M1 = 'dropped FUNCTION word (M1)'
C_SYN = 'synonym or different word'
C_STR = 'structural paraphrase'
C_TNS = "English tense within the Slovak's frame"
C_VOI = 'voice or passive'
C_ORD = 'word order'
C_AG = 'AG misfire'
C_REF = 'reference wrong or too narrow'
C_JDG = 'judge label doubtful'
C_OTH = 'other'
C_F4 = 'F4v2 subject-guard misfire (extension)'
CAUSES = [C_F4, C_REF, C_SYN, C_STR, C_TNS, C_M1, C_DET, C_VOI, C_AG, C_ORD, C_JDG, C_OTH]
EXT_WHY = ("No listed cause fits: F4v2 is the Slovak-morphology SUBJECT guard (checker_1i.py:608, decide 815-820). "
           "It rejects every correct answer of 5 sentences (250, 1038, 1214, 2461, 2989), including near-verbatim "
           "copies of the reference, although each answer's subject agrees with the Slovak. 'AG misfire' names a "
           "different guard, so the extension is needed.")

SID_NOTE = {
    250: "F4v2 fires on all 4 correct answers, incl. c5 ~ reference; subject vehicle/car = 'Vozidlo'",
    1038: "F4v2 fires on all 5, incl. c1 = reference with 'My'; friend/she = 'Kamaratka ... upravila'",
    1214: "F4v2 fires on all 5; 'He' = 'Povedal'",
    2461: "F4v2 fires on all 5; 'he' = 3sg 'foti'",
    2989: "F4v2 fires on all 5, incl. c5 ~ reference; 'she' = 'dala'",
    1013: "'Do zakruty' = into the bend; both references say 'around the curve'",
    1858: "'nosila' = carry/wear; reference 'fetch' is a different verb",
    2463: "reference invents 'her brother'; 'si ... bude utahovat' is pro-drop he/she",
    2495: "F3 reports 'got' missing (has got -> has); 'got' is a function word",
}
FR_CAUSE = {
    'A:250:c1': C_F4, 'A:250:c3': C_F4, 'A:250:c4': C_F4, 'A:250:c5': C_F4,
    'A:1038:c1': C_F4, 'A:1038:c2': C_F4, 'A:1038:c3': C_F4, 'A:1038:c4': C_F4, 'A:1038:c5': C_F4,
    'A:1214:c1': C_F4, 'A:1214:c2': C_F4, 'A:1214:c3': C_F4, 'A:1214:c4': C_F4, 'A:1214:c5': C_F4,
    'A:2461:c1': C_F4, 'A:2461:c2': C_F4, 'A:2461:c3': C_F4, 'A:2461:c4': C_F4, 'A:2461:c5': C_F4,
    'A:2989:c1': C_F4, 'A:2989:c2': C_F4, 'A:2989:c3': C_F4, 'A:2989:c4': C_F4, 'A:2989:c5': C_F4,
    'A:262:c3': (C_AG, "Slovak clause is itself passive ('bol poslany'), no agent to drop"),
    'A:276:c5': (C_SYN, "'tear ... off' for odtrhnut (+ 'which is why'); TIP"),
    'A:587:c2': (C_DET, "'one great idea' mirrors 'jeden'; tip_det_rule covers only the/a swaps"),
    'A:1013:c1': C_REF, 'A:1013:c2': C_REF, 'A:1013:c3': C_REF, 'A:1013:c4': C_REF, 'A:1013:c5': C_REF,
    'A:1212:c4': (C_REF, "pro-drop 'bude robit' has no gender, reference only 'she'; answer 'he' (+ grimace); frozen SAME"),
    'A:1702:c1': (C_STR, "'enjoys burning them' for 'palenie ju bavi'; frozen SAME"),
    'A:1858:c1': C_REF, 'A:1858:c2': C_REF, 'A:1858:c3': C_REF, 'A:1858:c4': C_REF,
    'A:2046:c2': (C_SYN, "literal 'isn't finishing yet' for 'este nekonci' vs reference 'ain't done'; 'Mate' for 'Kamo'"),
    'A:2463:c1': C_REF, 'A:2463:c3': C_REF, 'A:2463:c4': C_REF, 'A:2463:c5': C_REF,
    'A:2495:c1': C_M1, 'A:2495:c5': C_M1,
    'A:2560:m': (C_JDG, "writer M; 'Who scored?' drops 'the goal' (subsumed by 'scored'); owner rule: dropped content word = wrong"),
    'A:2640:c5': (C_STR, "'Since ..., he can finally get to work' for '..., takze ...' (+ he for pro-drop)"),
    'A:2798:c5': (C_SYN, "'like it normally does' for 'ako to zvycajne robi'"),
    'A:3109:c2': (C_REF, "pro-drop 'vysusi' has no gender, reference only 'she'; answer 'he' (+ 'got rid of')"),
    'A:3109:c3': (C_TNS, "'will remove' / 'Before' for perfective 'odstrani'; reference 'will have removed'"),
    'A:3709:c5': (C_TNS, "'She'll take off' for perfective present 'Zlozi' (future meaning); reference only 'takes off'"),
    'A:3783:c4': (C_SYN, "'If' for 'Ked' (zero conditional) + 'the match'"),
    'A:3790:c2': (C_REF, "'konci svoju' has no gender, reference only 'she'; answer 'he' (+ 'the rooftop')"),
    'A:3856:c4': (C_VOI, "'has been sworn in', 'will be changed' for active 'zlozila prisahu ... sa zmeni'"),
}
FA_CAUSE = {
    'A:110:m': ('content word dropped accepted', "'in one afternoon' dropped; frozen rejected (TIP)"),
    'A:276:m': ('content word dropped accepted', "'off the plant' dropped"),
    'A:301:m': ('content word dropped accepted', "'recycling' dropped"),
    'A:423:m': ('judge doubtful', "only 'honestly' (uprimne, discourse word) dropped; by the owner's function-word rule arguably correct"),
    'A:842:m': ('content word dropped accepted', "'the lid' dropped; frozen rejected (TIP)"),
    'A:1106:c4': ('grammar error accepted', "article-less fragment 'Truly legendary technique.' - the reference has the same fragment"),
    'A:1212:m': ('content word dropped accepted', "'in front of the mirror' dropped"),
    'A:1738:m': ('content word dropped accepted', "'Look!' (Pozri!) dropped"),
    'A:2046:m': ('content word dropped accepted', "'in the morning' (rano) dropped"),
    'A:2356:c5': ('grammar error accepted', "missing article 'Slightly unplanned stop.'"),
    'A:2486:m': ('content word dropped accepted', "'through the door' dropped"),
    'A:3060:c5': ('wrong word accepted', "'train golf' (unidiomatic for practise golf)"),
    'A:3285:m': ('content word dropped accepted', "'of chairs' dropped"),
    'A:3489:m': ('content word dropped accepted', "'now' (teraz) dropped"),
    'A:3563:m': ('content word dropped accepted', "'today' (dnes) dropped; the contrast usually/today is lost"),
    'A:3573:m': ('content word dropped accepted', "intensifier 'completely' (uplne) dropped - borderline"),
    'A:3672:m': ('content word dropped accepted', "'hot' dropped"),
    'A:3797:m': ('content word dropped accepted', "'in the room' dropped"),
    'A:3957:m': ('content word dropped accepted', "'raw' dropped"),
}
P2F_CAUSE = {
    'C:220002:c3': (C_VOI, "'I was told by him' for active 'povedal mi'"),
    'C:220003:c3': (C_TNS, "present simple 'toasts' vs reference present perfect continuous"),
    'C:220005:c1': (C_F4, "'he' = 'strazník'"), 'C:220005:c3': (C_F4, "'he' = 'strazník'"),
    'W:220005:w3': (C_F4, "writer-wrong ('about cheese'), judged correct; F4v2 rejects for subject"),
    'C:220016:c1': (C_REF, "'spustil kanvicu' = switched on the kettle; reference 'lowered the pot'"),
    'C:220016:c2': (C_REF, "same wrong reference"),
    'C:220016:c3': (C_REF, "same wrong reference (answer is also passive with by-agent)"),
    'C:220021:c1': (C_REF, "'Hore' = up there/up here; reference only 'up here'"),
    'C:220021:c2': (C_STR, "'There's wind up there' for 'Hore je vietor'"),
    'C:220025:c1': (C_F4, "'she' for pro-drop 'spi'; reference 'it'"),
    'C:220025:c2': (C_F4, "'she' for pro-drop 'spi'; reference 'it'"),
    'C:220030:c1': (C_DET, "'one painted face' mirrors 'jednu'"),
    'C:220030:c2': (C_DET, "'A fan' / 'one painted face'"),
    'C:220030:c3': (C_DET, "'has got one painted face'"),
    'C:220032:c2': (C_VOI, "agent kept in by-phrase passive"),
    'C:220040:c1': (C_DET, "'The woman' vs reference 'A woman'"),
    'C:220040:c2': (C_DET, "'The woman' / 'one gold medal'"),
    'C:220045:c3': (C_M1, "'and' dropped from the list"),
    'C:220048:c3': (C_TNS, "'never smiled' vs 'had never smiled' in the same past frame"),
    'C:220049:c2': (C_JDG, "'swim off away from' is not clean English"),
    'C:220051:c3': (C_VOI, "agent kept in by-phrase passive"),
    'C:220053:c1': (C_F4, "'He' = 'zboznoval'"), 'C:220053:c2': (C_F4, "'He' = 'zboznoval'"),
    'C:220055:c3': (C_REF, "singular 'they' for pro-drop 'Napise'; reference only 'He'"),
    'C:220057:c3': (C_REF, "singular 'they' for pro-drop 'Potrebuje'; reference only 'He'"),
    'C:220060:c1': (C_REF, "'Mal si' is 2sg = You; reference says 'He'"),
    'C:220060:c2': (C_REF, "'Mal si' is 2sg = You; reference says 'He'"),
}


def cause_of(d, key, sid=None):
    v = d[key]
    if isinstance(v, tuple):
        return v
    return v, SID_NOTE.get(sid, '')


# ------------------------------------------------------------------ 4.1 headline
def rate(stack, lev=None):
    sel = [it for it in ITEMS if lev is None or it['level'] == lev]
    c = [it for it in sel if it['judge_label'] == 'correct']
    w = [it for it in sel if it['judge_label'] == 'wrong']
    kc = sum(R[(stack, it['jid'])]['accept'] for it in c)
    kw = sum(R[(stack, it['jid'])]['accept'] for it in w)
    lo1, hi1, m = cp(kc, len(c))
    lo2, hi2, _ = cp(kw, len(w))
    return {'cov_k': kc, 'cov_n': len(c), 'cov': round(pct(kc, len(c)), 2),
            'cov_ci': [round(100 * lo1, 2), round(100 * hi1, 2)],
            'fa_k': kw, 'fa_n': len(w), 'fa': round(pct(kw, len(w)), 2),
            'fa_ci': [round(100 * lo2, 2), round(100 * hi2, 2)], 'method': m,
            'cov_point_met': pct(kc, len(c)) >= 90, 'cov_interval_met': 100 * lo1 >= 90,
            'fa_point_met': pct(kw, len(w)) < 5, 'fa_interval_met': 100 * hi2 < 5}


HEAD = {s: {lv: rate(s, None if lv == 'pooled' else lv) for lv in LEVELS + ['pooled']} for s in ('tonly', 'frozen')}

# ------------------------------------------------------------------ 4.2 verdict diffs
diffs = []
for it in ITEMS:
    t, f = R[('tonly', it['jid'])], R[('frozen', it['jid'])]
    if t['accept'] == f['accept'] and t['layer'] == f['layer']:
        continue
    lab = it['judge_label']
    if t['accept'] != f['accept']:
        kind = ('correct' if lab == 'correct' else 'wrong') + (' newly ACCEPTED' if t['accept'] else ' newly REJECTED')
    else:
        kind = 'layer only (same verdict)'
    if str(f['layer']).startswith('L2'):
        comp = 'L2 lock / LOCKTIP'
    elif t['reached_l3'] and f['reached_l3'] and t['l3_reply'] != f['l3_reply']:
        comp = "removed 'Practised grammar ... ALREADY VERIFIED' line -> different L3 reply"
    elif f['layer'] == 'F2B':
        comp = 'F2B removed (same L3 reply; F2B -> L3:TIPrej relabel)'
    else:
        comp = 'other'
    diffs.append({'jid': it['jid'], 'level': it['level'], 'label': lab, 'kind': kind, 'component': comp,
                  'answer': it['answer'], 'slovak': it['slovak'], 'v': it['v'],
                  't': '%s %s / %s' % ('ACC' if t['accept'] else 'rej', t['layer'], t['l3_reply']),
                  'f': '%s %s / %s' % ('ACC' if f['accept'] else 'rej', f['layer'], f['l3_reply'])})
diff_kinds = Counter(d['kind'] for d in diffs)
diff_comp = Counter(d['component'] for d in diffs)
# L3 reply transitions over all items reaching L3 in both stacks
trans = Counter()
for it in ITEMS:
    t, f = R[('tonly', it['jid'])], R[('frozen', it['jid'])]
    if t['reached_l3'] and f['reached_l3']:
        trans['%s: %s -> %s' % (it['judge_label'], f['l3_reply'], t['l3_reply'])] += 1
both_l3 = sum(trans.values())
changed_l3 = sum(v for k, v in trans.items() if k.split(': ')[1].split(' -> ')[0] != k.split(' -> ')[1])

# ------------------------------------------------------------------ 4.3 FR / 4.8 FA
FR, FA = [], []
for it in ITEMS:
    t = R[('tonly', it['jid'])]
    if it['judge_label'] == 'correct' and not t['accept']:
        c, note = cause_of(FR_CAUSE, it['jid'], it['sid'])
        FR.append({'jid': it['jid'], 'sid': it['sid'], 'level': it['level'], 'slovak': it['slovak'], 'v': it['v'],
                   'answer': it['answer'], 'layer': t['layer'], 'l3_reply': t['l3_reply'], 'cause': c,
                   'note': note, 'frozen': R[('frozen', it['jid'])]['accept']})
    if it['judge_label'] == 'wrong' and t['accept']:
        c, note = FA_CAUSE[it['jid']]
        FA.append({'jid': it['jid'], 'sid': it['sid'], 'level': it['level'], 'slovak': it['slovak'], 'v': it['v'],
                   'answer': it['answer'], 'layer': t['layer'], 'l3_reply': t['l3_reply'], 'cause': c, 'note': note,
                   'wtype': it['writer_type'] or 'intent-correct', 'judge': it['judge_reason'],
                   'frozen': R[('frozen', it['jid'])]['accept']})
assert set(x['jid'] for x in FR) == set(FR_CAUSE), 'FR cause map out of sync'
assert set(x['jid'] for x in FA) == set(FA_CAUSE), 'FA cause map out of sync'
fr_cause = Counter(x['cause'] for x in FR)
fr_layer = Counter(x['layer'] for x in FR)
cxl = defaultdict(Counter)
cxv = defaultdict(Counter)
for x in FR:
    cxl[x['cause']][x['layer']] += 1
    cxv[x['cause']][x['level']] += 1
LAYERS = ['L1', 'AG', 'F3', 'F4v2', 'F5', 'L3', 'L3:TIPrej']
m1_f5 = [x for x in FR if x['layer'] == 'F5']
m1_all = [x for x in FR if x['cause'] == C_M1]
f5_all = [(it['jid'], it['judge_label']) for it in ITEMS if R[('tonly', it['jid'])]['layer'] == 'F5']
f4_all = Counter(it['judge_label'] for it in ITEMS if R[('tonly', it['jid'])]['layer'] == 'F4v2')
fa_cause = Counter(x['cause'] for x in FA)
fa_wtype = Counter(x['wtype'] for x in FA)
N_C = HEAD['tonly']['pooled']['cov_n']

# ------------------------------------------------------------------ 4.9 2F probe 28
p2 = json.load(open(f'{P2F}/run/results_1u.json'))['rows']
p2ann = json.load(open(f'{P2F}/data/annotations.json'))
p2v = json.load(open(f'{P2F}/run/verdicts_1u.json'))
P2 = []
for r in p2:
    if r['judged'] == 'correct' and not r['final_accept']:
        a = p2ann[str(r['sid'])]
        c, note = P2F_CAUSE[r['item_id']]
        P2.append({'jid': r['item_id'], 'level': r['level'], 'slovak': r['sk'],
                   'v': (a.get('hygienised') or a).get('v'), 'answer': r['answer'], 'layer': r['final_layer'],
                   'l3_reply': p2v.get(r['item_id']), 'cause': c, 'note': note})
assert len(P2) == 28 and set(x['jid'] for x in P2) == set(P2F_CAUSE)
p2_nc = sum(1 for r in p2 if r['judged'] == 'correct')
p2_cause = Counter(x['cause'] for x in P2)
p2_layer = Counter(x['layer'] for x in P2)

# ------------------------------------------------------------------ 4.5 / 4.6
U_FR, U_COV = 20, 95.02
U_N = round(U_FR / (1 - U_COV / 100))                 # derived: 402
U_CAUSE = {C_DET: 12}
U_LAYER = {'AG': 1, 'L3': 7, 'L3:TIPrej': 12}
REACH = {
    C_F4: ('(a) offline rule', 22, "F4v2 abstains when the answer's subject equals the reference subject / on reported-speech and multi-clause sentences; 24 FR on 5 sentences; ~22 recover (250:c4 'The car' may still clash). FA side unmeasured: 20 judge-wrong items are also F4v2-rejected and would go on to L3"),
    C_REF: ('(c) annotation / reference', 16, "add he/she variants for pro-drop present/future (3), 'into the bend' (5), 'carry' for nosila (4), drop invented 'her brother' (4)"),
    C_SYN: ('(b) L3 prompt', 2, "WORDING_LINE already says synonyms are SAME; at most half move"),
    C_STR: ('(b) L3 prompt', 1, 'paraphrase line exists; 1 of 2'),
    C_TNS: ('(c) reference variant / (b) prompt', 2, "add 'will take off' variant for perfective present (3709); 3109:c3 via prompt"),
    C_M1: ('(a) offline rule', 2, "F3 treats 'got' of has-got as a function word"),
    C_DET: ('(a) offline rule', 1, "extend tip_det_rule to one<->a when the Slovak has 'jeden'"),
    C_VOI: ('(b) L3 prompt', 1, 'VOICE_SAME_LINE covers it in principle'),
    C_AG: ('(a) offline rule', 1, 'AG must not fire when the Slovak clause is itself passive (bol poslany)'),
    C_JDG: ('(d) not at all', 0, 'label question, not a checker question'),
}

# ------------------------------------------------------------------ write numbers.json
NUM = {
    'headline': HEAD, 'ref_1W_test': {'cov': '392/401 = 97.76 %', 'fa': '16/499 = 3.21 %'},
    'ref_2F_probe': {'cov': '154/182 = 84.62 %', 'fa': '11/178 = 6.18 %'},
    'frozen_L2_lock_layers': len(lock_layers),
    'diffs': {'n': len(diffs), 'kinds': dict(diff_kinds), 'components': dict(diff_comp),
              'l3_both_reached': both_l3, 'l3_reply_changed': changed_l3, 'l3_transitions': dict(trans)},
    'FR': {'n': len(FR), 'by_cause': dict(fr_cause), 'by_layer': dict(fr_layer),
           'cause_x_layer': {k: dict(v) for k, v in cxl.items()},
           'cause_x_level': {k: dict(v) for k, v in cxv.items()}, 'jids': {x['jid']: x['cause'] for x in FR}},
    'M1': {'F5_rejecting_dropped_function_word': len(m1_f5), 'F5_layer_items_all': f5_all,
           'dropped_function_word_any_layer': [x['jid'] + ' ' + x['layer'] for x in m1_all]},
    'F4v2_layer_items_by_label': dict(f4_all),
    'FA': {'n': len(FA), 'by_cause': dict(fa_cause), 'by_writer_type': dict(fa_wtype),
           'jids': {x['jid']: x['cause'] for x in FA}},
    'P2F_28': {'n': len(P2), 'n_correct': p2_nc, 'by_cause': dict(p2_cause), 'by_layer': dict(p2_layer),
               'jids': {x['jid']: x['cause'] for x in P2}},
    'U1': {'fr': U_FR, 'n_correct_derived': U_N, 'by_cause': U_CAUSE, 'by_layer': U_LAYER},
    'reach': {k: {'route': v[0], 'est_recovered': v[1]} for k, v in REACH.items()},
    'judge_noise': {'controls': '%d/%d' % (CTRL['agree'], CTRL['n']), 'per_pair': CTRL['per_session_pair'],
                    'intent': INTENT['confusion_writer_to_judge']},
    'ci_method': HEAD['tonly']['pooled']['method'],
}
json.dump(NUM, open(f'{BASE}/analysis/numbers.json', 'w'), indent=1, ensure_ascii=False)

# ------------------------------------------------------------------ ANALYSIS.md
L = []
w = L.append
w('# Phase 2I - ANALYSIS (stage 6, 21.9.2026)\n')
w('Generated by `phase2i/analysis/analyze.py` from run/results.jsonl, set/items.jsonl, judge/*, phase2f/p3/probe/*. '
  '0 Gemini calls, 0 headless sessions. Numbers are computed; the per-item CAUSE is the stage-6 agent\'s own '
  'categorisation (hard-coded in analyze.py). Intervals: exact 95 %% Clopper-Pearson (%s). '
  'Coverage = accepted / judge-correct; FA = accepted / judge-wrong.\n' % NUM['ci_method'])

w('## 4.1 Headline\n')
w('| stack | level | coverage k/n | coverage % [95 % CI] | FA k/n | FA % [95 % CI] | cov >= 90 point / interval | FA < 5 point / interval |')
w('|---|---|---|---|---|---|---|---|')
yn = lambda b: 'MET' if b else 'missed'
for s, name in (('tonly', 'TRANSLATION-ONLY'), ('frozen', 'FROZEN 1W')):
    for lv in LEVELS + ['pooled']:
        h = HEAD[s][lv]
        w('| %s | %s | %d/%d | %.2f [%.2f, %.2f] | %d/%d | %.2f [%.2f, %.2f] | %s / %s | %s / %s |' % (
            name, lv, h['cov_k'], h['cov_n'], h['cov'], *h['cov_ci'], h['fa_k'], h['fa_n'], h['fa'], *h['fa_ci'],
            yn(h['cov_point_met']), yn(h['cov_interval_met']), yn(h['fa_point_met']), yn(h['fa_interval_met'])))
w('| 1W test (reference) | pooled | 392/401 | 97.76 [95.78, 98.97] | 16/499 | 3.21 [1.84, 5.15] | MET / MET | MET / missed |')
w('| 2F probe (reference) | pooled | 154/182 | 84.62 [78.54, 89.53] | 11/178 | 6.18 [3.12, 10.79] | missed / missed | missed / missed |')
tp = HEAD['tonly']['pooled']
w('\nTRANSLATION-ONLY pooled: coverage %.2f %% misses 90 %% on the point (interval [%.2f, %.2f] straddles it); FA %.2f %% meets < 5 %% on the point only (upper bound %.2f %%). '
  'A1 and A2 clear 90 %% coverage; B1 and B2 sit at %.2f / %.2f %%. A2 FA is %.2f %%.\n' % (
      tp['cov'], *tp['cov_ci'], tp['fa'], tp['fa_ci'][1], HEAD['tonly']['B1']['cov'], HEAD['tonly']['B2']['cov'], HEAD['tonly']['A2']['fa']))

w('## 4.2 What the owner\'s decision changed\n')
w('Frozen produced **%d** L2-lock layers on these 900 items: the structure lock / LOCKTIP never decided an item here. '
  'Every verdict difference comes from the L3 reply (the removed line) except one F2B relabel.\n' % len(lock_layers))
w('| kind | n |\n|---|---|')
for k in ['correct newly ACCEPTED', 'wrong newly ACCEPTED', 'correct newly REJECTED', 'wrong newly REJECTED', 'layer only (same verdict)']:
    w('| %s | %d |' % (k, diff_kinds.get(k, 0)))
w('| **total items differing** | **%d** |\n' % len(diffs))
w('| removed component | n |\n|---|---|')
for k, v in diff_comp.most_common():
    w('| %s | %d |' % (k, v))
w('\n**The cost, plainly: %d wrong answers are newly accepted** (A:110:m, A:842:m - both content-word drops frozen caught as TIP). '
  'Against that, %d wrong answers are newly rejected, so FA falls 21 -> 19. Correct: %d newly accepted, %d newly rejected -> coverage falls 447 -> 443.\n' % (
      diff_kinds.get('wrong newly ACCEPTED', 0), diff_kinds.get('wrong newly REJECTED', 0),
      diff_kinds.get('correct newly ACCEPTED', 0), diff_kinds.get('correct newly REJECTED', 0)))
w('### Why TRANSLATION-ONLY accepts 4 fewer correct answers (stage 5\'s surprise)\n')
w('The TRANSLATION-ONLY request differs from FROZEN by exactly one user-prompt line (test_2i (f)): '
  '"Practised grammar: <topic> - ALREADY VERIFIED as correct in this answer; judge meaning and vocabulary only." '
  'Same model, temperature 0, same system text. So every reply change below is caused by that line. '
  'Yes - the line made FROZEN\'s L3 lenient: "judge meaning and vocabulary only" told it to look past form, and with it gone the model '
  'leans on the English reference. All 5 correct answers it now rejects sit on sentences whose reference is narrow or wrong '
  '(pro-drop gender fixed to "she", an invented "her brother", "fetch" for nosila, "loves the burning"). '
  'The same leniency ran the other way on grammar: of the wrong answers both stacks reject, grammar slips moved TIP -> DIFF.\n')
w('| jid | level | answer | reference(s) | FROZEN reply -> verdict | TONLY reply -> verdict |\n|---|---|---|---|---|---|')
for d in diffs:
    if d['label'] == 'correct' and d['kind'] != 'layer only (same verdict)':
        w('| %s | %s | %s | %s | %s | %s |' % (d['jid'], d['level'], esc(d['answer']), esc(' ‖ '.join(d['v'])), d['f'], d['t']))
w('\nL3 reply transitions FROZEN -> TONLY over the %d items that reached L3 in both stacks (%d changed):\n' % (both_l3, changed_l3))
w('| judge label: frozen -> tonly | n |\n|---|---|')
for k, v in sorted(trans.items()):
    w('| %s | %d |' % (k, v))
w('\n### Every item whose verdict or layer differs (%d)\n' % len(diffs))
w('| jid | level | label | kind | component | Slovak | answer | FROZEN | TONLY |\n|---|---|---|---|---|---|---|---|---|')
for d in diffs:
    w('| %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (d['jid'], d['level'], d['label'], d['kind'], d['component'],
                                                          esc(d['slovak']), esc(d['answer']), d['f'], d['t']))

w('\n## 4.3 Every false rejection of TRANSLATION-ONLY (%d of %d judge-correct)\n' % (len(FR), N_C))
w('Cause extension: **%s** - %s\n' % (C_F4, EXT_WHY))
w('Judge controls were 80/80, so "judge label doubtful" is used once only, where the owner\'s own rule contradicts the label.\n')
w('| # | jid | sid | level | Slovak | stored English reference(s) | answer | layer | L3 reply | cause | note | FROZEN |\n|---|---|---|---|---|---|---|---|---|---|---|---|')
for i, x in enumerate(FR, 1):
    w('| %d | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (
        i, x['jid'], x['sid'], x['level'], esc(x['slovak']), esc(' ‖ '.join(x['v'])), esc(x['answer']), x['layer'],
        esc(x['l3_reply']), x['cause'], esc(x['note']), 'acc' if x['frozen'] else 'rej'))

w('\n## 4.4 Tables\n')
w('### Per cause\n\n| cause | FR | share | rate of judge-correct |\n|---|---|---|---|')
for c in CAUSES:
    if fr_cause.get(c):
        w('| %s | %d | %.1f %% | %.2f %% |' % (c, fr_cause[c], pct(fr_cause[c], len(FR)), pct(fr_cause[c], N_C)))
w('| **total** | **%d** | 100 %% | %.2f %% |' % (len(FR), pct(len(FR), N_C)))
w('\n### Per layer\n\n| layer | FR |\n|---|---|')
for l in LAYERS:
    w('| %s | %d |' % (l, fr_layer.get(l, 0)))
w('\n### Cause x layer\n\n| cause | ' + ' | '.join(LAYERS) + ' |\n|---|' + '---|' * len(LAYERS))
for c in CAUSES:
    if fr_cause.get(c):
        w('| %s | ' % c + ' | '.join(str(cxl[c].get(l, 0) or '') for l in LAYERS) + ' |')
w('\n### Cause x level\n\n| cause | A1 | A2 | B1 | B2 |\n|---|---|---|---|---|')
for c in CAUSES:
    if fr_cause.get(c):
        w('| %s | ' % c + ' | '.join(str(cxv[c].get(l, 0) or '') for l in LEVELS) + ' |')
lvfr = Counter(x['level'] for x in FR)
w('| **total** | ' + ' | '.join(str(lvfr.get(l, 0)) for l in LEVELS) + ' |')

w('\n## 4.5 Against the test sets (1U)\n')
w('1U: 20 FR, 12 determiner; layers AG 1, L3 7, L3:TIPrej 12. 1U judge-correct n derived as %d from 20 FR at 95.02 %% coverage (derived, not re-read). Rates = FR / judge-correct.\n' % U_N)
w('| | 1U n | 1U rate | 2I TONLY n | 2I rate | verdict |\n|---|---|---|---|---|---|')
w('| determiner/article CHOICE | 12 | %.2f %% | %d | %.2f %% | same cause, much LOWER rate (tip_det_rule + article ruling hold) |' % (pct(12, U_N), fr_cause.get(C_DET, 0), pct(fr_cause.get(C_DET, 0), N_C)))
for c in [C_F4, C_REF, C_SYN, C_STR, C_TNS, C_M1, C_VOI, C_AG, C_JDG]:
    tag = {C_F4: 'NEW to production (F4v2 rejected no correct answer in 1U)', C_REF: 'NEW to production (1U references were hand-built)',
           C_AG: 'same, same rate'}.get(c, '1U\'s 8 non-determiner FR are not broken down in the figures carried; not comparable')
    w('| %s | %s | %s | %d | %.2f %% | %s |' % (c, '1' if c == C_AG else '-', '%.2f %%' % pct(1, U_N) if c == C_AG else '-',
                                                fr_cause.get(c, 0), pct(fr_cause.get(c, 0), N_C), tag))
w('\n| layer | 1U n | 1U rate | 2I n | 2I rate | |\n|---|---|---|---|---|---|')
for l in ['AG', 'L3', 'L3:TIPrej', 'F4v2', 'F3', 'F5', 'L1']:
    un = U_LAYER.get(l, 0)
    tn = fr_layer.get(l, 0)
    note = 'NEW' if (tn and not un) else ('higher' if pct(tn, N_C) > pct(un, U_N) * 1.2 else ('lower' if pct(tn, N_C) < pct(un, U_N) / 1.2 else 'same'))
    w('| %s | %d | %.2f %% | %d | %.2f %% | %s |' % (l, un, pct(un, U_N), tn, pct(tn, N_C), note if (un or tn) else ''))
w('\nNew in production: the F4v2 subject-guard misfire (24) and wrong/narrow references (16) - together 40 of %d FR. '
  'Same cause at a higher rate: L3 DIFF rejections (%.2f %% vs %.2f %%), driven by the reference-bound model. '
  'Lower: determiner (%.2f %% vs %.2f %%) and L3:TIPrej.\n' % (len(FR), pct(fr_layer.get('L3', 0), N_C), pct(7, U_N),
                                                              pct(fr_cause.get(C_DET, 0), N_C), pct(12, U_N)))

w('## 4.6 Reachability per cause (build nothing)\n')
w('| cause | FR | reachable by | est. recovered | how |\n|---|---|---|---|---|')
tot = 0
for c in CAUSES:
    if fr_cause.get(c):
        r = REACH[c]
        tot += r[1]
        w('| %s | %d | %s | %d | %s |' % (c, fr_cause[c], r[0], r[1], esc(r[2])))
w('| **total** | **%d** | | **%d** | coverage ceiling if all land: %d/%d = %.2f %% |\n' % (
    len(FR), tot, tp['cov_k'] + tot, N_C, pct(tp['cov_k'] + tot, N_C)))
w('Single biggest lever: F4v2 alone -> ~%d/%d = %.2f %% coverage (FA effect unmeasured: %d judge-wrong items are also F4v2-rejected today).\n' % (
    tp['cov_k'] + REACH[C_F4][1], N_C, pct(tp['cov_k'] + REACH[C_F4][1], N_C), f4_all.get('wrong', 0)))

w('## 4.7 M1 (F5 rejecting a dropped function/discourse word)\n')
w('**%d** false rejections are F5 rejecting a dropped function word. F5 decided only %d items in TRANSLATION-ONLY, all judge-wrong: %s. '
  'The nearest thing: %d FR where **F3** (deletion) rejects the dropped function word "got" of "has got": %s. '
  'The M1 defect (1S section 5) is real in the code but did not cost a correct answer in this set.\n' % (
      len(m1_f5), len(f5_all), ', '.join('%s (%s)' % a for a in f5_all), len(m1_all), ', '.join(x['jid'] + ' ' + x['layer'] for x in m1_all)))

w('## 4.8 Every false acceptance of TRANSLATION-ONLY (%d of %d judge-wrong)\n' % (len(FA), tp['fa_n']))
w('| cause | n |\n|---|---|')
for k, v in fa_cause.most_common():
    w('| %s | %d |' % (k, v))
w('\nBy writer type: %s. No time-frame miss and no agent drop was accepted.\n' % ', '.join('%s %d' % kv for kv in fa_wtype.most_common()))
w('| # | jid | level | Slovak | reference(s) | answer | writer type | judge reason | layer / reply | cause | note | FROZEN |\n|---|---|---|---|---|---|---|---|---|---|---|---|')
for i, x in enumerate(FA, 1):
    w('| %d | %s | %s | %s | %s | %s | %s | %s | %s / %s | %s | %s | %s |' % (
        i, x['jid'], x['level'], esc(x['slovak']), esc(' ‖ '.join(x['v'])), esc(x['answer']), x['wtype'], esc(x['judge']),
        x['layer'], x['l3_reply'], x['cause'], esc(x['note']), 'acc' if x['frozen'] else 'rej'))

w('\n## 4.9 The 2F probe\'s 28 false rejections (stored files, 0 calls)\n')
w('| cause | n | rate of %d judge-correct |\n|---|---|---|' % p2_nc)
for c in CAUSES:
    if p2_cause.get(c):
        w('| %s | %d | %.2f %% |' % (c, p2_cause[c], pct(p2_cause[c], p2_nc)))
w('\nBy layer: %s.\n' % ', '.join('%s %d' % kv for kv in p2_layer.most_common()))
w('| # | jid | level | Slovak | reference(s) | answer | layer | L3 reply | cause | note |\n|---|---|---|---|---|---|---|---|---|---|')
for i, x in enumerate(P2, 1):
    w('| %d | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (i, x['jid'], x['level'], esc(x['slovak']), esc(' ‖ '.join(x['v'])),
                                                             esc(x['answer']), x['layer'], esc(x['l3_reply']), x['cause'], esc(x['note'])))
w('\nThe probe shows the same two production-only causes (F4v2 misfire 7, wrong/narrow references 8) plus the determiner '
  'cluster 1U knew (5) that TIPdet/article ruling has since cut in 2I (1).\n')

w('## Judge noise\n')
w('Hidden duplicate controls: **%d/%d** agree.\n\n| session pair | agree / n |\n|---|---|' % (CTRL['agree'], CTRL['n']))
for k, v in CTRL['per_session_pair'].items():
    w('| %s | %d/%d |' % (k, v['agree'], v['n']))
w('\nWriter intent vs judge label: %d/%d agree; %s.\n' % (INTENT['agree'], INTENT['n'], ', '.join('%s %d' % kv for kv in INTENT['confusion_writer_to_judge'].items())))
w('| aid | level | writer intent | judge | judge reason | answer |\n|---|---|---|---|---|---|')
for d in INTENT['disagreements']:
    w('| %s | %s | %s%s | %s | %s | %s |' % (d['aid'], d['level'], d['writer_intent'], ' ' + d['writer_type'] if d.get('writer_type') else '',
                                           d['judge'], esc(d['reason']), esc(d['answer'])))
open(f'{BASE}/analysis/ANALYSIS.md', 'w').write('\n'.join(L) + '\n')
print(json.dumps({'head_tonly': {k: '%d/%d %.2f | %d/%d %.2f' % (v['cov_k'], v['cov_n'], v['cov'], v['fa_k'], v['fa_n'], v['fa']) for k, v in HEAD['tonly'].items()},
                  'ci_pooled': [tp['cov_ci'], tp['fa_ci']], 'diff': dict(diff_kinds), 'comp': dict(diff_comp),
                  'fr_cause': dict(fr_cause), 'fr_layer': dict(fr_layer), 'm1_f5': len(m1_f5), 'f5_all': f5_all,
                  'fa': dict(fa_cause), 'p2': dict(p2_cause), 'p2_layer': dict(p2_layer), 'lock_layers': len(lock_layers),
                  'trans_changed': changed_l3, 'u_n': U_N}, indent=0))

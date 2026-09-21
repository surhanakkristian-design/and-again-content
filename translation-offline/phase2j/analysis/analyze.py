#!/usr/bin/env python3
"""Phase 2J stage 9 - Part D analysis. 0 model calls.

Inputs (read only): phase2j/partD/run/{results.jsonl,HEADLINE_QUICK.json}, partD/set/items.jsonl,
partD/judge/intent_agreement.json, upload/B3_diff.jsonl, GEMINI_LEDGER.json, TOKENS.jsonl.
Outputs: phase2j/analysis/ANALYSIS.md + numbers.json.
Numbers are computed; the per-item CAUSE is the S9 agent's own categorisation (hard-coded below, 2I cause list,
extensions marked). Intervals: exact 95 % Clopper-Pearson (binomial tail bisection, log-space).
"""
import json, math, os, re, sys
from collections import Counter, defaultdict

P2J = '/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2j'
OUT = os.path.join(P2J, 'analysis')
assert os.path.abspath(OUT).startswith(P2J + '/'), 'write guard'


def jl(p):
    return [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]


# ------------------------------------------------------------------ exact Clopper-Pearson
def _logpmf(k, n, p):
    if p <= 0.0:
        return 0.0 if k == 0 else -math.inf
    if p >= 1.0:
        return 0.0 if k == n else -math.inf
    return (math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)
            + k * math.log(p) + (n - k) * math.log1p(-p))


def _cdf(k, n, p):  # P(X <= k)
    if k < 0:
        return 0.0
    if k >= n:
        return 1.0
    return min(1.0, sum(math.exp(_logpmf(i, n, p)) for i in range(0, k + 1)))


def _bis(f, lo=0.0, hi=1.0):  # f increasing in p, find root
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(mid) > 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def cp(k, n, a=0.05):
    lo = 0.0 if k == 0 else _bis(lambda p: (1 - _cdf(k - 1, n, p)) - a / 2)   # P(X>=k) = a/2
    hi = 1.0 if k == n else _bis(lambda p: (a / 2) - _cdf(k, n, p))          # P(X<=k) = a/2
    return (round(100 * lo, 2), round(100 * hi, 2))


def pct(k, n):
    return round(100.0 * k / n, 2) if n else 0.0


assert cp(443, 497) == (86.06, 91.73), cp(443, 497)
assert cp(19, 403) == (2.86, 7.26), cp(19, 403)


def esc(s):
    return str(s).replace('|', '/').replace('\n', ' ')


# ------------------------------------------------------------------ data
R = {r['jid']: r for r in jl(P2J + '/partD/run/results.jsonl')}
I = {i['jid']: i for i in jl(P2J + '/partD/set/items.jsonl')}
H = json.load(open(P2J + '/partD/run/HEADLINE_QUICK.json'))
IA = json.load(open(P2J + '/partD/judge/intent_agreement.json'))
LED = json.load(open(P2J + '/GEMINI_LEDGER.json'))
TOK = jl(P2J + '/TOKENS.jsonl')
B3 = defaultdict(list)
B3_ALL = jl(P2J + '/upload/B3_diff.jsonl')
for d in B3_ALL:
    if d['lang'] == 'sk':
        B3[d['exercise_id']].append(d)
assert set(R) == set(I) and len(I) == 900
LEVELS = ['A1', 'A2', 'B1', 'B2']

# ------------------------------------------------------------------ causes (S9 categorisation, 2I list + extensions)
C_F4 = 'F4v2 subject-guard misfire (extension)'
C_REF = 'reference wrong or too narrow'
C_SYN = 'synonym or different word'
C_STR = 'structural paraphrase'
C_TNS = "English tense within the Slovak's frame"
C_M1 = 'dropped FUNCTION word (M1)'
C_DET = 'determiner or article CHOICE'
C_VOI = 'voice or passive'
C_AG = 'AG misfire'
C_JDG = 'judge label doubtful'
C_F5X = 'F5 misfire: compound noun shortened (extension 2J)'
C_L3X = 'L3 rejects an answer equal to a stored reference (extension 2J)'
FR_ORDER = [C_F4, C_REF, C_SYN, C_STR, C_TNS, C_M1, C_DET, C_VOI, C_AG, C_JDG, C_F5X, C_L3X]
FR_2I = {C_F4: 24, C_REF: 16, C_SYN: 4, C_STR: 2, C_TNS: 2, C_M1: 2, C_DET: 1, C_VOI: 1, C_AG: 1, C_JDG: 1}

FR_CAUSE = {
    'A:1033:c3': (C_AG, "'the play will be performed at the theatre' keeps the agent as a place; AG reads agentless passive vs 'divadlo ... uvedie'"),
    'A:1568:c5': (C_STR, "'Look, a free space!' for 'Tam je volne miesto!' (+ 'over there'); TIP"),
    'A:1613:c1': (C_REF, "pro-drop 'opravuje' has no gender; both refs 'she' (B3 added 'wheels', not 'he'); answer 'he'"),
    'A:1613:c3': (C_REF, "pro-drop 'opravuje' has no gender; both refs 'she'; answer 'he'"),
    'A:1613:c5': (C_REF, "pro-drop 'opravuje' has no gender; both refs 'she'; answer 'he' (+ mending/teeny)"),
    'A:180:c2': (C_REF, "'jej' = her/its; refs only 'its' (+ 'rag' for 'handrickou')"),
    'A:180:c3': (C_L3X, "answer 'She'll wipe its big green leaves with a cloth.' = stored ref v[1] 'She will wipe ...' up to contraction; L3 DIFF"),
    'A:180:c5': (C_SYN, "'cleans' for 'utrie' (wipe); B3 'He' variant present"),
    'A:2126:c1': (C_M1, "F3 reports 'got' missing (has got -> has)"),
    'A:2152:c1': (C_REF, "'pohare' = glasses/jars; both refs 'jars'"),
    'A:2152:c2': (C_REF, "'pohare' = glasses/jars; both refs 'jars' (+ grandma/cupboard/have)"),
    'A:2152:c3': (C_REF, "'pohare' = glasses/jars; both refs 'jars'"),
    'A:2152:c4': (C_REF, "'pohare' = glasses/jars; both refs 'jars' (+ gran/store/drinking glasses)"),
    'A:2152:c5': (C_REF, "'pohare' = glasses/jars; both refs 'jars' (+ 'here')"),
    'A:22:c4': (C_REF, "'administrativa' = administration; ref 'paperwork'; ref damaged by B3 A-replacement ('slumped onto desk', 'her' deleted)"),
    'A:2358:c4': (C_DET, "'This snake' for 'Had' vs ref 'The snake'; TIP"),
    'A:2362:c2': (C_REF, "'ako on na holeni' attaches to him or to me; ref fixes 'the one on his shin', answer 'like his on my shin'"),
    'A:2362:c3': (C_REF, "same attachment ambiguity; answer 'such a scar on my shin as he does'"),
    'A:2724:c3': (C_SYN, "'jumping' for 'vrhat sa' (dive) + 'seriously' for 'bez kecov'; TIP"),
    'A:2724:c4': (C_SYN, "'no nonsense' for 'bez kecov' vs 'no cap'; B3 'she' variant present and matched"),
    'A:2787:c3': (C_SYN, "'the king's throne' for 'kralovskom trone' (royal)"),
    'A:2800:c1': (C_AG, "'its wheels are worn out' = the ref's own adjectival predicate for 'ma zodrate'; AG reads agentless passive"),
    'A:2800:c4': (C_AG, "'the wheels are worn out' adjectival; AG misfire"),
    'A:2800:c5': (C_AG, "'the wheels are worn down' adjectival; AG misfire"),
    'A:282:c1': (C_F5X, "'in the pan' for 'na panvici'; F5 reads 'frying' of 'frying pan' as a dropped content word"),
    'A:282:c2': (C_TNS, "'will she burn' for perfective present 'spali' (future meaning); refs present simple only"),
    'A:282:c3': (C_TNS, "'is he going to burn' for perfective present; refs present simple only"),
    'A:282:c5': (C_TNS, "'will he burn' for perfective present; refs present simple only"),
    'A:2889:c2': (C_REF, "ref 'Not gonna lie ... smoother' for 'Na rovinu ... ladnejsi' and drops 'tu' (here)"),
    'A:2889:c3': (C_REF, "same ref; answer 'Frankly ... more graceful ... here'"),
    'A:2889:c4': (C_REF, "same ref; answer 'Honestly ... as graceful ... here'"),
    'A:2889:c5': (C_REF, "same ref; answer 'Let's be honest ... more elegant ... here'"),
    'A:3147:c5': (C_AG, "'is priced at' read as agentless passive vs 'luxusny kocik je za 5000 eur'"),
    'A:315:m': (C_JDG, "writer M dropped 'them' (im); judge 'only a dropped pronoun'; F3 rejects the drop"),
    'A:3251:c3': (C_TNS, "'he will score' for 'do konca zapasu premeni' vs ref 'will have scored'; TIP"),
    'A:3390:c1': (C_REF, "'si snuroval' reads 2sg 'you were tying' (si = auxiliary) or reflexive 'he'; refs only 'He' (B3 added 'shoes', not the person)"),
    'A:3390:c2': (C_REF, "same person ambiguity; answer 'You'"),
    'A:3390:c3': (C_REF, "same person ambiguity; answer 'You'"),
    'A:3390:c4': (C_REF, "same person ambiguity; answer 'you'"),
    'A:3390:c5': (C_REF, "same person ambiguity; answer 'You'"),
    'A:365:c4': (C_REF, "'cena' = price, 'tabulku' = board/sign; refs 'bidding', 'paddle' (B3 'he' variant present)"),
    'A:40:c5': (C_M1, "F3 reports 'got' missing (has got -> has)"),
    'A:497:c5': (C_STR, "adds 'all' ('all completely empty'); TIP"),
    'A:54:c3': (C_REF, "ref truncated by B3 A-replacement to '... grins like that before a.'"),
    'A:92:c2': (C_REF, "'Ak povie ..., pusti sa' both pro-drop, gender open; ref fixes he/she (B3 listed the swap, did not add it)"),
    'A:92:c5': (C_REF, "same; answer she/he"),
    'A:2562:c1': (C_M1, "F3 reports 'got' missing (has got -> has)"),
    'A:2562:c3': (C_M1, "F3 reports 'got' missing (has got -> has); 'A man' free"),
}

A_CONT = 'content word dropped accepted'
A_GRAM = 'grammar error accepted'
A_JDG = 'judge doubtful'
A_WW = 'wrong word accepted'
A_AGD = 'agent drop accepted (extension 2J)'
A_TF = 'time-frame shift accepted (extension 2J)'
FA_ORDER = [A_CONT, A_GRAM, A_JDG, A_WW, A_AGD, A_TF]
FA_2I = {A_CONT: 15, A_GRAM: 2, A_JDG: 1, A_WW: 1}
FA_CAUSE = {
    'A:1396:m': (A_CONT, "'absolutely' (absolutne) dropped"),
    'A:1413:m': (A_CONT, "'office' (kancelarie) dropped"),
    'A:1720:m': (A_AGD, "passive drops the named agent 'sestry' (nurses); AG c0: the annotation says no nominative agent (annotation wrong)"),
    'A:1781:c4': (A_WW, "'bright' for 'farebna' (colourful)"),
    'A:1781:m': (A_CONT, "'colorful' dropped"),
    'A:2069:m': (A_CONT, "'street' (poulicny) dropped"),
    'A:2228:m': (A_CONT, "'yesterday' (vcera) dropped - the usually/yesterday contrast is lost"),
    'A:2237:m': (A_CONT, "'winding' (klukatom) dropped"),
    'A:233:m': (A_CONT, "'empty' (prazdnym) dropped"),
    'A:2397:m': (A_CONT, "'quickly' (rychlo) dropped"),
    'A:2829:c4': (A_WW, "'hot' for 'teply' (warm)"),
    'A:2889:m': (A_CONT, "'here' (tu) dropped - the ref itself omits 'here' (reference-caused)"),
    'A:3147:m': (A_CONT, "'luxury' (luxusny) dropped"),
    'A:3396:c4': (A_WW, "'give her colleague her hand' for 'podat ruku' (shake hands)"),
    'A:3412:m': (A_CONT, "'bull' (byka) dropped"),
    'A:3434:m': (A_CONT, "'same' (ten isty) dropped"),
    'A:3468:m': (A_CONT, "'good' (dobre) dropped"),
    'A:3523:m': (A_CONT, "'red' (cervenou) dropped"),
    'A:3523:w': (A_WW, "'sand' for 'hlinou' (clay/soil); ref 'dirt'"),
    'A:3553:m': (A_CONT, "'tomorrow' (zajtra) dropped"),
    'A:3624:m': (A_CONT, "'finally' (konecne) dropped"),
    'A:54:m': (A_CONT, "'backwards' (dozadu) dropped - the B3-truncated ref '... before a.' has no content to hold it against (reference-caused)"),
    'A:54:t': (A_TF, "present wish/grin shifted to past; the B3-truncated ref (reference-caused)"),
    'A:865:m': (A_CONT, "'camp' (tabora) dropped"),
}
REF_CAUSED_FA = {'A:2889:m', 'A:54:m', 'A:54:t'}

# ------------------------------------------------------------------ headline
def is_correct(j):
    return I[j]['judge_label'] == 'correct'


def acc(j):
    return bool(R[j]['accept'])


FR = sorted([j for j in I if is_correct(j) and not acc(j)], key=lambda j: (int(j.split(':')[1]), j))
FA = sorted([j for j in I if not is_correct(j) and acc(j)], key=lambda j: (int(j.split(':')[1]), j))
assert set(FR) == set(H['false_rejections']) and set(FA) == set(H['false_acceptances'])
assert set(FR) == set(FR_CAUSE), sorted(set(FR) ^ set(FR_CAUSE))
assert set(FA) == set(FA_CAUSE), sorted(set(FA) ^ set(FA_CAUSE))
assert all(not R[j]['call_failed'] for j in I)

TWO_I = {'A1': (120, 124, 2, 101), 'A2': (117, 125, 8, 100), 'B1': (103, 123, 6, 102), 'B2': (103, 125, 3, 100),
         'pooled': (443, 497, 19, 403)}


def cell(lev):
    js = [j for j in I if lev == 'pooled' or I[j]['level'] == lev]
    nc = sum(is_correct(j) for j in js)
    kc = sum(is_correct(j) and acc(j) for j in js)
    nw = sum(not is_correct(j) for j in js)
    kw = sum((not is_correct(j)) and acc(j) for j in js)
    ci_c, ci_w = cp(kc, nc), cp(kw, nw)
    return {'coverage': {'x': kc, 'n': nc, 'pct': pct(kc, nc), 'cp95': list(ci_c),
                         'point': 'MET' if pct(kc, nc) >= 90 else 'MISSED',
                         'interval': 'MET' if ci_c[0] >= 90 else 'MISSED'},
            'fa': {'x': kw, 'n': nw, 'pct': pct(kw, nw), 'cp95': list(ci_w),
                   'point': 'MET' if pct(kw, nw) <= 5 else 'MISSED',
                   'interval': 'MET' if ci_w[1] <= 5 else 'MISSED'}}


HEAD = {lev: cell(lev) for lev in LEVELS + ['pooled']}
assert (HEAD['pooled']['coverage']['x'], HEAD['pooled']['coverage']['n']) == (450, 498)
assert (HEAD['pooled']['fa']['x'], HEAD['pooled']['fa']['n']) == (24, 402)
TWO_I_CELLS = {}
for lev, (a, b, c, d) in TWO_I.items():
    TWO_I_CELLS[lev] = {'cov': (a, b, pct(a, b), cp(a, b)), 'fa': (c, d, pct(c, d), cp(c, d))}

# ------------------------------------------------------------------ B3 involvement
CHANGE_ACTIONS = {'added', 'replaced', 'removed'}


def b3_tag(j):
    ds = B3.get(I[j]['exercise_id'], [])
    if not ds:
        return '-'
    return ', '.join(sorted({'%s/%s' % (d['class'], d['action']) for d in ds}))


def b3_changed(j):
    return any(d['action'] in CHANGE_ACTIONS for d in B3.get(I[j]['exercise_id'], []))


def b3_gender(j):
    return any(d['class'] == 'W' and d['action'] == 'added' for d in B3.get(I[j]['exercise_id'], []))


def rows(js, cmap):
    out = []
    for j in js:
        i, r = I[j], R[j]
        c, note = cmap[j]
        out.append({'jid': j, 'level': i['level'], 'exercise_id': i['exercise_id'], 'slovak': i['slovak'], 'refs': i['v'],
                    'answer': i['answer'], 'writer_type': i['writer_type'] or 'intent-' + i['writer_intent'],
                    'layer': r['layer'], 'l3_reply': r['l3_reply'], 'judge_label': i['judge_label'],
                    'judge_reason': i['judge_reason'], 'cause': c, 'note': note, 'b3': b3_tag(j),
                    'b3_changed': b3_changed(j), 'b3_gender_variant': b3_gender(j)})
    return out


FRr, FAr = rows(FR, FR_CAUSE), rows(FA, FA_CAUSE)
fr_c, fa_c = Counter(x['cause'] for x in FRr), Counter(x['cause'] for x in FAr)
fr_layer, fa_layer = Counter(x['layer'] for x in FRr), Counter(x['layer'] for x in FAr)
assert dict(fr_layer) == H['fr_by_layer'] and dict(fa_layer) == H['fa_by_layer']
fr_cxv = defaultdict(Counter)
for x in FRr:
    fr_cxv[x['cause']][x['level']] += 1
fa_cxv = defaultdict(Counter)
for x in FAr:
    fa_cxv[x['cause']][x['level']] += 1
fa_wtype = Counter(x['writer_type'] for x in FAr)

f4_left = sum(1 for x in FRr if x['layer'] in ('F4v2', 'F4v3') or x['cause'] == C_F4)
f4_fa = sum(1 for x in FAr if x['layer'] in ('F4v2', 'F4v3'))
ref_fr = fr_c[C_REF]
fr_b3 = [x['jid'] for x in FRr if x['b3_changed']]
fa_b3 = [x['jid'] for x in FAr if x['b3_changed']]
fr_b3_any = [x['jid'] for x in FRr if x['b3'] != '-']
fa_b3_any = [x['jid'] for x in FAr if x['b3'] != '-']
fr_b3_gender = [x['jid'] for x in FRr if x['b3_gender_variant']]
fa_b3_gender = [x['jid'] for x in FAr if x['b3_gender_variant']]
set_exids = {i['exercise_id'] for i in I.values()}
set_b3_changed_ex = sorted(e for e in set_exids if any(d['action'] in CHANGE_ACTIONS for d in B3.get(e, [])))

# items on B3-changed rows: coverage / FA there vs elsewhere
def sub_rate(pred):
    js = [j for j in I if pred(j)]
    nc = sum(is_correct(j) for j in js); kc = sum(is_correct(j) and acc(j) for j in js)
    nw = sum(not is_correct(j) for j in js); kw = sum((not is_correct(j)) and acc(j) for j in js)
    return {'cov': [kc, nc, pct(kc, nc)], 'fa': [kw, nw, pct(kw, nw)]}


B3_SPLIT = {'b3_changed_rows': sub_rate(b3_changed), 'other_rows': sub_rate(lambda j: not b3_changed(j))}

# ------------------------------------------------------------------ B3 variant scan (deterministic, all SK rows)
MALE = {'he', 'him', 'his', 'himself'}
FEM = {'she', 'her', 'hers', 'herself'}


def toks(s):
    return re.findall(r"[a-z']+", (s or '').lower())


W_ADDED = [d for d in B3_ALL if d['lang'] == 'sk' and d['class'] == 'W' and d['action'] == 'added']
nonpure, mixed = [], []
for d in W_ADDED:
    a, b = toks(d['before']), toks(d['after'])
    diff = [(x, y) for x, y in zip(a, b) if x != y]
    pron = MALE | FEM | {'it', 'its', 'they', 'them', 'their', 'i', 'you', 'we', 'me', 'my', 'your', 'our', 'us'}
    if len(a) != len(b) or any(not (x.split("'")[0] in pron and y.split("'")[0] in pron) for x, y in diff):
        nonpure.append(d)
    bm, bf = bool(set(a) & MALE), bool(set(a) & FEM)
    am, af = bool(set(b) & MALE), bool(set(b) & FEM)
    if (am and af) and not (bm and bf):
        mixed.append(d)
A_REPL = [d for d in B3_ALL if d['lang'] == 'sk' and d['action'] == 'replaced']
trunc = [d for d in A_REPL if re.search(r"\b(a|an|the|to|of|onto|with|his|her|my|your|their)\s*[.!?]?\s*$", (d.get('after') or '').lower())
         or re.search(r"\b(onto|into|on|in|at|to)\s+(desk|table|floor|bed)\b", (d.get('after') or '').lower())]
BAD_SEEN = {22: "A-replacement removed 'her': \"...she wouldn't have slumped onto desk.\" (ungrammatical)",
            54: "A-replacement of 'trust fall' truncated the reference to \"...grins like that before a.\""}

# ------------------------------------------------------------------ Parts A/B/C, costs, tokens (from stage files)
agent_tok = sum(t.get('agent_est', 0) for t in TOK)
head_tok = sum(t.get('headless_tokens', 0) for t in TOK)
assert head_tok == 1980709, head_tok
gem = sum(v for v in LED.values() if isinstance(v, int)) if all(isinstance(v, int) for v in LED.values()) else None
S9_AGENT_EST = 150000

PARTS = [
    ('A1', 'F4v2 cause: checker_1i.sk_features ending heuristics (:552-563) read nouns/adverbs as verbs (ceste/zivote/plote -te, prilis -s, samozrejme -me); after_prep looks one token back'),
    ('A2', 'f4fix.py: PP prepositional-NP shadow + closed non-verb list (+ verb-loss guard), F4v2; S2c extended to F4v3 (guards_c.py:339, same misreading). Catches 21 / cost 1 (A:250:m) on the closed 2I set'),
    ('A3', 'closed-set re-score: 2I 443/497 = 89.13 % [86.06, 91.73] / FA 19/403 = 4.71 % [2.86, 7.26] -> A 464/497 = 93.36 % [90.80, 95.39] / 20/403 = 4.96 % [3.06, 7.56]; 43 new L3 calls'),
    ('A4', 'regression gate 1W 900 / 1S rows 1,080 / 1S packet 183: 0 F4v2 or F4v3 decision changes -> PASS, 0 calls'),
    ('A5', 'Czech reader has the same defect (prilis x15); f4fix.build_fixed(CK, cz) changes 18/4,064 CZ rows (SK 125); Czech has no F4v3'),
    ('C1', '20 closed-set FAs: F5 needs an order-preserving subsequence of a reference; returns None at checker_1i.py:669 -> continue :719 on all 20 (thin single refs + M answers also swap a token)'),
    ('C2', 'sized V1-V5, cheapest costs 16 correct on closed 2I for 3 catches -> NOT BUILT (no SK->EN content-word map)'),
    ('C3', 'A2 FA 8/100 = 8.00 % [3.52, 15.16] = 7 dropped words (now, today, totally, Look!, off the plant, hot, in the room) + 1 doubtful; all M, L3 SAME, single ref'),
    ('B1', 'deterministic ref audit: SK read 1,824/4,064, refs compared 1,169, flags 92 on 83 rows (person 44, number 19, neuter 15, gender_fixed_open 9, contradiction 5); CZ flags 107 on 99 rows; 2 reader defects repaired in the audit only'),
    ('B2', 'model audit 3,200/4,064 SK rows (3,413 refs; p032-p040 not run, token cap): faithful 2,566, adds content 65, narrows 172, wrong person/gender 469, other 141; 1,414,860 headless tokens; Czech sized ~1.81-1.86M, not run'),
    ('B3', 'SK rows changed 577 (refs on them 643 -> 1,191): W added 385, N added 164, A replaced 60, dedup 1; listed only W 84, O 141, N 8, A 5; CZ 0 changed (99 B1 flags listed)'),
    ('B4', 'closed 2I set A+B: 474/497 = 95.37 % [93.14, 97.04] / FA 21/403 = 5.21 % [3.25, 7.86]; 101 calls, $0.012708'),
]
DEFECTS = [
    'reader_nom gaps found in B1 (3sg past gender None; CZ bys/jsi/jsem... not read; SK si + l-participle) - repaired in the audit only, not in the stack',
    'B3 word-swap gender variants (385 added) were never reviewed by a person or model; this analysis scans them deterministically (see B3 variant scan)',
    'B3 A-class replacements can damage a reference: exercise 22 ("slumped onto desk") and 54 ("... before a.") are in Part D and cost 2 FR + 2 FA',
    'RUN_COMMIT is one commit after FREEZE_COMMIT (the commit carrying FREEZE_COMMIT.txt), recorded in partD/RUN_COMMIT.txt',
    'S2c freeze-commit slip: a zsh word-split bug skipped the pre-run commit; the 0-call run used exactly the FROZEN_SHA files (shasum -c 0 mismatches), committed right after',
    'B2 coverage 3,200/4,064 SK rows (p032-p040 not audited, token cap); Part D sampled only audited rows',
    'C2 (dropped-content-word rule) not built: no deterministic Slovak content-word -> English map; cheapest variant cost 16 correct on the closed 2I set',
    '1S packet (183) has no references/labels -> not sizable for C2',
    'Czech: B1 CZ flags (107) listed, 0 corrected; B2 Czech not run (sized only)',
    'AG misfires on adjectival predicates (worn out, priced at, performed at the theatre): 5 FR in Part D, unfixed',
    'F3 still treats has got -> has as a dropped word (M1): 4 FR in Part D, unfixed',
    'AG annotation miss: A:1720 annotation says no nominative agent though "sestry" is the agent -> agent drop accepted',
]

# ------------------------------------------------------------------ numbers.json
NUM = {
    'label': 'Phase 2J Part D analysis (S9), fresh set opened once, fixed TRANSLATION-ONLY stack; 0 model calls in S9',
    'headline': HEAD, 'two_i': {k: {'cov': [v['cov'][0], v['cov'][1], v['cov'][2], list(v['cov'][3])],
                                    'fa': [v['fa'][0], v['fa'][1], v['fa'][2], list(v['fa'][3])]} for k, v in TWO_I_CELLS.items()},
    'FR': {'n': len(FRr), 'by_cause': dict(fr_c), 'by_layer': dict(fr_layer), 'cause_x_level': {k: dict(v) for k, v in fr_cxv.items()},
           'items': FRr, 'f4_misfires_left': f4_left, 'reference_caused': ref_fr,
           'on_b3_changed_rows': fr_b3, 'on_b3_rows_any': fr_b3_any, 'on_b3_gender_variant_rows': fr_b3_gender},
    'FA': {'n': len(FAr), 'by_cause': dict(fa_c), 'by_layer': dict(fa_layer), 'by_writer_type': dict(fa_wtype),
           'cause_x_level': {k: dict(v) for k, v in fa_cxv.items()}, 'items': FAr, 'reference_caused': sorted(REF_CAUSED_FA),
           'on_b3_changed_rows': fa_b3, 'on_b3_rows_any': fa_b3_any, 'on_b3_gender_variant_rows': fa_b3_gender, 'f4_layer': f4_fa},
    'two_i_causes': {'FR': FR_2I, 'FA': FA_2I},
    'b3_split': B3_SPLIT, 'set_rows_b3_changed': len(set_b3_changed_ex),
    'b3_scan': {'W_added': len(W_ADDED), 'nonpure_swap': len(nonpure), 'mixed_gender_new': len(mixed),
                'A_replaced': len(A_REPL), 'A_replaced_truncation_suspect': len(trunc),
                'nonpure_examples': [(d['exercise_id'], d['before'], d['after']) for d in nonpure[:10]],
                'mixed_examples': [(d['exercise_id'], d['before'], d['after']) for d in mixed[:10]],
                'trunc_examples': [(d['exercise_id'], d['before'], d['after']) for d in trunc[:15]],
                'bad_seen_in_part_d': BAD_SEEN},
    'judge': {'controls': '79/80', 'control_pairs': {'1-2': '15/15', '1-3': '10/10', '1-4': '14/15', '2-3': '15/15', '2-4': '10/10', '3-4': '15/15'},
              'intent_agree': [IA['agree'], IA['n']], 'confusion': IA['confusion_writer_to_judge']},
    'writer_type_accepted': {},
    'gemini': {'ledger': LED, 'counted_total_from_ledger': gem, 'spend_usd': 0.122434, 'cap_calls': 1200, 'cap_usd': 1.00},
    'tokens': {'headless': head_tok, 'agent_est_S1_S8': agent_tok, 'agent_est_S9': S9_AGENT_EST,
               'total_est': head_tok + agent_tok + S9_AGENT_EST, 'budget': 4000000},
    'parts': PARTS, 'defects': DEFECTS,
}
wt = defaultdict(lambda: Counter())
for j, i in I.items():
    t = i['writer_type'] or 'C'
    wt[t]['n'] += 1
    wt[t]['accepted'] += acc(j)
    wt[t]['judge_correct'] += is_correct(j)
    wt[t]['judge_correct_accepted'] += is_correct(j) and acc(j)
    wt[t]['judge_wrong_accepted'] += (not is_correct(j)) and acc(j)
NUM['writer_type_accepted'] = {k: dict(v) for k, v in sorted(wt.items())}
json.dump(NUM, open(os.path.join(OUT, 'numbers.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1, sort_keys=True)

# ------------------------------------------------------------------ ANALYSIS.md
L = []
w = L.append


def f_ci(c):
    return '%.2f [%.2f, %.2f]' % (c[0], c[1][0], c[1][1])


w('# Phase 2J - ANALYSIS (stage 9, 21.9.2026)\n')
w('Generated by `phase2j/analysis/analyze.py` from partD/run/results.jsonl, partD/set/items.jsonl (judge_label = truth), partD/judge/*, '
  'upload/B3_diff.jsonl, GEMINI_LEDGER.json, TOKENS.jsonl. 0 Gemini calls, 0 headless sessions. Numbers are computed; the per-item '
  'CAUSE is the S9 agent\'s own categorisation on 2I\'s cause list (hard-coded in analyze.py); extensions are marked "(extension 2J)". '
  'Intervals: exact 95 % Clopper-Pearson (2I\'s 89.13 [86.06, 91.73] / 4.71 [2.86, 7.26] reproduced by the same code). '
  'Coverage = accepted / judge-correct; FA = accepted / judge-wrong. Targets: coverage >= 90 %, FA <= 5 %.\n')
w('## 1 Headline - Part D (fresh 100 sentences, opened once) beside 2I\n')
w('| level | 2J coverage k/n | 2J coverage % [95 % CP] | cov >= 90 point / interval | 2J FA k/n | 2J FA % [95 % CP] | FA <= 5 point / interval | 2I coverage | 2I FA |')
w('|---|---|---|---|---|---|---|---|---|')
for lev in LEVELS + ['pooled']:
    h, t = HEAD[lev], TWO_I_CELLS[lev]
    w('| %s | %d/%d | %.2f [%.2f, %.2f] | %s / %s | %d/%d | %.2f [%.2f, %.2f] | %s / %s | %d/%d = %.2f [%.2f, %.2f] | %d/%d = %.2f [%.2f, %.2f] |' % (
        ('**pooled**' if lev == 'pooled' else lev), h['coverage']['x'], h['coverage']['n'], h['coverage']['pct'], *h['coverage']['cp95'],
        h['coverage']['point'], h['coverage']['interval'], h['fa']['x'], h['fa']['n'], h['fa']['pct'], *h['fa']['cp95'],
        h['fa']['point'], h['fa']['interval'], t['cov'][0], t['cov'][1], t['cov'][2], *t['cov'][3], t['fa'][0], t['fa'][1], t['fa'][2], *t['fa'][3]))
P = HEAD['pooled']
w('\nPooled: coverage %.2f %% [%.2f, %.2f] meets 90 %% on the point only (2I 89.13 %% missed it); FA %.2f %% [%.2f, %.2f] misses 5 %% on the point '
  'and the interval (2I 4.71 %% met it on the point). Different fresh sentences, so the change is not a paired effect. Per level: A2 and B2 clear 90 %% '
  'coverage on the point (95.20 %%), A1 87.90 %% and B1 83.06 %% miss; FA meets 5 %% only at A1 (2.97 %%); A2, B1, B2 sit at ~7 %%. No level meets any '
  'target on the interval except none (all FA intervals reach above 5 %%, all coverage lower bounds below 90 %%).\n' % (
      P['coverage']['pct'], *P['coverage']['cp95'], P['fa']['pct'], *P['fa']['cp95']))

w('## 2 Cause tables beside 2I\n')
w('### False rejections (%d of %d judge-correct)\n' % (len(FRr), P['coverage']['n']))
w('| cause | 2J FR | 2J rate of judge-correct | 2I FR (of 497) | 2I rate |\n|---|---|---|---|---|')
for c in FR_ORDER:
    if fr_c.get(c) or FR_2I.get(c):
        w('| %s | %d | %.2f %% | %d | %.2f %% |' % (c, fr_c.get(c, 0), pct(fr_c.get(c, 0), P['coverage']['n']), FR_2I.get(c, 0), pct(FR_2I.get(c, 0), 497)))
w('| **total** | **%d** | %.2f %% | **54** | 10.87 %% |' % (len(FRr), pct(len(FRr), P['coverage']['n'])))
w('\nFR by layer: ' + ', '.join('%s %d' % kv for kv in sorted(fr_layer.items())) + ' (2I: F4v2 24, L3 20, L3:TIPrej 6, F3 3, AG 1).')
w('\n| cause | A1 | A2 | B1 | B2 |\n|---|---|---|---|---|')
for c in FR_ORDER:
    if fr_c.get(c):
        w('| %s | %s |' % (c, ' | '.join(str(fr_cxv[c].get(l, '')) for l in LEVELS)))
w('\n### False acceptances (%d of %d judge-wrong)\n' % (len(FAr), P['fa']['n']))
w('| cause | 2J FA | 2J rate of judge-wrong | 2I FA (of 403) | 2I rate |\n|---|---|---|---|---|')
for c in FA_ORDER:
    if fa_c.get(c) or FA_2I.get(c):
        w('| %s | %d | %.2f %% | %d | %.2f %% |' % (c, fa_c.get(c, 0), pct(fa_c.get(c, 0), P['fa']['n']), FA_2I.get(c, 0), pct(FA_2I.get(c, 0), 403)))
w('| **total** | **%d** | %.2f %% | **19** | 4.71 %% |' % (len(FAr), pct(len(FAr), P['fa']['n'])))
w('\nFA by layer: all %d L3 (reply SAME). By writer type: ' % len(FAr) + ', '.join('%s %d' % kv for kv in sorted(fa_wtype.items())) +
  ' (2I: M 16, intent-correct 3). New vs 2I: one agent drop and one time-frame shift were accepted (2I had none).')
w('\n| cause | A1 | A2 | B1 | B2 |\n|---|---|---|---|---|')
for c in FA_ORDER:
    if fa_c.get(c):
        w('| %s | %s |' % (c, ' | '.join(str(fa_cxv[c].get(l, '')) for l in LEVELS)))

w('\n### The specific counts asked for\n')
w('- F4v2 / F4v3 misfires left: **%d** FR (2I 24), %d FA on those layers. The Part A fix held on fresh sentences.' % (f4_left, f4_fa))
w('- Reference-caused FR ("%s"): **%d** of %d (2I 16 of 54) - now the largest FR cause. Reference-caused FA: %d (%s).' % (
    C_REF, ref_fr, len(FRr), len(REF_CAUSED_FA), ', '.join(sorted(REF_CAUSED_FA))))
w('- Part D rows with a B3-changed reference: %d of 100 sentences. FR on B3-changed rows: %d (%s); FA on B3-changed rows: %d (%s).' % (
    len(set_b3_changed_ex), len(fr_b3), ', '.join(fr_b3), len(fa_b3), ', '.join(fa_b3)))
w('- FR / FA on rows with a B3 word-swap gender variant: %d FR (%s), %d FA (%s). On these the swapped variant itself was well-formed; the '
  'rejection came from something else (tense, synonym, a second gender/person the swap did not cover, or L3 ignoring a matching variant).' % (
      len(fr_b3_gender), ', '.join(fr_b3_gender), len(fa_b3_gender), ', '.join(fa_b3_gender)))
w('- Rates on B3-changed vs other rows: coverage %d/%d = %.2f %% vs %d/%d = %.2f %%; FA %d/%d = %.2f %% vs %d/%d = %.2f %%.' % (
    *B3_SPLIT['b3_changed_rows']['cov'], *B3_SPLIT['other_rows']['cov'], *B3_SPLIT['b3_changed_rows']['fa'], *B3_SPLIT['other_rows']['fa']))
w('- **Bad B3 references seen in Part D** (both A-class replacements, not gender swaps): ' + '; '.join('ex %d: %s' % kv for kv in BAD_SEEN.items()) +
  '. Together they cost A:22:c4, A:54:c3 (FR) and A:54:m, A:54:t (FA).')
w('- B3 variant scan over all SK changes (deterministic): W-added %d, of which not a pure pronoun swap %d, newly mixed he+she %d (review candidates, '
  'can be legitimate with two people); A-replaced %d, truncation/missing-determiner suspects %d.' % (len(W_ADDED), len(nonpure), len(mixed), len(A_REPL), len(trunc)))
for tag, lst in (('not pure swap', nonpure[:10]), ('mixed he+she', mixed[:10]), ('A-replacement suspect', trunc[:15])):
    for d in lst:
        w('  - %s ex %s: "%s" -> "%s"' % (tag, d['exercise_id'], esc(d['before']), esc(d.get('after'))))

w('\n## 3 Every false rejection (%d)\n' % len(FRr))
w('| # | jid | level | Slovak | reference(s) | answer | layer | L3 | judge | cause | note | B3 |\n|---|---|---|---|---|---|---|---|---|---|---|---|')
for n, x in enumerate(FRr, 1):
    w('| %d | %s | %s | %s | %s | %s | %s | %s | %s: %s | %s | %s | %s |' % (
        n, x['jid'], x['level'], esc(x['slovak']), esc(' ‖ '.join(x['refs'])), esc(x['answer']), x['layer'], x['l3_reply'] or '-',
        x['judge_label'], esc(x['judge_reason']), x['cause'], esc(x['note']), x['b3']))
w('\n## 4 Every false acceptance (%d)\n' % len(FAr))
w('| # | jid | level | Slovak | reference(s) | answer | writer | layer | L3 | judge | cause | note | B3 |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|')
for n, x in enumerate(FAr, 1):
    w('| %d | %s | %s | %s | %s | %s | %s | %s | %s | %s: %s | %s | %s | %s |' % (
        n, x['jid'], x['level'], esc(x['slovak']), esc(' ‖ '.join(x['refs'])), esc(x['answer']), x['writer_type'], x['layer'],
        x['l3_reply'] or '-', x['judge_label'], esc(x['judge_reason']), x['cause'], esc(x['note']), x['b3']))

w('\n## 5 Judge noise and writer types\n')
w('Hidden duplicate controls **79/80** (2I 80/80); pairs ' + ', '.join('%s %s' % kv for kv in NUM['judge']['control_pairs'].items()) + '.')
w('Judge vs writer intent: %d/%d agree; confusion %s.\n' % (IA['agree'], IA['n'], json.dumps(IA['confusion_writer_to_judge'])))
w('| writer type | n | judge-correct | accepted | accepted & judge-correct | accepted & judge-wrong |\n|---|---|---|---|---|---|')
for k, v in NUM['writer_type_accepted'].items():
    w('| %s | %d | %d | %d | %d | %d |' % ({'C': 'correct (c1-c5)'}.get(k, k), v['n'], v['judge_correct'], v['accepted'], v['judge_correct_accepted'], v['judge_wrong_accepted']))
w('\nM (dropped word) is the only writer type the stack lets through in number: %d of its judge-wrong answers accepted.' % wt['M']['judge_wrong_accepted'])

w('\n## 6 Parts A / B / C, cost, tokens, defects\n')
w('| part | result |\n|---|---|')
for k, v in PARTS:
    w('| %s | %s |' % (k, esc(v)))
w('| D | %d/%d = %.2f %% [%.2f, %.2f] / FA %d/%d = %.2f %% [%.2f, %.2f]; 833 counted calls, $0.104052, opened once |' % (
    P['coverage']['x'], P['coverage']['n'], P['coverage']['pct'], *P['coverage']['cp95'], P['fa']['x'], P['fa']['n'], P['fa']['pct'], *P['fa']['cp95']))
w('\nGemini: ledger %s -> %s counted of the 1,200 cap; spend $0.122434 of $1.00 (S2 0.005674 + S5 0.012708 + S8 0.104052).' % (
    json.dumps(LED), gem))
w('Claude tokens: headless %s (B2 1,414,860 + writers 225,497 + judges 340,352); agent estimates S1-S8 %s + S9 ~%s = total ~%s of 4,000,000.' % (
    format(head_tok, ','), format(agent_tok, ','), format(S9_AGENT_EST, ','), format(head_tok + agent_tok + S9_AGENT_EST, ',')))
w('\n### Defects recorded, not fixed\n')
for d in DEFECTS:
    w('- ' + d)
open(os.path.join(OUT, 'ANALYSIS.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print(json.dumps({'cov': P['coverage'], 'fa': P['fa'], 'fr': dict(fr_c), 'fa_c': dict(fa_c), 'f4_left': f4_left,
                  'fr_b3': fr_b3, 'fa_b3': fa_b3, 'scan': NUM['b3_scan']['W_added'], 'nonpure': len(nonpure), 'mixed': len(mixed),
                  'trunc': len(trunc), 'gem': gem, 'wt': NUM['writer_type_accepted']}, ensure_ascii=False))

# Task C+E (Phase 1O) analysis over diag/ce_dump.json (built by ce_build.py). 0 model calls, stdlib only.
import json, os, re, math, random, collections, time
D = os.path.dirname(os.path.abspath(__file__)); O = os.path.dirname(D)
rows = json.load(open(os.path.join(D, 'ce_dump.json')))
open(os.path.join(O, 'access_log.jsonl'), 'a').write(json.dumps({'ts': time.strftime('%Y-%m-%dT%H:%M:%S'), 'side': 'taskCE', 'what': 'phase1o/diag/ce_dump.json (judged-correct items of 1N and 1M, derived)', 'caller': 'phase1o/diag/ce_analyse.py', 'n': len(rows), 'purpose': 'Task C+E tables, C3 distance analysis, E ceilings'}) + '\n')
# ---------- manual classification: id -> "CAUSE|E|flags|rationale"; flags: letter = optimistic ceiling member, letter+ = also conservative
M = {}
def add(s):
    for l in s.strip().split('\n'):
        i, c, e, f, r = [x.strip() for x in l.split('|', 4)]; M[i] = (c, e, f, r)
add('''C:160003:3732307761|DET|E3|b+ c+|sole difference that->the; equals stored v2 up to alt whole/entire; model DIFF against v1
C:160003:3517424121|PASS_BY|E2||by-passive with "by us"; F4v2 subject guard fires before the model
C:160012:344299418|DET|E3|c|those->the plus stored alt "door handles"; both stored variants say "those"
C:160012:2722403593|TENSE|E3|c|"is going to be polishing" vs will; bude lestit does not fix will / going to; also those->the
C:160012:2176442930|PASS_AGENTLESS|E2||agentless passive (label regime of 1N); agent Zuzana dropped
C:160013:2559106042|DROP|E5a||recombination of v1 and v2 (+alt cauldron); F5 sees a subsequence of v2 minus "in the": guard artefact, reference adequate
C:160013:2228538754|STRUCT|E2|b|fronted time adverbial, the/cauldron as in v2
W:160013:1795021316|LEX|E4||"pot" for kotol, written as a wrong word; judge generous
C:160015:3892272793|DROP|E1|a|refs say "all the way UP to"/"right up to"; Slovak "az k" has no "up"; answer without "up" -> F5; those->the would remain for L3
W:160015:3861351230|DROP|E5b||drops "az" (all the way): minor Slovak element omitted, judge tolerates, F5 does not
C:160017:1584049848|DROP|E2|b c|optional "that" omitted + alt words + tu->the; equals v2 up to alt and "that"
C:160020:3352119485|PASS_AGENTLESS|E2||agentless passive
W:160020:3986763842|TENSE|E3|c|past simple with "already" for past perfect on a tense_open sentence
W:160020:81015253|DROP|E5b||drops "already" (uz): minor element omitted, F5
W:160021:356150325|DROP|E4||drops "only" (az po = only after): meaning changes; judge generous
C:160024:2621707485|PASS_AGENTLESS|E2||agentless passive, "without any help" for sama
C:160026:853452892|TENSE|E3||past simple "translated ... until" for imperfective past; F2B tense guard on a tense_open sentence; a guard, not reachable by reference work
C:160028:1479798515|DROP|E1|a+|v2 says "take ... OUT to the container"; odniest has no "out"; without it the answer equals v2 exactly (L1 match)
C:160032:3731940252|STRUCT|E2|b|adverbial position (v2 order) + alt "properly"
C:160033:1495618468|LEX|E2|b|"sold the whole edition" for "sold out"; "told us ... already last year" as in v2/v3
C:160035:1168408523|LEX|E4||"putting" for pribija (nailing): manner lost; judge generous
C:160036:2901324230|PASS_AGENTLESS|E2||agentless passive
C:160038:3120993943|DROP|E1|a|refs "sheet of paper"/"piece of paper"; Slovak only "papier"; answer "the big paper" is a subsequence -> F5; that->the would remain
C:160038:4030922795|DROP|E2||drops "right now" (prave); the present continuous already carries it; F5
C:160040:3346784148|PASS_AGENTLESS|E2||agentless passive
C:160041:2099850102|LEX|E2||"in the wardrobe" for zo skrine; carry/backpack are stored alts
W:160042:2501266784|TENSE|E4||present simple "doesn't put ... until Monday" for a perfective future; writer TF error, judge generous
C:160044:1984378852|PASS_AGENTLESS|E2||agentless passive
C:160045:3626274490|DROP|E5b||drops "to us" (nam): minor element omitted, F5
C:160046:1206550562|PASS_BY|E2||by-passive, F4v2
C:160048:2251836920|PASS_AGENTLESS|E2||agentless passive
C:160049:3068188043|DET|E3|b c+|sole difference that->the; v2 has "the old alarm clock"
C:160050:968854585|DROP|E5b||drops "to us" (nam), F5
C:160051:2890458528|STRUCT|E2||Slovak passive rendered active "Someone had covered"
C:160051:3911354398|STRUCT|E2||Slovak passive rendered active "They had already covered"
C:160052:1176203340|PASS_AGENTLESS|E2||agentless passive
C:160053:703629798|DROP|E4||"the floor" for parket: content dropped, not a stored alt; F5
W:160053:337807729|DROP|E4||drops "parquet" and "straight" (v kuse); F5
C:160058:7291403|STRUCT|E2||"They stop working" for impersonal "sa uz nepracuje"
C:160058:3087519118|STRUCT|E2||generic "You don't work" for the impersonal
C:160060:4058632457|PASS_AGENTLESS|E2||agentless passive
C:160061:1686335759|DET|E3|b c+|sole difference those->the; v2 has "the new chairs"
C:160064:489138833|PASS_AGENTLESS|E2||agentless passive
C:160065:390080876|DET|E3|b c+|sole difference that->the (gate); v2 has "the gate"
W:160066:3107568222|TENSE|E4||present "have to" for budes musiet; judge-noise control disagreed on this id
C:160069:3501270450|PASS_BY|E2||by-passive, F4v2
W:160072:3478128531|TENSE|E4||future continuous for perfective posklada; writer T error
C:160074:1840606533|CLEFT|E2||"It must have been someone who changed the lock"
C:160076:306125269|PASS_BY|E2||by-passive, F4v2
C:160076:1794710932|PASS_AGENTLESS|E2||agentless passive, F4v2
W:160076:167794355|TENSE|E4||future continuous for perfective nafuka
C:160077:3518405772|DET|E3|b c+|sole difference those->the; v2 has "the letters"
C:160077:2678752144|LEX|E5a|b c|recombination of v1/v2 + stored alts (placed, covers) with "into"; inside the annotation, model DIFF
W:160079:812730797|TENSE|E4||"will hang" for a habitual present; writer TF error
C:160080:1527877606|PASS_BY|E2||by-passive, F4v2
C:160080:488008841|PASS_AGENTLESS|E2||agentless passive, F4v2
C:160082:210208198|DET|E3|b c|those->the, a->the, stored alt glasses
C:160082:4084815432|LEX|E2||"glass cups", "the crate", "right now" moved to the end
C:160082:266462698|LEX|E2|b c|"placing" for putting/packing, otherwise v2 with the/a
W:160082:1193922532|DET|E3|b c|"those glass jars" -> "the glasses" (stored alt)
C:160084:2484737775|PASS_AGENTLESS|E2||agentless passive
C:160085:2327882461|DET|E3|b c+|sole difference those->the; v2 has "the old magazines"
C:160085:2711421013|DET|E3|b c|those->the plus "up into"
C:160088:2020139039|PASS_AGENTLESS|E2||agentless passive
W:160088:148507747|LEX|E5a|b|"flutes" is a stored alt of whistles; model TIP anyway
W:160089:4106768492|DET|E5a|b+ c|equals v2 up to stored alts (lend, city museum); model DIFF against v1
C:160093:1903262848|LEX|E2||"skimmed through" not among the stored alts
C:160095:3693460798|DROP|E5b||drops "to us" (nam), F5
C:160096:4258255142|PASS_AGENTLESS|E2||agentless passive, also drops "ourselves"
W:160096:962295857|TENSE|E4||future continuous for perfective upevnime
C:160098:3632261589|DET|E3|c+|hodiny is plurale tantum: clock vs clocks; equals v3 but singular
C:160098:3538444671|DET|E3|c+|singular "the old clock is wound"; equals v1 but singular
C:160098:967233374|STRUCT|E3|c|singular clock + "someone winds" + reordering
C:160098:1885236053|DET|E3|c|singular clock + get-passive
C:160099:470727688|DET|E3|b c+|sole difference that->the (facade)
C:160100:3987111647|PASS_AGENTLESS|E2||agentless passive
W:150003:1432921193|LEX|E4||"from morning" for since; judge generous
C:150010:114744633|DET|E3||sole difference that->the; single stored reference
C:150010:3082912481|DROP|E5c||"even before" renders "este", which the single reference omits
C:150010:2104232765|TENSE|E3||past perfect + the
C:150020:3548556660|LEX|E2||"in our car within two hours"
C:150022:1356366378|DET|E3||sole difference those->the
C:150023:3677605260|TENSE|E3||present perfect simple for continuous; F2B
W:150024:3321815494|TENSE|E3||Slovak keby + by underdetermines present vs past unreal
C:150025:2769794712|STRUCT|E2||neg-raising "I don't think she has seen"
C:150031:554688955|TENSE|E3||"will finish" (tense of stored v2) in v1 order
C:150042:2458724250|DROP|E5b||drops "back/still" (este); F5
C:150047:3674302762|DROP|E2||"is on the radio" for "is played on the radio"; F5
C:150048:4174354734|LEX|E2||told for explained + "has to"
C:150054:3047262874|DROP|E5a||F8 misfire: optional "that"; the model said SAME
C:150054:2062420610|STRUCT|E5a||F8 misfire; the model said SAME
C:150054:811753297|LEX|E5a||F8 misfire on stored alts; the model said SAME
C:150058:4207449293|TENSE|E3||"has led" for has been leading; F2B
W:150058:1688612944|STRUCT|E4||"That team has had a new coach since September": meaning shifts; judge-noise id
W:150059:1376813231|TENSE|E3||third conditional; Slovak keby + by underdetermines
C:150060:3053978857|LEX|E5a||equals v2 up to stored alt "if"
C:150067:1467391870|TENSE|E3||no backshift + the
C:150069:1333247902|DROP|E5b||drops "number" (cislo); F5
C:150093:3620610463|TENSE|E3||"has looked after" for has been managing; F2B
C:150100:1314747791|STRUCT|E2||adverb position: "closes at four p.m. already"
C:150100:3939353743|LEX|E2||"shuts"
C:150102:2020804170|LEX|E5a||equals v2 up to stored alts
C:150109:4255028795|TENSE|E4||present continuous for a habitual
C:150113:2293516181|DROP|E5a||"finished" is a stored alt of "finished reading"; F5 fires anyway
C:150114:3835165800|LEX|E2||"every guest was"
C:150120:3953482596|DROP|E2||"lookout" for lookout tower; F5
C:150121:3878993162|TENSE|E3||"will go through" (v2 tense) with v1 wording
W:150129:3445682697|TENSE|E3||second conditional where refs have third; Slovak underdetermines
C:150133:1479544414|TENSE|E3||"will repair" (v2 tense) with v1 wording
C:150135:3096629094|STRUCT|E2||"In this bend you drive very carefully"
W:150035:3103579073|LEX|E4||"from morning" for since; judge generous''')
CLEFT = re.compile(r"^(it is|it was|it's|it must have been) .*\b(who|that)\b|^what .*\b(was|is) that\b", re.I)
# ---------- CP interval
def _lb(k, n, p):
    return math.exp(math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1) + (k * math.log(p) if k else 0) + ((n - k) * math.log(1 - p) if n - k else 0))
def cdf(k, n, p): return sum(_lb(i, n, p) for i in range(0, k + 1))
def cp(k, n, a=0.05):
    if n == 0: return (0, 0)
    def solve(f):
        lo, hi = 1e-12, 1 - 1e-12
        for _ in range(60):
            mid = (lo + hi) / 2
            if f(mid): lo = mid
            else: hi = mid
        return (lo + hi) / 2
    L = 0.0 if k == 0 else solve(lambda p: 1 - cdf(k - 1, n, p) < a / 2)
    U = 1.0 if k == n else solve(lambda p: cdf(k, n, p) > a / 2)
    return (round(100 * L, 2), round(100 * U, 2))
def R(k, n): return '%d/%d = %.2f%% [%.2f, %.2f]' % ((k, n, 100.0 * k / n) + cp(k, n)) if n else '0/0'
# ---------- text
CON = [("won't", 'will not'), ("can't", 'can not'), ("n't", ' not'), ("'ll", ' will'), ("'re", ' are'), ("'ve", ' have'), ("'m", ' am'), ("it's", 'it is'), ("he's", 'he is'), ("she's", 'she is'), ("that's", 'that is'), ("what's", 'what is')]
SP = {'colored': 'coloured', 'woolen': 'woollen', 'canceled': 'cancelled', 'shoveled': 'shovelled', 'catalogs': 'catalogues', 'neighbors': 'neighbours', 'center': 'centre'}
def tok(s):
    s = s.lower().replace('’', "'")
    for a, b in CON: s = s.replace(a, b)
    s = re.sub(r"[^a-z0-9' ]", ' ', s)
    return [SP.get(t, t) for t in s.replace("'", ' ').split()]
def altmap(alt):
    m = []
    for k, vs in (alt or {}).items():
        kt = tok(k)
        for v in vs or []:
            vt = tok(v)
            if vt and vt != kt: m.append((vt, kt))
    return sorted(m, key=lambda x: -len(x[0]))
def altnorm(t, m):
    out, i = [], 0
    while i < len(t):
        for vt, kt in m:
            if t[i:i + len(vt)] == vt and t[i:i + len(kt)] != kt:
                out += kt; i += len(vt); break
        else:
            out.append(t[i]); i += 1
    return out
def lev(a, b):
    p = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        c = [i]
        for j, y in enumerate(b, 1): c.append(min(p[j] + 1, c[j - 1] + 1, p[j - 1] + (x != y)))
        p = c
    return p[-1]
FUNC = set('a an the this that these those i you he she it we they me him her us them my your his its our their mine yours ours theirs myself yourself himself herself ourselves themselves is am are was were be been being do does did have has had will would shall should can could may might must to of in on at by for from with into onto up out off over under about as and or but if whether than then so not no who whom which what when while there here very just only still already yet also too all some any'.split())
PP = r"(\w+ed|\w+en|put|set|cut|built|brought|bought|sold|told|made|done|run|lent|sent|kept|left|taken|given|written|wound|hung|read|paid|held|found|swept|taught|caught|worn|sung|fed|led)"
PASS = re.compile(r"\b(am|is|are|was|were|be|been|being|get|gets|got)\b( \w+ly| not| already| still| always| usually| just)* " + PP + r"\b")
DEM = set('ten tá tie tú toho tej tom tým tých tento táto tieto túto tomu tými'.split())
for x in rows:
    m = altmap(x['alt']); a = altnorm(tok(x['answer']), m)
    best = None
    for r in x['refs']:
        rt = altnorm(tok(r), m); d = lev(a, rt)
        dn = d / max(len(a), len(rt))
        if best is None or dn < best[0]: best = (dn, d, rt, r)
    x['ntok'] = len(tok(x['answer'])); x['dist'] = best[0]; x['lev'] = best[1]
    st = lambda w: re.sub(r'(ing|ed|es|s)$', '', w)
    rs = {st(w) for w in best[2]}
    x['absent'] = sum(1 for w in a if w not in FUNC and st(w) not in rs)
    ap, rp = bool(PASS.search(' '.join(a))), bool(PASS.search(' '.join(best[2])))
    x['voice_mis'] = ap != rp
    x['open_mis'] = a[:2] != best[2][:2]
    x['far'] = best[0] >= 0.35
    x['struct'] = x['far'] or x['voice_mis'] or x['open_mis']
    x['cleft'] = bool(CLEFT.search(x['answer'].lower().replace('’', "'")))
    x['passive'] = (x['passive_w'] is not None or x['passive_j'] is not None) if x['set'] == '1n' else (ap and not rp)
    r0 = tok(x['refs'][0]); a0 = tok(x['answer'])
    nd = lambda t: sum(1 for i, w in enumerate(t) if w in ('those', 'these') or (w in ('that', 'this') and i + 1 < len(t) and t[i + 1] not in FUNC))
    x['sk_dem'] = any(w.strip('.,!?').lower() in DEM for w in x['sk'].split())
    x['det_swap'] = nd(r0) > nd(a0)
    x['l1'] = x['chk_step'] == 'match'
S = {'1n': [x for x in rows if x['set'] == '1n'], '1m': [x for x in rows if x['set'] == '1m']}
fr = [x for x in rows if not x['accepted']]
for x in fr:
    if x['id'] not in M:
        assert x['set'] == '1m' and x['cleft'] and x['intent'] == 'V', x['id']
        M[x['id']] = ('CLEFT', 'E2', '', 'it-cleft / pseudo-cleft of a writer-V item that the 1M judge called correct; focus construction, meaning kept')
    x['cause'], x['E'], x['flags'], x['why'] = M[x['id']]
assert len([x for x in fr if x['set'] == '1n']) == 76 and len([x for x in fr if x['set'] == '1m']) == 67 and set(M) == {x['id'] for x in fr}
SUB = collections.OrderedDict([('ALL', lambda x: True), ('NONPASS', lambda x: not x['passive']), ('NONPASS_NONCLEFT', lambda x: not x['passive'] and not x['cleft']), ('WRITER_C_NONPASS', lambda x: not x['passive'] and x['intent'] == 'C')])
out = {}
print('## denominators / coverage by subset')
for sn, f in SUB.items():
    for s in ('1m', '1n'):
        it = [x for x in S[s] if f(x)]; print('  %-17s %s coverage %s' % (sn, s, R(sum(x['accepted'] for x in it), len(it))))
print('  1m judged-correct: regex-passive %d, cleft %d (accepted %d) ; 1n cleft %d (accepted %d)' % (sum(x['passive'] for x in S['1m']), sum(x['cleft'] for x in S['1m']), sum(x['cleft'] and x['accepted'] for x in S['1m']), sum(x['cleft'] for x in S['1n']), sum(x['cleft'] and x['accepted'] for x in S['1n'])))
print('  intents of judged-correct: 1m %s | 1n %s' % (dict(collections.Counter(x['intent'] for x in S['1m'])), dict(collections.Counter(x['intent'] for x in S['1n']))))
LAY = ['L3', 'L3:TIPrej', 'F5', 'F4v2', 'F2B', 'F8']; CAU = ['DET', 'TENSE', 'PASS_AGENTLESS', 'PASS_BY', 'CLEFT', 'LEX', 'STRUCT', 'DROP']
tab = {}
for sn in ('ALL', 'NONPASS', 'NONPASS_NONCLEFT'):
    print('## FR by cause x layer, subset %s (count; rate %% of judged-correct in subset)' % sn)
    for s in ('1m', '1n'):
        n = len([x for x in S[s] if SUB[sn](x)]); f = [x for x in fr if x['set'] == s and SUB[sn](x)]
        print('  %s n=%d FR=%d' % (s, n, len(f)))
        for c in CAU:
            cc = [x for x in f if x['cause'] == c]
            print('    %-15s %2d %5.2f%%  | %s' % (c, len(cc), 100.0 * len(cc) / n, ' '.join('%s=%d' % (l, sum(x['layer'] == l for x in cc)) for l in LAY if any(x['layer'] == l for x in cc))))
            tab['%s/%s/%s' % (sn, s, c)] = {l: sum(x['layer'] == l for x in cc) for l in LAY}
        print('    by layer: ' + '  '.join('%s %d (%.2f%%)' % (l, sum(x['layer'] == l for x in f), 100.0 * sum(x['layer'] == l for x in f) / n) for l in LAY))
        tab['%s/%s/n' % (sn, s)] = n
print('## E buckets (count, % of FR of the set)')
for s in ('1m', '1n'):
    f = [x for x in fr if x['set'] == s]; c = collections.Counter(x['E'] for x in f)
    print('  %s: %s | merged E5 %d | nonpassive-noncleft: %s' % (s, dict(sorted(c.items())), sum(v for k, v in c.items() if k.startswith('E5')), dict(sorted(collections.Counter(x['E'] for x in f if not x['passive'] and not x['cleft']).items()))))
    print('     E x layer: ' + ' ; '.join('%s{%s}' % (e, ','.join('%s:%d' % (l, sum(1 for x in f if x['E'] == e and x['layer'] == l)) for l in LAY if any(x['E'] == e and x['layer'] == l for x in f))) for e in sorted(c)))
print('## ceilings 1N (base 350/426)')
f1 = [x for x in fr if x['set'] == '1n']
for L in 'abc':
    opt = [x for x in f1 if re.search(L + r'\+?(\s|$)', x['flags'])]; con = [x for x in f1 if (L + '+') in x['flags']]
    x_ = [y for y in f1 if L in y['flags'].replace('+', '').split()]
    print('  (%s) conservative +%d -> %s ; optimistic +%d -> %s' % (L, len(con), R(350 + len(con), 426), len(x_), R(350 + len(x_), 426)))
    out['ceil_' + L] = {'cons': len(con), 'opt': len(x_)}
un_o = [y for y in f1 if y['flags'].strip()]; un_c = [y for y in f1 if '+' in y['flags']]
mid_b = [y for y in f1 if 'b' in y['flags'].replace('+', '').split() and y['cause'] == 'DET' or 'b+' in y['flags']]
print('  union a|b|c: conservative +%d -> %s ; optimistic +%d -> %s ; (b) central (DET-only or exact variant) +%d -> %s' % (len(un_c), R(350 + len(un_c), 426), len(un_o), R(350 + len(un_o), 426), len(mid_b), R(350 + len(mid_b), 426)))
print('  overlap b&c optimistic %d ; layers of optimistic union %s' % (sum(1 for y in f1 if {'b', 'c'} <= set(y['flags'].replace('+', '').split())), dict(collections.Counter(y['layer'] for y in un_o))))
print('## F5 detail'); 
for s in ('1m', '1n'):
    for x in fr:
        if x['set'] == s and x['layer'] == 'F5': print('  %s %s [%s/%s] lev=%d %s' % (s, x['id'], x['cause'], x['E'], x['lev'], x['answer'][:70]))
for s in ('1m', '1n'):
    it = [x for x in S[s] if not x['passive'] and not x['l1']]
    sub = [x for x in it if 0 < x['lev'] <= 3 and x['dist'] < 0.2]
    print('  %s non-passive non-L1 items with lev 1-3: %d (%.1f%% of judged-correct %d); F5-rejected among them %d' % (s, len(sub), 100.0 * len(sub) / len(S[s]), len(S[s]), sum(x['layer'] == 'F5' for x in sub)))
print('## DET swap (ref[0] has that/those + noun, answer has fewer), non-passive non-cleft')
for s in ('1m', '1n'):
    it = [x for x in S[s] if not x['passive'] and not x['cleft']]
    sw = [x for x in it if x['det_swap']]; ns = [x for x in it if not x['det_swap']]
    print('  %s sentences with Slovak demonstrative %d/%d ; items det_swap %d/%d = %.1f%% ; acceptance det_swap %s ; no swap %s' % (s, len({x['sid'] for x in S[s] if x['sk_dem']}), len({x['sid'] for x in S[s]}), len(sw), len(it), 100.0 * len(sw) / len(it), R(sum(x['accepted'] for x in sw), len(sw)), R(sum(x['accepted'] for x in ns), len(ns))))
    sw3 = [x for x in sw if x['verdict']]; print('     of det_swap items reaching the model %d: %s' % (len(sw3), dict(collections.Counter(x['verdict'] for x in sw3))))
# ---------- C3
random.seed(1505)
def mean(v): return sum(v) / len(v) if v else float('nan')
def med(v): v = sorted(v); n = len(v); return (v[n // 2] if n % 2 else (v[n // 2 - 1] + v[n // 2]) / 2) if n else float('nan')
def clusters(it):
    d = collections.defaultdict(list)
    for x in it: d[x['sid']].append(x)
    return list(d.values())
def boot(itm, itn, stat, B=1000):
    cm, cn = clusters(itm), clusters(itn); ds = []
    for _ in range(B):
        a = [x for c in random.choices(cm, k=len(cm)) for x in c]; b = [x for c in random.choices(cn, k=len(cn)) for x in c]
        ds.append(stat(b) - stat(a))
    ds.sort(); return ds[int(0.025 * B)], ds[int(0.975 * B) - 1]
METR = [('tokens', lambda x: x['ntok']), ('dist', lambda x: x['dist']), ('lev', lambda x: x['lev']), ('absent_content', lambda x: x['absent']), ('struct_proxy', lambda x: 1.0 * x['struct']), ('far>=.35', lambda x: 1.0 * x['far']), ('voice_mismatch', lambda x: 1.0 * x['voice_mis']), ('opening_differs', lambda x: 1.0 * x['open_mis']), ('L1_match', lambda x: 1.0 * x['l1'])]
for sn in ('ALL', 'NONPASS', 'NONPASS_NONCLEFT', 'WRITER_C_NONPASS'):
    a = [x for x in S['1m'] if SUB[sn](x)]; b = [x for x in S['1n'] if SUB[sn](x)]
    print('## C3 %s: n 1m=%d 1n=%d  (mean | median ; diff of means 1N-1M with sentence-cluster bootstrap 95%%)' % (sn, len(a), len(b)))
    for name, g in METR:
        lo, hi = boot(a, b, lambda it: mean([g(x) for x in it]), 600)
        print('   %-16s 1m %.3f | %.3f   1n %.3f | %.3f   diff %+.3f [%+.3f, %+.3f]' % (name, mean([g(x) for x in a]), med([g(x) for x in a]), mean([g(x) for x in b]), med([g(x) for x in b]), mean([g(x) for x in b]) - mean([g(x) for x in a]), lo, hi))
BINS = [(-1, 0.0, 'd=0'), (0.0, 0.1, '(0,.1]'), (0.1, 0.2, '(.1,.2]'), (0.2, 0.3, '(.2,.3]'), (0.3, 0.45, '(.3,.45]'), (0.45, 9, '>.45')]
def binof(x):
    for i, (lo, hi, _) in enumerate(BINS):
        if lo < x['dist'] <= hi: return i
def decomp(a, b):
    na, nb = len(a), len(b); res = {}
    wa = [sum(binof(x) == i for x in a) / na for i in range(len(BINS))]; wb = [sum(binof(x) == i for x in b) / nb for i in range(len(BINS))]
    ra = [mean([x['accepted'] for x in a if binof(x) == i]) for i in range(len(BINS))]; rb = [mean([x['accepted'] for x in b if binof(x) == i]) for i in range(len(BINS))]
    pool = [mean([x['accepted'] for x in a + b if binof(x) == i]) for i in range(len(BINS))]
    fa = [r if r == r else p for r, p in zip(ra, pool)]; fb = [r if r == r else p for r, p in zip(rb, pool)]
    ca, cb = sum(w * r for w, r in zip(wa, fa)), sum(w * r for w, r in zip(wb, fb))
    n_at_m = sum(w * r for w, r in zip(wa, fb)); m_at_n = sum(w * r for w, r in zip(wb, fa))
    return {'cov_m': ca, 'cov_n': cb, 'gap': ca - cb, 'n_rates_at_m_mix': n_at_m, 'm_rates_at_n_mix': m_at_n, 'composition_A(1N reweighted to 1M mix)': n_at_m - cb, 'composition_B(1M reweighted to 1N mix)': ca - m_at_n, 'within_A': ca - n_at_m, 'within_B': m_at_n - cb, 'wa': wa, 'wb': wb, 'ra': ra, 'rb': rb}
for sn in ('ALL', 'NONPASS', 'NONPASS_NONCLEFT', 'WRITER_C_NONPASS'):
    a = [x for x in S['1m'] if SUB[sn](x)]; b = [x for x in S['1n'] if SUB[sn](x)]
    d = decomp(a, b); out['decomp_' + sn] = d
    print('## C3 bins %s: gap %.2f pts ; composition A %.2f / B %.2f ; within A %.2f / B %.2f' % (sn, 100 * d['gap'], 100 * d['composition_A(1N reweighted to 1M mix)'], 100 * d['composition_B(1M reweighted to 1N mix)'], 100 * d['within_A'], 100 * d['within_B']))
    for i, (_, _, lab) in enumerate(BINS):
        ka, na_ = sum(x['accepted'] for x in a if binof(x) == i), sum(1 for x in a if binof(x) == i); kb, nb_ = sum(x['accepted'] for x in b if binof(x) == i), sum(1 for x in b if binof(x) == i)
        print('    %-9s 1m mix %5.1f%% acc %-34s | 1n mix %5.1f%% acc %s' % (lab, 100 * d['wa'][i], R(ka, na_), 100 * d['wb'][i], R(kb, nb_)))
    cm, cn = clusters(a), clusters(b); cs, ws = [], []
    for _ in range(600):
        aa = [x for c in random.choices(cm, k=len(cm)) for x in c]; bb = [x for c in random.choices(cn, k=len(cn)) for x in c]
        dd = decomp(aa, bb); cs.append(100 * (dd['composition_A(1N reweighted to 1M mix)'] + dd['composition_B(1M reweighted to 1N mix)']) / 2); ws.append(100 * (dd['within_A'] + dd['within_B']) / 2)
    cs.sort(); ws.sort(); print('    bootstrap (sentence clusters, 600): composition(avg A,B) %.2f [%.2f, %.2f] ; within %.2f [%.2f, %.2f]' % (mean(cs), cs[15], cs[584], mean(ws), ws[15], ws[584]))
    out['boot_' + sn] = {'composition': [mean(cs), cs[15], cs[584]], 'within': [mean(ws), ws[15], ws[584]]}
# L3-only acceptance among items that reached the model, by bin (non-passive non-cleft)
print('## model layer only: items that reached L3 (verdict present), non-passive non-cleft: SAME share by bin')
for s in ('1m', '1n'):
    it = [x for x in S[s] if x['verdict'] and not x['passive'] and not x['cleft']]
    print('  %s reached %d: SAME %s ; ' % (s, len(it), R(sum(x['verdict'] == 'SAME' for x in it), len(it))) + ' '.join('%s %d/%d' % (BINS[i][2], sum(x['verdict'] == 'SAME' for x in it if binof(x) == i), sum(1 for x in it if binof(x) == i)) for i in range(len(BINS))))
    it2 = [x for x in it if not x['det_swap']]; print('     excluding det_swap items: SAME %s' % R(sum(x['verdict'] == 'SAME' for x in it2), len(it2)))
items = [{'id': x['id'], 'set': x['set'].upper(), 'layer': x['layer'], 'model_verdict': x['verdict'], 'cause': x['cause'], 'E': x['E'][:2], 'E_sub': x['E'], 'rationale': x['why'], 'passive': x['passive'], 'cleft': x['cleft'], 'dist': round(x['dist'], 3),
          **({'a': 'a' in x['flags'].replace('+', '').split(), 'b': 'b' in x['flags'].replace('+', '').split(), 'c': 'c' in x['flags'].replace('+', '').split(), 'a_conservative': 'a+' in x['flags'], 'b_conservative': 'b+' in x['flags'], 'c_conservative': 'c+' in x['flags']} if x['set'] == '1n' else {})} for x in fr]
json.dump(items, open(os.path.join(O, 'taskCE_items.json'), 'w'), ensure_ascii=False, indent=1)
out['tab'] = tab; json.dump(out, open(os.path.join(D, 'ce_numbers.json'), 'w'), indent=1)
print('written taskCE_items.json (%d rows), diag/ce_numbers.json' % len(items))

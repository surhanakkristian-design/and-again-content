#!/usr/bin/env python3
"""Phase 1h — three changes on top of the frozen Phase 1f stack, measured on the frozen Phase 1c sets
with gemini-3.1-flash-lite only.

  (A) F5      adjunct-deletion rule (fills F3's word-class gap; any-position deletions)
  (B) F4v2    subject guard derived ONLY from the Slovak morphology, abstaining when underdetermined
  (C) F2B     correct_with_tip boundary: a tip requires the meaning (span / ongoingness) to survive

  python3 phase1h/run_phase1h.py --selftest   # offline, no key, no network
  python3 phase1h/run_phase1h.py --plan       # needed calls vs the 1200 cap (offline)
  python3 phase1h/run_phase1h.py --calls      # model calls for anything the ledgers do not already have
  python3 phase1h/run_phase1h.py --tabulate   # offline ablation, re-runnable
  python3 phase1h/run_phase1h.py --all        # calls then tabulate

phase1c/, phase1e/, phase1f/ are READ-ONLY here. No previous phase's runner is imported: lib_prev.py is a
verbatim COPY of phase1e/run_phase1e.py whose HERE resolves to phase1h/, so every path constant inside it
(LEDGER, LOG, MODEL_CFG) points into phase1h/. Previous-phase ledgers are read with plain open().
run_phase1e.routing() / do_run() / probe() are never called.
KEY RULE: GEMINI_API_KEY is parsed inside lib_prev.load_key() at call time, sent only in the
x-goog-api-key header, never printed, never written, never on a command line; errors are redacted.
"""
import json, os, re, sys, datetime
from collections import Counter, defaultdict
from math import comb

HERE = os.path.dirname(os.path.abspath(__file__))
TO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import lib_prev as base                                   # verbatim copy of phase1e's module
import reference_hygiene as hyg                           # deterministic, zero model tokens

assert os.path.dirname(os.path.abspath(base.__file__)) == HERE, 'lib_prev must live in phase1h/'

P1E = os.path.join(TO, 'phase1e')
P1F = os.path.join(TO, 'phase1f')
P1E_LEDGER = os.path.join(P1E, 'calls.jsonl')             # read-only seed
P1F_LEDGER = os.path.join(P1F, 'calls.jsonl')             # read-only seed
P1G = os.path.join(TO, 'phase1g')
P1G_LEDGER = os.path.join(P1G, 'calls.jsonl')             # read-only seed (empty in 1g)
JUDGE_1F = os.path.join(P1F, 'judgements_1f.json')        # read-only
LEDGER = os.path.join(HERE, 'calls.jsonl')                # 1h's own ledger (new calls only)
DECISIONS = os.path.join(HERE, 'decisions.jsonl')
CALL_LOG = os.path.join(HERE, 'call_log.jsonl')
CAP = 1500
MAX_OUT = 24
MODEL = 'gemini-3.1-flash-lite'

base.LEDGER, base.LOG = LEDGER, CALL_LOG                  # every write of the copied module -> phase1h/
base.CALL_CAP, base.ATTEMPT_CAP = CAP, CAP
base.MODEL_CFG = os.path.join(P1E, 'model_config.json')   # read-only config of the pinned model

PC_LINE = ("The SLOVAK sentence is the ground truth and the English reference is only one valid rendering of "
           "it; judge the learner against the Slovak, not against the reference wording.")
_orig_prompt = base.prompt


def prompt(it, variant):
    """Byte-identical to Phase 1f (so the 1e/1f ledgers are reusable)."""
    if variant == 'P-C':
        lines = _orig_prompt(it, 'P-B').split('\n')
        lines.insert(len(lines) - 1, PC_LINE)
        return '\n'.join(lines)
    return _orig_prompt(it, variant)


base.prompt = prompt

NOT_REAL_FA_CLASSES = ('tip-accept', 'valid reading')
DISPUTED = ('W:16403:624976382', 'W:10366:3357618811')
ROW0 = {'coverage_n': 214, 'fa_raw': 15, 'fa_real': 6, 'accepted_correct': 193, 'accepted_with_tip': 21}

# ================================================================ grammar tables (copied from phase1f)
ARTICLES = {'a', 'an', 'the'}
DET = ARTICLES | {'some', 'any', 'this', 'that', 'these', 'those', 'his', 'her', 'its', 'their', 'my',
                  'your', 'our', 'one'}
QUANT_CLASSES = [{'many', 'much', 'a lot of', 'lots of', 'loads of', 'plenty of', 'a number of', 'several',
                  'a few', 'few', 'some'}]
BE = {'be', 'am', 'is', 'are', 'was', 'were', 'been', 'being', "'s", "'re", "'m"}
HAVE = {'have', 'has', 'had', 'having'}
DO = {'do', 'does', 'did', 'doing', 'done'}
MODALS = {'will', 'would', 'can', 'could', 'shall', 'should', 'may', 'might', 'must'}
AUX = BE | HAVE | DO | MODALS
PRONOUNS = {'i', 'you', 'he', 'she', 'it', 'we', 'they', 'there', 'who', 'someone', 'somebody', 'nobody',
            'everyone', 'anyone', 'one'}
PARTICLES = {'off', 'out', 'up', 'down', 'in', 'on', 'away', 'back', 'over', 'through', 'along', 'around',
             'about', 'forward', 'together', 'aside'}
ADVERBS = {'finally', 'completely', 'already', 'just', 'still', 'never', 'always', 'usually', 'often',
           'really', 'almost', 'nearly', 'totally', 'quietly', 'slowly', 'quickly', 'carefully', 'not',
           'ever', 'even', 'only', 'again', 'now', 'today', 'twice', 'once', 'hardly', 'barely', 'fully',
           'suddenly', 'immediately', 'recently', 'lately', 'certainly', 'probably', 'definitely'}
FUNCTION = (AUX | PRONOUNS | DET | ARTICLES | {'to', 'of', 'and', 'or', 'but', 'if', 'when', 'while',
            'because', 'so', 'than', 'as', 'at', 'by', 'for', 'from', 'into', 'with', 'without', 'before',
            'after', 'until', 'since', 'that', 'which', 'whose', 'where', 'what', 'how', 'why', 'whom',
            'no', 'nor', 'both', 'each', 'all', 'more', 'most', 'less', 'very', 'too', 'then', 'there',
            'here', 'above', 'below', 'under', 'behind', 'between', 'during', 'towards', 'toward', 'per'}
            | ADVERBS | PARTICLES)
IRREG = [('be', 'was', 'been'), ('be', 'were', 'been'), ('have', 'had', 'had'), ('do', 'did', 'done'),
         ('go', 'went', 'gone'), ('take', 'took', 'taken'), ('give', 'gave', 'given'), ('see', 'saw', 'seen'),
         ('come', 'came', 'come'), ('become', 'became', 'become'), ('run', 'ran', 'run'),
         ('begin', 'began', 'begun'), ('drink', 'drank', 'drunk'), ('sing', 'sang', 'sung'),
         ('bring', 'brought', 'brought'), ('buy', 'bought', 'bought'), ('think', 'thought', 'thought'),
         ('teach', 'taught', 'taught'), ('catch', 'caught', 'caught'), ('seek', 'sought', 'sought'),
         ('fight', 'fought', 'fought'), ('say', 'said', 'said'), ('pay', 'paid', 'paid'),
         ('lay', 'laid', 'laid'), ('make', 'made', 'made'), ('find', 'found', 'found'),
         ('hold', 'held', 'held'), ('keep', 'kept', 'kept'), ('sleep', 'slept', 'slept'),
         ('feel', 'felt', 'felt'), ('leave', 'left', 'left'), ('lose', 'lost', 'lost'),
         ('mean', 'meant', 'meant'), ('meet', 'met', 'met'), ('read', 'read', 'read'),
         ('send', 'sent', 'sent'), ('spend', 'spent', 'spent'), ('build', 'built', 'built'),
         ('sit', 'sat', 'sat'), ('stand', 'stood', 'stood'), ('understand', 'understood', 'understood'),
         ('get', 'got', 'got'), ('get', 'got', 'gotten'), ('forget', 'forgot', 'forgotten'),
         ('wear', 'wore', 'worn'), ('tear', 'tore', 'torn'), ('bear', 'bore', 'borne'),
         ('swear', 'swore', 'sworn'), ('break', 'broke', 'broken'), ('speak', 'spoke', 'spoken'),
         ('choose', 'chose', 'chosen'), ('freeze', 'froze', 'frozen'), ('steal', 'stole', 'stolen'),
         ('write', 'wrote', 'written'), ('ride', 'rode', 'ridden'), ('drive', 'drove', 'driven'),
         ('rise', 'rose', 'risen'), ('eat', 'ate', 'eaten'), ('fall', 'fell', 'fallen'),
         ('throw', 'threw', 'thrown'), ('know', 'knew', 'known'), ('grow', 'grew', 'grown'),
         ('blow', 'blew', 'blown'), ('fly', 'flew', 'flown'), ('draw', 'drew', 'drawn'),
         ('show', 'showed', 'shown'), ('hide', 'hid', 'hidden'), ('bite', 'bit', 'bitten'),
         ('hang', 'hung', 'hung'), ('swim', 'swam', 'swum'), ('ring', 'rang', 'rung'),
         ('sink', 'sank', 'sunk'), ('spring', 'sprang', 'sprung'), ('win', 'won', 'won'),
         ('shine', 'shone', 'shone'), ('shoot', 'shot', 'shot'), ('set', 'set', 'set'),
         ('put', 'put', 'put'), ('cut', 'cut', 'cut'), ('let', 'let', 'let'), ('hit', 'hit', 'hit'),
         ('shut', 'shut', 'shut'), ('cost', 'cost', 'cost'), ('hurt', 'hurt', 'hurt'),
         ('lend', 'lent', 'lent'), ('bend', 'bent', 'bent'), ('feed', 'fed', 'fed'),
         ('lead', 'led', 'led'), ('flee', 'fled', 'fled'), ('hear', 'heard', 'heard'),
         ('tell', 'told', 'told'), ('sell', 'sold', 'sold'), ('sweep', 'swept', 'swept'),
         ('weep', 'wept', 'wept'), ('creep', 'crept', 'crept'), ('deal', 'dealt', 'dealt'),
         ('dream', 'dreamt', 'dreamt'), ('spread', 'spread', 'spread'), ('wake', 'woke', 'woken'),
         ('wind', 'wound', 'wound'), ('strike', 'struck', 'struck'), ('stick', 'stuck', 'stuck'),
         ('dig', 'dug', 'dug'), ('sweat', 'sweat', 'sweat'), ('quit', 'quit', 'quit'),
         ('mistake', 'mistook', 'mistaken'), ('forgive', 'forgave', 'forgiven'),
         ('hold', 'held', 'held'), ('light', 'lit', 'lit'), ('slide', 'slid', 'slid')]
IRR_PAST = {p for _b, p, _pp in IRREG}
IRR_PP = {pp for _b, _p, pp in IRREG}
IRR_BASE = {b for b, _p, _pp in IRREG}
BE_FORMS = {'be', 'am', 'is', 'are', 'was', 'were', 'been', 'being'}
AUX_LEMMA = {**{f: 'be' for f in BE_FORMS}, **{f: 'have' for f in HAVE}, **{f: 'do' for f in DO}}
CONTRACT = {"'ll": 'will', "'ve": 'have', "'re": 'are', "'m": 'am', "'d": 'had|would', "'s": 'is|has'}


def toks(s):
    return base.norm(s).split()


def expand(tokens):
    out = []
    for t in tokens:
        if t == "won't":
            out += ['will', 'not']
            continue
        if t == "can't" or t == 'cannot':
            out += ['can', 'not']
            continue
        if t.endswith("n't") and len(t) > 3:
            stem = t[:-3]
            out += [{'wo': 'will', 'ca': 'can', 'sha': 'shall', 'ai': 'is|are|am'}.get(stem, stem), 'not']
            continue
        hit = None
        for c in ("'ll", "'ve", "'re", "'m", "'d", "'s"):
            if t.endswith(c) and len(t) > len(c):
                hit = c
                break
        if hit:
            out += [t[:-len(hit)], CONTRACT[hit]]
        else:
            out.append(t)
    return out


def is_aux(tok, want):
    return want in tok.split('|')


def form_of(tok):
    f = set()
    if tok.endswith('ing'):
        f.add('ing')
    if tok.endswith('ed'):
        f |= {'past', 'pp'}
    if tok in IRR_PAST or any(len(p) >= 4 and len(tok) > len(p) and tok.endswith(p) for p in IRR_PAST):
        f.add('past')
    if tok in IRR_PP or any(len(p) >= 4 and len(tok) > len(p) and tok.endswith(p) for p in IRR_PP):
        f.add('pp')
    if tok in IRR_BASE:
        f.add('base')
    if tok.endswith('s') and not tok.endswith('ss') and not tok.endswith('ous'):
        f.add('s')
    if not f or (tok not in IRR_PAST and tok not in IRR_PP and not tok.endswith(('ing', 'ed', 's'))):
        f.add('base')
    return f


# ================================================================ F1 (copied from phase1f, unchanged)
def parse_lock(lock):
    tk = expand(toks(lock.replace('..', ' .. ')))
    tk = [t for t in tk if t]
    if not tk:
        return {'kind': 'literal'}
    gap = '' if '..' not in lock else 'gap'
    chain, verb, pron_inside, needs_to = [], None, False, False
    rest = []
    for t in tk:
        if t == '..':
            continue
        if verb is None and (t in AUX or '|' in t):
            chain.append(t)
            continue
        if verb is None and t in PRONOUNS:
            pron_inside = True
            continue
        if verb is None:
            verb = t
        else:
            rest.append(t)
    if verb is None:
        if len(chain) >= 2:
            verb, chain = chain[-1], chain[:-1]
        else:
            return {'kind': 'bare_aux', 'chain': chain, 'literal': ' '.join(chain)}
    needs_to = 'to' in rest[:1]
    vf = form_of(verb)
    if not chain:
        if tk[0] in DET and len(tk) >= 2:
            return {'kind': 'det_noun', 'head': tk[-1]}
        for cls in QUANT_CLASSES:
            if ' '.join(tk) in cls or tk[0] in cls:
                return {'kind': 'quant', 'cls': cls}
        if verb in FUNCTION:
            return {'kind': 'literal'}
        for f in ('ing', 's', 'past', 'pp', 'base'):
            if f in vf:
                form = f
                break
        if verb in AUX_LEMMA:
            return {'kind': 'exact_aux_main', 'literal': verb}
        return {'kind': 'pattern', 'chain': [], 'verb': verb, 'form': form, 'gap': gap,
                'needs_to': needs_to, 'pron': pron_inside}
    last = chain[-1]
    if last in MODALS:
        form = 'base'
    elif last in HAVE:
        form = 'pp'
    elif last in BE_FORMS:
        form = 'ing' if verb.endswith('ing') else 'pp'
    else:
        form = 'base'
    if len(chain) >= 2 and chain[-1] in BE_FORMS and chain[-2] in HAVE:
        form = 'ing' if verb.endswith('ing') else 'pp'
    return {'kind': 'pattern', 'chain': chain, 'verb': verb, 'form': form, 'gap': gap,
            'needs_to': needs_to, 'pron': pron_inside, 'aux_main': verb in AUX_LEMMA}


def pattern_match(pat, answer):
    at = expand(toks(answer))
    if pat['kind'] == 'literal':
        return False
    if pat['kind'] in ('bare_aux', 'exact_aux_main'):
        want = pat['literal'].split()
        return any(all(is_aux(at[i + j], w) for j, w in enumerate(want))
                   for i in range(len(at) - len(want) + 1))
    if pat['kind'] == 'det_noun':
        return pat['head'] in at
    if pat['kind'] == 'quant':
        joined = ' '.join(at)
        return any((' ' + q + ' ') in (' ' + joined + ' ') for q in pat['cls'])
    chain, form = pat['chain'], pat['form']
    lift = pat.get('aux_main')
    win = 5 if pat.get('gap') else 4

    def verb_ok(i):
        t = at[i]
        if form not in form_of(t):
            return False
        if t in FUNCTION and not (lift and t in AUX_LEMMA):
            return False
        if pat.get('needs_to') and 'to' not in at[i + 1:i + 3]:
            return False
        return True

    if not chain:
        return any(verb_ok(i) for i in range(len(at)))
    starts = [i for i in range(len(at)) if is_aux(at[i], chain[0])]
    for s in starts:
        pos, ok = s, True
        for a in chain[1:]:
            nxt = [j for j in range(pos + 1, min(pos + 5, len(at))) if is_aux(at[j], a)]
            if not nxt:
                ok = False
                break
            pos = nxt[0]
        if not ok:
            continue
        for i in range(pos + 1, min(pos + 1 + win, len(at))):
            if verb_ok(i):
                return True
    return False


def f1_lock_ok(it):
    return any(pattern_match(parse_lock(lk), it['answer']) for lk in it['locks'])


# ================================================================ F2 (copied from phase1f, unchanged)
CONCESSIVE = ['even so', 'nevertheless', 'nonetheless', 'however', 'still', 'all the same', 'although',
              'though', 'even though', 'despite', 'in spite of', 'yet']
ABLE = ['am able to', 'is able to', 'are able to', 'was able to', 'were able to', 'be able to']
GOING = ['am going to', 'is going to', 'are going to', 'was going to', 'were going to']
HAVETO = ['have to', 'has to', 'had to', 'need to', 'needs to', 'needed to', 'have got to', 'has got to']
VERB_PATTERN_EQUIV = {'managed to': ['succeeded in', 'was able to', 'were able to', 'is able to',
                                     'managed in'],
                      'stopped': ['gave up'], 'started': ['began']}


def _has(answer, phrases):
    j = ' ' + ' '.join(expand(toks(answer))) + ' '
    return next((p for p in phrases if ' ' + p + ' ' in j), None)


def f2_equivalent(it):
    a, topic = it['answer'], (it['topic'] or '')
    at = expand(toks(a))
    for lk in it['locks']:
        pat = parse_lock(lk)
        ch = pat.get('chain') or []
        low = base.norm(lk).strip()
        if low == 'must' or 'must' in ch:
            h = _has(a, HAVETO)
            if h:
                return 'must->' + h, h
        if low in ('can', 'could') or 'can' in ch or 'could' in ch:
            h = _has(a, ABLE)
            if h:
                return 'can->' + h, h
        if 'will' in ch or 'would' in ch or low in ('will', 'would'):
            h = _has(a, GOING)
            if h:
                return ('will/would->' + h), h
        if 'should' in ch or low == 'should':
            h = _has(a, ['ought to'])
            if h:
                return 'should->ought to', h
        if pat.get('kind') == 'pattern' and ch and ch[-1] in BE_FORMS and pat['form'] == 'pp':
            for i, t in enumerate(at):
                if t in ('get', 'gets', 'got', 'getting', 'gotten'):
                    if any('pp' in form_of(x) and x not in FUNCTION for x in at[i + 1:i + 3]):
                        return 'be-passive->get-passive', 'got ' + at[i + 1]
        if low in VERB_PATTERN_EQUIV:
            h = _has(a, VERB_PATTERN_EQUIV[low])
            if h:
                return '%s->%s' % (low, h), h
        if 'causative' in topic.lower() and pat.get('kind') == 'pattern' and pat['form'] == 'pp':
            for i, t in enumerate(at):
                if t in ('had', 'has', 'have', 'got', 'get', 'gets'):
                    for x in at[i + 1:i + 4]:
                        if x not in FUNCTION and 'base' in form_of(x) and 'pp' not in form_of(x):
                            return 'causative-passive->causative-active', '%s .. %s' % (t, x)
        if 'relative' in topic.lower():
            return 'relative-clause variant', low
        if 'linker' in topic.lower():
            h = _has(a, CONCESSIVE)
            if h:
                return 'linker->' + h, h
        if 'conditional' in topic.lower() and pat.get('kind') == 'pattern' and not ch \
                and pat['form'] == 'past' and ('if' in at or 'wish' in at or 'wishes' in at):
            for i, t in enumerate(at):
                if t in ('was', 'were') and any(x.endswith('ing') for x in at[i + 1:i + 3]):
                    return 'past-simple->were+ing (subjunctive)', '%s %s' % (t, at[i + 1])
    return None


def f2_tip(it):
    return 'use the target structure: %s' % (it['locks'][0] if it['locks'] else '?')


# ================================================================ F3 (copied from phase1f, unchanged)
_ANN = {}


ANN_DIRS = [os.path.join(HERE, 'fresh', 'annotations_new_60'),
            os.path.join(base.P1C, 'annotated_after')]          # fresh first, then the frozen 80
HYGIENE = True                                                  # 2.3, applied to old and new alike


def raw_annot(eid):
    for d in ANN_DIRS:
        p = os.path.join(d, '%d.json' % eid)
        if os.path.exists(p):
            return json.load(open(p))
    return {}


def annot(eid):
    """The hygienised annotation (2.3). phase1c/ is never written; hygiene is applied in memory."""
    if eid not in _ANN:
        a = raw_annot(eid)
        if a and HYGIENE:
            a = hyg.hygienise(a, SK_OF.get(eid))[0]
        _ANN[eid] = a or {}
    return _ANN[eid]


def refs_of(it):
    a = annot(it['exercise_id'])
    out = [it['reference']] + [v for v in (a.get('v') or []) if isinstance(v, str)]
    if HYGIENE:
        out = hyg.gender_variants(out, a.get('g'))
    seen, uniq = set(), []
    for r in out:
        if r not in seen:
            seen.add(r)
            uniq.append(r)
    return uniq


def optional_tokens(it):
    a = annot(it['exercise_id'])
    opt = set(ARTICLES)
    for k, v in (a.get('d') or {}).items():
        opt.add(base.norm(k).strip())
        for alt in str(v).split('|'):
            opt.add(base.norm(alt).strip())
    for v in (a.get('v') or []):
        for m in re.findall(r'\(([^)]*)\)', str(v)):
            opt |= set(toks(m))
    return {x for x in opt if x}


def subseq_missing(learner, ref, opt):
    L = [t for t in learner if t not in opt]
    R = [t for t in ref if t not in opt]
    i, missing = 0, []
    for t in R:
        if i < len(L) and L[i] == t:
            i += 1
        else:
            missing.append(t)
    if i < len(L):
        return None
    return missing


def f3_deletion(it):
    opt = optional_tokens(it)
    lt = expand(toks(it['answer']))
    worst = None
    for r in refs_of(it):
        miss = subseq_missing(lt, expand(toks(r)), opt)
        if miss is None:
            return False, []
        content = [m for m in miss if m not in FUNCTION and m not in opt]
        if not content:
            return False, []
        worst = content if worst is None else worst
    return (True, worst) if worst else (False, [])


# ================================================================ F4 (phase1f version, kept for row 0)
SK_PRON = {'ja': ('1', 'sg', None), 'ty': ('2', 'sg', None), 'on': ('3', 'sg', 'm'),
           'ona': ('3', 'sg', 'f'), 'ono': ('3', 'sg', 'n'), 'my': ('1', 'pl', None),
           'vy': ('2', 'pl', None), 'oni': ('3', 'pl', 'm'), 'ony': ('3', 'pl', 'f')}
SK_AUX = {'som': ('1', 'sg'), 'si': ('2', 'sg'), 'sme': ('1', 'pl'), 'ste': ('2', 'pl')}
EN_SUBJ = {'i': ('1', 'sg', None), 'we': ('1', 'pl', None), 'you': ('2', None, None),
           'he': ('3', 'sg', 'm'), 'she': ('3', 'sg', 'f'), 'it': ('3', 'sg', 'n'),
           'they': ('3', 'pl', None)}
SK_PART = re.compile(r'(al|il|ol|ul|el|yl|ml|dl|tl|sl|hl|žl|čl)(a|o|i)?$')


def sk_subject(sk):
    t = re.findall(r"[a-záäčďéěíľĺňóôöŕřšťúůüýž]+", (sk or '').lower())
    for w in t:
        if w in SK_PRON:
            return SK_PRON[w]
    for w in t:
        if w in SK_AUX:
            p, n = SK_AUX[w]
            return p, n, None
    for w in t:
        if len(w) >= 4 and w.endswith('š'):
            return '2', 'sg', None
        if len(w) >= 5 and w.endswith('te'):
            return '2', 'pl', None
        if len(w) >= 5 and w.endswith('me'):
            return '1', 'pl', None
        if len(w) >= 4 and w.endswith(('ím', 'ám', 'im', 'am', 'em')) and not w.endswith('om'):
            return '1', 'sg', None
    for w in t:
        m = SK_PART.search(w) if len(w) >= 4 else None
        if m:
            g = m.group(2)
            return '3', ('pl' if g == 'i' else 'sg'), {'a': 'f', 'o': 'n', None: 'm'}.get(g)
    return '3', None, None


def en_subjects(text):
    return [w for w in expand(toks(text)) if w in EN_SUBJ]


def _compat(s, e):
    sp, sn, sg = s
    ep, en_, eg = e
    if sp == '2' and ep == '2':
        return True
    if sp != ep:
        return False
    if sn and en_ and sn != en_:
        return False
    if sg and eg and sg in ('m', 'f') and eg in ('m', 'f') and sg != eg:
        return False
    return True


def f4_subject_mismatch(it):
    s = sk_subject(it['sk'])
    R, A = en_subjects(it['reference']), en_subjects(it['answer'])
    if not s or not R or len(R) != len(A):
        return False, ''
    for r, a in zip(R, A):
        if r != a and _compat(s, EN_SUBJ[r]) and not _compat(s, EN_SUBJ[a]):
            return True, "subject '%s' for '%s'; the Slovak fixes person/number/gender %s" % (a, r, s)
    return False, ''


# ================================================================ (B) F4v2 — Slovak-only subject features
SK_PREP = {'s', 'so', 'z', 'zo', 'k', 'ku', 'v', 'vo', 'na', 'do', 'od', 'po', 'pod', 'nad', 'pred', 'za',
           'medzi', 'o', 'pri', 'cez', 'bez', 'u', 'popri', 'okolo', 'podľa', 'proti', 'voči'}
SK_NOT_VERB = {'sedem', 'osem', 'sem', 'tam', 'dom', 'program', 'problém', 'systém', 'krém', 'sám', 'iba',
               'však', 'ešte', 'aspoň', 'práve'}
VOW = 'aeiouáéíóúýäôyě'
SK_L_PART = re.compile(r'^(.*?)(l|la|lo|li|ly)$')


def _sk_words(sk):
    return re.findall(r"[a-záäčďéěíľĺňóôöŕřšťúůüýž]+", (sk or '').lower())


def sk_features(sk):
    """Person / number / gender derived ONLY from the Slovak. A feature stays None when the Slovak leaves it
    open or when two signals disagree. The English reference is never consulted."""
    w = _sk_words(sk)
    sig = []                                       # (source, person, number, gender)
    prev = ''
    for x in w:
        after_prep = prev in SK_PREP
        prev = x
        if x in SK_PRON:
            p, n, g = SK_PRON[x]
            if x == 'vy':                          # sg-polite or pl -> number and gender open
                n = None
            if x in ('on', 'ona', 'ono') and after_prep:
                continue                           # 'na ňom', 'o ňom' ... not a nominative subject
            sig.append(('pronoun ' + x, p, n, g))
            continue
        if x in SK_AUX and x != 'si':
            p, n = SK_AUX[x]
            sig.append(('past auxiliary ' + x, p, n, None))
            continue
        if after_prep or x in SK_NOT_VERB or len(x) < 4:
            continue
        if x.endswith('š'):
            sig.append(('present -š ' + x, '2', 'sg', None))
            continue
        if x.endswith('me') and len(x) >= 5:
            sig.append(('present -me ' + x, '1', 'pl', None))
            continue
        if x.endswith('te') and len(x) >= 5:
            sig.append(('present -te ' + x, '2', None, None))       # vy = sg-polite or pl -> number open
            continue
        if (x.endswith(('ím', 'ám', 'iem', 'em')) and len(x) >= 4
                and not x.endswith(('om', 'ním', 'tím', 'ctvom'))):    # -nim/-tim = verbal noun, not 1sg
            sig.append(('present -m ' + x, '1', 'sg', None))
            continue
    # An l-participle is only read when the sentence really carries a past / conditional marker. Without one
    # a word such as 'skola' (school) is an ordinary noun ending in -la, not a feminine participle, and the
    # guard stays silent. This is the defect that made Phase 1f's F4 kill the three C:9498 answers.
    past_marker = any(x in ('by', 'keby', 'aby', 'zeby', 'som', 'si', 'sme', 'ste') for x in w)
    parts = []
    prev = ''
    for x in w:
        after_prep = prev in SK_PREP
        prev = x
        if not past_marker or len(x) < 4 or x in SK_NOT_VERB or after_prep:
            continue
        m = SK_L_PART.match(x)
        if not m or not m.group(1):
            continue
        end, stem = m.group(2), m.group(1)
        if stem[-1:] not in VOW:                   # only vowel + l(+a/o/i/y) can be an l-participle
            continue
        num = 'pl' if end in ('li', 'ly') else 'sg'
        gen = {'l': 'm', 'la': 'f', 'lo': 'n', 'li': None, 'ly': None}[end]
        parts.append(('l-participle ' + x, num, gen))
    # 'si' is ambiguous EVERYWHERE: 2sg auxiliary ('videl si to', 'nemal by si sa pytat') or the
    # reflexive / dative clitic ('kuchynu si dali natocit'; 'keby si bola vzala sako' = you had taken /
    # she had taken for herself). It therefore yields no person, AND it must block the default 3rd person
    # a bare l-participle would otherwise assert - else the guard silently claims 3sg for a 2sg sentence.
    ambiguous_si = 'si' in w
    has_aux = (any(s[0].startswith('past auxiliary') for s in sig) or ambiguous_si)
    for label, num, gen in parts:
        sig.append((label, None if has_aux else '3', num, gen))

    def agree(idx):
        vals = {s[idx] for s in sig if s[idx] is not None}
        return list(vals)[0] if len(vals) == 1 else None

    return {'person': agree(1), 'number': agree(2), 'gender': agree(3)}, [s[0] for s in sig]


def f4v2_subject_mismatch(it):
    """Fires only when the answer's subject pronoun contradicts a feature the SLOVAK determines."""
    feats, sources = sk_features(it['sk'])
    if not any(feats.values()):
        return False, {'fired': False, 'reason': 'Slovak underdetermined', 'features': feats,
                       'signals': sources}
    A = en_subjects(it['answer'])
    if not A:
        return False, {'fired': False, 'reason': 'no subject pronoun in the answer', 'features': feats,
                       'signals': sources}
    def clash(a):
        p, n, g = EN_SUBJ[a]
        if feats['person'] and p and feats['person'] != p:
            return 'person'
        if feats['number'] and n and a != 'you' and feats['number'] != n:
            return 'number'
        if feats['gender'] in ('m', 'f') and g in ('m', 'f') and feats['gender'] != g:
            return 'gender'
        return None

    # English has no case marking on 'it'/'you', so a pronoun in the answer may be an object. If ANY pronoun
    # of the answer fits the Slovak, that one is taken to be the subject and the guard abstains.
    if any(clash(a) is None for a in A):
        return False, {'fired': False, 'reason': 'an answer pronoun is compatible with the Slovak',
                       'features': feats, 'signals': sources, 'pronouns': A}
    return True, {'fired': True, 'clash': clash(A[0]), 'answer_subject': A[0], 'features': feats,
                  'signals': sources, 'pronouns': A}


# ================================================================ (A) F5 — adjunct deletion, any position
PREP_HEADS = {'in', 'on', 'at', 'into', 'onto', 'out', 'from', 'to', 'by', 'with', 'without', 'behind',
              'above', 'below', 'under', 'over', 'through', 'across', 'near', 'beside', 'between', 'during',
              'before', 'after', 'until', 'since', 'for', 'against', 'toward', 'towards', 'around', 'about',
              'along', 'past', 'up', 'down', 'off', 'of', 'inside', 'outside', 'upon'}
INFO_FUNC = (ADVERBS | PARTICLES | PREP_HEADS |
             {'here', 'there', 'then', 'now', 'very', 'too', 'more', 'most', 'less', 'all', 'no', 'not',
              'one', 'while', 'when', 'where', 'because', 'if', 'ever', 'yet', 'so'})
NONINFO = (ARTICLES | {'some', 'any', 'this', 'that', 'these', 'those', 'his', 'her', 'its', 'their', 'my',
                       'your', 'our'} | PRONOUNS | AUX |
           {'and', 'or', 'to', 'of', 'as', 'than', 'which', 'who', 'whom', 'whose', 'but'})
DASH_RE = re.compile(r'\s[-–—]\s|—|–')


def _postdash_start(ref, opt):
    m = DASH_RE.search(ref or '')
    if not m:
        return 10 ** 6
    return len([t for t in expand(toks(ref[:m.start()])) if t not in opt])


def _subseq_positions(learner, ref, opt):
    """-> [(position_in_stripped_ref, token)] that the learner dropped, or None if not a subsequence."""
    L = [t for t in learner if t not in opt]
    R = [t for t in ref if t not in opt]
    i, missing = 0, []
    for pos, t in enumerate(R):
        if i < len(L) and L[i] == t:
            i += 1
        else:
            missing.append((pos, t))
    if i < len(L):
        return None
    return missing


def _spans(missing):
    out = []
    for pos, t in missing:
        if out and out[-1][-1][0] == pos - 1:
            out[-1].append((pos, t))
        else:
            out.append([(pos, t)])
    return out


def span_information(span, opt, postdash_start):
    """-> reason string when the deleted span carries stated time / place / manner / measure / result
    information, else None. A deletion of articles (or of item-marked optional words) never fires."""
    eff = [t for _p, t in span if t not in opt]
    if not eff:
        return None
    if any(p >= postdash_start for p, _t in span):
        return 'clause after the dash dropped (%s)' % ' '.join(eff[:6])
    if all(t in NONINFO for t in eff):
        return None
    content = [t for t in eff if t not in FUNCTION]
    if content:
        return 'content word(s) %s' % ' '.join(content[:4])
    if eff[0] in PREP_HEADS and len(eff) > 1:
        return 'prepositional phrase %s' % ' '.join(eff[:5])
    if any(t in PARTICLES for t in eff):
        return 'verb particle / directional %s' % ' '.join(eff[:4])
    if any(t in INFO_FUNC for t in eff):
        return 'adjunct adverb %s' % ' '.join(eff[:4])
    return None


def f5_adjunct_deletion(it):
    """Fires when the answer is a pure order-preserving subsequence of the reference or of an accepted
    variant AND the deleted span carries information. Never fires when the answer equals an accepted
    variant after normalisation, nor when the deletion is articles/closed-class only."""
    opt = optional_tokens(it)
    lt = expand(toks(it['answer']))
    lt_eff = [t for t in lt if t not in opt]
    fires = []
    for r in refs_of(it):
        rt = expand(toks(r))
        if [t for t in rt if t not in opt] == lt_eff:
            return False, {'fired': False, 'reason': 'answer equals an accepted variant', 'variant': r}
        miss = _subseq_positions(lt, rt, opt)
        if miss is None:
            continue
        if not miss:
            return False, {'fired': False, 'reason': 'no deletion against %s' % r}
        pds = _postdash_start(r, opt)
        reasons = []
        for sp in _spans(miss):
            why = span_information(sp, opt, pds)
            if why:
                reasons.append({'deleted': ' '.join(t for _p, t in sp), 'why': why, 'position': sp[0][0],
                                'ref_len': len([t for t in rt if t not in opt])})
        if not reasons:
            return False, {'fired': False, 'reason': 'deletion carries no information (articles/closed class)',
                           'variant': r, 'deleted': ' '.join(t for _p, t in miss)}
        fires.append({'variant': r, 'spans': reasons})
    if fires:
        f = fires[0]
        return True, {'fired': True, 'variant': f['variant'], 'spans': f['spans'],
                      'deleted': '; '.join(s['deleted'] for s in f['spans']),
                      'why': '; '.join(s['why'] for s in f['spans'])}
    return False, {'fired': False, 'reason': 'not a subsequence of any accepted variant'}


# ================================================================ (C) F2 boundary — a tip must keep meaning
SK_SPAN = [
    (r'\bv kuse\b', 'v kuse (in a row / straight)'),
    (r'\bnepretržite\b', 'nepretržite (non-stop)'),
    (r'\bneustále\b', 'neustále (constantly)'),
    (r'\bstále\b', 'stále (still / constantly)'),
    (r'\bodvtedy\b', 'odvtedy (since then)'),
    (r'\bpočas\b', 'počas (during)'),
    (r'\buž\b', 'už (already / for)'),
    (r'\bcel[ýáéuúoí]\w*\s+\w+', 'celý ... (whole / all ...)'),
    (r'\bod\s+\w+a\b', 'od ... (since ...)'),
    (r'\b(dv[ea]|tri|štyri|päť|šesť|sedem|osem|deväť|desať|\d+)\s+'
     r'(sekund\w*|minút\w*|hodin\w*|hodiny|dni|dní|dňa|týžd\w*|mesiac\w*|rok\w*|rokov)\b',
     'explicit time span'),
    (r'\b(hodinu|minútu|chvíľu|chvíľku|týždeň|mesiac)\b', 'duration noun in the accusative'),
]
SK_ONGOING = ('v kuse', 'nepretržite', 'neustále', 'stále', 'počas', 'už', 'celý', 'celú', 'celé', 'od rána')
EN_SPAN = {'for', 'since', 'straight', 'nonstop', 'row', 'already', 'still', 'whole', 'all', 'during',
           'hour', 'hours', 'minute', 'minutes', 'second', 'seconds', 'day', 'days', 'week', 'weeks',
           'month', 'months', 'year', 'years', 'morning', 'evening', 'night', 'afternoon', 'time',
           'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'long', 'while'}


def _continuous(answer):
    at = expand(toks(answer))
    for i, t in enumerate(at):
        if t in BE_FORMS or t in ('keep', 'keeps', 'kept', 'keeping'):
            if any(x.endswith('ing') for x in at[i + 1:i + 3]):
                return True
    return 'continuously' in at or 'nonstop' in at


def f2_boundary_violation(it):
    """A correct_with_tip acceptance is downgraded to wrong when the SLOVAK explicitly carries a duration /
    ongoingness / time span that the answer no longer expresses."""
    sk = (it['sk'] or '').lower()
    marks = [name for rx, name in SK_SPAN if re.search(rx, sk)]
    if not marks:
        return False, {'fired': False, 'reason': 'no Slovak span/ongoingness marker'}
    at = set(expand(toks(it['answer'])))
    digits = re.findall(r'\d+', it['answer'] or '')
    span_in_answer = sorted(at & en_span_tokens(it)) + digits
    topic = (it['topic'] or '').lower()
    cont_topic = ('continuous' in topic or 'progressive' in topic)
    ongoing = [o for o in SK_ONGOING if o in sk]
    if not span_in_answer:
        return True, {'fired': True, 'clash': 'stated span dropped', 'slovak_markers': marks,
                      'slovak_ongoing': ongoing, 'answer_span_tokens': [], 'topic': it['topic']}
    if ongoing and cont_topic and not _continuous(it['answer']):
        return True, {'fired': True, 'clash': 'ongoingness dropped (no continuous form in the answer)',
                      'slovak_markers': marks, 'slovak_ongoing': ongoing,
                      'answer_span_tokens': span_in_answer, 'topic': it['topic']}
    return False, {'fired': False, 'reason': 'span/ongoingness still expressed', 'slovak_markers': marks,
                   'slovak_ongoing': ongoing, 'answer_span_tokens': span_in_answer,
                   'continuous': _continuous(it['answer']), 'topic': it['topic']}


# ================================================================ decide
FLAGS = ('F1', 'F2', 'F3', 'F4', 'F4v2', 'F5', 'F2B')


def decide(it, flags, verdicts):
    trace = {}
    if flags.get('F3'):
        hit, miss = f3_deletion(it)
        if hit:
            return {'layer': 'F3', 'accepted': False, 'verdict': 'wrong', 'tip': None,
                    'why': 'missing meaning (%s)' % ' '.join(miss[:4]), 'trace': {'F3_missing': miss}}
    if flags.get('F5'):
        hit, tr = f5_adjunct_deletion(it)
        if hit:
            return {'layer': 'F5', 'accepted': False, 'verdict': 'wrong', 'tip': None,
                    'why': 'missing meaning (%s)' % tr['why'], 'trace': {'F5': tr}}
        trace['F5'] = tr
    if flags.get('F4v2'):
        hit, tr = f4v2_subject_mismatch(it)
        if hit:
            return {'layer': 'F4v2', 'accepted': False, 'verdict': 'wrong', 'tip': None,
                    'why': 'wrong subject: %s clash, answer "%s", Slovak %s'
                           % (tr['clash'], tr['answer_subject'], tr['features']), 'trace': {'F4v2': tr}}
        trace['F4v2'] = tr
    elif flags.get('F4'):
        hit, why = f4_subject_mismatch(it)
        if hit:
            return {'layer': 'F4', 'accepted': False, 'verdict': 'wrong', 'tip': None, 'why': why,
                    'trace': {}}
    lay, why = base.route(it)
    if lay == 'L1':
        out = {'layer': 'L1', 'accepted': True, 'verdict': it['verdict'], 'tip': None, 'why': why}
    else:
        tip = None
        if lay == 'L2':
            if it['step'] == 'mistake':
                return {'layer': 'L2', 'accepted': False, 'verdict': 'wrong', 'tip': None, 'why': why,
                        'trace': trace}
            released = False
            if flags.get('F1') and f1_lock_ok(it):
                released, why = True, 'F1 pattern match'
            if not released and flags.get('F2'):
                eq = f2_equivalent(it)
                if eq:
                    released, tip, why = True, f2_tip(it), 'F2 structure equivalent (%s)' % eq[0]
            if not released:
                return {'layer': 'L2', 'accepted': False, 'verdict': 'wrong', 'tip': None, 'why': why,
                        'trace': trace}
        v = verdicts.get(it['item_id'])
        if v is None:
            return {'layer': 'L3', 'accepted': False, 'verdict': 'failed', 'tip': None,
                    'why': 'no parsed verdict', 'trace': trace}
        if v == 'DIFF':
            return {'layer': 'L3', 'accepted': False, 'verdict': 'wrong', 'tip': None, 'why': 'model DIFF',
                    'trace': trace}
        acc = 'correct_with_tip' if (tip or v == 'TIP') else 'correct'
        out = {'layer': 'L3', 'accepted': True, 'verdict': acc,
               'tip': tip or (None if v == 'SAME' else 'model tip'), 'why': 'model %s' % v}
    if flags.get('F2B') and out['accepted'] and out['verdict'] == 'correct_with_tip':
        hit, tr = f2_boundary_violation(it)
        trace['F2B'] = tr
        if hit:
            return {'layer': 'F2B', 'accepted': False, 'verdict': 'wrong', 'tip': None,
                    'why': 'tip withdrawn: %s (%s); accepted at %s before the boundary'
                           % (tr['clash'], ', '.join(tr['slovak_markers']), out['layer']),
                    'trace': {'F2B': tr}}
    out['trace'] = trace
    return out


def needed_items(correct, wrong):
    """Items that reach L3 under ANY flag combination = F1+F2 on, every rejecting guard off."""
    flags = {'F1': True, 'F2': True}
    return [it for it in correct + wrong if decide(it, flags, {})['layer'] == 'L3']


# ================================================================ ledger / cache
def jl(path):
    if not os.path.exists(path):
        return []
    rows = []
    for line in open(path):
        line = line.strip()
        if line:
            try:
                rows.append(json.loads(line))
            except Exception:
                pass
    return rows


def seed_cache():
    """Byte-identical prompts only: 1e has P-B, 1f has P-B and P-C built by the same prompt() code."""
    out = {}
    for path, variants, tag in ((P1E_LEDGER, ('P-B',), '1e'), (P1F_LEDGER, ('P-B', 'P-C'), '1f'),
                               (P1G_LEDGER, ('P-B', 'P-C'), '1g')):
        for r in jl(path):
            iid = r.get('item_id') or ''
            if (r.get('model') == MODEL and r.get('variant') in variants and r.get('counted')
                    and r.get('verdict') in ('SAME', 'TIP', 'DIFF') and '#probe' not in iid
                    and '@' not in iid):
                out.setdefault((MODEL, r['variant'], iid), dict(r, reused_from=tag))
    return out


class Bud1h(base.Budget):
    def __init__(self):
        base.Budget.__init__(self)                       # reads phase1h/calls.jsonl only
        self.own = dict(self.cache)
        seeds = seed_cache()
        self.seeded = {k: v for k, v in seeds.items() if k not in self.cache}
        self.cache.update(self.seeded)


def verdict_map(variant, bud):
    return {k[2]: v['verdict'] for k, v in bud.cache.items() if k[0] == MODEL and k[1] == variant}


def cfg_1h():
    c = dict(json.load(open(base.MODEL_CFG))[MODEL])
    c['max_output'] = MAX_OUT
    return c


# ================================================================ statistics
def binom_cdf(k, n, p):
    if k < 0:
        return 0.0
    if k >= n:
        return 1.0
    return sum(comb(n, i) * (p ** i) * ((1 - p) ** (n - i)) for i in range(k + 1))


def clopper_pearson(k, n, alpha=0.05):
    """Exact 95 % binomial interval by bisection on the binomial CDF (no scipy dependency)."""
    if n == 0:
        return (0.0, 1.0)
    lo, hi = 0.0, 1.0
    if k > 0:
        a, b = 0.0, 1.0
        for _ in range(120):
            m = (a + b) / 2
            if 1 - binom_cdf(k - 1, n, m) < alpha / 2:
                a = m
            else:
                b = m
        lo = (a + b) / 2
    if k < n:
        a, b = 0.0, 1.0
        for _ in range(120):
            m = (a + b) / 2
            if binom_cdf(k, n, m) > alpha / 2:
                a = m
            else:
                b = m
        hi = (a + b) / 2
    return (round(lo, 6), round(hi, 6))


def sample_size():
    z, p = 1.959963985, 0.02
    out = {'target_p': p,
           'method': '95 % two-sided; exact = smallest n whose Clopper-Pearson interval for k = round(0.02 n) '
                     'lies inside p_hat +- d; "stable_from" = smallest n from which it also holds for the '
                     'next 150 values of n'}
    for d, key in ((0.01, 'half_width_1pp'), (0.015, 'half_width_1_5pp')):
        norm_n = int(-(-(z * z * p * (1 - p) / (d * d)) // 1))
        exact, stable = None, None
        for n in range(50, 3001):
            k = int(round(p * n))
            lo, hi = clopper_pearson(k, n)
            ph = k / n
            if (ph - lo) <= d and (hi - ph) <= d:
                if exact is None:
                    exact = {'n': n, 'k': k, 'p_hat': round(ph, 5), 'ci_pct': [round(100 * lo, 3),
                                                                               round(100 * hi, 3)]}
                if stable is None:
                    ok = True
                    for m in range(n, min(n + 150, 3001)):
                        km = int(round(p * m))
                        lo2, hi2 = clopper_pearson(km, m)
                        if (km / m - lo2) > d or (hi2 - km / m) > d:
                            ok = False
                            break
                    if ok:
                        stable = n
                if exact is not None and stable is not None:
                    break
        out[key] = {'normal_approximation_n': norm_n, 'clopper_pearson_smallest_n': exact,
                    'clopper_pearson_stable_from_n': stable}
    return out


# ================================================================ stages
def utc():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')


def stage_calls():
    correct, wrong = load_items_1h()
    need = needed_items(correct, wrong)
    bud = Bud1h()
    todo = []
    for variant in ('P-B', 'P-C'):
        have = verdict_map(variant, bud)
        todo += [(variant, it) for it in need if it['item_id'] not in have]
    print('needed %d items x 2 variants; new calls required: %d (cap %d, spent in 1h so far %d)'
          % (len(need), len(todo), CAP, bud.attempts))
    if len(todo) + bud.attempts > CAP:
        print('STOP: the plan exceeds the %d cap. No sampling, no silent skipping.' % CAP)
        sys.exit(4)
    if not todo:
        print('nothing to call: every needed verdict is in the 1e/1f ledgers with a byte-identical prompt.')
        return 0, 0
    cfg = cfg_1h()
    new, failed = 0, []
    for variant, it in todo:
        if bud.attempts >= CAP:
            print('STOP: 1200-call cap reached, aborting the run.')
            break
        r = base.call_model(bud, MODEL, variant, it, cfg)
        if r is None or r.get('verdict') not in ('SAME', 'TIP', 'DIFF'):
            r = base.call_model(bud, MODEL, variant, it, cfg)
        if r is None or r.get('verdict') not in ('SAME', 'TIP', 'DIFF'):
            failed.append('%s %s' % (variant, it['item_id']))
        else:
            new += 1
    print('new calls parsed %d, failed %d' % (new, len(failed)))
    return new, len(failed)


def row_stats(correct, wrong, flags, variant, bud, judge, strict_ids):
    vm = verdict_map(variant, bud)
    dc = {it['item_id']: decide(it, flags, vm) for it in correct}
    dw = {it['item_id']: decide(it, flags, vm) for it in wrong}
    r = {'flags': {f: bool(flags.get(f)) for f in FLAGS}, 'variant': variant}
    acc_c = [i for i, d in dc.items() if d['accepted']]
    r['coverage_n'] = len(acc_c)
    r['coverage_pct'] = round(100 * len(acc_c) / 235, 1)
    r['accepted_correct'] = sum(1 for i in acc_c if dc[i]['verdict'] == 'correct')
    r['accepted_with_tip'] = sum(1 for i in acc_c if dc[i]['verdict'] == 'correct_with_tip')
    bylv = defaultdict(lambda: [0, 0])
    for it in correct:
        b = bylv[it['level']]
        b[1] += 1
        b[0] += 1 if dc[it['item_id']]['accepted'] else 0
    r['coverage_by_level'] = {k: '%d/%d = %.1f %%' % (v[0], v[1], 100 * v[0] / v[1])
                              for k, v in sorted(bylv.items())}
    acc_w = [it for it in wrong if dw[it['item_id']]['accepted']]
    notreal = {it['item_id'] for it in wrong if (it.get('fa_class') or '') in NOT_REAL_FA_CLASSES}

    def real_set(strict):
        out = []
        for it in acc_w:
            iid = it['item_id']
            if iid in notreal and not (strict and iid in strict_ids):
                continue
            j = judge.get(iid)
            if j is None or j.get('real'):
                out.append(it)
        return out

    r['fa_raw'] = len(acc_w)
    r['fa_raw_ids'] = [it['item_id'] for it in acc_w]
    for strict, tag in ((False, 'lenient'), (True, 'strict')):
        rs = real_set(strict)
        k = len(rs)
        lo, hi = clopper_pearson(k, 105)
        r['fa_' + tag] = k
        r['fa_%s_pct' % tag] = round(100 * k / 105, 1)
        r['fa_%s_ci95' % tag] = [round(100 * lo, 2), round(100 * hi, 2)]
        r['fa_%s_ids' % tag] = [it['item_id'] for it in rs]
        r['fa_%s_by_type' % tag] = dict(Counter(it['wrong_type'] or '?' for it in rs))
    r['fa_by_type_raw'] = dict(Counter(it['wrong_type'] or '?' for it in acc_w))
    r['layers_correct'] = dict(Counter(d['layer'] for d in dc.values()))
    r['layers_wrong'] = dict(Counter(d['layer'] for d in dw.values()))
    r['L1_L2_L3_correct'] = [r['layers_correct'].get('L%d' % i, 0) for i in (1, 2, 3)]
    r['L1_L2_L3_wrong'] = [r['layers_wrong'].get('L%d' % i, 0) for i in (1, 2, 3)]
    guards = {}
    for g in ('F3', 'F4', 'F4v2', 'F5', 'F2B', 'L2'):
        kc = [i for i, d in dc.items() if d['layer'] == g and not d['accepted']]
        kw = [i for i, d in dw.items() if d['layer'] == g and not d['accepted']]
        guards[g] = {'kills_correct_n': len(kc), 'kills_correct': kc,
                     'kills_wrong_n': len(kw), 'kills_wrong': kw}
    guards['F1'] = {'note': 'F1 releases L2 vetoes; it never kills', 'kills_correct_n': 0,
                    'kills_wrong_n': 0, 'kills_correct': [], 'kills_wrong': []}
    guards['F2'] = {'note': 'F2 releases L2 vetoes with a tip; it never kills', 'kills_correct_n': 0,
                    'kills_wrong_n': 0, 'kills_correct': [], 'kills_wrong': []}
    r['guard_kills'] = guards
    r['failed_calls'] = sum(1 for d in list(dc.values()) + list(dw.values()) if d['verdict'] == 'failed')
    r['_dc'], r['_dw'] = dc, dw
    return r


ROWS_1G_SUPERSEDED = [
    ('[0] Phase 1f all four (F1F2F3F4)', 'P-B', {'F1': 1, 'F2': 1, 'F3': 1, 'F4': 1}),
    ('[1] +F5 only', 'P-B', {'F1': 1, 'F2': 1, 'F3': 1, 'F4': 1, 'F5': 1}),
    ('[2] F4v2 replaces F4 only', 'P-B', {'F1': 1, 'F2': 1, 'F3': 1, 'F4v2': 1}),
    ('[3] +F2 boundary only', 'P-B', {'F1': 1, 'F2': 1, 'F3': 1, 'F4': 1, 'F2B': 1}),
    ('[4] F5 + F4v2', 'P-B', {'F1': 1, 'F2': 1, 'F3': 1, 'F4v2': 1, 'F5': 1}),
    ('[5] F5 + F2 boundary', 'P-B', {'F1': 1, 'F2': 1, 'F3': 1, 'F4': 1, 'F5': 1, 'F2B': 1}),
    ('[6] F4v2 + F2 boundary', 'P-B', {'F1': 1, 'F2': 1, 'F3': 1, 'F4v2': 1, 'F2B': 1}),
    ('[7] all three new x P-B', 'P-B', {'F1': 1, 'F2': 1, 'F3': 1, 'F4v2': 1, 'F5': 1, 'F2B': 1}),
    ('[8] all three new x P-C', 'P-C', {'F1': 1, 'F2': 1, 'F3': 1, 'F4v2': 1, 'F5': 1, 'F2B': 1}),
]


def stage_tabulate():
    correct, wrong = load_items_1h()
    byid = {it['item_id']: it for it in correct + wrong}
    bud = Bud1h()
    judge = json.load(open(JUDGE_1F))
    ts = utc()
    rows = []
    open(DECISIONS, 'w').close()
    with open(DECISIONS, 'a') as fh:
        for label, variant, fl in ROWS:
            r = row_stats(correct, wrong, fl, variant, bud, judge, set(DISPUTED))
            r['label'] = label
            rows.append(r)
            for setname, d in (('correct', r['_dc']), ('wrong', r['_dw'])):
                for iid, dd in d.items():
                    fh.write(json.dumps({'row': label, 'variant': variant, 'set': setname, 'item_id': iid,
                                         'layer': dd['layer'], 'accepted': dd['accepted'],
                                         'verdict': dd['verdict'], 'why': dd['why'],
                                         'trace': dd.get('trace') or {}},
                                        ensure_ascii=False, default=str) + '\n')
    r0 = rows[0]
    problems = []
    got = {'coverage_n': r0['coverage_n'], 'fa_raw': r0['fa_raw'], 'fa_real': r0['fa_lenient'],
           'accepted_correct': r0['accepted_correct'], 'accepted_with_tip': r0['accepted_with_tip']}
    for k, v in ROW0.items():
        if got[k] != v:
            problems.append('%s = %s, Phase 1f reported %s' % (k, got[k], v))
    if problems:
        print('!!! LOUD WARNING: row 0 does NOT reproduce Phase 1f: %s. The measuring apparatus is suspect '
              'first — fix this before reading any other row.' % '; '.join(problems))
    else:
        print('row 0 reproduces Phase 1f exactly: coverage 214/235, FA raw 15, FA real (lenient) 6, '
              '193 correct / 21 with tip.')

    def regressions(r):
        return {'lost_correct': sorted(i for i, d in r['_dc'].items()
                                       if not d['accepted'] and r0['_dc'][i]['accepted']),
                'gained_correct': sorted(i for i, d in r['_dc'].items()
                                         if d['accepted'] and not r0['_dc'][i]['accepted']),
                'new_false_accept': sorted(i for i, d in r['_dw'].items()
                                           if d['accepted'] and not r0['_dw'][i]['accepted']),
                'fixed_wrong': sorted(i for i, d in r['_dw'].items()
                                      if not d['accepted'] and r0['_dw'][i]['accepted'])}

    for r in rows:
        r['vs_row0'] = regressions(r)

    # ---- F5 cost on the 235, measured on its own
    vmb = verdict_map('P-B', bud)
    base_fl = {'F1': 1, 'F2': 1, 'F3': 1, 'F4': 1}
    f5_cost, f5_gain = [], []
    for it in correct:
        d0 = decide(it, base_fl, vmb)
        d1 = decide(it, dict(base_fl, F5=1), vmb)
        if d1['layer'] == 'F5':
            tr = d1['trace']['F5']
            f5_cost.append({'item_id': it['item_id'], 'level': it['level'], 'sk': it['sk'],
                            'reference': it['reference'], 'answer': it['answer'],
                            'matched_variant': tr.get('variant'), 'deleted_span': tr.get('deleted'),
                            'why': tr.get('why'), 'would_otherwise_be_accepted': bool(d0['accepted'])})
    for it in wrong:
        d0 = decide(it, base_fl, vmb)
        d1 = decide(it, dict(base_fl, F5=1), vmb)
        if d1['layer'] == 'F5':
            f5_gain.append({'item_id': it['item_id'], 'type': it['wrong_type'],
                            'deleted_span': d1['trace']['F5'].get('deleted'),
                            'was_accepted': bool(d0['accepted'])})
    f5_block = {'rule': 'F5 measured on top of the Phase 1f all-four stack (F3 runs first, so these are the '
                        'items F3 misses)',
                'cost_on_235_total': len(f5_cost),
                'cost_on_235_that_were_accepted_before': sum(1 for x in f5_cost
                                                             if x['would_otherwise_be_accepted']),
                'kills_on_235': f5_cost, 'kills_on_105_total': len(f5_gain),
                'kills_on_105_that_were_accepted_before': sum(1 for x in f5_gain if x['was_accepted']),
                'kills_on_105': f5_gain}
    json.dump(f5_block, open(os.path.join(HERE, 'f5_cost_235.json'), 'w'), ensure_ascii=False, indent=1)

    # ---- F4v2 verification
    ver = {'requirement': 'all C:9498 answers abstain; W:4571:4142535241 and W:3494:4150910632 still fire',
           'c9498': [], 'must_fire': [], 'cost_on_235': [], 'kills_on_105': []}
    for it in correct + wrong:
        if it['item_id'].startswith('C:9498:') or it['item_id'] in ('W:4571:4142535241',
                                                                    'W:3494:4150910632'):
            fired, tr = f4v2_subject_mismatch(it)
            rec = {'item_id': it['item_id'], 'sk': it['sk'], 'reference': it['reference'],
                   'answer': it['answer'], 'f4v2_fires': fired, 'trace': tr,
                   'f4_1f_fired': f4_subject_mismatch(it)[0]}
            (ver['c9498'] if it['item_id'].startswith('C:9498:') else ver['must_fire']).append(rec)
    ver['c9498_all_abstain'] = all(not x['f4v2_fires'] for x in ver['c9498'])
    ver['must_fire_all_fire'] = all(x['f4v2_fires'] for x in ver['must_fire']) and len(ver['must_fire']) == 2
    fl_v2 = {'F1': 1, 'F2': 1, 'F3': 1, 'F4v2': 1}
    for it in correct:
        d = decide(it, fl_v2, vmb)
        if d['layer'] == 'F4v2':
            ver['cost_on_235'].append({'item_id': it['item_id'], 'level': it['level'],
                                       'sk': it['sk'], 'reference': it['reference'],
                                       'answer': it['answer'], 'why': d['why']})
    for it in wrong:
        d0 = decide(it, {'F1': 1, 'F2': 1, 'F3': 1}, vmb)
        d = decide(it, fl_v2, vmb)
        if d['layer'] == 'F4v2':
            ver['kills_on_105'].append({'item_id': it['item_id'], 'type': it['wrong_type'],
                                        'was_accepted': bool(d0['accepted']), 'why': d['why']})
    ver['cost_on_235_total'] = len(ver['cost_on_235'])
    ver['kills_on_105_total'] = len(ver['kills_on_105'])
    ver['verdict'] = 'PASS' if (ver['c9498_all_abstain'] and ver['must_fire_all_fire']) else 'FAIL'
    json.dump(ver, open(os.path.join(HERE, 'f4v2_verification.json'), 'w'), ensure_ascii=False, indent=1)

    # ---- F2 boundary: the two disputed items + kills on both sets
    disp = {}
    for iid in DISPUTED:
        it = byid.get(iid)
        if not it:
            disp[iid] = {'error': 'item id not present in the frozen sets'}
            continue
        fired, tr = f2_boundary_violation(it)
        d0 = decide(it, base_fl, vmb)
        d1 = decide(it, dict(base_fl, F2B=1), vmb)
        disp[iid] = {'sk': it['sk'], 'reference': it['reference'], 'answer': it['answer'],
                     'level': it['level'], 'topic': it['topic'], 'wrong_type': it['wrong_type'],
                     'fa_class_1e': it.get('fa_class'), 'boundary_fires': fired, 'trace': tr,
                     'decision_without_boundary': {k: d0[k] for k in ('layer', 'accepted', 'verdict', 'why')},
                     'decision_with_boundary': {k: d1[k] for k in ('layer', 'accepted', 'verdict', 'why')},
                     'comes_out_as': ('wrong' if not d1['accepted'] else d1['verdict'])}
    b_kills_c, b_kills_w = [], []
    for it in correct:
        d = decide(it, dict(base_fl, F2B=1), vmb)
        if d['layer'] == 'F2B':
            b_kills_c.append({'item_id': it['item_id'], 'level': it['level'], 'sk': it['sk'],
                              'reference': it['reference'], 'answer': it['answer'], 'why': d['why']})
    for it in wrong:
        d = decide(it, dict(base_fl, F2B=1), vmb)
        if d['layer'] == 'F2B':
            b_kills_w.append({'item_id': it['item_id'], 'type': it['wrong_type'], 'answer': it['answer'],
                              'why': d['why']})
    f2b_block = {'disputed': disp, 'kills_on_235_total': len(b_kills_c), 'kills_on_235': b_kills_c,
                 'kills_on_105_total': len(b_kills_w), 'kills_on_105': b_kills_w}
    json.dump(f2b_block, open(os.path.join(HERE, 'f2_boundary_disputed.json'), 'w'), ensure_ascii=False,
              indent=1)

    # ---- remaining errors of rows 7 and 8
    rem = {}
    for r in rows[-2:]:
        fa, fr = [], []
        for it in wrong:
            d = r['_dw'][it['item_id']]
            if d['accepted']:
                j = judge.get(it['item_id'])
                fa.append({'item_id': it['item_id'], 'level': it['level'], 'type': it['wrong_type'],
                           'sk': it['sk'], 'reference': it['reference'], 'answer': it['answer'],
                           'decision_path': '%s: %s' % (d['layer'], d['why']), 'verdict': d['verdict'],
                           'fa_class_1e': it.get('fa_class'), 'judgement_1f_real': (j or {}).get('real'),
                           'disputed': it['item_id'] in DISPUTED,
                           'judgement': 'TO BE ADDED BY THE NEXT AGENT'})
        for it in correct:
            d = r['_dc'][it['item_id']]
            if not d['accepted']:
                fr.append({'item_id': it['item_id'], 'level': it['level'], 'sk': it['sk'],
                           'reference': it['reference'], 'answer': it['answer'],
                           'decision_path': '%s: %s' % (d['layer'], d['why']),
                           'judgement': 'TO BE ADDED BY THE NEXT AGENT'})
        rem[r['label']] = {'variant': r['variant'], 'false_acceptances_raw_n': len(fa),
                           'false_acceptances_raw': fa, 'false_rejections_n': len(fr),
                           'false_rejections': fr}
    json.dump(rem, open(os.path.join(HERE, 'remaining_errors.json'), 'w'), ensure_ascii=False, indent=1)

    # ---- sample size + call counts
    ss = sample_size()
    json.dump(ss, open(os.path.join(HERE, 'sample_size.json'), 'w'), ensure_ascii=False, indent=1)
    mine = jl(LEDGER)
    need = needed_items(correct, wrong)
    new_n = sum(1 for x in mine if x.get('counted') and x.get('verdict') in ('SAME', 'TIP', 'DIFF'))
    used = 0
    for variant in ('P-B', 'P-C'):
        have = verdict_map(variant, bud)
        used += sum(1 for it in need if it['item_id'] in have)
    counts = {'new': new_n, 'reused': used - new_n, 'failed': sum(1 for x in mine if x.get('counted')
                                                                  and x.get('verdict') == 'PARSE_FAIL'),
              'cap': 1200, 'http_attempts_1h': len(mine),
              'r429': sum(1 for x in mine if x.get('http') == 429), 'model': MODEL,
              'needed_verdicts': 2 * len(need), 'verdicts_available': used,
              'note': 'reused = verdicts taken from the phase1e / phase1f ledgers with a byte-identical '
                      'prompt; new = HTTP calls made by Phase 1h'}
    json.dump(counts, open(os.path.join(HERE, 'call_counts.json'), 'w'), ensure_ascii=False, indent=1)

    # ---- results
    out = {'ts': ts, 'model': MODEL, 'row0_reproduction': ('OK' if not problems else problems),
           'row_design': 'rows 1-3 are the single-change rows (1f stack + exactly one change); rows 4-6 are '
                         'the pairwise combinations; row 7 all three; row 8 all three with P-C',
           'rows': [{k: v for k, v in r.items() if not k.startswith('_')} for r in rows],
           'f5_cost_235': f5_block,
           'f4v2_verification': {k: v for k, v in ver.items() if k not in ('c9498', 'must_fire')},
           'f4v2_required_cases': {'c9498': ver['c9498'], 'must_fire': ver['must_fire']},
           'f2_boundary': f2b_block, 'sample_size': ss, 'call_counts': counts,
           'lenient_vs_strict': {'lenient': "Phase 1e's 9 'not real' classifications kept as not real",
                                 'strict': 'the two disputed items %s counted as real' % (DISPUTED,)}}
    md = ['# Phase 1h — F5 adjunct deletion, F4v2 Slovak-only subject guard, F2 tip boundary (%s)\n' % MODEL,
          'Row 0 reproduction of Phase 1f: **%s**\n' % ('OK (214/235, FA raw 15, FA real 6, 193/21)'
                                                        if not problems else 'FAILED — ' + '; '.join(problems)),
          'Rows 1-3 are the SINGLE-change rows (each = the 1f stack + exactly one change); rows 4-6 are the '
          'pairwise combinations; row 7 is all three; row 8 is all three with P-C. Every figure comes from '
          'the same ledger, so the rows are comparable.\n',
          '| row | variant | flags | coverage /235 | A1/A2/B1/B2 | correct/tip | FA raw | FA lenient (95 % CP) '
          '| FA strict (95 % CP) | L1/L2/L3 correct | lost correct vs row 0 | new FA vs row 0 |',
          '|---|---|---|---|---|---|---|---|---|---|---|---|']
    for r in rows:
        lv = r['coverage_by_level']
        md.append('| %s | %s | %s | %d (%.1f %%) | %s | %d / %d | %d | %d = %.1f %% (%.1f–%.1f) | '
                  '%d = %.1f %% (%.1f–%.1f) | %d/%d/%d | %d | %d |'
                  % (r['label'], r['variant'], ''.join(f for f in FLAGS if r['flags'][f]),
                     r['coverage_n'], r['coverage_pct'],
                     ' · '.join((lv.get(k, '-').split(' = ')[1] if ' = ' in lv.get(k, '-') else '-')
                                for k in ('A1', 'A2', 'B1', 'B2')),
                     r['accepted_correct'], r['accepted_with_tip'], r['fa_raw'],
                     r['fa_lenient'], r['fa_lenient_pct'], r['fa_lenient_ci95'][0], r['fa_lenient_ci95'][1],
                     r['fa_strict'], r['fa_strict_pct'], r['fa_strict_ci95'][0], r['fa_strict_ci95'][1],
                     r['L1_L2_L3_correct'][0], r['L1_L2_L3_correct'][1], r['L1_L2_L3_correct'][2],
                     len(r['vs_row0']['lost_correct']), len(r['vs_row0']['new_false_accept'])))
    md.append('\nFalse acceptance by type (raw) and the real ids per row are in the json '
              '(`fa_by_type_raw`, `fa_lenient_ids`, `fa_strict_ids`, `fa_*_by_type`).\n')
    md.append('## Guard kills per row — correct set / wrong set\n')
    md.append('| row | F1 | F2 | F3 | F4 | F4v2 | F5 | F2B | L2 vetoes |')
    md.append('|---|---|---|---|---|---|---|---|---|')
    for r in rows:
        g = r['guard_kills']

        def cell(k):
            return '%d/%d' % (g.get(k, {}).get('kills_correct_n', 0), g.get(k, {}).get('kills_wrong_n', 0))
        md.append('| %s | %s | %s | %s | %s | %s | %s | %s | %s |'
                  % (r['label'], cell('F1'), cell('F2'), cell('F3'), cell('F4'), cell('F4v2'), cell('F5'),
                     cell('F2B'), cell('L2')))
    md.append('\n### Killed ids per guard and row\n')
    for r in rows:
        for g, v in r['guard_kills'].items():
            if v.get('kills_correct') or v.get('kills_wrong'):
                md.append('- %s **%s** — correct: %s | wrong: %s'
                          % (r['label'], g, ', '.join(v['kills_correct']) or 'none',
                             ', '.join(v['kills_wrong']) or 'none'))
    md.append('\n## Regressions vs row 0 (ids)\n')
    for r in rows[1:]:
        v = r['vs_row0']
        md.append('- **%s** — correct newly rejected: %s | wrong newly accepted: %s | wrong newly rejected: %s'
                  % (r['label'], ', '.join(v['lost_correct']) or 'none',
                     ', '.join(v['new_false_accept']) or 'none', ', '.join(v['fixed_wrong']) or 'none'))
    md.append('\n## F5 cost on the 235, reported on its own\n')
    md.append('- kills on the correct set: **%d** (of which %d were being accepted before F5)'
              % (f5_block['cost_on_235_total'], f5_block['cost_on_235_that_were_accepted_before']))
    for x in f5_block['kills_on_235']:
        md.append('  - `%s` (%s) deleted **%s** — %s\n    - reference: %s\n    - answer: %s'
                  % (x['item_id'], x['level'], x['deleted_span'], x['why'], x['reference'], x['answer']))
    md.append('- kills on the 105 wrong: %d (of which %d were being accepted)'
              % (f5_block['kills_on_105_total'], f5_block['kills_on_105_that_were_accepted_before']))
    md.append('\n## F4v2 verification: **%s**\n' % ver['verdict'])
    for x in ver['c9498'] + ver['must_fire']:
        md.append('- `%s` F4v2 fires: **%s** (Phase 1f F4 fired: %s)\n  - answer: %s\n  - trace: %s'
                  % (x['item_id'], x['f4v2_fires'], x['f4_1f_fired'], x['answer'],
                     json.dumps(x['trace'], ensure_ascii=False)))
    md.append('- F4v2 cost on the 235: %d %s' % (ver['cost_on_235_total'],
                                                 [x['item_id'] for x in ver['cost_on_235']]))
    md.append('- F4v2 kills on the 105: %d (%d of them were being accepted)'
              % (ver['kills_on_105_total'], sum(1 for x in ver['kills_on_105'] if x['was_accepted'])))
    md.append('\n## F2 boundary on the two disputed items\n')
    for iid, d in disp.items():
        md.append('- `%s` → **%s** (boundary fires: %s)\n  - Slovak: %s\n  - reference: %s\n  - answer: %s\n'
                  '  - trace: %s'
                  % (iid, d.get('comes_out_as'), d.get('boundary_fires'), d.get('sk'), d.get('reference'),
                     d.get('answer'), json.dumps(d.get('trace'), ensure_ascii=False)))
    md.append('- boundary kills on the 235: %d %s' % (f2b_block['kills_on_235_total'],
                                                      [x['item_id'] for x in b_kills_c]))
    md.append('- boundary kills on the 105: %d %s' % (f2b_block['kills_on_105_total'],
                                                      [x['item_id'] for x in b_kills_w]))
    md.append('\n## Sample size for an observed 2 %% false-acceptance rate\n```\n%s\n```'
              % json.dumps(ss, indent=1))
    md.append('\n## Call counts\n```\n%s\n```' % json.dumps(counts, indent=1))
    jp = os.path.join(HERE, 'results_%s.json' % ts)
    mp = os.path.join(HERE, 'results_%s.md' % ts)
    with open(jp, 'x') as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1, default=str)
    with open(mp, 'x') as fh:
        fh.write('\n'.join(md) + '\n')
    for r in rows:
        print('%-34s %s cov %3d (%4.1f %%)  raw %2d  lenient %2d [%.1f–%.1f]  strict %2d [%.1f–%.1f]'
              % (r['label'], r['variant'], r['coverage_n'], r['coverage_pct'], r['fa_raw'],
                 r['fa_lenient'], r['fa_lenient_ci95'][0], r['fa_lenient_ci95'][1],
                 r['fa_strict'], r['fa_strict_ci95'][0], r['fa_strict_ci95'][1]))
    print('F5 cost on the 235: %d (accepted before: %d) | F4v2 %s | boundary kills 235: %d / 105: %d'
          % (f5_block['cost_on_235_total'], f5_block['cost_on_235_that_were_accepted_before'],
             ver['verdict'], f2b_block['kills_on_235_total'], f2b_block['kills_on_105_total']))
    print('calls: new %d, reused %d, failed %d, cap %d' % (counts['new'], counts['reused'],
                                                           counts['failed'], counts['cap']))
    print('wrote %s and %s' % (os.path.basename(jp), os.path.basename(mp)))


def selftest():
    ok = True
    correct, wrong = base.load_items()        # RAW items: this assertion must still reproduce 1e routing
    print('loaded %d correct, %d wrong' % (len(correct), len(wrong)))
    if (len(correct), len(wrong)) != (235, 105):
        ok = False
        print('  FAIL: the frozen sets changed')
    rc = Counter(base.route(it)[0] for it in correct)
    rw = Counter(base.route(it)[0] for it in wrong)
    print('routing correct %s wrong %s (1e: C 100/48/87, W 9/39/57)' % (dict(rc), dict(rw)))
    if (rc['L1'], rc['L2'], rc['L3'], rw['L1'], rw['L2'], rw['L3']) != (100, 48, 87, 9, 39, 57):
        ok = False
        print('  FAIL: routing does not reproduce 1e')
    bud = Bud1h()
    need = needed_items(correct, wrong)
    for v in ('P-B', 'P-C'):
        have = verdict_map(v, bud)
        print('  %s: needed %d, cached %d, to call %d'
              % (v, len(need), sum(1 for it in need if it['item_id'] in have),
                 sum(1 for it in need if it['item_id'] not in have)))
    byid = {it['item_id']: it for it in correct + wrong}
    print('F4v2 required cases:')
    for iid in [i for i in byid if i.startswith('C:9498:')] + ['W:4571:4142535241', 'W:3494:4150910632']:
        f, tr = f4v2_subject_mismatch(byid[iid])
        want = not iid.startswith('C:9498:')
        if f != want:
            ok = False
        print('  %s %s fires=%s want=%s %s' % ('ok  ' if f == want else 'FAIL', iid, f, want,
                                               json.dumps(tr, ensure_ascii=False)))
    print('F5 on the ids named in 1f §8.4 / §5.1:')
    for iid in ('W:4612:586139873', 'W:11348:2987233244', 'W:7238:1943930546', 'W:8824:1740944184',
                'W:9907:325819033', 'W:14266:2043261128'):
        if iid in byid:
            f, tr = f5_adjunct_deletion(byid[iid])
            print('  %s fires=%s %s' % (iid, f, json.dumps(tr, ensure_ascii=False)[:240]))
    print('F2 boundary on the disputed items:')
    for iid in DISPUTED:
        if iid in byid:
            f, tr = f2_boundary_violation(byid[iid])
            print('  %s fires=%s %s' % (iid, f, json.dumps(tr, ensure_ascii=False)[:280]))
            print('     sk  = %s' % byid[iid]['sk'])
            print('     ref = %s' % byid[iid]['reference'])
            print('     ans = %s' % byid[iid]['answer'])
    print('CP check: 2/105 -> %s ; 6/105 -> %s' % (clopper_pearson(2, 105), clopper_pearson(6, 105)))
    print('SELFTEST %s' % ('PASS' if ok else 'FAIL'))
    return ok




# ================================================================ Phase 1h additions
import threading, time as _time, hashlib as _hashlib
from concurrent.futures import ThreadPoolExecutor

SK_OF = {}                      # exercise_id -> Slovak, filled by the loaders (hygiene 2.3 b needs it)
FRESH = os.path.join(HERE, 'fresh')
HYG_DIR = os.path.join(HERE, 'hygiene')

# ---------------------------------------------------------------- existing synonym groups (read-only)
SYN_FILES = ('table.json', 'ng_phase1c.json', 'review_added.json')
_SYN = None


def syn_groups():
    """The synonym groups that already exist in the project (phase1c/synonyms/*). No new word table."""
    global _SYN
    if _SYN is None:
        gs = []
        for fn in SYN_FILES:
            p = os.path.join(base.P1C, 'synonyms', fn)
            if os.path.exists(p):
                for g in (json.load(open(p)).get('groups') or []):
                    m = [base.norm(x).strip() for x in (g.get('m') or [])]
                    if len(m) > 1:
                        gs.append(m)
        _SYN = gs
    return _SYN


def syn_equivalents(phrase):
    """Co-members of every existing group that contains `phrase`."""
    p = base.norm(phrase).strip()
    out = set()
    for m in syn_groups():
        if p in m:
            out |= set(m)
    out.discard(p)
    return out


# ---------------------------------------------------------------- 2.1 L2 lock, non-verb spans
LINKERS = set(CONCESSIVE)                      # already in the code
RELATIVISERS = {'that', 'which', 'who', 'whom', 'whose'}


def _lock_is_non_verb(lk):
    """True when the locked span is a preposition or a linker (never a verb pattern)."""
    t = base.norm(lk).strip()
    if not t:
        return False
    if t in LINKERS:
        return True
    w = t.split()
    return all(x in PREP_HEADS or x in RELATIVISERS for x in w) and not any(x in AUX for x in w)


def lock_equivalent_ok(it):
    """2.1 — an equivalent preposition / linker satisfies the lock. Only for non-verb locked spans, only
    through the synonym groups that already exist (phase1c/synonyms/* and the item's own `alt`), and the
    equivalent must itself be a preposition or a linker."""
    ans = base.norm(it['answer'])
    a = annot(it['exercise_id'])
    alt = {base.norm(k).strip(): [base.norm(x).strip() for x in v]
           for k, v in (a.get('alt') or {}).items()}
    for lk in it.get('locks') or []:
        if not _lock_is_non_verb(lk):
            continue
        lkn = base.norm(lk).strip()
        cands = set(syn_equivalents(lkn))
        cands |= set(alt.get(lkn) or [])
        for k, vs in alt.items():
            if lkn in vs:
                cands |= set(vs) | {k}
        cands.discard(lkn)
        for c in cands:
            if not c or not _lock_is_non_verb(c):
                continue
            if (' ' + c + ' ') in ans:
                return True, {'lock': lk, 'equivalent': c}
    return False, None


def load_items_1h():
    """base.load_items() + 2.1. phase1c/ is read-only; only the in-memory item is changed."""
    correct, wrong = base.load_items()
    for it in correct + wrong:
        SK_OF.setdefault(it['exercise_id'], it['sk'])
        it['set'] = 'OLD'
    _ANN.clear()                             # re-read annotations now that SK_OF is filled (hygiene b)
    for it in correct + wrong:
        it['lock_released_2_1'] = None
        if not it['lock_ok']:
            ok, tr = lock_equivalent_ok(it)
            if ok:
                it['lock_ok'] = True
                it['lock_released_2_1'] = tr
    return correct, wrong


# ---------------------------------------------------------------- 2.2 F2B span match
def en_span_tokens(it):
    """EN_SPAN plus the renderings of a span that THIS item's annotation already accepts: the `p`
    insertions (+word), the `alt` members, and the co-members of the existing synonym groups that contain
    an EN_SPAN word. Fixes the over-eager 'stated span dropped' on C:9498 ('entire school' for 'cela')."""
    a = annot(it['exercise_id'])
    out = set(EN_SPAN)
    for m in syn_groups():
        if set(m) & EN_SPAN:
            out |= {x for x in m if ' ' not in x}
    for e in (a.get('p') or []):
        s = str(e)
        if s.startswith('+'):
            tok = base.norm(s[1:].split('@')[0]).strip()
            for w in tok.split():
                out.add(w)
    for k, vs in (a.get('alt') or {}).items():
        kk = set(toks(base.norm(k)))
        if kk & EN_SPAN:
            for v in vs:
                out |= set(toks(base.norm(v)))
    return out


# ---------------------------------------------------------------- fresh set loader (schema frozen here)
def _iid(kind, sid, en):
    return '%s:%d:%d' % (kind, int(sid), int(_hashlib.md5(en.encode()).hexdigest()[:8], 16))


def _jl_glob(pat):
    import glob
    rows = []
    for p in sorted(glob.glob(os.path.join(FRESH, pat))):
        rows += jl(p)
    return rows


def load_fresh():
    """The 60 new sentences. Returns (correct, wrong); empty lists when no fresh data exists yet."""
    sents = {int(r['sid']): r for r in jl(os.path.join(FRESH, 'new_sentences_60.jsonl'))}
    for sid, r in sents.items():
        SK_OF.setdefault(sid, r.get('sk'))
    if not sents:
        return [], []
    refs = {}
    for sid in sents:
        a = raw_annot(sid)
        v = [x for x in (a.get('v') or []) if isinstance(x, str)]
        refs[sid] = v[0] if v else (sents[sid].get('reference') or '')

    def mk(r, kind):
        sid = int(r['sid'])
        s = sents[sid]
        chk = r.get('chk') or {}
        lk = [x for x in (raw_annot(sid).get('lk') or []) if isinstance(x, str) and x.strip()]
        en = r['en']
        it = {'item_id': _iid(kind, sid, en), 'kind': kind, 'exercise_id': sid, 'set': 'NEW',
              'level': s.get('level'), 'topic': s.get('topic'), 'sk': s.get('sk'),
              'reference': refs.get(sid, ''), 'answer': en,
              'verdict': chk.get('verdict', 'wrong'), 'step': chk.get('step', 'auto'),
              'feedback': chk.get('feedback', ''), 'chk_missing': not chk,
              'wrong_type': r.get('type'), 'wrong_why': r.get('why', ''), 'locks': lk,
              'fa_class': None, 'fa_judgement': None, 'n': r.get('n')}
        it['lock_ok'] = (not lk) or any(base.norm(x).strip() in base.norm(en) for x in lk)
        it['lock_released_2_1'] = None
        if not it['lock_ok']:
            ok, tr = lock_equivalent_ok(it)
            if ok:
                it['lock_ok'], it['lock_released_2_1'] = True, tr
        return it

    correct = [mk(r, 'C') for r in _jl_glob('correct_part*.jsonl')]
    wrong = [mk(r, 'W') for r in _jl_glob('wrong_part*.jsonl')]
    return correct, wrong


def judgements_fresh():
    """{(set,item_id): 'correct'|'wrong'} from fresh/judgements.jsonl (the headline denominators)."""
    out = {}
    p = os.path.join(FRESH, 'judgements.jsonl')
    sents = {int(r['sid']): r for r in jl(os.path.join(FRESH, 'new_sentences_60.jsonl'))}
    idx = {}
    for kind, pat in (('C', 'correct_part*.jsonl'), ('W', 'wrong_part*.jsonl')):
        for r in _jl_glob(pat):
            idx[(kind, int(r['sid']), int(r['n']))] = _iid(kind, int(r['sid']), r['en'])
    for r in jl(p):
        k = (r['set'], int(r['sid']), int(r['n']))
        if k in idx:
            out[idx[k]] = r['real']
    _ = sents
    return out


# ---------------------------------------------------------------- calls: priority, concurrency, cap
_LEDGER_LOCK = threading.Lock()
_orig_append = base.ledger_append


def _locked_append(rec):
    with _LEDGER_LOCK:
        return _orig_append(rec)


base.ledger_append = _locked_append
PRIORITY = (('NEW', 'P-B'), ('NEW', 'P-C'), ('OLD', 'P-B'), ('OLD', 'P-C'))


def call_plan():
    """-> [(variant, item)] in the pre-registered priority order, reuse only on the OLD sets."""
    oc, ow = load_items_1h()
    fc, fw = load_fresh()
    bud = Bud1h()
    plan, seen = [], set()
    for st, var in PRIORITY:
        items = needed_items(oc, ow) if st == 'OLD' else needed_items(fc, fw)
        have = verdict_map(var, bud) if st == 'OLD' else verdict_map_own(var, bud)
        for it in items:
            k = (var, it['item_id'])
            if it['item_id'] in have or k in seen:
                continue
            seen.add(k)
            plan.append((var, it, st))
    return plan, bud


def verdict_map_own(variant, bud):
    """Fresh items may only use 1h's OWN ledger — never a previous phase's verdict."""
    return {k[2]: v['verdict'] for k, v in bud.own.items() if k[0] == MODEL and k[1] == variant}


def stage_calls_1h(threads=7):
    plan, bud = call_plan()
    cfg = cfg_1h()
    room = CAP - bud.used
    todo = plan[:max(0, room)]
    skipped = plan[len(todo):]
    print('plan %d, room %d, calling %d, not measured %d' % (len(plan), room, len(todo), len(skipped)))
    res = {'new': 0, 'failed': 0, 'capped': len(skipped)}
    lock = threading.Lock()

    def one(job):
        var, it, _st = job
        t0 = _time.time()
        r = base.call_model(bud, MODEL, var, it, cfg, max_out=MAX_OUT)
        ms = int(1000 * (_time.time() - t0))
        with lock:
            if r is None:
                res['capped'] += 1
            elif r.get('verdict') in ('SAME', 'TIP', 'DIFF'):
                res['new'] += 1
            else:
                res['failed'] += 1                     # unparsable = FAILED, never guessed, never retried
        return ms

    with ThreadPoolExecutor(max_workers=threads) as ex:
        lat = list(ex.map(one, todo))
    out = {'plan': len(plan), 'called': len(todo), 'cap': CAP, 'used_before': bud.used,
           'not_measured': [{'variant': v, 'item_id': i['item_id'], 'set': s} for v, i, s in skipped],
           'latency_ms': sorted(lat), **res}
    json.dump(out, open(os.path.join(HERE, 'call_counts.json'), 'w'), indent=1)
    print(json.dumps({k: v for k, v in out.items() if k != 'not_measured'})[:600])


# ---------------------------------------------------------------- extra, pre-registered tabulation
BANDS = ((1, 6), (7, 9), (10, 12), (13, 16), (17, 99))
USAGE_ASSUMPTION = None            # filled from the Phase 1e/1f reports by cost_per_user()


def band(sk):
    n = len(re.findall(r"[^\s]+", sk or ''))
    for lo, hi in BANDS:
        if lo <= n <= hi:
            return '%d-%d' % (lo, hi)
    return '?'


def cp(k, n):
    lo, hi = clopper_pearson(k, n) if n else (0.0, 0.0)
    return {'k': k, 'n': n, 'pct': (100.0 * k / n) if n else None, 'lo': 100 * lo, 'hi': 100 * hi}


def row_flags(name):
    f = dict.fromkeys(FLAGS, False)
    for k in ('F1', 'F2', 'F3', 'F4v2', 'F5', 'F2B'):
        f[k] = True
    return f, ('P-B' if name == 'row7' else 'P-C')


_J1F = None


def real_old(iid):
    """Phase 1g's STRICT judgement list: phase1f/judgements_1f.json (`real`) plus the two disputed items.
    A wrong-set item the judges never reached counts as really wrong (conservative denominator)."""
    global _J1F
    if _J1F is None:
        _J1F = json.load(open(JUDGE_1F)) if os.path.exists(JUDGE_1F) else {}
    if iid in DISPUTED:
        return 'real'
    r = _J1F.get(iid)
    if not isinstance(r, dict):
        return 'unjudged'
    return 'real' if r.get('real') else 'not_real'


def tabulate_1h():
    """Pre-registered: coverage (exact CP) by level / length band / OLD vs NEW, real FA by type and layer,
    routing shares, latency, cost, every real FA listed, every false rejection dumped by cause."""
    oc, ow = load_items_1h()
    fc, fw = load_fresh()
    bud = Bud1h()
    judge_fresh = judgements_fresh()
    strict = set(DISPUTED)
    out = {'ts': utc(), 'rows': {}}
    lat = [r.get('ms') for r in jl(LEDGER) if r.get('counted') and r.get('ms')]
    lat = sorted(x for x in lat if isinstance(x, (int, float)))
    tok_in = sum((r.get('usage') or {}).get('promptTokenCount', 0) for r in jl(LEDGER) if r.get('counted'))
    tok_out = sum((r.get('usage') or {}).get('candidatesTokenCount', 0) for r in jl(LEDGER) if r.get('counted'))
    for name in ('row7', 'row8'):
        flags, var = row_flags(name)
        vm_old = verdict_map(var, bud)
        vm_new = verdict_map_own(var, bud)
        R = {}
        for tag, C, W, vm in (('OLD', oc, ow, vm_old), ('NEW', fc, fw, vm_new)):
            if not C and not W:
                continue
            dec_c = {it['item_id']: decide(it, flags, vm) for it in C}
            dec_w = {it['item_id']: decide(it, flags, vm) for it in W}
            if tag == 'OLD':
                jc = {it['item_id']: 'correct' for it in C}
                jw = {it['item_id']: ({'real': 'wrong'}.get(real_old(it['item_id']),
                                                              real_old(it['item_id']))) for it in W}
            else:
                jc = {it['item_id']: judge_fresh.get(it['item_id']) for it in C}
                jw = {it['item_id']: judge_fresh.get(it['item_id']) for it in W}
            jgd_c = [it for it in C if jc.get(it['item_id']) == 'correct']
            jgd_w = [it for it in W if jw.get(it['item_id']) == 'wrong']
            acc = lambda it, d: d[it['item_id']]['accepted']
            r = {'raw_coverage': cp(sum(1 for it in C if acc(it, dec_c)), len(C)),
                 'judged_coverage': cp(sum(1 for it in jgd_c if acc(it, dec_c)), len(jgd_c)),
                 'raw_fa': cp(sum(1 for it in W if acc(it, dec_w)), len(W)),
                 'judged_fa': cp(sum(1 for it in jgd_w if acc(it, dec_w)), len(jgd_w)),
                 'by_level': {}, 'by_band': {}, 'fa_by_type': {}, 'fa_by_layer': Counter(),
                 'fa_ids': [], 'false_rejections': [], 'routing': Counter(),
                 'not_measured': sum(1 for it in C + W
                                     if (dec_c.get(it['item_id']) or dec_w.get(it['item_id']))['verdict']
                                     == 'failed')}
            for lv in sorted({it['level'] for it in jgd_c}):
                s = [it for it in jgd_c if it['level'] == lv]
                r['by_level'][lv] = cp(sum(1 for it in s if acc(it, dec_c)), len(s))
            for b in sorted({band(it['sk']) for it in jgd_c}):
                s = [it for it in jgd_c if band(it['sk']) == b]
                r['by_band'][b] = cp(sum(1 for it in s if acc(it, dec_c)), len(s))
            r_unjudged = [it['item_id'] for it in W
                          if jw.get(it['item_id']) == 'unjudged' and acc(it, dec_w)]
            for it in jgd_w:
                if acc(it, dec_w):
                    d = dec_w[it['item_id']]
                    lay = 'L1' if d['layer'] == 'L1' else ('L2' if d['layer'] == 'L2' else 'L3')
                    r['fa_by_layer'][lay] += 1
                    r['fa_by_type'][it['wrong_type'] or '?'] = r['fa_by_type'].get(it['wrong_type'] or '?', 0) + 1
                    r['fa_ids'].append({'item_id': it['item_id'], 'level': it['level'], 'type': it['wrong_type'],
                                        'sk': it['sk'], 'reference': it['reference'], 'answer': it['answer'],
                                        'layer': d['layer'], 'why': d['why']})
            for it in jgd_c:
                d = dec_c[it['item_id']]
                r['routing'][d['layer']] += 1
                if not d['accepted']:
                    r['false_rejections'].append({'item_id': it['item_id'], 'level': it['level'],
                                                  'layer': d['layer'], 'why': d['why'], 'sk': it['sk'],
                                                  'reference': it['reference'], 'answer': it['answer'],
                                                  'cause': d['layer']})
            causes = Counter(x['cause'] for x in r['false_rejections'])
            assert sum(causes.values()) == len(r['false_rejections']), 'cause counts must sum to the total'
            r['fr_by_cause'] = dict(causes)
            r['accepted_but_unjudged'] = r_unjudged      # NOT counted as FA; a judge must resolve them
            r['fa_by_layer'] = dict(r['fa_by_layer'])
            r['routing'] = dict(r['routing'])
            R[tag] = r
        out['rows'][name] = R
    out['latency_ms'] = {'n': len(lat), 'median': (lat[len(lat) // 2] if lat else None),
                         'p95': (lat[int(0.95 * (len(lat) - 1))] if lat else None)}
    out['tokens'] = {'in': tok_in, 'out': tok_out}
    out['cost_note'] = ('price table in lib_prev.PRICE (per 1M tokens); usage assumption for cost per '
                        'active user per month: see phase1e/REPORT_PHASE1E.md §cost — restate it in the '
                        'Phase 1h report, it is not re-derived here.')
    p = os.path.join(HERE, 'results_1h_%s.json' % utc())
    json.dump(out, open(p, 'w'), indent=1, default=str)
    print('wrote %s' % p)
    for name, R in out['rows'].items():
        for tag, r in R.items():
            print('%s %s: coverage judged %s/%s raw %s/%s | FA judged %s/%s raw %s/%s | routing %s'
                  % (name, tag, r['judged_coverage']['k'], r['judged_coverage']['n'],
                     r['raw_coverage']['k'], r['raw_coverage']['n'], r['judged_fa']['k'], r['judged_fa']['n'],
                     r['raw_fa']['k'], r['raw_fa']['n'], r['routing']))
    return out


def hygiene_cmd(path):
    rep = hyg.run(path, HYG_DIR, SK_OF if SK_OF else None)
    print(json.dumps({k: v for k, v in rep.items() if k not in ('examples_a', 'examples_b',
                                                                'ids_a', 'ids_b')}, indent=1))
    return rep


def selftest_1h():
    ok = selftest()
    print('--- Phase 1h checks ---')
    correct, wrong = load_items_1h()
    rel = [it['item_id'] for it in correct + wrong if it.get('lock_released_2_1')]
    print('2.1 lock released on %d items: %s' % (len(rel), rel[:12]))
    if 'C:23669:2842578131' not in rel:
        ok = False
        print('  FAIL: C:23669:2842578131 (over/above) not released by 2.1')
    byid = {it['item_id']: it for it in correct + wrong}
    f, tr = f2_boundary_violation(byid['C:9498:582627860'])
    print('2.2 C:9498:582627860 F2B fires=%s %s' % (f, json.dumps(tr, ensure_ascii=False)[:220]))
    if f:
        ok = False
        print('  FAIL: F2B still withdraws the tip on C:9498:582627860')
    for iid in DISPUTED:
        if iid in byid:
            print('2.2 kept? %s fires=%s' % (iid, f2_boundary_violation(byid[iid])[0]))
    a = annot(9244)
    print('2.3a C:9244 optional now: %s' % sorted(optional_tokens({'exercise_id': 9244}))[:14])
    for it in correct:
        if it['item_id'] in ('C:9244:3704016824', 'C:9992:718425012'):
            print('2.3a F5 on %s fires=%s' % (it['item_id'], f5_adjunct_deletion(it)[0]))
    print('2.3b g chain on 5595: %s (raw %s)' % (annot(5595).get('g'), raw_annot(5595).get('g')))
    print('SELFTEST-1H %s' % ('PASS' if ok else 'FAIL'))
    return ok


def main_1h():
    a = sys.argv[1:]
    act = a[0] if a else '--selftest'
    if act == '--selftest':
        sys.exit(0 if selftest_1h() else 1)
    elif act == '--hygiene':
        load_items_1h()
        hygiene_cmd(a[1] if len(a) > 1 else os.path.join(base.P1C, 'annotated_after'))
    elif act == '--plan':
        plan, bud = call_plan()
        c = Counter((s, v) for v, _i, s in plan)
        print('ledger used %d of cap %d; plan %d calls: %s' % (bud.used, CAP, len(plan), dict(c)))
        if len(plan) > CAP - bud.used:
            print('OVER CAP: %d items will be reported as not measured' % (len(plan) - (CAP - bud.used)))
    elif act == '--calls':
        stage_calls_1h()
    elif act == '--tabulate':
        tabulate_1h()
    elif act == '--all':
        stage_calls_1h()
        tabulate_1h()
    else:
        print(__doc__)
        sys.exit(1)


def main():
    a = sys.argv[1:]
    act = a[0] if a else '--selftest'
    if act == '--selftest':
        sys.exit(0 if selftest() else 1)
    elif act == '--plan':
        correct, wrong = load_items_1h()
        need = needed_items(correct, wrong)
        bud = Bud1h()
        for v in ('P-B', 'P-C'):
            have = verdict_map(v, bud)
            print('%s needed %d, cached %d, to call %d'
                  % (v, len(need), sum(1 for it in need if it['item_id'] in have),
                     sum(1 for it in need if it['item_id'] not in have)))
    elif act == '--calls':
        stage_calls()
    elif act == '--tabulate':
        stage_tabulate()
    elif act == '--all':
        stage_calls()
        stage_tabulate()
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == '__main__':
    main_1h()

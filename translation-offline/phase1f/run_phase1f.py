#!/usr/bin/env python3
"""Phase 1f — four offline fixes (F1 lock pattern / F2 structure tip / F3 deletion / F4 subject) on the
frozen Phase 1c sets, measured with gemini-3.1-flash-lite only, prompts P-B and P-C.

  python3 phase1f/run_phase1f.py --selftest        # offline, no key, no network
  python3 phase1f/run_phase1f.py --recount         # writes veto_recount.json (offline)
  python3 phase1f/run_phase1f.py --plan            # needed calls per stage vs cap (offline)
  python3 phase1f/run_phase1f.py --stage calls_pb  # model calls, P-B, only what the cache is missing
  python3 phase1f/run_phase1f.py --stage calls_pc  # model calls, P-C
  python3 phase1f/run_phase1f.py --stage tabulate  # offline, re-runnable, 32 combos
  python3 phase1f/run_phase1f.py --all             # calls_pb, calls_pc, tabulate in that order

Everything reusable is imported from phase1e/run_phase1e.py (load_items, route, norm, http, load_key,
redact, parse_verdict, prompt, Budget/ledger, cost_block, model_config thinking). phase1c/ and phase1e/
are READ-ONLY here: this script writes only inside phase1f/ (own calls.jsonl ledger, own decisions.jsonl).
Results files are written with a UTC timestamp in mode 'x' — nothing is ever overwritten.
KEY RULE: GEMINI_API_KEY is read by base.load_key() at call time only, sent in the x-goog-api-key header,
never printed, never written, never on a command line. --plan/--selftest/--recount/--stage tabulate never
touch it.
"""
import json, os, re, sys, time, datetime
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
TO = os.path.dirname(HERE)
P1E = os.path.join(TO, 'phase1e')
sys.path.insert(0, P1E)
import run_phase1e as base                                      # noqa: E402  (reuse, never edit)

P1E_LEDGER = os.path.join(P1E, 'calls.jsonl')                   # read-only seed
LEDGER = os.path.join(HERE, 'calls.jsonl')                      # 1f's own append-only ledger
LOG = os.path.join(HERE, 'decisions.jsonl')
RECOUNT = os.path.join(HERE, 'veto_recount.json')
JUDGE_1F = os.path.join(HERE, 'judgements_1f.json')
LATEST = os.path.join(HERE, 'latest.txt')
CAP = 1200                                                      # HTTP attempts, 1f only
MAX_OUT = 24
MODEL = 'gemini-3.1-flash-lite'

# 1f gets its own ledger/log/caps; base.call_model reads these module globals at call time.
base.LEDGER, base.LOG, base.CALL_CAP, base.ATTEMPT_CAP = LEDGER, LOG, CAP, CAP

# P-B is byte-identical to 1e by construction: P-C is built by inserting one line into base.prompt(it,'P-B').
PC_LINE = ("The SLOVAK sentence is the ground truth and the English reference is only one valid rendering of "
           "it; judge the learner against the Slovak, not against the reference wording.")
_orig_prompt = base.prompt


def prompt(it, variant):
    if variant == 'P-C':
        lines = _orig_prompt(it, 'P-B').split('\n')
        lines.insert(len(lines) - 1, PC_LINE)
        return '\n'.join(lines)
    return _orig_prompt(it, variant)


base.prompt = prompt

# 1e §1 note: "raw FA column shows 24 / 22 / 11 including them" vs real 15 / 13 / 2 — the difference is
# exactly the 9 L1 accepts that Phase 1c had already judged tip-accept / valid reading, and 1e §3 states
# "Every L3 accept of a wrong-set item is counted as real - no re-review was done". So the only wrong-set
# items 1e judged NOT really false acceptances are those 9, identified by the frozen fa_class field.
NOT_REAL_FA_CLASSES = ('tip-accept', 'valid reading')
BASELINE_COVERAGE_PB = 177      # 1e §1, Flash-Lite x P-B = 75.3 % (235). The brief's 180/235 = 76.6 % is
BASELINE_COVERAGE_PA = 180      # 1e's P-A row; P-B is the baseline asked for here, so we assert 177.

# ---------------------------------------------------------------- grammar tables
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
# closed irregular table: base, past, participle(s)  — grammar knowledge, not item annotation
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
    """Contractions -> full forms; ambiguous ones become 'is|has' / 'had|would' slots."""
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
    """All plausible forms of a token: subset of base/s/ing/past/pp."""
    f = set()
    if tok.endswith('ing'):
        f.add('ing')
    if tok.endswith('ed'):
        f |= {'past', 'pp'}
    if tok in IRR_PAST or any(len(p) >= 4 and len(tok) > len(p) and tok.endswith(p) for p in IRR_PAST):
        f.add('past')                                 # prefixed irregulars: overcame, rewritten, unseen
    if tok in IRR_PP or any(len(p) >= 4 and len(tok) > len(p) and tok.endswith(p) for p in IRR_PP):
        f.add('pp')
    if tok in IRR_BASE:
        f.add('base')
    if tok.endswith('s') and not tok.endswith('ss') and not tok.endswith('ous'):
        f.add('s')
    if not f or (tok not in IRR_PAST and tok not in IRR_PP and not tok.endswith(('ing', 'ed', 's'))):
        f.add('base')
    return f


# ---------------------------------------------------------------- F1: lock as grammatical pattern
def parse_lock(lock):
    """-> dict(kind=..., chain=[aux...], verb=..., form=..., gap=bool, needs_to=bool) or kind='literal'."""
    tk = expand(toks(lock.replace('..', ' .. ')))
    tk = [t for t in tk if t]
    if not tk:
        return {'kind': 'literal'}
    gap = '' if '..' not in lock else 'gap'
    chain, verb, pron_inside, needs_to = [], None, False, False
    rest = []
    for i, t in enumerate(tk):
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
        if len(chain) >= 2:                           # lock "had been": aux chain + be/have as main verb
            verb, chain = chain[-1], chain[:-1]
        else:                                         # bare aux/modal lock ("can", "must", "is")
            return {'kind': 'bare_aux', 'chain': chain, 'literal': ' '.join(chain)}
    needs_to = 'to' in rest[:1]
    # non-verb locks: determiner+noun, quantifier, function word
    vf = form_of(verb)
    if not chain:
        if tk[0] in DET and len(tk) >= 2:
            return {'kind': 'det_noun', 'head': tk[-1]}
        for cls in QUANT_CLASSES:
            if ' '.join(tk) in cls or tk[0] in cls:
                return {'kind': 'quant', 'cls': cls}
        if verb in FUNCTION:
            return {'kind': 'literal'}
        # bare main verb: form from morphology (prefer the most specific)
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
    lift = pat.get('aux_main')                        # lock's main verb is be/have/do -> aux tokens allowed
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


# ---------------------------------------------------------------- F2: structure equivalents (closed table)
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
    """-> (family, hit) when the answer uses a recognised structural equivalent of the lock, else None."""
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
            for i, t in enumerate(at):                      # be-passive -> get-passive
                if t in ('get', 'gets', 'got', 'getting', 'gotten'):
                    if any('pp' in form_of(x) and x not in FUNCTION for x in at[i + 1:i + 3]):
                        return 'be-passive->get-passive', 'got ' + at[i + 1]
        if low in VERB_PATTERN_EQUIV:
            h = _has(a, VERB_PATTERN_EQUIV[low])
            if h:
                return '%s->%s' % (low, h), h
        if 'causative' in topic.lower() and pat.get('kind') == 'pattern' and pat['form'] == 'pp':
            for i, t in enumerate(at):                      # had sth done -> had sb do sth
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
            for i, t in enumerate(at):                      # were + -ing subjunctive for a past simple
                if t in ('was', 'were') and any(x.endswith('ing') for x in at[i + 1:i + 3]):
                    return 'past-simple->were+ing (subjunctive)', '%s %s' % (t, at[i + 1])
    return None


def f2_tip(it):
    return 'use the target structure: %s' % (it['locks'][0] if it['locks'] else '?')


# ---------------------------------------------------------------- F3: deletion guard
_ANN = {}


def annot(eid):
    if eid not in _ANN:
        p = os.path.join(base.P1C, 'annotated_after', '%d.json' % eid)
        _ANN[eid] = json.load(open(p)) if os.path.exists(p) else {}
    return _ANN[eid]


def refs_of(it):
    a = annot(it['exercise_id'])
    out = [it['reference']] + [v for v in (a.get('v') or []) if isinstance(v, str)]
    seen, uniq = set(), []
    for r in out:
        if r not in seen:
            seen.add(r)
            uniq.append(r)
    return uniq


def optional_tokens(it):
    """Words the item data itself marks as alternatives/optional: 'd' (determiner or word alternatives) keys
    and values, plus anything in parentheses in an accepted variant. There is no other optional marker in the
    1e item data (annotated_after: v / lk / s / d / m / alt)."""
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
    """learner subsequence of ref (both stripped of optional words) -> list of missing ref tokens."""
    L = [t for t in learner if t not in opt]
    R = [t for t in ref if t not in opt]
    i, missing = 0, []
    for t in R:
        if i < len(L) and L[i] == t:
            i += 1
        else:
            missing.append(t)
    if i < len(L):
        return None                                   # learner has tokens the reference does not -> not a deletion
    return missing


def f3_deletion(it):
    """-> (True, missing_content_words) when the answer is a pure deletion from EVERY accepted reference."""
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


# ---------------------------------------------------------------- F4: subject guard
SK_PRON = {'ja': ('1', 'sg', None), 'ty': ('2', 'sg', None), 'on': ('3', 'sg', 'm'),
           'ona': ('3', 'sg', 'f'), 'ono': ('3', 'sg', 'n'), 'my': ('1', 'pl', None),
           'vy': ('2', 'pl', None), 'oni': ('3', 'pl', 'm'), 'ony': ('3', 'pl', 'f')}
SK_AUX = {'som': ('1', 'sg'), 'si': ('2', 'sg'), 'sme': ('1', 'pl'), 'ste': ('2', 'pl')}
EN_SUBJ = {'i': ('1', 'sg', None), 'we': ('1', 'pl', None), 'you': ('2', None, None),
           'he': ('3', 'sg', 'm'), 'she': ('3', 'sg', 'f'), 'it': ('3', 'sg', 'n'),
           'they': ('3', 'pl', None)}


SK_PART = re.compile(r'(al|il|ol|ul|el|yl|ml|dl|tl|sl|hl|žl|čl)(a|o|i)?$')


def sk_subject(sk):
    """Conservative (person, number, gender); None in a slot means the Slovak leaves it open. 1st/2nd person
    from an explicit pronoun, the past-tense auxiliary or an unambiguous ending; 3rd-person number/gender only
    from a past participle (-l/-la/-lo/-li). base.norm() must NOT be used here: it deletes Slovak diacritics
    and would turn 'necháš' into 'nech' and 'stolička' into a fake -li participle."""
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
    """Nominative pronouns in order = the clause subjects (EN_SUBJ has no object forms)."""
    return [w for w in expand(toks(text)) if w in EN_SUBJ]


def _compat(s, e):
    sp, sn, sg = s
    ep, en_, eg = e
    if sp == '2' and ep == '2':                       # "you" matches both ty and vy
        return True
    if sp != ep:
        return False
    if sn and en_ and sn != en_:
        return False
    if sg and eg and sg in ('m', 'f') and eg in ('m', 'f') and sg != eg:
        return False
    return True


def f4_subject_mismatch(it):
    """Fires only when BOTH sides are confidently determined: the Slovak fixes the subject, the reference
    (a correct rendering) confirms that reading, and the answer's aligned subject contradicts it."""
    s = sk_subject(it['sk'])
    R, A = en_subjects(it['reference']), en_subjects(it['answer'])
    if not s or not R or len(R) != len(A):
        return False, ''
    for r, a in zip(R, A):
        if r != a and _compat(s, EN_SUBJ[r]) and not _compat(s, EN_SUBJ[a]):
            return True, "subject '%s' for '%s'; the Slovak fixes person/number/gender %s" % (a, r, s)
    return False, ''


# ---------------------------------------------------------------- decide (offline pipeline per combo)
FLAGS = ('F1', 'F2', 'F3', 'F4')


def decide(it, flags, verdicts):
    """-> dict(layer, verdict, accepted, tip, why). verdicts: {item_id: 'SAME'|'TIP'|'DIFF'|None}"""
    if flags.get('F3'):
        hit, miss = f3_deletion(it)
        if hit:
            return {'layer': 'F3', 'accepted': False, 'verdict': 'wrong', 'tip': None,
                    'why': 'missing meaning (%s)' % ' '.join(miss[:4])}
    if flags.get('F4'):
        hit, why = f4_subject_mismatch(it)
        if hit:
            return {'layer': 'F4', 'accepted': False, 'verdict': 'wrong', 'tip': None, 'why': why}
    lay, why = base.route(it)
    if lay == 'L1':
        return {'layer': 'L1', 'accepted': True, 'verdict': it['verdict'], 'tip': None, 'why': why}
    tip = None
    if lay == 'L2':
        if it['step'] == 'mistake':
            return {'layer': 'L2', 'accepted': False, 'verdict': 'wrong', 'tip': None, 'why': why}
        released = False
        if flags.get('F1') and f1_lock_ok(it):
            released, why = True, 'F1 pattern match'
        if not released and flags.get('F2'):
            eq = f2_equivalent(it)
            if eq:
                released, tip, why = True, f2_tip(it), 'F2 structure equivalent (%s)' % eq[0]
        if not released:
            return {'layer': 'L2', 'accepted': False, 'verdict': 'wrong', 'tip': None, 'why': why}
    v = verdicts.get(it['item_id'])
    if v is None:
        return {'layer': 'L3', 'accepted': False, 'verdict': 'failed', 'tip': None, 'why': 'no parsed verdict'}
    if v == 'DIFF':
        return {'layer': 'L3', 'accepted': False, 'verdict': 'wrong', 'tip': None, 'why': 'model DIFF'}
    acc = 'correct_with_tip' if (tip or v == 'TIP') else 'correct'
    return {'layer': 'L3', 'accepted': True, 'verdict': acc, 'tip': tip or (None if v == 'SAME' else 'model tip'),
            'why': 'model %s' % v}


def needed_items(correct, wrong):
    """Items reaching L3 under ANY flag combination = F1+F2 on, F3/F4 off."""
    flags = {'F1': True, 'F2': True, 'F3': False, 'F4': False}
    out = []
    for it in correct + wrong:
        d = decide(it, flags, {})
        if d['layer'] == 'L3':
            out.append(it)
    return out


# ---------------------------------------------------------------- cache / ledger
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
    """P-B verdicts from 1e (read-only). Prompt is byte-identical by construction: same items from
    base.load_items(), same base.prompt(it,'P-B')."""
    out = {}
    for r in jl(P1E_LEDGER):
        if (r.get('model') == MODEL and r.get('variant') == 'P-B' and r.get('counted')
                and r.get('verdict') in ('SAME', 'TIP', 'DIFF')
                and '#probe' not in (r.get('item_id') or '') and '@' not in (r.get('item_id') or '')):
            out[(MODEL, 'P-B', r['item_id'])] = dict(r, from_1e=True)
    return out


class Bud1f(base.Budget):
    def __init__(self):
        base.Budget.__init__(self)                    # reads base.LEDGER == phase1f/calls.jsonl
        self.own = dict(self.cache)
        self.cache.update({k: v for k, v in seed_cache().items() if k not in self.cache})
        self.reused_1e = sum(1 for v in self.cache.values() if v.get('from_1e'))


def verdict_map(variant, bud):
    return {k[2]: v['verdict'] for k, v in bud.cache.items() if k[0] == MODEL and k[1] == variant}


def cfg_1f():
    cfgs = json.load(open(base.MODEL_CFG))
    c = dict(cfgs[MODEL])
    c['max_output'] = MAX_OUT                         # 1e thinking setting, 1f output cap
    return c


# ---------------------------------------------------------------- stages
def stage_calls(variant):
    correct, wrong = base.load_items()
    need = needed_items(correct, wrong)
    bud = Bud1f()
    have = verdict_map(variant, bud)
    todo = [it for it in need if it['item_id'] not in have]
    if len(todo) > CAP - bud.attempts:
        print('STOP: %s needs %d calls but only %d of the %d attempt cap are left.'
              % (variant, len(todo), CAP - bud.attempts, CAP))
        sys.exit(4)
    cfg = cfg_1f()
    print('stage calls_%s: %d needed, %d cached (%d reused from 1e), %d to call'
          % (variant[-1].lower(), len(need), len(need) - len(todo), bud.reused_1e, len(todo)))
    fails, done = [], 0
    for it in todo:
        r = base.call_model(bud, MODEL, variant, it, cfg)
        if r is None or r.get('verdict') in (None, 'PARSE_FAIL'):
            r = base.call_model(bud, MODEL, variant, it, cfg)          # retry ONCE, never guessed
        if r is None or r.get('verdict') not in ('SAME', 'TIP', 'DIFF'):
            fails.append(it['item_id'])
        else:
            done += 1
        base.log_decision({'stage': 'calls_' + variant, 'item_id': it['item_id'], 'variant': variant,
                           'verdict': (r or {}).get('verdict'), 'http': (r or {}).get('http')})
    out = {'stage': 'calls_' + variant, 'variant': variant, 'needed': len(need), 'called': len(todo),
           'parsed': done, 'failed_ids': fails, 'attempts_after': bud.attempts, 'r429': bud.r429,
           'reused_from_1e': bud.reused_1e, 'cap': CAP}
    write_results('calls_' + variant, out, '\n'.join('- %s: %s' % (k, v) for k, v in out.items()))
    print(json.dumps({k: v for k, v in out.items() if k != 'failed_ids'}))


def evaluate(correct, wrong, flags, variant, bud, judge):
    vm = verdict_map(variant, bud)
    rows = {'flags': {f: bool(flags.get(f)) for f in FLAGS}, 'variant': variant}
    dc = {it['item_id']: decide(it, flags, vm) for it in correct}
    dw = {it['item_id']: decide(it, flags, vm) for it in wrong}
    acc_c = [i for i, d in dc.items() if d['accepted']]
    rows['coverage_n'] = len(acc_c)
    rows['coverage_pct'] = round(100 * len(acc_c) / 235, 1)
    rows['accepted_correct'] = sum(1 for i in acc_c if dc[i]['verdict'] == 'correct')
    rows['accepted_with_tip'] = sum(1 for i in acc_c if dc[i]['verdict'] == 'correct_with_tip')
    bylv = defaultdict(lambda: [0, 0])
    for it in correct:
        b = bylv[it['level']]
        b[1] += 1
        b[0] += 1 if dc[it['item_id']]['accepted'] else 0
    rows['coverage_by_level'] = {k: '%d/%d = %.1f %%' % (v[0], v[1], 100 * v[0] / v[1]) for k, v in sorted(bylv.items())}
    acc_w = [it for it in wrong if dw[it['item_id']]['accepted']]
    notreal = {it['item_id'] for it in wrong if (it.get('fa_class') or '') in NOT_REAL_FA_CLASSES}
    unjudged = []
    real = 0
    for it in acc_w:
        iid = it['item_id']
        if iid in notreal:
            continue
        j = judge.get(iid)
        if j is None:
            unjudged.append({'item_id': iid, 'type': it['wrong_type'], 'sk': it['sk'],
                             'reference': it['reference'], 'answer': it['answer']})
            real += 1                                  # unjudged counts as REAL (conservative)
        elif j.get('real'):
            real += 1
    rows['fa_raw'] = len(acc_w)
    rows['fa_real'] = real
    rows['fa_real_pct'] = round(100 * real / 105, 1)
    rows['fa_by_type_raw'] = dict(Counter(it['wrong_type'] or '?' for it in acc_w))
    rows['fa_by_type_real'] = dict(Counter(it['wrong_type'] or '?' for it in acc_w
                                           if it['item_id'] not in notreal))
    rows['unjudged_acceptances'] = unjudged
    rows['layers_correct'] = dict(Counter(d['layer'] for d in dc.values()))
    rows['layers_wrong'] = dict(Counter(d['layer'] for d in dw.values()))
    rows['failed_calls'] = sum(1 for d in list(dc.values()) + list(dw.values()) if d['verdict'] == 'failed')
    rows['_dc'], rows['_dw'] = dc, dw
    return rows


def combos():
    out = []
    for n in range(16):
        out.append({f: bool(n >> i & 1) for i, f in enumerate(FLAGS)})
    return out


def stage_tabulate():
    correct, wrong = base.load_items()
    bud = Bud1f()
    judge = json.load(open(JUDGE_1F)) if os.path.exists(JUDGE_1F) else {}
    recount = do_recount(correct, quiet=True)
    allrows = []
    for v in ('P-B', 'P-C'):
        for fl in combos():
            allrows.append(evaluate(correct, wrong, fl, v, bud, judge))
    key = lambda r: (r['variant'], tuple(r['flags'][f] for f in FLAGS))
    idx = {key(r): r for r in allrows}
    base_row = idx[('P-B', (False, False, False, False))]
    warn = None
    if base_row['coverage_n'] != BASELINE_COVERAGE_PB:
        warn = ('!!! LOUD WARNING: the P-B no-flag baseline is %d/235, not the 1e value %d/235 (75.3 %%). '
                'The measuring apparatus is suspect first.' % (base_row['coverage_n'], BASELINE_COVERAGE_PB))
        print(warn)
    else:
        print('baseline OK: P-B no flags = %d/235 = %.1f %% reproduces 1e §1 (the brief\'s 180/235 = 76.6 %% '
              'is 1e\'s P-A row, not P-B)' % (base_row['coverage_n'], base_row['coverage_pct']))

    def reg(row):
        g_c = [i for i, d in row['_dc'].items() if d['accepted'] and not base_row['_dc'][i]['accepted']]
        r_c = [i for i, d in row['_dc'].items() if not d['accepted'] and base_row['_dc'][i]['accepted']]
        g_w = [i for i, d in row['_dw'].items() if not d['accepted'] and base_row['_dw'][i]['accepted']]
        r_w = [i for i, d in row['_dw'].items() if d['accepted'] and not base_row['_dw'][i]['accepted']]
        return {'gained_correct': g_c, 'lost_correct': r_c, 'fixed_wrong': g_w, 'new_false_accept': r_w}

    for r in allrows:
        r['vs_baseline'] = reg(r)
    qual = [r for r in allrows if r['fa_real'] <= 2]
    best = max(qual, key=lambda r: r['coverage_n']) if qual else min(allrows, key=lambda r: (r['fa_real'], -r['coverage_n']))
    order = [('Phase 1e baseline (P-B, no flags)', 'P-B', (0, 0, 0, 0)),
             ('+F1', 'P-B', (1, 0, 0, 0)), ('+F2', 'P-B', (0, 1, 0, 0)), ('+F3', 'P-B', (0, 0, 1, 0)),
             ('+F4', 'P-B', (0, 0, 0, 1)), ('F1+F2', 'P-B', (1, 1, 0, 0)),
             ('all four', 'P-B', (1, 1, 1, 1)), ('all four with P-C', 'P-C', (1, 1, 1, 1))]
    named = [(lab, idx[(v, tuple(bool(x) for x in f))]) for lab, v, f in order]
    named.append(('best found%s' % ('' if qual else ' (NONE qualifies at <=2 real FA; lowest-FA row shown)'), best))

    # F3 / F4 offline cost and savings, measured separately
    fx = {}
    for f in ('F3', 'F4'):
        base_fl = {'F1': True, 'F2': True, 'F3': False, 'F4': False}
        vm = verdict_map('P-B', bud)
        kills_c, kills_w = [], []
        for it in correct:
            d0 = decide(it, base_fl, vm)
            d1 = decide(it, dict(base_fl, **{f: True}), vm)
            if d1['layer'] == f:
                kills_c.append({'item_id': it['item_id'], 'why': d1['why'],
                                'would_have_been_accepted': bool(d0['accepted'])})
        for it in wrong:
            d0 = decide(it, base_fl, vm)
            d1 = decide(it, dict(base_fl, **{f: True}), vm)
            if d1['layer'] == f:
                kills_w.append({'item_id': it['item_id'], 'type': it['wrong_type'],
                                'was_accepted': bool(d0['accepted'])})
        fx[f] = {'cost_on_235': {'total': len(kills_c),
                                 'would_otherwise_be_accepted': [k for k in kills_c if k['would_have_been_accepted']],
                                 'rejected_anyway': [k for k in kills_c if not k['would_have_been_accepted']]},
                 'savings_on_105': {'total': len(kills_w),
                                    'real_savings_was_accepted': [k for k in kills_w if k['was_accepted']],
                                    'already_rejected': [k for k in kills_w if not k['was_accepted']]}}

    # latency / tokens / cost from 1f calls only
    mine = [r for r in jl(LEDGER) if r.get('counted') and r.get('latency_ms')]
    lat = sorted(r['latency_ms'] for r in mine if not r.get('cold'))
    pk = lambda q: lat[min(len(lat) - 1, int(q * len(lat)))] if lat else None
    tok = {k: (sum((r.get(v) or 0) for r in mine) / len(mine) if mine else 0)
           for k, v in (('in', 'prompt_tokens'), ('out', 'candidates_tokens'),
                        ('thoughts', 'thoughts_tokens'), ('cached', 'cached_tokens'))}
    l3_share = (best['layers_correct'].get('L3', 0)) / 235
    per_call, price = base.cost_block({'tok': tok}, base.PRICE['lite'])
    cost = {'calls_1f': len(mine), 'lat_median_ms': pk(0.5), 'lat_p95_ms': pk(0.95), 'tokens_avg': tok,
            'measured_spend_usd': 0.0 if not mine else None,
            'measured_spend_note': 'free tier: $0 billed; the figures below are list-price equivalents',
            'list_price_per_call_usd': per_call, 'price': price,
            'best_row_L3_share_of_correct': round(l3_share, 3),
            'usd_per_active_user_per_month': (per_call * 20 * 30 * l3_share) if per_call else None,
            'cost_assumptions': '1e cost_block: 20 exercises/day x 30 days x the best row\'s L3 share of '
                                'the correct-answer distribution; Flash-Lite $0.25 in / $1.50 out / $0.025 cached per 1M'}

    fr = [{'item_id': i, 'sk': it['sk'], 'reference': it['reference'], 'answer': it['answer'],
           'layer': best['_dc'][i]['layer'], 'why': best['_dc'][i]['why']}
          for it in correct for i in [it['item_id']] if not best['_dc'][i]['accepted']]
    out = {'ts': utc(), 'model': MODEL, 'baseline_warning': warn, 'recount_totals': recount['totals'],
           'rows': [{'label': lab, **{k: v for k, v in r.items() if not k.startswith('_')}} for lab, r in named],
           'all_32_combos': [{k: v for k, v in r.items() if not k.startswith('_')} for r in allrows],
           'f3_f4_offline': fx, 'cost': cost,
           'best': {'label': named[-1][0], 'flags': best['flags'], 'variant': best['variant'],
                    'coverage': '%d/235 = %.1f %%' % (best['coverage_n'], best['coverage_pct']),
                    'fa_real': best['fa_real'], 'remaining_false_rejections': fr},
           'reused_from_1e': bud.reused_1e, 'calls_1f': len(mine)}
    md = ['# Phase 1f — four offline fixes x {P-B, P-C}, %s\n' % MODEL,
          (warn or 'Baseline reproduced: P-B no flags = %d/235.' % base_row['coverage_n']) + '\n',
          '| row | variant | flags | coverage /235 | correct / with tip | FA raw | FA REAL | FA by type (raw) | L1/L2/L3 correct | F3/F4 kills | failed |',
          '|---|---|---|---|---|---|---|---|---|---|---|']
    for lab, r in named:
        lc = r['layers_correct']
        md.append('| %s | %s | %s | %d (%.1f %%) | %d / %d | %d | %d (%.1f %%) | %s | %d/%d/%d | %d/%d | %d |' % (
            lab, r['variant'], ''.join(f for f in FLAGS if r['flags'][f]) or '-', r['coverage_n'],
            r['coverage_pct'], r['accepted_correct'], r['accepted_with_tip'], r['fa_raw'], r['fa_real'],
            r['fa_real_pct'], json.dumps(r['fa_by_type_raw']), lc.get('L1', 0), lc.get('L2', 0), lc.get('L3', 0),
            lc.get('F3', 0), lc.get('F4', 0), r['failed_calls']))
    md.append('\n## F3 / F4 offline cost and savings\n```\n%s\n```' % json.dumps(
        {k: {'cost_on_235': {kk: (vv if isinstance(vv, int) else len(vv)) for kk, vv in v['cost_on_235'].items()},
             'savings_on_105': {kk: (vv if isinstance(vv, int) else len(vv)) for kk, vv in v['savings_on_105'].items()}}
         for k, v in fx.items()}, indent=1))
    md.append('\n## Cost\n```\n%s\n```' % json.dumps(cost, indent=1))
    md.append('\n## Best row\n```\n%s\n```' % json.dumps(out['best']['flags']) + '\n%s, real FA %d'
              % (out['best']['coverage'], best['fa_real']))
    md.append('\nRemaining false rejections of the best row: %d (ids and text in the json).' % len(fr))
    write_results('tabulate', out, '\n'.join(md))
    for lab, r in named:
        print('%-46s %s %-4s cov %3d (%4.1f %%)  FA raw %2d real %2d  failed %d'
              % (lab, r['variant'], ''.join(f for f in FLAGS if r['flags'][f]) or '-', r['coverage_n'],
                 r['coverage_pct'], r['fa_raw'], r['fa_real'], r['failed_calls']))


def utc():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')


def write_results(stage, obj, md):
    ts = utc()
    jp = os.path.join(HERE, 'results_%s_%s.json' % (stage, ts))
    mp = os.path.join(HERE, 'results_%s_%s.md' % (stage, ts))
    with open(jp, 'x') as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=1, default=str)
    with open(mp, 'x') as fh:
        fh.write(md + '\n')
    open(LATEST, 'w').write('%s %s\n%s\n' % (stage, os.path.basename(jp), os.path.basename(mp)))
    print('wrote %s and %s' % (os.path.basename(jp), os.path.basename(mp)))


# ---------------------------------------------------------------- recount of the 48 L2 vetoes
# One category per item, assigned by hand from the audit of all 48 (1e §2.2 gave ~17/~10/4/~18 = 49; this is
# the exact 48). string_artefact carries a sub-kind.
CAT = {
 'C:25921:2722616817': ('article_quantifier', "'the volcano' for lock 'a volcano': determiner alternative, noun intact"),
 'C:25921:4183818791': ('article_quantifier', "'the volcano' for lock 'a volcano', clause order moved"),
 'C:25921:281084965': ('article_quantifier', "'the volcano' for lock 'a volcano' (verb synonym observe/watch)"),
 'C:27097:2811648899': ('article_quantifier', "'loads of ads' for the quantifier lock 'many'"),
 'C:3603:3992987775': ('different_verb', "'would return' for lock 'would bring': modal+base intact"),
 'C:4612:1570109430': ('avoids_structure', "'were holding' for the past simple 'held' in the 2nd conditional"),
 'C:4612:661580552': ('avoids_structure', "'were him holding' for the past simple 'held'"),
 'C:7716:2396798202': ('avoids_structure', "'succeeded in staying' for 'managed to stay': gerund for infinitive"),
 'C:9907:2522110302': ('different_verb', "'had worn' for lock 'had taken': had+participle intact"),
 'C:9907:3412931110': ('string_artefact:contraction', "\"she'd taken\" = 'she had taken'"),
 'C:7558:2926388663': ('other', 'vetoed by the mistake library (step=mistake), not by the lock; F1/F2 never see it'),
 'C:7687:4238972801': ('string_artefact:gap', "'had the kitchen filmed' vs the gap lock 'had .. filmed'"),
 'C:7687:4155332440': ('avoids_structure', "active causative 'had someone film' for the passive 'had .. filmed'"),
 'C:7687:895858192': ('string_artefact:gap', "'had the kitchen filmed' vs the gap lock, clause order moved"),
 'C:9607:557999307': ('string_artefact:contraction', "\"It's said\" = 'it is said'"),
 'C:10043:3485295168': ('different_verb', "'had had' for lock 'had been': had+participle intact"),
 'C:26084:2889436188': ('avoids_structure', "'is able to find' for the modal 'can'"),
 'C:23669:2842578131': ('other', "non-verb lexical lock: 'over' for the preposition 'above'"),
 'C:24733:852799016': ('avoids_structure', "'have to hold' for 'must'"),
 'C:24733:3435761164': ('avoids_structure', "'need to hold' for 'must'"),
 'C:21124:3846512962': ('string_artefact:contraction', "\"she's dancing\" = 'she is dancing'"),
 'C:5595:3589927967': ('string_artefact:adverb', "'has finally stamped' vs lock 'has stamped'"),
 'C:5595:3701842021': ('different_verb', "'has put a stamp on' for 'has stamped' (adverb inside as well)"),
 'C:9244:3137708535': ('avoids_structure', "past simple 'rolled' for the past continuous 'were rolling'"),
 'C:6365:737430791': ('different_verb', "'would shoot' for 'would film'"),
 'C:6365:3896805648': ('avoids_structure', "'were going to shoot' for 'would film'"),
 'C:9498:3533979063': ('avoids_structure', 'zero relative clause for the lock that/which/behind which'),
 'C:9498:582627860': ('avoids_structure', 'zero relative clause for the lock that/which/behind which'),
 'C:9495:3595000117': ('avoids_structure', "get-passive 'got rewritten' for the be-passive 'was rewritten'"),
 'C:2929:3358097520': ('string_artefact:adverb', "'has completely gone out' vs lock 'has gone out'"),
 'C:119:1797996295': ('different_verb', "'has he been holding' for 'has she been tapping' (pronoun differs too)"),
 'C:119:3077862892': ('different_verb', "'has she been holding' for 'has she been tapping'"),
 'C:119:1941901414': ('string_artefact:pronoun', "'has he been tapping': pronoun inside the locked span"),
 'C:5959:1797630685': ('different_verb', "'will lower' for lock 'will drop'"),
 'C:5959:1103758532': ('different_verb', "\"she'll lower\": contraction plus a different verb"),
 'C:5959:378048785': ('different_verb', "'will reduce' for lock 'will drop'"),
 'C:3494:807783543': ('different_verb', "'had fallen' for lock 'had landed'"),
 'C:2955:580212365': ('string_artefact:contraction', "\"he'd turned\" = 'he had turned'"),
 'C:2874:218906999': ('avoids_structure', "'ought to have gone' for 'should have seen/gone'"),
 'C:8209:4039329764': ('different_verb', "'will have reserved' for 'will have booked'"),
 'C:10013:36155575': ('different_verb', "'is pushing' for 'is holding/is pressing'"),
 'C:10366:4213838839': ('different_verb', "'will have been heating' for 'will have been reheating'"),
 'C:10366:1295155330': ('different_verb', "'will have been warming up' for 'will have been reheating'"),
 'C:7998:2832146901': ('avoids_structure', "'that she now spends every morning on': stranded preposition for where/on which"),
 'C:10107:4080641578': ('other', "non-verb lexical lock: 'nevertheless' for the linker 'even so'"),
 'C:10107:2948469327': ('avoids_structure', "'Although the terminal was empty' instead of the practised linker"),
 'C:6884:2193979428': ('string_artefact:pronoun', "'Had he set off': inversion puts a pronoun inside the span"),
 'C:6884:181523403': ('different_verb', "'had set out' for 'had set off / had started / had left'"),
}
RELEASABLE = ('different_verb', 'article_quantifier')                  # + every string_artefact:*


def l2_correct(correct):
    return [it for it in correct if base.route(it)[0] == 'L2']


def do_recount(correct, quiet=False):
    items = l2_correct(correct)
    rows, tot = [], Counter()
    for it in items:
        cat, why = CAT.get(it['item_id'], ('other', 'UNCLASSIFIED'))
        rows.append({'item_id': it['item_id'], 'exercise_id': it['exercise_id'], 'lock': it['locks'],
                     'answer': it['answer'], 'reference': it['reference'], 'topic': it['topic'],
                     'category': cat.split(':')[0], 'sub': (cat.split(':')[1] if ':' in cat else None),
                     'reason': why})
        tot[cat.split(':')[0]] += 1
        if ':' in cat:
            tot['string_artefact:' + cat.split(':')[1]] += 1
    obj = {'n_items': len(items), 'source': 'the 48 correct items Phase 1e routed to L2',
           'note': '1e §2.2 estimated ~17 different-verb / ~10 string artefacts / 4 article-quantifier / '
                   '~18 different grammar = 49; this exact recount sums to %d' % len(items),
           'totals': dict(tot), 'items': rows}
    assert sum(v for k, v in tot.items() if ':' not in k) == len(items), 'totals must sum to %d' % len(items)
    if not quiet:
        with open(RECOUNT, 'w') as fh:
            json.dump(obj, fh, ensure_ascii=False, indent=1)
        print('veto_recount.json: %d items, totals %s' % (len(items), json.dumps(obj['totals'])))
    return obj


# ---------------------------------------------------------------- plan / selftest
def do_plan():
    correct, wrong = base.load_items()
    need = needed_items(correct, wrong)
    bud = Bud1f()
    pb_have = verdict_map('P-B', bud)
    pc_have = verdict_map('P-C', bud)
    pb = [it for it in need if it['item_id'] not in pb_have]
    pc = [it for it in need if it['item_id'] not in pc_have]
    print('needed set (reach L3 under ANY flag combo = F1+F2 on): %d items (%d correct, %d wrong)'
          % (len(need), sum(1 for i in need if i['kind'] == 'C'), sum(1 for i in need if i['kind'] == 'W')))
    print('  reused from 1e (P-B, byte-identical prompt): %d' % bud.reused_1e)
    print('  stage calls_pb: %d new calls' % len(pb))
    print('  stage calls_pc: %d new calls' % len(pc))
    print('  total planned %d + already spent in 1f %d = %d of the %d attempt cap'
          % (len(pb) + len(pc), bud.attempts, len(pb) + len(pc) + bud.attempts, CAP))
    if len(pb) + len(pc) + bud.attempts > CAP:
        print('STOP: needed > cap - used. No calls, no sampling, no silent skipping.')
    return len(pb), len(pc)


UNIT = [  # (lock, answer, expect_release)
    ('is dancing', "she's dancing in the rain", True),
    ('is dancing', 'she is dancing in the rain', True),
    ('has stamped', 'he has finally stamped the document', True),
    ('has stamped', 'he has stamped the document', True),
    ('had .. filmed', 'they had the kitchen filmed while they cooked', True),
    ('has she been tapping', 'how long has he been holding that card', True),
    ('had set off', 'had he set off earlier he would have missed the fog', True),
    ('will drop', 'if he turns the ring once more he will lower the price again', True),
    ('will drop', 'he lowered the price again', False),
    ('will drop', 'she drops the price again', False),
    ('a volcano', 'they watch the volcano from the ridge', True),
    ('is', 'the big plates are white and very clean', False),
    ('is', 'the big plate was white and very clean', False),
    ('wears', 'she is wearing the skirt in the park every sunday', False),
    ('must', 'the cup is hot so you have to hold it carefully', False),
    ('managed to', 'she succeeded in staying totally still', False),
    ('will have booked', 'by friday she will book a fifth appointment', False),
]


def selftest():
    ok = True
    correct, wrong = base.load_items()
    rc, rw = defaultdict(list), defaultdict(list)
    for it in correct:
        rc[base.route(it)[0]].append(it)
    for it in wrong:
        rw[base.route(it)[0]].append(it)
    print('(1) routing: correct L1/L2/L3 = %d/%d/%d (1e 100/48/87) | wrong = %d/%d/%d (1e 9/39/57)'
          % (len(rc['L1']), len(rc['L2']), len(rc['L3']), len(rw['L1']), len(rw['L2']), len(rw['L3'])))
    if (len(rc['L1']), len(rc['L2']), len(rc['L3'])) != (100, 48, 87) or \
       (len(rw['L1']), len(rw['L2']), len(rw['L3'])) != (9, 39, 57):
        ok = False
        print('    FAIL: routing does not reproduce 1e')
    rec = do_recount(correct)
    cats = {r['item_id']: (r['category'], r['reason']) for r in rec['items']}
    unclass = [i for i, (c, w) in cats.items() if w == 'UNCLASSIFIED']
    if unclass:
        ok = False
        print('    FAIL unclassified: %s' % unclass)

    rel = [it for it in rc['L2'] if it['step'] != 'mistake' and f1_lock_ok(it)]
    vet = [it for it in rc['L2'] if it not in rel]
    print('(2) F1 on the 48: released %d, still vetoed %d' % (len(rel), len(vet)))
    bad = [it['item_id'] for it in rel if cats[it['item_id']][0] not in RELEASABLE
           and not cats[it['item_id']][0].startswith('string_artefact')]
    bad2 = [it['item_id'] for it in vet if cats[it['item_id']][0] in RELEASABLE
            or cats[it['item_id']][0].startswith('string_artefact')]
    print('    released categories: %s' % json.dumps(dict(Counter(cats[it['item_id']][0] for it in rel))))
    print('    still vetoed: %s' % json.dumps(dict(Counter(cats[it['item_id']][0] for it in vet))))
    for it in vet:
        print('      VETOED %s [%s] %s' % (it['item_id'], cats[it['item_id']][0], cats[it['item_id']][1]))
    if bad or bad2:
        ok = False
        print('    FAIL: F1 disagrees with veto_recount categories: released-but-not-releasable %s / '
              'vetoed-but-releasable %s' % (bad, bad2))
    f2 = [it for it in vet if it['step'] != 'mistake' and f2_equivalent(it)]
    print('    F2 releases %d of the %d still vetoed: %s'
          % (len(f2), len(vet), json.dumps({it['item_id']: f2_equivalent(it)[0] for it in f2})))
    wrel = [it for it in rw['L2'] if it['step'] != 'mistake' and f1_lock_ok(it)]
    wf2 = [it for it in rw['L2'] if it['step'] != 'mistake' and not f1_lock_ok(it) and f2_equivalent(it)]
    print('    F1 on the 39 wrong vetoes: releases %d %s' % (len(wrel), json.dumps(
        dict(Counter(it['wrong_type'] or '?' for it in wrel)))))
    for it in wrel:
        print('      RELEASED %s type %s: %s' % (it['item_id'], it['wrong_type'], it['answer']))
    if any(it['wrong_type'] == 'T' for it in wrel):
        ok = False
        print('    FAIL/BUG: F1 releases a type-T (tense) wrong item — must be fixed')
    print('    F2 on the 39: releases %d' % len(wf2))

    print('(3) unit cases')
    for lock, ans, exp in UNIT:
        got = pattern_match(parse_lock(lock), ans)
        flag = 'ok ' if got == exp else 'FAIL'
        if got != exp:
            ok = False
        print('    %s lock %-20r vs %-56r -> %s (want %s)' % (flag, lock, ans, got, exp))

    print('(4) F3 / F4 offline')
    fl = {'F1': True, 'F2': True, 'F3': False, 'F4': False}
    vm = verdict_map('P-B', Bud1f())
    for f in ('F3', 'F4'):
        for label, items, n in (('cost on 235 correct', correct, 235), ('savings on 105 wrong', wrong, 105)):
            k = []
            for it in items:
                d0 = decide(it, fl, vm)
                d1 = decide(it, dict(fl, **{f: True}), vm)
                if d1['layer'] == f:
                    k.append((it, d0['accepted']))
            print('    %s %s: %d of %d (%d would otherwise be accepted, %d not)'
                  % (f, label, len(k), n, sum(1 for _i, a in k if a), sum(1 for _i, a in k if not a)))
            if f == 'F4' and 'wrong' in label:
                for it, a in k:
                    print('       type %s accepted_before=%s %s' % (it['wrong_type'], a, it['answer'][:70]))

    print('(5) plan')
    do_plan()
    print('\nSELFTEST %s' % ('PASS' if ok else 'FAIL'))
    return ok


def main():
    a = sys.argv[1:]
    act = a[0] if a else '--selftest'
    if act == '--selftest':
        sys.exit(0 if selftest() else 1)
    elif act == '--recount':
        do_recount(base.load_items()[0])
    elif act == '--plan':
        do_plan()
    elif act == '--stage':
        st = a[1]
        if st == 'calls_pb':
            stage_calls('P-B')
        elif st == 'calls_pc':
            stage_calls('P-C')
        elif st == 'tabulate':
            stage_tabulate()
        else:
            print('unknown stage %s' % st)
            sys.exit(1)
    elif act == '--all':
        stage_calls('P-B')
        stage_calls('P-C')
        stage_tabulate()
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == '__main__':
    main()

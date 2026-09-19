#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phase 1W §2.1 - AG agent reader v6: a nominative-SUBJECT reader (0 model calls, offline).

Replaces the fallback of agent_drop_v2.slovak_agent (sentence-initial token = agent, which returned
`Pod`, `Na`, `V`, `Pozri`, `Ak` ...). writer_tags.agent still wins, exactly as before.
Reader: sentences -> clauses (AG v3/v4/v5 clause splitter agent_drop_v3.split_sk, reused) -> the MAIN
clause (first clause that does not open with a subordinator/relative, is not an imperative/discourse
chunk, and carries a finite verb; a verbless NP chunk followed by a relative clause is re-attached)
-> finite-verb features (person/number, checker_1i.sk_features = the F4v2 reader, l-participle
fallback via f9) -> the nominative NP that AGREES with it anywhere in the clause:
  1. an overt nominative personal pronoun agreeing in person/number (gender where known);
  2. 1st/2nd person verb without an overt pronoun -> abstain (pro-drop);
  3. reflexive sa/si (cz se/si) in the clause -> abstain (reflexive-passive risk, as v2 did);
  4. a pre-verbal NP (prepositional phrases skipped) whose head is nominative-shaped and agrees in number;
  5. after a byť/být form only: the post-copula NP (existential "Na stole je modrá miska").
Nothing agrees -> abstain (None). Variant 'pron' = steps 1-2 only (nouns always abstain).
The Slovak modules are not edited; installed() swaps slovak_agent on a module object in memory only.
Czech path: lang='cz' with the phase1v/trackC Czech modules (cz_reader.build)."""
import os, re, sys, json, contextlib, importlib.util
sys.dont_write_bytecode = True
BASE = os.path.expanduser("~/Projects/and-again-content/translation-offline")
HERE = os.path.dirname(os.path.abspath(__file__))
for _p in (BASE, os.path.join(BASE, 'phase1u', 'taskA'), os.path.join(BASE, 'phase1t', 'taskA'),
           os.path.join(BASE, 'phase1s', 'taskC')):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import agent_drop_v3 as V3                                                   # noqa: E402  (split_sk)


def _load(name, rel):
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, os.path.join(BASE, rel))
    m = importlib.util.module_from_spec(spec); sys.modules[name] = m; spec.loader.exec_module(m); return m


_SK = {}


def sk_mods():
    if not _SK:
        _SK['f9'] = _load('f9_1n', 'phase1n/f9.py')
        _SK['CK'] = _load('checker_1i', 'phase1i/checker_1i.py')
    return _SK


S = lambda s: set(s.split())
PRON = {'sk': {'ja': ('1', 'sg', None), 'ty': ('2', 'sg', None), 'on': ('3', 'sg', 'm'), 'ona': ('3', 'sg', 'f'),
               'ono': ('3', 'sg', 'n'), 'my': ('1', 'pl', None), 'vy': ('2', 'pl', None), 'oni': ('3', 'pl', None),
               'ony': ('3', 'pl', None)},
        'cz': {'já': ('1', 'sg', None), 'ty': ('2', 'sg', None), 'on': ('3', 'sg', 'm'), 'ona': ('3', 'sg', 'f'),
               'ono': ('3', 'sg', 'n'), 'my': ('1', 'pl', None), 'vy': ('2', 'pl', None), 'oni': ('3', 'pl', None),
               'ony': ('3', 'pl', None)}}
PREP = {'sk': S("na nad pod pred za v vo do z zo s so k ku o od po pri cez medzi bez pre proti kvôli okolo vedľa "
                "počas podľa u spod sponad popri pozdĺž oproti naproti"),
        'cz': S("na nad pod před za v ve do z ze s se k ke ku o od po při přes mezi bez pro proti kvůli kolem vedle "
                "během podle u naproti skrz")}
SUB = {'sk': S("že keď keďže lebo pretože hoci kým ak aby odkedy akonáhle pokiaľ ktorý ktorá ktoré ktorí ktorého "
               "ktorej ktorému ktorým ktorú ktorých ktorými čo kto kde kam kedy ako prečo či") | set(V3.SK_CONN),
       'cz': S("že když protože jestli jestliže zda zdali aby než až který která které kteří kterého kterou kterým "
               "kterých kterými kde kam kdy jak proč co kdo pokud dokud zatímco ačkoli ačkoliv")}
IMPER = {'sk': S("pozri pozrite pozrime hádaj hádajte daj dajte poď poďte počkaj počkajte sleduj sledujte počúvaj "
                 "počúvajte pozor predstav predstavte vidíš vieš"),
         'cz': S("podívej podívejte hele koukni koukněte koukej hádej hádejte dej dejte pojď pojďte počkej počkejte "
                 "poslouchej pozor představ vidíš víš")}
STOP = {'sk': S("a ale aj i alebo no tak teda však lebo tu tam teraz dnes včera zajtra vždy často už ešte stále len "
                "iba tiež veľmi hneď potom práve asi možno nie áno ani hej kámo kamo kamoš brácho zlato wow fakt bože "
                "ach ó oh ups jaj hm hmm naozaj určite zrazu skoro neskoro dosť trochu moc celkom opäť znova zase "
                "večer ráno prosím ďakujem okej ok super jasne sem odtiaľ niekedy nikdy vôbec takmer spolu sám sama "
                "samo sami rýchlo pomaly dobre zle ticho hlasno ľahko ťažko blízko ďaleko vysoko nízko hore dole vonku "
                "vnútri doma dlho krátko presne úplne skutočne samozrejme konečne opatrne rovno potichu nahlas všade "
                "niekde nikde tu to toto tamto ma mňa mi mne ťa teba ti tebe ho jeho mu jemu ju jej ich im nás nám vás "
                "vám nich nim nimi ňom ňu ním ňou seba sebe sebou sa si nej nemu naňho naň"),
        'cz': S("a ale i nebo no tak teda však tady tam teď dnes včera zítra vždy často už ještě pořád jen taky také "
                "velmi hned pak právě asi možná ne ano ani hele fakt bože ach oh jo hm opravdu určitě najednou brzy "
                "pozdě dost trochu moc docela zase znovu večer ráno prosím díky okej ok super jasně sem odtud někdy "
                "nikdy vůbec skoro spolu sám sama samo sami rychle pomalu dobře špatně tiše nahlas lehce těžko blízko "
                "daleko vysoko nízko nahoře dole venku uvnitř doma dlouho krátce přesně úplně samozřejmě konečně "
                "opatrně rovnou všude někde nikde to toto tohle mě mně mi mnou tě tebe ti tobě tebou ho jeho mu jemu "
                "jí ji její jim jich nás nám námi vás vám vámi nich nim nimi něm ní ním se si sebe sobě sebou")}
DET = {'sk': S("ten tá tí tie tento táto títo tieto tamten tamtá tamtie každý každá každé všetci všetky môj moja "
               "moje moji tvoj tvoja tvoje náš naša naše váš vaša vaše jeho jej ich svoj svoja svoje nejaký nejaká "
               "nejaké žiadny žiadna žiadne jeden jedna jedno taký taká také celý celá celé"),
       'cz': S("ten ta ti ty tento tato tihle každý každá každé všichni všechny můj moje moji tvůj tvoje náš naše "
               "váš vaše jeho její jejich nějaký nějaká nějaké žádný žádná žádné jeden jedna jedno takový taková "
               "celý celá celé")}
PLNUM = {'sk': S("dva dve dvaja traja tri štyri štyria oba obe obaja"), 'cz': S("dva dvě tři čtyři oba obě")}
QUANT = {'sk': S("viac veľa málo niekoľko pár päť šesť sedem osem deväť desať"),
         'cz': S("víc více hodně málo několik pár pět šest sedm osm devět deset")}
BYT = {'sk': S("je sú som sme ste bol bola bolo boli budem budeš bude budeme budete budú"),
       'cz': S("je jsou jsem jsi jsme jste byl byla bylo byli byly bude budou budu budeš budeme budete není nejsou")}
MODAL = {'sk': S("môže môžu musí musia chce chcú vie vedia má majú treba smie"),
         'cz': S("může můžou mohou musí musejí chce chtějí ví vědí má mají smí")}
VEND = {'sk': ('ajú', 'ujú', 'ejú', 'ieme', 'íme', 'áme', 'eme', 'ete', 'íte', 'áte', 'iete', 'ieš', 'íš', 'áš', 'eš',
               'ujem', 'uje'),
        'cz': ('ají', 'ují', 'eme', 'íme', 'áme', 'ete', 'íte', 'áte', 'íš', 'áš', 'eš', 'uji', 'uje', 'ujou')}
OBLEND = {'sk': ('om', 'ou', 'ov', 'ami', 'ách', 'och', 'iach', 'ím', 'ým', 'ých', 'ymi', 'imi', 'ej', 'ého', 'ému',
                 'ho', 'mu', 'ovi', 'u', 'ú'),
          'cz': ('em', 'ou', 'ů', 'ům', 'ech', 'ích', 'ách', 'ami', 'emi', 'ími', 'ým', 'ých', 'ého', 'ému', 'ě', 'u',
                 'ovi', 'ím', 'ám')}
PLEND = {'sk': ('i', 'y', 'ia', 'ovia', 'atá', 'ata'), 'cz': ('i', 'y', 'ové', 'ata')}
AMBI = {'sk': ('e',), 'cz': ('e', 'a')}
ADJEND = ('ý', 'á', 'é', 'í')
AUX1 = {'sk': S("som sme"), 'cz': S("jsem jsme")}
AUX2 = {'sk': S("ste"), 'cz': S("jsi jste")}
REFLEX = {'sk': re.compile(r'(^|\s)(sa|si)(\s|$)', re.I), 'cz': re.compile(r'(^|\s)(se|si)(\s|$)', re.I)}
QUOTES = '„“”"\'‚‘’«»—–-…()*'
STOPALL = {L: STOP[L] | SUB[L] | IMPER[L] for L in ('sk', 'cz')}


def _toks(s):
    out = []
    for w in re.findall(r"[^\s.,!?;:()\"]+", s or ''):
        w = w.strip(QUOTES)
        if w:
            out.append(w)
    return out


def _lpset(text, f9):
    try:
        tt = f9.tok(text)
        return {tt[i].lower() for i in range(len(tt)) if f9._is_l_part(tt, i)}
    except Exception:
        return set()


def _norm_feats(f):
    p, n, g = f.get('person'), f.get('number'), f.get('gender')
    p = str(p)[0] if p not in (None, '') else None
    n = ('pl' if str(n).lower().startswith('p') else 'sg') if n else None
    g = str(g)[0].lower() if g and str(g)[0].lower() in 'mfn' else None
    return p, n, g


def _feats(text, CK, lps, L):
    try:
        p, n, g = _norm_feats(CK.sk_features(text)[0])
    except Exception:
        p = n = g = None
    if p is None and n is None and lps:
        low = [w.lower() for w in _toks(text)]
        lp = [w for w in low if w in lps]
        if lp:
            n = 'pl' if lp[0].endswith(('li', 'ly')) else 'sg'
            p = '1' if set(low) & AUX1[L] else '2' if set(low) & AUX2[L] else '3'
    if p is None and n is None:
        return None
    return p, n, g


_VC = {}


def _verbish(tok, low, L, CK, lps):
    if low in BYT[L] or low in MODAL[L] or low in lps or low.endswith(VEND[L]):
        return True
    if low in STOPALL[L] or low in PREP[L] or low in DET[L] or low in PRON[L]:
        return False
    k = (L, id(CK), low)
    if k not in _VC:
        try:
            p, n, _ = _norm_feats(CK.sk_features(tok)[0])
            _VC[k] = bool(p or n)
        except Exception:
            _VC[k] = False
    return _VC[k]


def _nums(low, mods, h, L):
    ml = [low[m] for m in mods]
    if any(x in QUANT[L] for x in ml):
        return {'sg'}
    if any(x in PLNUM[L] for x in ml):
        return {'pl'}
    w = low[h]
    if w.endswith(AMBI[L]):
        return {'sg', 'pl'}
    if w.endswith(PLEND[L]):
        return {'pl'}
    return {'sg'}


def _np(t, low, i, L, vidx):
    j, mods = i, []
    while (j < len(low) and len(mods) < 4 and j not in vidx and
           (low[j] in DET[L] or low[j] in QUANT[L] or low[j] in PLNUM[L] or
            (len(low[j]) > 3 and low[j].endswith(ADJEND) and j + 1 < len(low) and j + 1 not in vidx
             and low[j + 1] not in PREP[L] and low[j + 1] not in STOPALL[L]))):
        mods.append(j); j += 1
    if j >= len(low) or j in vidx:
        return None
    h = low[j]
    if (h in PREP[L] or h in STOPALL[L] or h in BYT[L] or h in PRON[L] or h in DET[L] or len(h) < 2
            or not h.replace('-', '').isalpha()):
        return None
    quant = any(low[m] in QUANT[L] for m in mods)
    if not quant and h.endswith(OBLEND[L]) and not (t[j][:1].isupper() and h.endswith('om')):
        return None
    return mods, j, _nums(low, mods, j, L)


def _skip_pp(low, j, L, vidx):
    while j < len(low) and j not in vidx and (low[j] in DET[L] or low[j] in PLNUM[L] or low[j] in QUANT[L]
                                             or (len(low[j]) > 3 and low[j].endswith(ADJEND))):
        j += 1
    if j < len(low) and j not in vidx and low[j] not in PREP[L] and low[j] not in SUB[L]:
        j += 1
    return j


def _decide_clause(t, low, f, L, variant, CK, lps):
    p, n, g = f
    for i, w in enumerate(low):
        pr = PRON[L].get(w)
        if pr and (p is None or p == pr[0]) and (n is None or n == pr[1]) and \
                not (pr[2] and g and n != 'pl' and g != pr[2]):
            return t[i], 'pronoun'
    if variant == 'pron':
        return None, 'abstain:pronoun-only variant'
    if p in ('1', '2'):
        return None, 'abstain:1st/2nd person pro-drop'
    if REFLEX[L].search(' '.join(low)):
        return None, 'abstain:reflexive clause'
    vidx = {i for i in range(len(low)) if _verbish(t[i], low[i], L, CK, lps)}
    if not vidx:
        return None, 'abstain:no finite verb token'
    vi = min(vidx)
    if low[0] in ('to', 'toto', 'tohle') and len(low) > 1 and low[1] in BYT[L]:
        return t[0], 'demonstrative+copula'
    i = 0
    while i < vi:
        if low[i] in PREP[L]:
            i = _skip_pp(low, i + 1, L, vidx); continue
        if low[i] in STOPALL[L]:
            i += 1; continue
        r = _np(t, low, i, L, vidx)
        if r:
            mods, h, nums = r
            if h < vi and (n is None or n in nums):
                return ' '.join(t[m] for m in mods + [h]), 'noun-preverbal'
            i = h + 1; continue
        i += 1
    if low[vi] in BYT[L]:
        i = vi + 1
        while i < len(low):
            if low[i] in PREP[L]:
                i = _skip_pp(low, i + 1, L, vidx); continue
            if low[i] in STOPALL[L] or i in vidx:
                i += 1; continue
            r = _np(t, low, i, L, vidx)
            if r and (n is None or n in r[2]):
                return ' '.join(t[m] for m in r[0] + [r[1]]), 'noun-postcopula'
            break
    return None, 'abstain:no agreeing nominative'


def read(sk, lang='sk', variant='full', mods=None):
    """-> (agent string or None, info).  Never raises."""
    L = lang
    try:
        mods = mods or sk_mods()
        CK, f9 = mods['CK'], mods['f9']
        for s in re.split(r'[.!?…]+', sk or ''):
            if not s.strip():
                continue
            pending, prev_sub = None, False
            for c in V3.split_sk(s):
                t = _toks(c); low = [w.lower() for w in t]
                if not t:
                    continue
                if low[0] in SUB[L]:
                    prev_sub = True; continue
                if low[0] in IMPER[L] or all(w in STOPALL[L] for w in low):
                    pending, prev_sub = None, False; continue
                lps = _lpset(c, f9)
                f = _feats(c, CK, lps, L)
                if f is None:
                    pending, prev_sub = (t, low), False; continue
                if pending and prev_sub:
                    t, low = pending[0] + t, pending[1] + low
                a, why = _decide_clause(t, low, f, L, variant, CK, lps)
                return a, {'clause': ' '.join(t), 'feats': f, 'why': why}
        return None, {'why': 'abstain:no main clause with a finite verb'}
    except Exception as e:                                            # pragma: no cover
        return None, {'why': 'abstain:crash %r' % (e,)}


def _default():
    try:
        return json.load(open(os.path.join(HERE, 's2_result.json'), encoding='utf-8'))['chosen_variant']
    except Exception:
        return 'full'


@contextlib.contextmanager
def installed(v2mod, lang='sk', variant='DEFAULT', mods=None):
    """Swap v2mod.slovak_agent (in memory) for the v6 reader; variant None = leave the 1V reader."""
    variant = _default() if variant == 'DEFAULT' else variant
    if variant is None:
        yield None
        return
    orig = v2mod.slovak_agent
    prons = set(getattr(v2mod, 'SK_PRON', ())) | set(PRON[lang])

    def slovak_agent(sk, ann, wtags):
        wtags = wtags or {}
        a, src = wtags.get('agent'), 'writer_tags.agent'
        if not a:
            a, src = read(sk, lang, variant, mods)[0], 'sk_nominative_reader_v6'
        if not a:
            return None, None, 'none'
        return a.strip(), ('pronoun' if a.strip().lower() in prons else 'noun'), src
    v2mod.slovak_agent = slovak_agent
    try:
        yield slovak_agent
    finally:
        v2mod.slovak_agent = orig

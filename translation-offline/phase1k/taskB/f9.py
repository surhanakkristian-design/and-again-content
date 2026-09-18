#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""F9 - Slovak-anchored TIME-FRAME guard.  100% OFFLINE: no model, no API, no network, no DB.

API
    sk_frame(slovak, annotation=None) -> dict   clause frames + sentence verdict
    en_frame(answer)                  -> dict   English main-clause frame
    check(slovak, annotation, answer) -> {"verdict": reject|accept|tip|abstain, "sk":…, "en":…, "reason":…}

Design principle (Phase 1j Task A): the script may assert LESS than the truth, never more.
Every uncertainty widens the Slovak frame set or abstains; a reject needs an asserted Slovak
frame AND a confidently detected English frame that is incompatible with it.
"""
import re
import sys

# --------------------------------------------------------------------------- Slovak lexicons
BUD = set("budem budeš bude budeme budete budú nebudem nebudeš nebude nebudeme nebudete nebudú".split())
COP = set("je sú som sme ste niet".split())   # NOT "si"/"nie": reflexive particle / negation
MOD = set("""musí musia musím musíš musíme musíte nemusí nemusím môže môžem môžeš môžeme môžete môžu nemôže nemôžem
chce chcem chceš chceme chcete chcú nechce vie viem vieš vieme viete vedia nevie dokáže dokážem dokážeš dokážu
smie smú má máš mám máme máte majú nemá nemám nemajú potrebuje potrebujem potrebujeme potrebujú""".split())
GO = set("idem ideš ide ideme idete idú".split())          # ide + infinitive = going-to future
CHYSTA = set("chystám chystáš chystá chystáme chystáte chystajú".split())

# common unprefixed / lexical perfectives (present form = future meaning)
PERF_LEX = set("""kúpi kúpim kúpiš kúpime kúpite kúpia dá dám dáš dáme dáte dajú vráti vrátim vrátia vrátime
povie poviem povieš povedia príde prídem prídeš prídeme prídete prídu stretne stretnem stretnú začne začnem začnú
skončí skončím skončia nájde nájdem nájdeš nájdu vezme vezmem vezmú pustí pustím pustia padne padnem padnú
sadne sadnem sadnú vstane vstanem vstanú ukáže ukážem ukážu pošle pošlem pošlú zastaví zastavím zastavia
zovrie hodí hodím hodia chytí chytím chytia pozve pozvem pozvú kývne kývnu zoberie zoberiem zoberú
dostane dostanem dostanú stane stanú otvorí otvorím otvoria zatvorí zatvoria zavrie zavriem zavrú
zníži znížim znížia zvýši zvýšia spozná spoznám spoznajú prestane prestanú""".split())

# verbs that merely LOOK prefixed / secondary imperfectives - never treat as perfective
IMPF_EXC = set("""pozerá pozerám pozeráš pozeráme pozerajú pracuje pracujem pracuješ pracujeme pracujú
používa používam používaš používajú pomáha pomáham pomáhajú znamená znamenajú záleží pozná poznám poznáš poznajú
stojí stojím stoja spieva spievam spievajú navštevuje navštevujem navštevujú potrebuje potrebujem potrebujú
počúva počúvam počúvajú počuje počujem počujú rozumie rozumiem rozumejú odpovedá odpovedajú zabúda zabúdajú
začína začínam začínajú pripravuje pripravujem pripravujú podáva podávam podávajú podávame prekáža prekážajú
zostáva zostávam zostávajú ostáva ostávam ostávajú obsahuje obsahujú opakuje opakujem opakujú vyzerá vyzerajú
nachádza nachádzajú prikladá prikladám prikladajú dopadá dopadajú prináša prinášajú odchádza odchádzajú
prichádza prichádzajú vychádza vychádzajú odpočíva odpočívajú pozoruje pozorujem pozorujú pozorujeme
nakupuje nakupujú vyhadzuje vyhadzujú ukazuje ukazujú zakladá zakladajú vydáva vydávajú rozdáva rozdávajú
odovzdáva odovzdávajú nastáva nastávajú poznáva poznávajú pokračuje pokračujú rozmýšľa rozmýšľajú
zaujíma zaujímajú pamätá pamätajú odmieta odmietajú prekladá prekladajú doháňa dopĺňa naháňa naháňajú
nahrádza nahrádzajú opúšťa opúšťajú púšťa púšťajú""".split())

# general imperfective present forms (kept small and generic)
IMPF_LEX = set("""robí robím robíš robíme robíte robia vidí vidím vidíš vidia čaká čakám čakáš čakáme čakajú
drží držím držíš držia spí spím spia sedí sedím sedia beží bežím bežia píše píšem píšu číta čítam čítajú
hovorí hovorím hovoríš hovoria vraví vravím vravia kreslí kreslím kreslia tancuje tancujem tancujú
hrá hrám hráš hráme hrajú chodí chodím chodia nosí nosím nosia berie beriem berú dáva dávam dávajú
letí letím letia svieti svietia horí horia rastie rastú padá padajú hľadá hľadám hľadajú tlačí tlačím tlačia
dvíha dvíham dvíhajú trávi trávim trávia míňa míňajú šprintuje šprintujem šprintujú trénuje trénujem trénujú
cvičí cvičím cvičia miluje milujem milujú myslí myslím myslia verí verím veria cíti cítim cítia
sleduje sledujem sledujú ide idem ideš idú stúpa stúpam stúpajú kýve kývu hýbe hýbu pohybuje pohybujú
sfukuje sfukujú vyplazuje vyplazujú spúšťa spúšťajú kváka kvákajú balí balím balia nesie nesiem nesú
žije žijem žijú býva bývam bývajú učí učím učia varí varím varia píska pískajú smeje smejú plače plačú
rozohrieva rozohrievajú zohrieva zohrievajú prší sneží""".split())

PREF = ('roz', 'pri', 'pre', 'nad', 'pod', 'ob', 'od', 'do', 'na', 'po', 'vy', 'za', 'vz')
IMPF_SUF = ('áva', 'ávam', 'ávaš', 'ávajú', 'ieva', 'ievam', 'ievajú', 'úva', 'úvam', 'úvajú',
            'ína', 'ínam', 'ínajú')

FUT_ANCHOR = ('zajtra', 'pozajtra', 'čoskoro', 'onedlho', 'neskôr', 'o chvíľu', 'o hodinu', 'o minútu',
              'o týždeň', 'o rok', 'budúci', 'budúcu', 'budúce', 'budúcom', 'budúceho', 'najbližšie')
DO_TIME = set("""piatku soboty nedele pondelka utorka stredy štvrtka zatvárania konca rána večera obeda polnoci
desiatej jedenástej dvanástej ôsmej siedmej šiestej piatej štvrtej tretej druhej leta zimy jari jesene
septembra októbra novembra decembra januára februára marca apríla mája júna júla augusta""".split())

SUB_MARK = set("""ak keď keby kým až že prečo kedy či ktorý ktorá ktoré ktorú ktorom ktorého ktorej ktorým ktorými
aby lebo pretože kiež kiežby hoci napriek odkedy akonáhle pokiaľ zatiaľ keďže akoby
kam kade kde odkiaľ kadiaľ ktorí ktorých koho komu čím akým""".split())
SUB_START2 = (('len', 'čo'), ('hneď', 'ako'), ('skôr', 'než'), ('skôr', 'ako'), ('ako', 'dlho'), ('v', 'momente'))
REPORT_V = set("""povedal povedala povedali spýtal spýtala spýtali myslel myslela mysleli vedel vedela vedeli
tvrdil tvrdila oznámil oznámila napísal napísala odpovedal odpovedala sľúbil sľúbila vysvetlil vysvetlila""".split())

# nouns / adjectives / adverbs that end like an l-participle but are not verbs
L_NONVERB = set("""svetlo svetlá číslo jedlo kreslo zrkadlo sedlo maslo heslo krídlo čelo telo kolo pravidlo
divadlo mydlo sklo hrdlo dielo vlákno škola chvíľa sila vila ihla metla skala tehla guľa tabuľa tabuli chvíli
posteli ceduli soli role stôl uhol kotol popol orol posol apríl hotel motel kanál materiál obal email koktail
gél model panel tunel kábel štýl cieľ diel anjel bicykel kúpeľ ale asi iba vôbec bola boli bol bolo
jedla svetla čísla krídla kresla zrkadla tela čela kola diela pravidla mydla""".split())
# (bol/bola/bolo/boli deliberately NOT blocked: handled explicitly as past auxiliaries below)
L_NONVERB -= {'bol', 'bola', 'bolo', 'boli'}
DET = set("""ten tá to toho tej tú tom tomu tej tento táto toto tohto tejto túto jeden jedna jedno jednu jednej
môj moja moje môjho svoj svoja svoje svojho jeho jej ich náš naša naše váš vaša vaše celý celá celé celú
každý každá každé každú nejaký nejaká nejaké ďalší ďalšia ďalšie prvý druhý tretí posledný""".split())
PREPS = set("""na v vo z zo s so k ku o od do pri po pre cez medzi nad pod za bez okolo popri podľa oproti
vedľa spod spoza počas namiesto vďaka kvôli""".split())
ADJ_END = ('ý', 'á', 'é', 'í', 'ú', 'ého', 'ému', 'ým', 'ou', 'ej', 'ie', 'iu', 'om', 'ých', 'ými')
NON_VERB_I = set("""veľkí malí dobrí zlí prví druhí tretí cudzí ďalší starší mladší horší lepší najlepší
najhorší krajší tichší rýchlejší poslední bratia ľudia srdcia hostia kolegovia vajcia""".split())

WORD = re.compile(r"[a-záäčďéěíĺľňóôŕšťúýžô]+", re.I)
CLAUSE_SPLIT = re.compile(r"[,;!?…]|—|–|\s-\s|\bale\b|\btakže\b|\blebo\b|\bpreto\b|\bpretože\b|\ba\b", re.I)


def tok(s):
    return WORD.findall((s or '').lower().replace('„', ' ').replace('“', ' '))


def _is_l_part(toks, i):
    w = toks[i]
    if w in ('bol', 'bola', 'bolo', 'boli'):
        return True
    if w in L_NONVERB or w in DET:
        return False
    if not (w.endswith('l') or w.endswith('la') or w.endswith('lo') or w.endswith('li')):
        return False
    stem = w[:-2] if w[-1] in 'aoi' else w[:-1]
    if len(stem) < 2:
        return False
    prev = toks[i - 1] if i else ''
    prev2 = toks[i - 2] if i > 1 else ''
    if prev in PREPS or prev2 in PREPS:
        return False                                  # inside a prepositional phrase -> noun
    if prev in DET or (prev and any(prev.endswith(e) for e in ('ý', 'á', 'é', 'ú', 'ej', 'ého', 'ým', 'ou', 'ie'))
                       and prev not in ('by',)):
        return False                                  # an adjective/determiner before it -> noun
    return True


def _looks_present(w):
    """Is this token a finite PRESENT-form verb?  Conservative: unknown -> False (abstain)."""
    if w in BUD:
        return False
    if w in COP or w in MOD or w in GO or w in CHYSTA or w in IMPF_LEX or w in IMPF_EXC or w in PERF_LEX:
        return True
    base = w[2:] if w.startswith('ne') and len(w) > 5 else w
    if any(base.endswith(s) for s in ('uje', 'ujem', 'uješ', 'ujeme', 'ujete', 'ujú')):
        return True
    if any(s in base for s in ('áva', 'ieva', 'úva')):
        return True
    if len(base) >= 4 and (base.endswith('om') or base.endswith('ým') or base.endswith('im')
                           and not base.endswith('ním')):
        return False                       # instrumental / dative noun or adjective, not a 1sg verb
    if len(base) >= 4 and (base.endswith('m') or base.endswith('š') or base.endswith('me') or base.endswith('te')):
        return True
    if base.endswith('ajú') or base.endswith('ujú') or base.endswith('ejú') or base.endswith('jú'):
        return True
    if base.endswith('í') and len(base) >= 4 and base not in NON_VERB_I and not base.endswith('ší'):
        return True
    if base.endswith('ia') and len(base) >= 5 and base not in NON_VERB_I:
        return True
    if _prefixed(base) and (base.endswith('e') or base.endswith('á') or base.endswith('ú')) and len(base) >= 5:
        return True
    return False


def _prefixed(w):
    for p in PREF:
        if w.startswith(p) and len(w) - len(p) >= 4:
            return p
    return None


def aspect(w):
    """'perf' | 'impf' | None (unknown).  None widens the frame, it never narrows it."""
    if w in PERF_LEX:
        return 'perf'
    if w in IMPF_EXC or w in IMPF_LEX or w in COP or w in MOD or w in GO or w in CHYSTA:
        return 'impf'
    base = w[2:] if w.startswith('ne') and len(w) > 5 else w
    if base in PERF_LEX:
        return 'perf'
    if base in IMPF_EXC or base in IMPF_LEX:
        return 'impf'
    if any(base.endswith(s) or s in base for s in IMPF_SUF):
        return 'impf'
    if _prefixed(base):
        return 'perf'
    if base.endswith('uje') or base.endswith('ujú') or base.endswith('ujem') or base.endswith('uješ'):
        # unprefixed -uje verbs are imperfective; a prefixed one (spozoruje, skontroluje) is usually
        # PERFECTIVE -> aspect unknown, which widens the frame instead of asserting present
        for pp in PREF + ('s', 'z', 'o', 'u', 'vz', 'ob', 'nad'):
            if base.startswith(pp) and len(base) - len(pp) >= 4:
                return None
        return 'impf'
    if base.endswith('á') and len(base) >= 4:
        return 'impf'
    return None


def _clauses(sk):
    parts = [p.strip() for p in CLAUSE_SPLIT.split(sk or '') if p and p.strip()]
    out = []
    for p in parts:
        t = tok(p)
        if not t:
            continue
        mark = None
        if t[0] in SUB_MARK:
            mark = t[0]
        elif len(t) > 1 and (t[0], t[1]) in SUB_START2:
            mark = t[0] + ' ' + t[1]
        out.append({'text': p, 'toks': t, 'marker': mark, 'is_sub': mark is not None})
    return out


def _anchor(toks):
    s = ' '.join(toks)
    for a in FUT_ANCHOR:
        if a in s:
            return a
    for i, w in enumerate(toks):
        if w == 'do' and i + 1 < len(toks) and toks[i + 1] in DO_TIME:
            return 'do ' + toks[i + 1]
    return None


def _clause_frame(cl, reported=False):
    t = cl['toks']
    fr, why, asp = None, '', None
    if 'by' in t or 'keby' in t or 'kiežby' in t or (t[0] == 'kiež' and 'by' in t):
        fr, why = {'conditional'}, 'conditional particle "by"'
    else:
        bud = [w for w in t if w in BUD]
        lpart = [i for i in range(len(t)) if _is_l_part(t, i)]
        cand = []
        for i2, w2 in enumerate(t):
            if i2 and t[i2 - 1] in PREPS:
                continue                      # a finite verb never follows a preposition
            if _looks_present(w2):
                cand.append(w2)
        strong = [w2 for w2 in cand if w2 in COP or w2 in MOD or w2 in GO or w2 in CHYSTA or w2 in IMPF_LEX
                  or w2 in IMPF_EXC or w2 in PERF_LEX or w2.endswith('uje') or w2.endswith('ujú')
                  or w2.endswith('ajú')]
        pres = ([strong[0]] + cand) if strong else cand
        if bud:
            fr, why = {'future'}, 'future auxiliary "%s"' % bud[0]
        elif lpart:
            fr, why = {'past'}, 'l-participle "%s"' % t[lpart[0]]
        elif pres:
            v = pres[0]
            asp = aspect(v)
            anc = _anchor(t)
            if v in GO or v in CHYSTA:
                if any(w.endswith('ť') for w in t):
                    fr, why = {'future', 'present'}, '"%s" + infinitive (going-to)' % v
                else:
                    fr, why = {'present'}, 'present verb "%s"' % v
            elif asp == 'perf':
                if anc:
                    fr, why = {'future'}, 'perfective present "%s" + future anchor "%s"' % (v, anc)
                else:
                    fr, why = {'future', 'present'}, 'perfective present "%s", no future anchor' % v
            elif asp == 'impf':
                fr = {'present', 'future'} if anc else {'present'}
                why = 'imperfective present "%s"%s' % (v, ' + anchor "%s"' % anc if anc else '')
            else:
                fr, why = {'future', 'present'}, 'present-form verb "%s", aspect unknown' % v
    cl['frame'] = fr
    cl['aspect'] = asp
    cl['reason'] = why
    return cl


def sk_frame(slovak, annotation=None):
    cls = _clauses(slovak)
    toks_all = tok(slovak)
    reported = any(w in REPORT_V for w in toks_all) and any(w in ('že', 'prečo', 'kedy', 'či', 'ako') for w in toks_all)
    for c in cls:
        _clause_frame(c, reported)
    main = None
    for c in cls:
        if not c['is_sub'] and c['frame']:
            main = c
            break
    if main is None:                       # everything subordinate (wish/if-only sentences)
        for c in cls:
            if c['frame']:
                main = c
                break
    frames = sorted(main['frame']) if main else []
    verdict = (frames[0] if len(frames) == 1 else (set(frames) if frames else None))
    return {'frames': frames, 'verdict': verdict, 'reported': reported,
            'main': main['text'] if main else None,
            'reason': (main['reason'] if main else 'no finite verb signal found -> abstain'),
            'clauses': [{'text': c['text'], 'marker': c['marker'], 'is_sub': c['is_sub'],
                         'frame': sorted(c['frame']) if c['frame'] else None, 'reason': c['reason']} for c in cls]}


# --------------------------------------------------------------------------- English
IRREG = {}
for _row in """be was were been|go went gone|do did done|have had had|say said said|see saw seen|take took taken
make made made|come came come|know knew known|get got got|give gave given|find found found|think thought thought
tell told told|become became become|show showed shown|leave left left|feel felt felt|put put put|bring brought brought
begin began begun|keep kept kept|hold held held|write wrote written|stand stood stood|hear heard heard|let let let
mean meant meant|set set set|meet met met|run ran run|pay paid paid|sit sat sat|speak spoke spoken|lie lay lain
lead led led|read read read|grow grew grown|lose lost lost|fall fell fallen|send sent sent|build built built
understand understood understood|draw drew drawn|break broke broken|spend spent spent|cut cut cut|rise rose risen
drive drove driven|buy bought bought|wear wore worn|choose chose chosen|seek sought sought|throw threw thrown
catch caught caught|deal dealt dealt|win won won|forget forgot forgotten|eat ate eaten|drink drank drunk
sleep slept slept|swim swam swum|ring rang rung|sing sang sung|blow blew blown|hit hit hit|hurt hurt hurt
shut shut shut|cost cost cost|teach taught taught|fight fought fought|sell sold sold|stick stuck stuck
slide slid slid|shine shone shone|freeze froze frozen|stop stopped stopped""".replace('\n', '|').split('|'):
    _p = _row.split()
    if len(_p) == 3:
        IRREG[_p[1]] = _p[0]
        IRREG.setdefault(_p[2], _p[0])
PAST_IRREG = set()
PP_IRREG = set()
for _row in """be was were been|go went gone|take took taken|see saw seen|write wrote written|break broke broken
do did done|give gave given|speak spoke spoken|show showed shown|draw drew drawn|throw threw thrown|know knew known
drive drove driven|choose chose chosen|freeze froze frozen|eat ate eaten|drink drank drunk|blow blew blown
sing sang sung|ring rang rung|swim swam swum|fall fell fallen|grow grew grown|wear wore worn|forget forgot forgotten
rise rose risen|begin began begun|become became become|come came come|run ran run|lie lay lain""".replace('\n', '|').split('|'):
    _p = _row.split()
    if len(_p) == 3:
        PAST_IRREG.add(_p[1])
        PP_IRREG.add(_p[2])
_SIMPLE = set(IRREG) - {'be'}
PAST_FORMS = set(IRREG) | PAST_IRREG
PP_ADJ = set("""tired interested excited bored closed married worried scared surprised pleased annoyed
crowded born""".split())
PP_ALL = set(IRREG) | PP_IRREG | {'read', 'put', 'cut', 'let', 'set', 'hit', 'shut', 'cost', 'hurt'}
FUNC = set("""of in on at to for with from by and or but the a an this that these those very more most too so
just not into onto over under out up down about around after before during until than as there his her their
my your our its no any some all one two three every each right now still also again back""".split())
BASE_V = set("""wake go come work play wait hold spend buy run sit stand walk talk speak look watch see know think
want need like love live stay leave keep make take give get put draw write read sing dance sleep eat drink open
close start stop finish check press push pull throw catch drop wear wash wipe pour cook bake film build repair fix
call ask tell say help show bring send meet feel smell sound seem become rise fall fly swim jump touch spot notice
train practise practice drive ride climb count pay cost mean matter happen arrive return visit use hang lie lay
laugh cry smile shout whisper breathe hurt heal grow plant water tie cut slide shine blow ring hit kick score save
lose win choose pick carry lift lower roll turn twist bend shake wave point snap clap wobble stick pass sell
believe remember forget understand explain decide agree refuse manage try wonder hope wish""".split())
SUBCONJ = set("""if when while after before once unless although though because whenever until as""".split())
REL = set("""that which who whom whose""".split())
EN_SUBJ = set("""i you he she it we they there this that these those""".split())
CONTRACT = {"won't": "will not", "can't": "can not", "n't": " not"}
ETOK = re.compile(r"[a-z_]+(?:'[a-z]+)?")
AMBIG_V = set("hit put cut let set cost hurt read shut spread split quit beat".split())
ADV_SKIP = set("already just now still also never always recently finally only ever".split())


def _en_tokens(ans):
    s = (ans or '').lower().replace('’', "'")
    s = s.replace("won't", "will not").replace("can't", "can not")
    s = re.sub(r"n't\b", " not", s)
    s = s.replace("'ll", " will").replace("'d", " would").replace("'ve", " have").replace("'re", " are")
    s = s.replace("'m", " am").replace("'s", " s_amb")
    return ETOK.findall(s) + []


def _is_pp(w):
    return w in PP_ALL or w == 'been' or (w.endswith('ed') and len(w) > 3)


def _hits(t):
    """every finite verb group found, left to right: (index, frame, perfect, reason)"""
    out = []
    for i, w in enumerate(t):
        k = i + 1
        while k < len(t) and t[k] in ADV_SKIP:      # "she's ALREADY put", "he has JUST finished"
            k += 1
        nxt = t[k] if k < len(t) else ''
        nxt2 = t[k + 1] if k + 1 < len(t) else ''
        hit = None
        if w in ('will', 'shall'):
            hit = ('future', False, 'modal "%s"' % w)
        elif w in ('would', 'could', 'might', 'should'):
            hit = ('conditional', nxt == 'have', 'modal "%s"' % w)
        elif w == 's_amb':
            hit = ('present', bool(nxt == 'been' or (_is_pp(nxt) and nxt not in PP_ADJ)), "'s")
        elif w in ('am', 'is', 'are'):
            hit = (('future', False, '"going to"') if (nxt == 'going' and nxt2 == 'to')
                   else ('present', False, 'present be "%s"' % w))
        elif w in ('was', 'were'):
            hit = (('past', False, '"was going to"') if (nxt == 'going' and nxt2 == 'to')
                   else ('past', False, 'past be "%s"' % w))
        elif w in ('has', 'have') and (nxt == 'been' or _is_pp(nxt) or (nxt == 'not' and _is_pp(nxt2))):
            hit = ('present', True, 'present perfect')
        elif w == 'had' and (nxt == 'been' or _is_pp(nxt) or (nxt == 'not' and _is_pp(nxt2))):
            hit = ('past', True, 'past perfect')
        elif w in ('do', 'does'):
            hit = ('present', False, 'auxiliary "%s"' % w)
        elif w == 'did':
            hit = ('past', False, 'auxiliary "did"')
        elif w in ('can', 'must', 'may'):
            hit = ('present', False, 'present modal "%s"' % w)
        elif w == 'used' and nxt == 'to':
            hit = ('past', False, '"used to"')
        elif w in PAST_FORMS and w not in ('be', 'read', 'put', 'cut', 'let', 'set', 'hit', 'shut', 'cost', 'hurt'):
            hit = ('past', False, 'irregular past "%s"' % w)
        elif (w.endswith('ed') and len(w) > 3 and w not in PP_ADJ and i > 0
              and t[i - 1] not in ('a', 'an', 'the', 'very', 'so', 'is', 'are', 'was', 'were', 'been', 'being',
                                   'get', 'gets', 'got', 'be', 'more', 'most')):
            hit = ('past', False, 'regular past "%s"' % w)
        if hit:
            out.append((i,) + hit)
    return out


def _bare_present(tt):
    """subject + bare present verb ("she usually draws", "customs lets"); None when not confident."""
    for k, w in enumerate(tt):
        if w in REL or (k > 0 and w in SUBCONJ):
            tt = tt[:k]
            break
    for i, w in enumerate(tt):
        if w in FUNC or w == 's_amb':
            continue
        for j in range(i + 1, min(i + 4, len(tt))):
            v = tt[j]
            if v in FUNC:
                break
            if v in AMBIG_V:
                return {'frame': None, 'perfect': False, 'reason': 'past=present ambiguous verb -> abstain'}
            if v.endswith('s') and not v.endswith('ss') and len(v) > 3 and v[:-1] not in FUNC:
                return {'frame': 'present', 'perfect': False, 'reason': 'verb+s after the subject', 'verb': v}
            if v in BASE_V:
                return {'frame': 'present', 'perfect': False, 'reason': 'base verb after the subject', 'verb': v}
        break
    return None


def en_frame(answer):
    raw = (answer or '').strip()
    t = _en_tokens(raw)
    if not t:
        return {'frame': None, 'perfect': False, 'reason': 'empty'}
    lead_sub = t[0] in SUBCONJ
    c = raw.find(',')
    if lead_sub and c > 0:
        t2 = _en_tokens(raw[c + 1:])
        if t2:
            t, lead_sub = t2, False
    hits = _hits(t)
    if not hits:
        return _bare_present(t) or {'frame': None, 'perfect': False,
                                    'reason': 'no finite verb found with confidence -> abstain'}
    # a relative pronoun / mid-sentence conjunction swallows the next finite verb group
    skip = set()
    for i, w in enumerate(t):
        if i > 0 and (w in REL or w in SUBCONJ):
            for h in hits:
                if h[0] > i and h[0] not in skip:
                    skip.add(h[0])
                    break
    main = [h for h in hits if h[0] not in skip] or hits
    if len(main) >= 2 and main[0][1] == 'past' and not any(w in REL for w in t[:main[0][0]]):
        pre = t[:main[0][0]]
        if sum(1 for w in pre if w in ('the', 'a', 'an', 'this', 'that', 'these', 'those', 'my', 'his', 'her',
                                       'their', 'our', 'your')) >= 2:
            main = main[1:]        # reduced relative clause: "The ball the dog fetched is ..."
    if lead_sub and len(main) >= 2:
        main = main[1:]            # "When she arrives he will call" (no comma)
    i, fr, pf, why = main[0]
    bp = _bare_present(t[:i])
    if bp:
        return bp
    return {'frame': fr, 'perfect': pf, 'reason': why, 'verb': t[i]}


# --------------------------------------------------------------------------- verdict
REPORTED_STRICT = False       # True => backshift violations are rejected, not tipped
WISH_SK = set('prial priala želal želala chcel chcela kiež kiežby'.split())


def _ann(annotation):
    if isinstance(annotation, dict):
        return annotation.get('hygienised') or annotation.get('raw') or annotation
    return {}


def check(slovak, annotation, answer):
    sk = sk_frame(slovak, annotation)
    en = en_frame(answer)
    a = _ann(annotation)
    lk = [x for x in (a.get('lk') or []) if isinstance(x, str) and x.strip()]
    low = (answer or '').lower()
    tip_struct = None
    if lk and not any(x.lower() in low for x in lk):
        tip_struct = 'practised structure not used (expected: %s)' % ' / '.join(sorted(set(lk))[:3])
    allowed = set(sk['frames'])
    ef, perf = en['frame'], en['perfect']

    def out(v, why):
        return {'verdict': v, 'sk': sk, 'en': en, 'reason': why,
                'sk_frames': sorted(allowed), 'en_ frame': ef}

    if not allowed:
        return out('abstain', 'Slovak time frame not asserted: ' + sk['reason'])
    if ef is None:
        return out('abstain', 'English finite verb not identified: ' + en['reason'])
    if ef == 'present' and perf and ({'present', 'past'} & allowed):
        return out('tip' if tip_struct else 'accept', tip_struct or 'present perfect is compatible with the Slovak frame')
    if ef in allowed:
        if sk['reported'] and ef == 'past' and 'present' in allowed:
            pass
        return out('tip' if tip_struct else 'accept',
                   tip_struct or 'time frame matches the Slovak (%s)' % '/'.join(sorted(allowed)))
    # soft cases - never reject
    if ef == 'future' and 'present' in allowed:
        return out('tip', 'Slovak is present here; an English future is a time-frame shift (soft)')
    if ef == 'present' and 'future' in allowed:
        return out('tip', 'Slovak points at the future; English present with future meaning is tolerated')
    if ef == 'conditional' and ('future' in allowed or sk['reported']):
        return out('tip', 'would/future-in-the-past tolerated')
    if ef == 'conditional' and 'past' in allowed:
        return out('tip', 'conditional vs Slovak past - not asserted')
    if 'conditional' in allowed and ef == 'past':
        return out('abstain', 'Slovak conditional; an English past may belong to the if-clause')
    # hard incompatibilities
    sk_toks = tok(slovak)
    if 'vraj' in sk_toks and (en.get('verb') in ('say', 'says', 'said', 'tell', 'tells', 'told', 'hear', 'heard')):
        return out('abstain', 'Slovak evidential "vraj": the English reporting clause carries the frame')
    if 'conditional' in allowed and ef in ('present', 'future'):
        if (WISH_SK & set(sk_toks)) or 'wish' in low or ' were ' in low or 'would' in low:
            return out('tip', 'Slovak wish/conditional rendered with an English wish-clause - not asserted')
        return out('reject', 'Slovak is conditional ("by"); the answer states it as %s' % ef)
    if ef == 'past' and 'past' not in allowed:
        return out('reject', 'Slovak time frame is %s; the answer is past' % '/'.join(sorted(allowed)))
    if ef in ('present', 'future') and allowed == {'past'}:
        return out('reject', 'Slovak time frame is past; the answer is %s' % ef)
    return out('abstain', 'frames %s vs %s: not asserted' % (sorted(allowed), ef))


# --------------------------------------------------------------------------- selftest
CASES = [
    # (slovak, answer, allowed verdicts)
    ("Do piatku ona dokončí cviky.", "By Friday she will finish the exercises.", {'accept', 'tip'}),
    ("Do piatku ona dokončí cviky.", "By Friday she finishes the exercises.", {'tip', 'accept', 'abstain'}),
    ("Do piatku ona dokončí cviky.", "By Friday she finished the exercises.", {'reject'}),
    ("Po dopade je na kameňoch trochu šťavy.", "After the impact there was a bit of juice on the stones.", {'reject'}),
    ("Po dopade je na kameňoch trochu šťavy.", "After the impact there is a bit of juice on the stones.", {'accept', 'tip'}),
    ("On trénoval hodiny.", "He trained for hours.", {'accept', 'tip'}),
    ("On trénoval hodiny.", "He was training for hours.", {'accept', 'tip'}),
    ("On trénoval hodiny.", "He had been training for hours.", {'accept', 'tip'}),
    ("On trénoval hodiny.", "He trains for hours.", {'reject'}),
    ("On trénoval hodiny.", "He has trained for hours.", {'accept', 'tip'}),
    ("Ak sa on dotkne kaktusa, strávi večer vyťahovaním tŕňov.", "If he touches the cactus, he will spend the evening pulling out thorns.", {'accept', 'tip'}),
    ("Ak sa on dotkne kaktusa, strávi večer vyťahovaním tŕňov.", "If he touched the cactus, he spent the evening pulling out thorns.", {'reject'}),
    ("Keď ona príde domov, my zavoláme.", "When she arrives home, we will call.", {'accept', 'tip'}),
    ("Ona si kúpi ďalší prívesok.", "She will buy another pendant.", {'accept', 'tip'}),
    ("Ona si kúpi ďalší prívesok.", "She bought another pendant.", {'reject'}),
    ("Zajtra on zavolá lekárovi.", "Tomorrow he will call the doctor.", {'accept', 'tip'}),
    ("Zajtra on zavolá lekárovi.", "Yesterday he called the doctor.", {'reject'}),
    ("Bývam tu päť rokov.", "I have lived here for five years.", {'accept', 'tip'}),
    ("Bývala tu päť rokov.", "She has lived here for five years.", {'accept', 'tip'}),
    ("Ona práve teraz drží pohár.", "She is holding the glass right now.", {'accept', 'tip'}),
    ("Ona práve teraz drží pohár.", "She was holding the glass.", {'reject'}),
    ("Ona práve teraz drží pohár.", "She has been holding the glass.", {'accept', 'tip'}),
    ("Keby duriány nesmrdeli, colnica by ich pustila.", "If durians did not smell, customs would let them through.", {'accept', 'tip', 'abstain'}),
    ("Keby duriány nesmrdeli, colnica by ich pustila.", "Customs lets them through.", {'reject'}),
    ("Kiež by môj kocúr bol pokojný.", "I wish my cat were calm.", {'abstain', 'accept', 'tip'}),
    ("Tréner by si prial hrubšie lapy.", "The coach will want thicker mitts.", {'reject', 'tip'}),
    ("On povedal, že puk letí rýchlejšie.", "He said the puck flies faster.", {'accept', 'tip'}),
    ("On povedal, že puk letí rýchlejšie.", "He says the puck flies faster.", {'reject'}),
    ("Inžinier sa ho spýtal, kedy privezie auto.", "The engineer asked him when he would bring the car back.", {'accept', 'tip', 'abstain'}),
    ("Hovorí sa, že ona trénovala vo výške.", "It is said that she trained at altitude.", {'accept', 'tip'}),
    ("Ona opravila bicykel.", "She repaired the bike.", {'accept', 'tip'}),
    ("Ona opravila bicykel.", "She repairs the bike.", {'reject'}),
    ("Ona opravuje bicykel.", "She is repairing the bike.", {'accept', 'tip'}),
    ("Ona opravuje bicykel.", "She repaired the bike.", {'reject'}),
    ("Muž sedí na drevenej lavičke.", "The man is sitting on a wooden bench.", {'accept', 'tip'}),
    ("Muž sedí na drevenej lavičke.", "The man sat on a wooden bench.", {'reject'}),
    ("Dôkaz je na korkovej tabuli.", "The proof is on the cork board.", {'accept', 'tip'}),
    ("Dôkaz je na korkovej tabuli.", "The proof was on the cork board.", {'reject'}),
    ("V auguste to už bude desať rokov.", "In August it will be ten years.", {'accept', 'tip'}),
    ("V auguste to už bude desať rokov.", "In August it was ten years.", {'reject'}),
    ("Ona ide utrieť prach.", "She is going to wipe the dust.", {'accept', 'tip'}),
    ("Ona ide utrieť prach.", "She wiped the dust.", {'reject'}),
    ("Deti sa zobudia o siedmej ráno.", "The children wake up at seven in the morning.", {'accept', 'tip'}),
    ("Deti sa zobudia o siedmej ráno.", "The children will wake up at seven in the morning.", {'accept', 'tip'}),
    ("Každú loď ty spozoruješ skôr než ktokoľvek iný.", "You spot every boat before anyone else.", {'accept', 'tip'}),
    ("Každú loď ty spozoruješ skôr než ktokoľvek iný.", "You will spot every boat before anyone else.", {'accept', 'tip'}),
    ("Každú loď ty spozoruješ skôr než ktokoľvek iný.", "You spotted every boat before anyone else.", {'reject'}),
    ("Lopta, ktorú pes priniesol, je teraz od blata.", "The ball that the dog brought is covered in mud now.", {'accept', 'tip'}),
    ("Lopta, ktorú pes priniesol, je teraz od blata.", "The ball that the dog brought was covered in mud.", {'reject'}),
    ("Na lavičke je jeden dlhý obväz.", "There is one long bandage on the bench.", {'accept', 'tip'}),
    ("Ona si naniesla už dve vrstvy laku.", "She's already put on two coats of varnish.", {'accept', 'tip'}),
    ("On dnes preveril už šesť zdrojov.", "He has already verified six sources today.", {'accept', 'tip'}),
    ("Medveď, ktorého laby boli obrovské, stál pri rieke.", "The bear, whose paws were huge, stood by the river.", {'accept', 'tip'}),
    ("On by si prial teplejšiu zimu.", "He wishes the winter were warmer.", {'accept', 'tip', 'abstain'}),
    ("Ona vraj zavrela dielňu minulý rok.", "They say she closed the workshop last year.", {'accept', 'tip', 'abstain'}),
    ("Zvyčajne on píše listy, ale dnes napísal báseň.", "He usually writes letters, but today he wrote a poem.", {'accept', 'tip'}),
    ("Auto, ktoré mechanik opravil, je teraz čisté.", "The car the mechanic repaired is now clean.", {'accept', 'tip'}),
    ("Hovorí sa, že on pracoval v bani.", "It's said he worked in a mine.", {'accept', 'tip'}),
    ("Niekto udrel do zvona.", "Someone hit the bell.", {'abstain', 'accept', 'tip'}),
    ("Ona práve drží pohár.", "She's holding the glass.", {'accept', 'tip'}),
    ("On práve napísal list.", "He's written the letter.", {'accept', 'tip'}),
    ("On práve napísal list.", "He writes the letter.", {'reject'}),
]


def selftest():
    bad = []
    for sk, en, ok in CASES:
        r = check(sk, None, en)
        if r['verdict'] not in ok:
            bad.append((sk, en, r['verdict'], sorted(ok), r['reason'], r['sk']['reason'], r['en']['reason']))
    print('F9 selftest: %d cases, %d failures' % (len(CASES), len(bad)))
    for b in bad:
        print('  FAIL %-58s | %-52s -> %-8s want %s\n        sk=%s | en=%s' % (b[0][:58], b[1][:52], b[2], b[3], b[5], b[6]))
    return 1 if bad else 0


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        sys.exit(selftest())
    for s in sys.argv[1:]:
        print(s, sk_frame(s))

#!/usr/bin/env python3
"""Deterministic pronoun/person sweep (brief 23.9.2026, Part A).  No model.  Input: work/snapshot_before.json (SELECT).

Every pronoun maps to a set of PERSON(/GENDER) classes: 1s 1p 2 3m 3f 3n 3p (a genderless 3rd singular = {3m,3f,3n}).
Two classes are COMPATIBLE when their sets intersect.
  E  = ordered English SUBJECT pronouns (I we you he she they)
  Ea = E + English object/possessive/reflexive forms (me us him her them my our your his their himself herself ...)
  N  = ordered native SUBJECT pronouns (brief lists; impersonal/ambiguous uses removed, see NATIVE)
Rule (FLAG): E and N both non-empty, the FIRST English subject E[0] and the FIRST native subject N[0] are incompatible,
  AND no native subject anywhere is compatible with E[0] (the English subject is not rendered by any native subject),
  AND N[0] is compatible with no English pronoun of any case (the native subject is not somebody the English names).
  Turkish / Hungarian: gender never counts (decision 22) -> 3m/3f/3n collapse to 3s, only person/number can differ.
Possessive rule (de, ua only; the other natives do not mark the owner's gender on the possessive): when the English
  has NO subject pronoun and its first word (after a vocative/interjection + comma) is His/Her/Their, the native's
  first possessive determiner (de sein*/ihr*, ua його/її/їхн*) is compared the same way.
R2 (all six natives): E-or-Ea non-empty and some native subject pronoun is compatible with NO English pronoun of any
  case (the native names a person the English never mentions, e.g. es "él" where the English has only she/her).
The rule prefers false negatives: a sentence with several people is flagged only when the first subject is rendered
by no native subject AND the native's first subject is nobody the English mentions."""
import json, os, re, sys, collections
H = os.path.dirname(os.path.abspath(__file__))
S3 = {'3m', '3f', '3n'}
EN_SUBJ = {'i': {'1s'}, 'we': {'1p'}, 'you': {'2'}, 'he': {'3m'}, 'she': {'3f'}, 'they': {'3p'}}
EN_OTHER = {'me': {'1s'}, 'my': {'1s'}, 'mine': {'1s'}, 'myself': {'1s'}, 'us': {'1p'}, 'our': {'1p'}, 'ours': {'1p'},
            'ourselves': {'1p'}, 'your': {'2'}, 'yours': {'2'}, 'yourself': {'2'}, 'yourselves': {'2'}, 'him': {'3m'},
            'his': {'3m'}, 'himself': {'3m'}, 'her': {'3f'}, 'hers': {'3f'}, 'herself': {'3f'}, 'them': {'3p'},
            'their': {'3p'}, 'theirs': {'3p'}, 'themselves': {'3p'}, 'it': {'3n'}, 'its': {'3n'}, 'itself': {'3n'}}
NATIVE = {
    'de': {'ich': {'1s'}, 'wir': {'1p'}, 'du': {'2'}, 'ihr': {'2', '3f', '3n'}, 'er': {'3m', '3n'}, 'sie': {'3f', '3p', '3n'}},
    'ua': {'я': {'1s'}, 'ми': {'1p'}, 'ти': {'2'}, 'ви': {'2'}, 'він': {'3m', '3n'}, 'вона': {'3f', '3n'}, 'воно': S3,
           'вони': {'3p'}},
    'es': {'yo': {'1s'}, 'nosotros': {'1p'}, 'nosotras': {'1p'}, 'tú': {'2'}, 'vos': {'2'}, 'usted': {'2'},
           'ustedes': {'2'}, 'vosotros': {'2'}, 'vosotras': {'2'}, 'él': {'3m', '3n'}, 'ella': {'3f', '3n'}, 'ellos': {'3p'},
           'ellas': {'3p'}},
    'fr': {'je': {'1s'}, "j": {'1s'}, 'nous': {'1p'}, 'tu': {'2'}, 'vous': {'2'}, 'il': {'3m', '3n'}, 'elle': {'3f', '3n'},
           'ils': {'3p'}, 'elles': {'3p'}},
    'tr': {'ben': {'1s'}, 'biz': {'1p'}, 'sen': {'2'}, 'siz': {'2'}, 'o': S3, 'onlar': {'3p'}},
    'hu': {'én': {'1s'}, 'mi': {'1p'}, 'te': {'2'}, 'ti': {'2'}, 'ön': {'2'}, 'önök': {'2'}, 'ő': S3, 'ők': {'3p'}}}
POSS = {'de': [(re.compile(r'^sein(e|er|es|em|en)?$'), {'3m', '3n'}), (re.compile(r'^ihr(e|er|es|em|en)?$'), {'3f', '3p', '2'})],
        'ua': [(re.compile(r'^його$'), {'3m', '3n'}), (re.compile(r'^її$'), {'3f'}), (re.compile(r'^їхн'), {'3p'})]}
GENDERLESS = {'tr', 'hu'}
FR_IMPERS = re.compile(r"\bil (y a|y avait|y aura|y aurait|faut|fallait|faudra|faudrait|fait|faisait|pleut|neige|"
                       r"semble|semblait|reste|restait|paraît|s'agit|suffit|suffisait|vaut|valait|est temps|était temps|"
                       r"est (?:\w+ )?(?:de|d'|que|qu')|était (?:\w+ )?(?:de|d'|que|qu')|vaut mieux|se peut|se passe|arrive)\b", re.I)
DE_DROP = re.compile(r"\b(weißt du(?: was)?|stell dir vor|schau mal|sag mal|glaub mir|hör mal|siehst du)\b", re.I)
TR_FIXED = re.compile(r"\bo (yüzden|zaman|sırada|anda|saatte|kadar|gün|an)\b", re.I)
DE_ART = {'der', 'die', 'das', 'den', 'dem', 'des', 'ein', 'eine', 'einen', 'einem', 'einer', 'eines', 'kein', 'keine'}
TR_CLAUSE = {'ama', 've', 'fakat', 'çünkü', 'ancak', 'ki'}
EN_DEM = re.compile(r"\b(that|those)\b", re.I)
FR_IMPERS2 = re.compile(r"\bil\s+(?:ne\s+|n['’])?(?:(?:me|te|lui|nous|vous|leur)\s+|[mt]['’])?(?:y\s+(?:a|avait|aura|aurait|eut)|reste|restait|restera|faut|fallait|faudra|faudrait)\b", re.I)
EN_IMPLICIT_I = re.compile(r"\b(not gonna lie|gonna lie|no lie|same|me too|impressed|i swear|swear|trust me|hopefully|dunno|relatable|got you|gonna need)\b", re.I)
FR_DROP = re.compile(r"(rendez-vous|s'il vous plaît|s’il vous plaît|s'il te plaît|s’il te plaît|-t-il|-il\b(?=\s*[?,]))", re.I)
WORD = re.compile(r"[\w’']+", re.U)


def en_tokens(s):
    out = []
    for w in WORD.findall(s):
        w = w.replace('’', "'").strip("'")
        if w:
            out.append(w.split("'")[0] if "'" in w else w)
    return out


def norm(c, lang):
    return {'3s' if x in S3 else x for x in c} if lang in GENDERLESS else c


def english(s):
    toks = en_tokens(s)
    E, Ea = [], []
    for i, t in enumerate(toks):
        lo = t.lower()
        if lo == 'i' and t != 'I':
            continue
        if lo in EN_SUBJ:
            E.append((t, EN_SUBJ[lo])); Ea.append((t, EN_SUBJ[lo]))
        elif lo in EN_OTHER:
            Ea.append((t, EN_OTHER[lo]))
    if EN_IMPLICIT_I.search(s):
        Ea.append(('(implicit I)', {'1s'}))   # "Not gonna lie", "Honestly, same", "Impressed already" = the speaker
    return E, Ea


def native(s, lang, en_dem=False):
    txt = s
    if lang == 'fr':
        txt = FR_IMPERS.sub(' ', FR_IMPERS2.sub(' ', FR_DROP.sub(' ', txt)))
    if lang == 'de':
        txt = DE_DROP.sub(' ', txt)
    if lang == 'tr':
        txt = TR_FIXED.sub(' ', txt)
    toks = WORD.findall(txt)
    # clause starts (tr "o"): token index 0, or preceded by , ; : — - quote, or a coordinating conjunction
    starts = {0}
    pos = [m.start() for m in WORD.finditer(txt)]
    for i in range(1, len(toks)):
        between = txt[pos[i - 1] + len(toks[i - 1]):pos[i]]
        if re.search(r'[,;:—–\-.!?“”"«»]', between) or toks[i - 1].lower() in TR_CLAUSE:
            starts.add(i)
    q = s.strip().endswith('?')
    N = []
    for i, t in enumerate(toks):
        raw = t.replace('’', "'")
        lo = raw.lower()
        if lang == 'fr' and "'" in lo:
            a, b = lo.split("'", 1)
            lo = b if b in ('il', 'ils', 'elle', 'elles') else a      # s'il / qu'elle -> il / elle; j'ai -> j
        if lang == 'hu' and lo == 'mi' and re.match(r'[^.!]*\?', txt[pos[i]:]):
            continue                          # "Mi …?" = what
        if lang == 'tr' and lo == 'o' and (i not in starts or en_dem):
            continue                          # "o" = that (demonstrative) unless clause-initial and no English that/those
        c = NATIVE[lang].get(lo)
        if c is None:
            continue
        nxt = toks[i + 1:i + 3]
        if lang == 'de' and lo == 'ihr' and nxt and (nxt[0][:1].isupper() or (nxt[0].lower() not in DE_ART and len(nxt) > 1 and nxt[1][:1].isupper())):
            continue                          # possessive determiner "ihr(e) + Noun", not a subject
        if lang == 'de' and raw == 'Sie':
            c = {'3f', '3p', '3n', '2'}       # capitalised: formal you, or she/they after . ! : 
        N.append((raw, c))
    return N


def compat(a, b, lang):
    return bool(norm(a, lang) & norm(b, lang))


LEAD = re.compile(r'^\s*(?:[\w’\']+(?:\s+[\w’\']+)?\s*[,!]\s*)?', re.U)


def poss_first(s, lang=None):
    s2 = LEAD.sub('', s, count=1) if re.match(r'^\s*[\w’\']+(\s+[\w’\']+)?\s*[,!]', s) else s
    toks = WORD.findall(s2)
    if not toks:
        return None
    if lang is None:
        lo = toks[0].lower()
        return (toks[0], EN_OTHER[lo]) if lo in ('his', 'her', 'their') else None
    for t in WORD.findall(s):
        for rx, c in POSS[lang]:
            if rx.match(t.lower()):
                return (t, c)
    return None


def decide(en, nat, lang):
    E, Ea = english(en)
    N = native(nat, lang, bool(EN_DEM.search(en)))
    if E and N:
        e0, n0 = E[0], N[0]
        if (not compat(e0[1], n0[1], lang) and not any(compat(e0[1], n[1], lang) for n in N)
                and not any(compat(n0[1], a[1], lang) for a in Ea)):
            return {'rule': 'subject', 'en_subj': e0[0], 'native_subj': n0[0], 'E': [x[0] for x in E], 'N': [x[0] for x in N]}
    if not E and lang in POSS:
        ep = poss_first(en)
        if ep:
            np_ = poss_first(nat, lang)
            if np_ and not compat(ep[1], np_[1], lang) and not any(compat(np_[1], a[1], lang) for a in Ea):
                return {'rule': 'possessive', 'en_subj': ep[0], 'native_subj': np_[0], 'E': [ep[0]], 'N': [np_[0]]}
    return None


def decide_wide(en, nat, lang):
    """Diagnostic only: ANY native subject that is compatible with no English pronoun of any case."""
    E, Ea = english(en)
    N = native(nat, lang, bool(EN_DEM.search(en)))
    if Ea and N:
        bad = [n for n in N if not any(compat(n[1], a[1], lang) for a in Ea)]
        if bad:
            return {'rule': 'wide', 'native_subj': bad[0][0], 'E': [x[0] for x in Ea], 'N': [x[0] for x in N]}
    return None


def main(name='before'):
    rows = json.load(open(f'{H}/work/snapshot_{name}.json'))
    by = collections.defaultdict(dict)
    for r in rows:
        by[r['exercise_id']][r['language_code']] = r
    flags, wide, cnt = [], [], collections.Counter()
    for eid in sorted(by):
        en = (by[eid]['en']['full_sentence'] or '').strip()
        for lang in ('de', 'ua', 'es', 'fr', 'tr', 'hu'):
            r = by[eid].get(lang)
            nat = (r or {}).get('full_sentence') or ''
            if not en or not nat.strip():
                cnt[lang + '_empty'] += 1; continue
            w = decide_wide(en, nat, lang)
            d = decide(en, nat, lang)
            if w:
                cnt[lang + '_R2'] += 1
                wide.append(dict(w, exercise_id=eid, lang=lang, en=en, native=nat))
            if d:
                cnt[lang + '_R1'] += 1
            d = d or w
            if d:
                cnt[lang] += 1
                flags.append(dict(d, exercise_id=eid, lang=lang, id=r['id'], level=r['level'], en=en, native=nat))
    json.dump(flags, open(f'{H}/work/flags_{name}.json', 'w'), ensure_ascii=False, indent=1)
    json.dump(wide, open(f'{H}/work/wide_{name}.json', 'w'), ensure_ascii=False, indent=1)
    print(json.dumps({k: cnt[k] for k in sorted(cnt)}), 'total', len(flags))
    return flags


if __name__ == '__main__':
    main(*(sys.argv[1:2] or ['before']))

#!/usr/bin/env python3
"""Phase 2J S4 / B1 - deterministic reference audit, 0 model calls.
For every stored reference (every `v` entry) of phase2i/upload annotations_{sk,cz}_fixed.jsonl: the English subject
pronoun of the aligned sentence vs the source person/number/gender from phase1w/reader_nom.read with the A2 fix
(f4fix.build_fixed, incl. the S2 verb-head rule) swapped into the reader's sk_features; Czech via cz_reader.build() +
f4fix.build_fixed(CK, 'cz').   python3 -B /abs/phase2j/partB/b1_audit.py"""
import collections, json, os, re, sys, types
sys.dont_write_bytecode = True
OUT = os.path.dirname(os.path.abspath(__file__)); P2J = os.path.dirname(OUT); TOFF = os.path.dirname(P2J)
for p in (P2J, TOFF + '/phase1w', TOFF + '/phase1v/trackC'):
    sys.path.insert(0, p)
import f4fix                      # noqa: E402
import reader_nom as RN           # noqa: E402
import cz_reader as CZ            # noqa: E402

def fixed_mods(C, f9, lang):
    fx = f4fix.build_fixed(C, lang)
    m = types.ModuleType('ck_b1_' + lang); m.__dict__.update(C.__dict__); m.sk_features = fx['sk_features']
    return {'CK': m, 'f9': f9}
SKM = RN.sk_mods(); CZB = CZ.build()
MODS = {'sk': fixed_mods(SKM['CK'], SKM['f9'], 'sk'), 'cz': fixed_mods(CZB['CK'], CZB['f9'], 'cz')}
VARIANT = RN._default()
SUBJ = {'i': ('1', 'sg', None), 'you': ('2', None, None), 'he': ('3', 'sg', 'm'), 'she': ('3', 'sg', 'f'),
        'it': ('3', 'sg', 'n'), 'we': ('1', 'pl', None), 'they': ('3', 'pl', None)}
LEAD = set("and but so then now well oh ah yes yeah no okay ok honestly maybe still look hey wow seriously actually sure "
           "also today yesterday tomorrow tonight suddenly finally besides anyway please luckily unfortunately".split())
SUBORD = set("when if because that while although though since after before until unless once as whether".split())
SPLIT = r'[.!?…]+'

def en_subject(sent):
    """First subject pronoun in main-clause position: preceded only by LEAD words / punctuation, or right after punctuation.
    A sentence opening with a subordinator is read from its first comma on. Pronouns inside quotes are ignored."""
    s = re.sub(r'[“"][^”"]*[”"]', ' ', sent.replace('’', "'"))
    toks = re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?|[,;:—–]", s)
    if toks and toks[0].lower() in SUBORD:
        toks = toks[toks.index(',') + 1:] if ',' in toks else []
    only_lead, prev = True, None
    for t in toks:
        if not t[0].isalpha():
            prev = t; continue
        w = t.lower().split("'")[0]
        if w in SUBJ and (only_lead or (prev is not None and not prev[0].isalpha())):
            return w
        if w not in LEAD:
            only_lead = False
        prev = t
    return None

def sent_index(src, clause):
    first = (clause or '').split()[:1]
    for k, s in enumerate(x for x in re.split(SPLIT, src) if x.strip()):
        if first and first[0] in RN._toks(s):
            return k
    return 0

def classify(feats, pron, explicit):
    p, n, g = feats; ep, en_, eg = SUBJ[pron]
    if p and ep != p:
        return 'person'
    if n and en_ and en_ != n:
        return 'number'
    if ep == '3' and en_ == 'sg' and n != 'pl':
        if g in ('m', 'f') and eg in ('m', 'f') and g != eg:
            return 'gender_contradiction'
        if g == 'n' and eg in ('m', 'f'):
            return 'neuter_as_he_she'
        if g is None and eg in ('m', 'f') and not explicit:
            return 'gender_fixed_open'
    return None

RES = {}
for L in ('sk', 'cz'):
    rows = [json.loads(l) for l in open(TOFF + '/phase2i/upload/annotations_%s_fixed.jsonl' % L, encoding='utf-8')]
    c = collections.Counter(); flags = []; ex = collections.defaultdict(list); why = collections.Counter()
    for r in rows:
        a, info = RN.read(r['src'], L, VARIANT, MODS[L])
        f = info.get('feats')
        why[(info.get('why') or '').split(':')[0]] += 1
        if not f:
            c['rows_unread'] += 1; c['refs_unread'] += len(r['v']); continue
        c['rows_read'] += 1
        explicit = bool(a) and a.lower().split()[0] not in RN.PRON[L]
        k = sent_index(r['src'], info.get('clause'))
        nsrc = len([x for x in re.split(SPLIT, r['src']) if x.strip()])
        for i, ref in enumerate(r['v']):
            ens = [x for x in re.split(SPLIT, ref) if x.strip()]
            aligned = len(ens) == nsrc and k < len(ens)
            pron = en_subject(ens[k]) if aligned else next((q for q in map(en_subject, ens) if q), None)
            c['refs_read'] += 1
            if pron is None:
                c['refs_no_en_pronoun'] += 1; continue
            c['refs_compared'] += 1; c['refs_compared_aligned'] += aligned
            cls = classify(f, pron, explicit)
            if cls:
                c['flag_' + cls] += 1; c['flag_%s_aligned' % cls] += aligned
                d = {'exercise_id': r['exercise_id'], 'lang': L, 'level': r.get('level'), 'ref_index': i, 'class': cls,
                     'src': r['src'], 'ref': ref, 'en_pronoun': pron, 'src_feats': list(f), 'src_agent': a,
                     'explicit_subject': explicit, 'aligned': aligned, 'reader_why': info.get('why'), 'clause': info.get('clause')}
                flags.append(d)
                if len(ex[cls]) < 10:
                    ex[cls].append(d)
    with open(OUT + '/B1_flags_%s.jsonl' % L, 'w', encoding='utf-8') as fh:
        for d in flags:
            fh.write(json.dumps(d, ensure_ascii=False) + '\n')
    c['rows'] = len(rows); c['refs'] = sum(len(r['v']) for r in rows); c['flags'] = len(flags)
    c['rows_flagged'] = len({d['exercise_id'] for d in flags})
    RES[L] = {'counts': dict(sorted(c.items())), 'reader_why': dict(why.most_common()), 'examples': ex}
json.dump(RES, open(OUT + '/B1_result.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
CL = ['person', 'number', 'gender_contradiction', 'gender_fixed_open', 'neuter_as_he_she']
md = ["# Phase 2J S4 - B1 deterministic reference audit (0 model calls)", "",
      "Source features: `phase1w/reader_nom.read(src, lang, variant=%r, mods)` (reader v6; main clause = first non-subordinate clause "
      "with a finite verb) with the A2 fix on: `f4fix.build_fixed(CK, lang)['sk_features']` (PP shadow + NV list + S2 verb-head rule) "
      "swapped into the reader's CK. Czech: `phase1v/trackC/cz_reader.build()` (em/se/jestli/aspect) + `f4fix.build_fixed(CK,'cz')`." % VARIANT, "",
      "English side: every stored reference (`v`), the sentence aligned with the Slovak clause (same index when sentence counts match; "
      "otherwise the first sentence with a pronoun, `aligned=false`); the subject pronoun = first I/you/he/she/it/we/they preceded only "
      "by discourse words or right after punctuation; a leading subordinate clause is skipped to its comma; quoted speech ignored. "
      "No pronoun (noun subject, imperative, fragment) = not compared.", "",
      "## Rules (decided here)",
      "- `person`: reference pronoun person != source person.",
      "- `number`: sg/pl differ (`you` carries no number, so 2sg/2pl never flag number).",
      "- `gender_contradiction`: source 3sg m/f fixed, reference he/she of the other gender.",
      "- `gender_fixed_open`: source 3sg with gender OPEN (present/future pro-drop, no explicit subject NP) and the reference fixes he or she -> "
      "B3 adds the other-gender variant. With an explicit noun subject the gender is left to the noun (not flagged).",
      "- `neuter_as_he_she`: source 3sg neuter (dieťa/dievča/dítě/děvče...) rendered he/she - REVIEW class, often correct; B3 must not act on it blindly.",
      "- 1sg/2sg (and 1pl/2pl) past: gender is marked only by the l-participle; English I/you/we carry no gender, so a pronoun can never fix or "
      "contradict it -> NEVER flagged here. Gender fixed by other words (\"as his wife\") is B2's job.",
      "- 3sg m/f + `it`: correct for inanimate nouns, not flagged. Reader abstains -> row unread, not compared.", ""]
for L in ('sk', 'cz'):
    c = RES[L]['counts']
    md += ["## %s" % L.upper(), "", "| count | value |", "|---|---|"] + ["| %s | %s |" % (k, v) for k, v in c.items() if not k.startswith('flag_')]
    md += ["", "| class | flags | of which aligned |", "|---|---|---|"] + ["| %s | %d | %d |" % (k, c.get('flag_' + k, 0), c.get('flag_%s_aligned' % k, 0)) for k in CL]
    md += ["", "reader why (prefix): `%s`" % json.dumps(RES[L]['reader_why'], ensure_ascii=False), ""]
    for k in CL:
        md += ["### %s %s - examples (up to 10)" % (L.upper(), k), ""]
        for d in RES[L]['examples'].get(k, []):
            md.append("- %s [%s] `%s` -> `%s` (EN %s vs src %s, agent %r, aligned %s)" % (d['exercise_id'], d['level'], d['src'], d['ref'], d['en_pronoun'], '/'.join(str(x) for x in d['src_feats']), d['src_agent'], d['aligned']))
        md.append("")
open(OUT + '/B1.md', 'w', encoding='utf-8').write('\n'.join(md) + '\n')
for L in ('sk', 'cz'):
    print(L, json.dumps(RES[L]['counts']), json.dumps(RES[L]['reader_why'], ensure_ascii=False)[:300])

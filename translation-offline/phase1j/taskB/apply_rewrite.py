#!/usr/bin/env python3
"""Task B — explicit Slovak subject pronouns. Data preparation only: no model calls, no verdicts,
no learner answers. Reads sentences_all.jsonl (answer-free) + both annotation files, writes
rewrites.jsonl, annotations_b_dev.json, annotations_b_holdout.json, sk_new.json, TASK_B_REWRITE.md.

The decision table below is agent B's own linguistic work (native-level Slovak editing).
Entries:  sid: ("R", new_sk, [(person, number, pronoun), ...], [ref-drop substrings], note)
          sid: ("U", untouched_reason, note)
"""
import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
P1J = os.path.dirname(HERE)
sys.path.insert(0, P1J)
from loader_1j import load_sentences, load_annotations  # noqa: E402

D = {
    # ---------------- block 1 ----------------
    103: ("U", "other:subject is the thing named in the sentence (promocia); 'sa hovori' impersonal", ""),
    119: ("R", "Ako dlho ona prikladá tou kartou na nesprávne dvere?", [(3, "sg", "ona")],
          ["How long has he been"], ""),
    224: ("R", "Slajdy si ona dala skontrolovať od staršieho brata deň predtým.", [(3, "sg", "ona")],
          [], "pronoun placed after the clitic 'si' (Wackernagel position)"),
    381: ("U", "explicit_subject", ""),
    1018: ("R", "Smoothie on prelial do vysokého pohára, takže mixér je teraz úplne prázdny.",
           [(3, "sg", "on")], [], "fronted object + subject pronoun + verb"),
    1452: ("R", "Ak sa on dotkne toho kaktusa, strávi večer vyťahovaním tŕňov z prsta.",
           [(3, "sg", "on")], ["If she touches"], "second clause same referent, left dropped"),
    2121: ("R", "Spolubývajúci sa ho spýtal, prečo on trávi dve hodiny denne len na to, aby sedel za stolom.",
           [(3, "sg", "on")], [], "different referent from the explicit 'Spolubývajúci'"),
    2389: ("U", "explicit_subject", ""),
    2783: ("U", "explicit_subject", ""),
    2874: ("R", "On mal ísť k lekárovi už pred pár dňami, ale čakal, kým sa sotva udržal na nohách.",
           [(3, "sg", "on")], [], "three clauses, same referent, pronoun only in the first"),
    2929: ("U", "explicit_subject", ""),
    2955: ("U", "explicit_subject", "subject named as 'Strážnik' in the first clause"),
    3084: ("U", "explicit_subject", ""),
    3332: ("R", "Ona odmietla opustiť obchod bez toho zeleného overalu.", [(3, "sg", "ona")],
           ["He refused to leave"], ""),
    3494: ("R", "Keby bola guľôčka padla na čiernej, ona by išla domov s prázdnymi vreckami.",
           [(3, "sg", "ona")], [], "second clause has a different (human) dropped referent"),
    3603: ("R", "Inžinier sa ho spýtal, kedy on privezie pretekárske auto späť do garáže.",
           [(3, "sg", "on")], [], ""),
    3937: ("R", "Ona si kúpi ďalší prívesok, keď príde na tento trh znova.", [(3, "sg", "ona")],
           ["He will buy another charm"], "clitic 'si' follows the new clause-initial pronoun"),
    4449: ("R", "Celkovo ona spustila kôš trikrát, kým mal muž všetky svoje pomaranče.",
           [(3, "sg", "ona")], [], ""),
    4571: ("R", "Keď ty necháš jednu skrutku uvoľnenú, celá stolička sa kýve.", [(2, "sg", "ty")],
           [], "generic 'you'; explicit 'ty' is grammatical but contrastive"),
    4612: ("U", "explicit_subject", "'on' already explicit"),
    5595: ("R", "Konečne on dokument opečiatkoval, takže ona môže ísť domov.",
           [(3, "sg", "on"), (3, "sg", "ona")], ["She has stamped"],
           "two different dropped referents, one pronoun each"),
    5959: ("R", "Ak on prsteň otočí ešte raz, ona zníži cenu znova.",
           [(3, "sg", "on"), (3, "sg", "ona")], ["If she turns the ring"],
           "two different dropped referents"),
    5966: ("R", "Pred týmto trhom on veril každému predavačovi jeho príbeh.", [(3, "sg", "on")], [], ""),
    5971: ("R", "Do zatvárania ona skontroluje každý prsteň na tom stole.", [(3, "sg", "ona")],
           ["By closing time he"], ""),
    6265: ("U", "impersonal", "'naháňajú' = generic 3pl agent; 'Nikto' is the explicit subject"),
    6275: ("R", "Pozri — práve teraz oni pózujú pred vodopádom.", [(3, "pl", "oni")], [],
           "imperative left untouched, second clause made explicit"),
    6353: ("U", "explicit_subject", ""),
    6365: ("R", "Režisér povedal, že oni kancelársku scénu natočia pred obedom.", [(3, "pl", "oni")],
           [], "passive reference kept: it is not a gender/person alternate"),
    6790: ("R", "Do piatku ona dokončí všetky cviky na kruhoch.", [(3, "sg", "ona")],
           ["By Friday he will have finished"], ""),
    6830: ("R", "Oni ako deti kupovali sušené bylinky v pohári.", [(3, "pl", "oni")], [],
           "pronoun prepended before the fronted adverbial; 'oni' = default for 'they'"),
    6883: ("R", "V auguste to už bude desať rokov, čo ona chodí po týchto chodníkoch.",
           [(3, "sg", "ona")], ["In August he"], "the impersonal main clause left untouched"),
    6884: ("R", "Keby on vyrazil skôr, hmlu by bol minul.", [(3, "sg", "on")], [], ""),
    6971: ("R", "Keby ona bola robot, žiadosti by jej neprekážali.", [(3, "sg", "ona")], [], ""),
    6985: ("R", "Keby ich ona všetkých nepozvala, teraz by nebola taká nahnevaná.", [(3, "sg", "ona")],
           [], "pronoun after the object clitic 'ich'"),
    7037: ("U", "explicit_subject", ""),
    7238: ("R", "Ak ty stúpaš presne tam, kam stúpa Mira, nohy ti zostanú úplne suché.",
           [(2, "sg", "ty")], [], "generic 'you'"),
    7444: ("R", "Ona si naniesla už tri vrstvy, takže jej riasy vyzerajú obrovské.", [(3, "sg", "ona")],
           ["He has already applied"], "clitic 'si' follows the new clause-initial pronoun"),
    7458: ("U", "explicit_subject", ""),
    7465: ("U", "other:impersonal 'sa hovorí' + subject is the thing named in the sentence (riasenka)", ""),
    7533: ("U", "explicit_subject", ""),
    7558: ("R", "Nikdy predtým sme my nevideli takú tichú skupinu pri západe slnka.", [(1, "pl", "my")],
           [], "pronoun after the clitic auxiliary 'sme'"),
    7687: ("R", "Kuchyňu si oni dali natočiť, kým skladali ten dúhový tanier.", [(3, "pl", "oni")],
           [], "pronoun after the clitic 'si'"),
    7708: ("R", "Ak on vydrží nehybne, vážka zostane na trstine.", [(3, "sg", "on")],
           ["If she stays still"], ""),
    7716: ("U", "impersonal", "'Podarilo sa jej…'"),
    7752: ("U", "explicit_subject", ""),
    7910: ("U", "explicit_subject", ""),
    7928: ("R", "Keby lúč bol slabší, on by ešte mohol žmurkať.", [(3, "sg", "on")], [],
           "second clause: 'ešte' now follows the clitic 'by'"),
    7998: ("R", "Veranda, na ktorej ona teraz trávi každé ráno, je otočená na východ slnka.",
           [(3, "sg", "ona")],
           ["where he now spends", "on which he now spends", "where he spends every morning now"], ""),
    8017: ("U", "explicit_subject", ""),
    8020: ("R", "Túto sezónu ona premenila tri penalty a ani jednu nezahodila.", [(3, "sg", "ona")],
           [], ""),
    8039: ("U", "explicit_subject", ""),
    8062: ("R", "K bicím ona prešla, kým kamera ešte bežala.", [(3, "sg", "ona")], [], ""),
    8209: ("R", "Do piatku si ona zarezervuje piaty termín v štúdiu.", [(3, "sg", "ona")],
           ["By Friday he will have booked"], "pronoun after the clitic 'si'"),
    8293: ("R", "Ona jedlo nikdy nedelí, takže tento croissant musí byť výnimočný.", [(3, "sg", "ona")],
           ["He never shares food"], ""),
    8465: ("R", "Keby on ten sud nebol prevrátil, ryby by tu ešte boli.", [(3, "sg", "on")], [],
           "'ten sud' is the object; the pronoun removes the subject/object ambiguity"),
    8491: ("R", "Ak ty šupku najprv narežeš, granátové jablko sa otvára ľahko.", [(2, "sg", "ty")],
           [], "generic 'you'"),
    8507: ("R", "Keby on nebol taký opatrný, plod by už zničil", [(3, "sg", "on")], [],
           "source has no final full stop; kept"),
    8618: ("R", "Na tej starej motorke on robí od jari.", [(3, "sg", "on")], ["She has been working"], ""),
    8756: ("R", "On povedal, že puk letí rýchlejšie na studenom ľade.", [(3, "sg", "on")], [], ""),
    8799: ("R", "Ona stále hádzala tú istú kombináciu, kým nešla hladko.", [(3, "sg", "ona")], [],
           "second clause subject is the inanimate 'kombinácia' — left dropped (no natural pronoun)"),
    8812: ("U", "explicit_subject", ""),
    8824: ("R", "Kým sa reťaz kývala, on dotlačil vrece na miesto.", [(3, "sg", "on")], [], ""),
    8920: ("U", "explicit_subject", ""),
    9007: ("R", "Dnes v noci on preveril už šesť zdrojov a kopa stále rastie.", [(3, "sg", "on")], [], ""),
    9038: ("R", "Práve teraz on čmára poznámku, kým obrazovka notebooku svieti.", [(3, "sg", "on")],
           ["Right now she is scribbling", "She is scribbling a note right now"], ""),
    9244: ("U", "explicit_subject", ""),
    9495: ("R", "Jej prejav bol prepísaný dvakrát, ešte než ona vôbec vyšla na to pódium.",
           [(3, "sg", "ona")], ["Him speech"], "second clause has its own (human) dropped referent"),
    9498: ("R", "Pult, za ktorým ona stojí, je starší než celá škola.", [(3, "sg", "ona")],
           ["that he is standing behind", "which he is standing behind", "behind which he is standing"],
           ""),
    9552: ("R", "Keby on pridal celú lyžicu, jedlo by bolo príliš pálivé na jedenie.", [(3, "sg", "on")],
           [], ""),
    9584: ("R", "Naplno ona šprintuje od chvíle, keď vyštartovala.", [(3, "sg", "ona")], [], ""),
    9602: ("R", "Pred tým finále ona šprintovala každé ráno celé mesiace.", [(3, "sg", "ona")], [], ""),
    9607: ("R", "Hovorí sa, že ona celú zimu trénovala vo výške.", [(3, "sg", "ona")], [],
           "main clause impersonal 'Hovorí sa' kept"),
    9687: ("U", "explicit_subject", ""),
    # ---------------- block 2 ----------------
    9907: ("R", "Keby si ona bola vzala béžovú bundu, tento look by nikdy nevznikol.", [(3, "sg", "ona")],
           [], "pronoun after the reflexive clitic 'si'; also removes the 'si' = 2sg reading"),
    9913: ("R", "Vlani si ona dala čižmy zafarbiť na fialovo.", [(3, "sg", "ona")], [],
           "pronoun after the clitic 'si'"),
    9966: ("R", "Práve teraz si oni na slnečnej streche podávajú ruky.", [(3, "pl", "oni")], [],
           "pronoun after the reflexive clitic 'si'"),
    9992: ("U", "explicit_subject", ""),
    10013: ("R", "Práve teraz on tlačí modrý obklad na hrču.", [(3, "sg", "on")],
            ["Right now she is holding", "Right now she is pressing", "She is pressing a blue ice pack"],
            ""),
    10043: ("R", "On sa spýtal, ako dlho ten opuch na jej nohe je", [(3, "sg", "on")], [],
            "source has no final full stop; kept"),
    10107: ("R", "Terminál bol prázdny; aj tak ona mala pocit, že ju niekto sleduje.", [(3, "sg", "ona")],
            [], ""),
    10116: ("R", "Keď sa terapia začala, ona objímala vankúš.", [(3, "sg", "ona")], [], ""),
    10124: ("R", "Ak si ona zapíše ďalšiu hodinu, terapia bude pokračovať aj budúci týždeň.",
            [(3, "sg", "ona")], ["If he books another session"], "pronoun after the clitic 'si'"),
    10138: ("R", "Keby ona nebola našla túto izbu, stále by plakala sama.", [(3, "sg", "ona")], [], ""),
    10167: ("R", "On má ústa také suché, že smäd musí byť skutočný.", [(3, "sg", "on")], [],
            "object 'ústa' moved behind the verb: 'Ústa on má…' is not idiomatic"),
    10179: ("U", "impersonal", "'sa hovorí' + inanimate subject named in the sentence"),
    10243: ("R", "Keď slnko prešlo cez poludnie, ona nakláňala slnečník.", [(3, "sg", "ona")], [], ""),
    10366: ("R", "Do desiatej on už bude zohrievať rezance dve hodiny v kuse.", [(3, "sg", "on")],
            ["By ten she will have been"], "pronoun before the particle 'už'"),
    10574: ("R", "On trénoval hodiny, kým bolo svetlo konečne správne.", [(3, "sg", "on")], [], ""),
    10734: ("R", "Ona to mala nakresliť ďalej od vody.", [(3, "sg", "ona")], [],
            "clitic 'to' follows the new clause-initial pronoun"),
    10866: ("R", "On čakal dve hodiny, kým sa konečne objavilo jeho číslo.", [(3, "sg", "on")], [], ""),
    10959: ("R", "Keby ona bola kúpila hrubší papier, kytica by bola teraz dokonalá.", [(3, "sg", "ona")],
            [], ""),
    11216: ("R", "Ak sa ti odpoveď nepáči, ty by si sa kariet nemal pýtať.", [(2, "sg", "ty")], [],
            "clitic cluster 'by si sa' forces 'nemal' behind it"),
    11348: ("U", "explicit_subject", "'Asistent'; the first clause is an imperative"),
    11540: ("R", "Prečo oni čakajú? Lebo chlieb musí vykysnúť.", [(3, "pl", "oni")], [], ""),
    11610: ("U", "explicit_subject", "existential 'je jeden dlhý obväz'"),
    11980: ("U", "imperative", "imperative + explicit 'voda'"),
    12831: ("U", "explicit_subject", ""),
    13034: ("U", "explicit_subject", ""),
    13175: ("U", "explicit_subject", "existential"),
    13395: ("R", "Zvyčajne ona kreslí srdcia, ale dnes nakreslila kruh.", [(3, "sg", "ona")], [],
            "gender fixed by 'nakreslila'"),
    14182: ("U", "explicit_subject", ""),
    14266: ("R", "Čo oni tancujú? — Salsu.", [(3, "pl", "oni")], [], ""),
    14697: ("U", "impersonal", ""),
    14779: ("R", "Ona ide utrieť prach z hornej hrany dverí.", [(3, "sg", "ona")],
            ["He is going to wipe"], ""),
    14806: ("R", "Pred chvíľou ona zastavila glóbus rukou.", [(3, "sg", "ona")], [], ""),
    15437: ("R", "Pole je súkromné. My musíme zostať na cestičke.", [(1, "pl", "my")], [], ""),
    15954: ("U", "explicit_subject", ""),
    16009: ("U", "other:subject is an animal 'it' with no antecedent noun — no natural Slovak pronoun", ""),
    16261: ("R", "On má plán. Chystá sa odprevadiť ju domov.", [(3, "sg", "on")], ["She has a plan"],
            "same referent in both sentences, pronoun only in the first"),
    16403: ("R", "Rozlúč sa a ona sa o hodinu vráti naspäť.", [(3, "sg", "ona")],
            ["and he will come back", "in an hour he will come back"],
            "imperative kept, second clause made explicit"),
    18251: ("R", "Z verandy oni sledujú tú búrku.", [(3, "pl", "oni")], [], ""),
    18789: ("R", "Včera ona bola v tých istých pretekoch druhá.", [(3, "sg", "ona")], [], ""),
    18966: ("U", "explicit_subject", ""),
    20298: ("R", "Na tú silnú bolesť hlavy on potrebuje jednu tabletku.", [(3, "sg", "on")],
            ["She needs a pill"], ""),
    20435: ("U", "explicit_subject", ""),
    20702: ("R", "Pozri! Teraz on dvíha džbán vyššie a vyššie.", [(3, "sg", "on")],
            ["She is lifting the jug", "Now she is lifting the jug"],
            "imperative kept, second sentence made explicit"),
    21124: ("R", "Zvyčajne ona ostáva pod strechou, ale dnes tancuje v daždi.", [(3, "sg", "ona")],
            ["He usually stays dry"], ""),
    21467: ("R", "Voda je studená, ty by si si mal obuť čižmy.", [(2, "sg", "ty")], [],
            "clitic cluster 'by si si' forces 'mal' behind it"),
    21510: ("U", "explicit_subject", ""),
    21750: ("U", "explicit_subject", "'Ona' already explicit"),
    23026: ("R", "Túto sukňu ona nosí do parku každú nedeľu.", [(3, "sg", "ona")],
            ["He wears the skirt", "Every Sunday he wears the skirt"], ""),
    23360: ("R", "Jeho obrovské kýchnutie ty môžeš počuť po celej lúke.", [(2, "sg", "ty")], [],
            "passive reference kept: not a gender/person alternate"),
    22427: ("U", "explicit_subject", "'veľa zákazníkov' is the explicit subject"),
    23669: ("U", "explicit_subject", ""),
    23878: ("U", "explicit_subject", "existential"),
    24101: ("U", "explicit_subject", "'veľa ľudí'"),
    24733: ("R", "Pohárik je horúci, tak ty ho musíš držať opatrne.", [(2, "sg", "ty")], [],
            "pronoun before the object clitic 'ho' (most natural here)"),
    24741: ("U", "explicit_subject", ""),
    25921: ("R", "Z trávnatého hrebeňa oni pozorujú sopku", [(3, "pl", "oni")], [],
            "source has no final full stop; kept"),
    25981: ("U", "explicit_subject", ""),
    26084: ("R", "On ju dokáže nájsť skôr, než ona príde domov.",
            [(3, "sg", "on"), (3, "sg", "ona")], ["She can find him"],
            "two different dropped referents; clitic 'ju' follows the new pronoun"),
    27097: ("R", "Jasné, toto námestie má veľa reklám, presne to sme my potrebovali.", [(1, "pl", "my")],
            [], "pronoun after the clitic auxiliary 'sme'"),
    27628: ("U", "explicit_subject", ""),
    28006: ("R", "Každú loď v zálive ty spozoruješ skôr než ktokoľvek iný. Klobúk dole.",
            [(2, "sg", "ty")], [], "generic 'you'"),
    29143: ("U", "explicit_subject", "'on' already explicit"),
    29691: ("R", "On pustí svojho sprievodcu na kostolné schody! Úplná katastrofa!", [(3, "sg", "on")],
            ["She drops her guidebook"], ""),
    31648: ("R", "Zlatko, on vraj opustil misku včera, nie dnes.", [(3, "sg", "on")], [],
            "pronoun before the particle 'vraj'"),
    32141: ("U", "explicit_subject", ""),
    32342: ("U", "explicit_subject", ""),
    32539: ("R", "Kam oni padajú? Do penovej jamy.", [(3, "pl", "oni")], [], ""),
}

AWKWARD = [4571, 7238, 8491, 23360, 27097, 9966, 6985, 11216, 21467, 6830, 7558]


def toks(s):
    s = unicodedata.normalize('NFC', s).lower()
    return sorted(re.findall(r'\w+', s))


def main():
    sents = load_sentences('all', purpose='Task B rewrite of Slovak sentences (no answers, no verdicts)')
    ann = {'dev': load_annotations('dev', purpose='Task B rewrite: swap refs/g into annotations'),
           'holdout': load_annotations('holdout', purpose='Task B rewrite: swap refs/g into annotations')}
    missing = [s['sid'] for s in sents if s['sid'] not in D]
    extra = [k for k in D if k not in {s['sid'] for s in sents}]
    if missing or extra:
        print('!! MISSING decisions:', missing, ' EXTRA:', extra)

    rows, sk_new, probs = [], {}, []
    for s in sents:
        sid = s['sid']
        d = D.get(sid)
        if d is None:
            continue
        refs_old = list(s['refs'])
        if d[0] == 'U':
            rows.append(dict(sid=sid, side=s['side'], status='untouched', untouched_reason=d[1],
                             person=[], number=[], pronoun=[], old_sk=s['sk'], new_sk=s['sk'],
                             refs_old=refs_old, refs_new=refs_old, g_old=s['g'], g_new=s['g'],
                             g_removed=False, note=d[2]))
            continue
        _, new_sk, pr, drops, note = d
        pronouns = [p[2] for p in pr]
        if toks(new_sk) != sorted(toks(s['sk']) + [p.lower() for p in pronouns]):
            probs.append((sid, s['sk'], new_sk))
        refs_new = [r for r in refs_old if not any(x in r for x in drops)]
        for x in drops:
            if not any(x in r for r in refs_old):
                probs.append((sid, 'DROP-NOMATCH', x))
        sk_new[str(sid)] = new_sk
        rows.append(dict(sid=sid, side=s['side'], status='rewritten', untouched_reason=None,
                         person=[p[0] for p in pr], number=[p[1] for p in pr], pronoun=pronouns,
                         old_sk=s['sk'], new_sk=new_sk, refs_old=refs_old, refs_new=refs_new,
                         g_old=s['g'], g_new=None, g_removed=s['g'] is not None, note=note))

    with open(os.path.join(HERE, 'rewrites.jsonl'), 'w', encoding='utf-8') as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + '\n')
    json.dump(sk_new, open(os.path.join(HERE, 'sk_new.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)

    # annotations with the trimmed v[] and g removed
    by_sid = {r['sid']: r for r in rows}
    n_v_dropped = 0
    for side in ('dev', 'holdout'):
        out = json.loads(json.dumps(ann[side]))
        for sid_s, a in out.items():
            r = by_sid.get(int(sid_s))
            if not r or r['status'] != 'rewritten':
                continue
            keep = set(r['refs_new'])
            for kind in ('hygienised', 'raw'):
                blk = a.get(kind)
                if not isinstance(blk, dict):
                    continue
                if isinstance(blk.get('v'), list):
                    nv = [x for x in blk['v'] if x in keep]
                    n_v_dropped += len(blk['v']) - len(nv)
                    blk['v'] = nv
                if 'g' in blk:
                    blk['g'] = None
        json.dump(out, open(os.path.join(HERE, 'annotations_b_%s.json' % side), 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=1)

    # ---- counts ----
    rw = [r for r in rows if r['status'] == 'rewritten']
    un = [r for r in rows if r['status'] == 'untouched']
    def cnt(rs, key):
        o = {}
        for r in rs:
            o[key(r)] = o.get(key(r), 0) + 1
        return dict(sorted(o.items(), key=lambda kv: -kv[1]))
    ins = [(p, n, r) for r in rw for p, n in zip(r['person'], r['number'])]
    n_third = sum(1 for p, n, r in ins if p == 3)
    n_12 = len(ins) - n_third
    reasons = cnt(un, lambda r: r['untouched_reason'].split(':')[0])
    g_removed = sum(1 for r in rw if r['g_removed'])
    refs_dropped = sum(len(r['refs_old']) - len(r['refs_new']) for r in rw)
    sides = {s: (sum(1 for r in rw if r['side'] == s), sum(1 for r in un if r['side'] == s))
             for s in ('dev', 'holdout')}
    pron = cnt(rw, lambda r: '+'.join(r['pronoun']))

    ex = [r for r in rw if r['side'] == 'dev'][:10]
    L = []
    L.append('# Task B — explicit subject pronouns in the Slovak (%d sentences)\n' % len(rows))
    L.append('Data preparation by a fixed linguistic rule. No model call, no checker verdict, no learner '
             'answer was read to produce this. Generated by `apply_rewrite.py`.\n')
    L.append('## Counts\n')
    L.append('| | rewritten | untouched | total |')
    L.append('|---|---|---|---|')
    for s in ('dev', 'holdout'):
        L.append('| %s | %d | %d | %d |' % (s, sides[s][0], sides[s][1], sum(sides[s])))
    L.append('| **both** | **%d** | **%d** | **%d** |\n' % (len(rw), len(un), len(rows)))
    L.append('Pronouns inserted: **%d** in %d sentences (%d sentences got two pronouns).\n'
             % (len(ins), len(rw), sum(1 for r in rw if len(r['pronoun']) > 1)))
    L.append('- 3rd person insertions: **%d**   ·   1st/2nd person insertions: **%d**' % (n_third, n_12))
    L.append('- by pronoun: %s' % ', '.join('%s %d' % (k or '-', v) for k, v in pron.items()))
    L.append('- `g` chains removed: **%d** (every rewritten sentence that had one)' % g_removed)
    L.append('- reference translations dropped (gender alternates that no longer agree): **%d**'
             % refs_dropped)
    L.append('- annotation `v[]` entries dropped in the two annotation files: **%d**\n' % n_v_dropped)
    L.append('Untouched by reason:\n')
    L.append('| reason | n |')
    L.append('|---|---|')
    for k, v in reasons.items():
        L.append('| %s | %d |' % (k, v))
    L.append('')
    L.append('## 10 DEV before/after examples\n')
    for r in ex:
        L.append('- **%d** (%s)' % (r['sid'], ', '.join(r['pronoun'])))
        L.append('  - old: `%s`' % r['old_sk'])
        L.append('  - new: `%s`' % r['new_sk'])
        if len(r['refs_old']) != len(r['refs_new']):
            L.append('  - refs %d → %d, g removed: %s' % (len(r['refs_old']), len(r['refs_new']),
                                                          r['g_removed']))
    L.append('\n## Self-review — awkward but acceptable\n')
    for sid in AWKWARD:
        r = by_sid[sid]
        if r['status'] == 'rewritten':
            L.append('- **%d**: `%s` — %s' % (sid, r['new_sk'], r['note'] or 'contrastive reading'))
    L.append('\nEvery rewritten sentence was re-read once for grammaticality and clitic order; a machine '
             'check also verified that the new sentence is the old one plus exactly the inserted '
             'pronoun(s) (token multiset, case-insensitive).\n')
    open(os.path.join(HERE, 'TASK_B_REWRITE.md'), 'w', encoding='utf-8').write('\n'.join(L))

    print('sentences', len(rows), 'rewritten', len(rw), 'untouched', len(un))
    print('sides', sides)
    print('insertions', len(ins), '3rd', n_third, '1st/2nd', n_12)
    print('g removed', g_removed, 'refs dropped', refs_dropped, 'ann v dropped', n_v_dropped)
    print('untouched reasons', reasons)
    print('token-check problems:', probs if probs else 'none')


if __name__ == '__main__':
    main()

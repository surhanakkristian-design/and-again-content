#!/usr/bin/env python3
"""Phase 1k — the 70 NEW Slovak holdout sentences (agent P, authored by hand).

Emits, deterministically and with 0 model calls:
    fresh/sentences_fresh.jsonl   full records (1j sentence schema + annotation + gold metadata)
    fresh/annotations_fresh.json  {"<sid>": {"hygienised":…, "raw":…}}
    fresh/writer_input.jsonl      {wid, slovak, level, topic} ONLY
    HANDOFF_P.md                  counts + overlap check + how to call everything

Arm-B convention: an explicit subject pronoun wherever Slovak would drop the subject; noun subjects
stay as they are; no `g` chain anywhere (the pronoun states the gender).

Row = (level, topic, sk, [refs], [locks parallel to refs], alt, tf_gold, voice_sk, agent_nom,
       perfective_present, tense_open)
"""
import json
import os
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
K = os.path.dirname(HERE)
ROOT = os.path.dirname(K)
P1J = os.path.join(ROOT, 'phase1j')
SID0 = 140001  # max existing sid 32539 + >100000

A, IMP, PAS = 'active_agent', 'impersonal', 'passive'

ROWS = [
    # ---------------------------------------------------------------- present (frame: present)
    ('A1', 'Present Simple', 'Ona každé ráno pije zelený čaj s medom.',
     ['She drinks green tea with honey every morning.'], ['drinks'],
     {'drinks': ['has']}, 'present', A, True, False, False),
    ('A1', 'Present Continuous', 'On práve teraz umýva staré tenisky v dreze.',
     ['He is washing his old trainers in the sink right now.'], ['is washing'],
     {'trainers': ['sneakers', 'trainers'], 'sink': ['basin']}, 'present', A, True, False, False),
    ('A1', 'Present Simple', 'Moja sestra nosí okuliare iba pri čítaní.',
     ['My sister only wears glasses when she reads.',
      'My sister wears glasses only for reading.'], ['wears', 'wears'],
     {'glasses': ['spectacles']}, 'present', A, True, False, False),
    ('A2', 'Present Simple', 'My chodíme do tej pekárne každú sobotu ráno.',
     ['We go to that bakery every Saturday morning.'], ['go'],
     {}, 'present', A, False, False, False),
    ('A2', 'Present Continuous', 'Ty teraz držíš môj dáždnik a ja mrznem.',
     ['You are holding my umbrella now and I am freezing.'], ['are holding'],
     {'freezing': ['cold']}, 'present', A, True, False, False),
    ('B1', 'Present Simple', 'Ona nikdy neposiela e-maily po desiatej večer.',
     ['She never sends emails after ten in the evening.'], ['never sends'],
     {'emails': ['e-mails']}, 'present', A, True, False, False),
    ('B1', 'Present Perfect Continuous', 'Oni už dve hodiny čakajú na autobus pred knižnicou.',
     ['They have been waiting for the bus in front of the library for two hours.'],
     ['have been waiting'], {'in front of': ['outside']}, 'present', A, False, False, False),
    ('A2', 'Present Simple', 'Tento vlak zastavuje v každej malej dedine.',
     ['This train stops in every small village.'], ['stops'],
     {'village': ['hamlet']}, 'present', A, False, False, False),
    ('B1', 'Modal verbs', 'Ty musíš odovzdať ten formulár ešte dnes popoludní.',
     ['You must hand in that form this afternoon.',
      'You have to hand in that form this afternoon.'], ['must hand in', 'have to hand in'],
     {'hand in': ['submit', 'turn in'], 'form': ['sheet']}, 'present', A, True, False, False),
    ('B2', 'All Present Tenses', 'Ona vždy zabudne kľúče, keď sa ponáhľa do práce.',
     ['She always forgets her keys when she is rushing to work.'], ['always forgets'],
     {'rushing': ['hurrying']}, 'present', A, True, False, False),
    ('A1', 'Present Simple', 'Ja rád varím cestoviny pre celú rodinu.',
     ['I like cooking pasta for the whole family.',
      'I like to cook pasta for the whole family.'], ['like cooking', 'like to cook'],
     {'whole': ['entire']}, 'present', A, True, False, False),
    ('B2', 'Relative clauses', 'Sused, ktorý býva nad nami, opravuje bicykle v garáži.',
     ['The neighbour who lives above us repairs bikes in the garage.'], ['who lives'],
     {'bikes': ['bicycles'], 'repairs': ['fixes']}, 'present', A, True, False, False),
    ('A2', 'Present Continuous', 'Oni práve natierajú plot na zeleno.',
     ['They are painting the fence green right now.'], ['are painting'],
     {'fence': ['fencing']}, 'present', A, True, False, False),
    ('B2', 'Present Perfect Continuous', 'Ona pracuje na tej diplomovke už tri mesiace.',
     ['She has been working on that thesis for three months.'], ['has been working'],
     {'thesis': ['dissertation']}, 'present', A, False, False, False),
    ('A2', 'Advanced Passive Voice', 'V tejto časti nemocnice sa nefajčí ani na balkóne.',
     ['Smoking is not allowed in this part of the hospital, not even on the balcony.',
      'There is no smoking in this part of the hospital, not even on the balcony.'],
     ['is not allowed', 'is no smoking'], {}, 'present', IMP, False, False, False),
    ('B1', 'Reported speech', 'Hovorí sa, že tá kaviareň na rohu mení majiteľa.',
     ['They say that the café on the corner is changing owners.',
      'It is said that the café on the corner is changing owners.'],
     ['They say', 'It is said'], {'café': ['coffee shop', 'cafe']},
     'present', IMP, False, False, False),

    # ---------------------------------------------------------------- past imperfective (open)
    ('A2', 'Past Simple or Continuos', 'On trénoval hodiny pred tým dôležitým zápasom.',
     ['He trained for hours before that important match.',
      'He was training for hours before that important match.'], ['trained', 'was training'],
     {'match': ['game']}, 'past', A, False, False, True),
    ('B1', 'Past Simple or Continuos', 'Ona celý večer písala poznámky do modrého zošita.',
     ['She was writing notes in the blue notebook all evening.',
      'She wrote notes in the blue notebook all evening.'], ['was writing', 'wrote'],
     {'notebook': ['exercise book']}, 'past', A, True, False, True),
    ('B1', 'Past Simple or Continuos', 'Oni minulý rok predávali med na trhu pri rieke.',
     ['They sold honey at the market by the river last year.',
      'They were selling honey at the market by the river last year.'],
     ['sold', 'were selling'], {'market': ['marketplace']}, 'past', A, True, False, True),
    ('A2', 'Used to, Would', 'Ja som ako dieťa zbieral staré mince.',
     ['I used to collect old coins as a child.',
      'I collected old coins as a child.'], ['used to collect', 'collected'],
     {'coins': ['coins']}, 'past', A, True, False, True),
    ('B2', 'Used to, Would', 'Moja babka nám každú nedeľu piekla jablkový koláč.',
     ['My grandma used to bake us an apple pie every Sunday.',
      'My grandma baked us an apple pie every Sunday.'], ['used to bake', 'baked'],
     {'grandma': ['grandmother'], 'pie': ['cake']}, 'past', A, True, False, True),
    ('B1', 'Past Simple or Continuos', 'Ty si čakal na peróne, keď začalo pršať.',
     ['You were waiting on the platform when it started raining.',
      'You waited on the platform when it started raining.'], ['were waiting', 'waited'],
     {'platform': ['platform']}, 'past', A, False, False, True),
    ('A2', 'Used to, Would', 'My sme minulé leto chodili k jazeru takmer denne.',
     ['We went to the lake almost every day last summer.',
      'We used to go to the lake almost every day last summer.'], ['went', 'used to go'],
     {'almost every day': ['nearly every day']}, 'past', A, False, False, True),
    ('B1', 'Past Simple or Continuos', 'On opravoval tú kosačku celé popoludnie a nakoniec to vzdal.',
     ['He was fixing that lawnmower all afternoon and in the end he gave up.',
      'He fixed that lawnmower all afternoon and in the end he gave up.'],
     ['was fixing', 'fixed'], {'lawnmower': ['mower'], 'gave up': ['quit']},
     'past', A, True, False, True),
    ('B2', 'Past Simple or Continuos', 'Ona vtedy učila na základnej škole v malom meste.',
     ['She was teaching at a primary school in a small town at that time.',
      'She taught at a primary school in a small town at that time.'],
     ['was teaching', 'taught'], {'primary school': ['elementary school']},
     'past', A, False, False, True),
    ('A2', 'Past Simple or Continuos', 'Oni sa vlani učili po španielsky cez víkendy.',
     ['They studied Spanish at weekends last year.',
      'They were studying Spanish at weekends last year.'], ['studied', 'were studying'],
     {'at weekends': ['on weekends']}, 'past', A, False, False, True),

    # ---------------------------------------------------------------- past perfective
    ('A1', 'Past Simple', 'Ona včera stratila peňaženku v autobuse.',
     ['She lost her wallet on the bus yesterday.'], ['lost'],
     {'wallet': ['purse']}, 'past', A, True, False, False),
    ('A2', 'Past Simple', 'On rozbil pohár a hneď to upratal.',
     ['He broke a glass and cleaned it up straight away.'], ['broke'],
     {'straight away': ['right away', 'immediately']}, 'past', A, True, False, False),
    ('B1', 'Past Perfect', 'Keď sme prišli, on už zjedol celú polievku.',
     ['When we arrived, he had already eaten the whole soup.'], ['had already eaten'],
     {'whole': ['entire']}, 'past', A, True, False, False),
    ('B2', 'Past Perfect', 'Ona odišla skôr, než jej stihli poďakovať.',
     ['She left before they managed to thank her.'], ['left'],
     {'managed to': ['could', 'had a chance to']}, 'past', A, False, False, False),
    ('B2', 'Reported speech', 'Povedal nám, že ten balík odoslal už v pondelok.',
     ['He told us that he had sent the parcel on Monday.',
      'He told us he sent the parcel on Monday.'], ['had sent', 'sent'],
     {'parcel': ['package']}, 'past', A, True, False, False),
    ('B1', 'Reported speech', 'Spýtala sa ma, či ja ovládam ten program.',
     ['She asked me whether I could use that program.',
      'She asked me if I knew that program.'], ['asked', 'asked'],
     {'program': ['programme', 'software']}, 'past', A, True, False, False),
    ('B2', 'Advanced Passive Voice', 'Ten most bol postavený ešte pred vojnou.',
     ['That bridge was built before the war.'], ['was built'],
     {}, 'past', PAS, False, False, False),
    ('B1', 'Advanced Passive Voice', 'Dom na kopci bol predaný minulý mesiac.',
     ['The house on the hill was sold last month.'], ['was sold'],
     {'hill': ['hillside']}, 'past', PAS, False, False, False),
    ('B2', 'Advanced Passive Voice', 'Bolo mi povedané, že termín sa už nedá zmeniť.',
     ['I was told that the deadline cannot be changed any more.'], ['was told'],
     {'deadline': ['date']}, 'mixed', PAS, False, False, False),
    ('A2', 'Past Simple', 'Deti našli pod schodmi malú korytnačku.',
     ['The children found a small tortoise under the stairs.'], ['found'],
     {'tortoise': ['turtle'], 'stairs': ['steps', 'staircase']}, 'past', A, True, False, False),
    ('B1', 'Past Simple', 'My sme ten nábytok zložili za dve hodiny.',
     ['We put that furniture together in two hours.',
      'We assembled that furniture in two hours.'], ['put together', 'assembled'],
     {}, 'past', A, True, False, False),

    # ---------------------------------------------------------------- perfective present = future
    ('A2', 'All Future Tenses', 'Do stredy ona pripraví podklady pre nového klienta.',
     ['She will prepare the materials for the new client by Wednesday.'], ['will prepare'],
     {'materials': ['documents', 'papers']}, 'future', A, True, True, False),
    ('B1', 'All Future Tenses', 'On ti zajtra pošle nové heslo.',
     ['He will send you the new password tomorrow.'], ['will send'],
     {'password': ['passcode']}, 'future', A, True, True, False),
    ('B1', 'All Future Tenses', 'Ona to kreslo prenesie do vedľajšej izby.',
     ['She will move that armchair into the next room.'], ['will move'],
     {'armchair': ['chair'], 'move': ['carry']}, 'future', A, True, True, False),
    ('B2', 'All Future Tenses', 'My tú zmluvu podpíšeme bez akýchkoľvek zmien.',
     ['We will sign that contract without any changes.'], ['will sign'],
     {'contract': ['agreement']}, 'future', A, True, True, False),
    ('B2', 'Relative clauses', 'Ja ti kúpim tú knihu o vtákoch, ktorú si chcela.',
     ['I will buy you that book about birds you wanted.'], ['will buy'],
     {'book about birds': ['bird book']}, 'future', A, True, True, False),
    ('B1', '1. Conditional', 'Ak ona stihne ten vlak, bude doma pred obedom.',
     ['If she catches that train, she will be home before noon.'], ['catches'],
     {'noon': ['lunchtime', 'midday']}, 'future', A, True, True, False),
    ('B1', '1. Conditional', 'Keď on dopíše ten list, hneď ho odnesie na poštu.',
     ['When he finishes that letter, he will take it to the post office right away.'],
     ['finishes'], {'right away': ['straight away']}, 'future', A, True, True, False),
    ('B2', 'All Future Tenses', 'Oni ten starý plot rozoberú ešte pred zimou.',
     ['They will take that old fence apart before winter.',
      'They will dismantle that old fence before winter.'],
     ['will take apart', 'will dismantle'], {}, 'future', A, True, True, False),
    ('B2', 'All Future Tenses', 'Vy nám o tom poviete zajtra na stretnutí.',
     ['You will tell us about it at the meeting tomorrow.'], ['will tell'],
     {'meeting': ['meeting']}, 'future', A, True, True, False),
    ('B2', 'Future Perfect Simple', 'Do konca mesiaca ona prečíta všetky tie správy.',
     ['By the end of the month she will have read all those reports.'], ['will have read'],
     {'reports': ['reports']}, 'future', A, True, True, False),
    ('B1', 'All Future Tenses', 'Ten technik vymení rozbité sklo na displeji.',
     ['The technician will replace the broken glass on the display.'], ['will replace'],
     {'display': ['screen'], 'technician': ['engineer']}, 'future', A, True, True, False),
    ('A2', 'All Future Tenses', 'On ti to vysvetlí cestou domov.',
     ['He will explain it to you on the way home.'], ['will explain'],
     {}, 'future', A, True, True, False),
    ('B2', '1. Conditional', 'Ak my odložíme ten výlet, sprievodca nám vráti peniaze.',
     ['If we postpone the trip, the guide will give us our money back.'], ['postpone'],
     {'postpone': ['put off'], 'trip': ['excursion']}, 'future', A, True, True, False),

    # ---------------------------------------------------------------- bude + infinitive
    ('A2', 'All Future Tenses', 'Ona bude celý budúci týždeň pracovať z domu.',
     ['She will be working from home all next week.',
      'She is going to work from home all next week.'],
     ['will be working', 'is going to work'], {}, 'future', A, False, False, False),
    ('B1', 'All Future Tenses', 'Oni budú opravovať tú cestu až do jesene.',
     ['They will be repairing that road until the autumn.'], ['will be repairing'],
     {'autumn': ['fall'], 'road': ['street']}, 'future', A, True, False, False),
    ('A1', 'All Future Tenses', 'Ja budem variť večeru, kým ty upraceš kuchyňu.',
     ['I will cook dinner while you tidy the kitchen.'], ['will cook'],
     {'tidy': ['clean up', 'tidy up']}, 'future', A, True, False, False),
    ('B2', 'All Future Tenses', 'On bude čakať pred kinom asi o siedmej.',
     ['He will be waiting in front of the cinema at about seven.'], ['will be waiting'],
     {'cinema': ['movie theatre'], 'in front of': ['outside']}, 'future', A, False, False, False),
    ('B1', 'All Future Tenses', 'My budeme sledovať ten zápas u susedov.',
     ['We will watch that match at the neighbours.',
      'We are going to watch that match at the neighbours.'],
     ['will watch', 'are going to watch'], {'match': ['game']}, 'future', A, True, False, False),
    ('B2', 'All Future Tenses', 'Vy budete dostávať tie správy každé ráno.',
     ['You will be getting those reports every morning.',
      'You will receive those reports every morning.'], ['will be getting', 'will receive'],
     {}, 'future', A, False, False, False),

    # ---------------------------------------------------------------- conditionals
    ('B1', '2. Conditional', 'Keby ona mala viac času, naučila by sa hrať na gitare.',
     ['If she had more time, she would learn to play the guitar.'], ['would learn'],
     {}, 'conditional', A, False, False, False),
    ('B2', '3. Conditional', 'Keby sme boli odišli skôr, neboli by sme zmeškali ten let.',
     ['If we had left earlier, we would not have missed that flight.'],
     ['would not have missed'], {'flight': ['plane']}, 'conditional', A, False, False, False),
    ('B1', '2. Conditional', 'Ja by som ti požičal auto, ale je v servise.',
     ['I would lend you the car, but it is at the garage.'], ['would lend'],
     {'garage': ['repair shop', 'service']}, 'conditional', A, True, False, False),
    ('B2', '2. Conditional', 'On by ten problém vyriešil za jediné popoludnie.',
     ['He would solve that problem in a single afternoon.'], ['would solve'],
     {'single': ['one']}, 'conditional', A, True, False, False),
    ('B1', '2. Conditional', 'Oni by radi pozvali celú triedu na záhradu.',
     ['They would like to invite the whole class to the garden.'], ['would like to invite'],
     {'whole': ['entire']}, 'conditional', A, True, False, False),
    ('B2', '3. Conditional', 'Keby si ty povedal pravdu hneď, nikto by sa nehneval.',
     ['If you had told the truth right away, nobody would have been angry.'],
     ['would have been'], {'right away': ['straight away']},
     'conditional', A, True, False, False),
    ('A2', '2. Conditional', 'My by sme tam išli pešo, keby nepršalo.',
     ['We would walk there if it was not raining.',
      'We would walk there if it were not raining.'], ['would walk', 'would walk'],
     {}, 'conditional', A, False, False, False),
    ('B1', '2. Conditional', 'Ona by tú skriňu presunula bližšie k oknu.',
     ['She would move that wardrobe closer to the window.'], ['would move'],
     {'wardrobe': ['closet', 'cupboard']}, 'conditional', A, True, False, False),

    # ---------------------------------------------------------------- impersonal / passive extras
    ('B2', 'Advanced Passive Voice', 'O tom novom moste sa píše vo všetkých novinách.',
     ['That new bridge is written about in all the newspapers.',
      'They write about that new bridge in all the newspapers.'],
     ['is written about', 'write about'], {'newspapers': ['papers']},
     'present', IMP, False, False, False),
    ('B1', 'Advanced Passive Voice', 'Tie dvere budú natreté do soboty.',
     ['Those doors will be painted by Saturday.'], ['will be painted'],
     {}, 'future', PAS, False, False, False),
    ('A2', 'Advanced Passive Voice', 'V nedeľu sa tu nepredáva čerstvý chlieb.',
     ['Fresh bread is not sold here on Sundays.'], ['is not sold'],
     {'Fresh': ['New']}, 'present', IMP, False, False, False),
    ('B2', 'Reported speech', 'Oznámili nám, že letisko zatvoria kvôli hmle.',
     ['They told us that they would close the airport because of the fog.',
      'We were told that the airport would be closed because of the fog.'],
     ['would close', 'would be closed'], {'because of': ['due to']},
     'mixed', IMP, False, False, False),
    ('B1', 'Advanced Passive Voice', 'Na tej ulici sa parkuje len za poplatok.',
     ['Parking in that street is only allowed for a fee.',
      'You can only park in that street for a fee.'], ['is only allowed', 'can only park'],
     {'fee': ['charge']}, 'present', IMP, False, False, False),
    ('B2', 'Advanced Passive Voice', 'Tá socha bola odhalená pred dvoma rokmi.',
     ['That statue was unveiled two years ago.'], ['was unveiled'],
     {'unveiled': ['revealed']}, 'past', PAS, False, False, False),
]


def band_of(sk):
    n = len([w for w in re.split(r'\s+', sk.strip()) if w])
    return '1-6' if n <= 6 else '7-9' if n <= 9 else '10-12' if n <= 12 else \
        '13-16' if n <= 16 else '17+'


def nrm(s):
    s = unicodedata.normalize('NFKD', str(s))
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9 ]', '', s.lower()).strip()


def content(s):
    return {w for w in nrm(s).split() if len(w) > 3}


def main():
    recs, anns, winput = [], {}, []
    for i, (lv, topic, sk, refs, lk, alt, tf, voice, agent, perf, open_) in enumerate(ROWS):
        sid = SID0 + i
        ann = {'id': sid, 't': 9000 + i, 'lv': lv, 'v': list(refs), 'lk': list(lk),
               'alt': dict(alt)}
        anns[str(sid)] = {'hygienised': ann, 'raw': json.loads(json.dumps(ann))}
        recs.append({
            'sid': sid, 'side': 'fresh', 'level': lv, 'band': band_of(sk), 'topic': topic,
            'half': 'NEW', 'sk': sk, 'reference': refs[0], 'refs': list(refs),
            'annotation_v': list(refs), 'annotation_alt': dict(alt), 'annotation_d': None,
            'annotation_p': None, 'g': None, 'g_raw': None, 'locks': list(lk), 'n_items': None,
            'annotation': anns[str(sid)],
            'tf_gold': tf, 'voice_sk': voice, 'agent_nom': agent,
            'perfective_present': perf, 'tense_open': open_,
        })
        winput.append({'wid': sid, 'slovak': sk, 'level': lv, 'topic': topic})

    n_words = [len(r['sk'].split()) for r in recs]
    assert len(recs) == 70, len(recs)
    assert all(6 <= w <= 18 for w in n_words), [w for w in n_words if not 6 <= w <= 18]
    assert len({r['sid'] for r in recs}) == 70

    # ---- overlap check against the 140 existing sentences (original + arm-B) ------------
    old_sk, old_en, old_words = set(), set(), []
    for line in open(os.path.join(P1J, 'sentences_all.jsonl'), encoding='utf-8'):
        s = json.loads(line)
        old_sk.add(nrm(s['sk']))
        old_words.append(content(s['sk']))
        for e in [s['reference']] + list(s['refs'] or []):
            old_en.add(nrm(e))
    for line in open(os.path.join(P1J, 'taskB', 'rewrites.jsonl'), encoding='utf-8'):
        r = json.loads(line)
        old_sk.add(nrm(r['new_sk']))
        old_words.append(content(r['new_sk']))
        for e in list(r['refs_new'] or []):
            old_en.add(nrm(e))
    dup_sk = [r['sid'] for r in recs if nrm(r['sk']) in old_sk]
    dup_en = [r['sid'] for r in recs if any(nrm(e) in old_en for e in r['refs'])]
    jac = []
    for r in recs:
        c = content(r['sk'])
        best = max((len(c & o) / len(c | o)) if (c | o) else 0.0 for o in old_words)
        jac.append((best, r['sid']))
    jac.sort(reverse=True)
    overlap_ok = not dup_sk and not dup_en and jac[0][0] < 0.5

    os.makedirs(HERE, exist_ok=True)
    with open(os.path.join(HERE, 'sentences_fresh.jsonl'), 'w', encoding='utf-8') as fh:
        for r in recs:
            fh.write(json.dumps(r, ensure_ascii=False) + '\n')
    with open(os.path.join(HERE, 'writer_input.jsonl'), 'w', encoding='utf-8') as fh:
        for r in winput:
            fh.write(json.dumps(r, ensure_ascii=False) + '\n')
    json.dump(anns, open(os.path.join(HERE, 'annotations_fresh.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)

    def cnt(key):
        d = {}
        for r in recs:
            d[r[key]] = d.get(r[key], 0) + 1
        return dict(sorted(d.items(), key=lambda kv: (-kv[1], str(kv[0]))))

    lev = cnt('level')
    tf = cnt('tf_gold')
    vo = cnt('voice_sk')
    agent = sum(1 for r in recs if r['agent_nom'])
    perf = sum(1 for r in recs if r['perfective_present'])
    open_ = sum(1 for r in recs if r['tense_open'])
    bude = sum(1 for r in recs if r['tf_gold'] == 'future' and not r['perfective_present']
               and r['voice_sk'] == 'active_agent')
    past_imp = sum(1 for r in recs if r['tf_gold'] == 'past' and r['tense_open'])
    imp_pas = sum(1 for r in recs if r['voice_sk'] in ('impersonal', 'passive'))
    tgt = {'A1': 6, 'A2': 16, 'B1': 25, 'B2': 23}

    def row(name, got, target, ok):
        return '| %s | %s | %s | %s |' % (name, got, target, 'OK' if ok else 'MISS')

    tbl = [
        '| metric | got | target | |', '|---|---|---|---|',
        row('level A1/A2/B1/B2', '/'.join(str(lev.get(l, 0)) for l in ('A1', 'A2', 'B1', 'B2')),
            '6/16/25/23 (= DEV 70 of 1j)', all(lev.get(l, 0) == v for l, v in tgt.items())),
        row('tf_gold', ' · '.join('%s %d' % kv for kv in tf.items()), 'spread', True),
        row('voice_sk', ' · '.join('%s %d' % kv for kv in vo.items()),
            'impersonal+passive >= 10', imp_pas >= 10),
        row('agent_nom (nom. agent + transitive)', agent, '>= 42', agent >= 42),
        row('perfective_present futures', perf, '>= 12', perf >= 12),
        row('bude + infinitive futures', bude, '>= 6', bude >= 6),
        row('conditionals (by)', tf.get('conditional', 0), '>= 8',
            tf.get('conditional', 0) >= 8),
        row('plain present', tf.get('present', 0), '>= 15', tf.get('present', 0) >= 15),
        row('past total', tf.get('past', 0), '>= 20', tf.get('past', 0) >= 20),
        row('past imperfective (tense_open)', past_imp, '>= 10', past_imp >= 10),
        row('Slovak length 6-18 words', '%d-%d' % (min(n_words), max(n_words)), '6-18', True),
        row('overlap with the existing 140', 'sk dup %d, en dup %d, max content Jaccard %.2f'
            % (len(dup_sk), len(dup_en), jac[0][0]), '0 / 0 / < 0.50', overlap_ok),
    ]
    handoff = HANDOFF.replace('@@TABLE@@', '\n'.join(tbl)) \
        .replace('@@SIDS@@', '%d..%d' % (recs[0]['sid'], recs[-1]['sid'])) \
        .replace('@@JAC@@', ', '.join('%d (%.2f)' % (s, v) for v, s in jac[:3]))
    open(os.path.join(K, 'HANDOFF_P.md'), 'w', encoding='utf-8').write(handoff)
    print('\n'.join(tbl))
    print('wrote sentences_fresh.jsonl (70), annotations_fresh.json, writer_input.jsonl,'
          ' HANDOFF_P.md')
    assert overlap_ok, 'overlap check failed'
    assert all(lev.get(l, 0) == v for l, v in tgt.items()), lev
    for need, got in (('agent', agent >= 42), ('perf', perf >= 12), ('bude', bude >= 6),
                      ('cond', tf.get('conditional', 0) >= 8),
                      ('pres', tf.get('present', 0) >= 15), ('past', tf.get('past', 0) >= 20),
                      ('pastimp', past_imp >= 10), ('imp', imp_pas >= 10)):
        assert got, 'quota missed: ' + need
    return 0


HANDOFF = """# Phase 1k — HANDOFF from agent P (prep)

Read `phase1k/CONTEXT_1K.md` first (it carries the owner's §0 verbatim). Everything below is
produced by `phase1k/fresh/make_fresh.py` (deterministic, 0 model calls, 0 DB reads).

## 1 The 70 fresh sentences — counts

sids **@@SIDS@@** (max existing sid 32539 + >100000), `side:"fresh"`, arm-B form (explicit subject
pronoun wherever Slovak would drop it; noun subjects untouched), `g` = null everywhere.

@@TABLE@@

Closest existing sentences by content-word Jaccard (sid (score)): @@JAC@@ — no normalised Slovak
sentence and no English reference equals an existing one (original or arm-B rewritten).

`tf_gold`/`voice_sk`/`agent_nom`/`perfective_present`/`tense_open` are **gold metadata for
reporting only** — no checker layer, guard or prompt may read them. `agent_nom:true` means the
Slovak names a nominative agent AND the verb is transitive, i.e. an English passive recast is
possible and, per §0 B1, WRONG.

## 2 Schema notes

- Fresh records use the Phase 1j `sentences_all.jsonl` keys plus `annotation`
  (`{hygienised, raw}`, the `$J/*/annotations.json` shape: `id, t, lv, v, lk, alt`) plus the five
  gold fields. `annotations_fresh.json` is the same annotation keyed by `"<sid>"`, so existing
  checker code can be seeded exactly as in `baseline_dev_1j.py`.
- `lk` is parallel to `v` (one lock per accepted reference) and is the **practised structure** —
  under §0 it may only produce a TIP, never a rejection.
- `t` is synthetic (9000+) and carries no `m` mistake patterns, so no pattern lookup can fire on a
  fresh sentence. `n_items` is null until the answer writer has run.
- `band` is the Slovak word-count bucket, the same convention as Phase 1j.
- Item ids: `C:<sid>:<crc32(text)>` for intent C, `W:<sid>:<crc32(text)>` otherwise.

## 3 How to read data (always through the loader)

```python
import os, sys
K = os.path.expanduser('~/Projects/and-again-content/translation-offline/phase1k')
sys.path.insert(0, K)
from loader_1k import (load_dev_items, load_dev_annotations, load_holdout1j_items,
                       load_fresh_sentences, load_fresh_annotations, load_fresh_items)
dev  = load_dev_items(purpose='…')             # 490, arm-B sk/reference/refs
ann  = load_dev_annotations(purpose='…')       # arm-B annotations (g removed)
hol  = load_holdout1j_items(purpose='…')       # 490, labelled replay
frs  = load_fresh_sentences(purpose='…')       # 70, answer-free, always readable
itm  = load_fresh_items(purpose='…')           # GATED: needs PHASE1K_OPEN_FRESH=1
```

Every call appends `{ts, side, what, caller, n, purpose}` to `phase1k/access_log.jsonl`.
`$J` is `chmod -R a-w`: `loader_1k` neuters `loader_1j._log` and logs into `$K` instead, and sets
`sys.dont_write_bytecode` — still run python with `PYTHONDONTWRITEBYTECODE=1`.

## 4 The answer writer → the judge input

1. The writer reads ONLY `phase1k/fresh/writer_input.jsonl` (`{wid, slovak, level, topic}`) and
   writes `phase1k/fresh/writer_output.jsonl`, one line per sentence:
   `{"wid": 140001, "answers": [{"text": "…", "intent": "C|T|W|M|S|V|TF"}, …]}`
   Quotas enforced by the builder: per sentence **>= 3 C and >= 4 wrong**, overall **>= 30 V**
   (active→passive recast, the §0 B1 probe) and **>= 30 TF** (time-frame shift, the B2 probe).
   Exact duplicate texts inside one sentence are dropped before the quota check.
2. Then, exactly:

```
cd ~/Projects/and-again-content/translation-offline
PYTHONDONTWRITEBYTECODE=1 python3 phase1k/judge/build_judge_input.py
```

   It prints counts only and writes `fresh/items_fresh.jsonl`, `judge/in_1..in_4.jsonl`
   (Phase 1j DEV 490 + fresh + 60 control duplicates, shuffled with seed `phase1k-judge`, equal
   sizes, each control in a different chunk than its original), `judge/in_5.jsonl` (the 490
   Phase 1j HOLDOUT items) and `judge/key.jsonl` (j → {id, sid, source, dup_of}; forbidden to the
   judge). Judge lines carry **only** `{j, sk, en}`. A malformed writer_output fails loudly with a
   `WRITER_OUTPUT ERROR:` message. `python3 phase1k/judge/build_judge_input.py --selftest` runs the
   whole build on a fabricated writer_output in a temp dir.

## 5 Agent P self-count

11 tool calls (3 recon/inspect Bash, 4 Write, 2 Edit, 2 Bash build+selftest+lock+verify) — cap was 12.
"""


if __name__ == '__main__':
    sys.exit(main())

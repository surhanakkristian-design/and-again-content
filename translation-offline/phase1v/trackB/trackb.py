#!/usr/bin/env python3
"""Phase 1V / Track B - annotation cost of 60 real production Slovak sentences (0 Gemini calls).
The 1J arm-B rewrite (phase1j/taskB/apply_rewrite.py) and the 1M/1N annotation
(phase1m/make_annotations_part2.py schema) are HAND-AUTHORED agent work in the existing pipeline -
no Gemini call exists in either. So this track makes 0 model calls; token cost is measured on the
authored artefacts. Gold written by this agent from the Slovak alone, BEFORE any guard was run
(spec = phase1t/taskB/GOLD_SPEC_SK.md). Guards: phase1t/taskB/cz_validate.py g1-g4 + e2e, unchanged."""
import os, re, sys, json, math, importlib.util

BASE = os.path.expanduser("~/Projects/and-again-content/translation-offline")
HERE = os.path.join(BASE, "phase1v", "trackB")
sys.path.insert(0, BASE)

# ------------------------------------------------------------------ 1. GOLD (raw DB sentence)
# n: (tf, person, subject, voice, embedded_agents, fragment, tf_note)
AA, PD, IM = "active_agent", "active_prodrop", "impersonal"
GOLD = {
 1: ("present", "3pl", "traja pasažieri", AA, [], False, ""),
 2: ("present", "3sg", "Táto mikina s kapucňou", AA, [], False, ""),
 3: ("present", "3sg", "Každá krava", AA, [], False, ""),
 4: ("present", "3sg", "Muž v obleku", AA, [], False, ""),
 5: ("present", "3pl", "Skrinky", AA, [], False, ""),
 6: ("future", "3sg", None, PD, [], False, "perfective present"),
 7: ("present", "3pl", "dve fľaštičky dezinfekcie na ruky", AA, [], False, ""),
 8: ("present", "3sg", "On", AA, [], False, ""),
 9: ("present", "3pl", None, PD, [], False, ""),
 10: ("present", "3sg", "to", AA, [], False, ""),
 11: ("present", "3sg", None, PD, [], False, "ísť + infinitive, prospective"),
 12: ("present", "3sg", "skúter", AA, [], False, ""),
 13: ("present", "3pl", "Tínedžeri", AA, [], False, ""),
 14: ("past", "3sg", "vták", AA, ["to"], False, ""),
 15: ("present", "3pl", "muchy", AA, [], False, ""),
 16: ("present", "3sg", "Tatér", AA, [], False, ""),
 17: ("future", "3sg", None, PD, ["tá"], False, "perfective present"),
 18: ("present", "3sg", None, PD, [], False, ""),
 19: ("present", "3pl", "dvaja šťastní ľudia", AA, [], False, ""),
 20: ("present", "3pl", "dve misky jahôd", AA, [], False, ""),
 21: ("present", "3sg", "Jedlo", AA, [], False, ""),
 22: ("past", "1sg", None, PD, ["vodopád"], False, "main = počula som"),
 23: ("present", "3sg", "modrá miska", AA, [], False, ""),
 24: ("present", "3sg", "Blesk", AA, [], False, "main = šľahá"),
 25: ("future", "3sg", None, PD, [], False, "perfective present; main = cvakne"),
 26: ("present", "3sg", "On", AA, [], False, ""),
 27: ("present", "3sg", "Tím", AA, [], False, ""),
 28: ("present", "3sg", None, PD, [], False, ""),
 29: ("present", "3sg", "Tento chalan", AA, [], False, ""),
 30: ("present", "3pl", "Kone", AA, ["oni"], False, ""),
 31: ("present", "3sg", "Krúžok", AA, [], False, ""),
 32: ("past", "3sg", None, PD, [], False, ""),
 33: ("past", "3sg", None, PD, [], False, ""),
 34: ("past", "3sg", "Tom", AA, [], False, ""),
 35: ("past", "3sg", None, PD, ["moja promócia", "to"], False, "main = Všetkým povedal"),
 36: ("present", "3sg", None, PD, [], False, ""),
 37: ("present", "3sg", "Koliesko", AA, ["povrch"], False, ""),
 38: ("past", "3sg", "Ona", AA, ["prachová plachta"], False, ""),
 39: ("past", "3sg", None, PD, [], False, ""),
 40: ("present", "3sg", "Zopnutá kopa", AA, ["miska vedľa nej"], False, ""),
 41: ("present", "3pl", "Trosky", AA, ["škody"], False, ""),
 42: ("future", "3sg", "viac úlomkov", AA, ["škrabanie"], False, "perfective present"),
 43: ("past", "3sg", None, PD, [], False, ""),
 44: ("future", "3sg", "monitor", AA, [], False, "perfective present"),
 45: ("present", "3pl", None, PD, [], False, ""),
 46: ("future", "3pl", None, PD, [], False, ""),
 47: ("future", "3sg", None, PD, [], False, "perfective present"),
 48: ("future", "3sg", "šíp", AA, [], False, "perfective present (gnomic)"),
 49: ("future", "2sg", None, PD, [], False, "perfective present"),
 50: ("future", "3sg", None, PD, [], False, ""),
 51: ("present", "3sg", None, PD, [], False, ""),
 52: ("past", "3sg", "Jazero", AA, [], False, ""),
 53: ("present", "3sg", None, PD, ["slová"], False, "main = číta"),
 54: ("past", "3sg", None, PD, [], False, ""),
 55: ("past", "3sg", None, PD, [], False, ""),
 56: ("present", "3sg", None, IM, [], False, "je známe"),
 57: ("past", "3sg", None, PD, [], False, ""),
 58: ("past", "3sg", "Voľný kop", AA, ["nikto v múre"], False, ""),
 59: ("past", "3sg", "mäsiar", AA, ["jeho obchod"], False, ""),
 60: ("past", "3pl", None, PD, [], False, ""),
}

# ------------------------------------------------------------------ 2. ARM-B REWRITE (1J rule)
# n: ("R", new_sk, pronoun, where)  where = "main" | "embedded"   |  ("U", reason)
REWRITE = {
 1: ("U", "explicit_subject"), 2: ("U", "explicit_subject"), 3: ("U", "explicit_subject"),
 4: ("U", "explicit_subject"), 5: ("U", "explicit_subject"),
 6: ("R", "On si skúsi štyri tričká, kým si jedno vyberie.", "on", "main"),
 7: ("U", "explicit_subject"), 8: ("U", "explicit_subject"),
 9: ("R", "Oni majú pohár medu a drevenú naberačku.", "oni", "main"),
 10: ("U", "explicit_subject"),
 11: ("R", "Ona ide držať dve veľké kosti, kámo.", "ona", "main"),
 12: ("U", "explicit_subject"), 13: ("U", "explicit_subject"), 14: ("U", "explicit_subject"),
 15: ("U", "explicit_subject"), 16: ("U", "explicit_subject"),
 17: ("R", "Ona si sadne na stoličku a tá sa ani nepohne.", "ona", "main"),
 18: ("R", "Ona do Ríma chodí často, ale včera večer prišla sama.", "ona", "main"),
 19: ("U", "explicit_subject"), 20: ("U", "explicit_subject"),
 21: ("R", "Jedlo je stále na sporáku, ale oni tancujú ďalej.", "oni", "embedded"),
 22: ("R", "Hádaj čo, ja som počula, že za tamtým kamenným mostom je vodopád.", "ja", "main"),
 23: ("U", "explicit_subject"), 24: ("U", "explicit_subject"),
 25: ("R", "Pozri na tie nožnice! Ona hneď cvakne", "ona", "main"),
 26: ("U", "explicit_subject"), 27: ("U", "explicit_subject"),
 28: ("R", "Na placku on dáva veľa syra", "on", "main"),
 29: ("U", "explicit_subject"), 30: ("U", "explicit_subject"),
 31: ("R", "Krúžok, ktorý ona schytila z dlaždíc, jej teraz kvapká nad hlavou.", "ona", "embedded"),
 32: ("R", "Ona toto už robila — tú otočku musela nacvičovať aspoň stokrát.", "ona", "main"),
 33: ("R", "Ona pritlačila pečať na dekrét a v miestnosti stíchlo.", "ona", "main"),
 34: ("U", "explicit_subject"),
 35: ("R", "„Dnes je moja promócia,“ povedal. On všetkým povedal, že to je deň jeho promócie.", "on", "main"),
 36: ("R", "Ona je z toho zápasu veľmi nadšená, však?", "ona", "main"),
 37: ("U", "explicit_subject"), 38: ("U", "explicit_subject"),
 39: ("R", "On šprintoval za loptou, keď sa zrazu chytil za lýtko. Katastrofa!", "on", "main"),
 40: ("U", "explicit_subject"), 41: ("U", "explicit_subject"),
 42: ("R", "Ak on zoškrabe viac farby, viac úlomkov odpadne, lebo škrabanie robí úlomky.", "on", "embedded"),
 43: ("R", "Ona povedala, že kamarátku za to neodsudzuje", "ona", "main"),
 44: ("R", "Ak on zapojí poslednú zástrčku, zapne sa monitor. Skutočný vizionár, jasne.", "on", "embedded"),
 45: ("R", "Oni súťažia pred veľkým davom, však?", "oni", "main"),
 46: ("R", "Do záverečného hvizdu oni budú behať v tej horúčave deväťdesiat minút.", "oni", "main"),
 47: ("R", "Dnes do deviatej on zahrá každú pieseň, ktorú pozná, aspoň trikrát.", "on", "main"),
 48: ("U", "explicit_subject"),
 49: ("R", "Do západu slnka ty skontroluješ kompas stokrát, kapitánka. Rešpekt.", "ty", "main"),
 50: ("R", "Do večera on bude mať poslané svoje video z tunela všetkým, ktorých pozná. Zjavne skromný cestovateľ.", "on", "main"),
 51: ("R", "On si želá, aby bol odišiel z domu skôr! Každý jeden presun je úplná nočná mora!", "on", "main"),
 52: ("R", "Jazero zrkadlilo stromy dokonale, kým on neskočil a všetko nezničil!", "on", "embedded"),
 53: ("R", "Pozri sa naňho - on číta tú istú stranu už tretíkrát a dúfa, že sa slová zmenia.", "on", "main"),
 54: ("R", "On poprel, že vypílil medveďovi nohy príliš tenké.", "on", "main"),
 55: ("R", "On mal ponožky premočené, lebo celú minútu stál v tej mláke bez toho, aby si to všimol.", "on", "main"),
 56: ("U", "impersonal"),
 57: ("R", "On priznal, že bol úplne vyčerpaný po najhoršom týždni svojho života!", "on", "main"),
 58: ("U", "explicit_subject"), 59: ("U", "explicit_subject"),
 60: ("R", "Paradajky si oni v to ráno dali natrhať v gazdovskom obchode.", "oni", "main"),
}

# ------------------------------------------------------------------ 3. ANNOTATION (1M/1N schema)
# n: (v, lk, alt, tf_gold, perfective_present, tense_open); voice_sk/agent_nom derived from after-gold
ANN = {
 1: (["Three passengers are waiting under the small shelter.", "Three passengers wait under the small shelter."], ["are waiting", "wait"], {"shelter": ["canopy", "roof"], "passengers": ["travellers"]}, "present", False, True),
 2: (["This hoodie is too big for me!"], ["is"], {"hoodie": ["hooded sweatshirt"], "too big": ["way too big"]}, "present", False, False),
 3: (["Every cow has a big brass bell.", "Every cow has got a big brass bell."], ["has", "has got"], {"big": ["large"], "Every": ["Each"]}, "present", False, False),
 4: (["The man in the suit is a businessman."], ["is"], {"businessman": ["entrepreneur"]}, "present", False, False),
 5: (["The lockers are in the long corridor by the classrooms.", "The lockers are in the long hallway next to the classrooms."], ["are", "are"], {"corridor": ["hallway"], "by": ["next to", "near"]}, "present", False, False),
 6: (["He will try on four T-shirts before he chooses one.", "He tries on four T-shirts before he picks one."], ["will try", "tries"], {"chooses": ["picks"], "T-shirts": ["tees"]}, "future", True, True),
 7: (["There are two little bottles of hand sanitizer in her bag.", "Two bottles of hand sanitizer are in her bag."], ["are", "are"], {"hand sanitizer": ["hand sanitiser"], "bag": ["handbag"]}, "present", False, False),
 8: (["He is pouring lentils onto this bowl of rice.", "He pours lentils onto this bowl of rice."], ["is pouring", "pours"], {"onto": ["on"]}, "present", False, True),
 9: (["They have a jar of honey and a wooden dipper.", "They have got a jar of honey and a wooden dipper."], ["have", "have got"], {"dipper": ["honey dipper", "ladle"], "jar": ["pot"]}, "present", False, False),
 10: (["It is that old restaurant, not the new one.", "It's the old restaurant, not a new one."], ["is", "is"], {}, "present", False, False),
 11: (["She is going to hold two big bones, mate.", "She's gonna hold two big bones, bro."], ["is going to", "is going to"], {"mate": ["bro", "dude"], "big": ["large"]}, "present", False, True),
 12: (["Where is the scooter falling? Into the tall reeds.", "Where does the scooter fall? Into the tall reeds."], ["is falling", "does fall"], {"tall": ["high"]}, "present", False, True),
 13: (["The teenagers are playing a game on the big TV.", "The teenagers play a game on the big TV."], ["are playing", "play"], {"TV": ["television"], "big": ["large"]}, "present", False, True),
 14: (["A bird has landed on him! It is that amazing moment.", "A bird landed on him! It is an amazing moment."], ["has landed", "landed"], {"amazing": ["incredible"]}, "past", False, True),
 15: (["In summer there are always flies in the kitchen."], ["are"], {"In summer": ["In the summer"]}, "present", False, False),
 16: (["The tattoo artist is peeling off the film very slowly.", "The tattooist peels the film very slowly."], ["is peeling", "peels"], {"film": ["foil", "wrap"], "tattoo artist": ["tattooist"]}, "present", False, True),
 17: (["She will sit down on the chair and it will not even move.", "She sits down on the chair and it does not even move."], ["will sit", "sits"], {"chair": ["seat"]}, "future", True, True),
 18: (["She often goes to Rome, but last night she came alone.", "She visits Rome often, but last night she came on her own."], ["goes + came", "visits + came"], {"alone": ["on her own", "by herself"]}, "present", False, False),
 19: (["There are two happy people at this tiny table."], ["are"], {"tiny": ["very small", "little"]}, "present", False, False),
 20: (["There are two bowls of strawberries on the table."], ["are"], {}, "present", False, False),
 21: (["The food is still on the stove, but they keep dancing.", "The food is still on the cooker, but they are dancing on."], ["is + keep", "is + are dancing"], {"stove": ["cooker"]}, "present", False, False),
 22: (["Guess what, I heard that there is a waterfall behind that stone bridge.", "Guess what, I've heard there's a waterfall behind that stone bridge."], ["heard", "have heard"], {"that": ["the"]}, "past", False, True),
 23: (["There is a blue bowl on the small table."], ["is"], {"small": ["little"]}, "present", False, False),
 24: (["Look! Lightning is flashing over the sea right now."], ["is flashing"], {"flashing": ["striking"], "right now": ["just now"]}, "present", False, False),
 25: (["Look at those scissors! She is going to snip in a second.", "Look at those scissors! She'll snip right away."], ["is going to", "will"], {"snip": ["cut", "click"]}, "future", True, True),
 26: (["He also has blue paint. He is going to use it for the sky.", "He has got blue paint too. He is about to use it for the sky."], ["has + is going to", "has got + is about to"], {"paint": ["colour"]}, "present", False, False),
 27: (["The team plays on this court every Friday."], ["plays"], {"court": ["pitch", "field"]}, "present", False, False),
 28: (["He is putting a lot of cheese on the patty.", "He puts a lot of cheese on the patty."], ["is putting", "puts"], {"a lot of": ["lots of", "plenty of"]}, "present", False, True),
 29: (["This guy is lazier than my cat."], ["is"], {"guy": ["lad", "boy"]}, "present", False, False),
 30: (["Horses usually eat feed, but now they are eating hay."], ["eat + are eating"], {"feed": ["fodder"]}, "present", False, False),
 31: (["The ring she grabbed off the tiles is now dripping above her head."], ["grabbed + is dripping"], {"grabbed": ["snatched"], "ring": ["hoop"]}, "present", False, False),
 32: (["She has done this before — she must have practised that turn at least a hundred times.", "She did this before — she had to practise that spin at least a hundred times."], ["has done + must have practised", "did + had to practise"], {"turn": ["spin"]}, "past", False, True),
 33: (["She pressed the seal onto the decree and the room fell silent.", "She pressed the seal onto the decree and the room went quiet."], ["pressed", "pressed"], {"fell silent": ["went quiet"]}, "past", False, False),
 34: (["Tom said he was running slowly on purpose, not because he was tired.", "Tom said that he was jogging slowly deliberately, not because he was tired."], ["said + was running", "said + was jogging"], {"on purpose": ["deliberately"]}, "past", False, True),
 35: (["\"Today is my graduation,\" he said. He told everyone that it was his graduation day."], ["said + told"], {"graduation": ["graduation ceremony"]}, "past", False, True),
 36: (["She is very excited about the match, isn't she?", "She is really enthusiastic about that match, isn't she?"], ["is", "is"], {"excited": ["enthusiastic", "thrilled"]}, "present", False, False),
 37: (["The little wheel rolls across it without a single wobble, so the surface must be perfectly flat.", "The wheel is rolling over it without a single wobble, so the surface must be completely flat."], ["rolls", "is rolling"], {"perfectly": ["completely"]}, "present", False, True),
 38: (["She was dragging the chest across the attic floor when the dust sheet tore."], ["was dragging + tore"], {"chest": ["trunk"], "dragging": ["hauling", "pulling"]}, "past", False, False),
 39: (["He was sprinting after the ball when he suddenly grabbed his calf. Disaster!"], ["was sprinting + grabbed"], {"after": ["for"]}, "past", False, False),
 40: (["The clipped pile is not moving, and the bowl next to it is not moving either."], ["is not moving"], {"bowl": ["dish"]}, "present", False, False),
 41: (["The wreckage is still smoking, so the damage must be very recent."], ["is smoking + must be"], {"wreckage": ["debris"], "recent": ["fresh"]}, "present", False, False),
 42: (["If he scrapes off more paint, more chips will fall off, because scraping makes chips."], ["scrapes + will fall"], {"chips": ["flakes"]}, "future", True, False),
 43: (["She said that she didn't judge her friend for it.", "She said she does not judge her friend for that."], ["said + didn't judge", "said + does not judge"], {"friend": ["girlfriend"]}, "past", False, True),
 44: (["If he plugs in the last plug, the monitor will turn on. A true visionary, clearly."], ["plugs + will turn on"], {"turn on": ["switch on", "come on"]}, "future", True, False),
 45: (["They are competing in front of a big crowd, aren't they?"], ["are competing"], {"big": ["large", "huge"]}, "present", False, False),
 46: (["By the final whistle they will have been running in that heat for ninety minutes."], ["will have been running"], {"heat": ["hot weather"]}, "future", False, False),
 47: (["By nine tonight he will have played every song he knows at least three times.", "By nine today he will play every song he knows at least three times."], ["will have played", "will play"], {"tonight": ["today"]}, "future", True, True),
 48: (["In weather like this an arrow rarely hits the centre of the target so cleanly.", "Rarely does an arrow hit the bullseye that cleanly in weather like this."], ["hits", "does hit"], {"centre of the target": ["bullseye"]}, "future", True, True),
 49: (["By sunset you will have checked the compass a hundred times, captain. Respect."], ["will have checked"], {}, "future", True, False),
 50: (["By tonight he will have sent his tunnel video to everyone he knows. Clearly a modest traveller."], ["will have sent"], {"modest": ["humble"]}, "future", False, False),
 51: (["He wishes he had left home earlier! Every single transfer is a complete nightmare!"], ["wishes + had left"], {"transfer": ["connection", "change"]}, "present", False, False),
 52: (["The lake had been mirroring the trees perfectly until he jumped in and ruined everything!", "The lake was reflecting the trees perfectly until he jumped and destroyed everything!"], ["had been mirroring", "was reflecting"], {"mirroring": ["reflecting"], "ruined": ["destroyed", "spoiled"]}, "past", False, True),
 53: (["Look at him - he is reading the same page for the third time already, hoping the words will change."], ["is reading"], {}, "present", False, False),
 54: (["He denied that he had sawn the bear's legs too thin.", "He denied having sawn the bear's legs too thin."], ["denied + had sawn", "denied + having sawn"], {"sawn": ["cut"]}, "past", False, True),
 55: (["His socks were soaked because he had been standing in that puddle for a whole minute without noticing.", "His socks were soaking wet, because he stood in that puddle for a whole minute without noticing it."], ["were + had been standing", "were + stood"], {"soaked": ["soaking wet", "drenched"]}, "past", False, True),
 56: (["About this species, the flamingo, it is known that it gets its pink colour from its food.", "This species, the flamingo, is known to get its pink colour from its food."], ["is known", "is known"], {"colour": ["color"], "food": ["diet"]}, "present", False, False),
 57: (["He admitted that he had been completely exhausted after the worst week of his life!", "He admitted being completely exhausted after the worst week of his life!"], ["admitted + had been", "admitted + being"], {"exhausted": ["worn out"]}, "past", False, True),
 58: (["The free kick, which nobody in the wall even saw, ended up in the top corner."], ["ended up"], {"ended up": ["finished"]}, "past", False, False),
 59: (["Bestie, the butcher told me he wishes his shop had more customers today.", "Girl, the butcher told me he would like his shop to have more customers today."], ["told + wishes", "told + would like"], {"Bestie": ["Girl", "Mate"]}, "past", False, True),
 60: (["They had the tomatoes picked at the farm shop that morning.", "That morning they had tomatoes picked for them at the farm shop."], ["had picked", "had picked"], {"farm shop": ["farmers' shop"]}, "past", False, False),
}


def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(BASE, rel))
    m = importlib.util.module_from_spec(spec); sys.modules[name] = m; spec.loader.exec_module(m); return m


def cp(k, n, a=0.05):
    def cdf(x, p):
        return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(x + 1))
    def bis(f):
        lo, hi = 0.0, 1.0
        for _ in range(60):
            mid = (lo + hi) / 2
            if f(mid): lo = mid
            else: hi = mid
        return (lo + hi) / 2
    lo = 0.0 if k == 0 else bis(lambda p: 1 - cdf(k - 1, p) < a / 2)
    hi = 1.0 if k == n else bis(lambda p: cdf(k, p) > a / 2)
    return [round(100 * lo, 2), round(100 * hi, 2)]


def fisher_2x2(a, b, c, d):
    n1, n2, m1, N = a + b, c + d, a + c, a + b + c + d
    def pr(x):
        return math.comb(n1, x) * math.comb(n2, m1 - x) / math.comb(N, m1)
    p0 = pr(a)
    return sum(pr(x) for x in range(max(0, m1 - n2), min(n1, m1) + 1) if pr(x) <= p0 * (1 + 1e-9))


def ntok(s):
    try:
        import tiktoken
        return len(tiktoken.get_encoding("cl100k_base").encode(s)), "tiktoken cl100k_base"
    except Exception:
        return math.ceil(len(s.encode("utf-8")) / 4), "utf8 bytes / 4"


# ------------------------------------------------------------------ build rows + gold after
raw = json.load(open(os.path.join(HERE, "sample_raw.json"), encoding="utf-8"))
raw = raw if isinstance(raw, list) else raw["rows"]
rows = []
for i, r in enumerate(raw, 1):
    tf, pers, subj, voice, emb, frag, note = GOLD[i]
    g0 = {"n": i, "tf": tf, "tf_note": note, "person": pers, "subject_explicit": subj is not None,
          "subject": subj, "voice": voice, "agent_nom": voice == AA, "embedded_agents": emb, "fragment": frag}
    rw = REWRITE[i]
    g1_ = json.loads(json.dumps(g0))
    new = r["sk"]
    if rw[0] == "R":
        new, pron, where = rw[1], rw[2], rw[3]
        a = [w.lower() for w in re.findall(r"\w+", r["sk"])]
        b = [w.lower() for w in re.findall(r"\w+", new)]
        for w in a:
            b.remove(w)
        assert b == [pron], (i, b)                      # 1J machine check: old + exactly the pronoun
        if where == "main":
            g1_.update(subject=pron, subject_explicit=True, voice=AA, agent_nom=True)
        else:
            g1_["embedded_agents"] = g1_["embedded_agents"] + [pron]
    v, lk, alt, tfg, pp, topen = ANN[i]
    ann = {"id": r["exercise_id"], "t": 9000 + i, "lv": r["level"], "v": v, "lk": lk, "alt": alt,
           "tf_gold": tfg, "voice_sk": g1_["voice"], "agent_nom": g1_["agent_nom"],
           "perfective_present": pp, "tense_open": topen}
    rows.append({"n": i, "exercise_id": r["exercise_id"], "level": r["level"], "en": r["en"],
                 "sk_raw": r["sk"], "sk_new": new, "rewrite": list(rw), "gold_before": g0,
                 "gold_after": g1_, "annotation": ann})

# ------------------------------------------------------------------ token cost of the authored artefacts
tok_rw, tok_ann, tok_gold = [], [], []
for r in rows:
    rw = REWRITE[r["n"]]
    rw_obj = {"n": r["n"], "status": rw[0], "new_sk": rw[1] if rw[0] == "R" else None,
              "reason": rw[1] if rw[0] == "U" else None, "pronoun": rw[2] if rw[0] == "R" else None}
    t1, how = ntok(json.dumps(rw_obj, ensure_ascii=False)); tok_rw.append(t1)
    t2, _ = ntok(json.dumps(r["annotation"], ensure_ascii=False)); tok_ann.append(t2)
    t3, _ = ntok(json.dumps(r["gold_before"], ensure_ascii=False)); tok_gold.append(t3)
nR = sum(1 for r in rows if r["rewrite"][0] == "R")
nR_rows = [t for t, r in zip(tok_rw, rows) if r["rewrite"][0] == "R"]

# ------------------------------------------------------------------ guards (phase1t/taskB method, unchanged)
f9 = load("f9_1n", "phase1n/f9.py")
CK = load("checker_1i", "phase1i/checker_1i.py")
V2 = load("agent_drop_v2", "phase1s/taskC/agent_drop_v2.py")
V3 = load("agent_drop_v3", "phase1t/taskA/agent_drop_v3.py")
src = open(os.path.join(BASE, "phase1t/taskB/cz_validate.py"), encoding="utf-8").read()
body = src[src.index("WORD = re.compile"):src.index("\nout = []")]
NS = {"re": re, "json": json, "os": os, "f9": f9, "CK": CK, "V2": V2, "V3": V3}
exec(body, NS)

res = {}
for state in ("before", "after"):
    per = {k: {} for k in ("g1", "g2", "g3_v2", "g3_v3", "g4_v2", "g4_v3")}
    errs = {k: [] for k in per}
    e2e_rej = {"ann_empty": [], "ann_used": []}
    for r in rows:
        text = r["sk_raw"] if state == "before" else r["sk_new"]
        g = r["gold_before"] if state == "before" else r["gold_after"]
        out = {"g1": NS["g1"](text, g)["class"], "g2": NS["g2"](text, g)["class"],
               "g3_v2": NS["g3"](text, g, V2), "g3_v3": NS["g3"](text, g, V3), "g4": NS["g4"](text, g)}
        cls = {"g1": out["g1"], "g2": out["g2"], "g3_v2": out["g3_v2"]["class"], "g3_v3": out["g3_v3"]["class"],
               "g4_v2": out["g4"]["class_v2"], "g4_v3": out["g4"]["class_v3"]}
        for k, c in cls.items():
            key = "ERROR" if str(c).startswith("ERROR") else c
            per[k][key] = per[k].get(key, 0) + 1
            if key == "ERROR":
                extra = out[k]["agent"] if k.startswith("g3") else ""
                errs[k].append([r["n"], text[:80], c, g["subject"], g["voice"], g["tf"], g["person"], extra])
        ann = {} if state == "before" else r["annotation"]
        for lbl, a in (("ann_empty", {}), ("ann_used", ann)):
            if state == "before" and lbl == "ann_used":
                continue
            try:
                d = V3.decide(text, a, {}, r["en"], r["en"], "primary")
                if d.get("fired"):
                    e2e_rej[lbl].append([r["n"], d.get("reason"), d.get("agent")])
            except Exception as ex:
                e2e_rej[lbl].append([r["n"], "CRASH " + repr(ex), None])
        r.setdefault("guards", {})[state] = cls
    rate = {k: {"ERROR": v.get("ERROR", 0), "rate_pct": round(100 * v.get("ERROR", 0) / len(rows), 2),
                "cp95": cp(v.get("ERROR", 0), len(rows)), "counts": v} for k, v in per.items()}
    res[state] = {"per_guard": rate, "errors": errs, "e2e_ag_v3_rejects_en_reference": e2e_rej}

ag_b = res["before"]["per_guard"]["g3_v2"]["ERROR"]
summary = {
    "n": len(rows), "levels": {lv: sum(1 for r in rows if r["level"] == lv) for lv in ("A1", "A2", "B1", "B2")},
    "gemini_calls": {"planned": 0, "counted": 0, "failed": 0, "retried": 0, "spend_usd": 0.0},
    "B1": {"needed_rewrite": nR, "of": len(rows), "pct": round(100 * nR / len(rows), 2), "cp95": cp(nR, len(rows)),
           "1J": "91/140 = 65.0 %", "fisher_p_vs_1J": round(fisher_2x2(nR, len(rows) - nR, 91, 49), 4),
           "tokenizer": ntok("x")[1],
           "rewrite_tok_per_sentence_all60": round(sum(tok_rw) / len(rows), 1),
           "rewrite_tok_per_rewritten_sentence": round(sum(nR_rows) / max(1, nR), 1),
           "annotation_tok_per_sentence": round(sum(tok_ann) / len(rows), 1),
           "gold_tok_per_sentence": round(sum(tok_gold) / len(rows), 1),
           "rewrite_tok_total": sum(tok_rw), "annotation_tok_total": sum(tok_ann),
           "by_level_ann_tok": {lv: round(sum(t for t, r in zip(tok_ann, rows) if r["level"] == lv) / 15, 1)
                                for lv in ("A1", "A2", "B1", "B2")},
           "by_level_rewrites": {lv: sum(1 for r in rows if r["level"] == lv and r["rewrite"][0] == "R")
                                 for lv in ("A1", "A2", "B1", "B2")}},
    "B2": {s: {k: [v["ERROR"], v["rate_pct"], v["cp95"]] for k, v in res[s]["per_guard"].items()} for s in res},
    "B2_counts": {s: {k: v["counts"] for k, v in res[s]["per_guard"].items()} for s in res},
    "B2_AG_vs_1T": {"this_raw": "%d/60 = %.2f %% %s" % (ag_b, 100 * ag_b / 60, cp(ag_b, 60)),
                    "1T_sk_raw": "47/120 = 39.17 % [30.4, 48.5]",
                    "fisher_p": round(fisher_2x2(ag_b, 60 - ag_b, 47, 73), 4)},
    "e2e": {s: {k: len(v) for k, v in res[s]["e2e_ag_v3_rejects_en_reference"].items()} for s in res},
}
N_ALL = 5895
t_rw, t_ann = sum(tok_rw) / 60, sum(tok_ann) / 60
summary["B3"] = {"n": N_ALL, "model": "linear", "rewrite_tok": round(t_rw * N_ALL),
                 "annotation_tok": round(t_ann * N_ALL), "gold_tok_if_gold_needed": round(sum(tok_gold) / 60 * N_ALL),
                 "total_authored_tok": round((t_rw + t_ann) * N_ALL),
                 "rewrites_expected": round(nR / 60 * N_ALL), "rewrites_cp95": [round(x / 100 * N_ALL) for x in cp(nR, 60)],
                 "gemini_checking_calls": 0}
json.dump({"summary": summary, "results": res, "rows": rows},
          open(os.path.join(HERE, "trackb_results.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps(summary, ensure_ascii=False, indent=1))
for s in res:
    print("====", s)
    for k, v in res[s]["errors"].items():
        for e in v:
            print(" ", k, e)
    for k, v in res[s]["e2e_ag_v3_rejects_en_reference"].items():
        for e in v:
            print("  e2e", k, e)

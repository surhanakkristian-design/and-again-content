import json, re, os
C = {
 "@ART": ("missing article", "w", "article dropped before a singular countable noun (pillow for a pillow)",
  "Pred počítateľným podstatným menom v jednotnom čísle chýba člen: „{right}“.",
  "Před počitatelným podstatným jménem v jednotném čísle chybí člen: „{right}“.",
  "A singular countable noun needs an article: “{right}”."),
 "@ARTX": ("extra article", "w", "article added where English has none (the next week, the nature)",
  "Tu sa člen nepoužíva: „{right}“, nie „{wrong}“.",
  "Tady se člen nepoužívá: „{right}“, ne „{wrong}“.",
  "No article here: “{right}”, not “{wrong}”."),
 "@IRR": ("regular form of irregular verb", "w", "-ed added to an irregular verb (striked, bursted, flied)",
  "Nepravidelné sloveso: správny tvar je „{right}“, nie „{wrong}“.",
  "Nepravidelné sloveso: správný tvar je „{right}“, ne „{wrong}“.",
  "Irregular verb: the correct form is “{right}”, not “{wrong}”."),
 "@S3": ("missing third person -s", "w", "Present Simple verb without -s after he/she/it or a singular noun",
  "Pri podmete v jednotnom čísle (he, she, it) treba v Present Simple -s: „{right}“.",
  "U podmětu v jednotném čísle (he, she, it) je v Present Simple potřeba -s: „{right}“.",
  "A singular subject (he, she, it) needs -s in Present Simple: “{right}”."),
 "@PREP": ("calqued preposition", "w", "wrong, extra or missing preposition copied from Slovak/Czech (struck into, on place)",
  "Správne spojenie je „{right}“, nie „{wrong}“.",
  "Správné spojení je „{right}“, ne „{wrong}“.",
  "The correct phrase is “{right}”, not “{wrong}”."),
 "@DNEG": ("double negation", "w", "second negative added (didn't … nothing, never doesn't, neither isn't)",
  "V angličtine je vo vete len jeden zápor: „{right}“, nie „{wrong}“.",
  "V angličtině je ve větě jen jeden zápor: „{right}“, ne „{wrong}“.",
  "English uses only one negative here: “{right}”, not “{wrong}”."),
 "@POSS": ("article or dative with body part", "w", "the/you instead of a possessive with a body part (burn you the fingers, above the head)",
  "Pri častiach tela patrí privlastňovacie zámeno: „{right}“, nie „{wrong}“.",
  "U částí těla patří přivlastňovací zájmeno: „{right}“, ne „{wrong}“.",
  "Body parts take a possessive: “{right}”, not “{wrong}”."),
 "@WO": ("adverb between verb and object", "w", "adverb put between the verb and its object (score first the skin)",
  "Príslovka nestojí medzi slovesom a predmetom: „{right}“.",
  "Příslovce nestojí mezi slovesem a předmětem: „{right}“.",
  "Don't put the adverb between the verb and its object: “{right}”."),
 "@CALQ": ("word-for-word calque", "w", "phrase translated word for word from Slovak/Czech (today morning, this night, there where)",
  "Doslovný preklad nesedí, po anglicky je to „{right}“, nie „{wrong}“.",
  "Doslovný překlad nesedí, anglicky je to „{right}“, ne „{wrong}“.",
  "A word-for-word translation doesn't work: say “{right}”, not “{wrong}”."),
 "@WORD": ("wrong word choice", "w", "false friend or near-synonym with a different meaning (work for job, true for real, quiet for still)",
  "Význam nesedí: tu patrí „{right}“, nie „{wrong}“.",
  "Význam nesedí: sem patří „{right}“, ne „{wrong}“.",
  "Wrong word for this meaning: use “{right}”, not “{wrong}”."),
 "@NAT": ("less natural wording", "t", "correct near-synonym or phrasing that sounds less natural (legs for feet, two times for twice)",
  "Prirodzenejšie je „{right}“ ako „{wrong}“.",
  "Přirozenější je „{right}“ než „{wrong}“.",
  "“{right}” sounds more natural than “{wrong}”."),
 "@REFL": ("reflexive verb as Passive", "w", "Slovak/Czech reflexive verb (sa/se) turned into be + participle (was started, is opened)",
  "Zvratné sloveso („sa“) tu nie je Passive: patrí „{right}“, nie „{wrong}“.",
  "Zvratné sloveso („se“) tu není Passive: patří „{right}“, ne „{wrong}“.",
  "This is not Passive in English: use “{right}”, not “{wrong}”."),
 "@DIDNT": ("past form after didn't", "w", "past form kept after did/didn't (didn't saw, did she went)",
  "Po „did/didn't“ patrí base form: „{right}“, nie „{wrong}“.",
  "Po „did/didn't“ patří base form: „{right}“, ne „{wrong}“.",
  "After “did/didn't” use the base form: “{right}”, not “{wrong}”."),
}

def build(tid, topic, level, rows, outdir):
    items = []
    for i, r in enumerate(rows, 1):
        if isinstance(r, str): r = C[r]
        kind, v, pat, sk, cz, en = r
        slots = []
        for s in re.findall(r'\{(\w+)\}', sk + cz + en):
            if s not in slots: slots.append(s)
        order = ['right', 'wrong']
        slots = [s for s in order if s in slots] + [s for s in slots if s not in order]
        items.append({"id": f"{tid}.{i:02d}", "kind": kind, "verdict": "wrong" if v == "w" else "correct_with_tip",
                      "pattern": pat, "slots": slots, "sk": sk, "cz": cz, "en": en})
    d = {"type_id": tid, "topic": topic, "level": level, "items": items}
    with open(os.path.join(outdir, f"{tid}.json"), "w") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
    return d

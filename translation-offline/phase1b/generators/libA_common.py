import json, re, os
BASE = os.path.expanduser('~/Projects/and-again-content/translation-offline/phase1b')
TOPICS = json.load(open(BASE + '/selection/topics.json'))

# generic items: key -> (kind, verdict, pattern, sk, cz, en)
G = {
 'art_miss': ("missing article", "w", "drop a/an/the before a noun",
   "Chýba člen: „{right}“.", "Chybí člen: „{right}“.", "An article is missing: “{right}”."),
 'art_wrong': ("wrong article", "w", "a/an where the belongs, or the where a/an belongs",
   "Tu patrí „{right}“, nie „{wrong}“.", "Tady patří „{right}“, ne „{wrong}“.", "Use “{right}” here, not “{wrong}”."),
 'an_a': ("a/an mixed up", "w", "a before a vowel sound or an before a consonant sound",
   "Podľa výslovnosti patrí „{right}“, nie „{wrong}“.", "Podle výslovnosti patří „{right}“, ne „{wrong}“.", "By sound, it is “{right}”, not “{wrong}”."),
 'a_uncount': ("a with uncountable noun", "w", "a/an before an uncountable noun (a sugar, a water)",
   "Toto slovo sa nepočíta, bez „a“: „{right}“.", "Toto slovo se nepočítá, bez „a“: „{right}“.", "This noun is uncountable, so no “a”: “{right}”."),
 'a_plural': ("a with plural noun", "w", "a/an before a plural noun (a books)",
   "Pred množným číslom nepatrí „a“: „{right}“.", "Před množným číslem nepatří „a“: „{right}“.", "No “a” before a plural: “{right}”."),
 'prep': ("wrong preposition", "w", "replace the preposition with a typical SK/CZ calque (in/on/at/to/for)",
   "Zlá predložka: „{right}“, nie „{wrong}“.", "Špatná předložka: „{right}“, ne „{wrong}“.", "Wrong preposition: “{right}”, not “{wrong}”."),
 'prep_extra': ("extra preposition", "w", "insert a preposition English does not use (go to home, enter into)",
   "Tu nepatrí predložka: „{right}“.", "Tady nepatří předložka: „{right}“.", "No preposition here: “{right}”."),
 'natural': ("less natural wording", "c", "grammatical, same meaning, but a clumsy calque (strong headache, on the meadow)",
   "Prirodzenejšie je „{right}“.", "Přirozenější je „{right}“.", "More natural: “{right}”."),
 'word': ("wrong word", "w", "a different word whose meaning does not fit (carry for wear, listen for hear)",
   "Toto slovo tu nesedí: „{right}“, nie „{wrong}“.", "Toto slovo sem nesedí: „{right}“, ne „{wrong}“.", "Wrong word here: “{right}”, not “{wrong}”."),
 'false_friend': ("false friend", "w", "an SK/CZ look-alike word (automat, reklama, control)",
   "Anglické „{wrong}“ znamená niečo iné: „{right}“.", "Anglické „{wrong}“ znamená něco jiného: „{right}“.", "“{wrong}” means something else here: “{right}”."),
 's3': ("missing 3rd person -s", "w", "drop -s/-es from a he/she/it verb",
   "Pri „he/she/it“ chýba -s: „{right}“.", "U „he/she/it“ chybí -s: „{right}“.", "With he/she/it, add -s: “{right}”."),
 's_extra': ("-s with plural subject", "w", "add -s to a verb after I/you/we/they or a plural noun",
   "Tu je sloveso bez -s: „{right}“.", "Tady je sloveso bez -s: „{right}“.", "No -s on the verb here: “{right}”."),
 'plural_miss': ("missing plural -s", "w", "singular noun where the plural is needed (after two, many)",
   "Tu patrí množné číslo: „{right}“.", "Tady patří množné číslo: „{right}“.", "Use the plural here: “{right}”."),
 'plural_extra': ("plural instead of singular", "w", "add -s to a noun that must stay singular (after one, every)",
   "Tu patrí jednotné číslo: „{right}“.", "Tady patří jednotné číslo: „{right}“.", "Use the singular here: “{right}”."),
 'every_pl': ("plural after every", "w", "noun with -s after every/each",
   "Po „every“ je slovo bez -s: „{right}“.", "Po „every“ je slovo bez -s: „{right}“.", "After “every”, no plural: “{right}”."),
 'people_s': ("peoples/childrens", "w", "add -s to people/children/men/women",
   "„{right}“ už je množné číslo, bez -s.", "„{right}“ už je množné číslo, bez -s.", "“{right}” is already plural: no -s."),
 'uncount_pl': ("plural of uncountable noun", "w", "add -s to evidence, information, advice, money, furniture",
   "Toto slovo nemá množné číslo: „{right}“.", "Toto slovo nemá množné číslo: „{right}“.", "This noun has no plural: “{right}”."),
 'adj_s': ("-s on adjective", "w", "add -s to an adjective before a plural noun (olds books)",
   "Prídavné meno nemá -s: „{right}“.", "Přídavné jméno nemá -s: „{right}“.", "Adjectives never take -s: “{right}”."),
 'order': ("word order calque", "w", "keep SK/CZ word order (object first, verb after the place phrase)",
   "Nesprávne poradie slov: „{right}“.", "Nesprávné pořadí slov: „{right}“.", "Wrong word order: “{right}”."),
 'order_tip': ("unusual word order", "c", "understandable but unusual order (time phrase in the middle)",
   "Prirodzenejšie poradie: „{right}“.", "Přirozenější pořadí: „{right}“.", "More natural word order: “{right}”."),
 'subj_miss': ("missing subject", "w", "drop the subject pronoun (SK/CZ pro-drop)",
   "Chýba podmet: „{right}“.", "Chybí podmět: „{right}“.", "The subject is missing: “{right}”."),
 'word_miss': ("missing small word", "w", "drop a needed small word (of, out, on, it, to)",
   "Chýba slovo: „{right}“.", "Chybí slovo: „{right}“.", "A word is missing: “{right}”."),
 'word_extra': ("extra word", "w", "add a word English does not use here (shake their hands, return back)",
   "Slovo navyše, stačí „{right}“.", "Slovo navíc, stačí „{right}“.", "One word too many: just “{right}”."),
 'reflexive': ("reflexive calque", "w", "translate sa/se as himself/herself/itself/you",
   "„sa“ sa tu neprekladá: „{right}“.", "„se“ se tady nepřekládá: „{right}“.", "No reflexive pronoun here: “{right}”."),
 'obj_pron': ("wrong pronoun form", "w", "subject form instead of object form or vice versa (he/him, she/her)",
   "Tu patrí „{right}“, nie „{wrong}“.", "Tady patří „{right}“, ne „{wrong}“.", "Use “{right}” here, not “{wrong}”."),
 'it_thing': ("him/her for a thing", "w", "him/her for an object (SK/CZ grammatical gender)",
   "Vec je v angličtine „it“: „{right}“.", "Věc je v angličtině „it“: „{right}“.", "For a thing, use “it”: “{right}”."),
 'body_poss': ("the with body part", "w", "the instead of my/his/her/its before a body part",
   "Pri časti tela patrí „my/his/her/its“: „{right}“.", "U části těla patří „my/his/her/its“: „{right}“.", "Body parts take “my/his/her/its”: “{right}”."),
 'adj_adv': ("adjective instead of adverb", "w", "adjective where the -ly adverb is needed (slow for slowly)",
   "K slovesu patrí tvar s -ly: „{right}“.", "Ke slovesu patří tvar s -ly: „{right}“.", "With a verb, use the -ly form: “{right}”."),
 'will_time': ("will after if/when/before", "w", "put will into an if/when/before/until clause",
   "Po „if“, „when“, „before“ nepatrí „will“: „{right}“.", "Po „if“, „when“, „before“ nepatří „will“: „{right}“.", "No “will” after if/when/before: “{right}”."),
 'to_modal': ("to after modal", "w", "insert to after can/must/should/will",
   "Po „can/must/should/will“ nepatrí „to“: „{right}“.", "Po „can/must/should/will“ nepatří „to“: „{right}“.", "No “to” after can/must/should/will: “{right}”."),
 'dneg': ("double negative", "w", "two negatives in one clause (don't … nothing, isn't no)",
   "V angličtine stačí jeden zápor: „{right}“.", "V angličtině stačí jeden zápor: „{right}“.", "English uses only one negative: “{right}”."),
 'tense_other': ("wrong tense of another verb", "w", "change the tense of a verb outside the practised span",
   "Toto sloveso je v inom čase: „{right}“.", "Toto sloveso je v jiném čase: „{right}“.", "This verb is in a different tense: “{right}”."),
 'is_for_are': ("is instead of are", "w", "is/was with a plural subject",
   "Pri viacerých patrí „are“: „{right}“, nie „{wrong}“.", "U více lidí či věcí patří „are“: „{right}“, ne „{wrong}“.", "With more than one, use “are”: “{right}”, not “{wrong}”."),
 'are_for_is': ("are instead of is", "w", "are/were with a singular or uncountable subject",
   "Pri jednej veci či osobe patrí „is“: „{right}“, nie „{wrong}“.", "U jedné věci či osoby patří „is“: „{right}“, ne „{wrong}“.", "With one person or thing, use “is”: “{right}”, not “{wrong}”."),
 'much_very': ("much instead of very", "w", "much before a plain adjective (much strong)",
   "Tu patrí „very“, nie „much“: „{right}“.", "Tady patří „very“, ne „much“: „{right}“.", "Use “very” here, not “much”: “{right}”."),
 'have_age': ("have for age", "w", "have/has (got) + years for age (calque of mať rokov)",
   "Vek sa vyjadruje cez „be“: „{right}“.", "Věk se vyjadřuje pomocí „be“: „{right}“.", "Use “be” for age: “{right}”."),
 'missing_there': ("missing there", "w", "start with the place phrase and drop there (On the bench is a bag)",
   "Chýba „there“: „{right}“.", "Chybí „there“: „{right}“.", "“there” is missing: “{right}”."),
 'ago': ("before instead of ago", "w", "calque před/pred + time instead of … ago",
   "„Pred“ + čas sa prekladá „… ago“: „{right}“.", "„Před“ + čas se překládá „… ago“: „{right}“.", "Use “ago” after the time: “{right}”."),
}

def build(t, items):
    info = TOPICS[str(t)]
    out = []
    for n, it in enumerate(items, 1):
        if isinstance(it, str):
            key, _, v = it[2:].partition('/')
            kind, verdict, pattern, sk, cz, en = G[key]
            if v: verdict = v
        else:
            kind, verdict, pattern, sk, cz, en = it
        txt = sk + cz + en
        slots = [s for s in ('right', 'wrong') if '{%s}' % s in txt]
        slots += [s for s in dict.fromkeys(re.findall(r'\{(\w+)\}', txt)) if s not in slots]
        out.append({"id": f"{t}.{n:02d}", "kind": kind,
                    "verdict": "wrong" if verdict == 'w' else "correct_with_tip",
                    "pattern": pattern, "slots": slots, "sk": sk, "cz": cz, "en": en})
    d = {"type_id": t, "topic": info['topic'], "level": info['level'], "items": out}
    with open(f"{BASE}/mistakes/{t}.json", 'w') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
    return len(out)

You are the blind writer for a measurement of a translation checker.

You see ONLY the Slovak sentence, its CEFR level and its topic. You do NOT see any English
reference translation and you do NOT see any annotation. Do not ask for them; they do not exist
for you. Write from the Slovak alone.

For EACH sentence below, write exactly 3 CORRECT English translations and exactly 3 WRONG
English translations.

ACCEPTANCE RULES (these are the owner's rules, verbatim, and they are the only
rules that decide):
- the Slovak sentence is the ground truth, not the English reference;
- a passive is acceptable;
- a dropped agent where the Slovak names one is WRONG;
- a missing obligatory English article is an ERROR;
- the time frame must match the Slovak while the English tense inside that frame is free;
- a dropped function word is correct, a dropped content word is wrong, added content is wrong.

CORRECT answers must be acceptable under those rules, and the three should differ from each other
(different wording, a passive, a different but time-frame-preserving tense, a dropped function
word, and so on) - not three copies of one sentence.

WRONG answers must be wrong under those rules, and each must be wrong for ONE identifiable reason.
Give each wrong answer a type:
  T = the time frame does not match the Slovak (tense inside a matching frame is NOT an error)
  S = the subject/agent is wrong, or an agent the Slovak names is dropped
  M = something the Slovak says is missing in the English - a dropped CONTENT word, or a missing
      obligatory English article
  W = wrong word choice, changed meaning, or added content the Slovak does not have
Make the wrong answers plausible near-misses, not gibberish: a whole-sentence mistranslation
teaches nothing. Keep everything else about the sentence right.

Give every answer a tag from exactly this list:
plain, determiner, aspect, number, by-passive, by-passive-embedded, skp-passive, drop-main, drop-fronted, drop-misaligned, drop-other, time-frame, missing-article
Use "plain" when nothing more specific fits; "missing-article" for a missing obligatory article;
"time-frame" for a wrong time frame; "drop-main" / "drop-fronted" / "drop-misaligned" /
"drop-other" for a dropped agent; "by-passive" / "by-passive-embedded" for an English by-passive;
"determiner" / "aspect" / "number" for those differences.

Write ONE file, writers/writer_part3.json, and nothing else. Exact JSON shape:
[
 {"sid": 220001,
  "correct": [{"answer": "...", "tag": "plain"}, {"answer": "...", "tag": "by-passive"},
              {"answer": "...", "tag": "plain"}],
  "wrong":   [{"answer": "...", "tag": "time-frame", "type": "T"},
              {"answer": "...", "tag": "drop-main", "type": "S"},
              {"answer": "...", "tag": "missing-article", "type": "M"}]},
 ...
]
One object per sentence, all 15 sentences, in the order given. No commentary, no markdown fence
inside the file - the file must parse as JSON.

THE SENTENCES:
- sid 220031 | level A1 | topic: Singular and plural
  Slovak: Pri ľade kráčajú ďalšie dva tučniaky
- sid 220032 | level B1 | topic: Present Perfect Continuous
  Slovak: Stíhačkový hriankovač ohrieva tie isté dva krajce už tri minúty.
- sid 220033 | level B2 | topic: All Past Tenses
  Slovak: Do obeda odovzdalo 200 voličov svoje volebné lístky, výrazne pred termínom.
- sid 220034 | level A1 | topic: HAVE GOT
  Slovak: On má sivú handričku na čistenie auta.
- sid 220035 | level A1 | topic: This, That, These...
  Slovak: Tieto konzervy vyletujú z jeho papierovej tašky.
- sid 220036 | level B1 | topic: Passive or Active
  Slovak: On kladie slaninu vedľa vajíčka do čiernej panvice.
- sid 220037 | level A2 | topic: Countable and uncountable
  Slovak: Katastrofa! Ona nemá čas na dlhú návštevu!
- sid 220038 | level B1 | topic: Present Perfect Continuous
  Slovak: Už päť minút hľadá gumičku do vlasov a na zápästí má tri.
- sid 220039 | level B2 | topic: Future Perfect Continuous
  Slovak: O šiestej už bude búchať do tých lap dve hodiny v kuse.
- sid 220040 | level A1 | topic: A, AN, THE
  Slovak: Žena mu na krk zavesí jednu zlatú medailu.
- sid 220041 | level A2 | topic: Basic conjunctions
  Slovak: Kámo, dvere sú už otvorené, tak odhaľujú celé údolie, fakt.
- sid 220042 | level A2 | topic: Past Simple
  Slovak: On spal. Preto nič videl.
- sid 220043 | level A1 | topic: HAVE GOT
  Slovak: Trénerka má obväz a bielu pásku.
- sid 220044 | level B2 | topic: All Past Tenses
  Slovak: Kým došiel k úzkemu chodníku, on zliezal hodinu dolu po skalných rímsach.
- sid 220045 | level A1 | topic: Singular and plural
  Slovak: Jedna košeľa, jeden golier a dve červené kravaty.

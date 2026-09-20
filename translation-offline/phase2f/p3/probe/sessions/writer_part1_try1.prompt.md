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

Write ONE file, writers/writer_part1.json, and nothing else. Exact JSON shape:
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
- sid 220001 | level A1 | topic: Prepositions of place/time
  Slovak: Špinavú dlážku čistí v pondelok ráno. Absolútna katastrofa!
- sid 220002 | level B2 | topic: Modals in past
  Slovak: Kámoška, povedal mi, že ten ľadovec bol obrovský; musel sa tam cítiť taký maličký.
- sid 220003 | level B1 | topic: Present Perfect Continuous
  Slovak: Model stíhačky opeká chlieb približne tri minúty.
- sid 220004 | level B1 | topic: Question tags
  Slovak: Ten most preklenuje celý desivý kaňon, však?
- sid 220005 | level B1 | topic: Modal verbs Probability
  Slovak: Ten strážnik o syre nemôže vedieť — rampu dvíha príliš rýchlo.
- sid 220006 | level A1 | topic: TO BE
  Slovak: Útok je rýchly a hlasný na zelenom poli.
- sid 220007 | level A1 | topic: Prepositions of place/time
  Slovak: Stojí bosý na teplom piesku.
- sid 220008 | level A2 | topic: Adjective comparison
  Slovak: Nebudem klamať, letíš vysoko, dokonca vyššie než borovice.
- sid 220009 | level A2 | topic: Modal verb SHOULD
  Slovak: Stroj by si mal tlačiť veľmi pomaly.
- sid 220010 | level A2 | topic: There is, are
  Slovak: Na dunách je len jedna ťava.
- sid 220011 | level B1 | topic: Future Continuous
  Slovak: Úprimne, dúha možno vybledne, ale zajtra v tomto čase budeš ukazovať svoje video všetkým.
- sid 220012 | level A2 | topic: Present or Past Simple
  Slovak: Správa: oni zvyčajne dávajú pohľadnice, ale včera jej oni dali 12 darčekov.
- sid 220013 | level B2 | topic: All Past Tenses
  Slovak: Ponorka sa pohybovala pod hladinou istý čas, kým ju plavci spozorovali.
- sid 220014 | level A1 | topic: Singular and plural
  Slovak: Dvaja kamaráti potrebujú dva hrebene
- sid 220015 | level B1 | topic: Gerund vs Infinitive
  Slovak: Stále ukladal ďalšie knihy na kopu, kým sa nezakývala.

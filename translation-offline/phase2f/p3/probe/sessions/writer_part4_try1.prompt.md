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

Write ONE file, writers/writer_part4.json, and nothing else. Exact JSON shape:
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
- sid 220046 | level A2 | topic: Much, Many, Some...
  Slovak: Takže mi povedal, že v meste nejazdí veľkou rýchlosťou.
- sid 220047 | level A1 | topic: Singular and plural
  Slovak: Fakt, tvoje dve baterky pekne osvetľujú tú tmavú rímsu.
- sid 220048 | level B1 | topic: Past Perfect Simple
  Slovak: Nebudem klamať, bol si ten najšarmantnejší úradník; ona sa nikdy predtým tak neusmievala.
- sid 220049 | level A2 | topic: Future BE GOING TO
  Slovak: Ryby majú plán. Idú uplávať preč od žraloka.
- sid 220050 | level B1 | topic: Past Simple or Continuos
  Slovak: V momente, keď barla dopadla na mokrú podlahu, chytil ju pevne a šiel ďalej.
- sid 220051 | level B1 | topic: Present Perfect Continuous
  Slovak: Približne štyridsať študentov žiada o členstvo na klubovom veľtrhu od obeda.
- sid 220052 | level B2 | topic: All Present Tenses
  Slovak: Aktualizácia stavu: skriňa zostala uprataná 3 týždne po sebe.
- sid 220053 | level B1 | topic: So, Neither, Nor
  Slovak: Pamätník zbožňoval, a samozrejme aj jeho fotoaparát.
- sid 220054 | level B1 | topic: Passive or Active
  Slovak: Stupne víťazov boli postavené zo žineniek asi za minútu.
- sid 220055 | level B2 | topic: Articles advanced
  Slovak: Napíše svoje meno na poslednú stranu zmluvy na novú prácu a kancelária tlieska.
- sid 220056 | level A1 | topic: This, That, These...
  Slovak: Táto váha ukazuje oveľa viac ako pred chvíľou.
- sid 220057 | level B2 | topic: Causative HAVE/GET
  Slovak: Potrebuje si dať starý akordeón opraviť, kým klávesy úplne neprestanú fungovať.
- sid 220058 | level A2 | topic: Present or Past Simple
  Slovak: Ty zvyčajne nenávidíš rady, ale včera večer si čakala na záchod. Rešpekt.
- sid 220059 | level A1 | topic: Modal verb CAN
  Slovak: Mäkká guma môže vyčistiť celú stranu.
- sid 220060 | level B2 | topic: Modals in past
  Slovak: Mal si skontrolovať kolíky pred tým zápasom - dva sa uvoľnili už v prvých desiatich minútach.

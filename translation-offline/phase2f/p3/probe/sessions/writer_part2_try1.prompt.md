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

Write ONE file, writers/writer_part2.json, and nothing else. Exact JSON shape:
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
- sid 220016 | level B1 | topic: Past Perfect Simple
  Slovak: Kým spustil kanvicu, všetci, čo zízali na jeho fúzy, úplne stíchli!
- sid 220017 | level A2 | topic: Adjective comparison
  Slovak: Táto ceruzka je ostrejšia ako tá tupá.
- sid 220018 | level B2 | topic: All Present Tenses
  Slovak: Vraj sa rúti dolu tou riekou každé leto, kamoška.
- sid 220019 | level A2 | topic: Modal verb SHOULD
  Slovak: Ten hmyz je drobný, tak ona by mala skúmať ho lupou.
- sid 220020 | level B1 | topic: Present Perfect Continuous
  Slovak: Muž obdivuje svoje luxusné auto už dvadsať minút.
- sid 220021 | level A1 | topic: Modal verb CAN
  Slovak: Hore je vietor. Môžeš vidieť tú vlajku?
- sid 220022 | level A2 | topic: Adjective comparison
  Slovak: Úprimne, dnes si hlasnejší než celý národný tím.
- sid 220023 | level A2 | topic: Basic conjunctions
  Slovak: Počúvaj, povedala, že majú rovnaké šaty, ale sú stále kamarátky.
- sid 220024 | level B2 | topic: All Future Tenses
  Slovak: Do porady o 9:00 sa zotaví z takého vyčerpania.
- sid 220025 | level B2 | topic: Reported speech
  Slovak: Poprosila ma, aby som nehýbal rukou, kým spí.
- sid 220026 | level B2 | topic: All Present Tenses
  Slovak: Kdeže, gekón práve teraz chrlí oheň, lebo papričky sú také pálivé.
- sid 220027 | level A2 | topic: Going to or Will
  Slovak: Vločky sú v miske – hneď ich zje
- sid 220028 | level B2 | topic: Causative HAVE/GET
  Slovak: Pred vhadzovaním si dala omotať hokejku páskou.
- sid 220029 | level B2 | topic: Reported speech
  Slovak: Kamarát tvrdil, že sa ho celý večer nikto nedotkol.
- sid 220030 | level A1 | topic: A, AN, THE
  Slovak: Fanúšik má jednu pomaľovanú tvár a šálu.

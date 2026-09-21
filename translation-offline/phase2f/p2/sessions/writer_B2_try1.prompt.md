# Phase 2F Part 2 - writer spec (level B2)

You are a blind writer.  You see ONLY a list of Czech sentences, each with its CEFR level and its
grammar topic.  You never see an English reference translation and you never see any annotation.
Write, for each Czech sentence, NINE English answers: four that a careful teacher would mark
CORRECT and five that the same teacher would mark WRONG.

## The acceptance rules the judge will use (write to these, they are the owner's words)
the Czech sentence is the ground truth, not the English reference; a passive is acceptable; a
dropped agent where the Czech names one is WRONG; a missing obligatory English article is an
ERROR; the time frame must match the Czech while the English tense inside that frame is free; a
dropped function word is correct, a dropped content word is wrong, added content is wrong.

## The nine slots
c1  a plain faithful translation.                                   tags ["plain"]
c2  c1 with ONE determiner changed (a/an/the/this/that/my/...), still correct.
                                                                    tags ["determiner"]
c3  If the Czech names a doer: an English passive that KEEPS that doer in a by-phrase.
                                                                    tags ["by-passive"]
    If the Czech names no doer (it is impersonal, reflexive-passive or agentless): an English
    passive with no by-phrase.                                      tags ["skp-passive"]
c4  a fluent paraphrase that is still the same sentence.            tags ["paraphrase"]
w1  If the Czech names a doer: c1 with that doer DROPPED (turn it into an agentless passive or
    delete the subject).  type "M".                                 tags ["drop-main"]
    If the Czech names no doer: a time-frame shift.  type "T".      tags ["time-frame"]
w2  as w1, a DIFFERENT wording of the same error.                   same type and tags as w1
w3  a time-frame shift (past/present/future changed against the Czech).  type "T"
                                                                    tags ["time-frame"]
w4  c1 with an obligatory English article removed.  type "S"        tags ["missing-article"]
w5  one content word replaced by a wrong one.  type "W"             tags ["wrong-word"]

Every wrong answer carries exactly one of the types "T" (time frame), "W" (wrong word),
"M" (missing agent), "S" (slip).  Correct answers carry type null.  Tags must come from this list
and the exact strings matter, the floor check counts them:
plain, determiner, aspect, paraphrase, by-passive, skp-passive, drop-fronted, drop-misaligned, drop-main, drop-other, time-frame, missing-article, agreement, preposition, word-order, wrong-word

## Output
Write the file /Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2f/p2/set/writers/writer_B2.json - a JSON list, one object per sentence, in the order given:

[{"sid": 210001,
  "answers": {"c1": {"en": "...", "type": null, "tags": ["plain"]},
              "c2": {"en": "...", "type": null, "tags": ["determiner"]},
              "c3": {"en": "...", "type": null, "tags": ["by-passive"]},
              "c4": {"en": "...", "type": null, "tags": ["paraphrase"]},
              "w1": {"en": "...", "type": "M", "tags": ["drop-main"]},
              "w2": {"en": "...", "type": "M", "tags": ["drop-main"]},
              "w3": {"en": "...", "type": "T", "tags": ["time-frame"]},
              "w4": {"en": "...", "type": "S", "tags": ["missing-article"]},
              "w5": {"en": "...", "type": "W", "tags": ["wrong-word"]}}}, ...]

No prose outside the file.  Reply in <= 6 lines with the counts you wrote.

## Your sentences
- sid 210076 | level B2 | topic: 3. Conditional
  Kdyby se té police nebyl dotkl, džbán by byl ještě celý.
- sid 210077 | level B2 | topic: Modals in past
  Brácho, to štěně mělo počkat o chvilku dýl, ale trpělivost není jeho vibe, fakt.
- sid 210078 | level B2 | topic: Wish clauses
  Přála by si, aby zlato vypadalo naživo tak jasně jako na kameře.
- sid 210079 | level B2 | topic: Causative HAVE/GET
  Musela si dokument nechat orazítkovat, než úřad zavřel.
- sid 210080 | level B2 | topic: 3. Conditional
  Kdyby kočka použila jen strojek, vršek by nebyl tak plochý.
- sid 210081 | level B2 | topic: Wish clauses
  Přeje si, aby se nit netrhala tak často.
- sid 210082 | level B2 | topic: Wish clauses
  V polovině schodů si přála, aby radši použila výtah.
- sid 210083 | level B2 | topic: Future Perfect Continuous
  Do šesti budou toho průvodce nosit pět hodin.
- sid 210084 | level B2 | topic: Future Perfect Simple
  Noční můra! Do poledne já přečtu každý časopis v téhle čekárně.
- sid 210085 | level B2 | topic: Advanced linkers
  Zkouší se s kartičkami, aby si u zkoušky dokázal vybavit odpovědi.
- sid 210086 | level B2 | topic: Future Perfect Simple
  Do večera obrousí všechny budky v dílně, jinak je konec!
- sid 210087 | level B2 | topic: Future Perfect Simple
  Do konce léta přeplave každé jezero v tomhle údolí.
- sid 210088 | level B2 | topic: Causative HAVE/GET
  Firma si druhý den dala záběry zkontrolovat meteorologem.
- sid 210089 | level B2 | topic: Past Perfect Continuous
  Na tom nástupišti čekala hodinu, než to vzdala a sedla si.
- sid 210090 | level B2 | topic: All Present Tenses
  Podívej se na něj teď - utírá si obličej čistým bílým ručníkem.
- sid 210091 | level B2 | topic: 3. Conditional
  Kdyby nebyl vlezl tím oknem, nebyl by spadl.
- sid 210092 | level B2 | topic: All Past Tenses
  Ona doufala dlouho, než klíček konečně vyrostl.
- sid 210093 | level B2 | topic: Inversion basic
  Nikdy neviděl ve své kuchyni tak naprostý neúspěch.
- sid 210094 | level B2 | topic: Relative clauses
  Boxerka, jejíž rukavice jsou jasně červené, se při závěrečném gongu směje.
- sid 210095 | level B2 | topic: Advanced linkers
  V důsledku třicetinásobného točení na židli nestihl termín.
- sid 210096 | level B2 | topic: All Present Tenses
  Podívej se hned teď na obzor - slunce svítí přesně mezi dvěma paneláky.
- sid 210097 | level B2 | topic: Relative clauses
  Stadion, jehož sedadla byla úplně plná, se rozléhal jásotem rodin.
- sid 210098 | level B2 | topic: Causative HAVE/GET
  Chce si nechat dovézt víc nití do pátku.
- sid 210099 | level B2 | topic: Future Perfect Continuous
  Do září budou hrávat tuhle hru v té zahradě dva roky.
- sid 210100 | level B2 | topic: Relative clauses
  Gauč, který přesunula po podlaze, je teď otočený k oknu.

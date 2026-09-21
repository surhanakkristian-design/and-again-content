# Phase 2F Part 2 - writer spec (level A1)

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
Write the file /Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2f/p2/set/writers/writer_A1.json - a JSON list, one object per sentence, in the order given:

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
- sid 210001 | level A1 | topic: A, AN, THE
  Rukou zastaví ten točící se globus.
- sid 210002 | level A1 | topic: My, Your, His,...
  Křičí a jeho prst má přímo u jejího obličeje.
- sid 210003 | level A1 | topic: Present Simple
  On sedí na dlouhé dřevěné lavičce v parku.
- sid 210004 | level A1 | topic: My, Your, His,...
  Rybář ji učí svoje vlastní slova.
- sid 210005 | level A1 | topic: Modal verb CAN
  Dokážeš projít mezi lany taky?
- sid 210006 | level A1 | topic: My, Your, His,...
  Namáčí chleba do svého oblíbeného olivového oleje.
- sid 210007 | level A1 | topic: Wh- questions
  Kdo to je? Studentka v červeném baretu.
- sid 210008 | level A1 | topic: Present Simple
  Jeden pohled a odborník ničí sen celé rodiny!
- sid 210009 | level A1 | topic: Modal verb CAN
  Pět set studentů může sedět v této přednáškové síni.
- sid 210010 | level A1 | topic: My, Your, His,...
  Ona píše svůj plán do diáře.
- sid 210011 | level A1 | topic: Singular and plural
  Mraky skrývají silnice a města dole.
- sid 210012 | level A1 | topic: Modal verb CAN
  S klíčem ona může odemknout zámek.
- sid 210013 | level A1 | topic: Prepositions of place/time
  Dóza s pudrem stojí na malém stolku.
- sid 210014 | level A1 | topic: TO BE
  Dvě obrovské řady jsou na protilehlých stranách a nikdo nepřechází!
- sid 210015 | level A1 | topic: This, That, These...
  Tyhle sušenky na plechu voní úžasně.
- sid 210016 | level A1 | topic: HAVE GOT
  Slon má dva dlouhé bílé kly.
- sid 210017 | level A1 | topic: A, AN, THE
  Termín pátek: potřebujeme fotku modrého moře.
- sid 210018 | level A1 | topic: Present Simple
  Před každým plaváním si nandá brýle.
- sid 210019 | level A1 | topic: This, That, These...
  Tyhle duny v poušti jsou velmi vysoké.
- sid 210020 | level A1 | topic: Cardinal numbers
  Žirafa pije se dvěma předníma nohama od sebe.
- sid 210021 | level A1 | topic: TO BE
  Nebe nad mraky je úplně zlaté.
- sid 210022 | level A1 | topic: This, That, These...
  Tenhle polibek je na jeho tváři, takže je to polibek na tvář.
- sid 210023 | level A1 | topic: Singular and plural
  V tomhle malém holičství pracují dva holiči
- sid 210024 | level A1 | topic: My, Your, His,...
  Položí si svou ruku na hruď a dýchá.
- sid 210025 | level A1 | topic: Prepositions of place/time
  Majitelka je v své kavárně, takže není mimo ni.

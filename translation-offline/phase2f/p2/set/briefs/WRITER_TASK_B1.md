# Phase 2F Part 2 - writer spec (level B1)

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
Write the file /Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2f/p2/set/writers/writer_B1.json - a JSON list, one object per sentence, in the order given:

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
- sid 210051 | level B1 | topic: Reported speech
  Křičela, že někdo posunul kompas a výlet je zničený!
- sid 210052 | level B1 | topic: Present Perfect Simple or Continuos
  Jsou promočení a bez dechu, protože se od svítání prodírali nahoru tím hřebenem.
- sid 210053 | level B1 | topic: 1. Conditional
  Když ten lavor teď překlopí, všechna mýdlová voda skončí v záhonu.
- sid 210054 | level B1 | topic: 1. Conditional
  Když zamává dost silně, přeletí celou zátoku, aniž by se dotkl vody.
- sid 210055 | level B1 | topic: Question tags
  „Dobrá hygiena není těžká, že jo?“ říká s palcem nahoře.
- sid 210056 | level B1 | topic: Passive
  Koule byla hozena skoro patnáct metrů do pole.
- sid 210057 | level B1 | topic: 2. Conditional
  Kdyby se muži v kanduře nelíbily návrhy, dnes by nebyla žádná dohoda.
- sid 210058 | level B1 | topic: 1. Conditional
  Když na ten krajíc natře ještě víc másla, rozpadne se.
- sid 210059 | level B1 | topic: Reported speech
  Takže, řekla mi, že se rozbrečela, protože A+ nestačilo.
- sid 210060 | level B1 | topic: Passive
  Všechno odmítnuté oblečení je věšeno zpátky na ramínka prodavačkou.
- sid 210061 | level B1 | topic: Modal verbs Probability
  Nervózní nemůže být — koukni, jak má na pultu klidné ruce.
- sid 210062 | level B1 | topic: Passive
  Poslední místo na ulici bylo obsazeno malinkým modrým autem! Naprosto neuvěřitelné!
- sid 210063 | level B1 | topic: Question tags
  Její styl je porazil, že?
- sid 210064 | level B1 | topic: Past Perfect Simple
  Než se dostala k přepážce, na ovoce v kufru už úplně zapomněla
- sid 210065 | level B1 | topic: 1. Conditional
  Když půjdeš ještě blíž, kočky seskočí z kvádru.
- sid 210066 | level B1 | topic: Used to, Would
  Každé léto jejího dětství babička právala košile na tomhle dvoře.
- sid 210067 | level B1 | topic: 2. Conditional
  Kdyby byla poleva kyselá, její jazyk by zůstal v puse.
- sid 210068 | level B1 | topic: Past Simple or Continuos
  Pustil se kamenného stropu, roztáhl křídla a dvakrát mávl, aby se udržel ve vzduchu.
- sid 210069 | level B1 | topic: Past Simple or Continuos
  Zatímco se knihy nahoře kývaly, šel chodbou.
- sid 210070 | level B1 | topic: Used to, Would
  Tenhle přechod býval součástí jejího 20minutového dojíždění, než se oddělení přestěhovalo.
- sid 210071 | level B1 | topic: 1. Conditional
  Když kostky ujedou, všechny tři skončí na žíněnce.
- sid 210072 | level B1 | topic: Future Continuous
  Zítra touhle dobou bude mít na sobě ten zlatý odstín na pódiu, pod opravdovými světly.
- sid 210073 | level B1 | topic: Past Continuous
  Zatímco ostatní cestující čekali ve frontě, ona už kráčela nástupním mostem.
- sid 210074 | level B1 | topic: Past Simple or Continuos
  Tiše vzdychala, když autobus zastavil na červenou.
- sid 210075 | level B1 | topic: 0 Conditional
  Když dýcháš zhluboka, tvoje plíce nabírají víc vzduchu.

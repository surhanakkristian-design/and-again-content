# Phase 2F Part 2 - writer spec (level A2)

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
Write the file /Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2f/p2/set/writers/writer_A2.json - a JSON list, one object per sentence, in the order given:

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
- sid 210026 | level A2 | topic: There is, are
  Na stole je jedna velká paletka.
- sid 210027 | level A2 | topic: Countable and uncountable
  Vole, jeden výkřik nadělá fakt hodně hluku.
- sid 210028 | level A2 | topic: Must, Have to...
  Pravidlo oslavy: každý musí dát dárek, protože dárek je na dávání.
- sid 210029 | level A2 | topic: Past Simple
  Včera krabici taky zavázala provázkem.
- sid 210030 | level A2 | topic: Present Continuous
  Velmi chytré, samozřejmě. Právě teď on má na hlavě v sauně kožešinovou čepici.
- sid 210031 | level A2 | topic: Past Simple
  Včera ostříhala tu samou ovci.
- sid 210032 | level A2 | topic: Countable and uncountable
  Nepotřebuješ hodně vody na špinavou podlahu. Klobouk dolů.
- sid 210033 | level A2 | topic: Adverb formation
  Hořáky zapaluje velmi rychle
- sid 210034 | level A2 | topic: Basic conjunctions
  Nahráváš to znovu, protože první záběr je špatný? Klobouk dolů.
- sid 210035 | level A2 | topic: Present or Past Simple
  Dneska kašle míň, ale včera kašlala hodně.
- sid 210036 | level A2 | topic: Basic conjunctions
  Hele, snažil se zavřít bránu, ale zámek se zasekl.
- sid 210037 | level A2 | topic: Present or Past Simple
  Chodí sem každý podzim, ale včera přišli pozdě.
- sid 210038 | level A2 | topic: Present Continuous
  Podívej! Právě si češe vlasy kartáčem.
- sid 210039 | level A2 | topic: Basic conjunctions
  Hračka se naklání, ale nespadne.
- sid 210040 | level A2 | topic: Adverb formation
  Z mlhy se vrátil najednou
- sid 210041 | level A2 | topic: Present Continuous or Simple
  Normálně jen čte, ale dnes sbírá důkazy. Vole, šílený.
- sid 210042 | level A2 | topic: Present or Past Simple
  Dokonalé. On se obvykle balí nalehko, ale včera nesl těžkou věž.
- sid 210043 | level A2 | topic: Much, Many, Some...
  Kolik prázdných židlí je v místnosti?
- sid 210044 | level A2 | topic: Present Continuous or Simple
  Obvykle pracuje v posteli, ale dneska sedí u stolu.
- sid 210045 | level A2 | topic: Must, Have to...
  Branka je hrozně těžká. Musíte ji nést spolu!
- sid 210046 | level A2 | topic: Going to or Will
  Ona míří puškou na terč. Ona se chystá vystřelit.
- sid 210047 | level A2 | topic: Adverb formation
  Zeleninu úhledně naskládal na bílý talíř.
- sid 210048 | level A2 | topic: Present Continuous
  Podívej! Právě teď mu podává kolík.
- sid 210049 | level A2 | topic: There is, are
  Nade dveřmi je jedna malá kamera.
- sid 210050 | level A2 | topic: Basic conjunctions
  Tvoje kuchyně je levná, ale tvoje jídlo vypadá úžasně. Respekt.

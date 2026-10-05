from gen_7288_7290_7291_7292_lib import write
owl=[(.34,.46,.40,.14),(.30,.41,.44,.17),(.30,.37,.48,.18),(.32,.36,.56,.19),(.35,.36,.50,.18),(.51,.37,.24,.20),(.53,.36,.22,.20),(.54,.36,.22,.20)]
lig=[(.35,.25,.30,.21),(.36,.26,.28,.15),(.36,.23,.28,.14),(.36,.55,.24,.14),None,None,None,None]
F="female"
write(7290,"B","library",F,
 [("to swoop through the library","the barn owl",F,owl),
  ("to perch on the ladder","the barn owl",F,owl),
  ("to flash behind the window","the lightning",F,lig)],
 3.7,[("a barn owl",.65,.46,F),("a ladder",.62,.80,F),("a rose window",.47,.25,F),("bookshelves",.15,.45,F)],
 "What is the barn owl doing?","The owl is swooping through the library.",F,
 "Only one moving target, so the owl takes two phrases. Lightning box is split off above (or below at 1.7) the flying owl, so it covers only part of the bolt; lightning is gone from 2.2 s (off). Key word 'library' is the whole scene, used in phrase + answer rather than as a pill.")

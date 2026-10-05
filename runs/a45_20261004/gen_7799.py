from gen_7796_7797_7798_7799_lib import write
W=[(.48,.34,.43,.53),(.44,.35,.46,.53),(.41,.34,.49,.53),(.40,.34,.49,.55),(.49,.34,.31,.56),(.55,.34,.29,.56),(.54,.34,.29,.55),(.54,.34,.29,.54)]
M=[(.17,.31,.22,.25),(.18,.31,.22,.25),(.19,.31,.21,.25),(.20,.31,.19,.25),(.21,.31,.22,.25),(.22,.31,.22,.25),(.22,.31,.22,.25),(.22,.31,.22,.25)]
write(7799,"B","democracy","female",
 [("to count the raised hands","the woman in red","female",W),
  ("to scribble on a clipboard","the woman in red","female",W),
  ("to stand with folded arms","the man in white","male",M)],
 3.7,
 [("an arched window",.61,.28,"female"),("bunting",.80,.36,"female"),("a clipboard",.68,.50,"female"),("a parquet floor",.45,.93,"female")],
 "What is the woman in red doing?","She is counting the raised hands.","female",
 "Woman in a dark red jumper used twice (seated people all raise hands, so no unique third person besides the man). She points/counts 0.2-1.7, writes 2.2-3.7. Her pointing hand nearly touches the man's box at 1.7 (split at x .39/.40).")

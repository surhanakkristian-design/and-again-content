from gen_7796_7797_7798_7799_lib import write
O=[(0,.69,.27,.29),(0,.69,.25,.29),(0,.64,.22,.34),(0,.62,.22,.34),(0,.61,.25,.28),(0,.60,.29,.27),(0,.60,.30,.28),(0,.59,.31,.29)]
B=[(.08,.35,.26,.34),(.18,.37,.20,.32),(.22,.42,.18,.30),(.22,.43,.18,.28),(.25,.43,.18,.27),(.29,.44,.18,.27),(.30,.44,.18,.26),(.31,.44,.18,.27)]
Y=[(.60,.39,.28,.29),(.60,.46,.26,.27),(.59,.50,.27,.23),(.59,.53,.31,.20),(.57,.55,.31,.17),(.57,.55,.29,.16),(.59,.54,.26,.16),(.57,.53,.27,.17)]
write(7797,"B","decline","male",
 [("to kneel by the blower","the man in orange","male",O),
  ("to clutch his head","the man in blue","male",B),
  ("to end up sitting down","the woman in yellow","female",Y)],
 3.7,
 [("a food truck",.12,.50,"male"),("tents",.85,.47,"male"),("a bouncy castle",.75,.70,"male"),("an air blower",.38,.80,"male")],
 "What is happening to the bouncy castle?","The bouncy castle is deflating.","male",
 "Mixed group, defaultVoice male (evenId false). Castle not used as tap target (its box would cover the jumpers). Man in blue clutches his head mainly 0.2-1.7. Orange/blue boxes split at their feet/head where they touch (0.2-0.7 split in y, later in x).")

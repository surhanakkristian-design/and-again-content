from w_7378_7379_7381_7382_lib import write
wom = [(.42,.38,.79,.76),(.43,.39,.79,.76),(.46,.42,.79,.77),(.49,.44,.82,.78),(.54,.47,.84,.78),(.53,.50,.82,.79),(.54,.56,.83,.80),(.54,.54,.82,.81)]
fl  = [(.20,.40,.41,.79),(.19,.26,.42,.80),(.05,.03,.45,.81),(.16,0,.48,.82),(.18,0,.52,.84),(.17,0,.52,.85),(.18,0,.53,.87),(.20,0,.53,.87)]
write(7382, "B", "natural gas", "female",
 [("to kneel on the ice", "the woman in red", "female", wom),
  ("to throw her head back", "the woman in red", "female", wom),
  ("to shoot into the sky", "the flame", "female", fl)],
 0.7,
 [("a flame", .32, .50, "female"), ("a wooden cabin", .84, .39, "female"), ("a gas cylinder", .86, .62, "female"), ("frozen bubbles", .70, .88, "female")],
 "What is the woman in red doing?", "She is kneeling on the dark ice.", "female",
 "key word 'natural gas' not placed as a noun (the gas itself is invisible); the two people behind both take photos, so they are not used and the woman carries two phrases; flame box clipped at the woman's hand where they meet")

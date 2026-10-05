from gen_7102_7110_7111_7116_lib import write
ff = [(.41,.31,.18,.15),(.41,.33,.18,.15),(.41,.36,.18,.14),(.41,.37,.18,.15),(.41,.40,.18,.14),(.42,.40,.18,.13),None,None]
eng = [(.40,.54,.40,.20),(.39,.54,.40,.19),(.40,.53,.35,.20),(.35,.52,.35,.22),(.28,.54,.38,.21),(.22,.54,.43,.22),(.28,.50,.44,.28),(.31,.48,.67,.32)]
bc = [(.49,.23),(.49,.23),(.50,.22),(.49,.22),(.50,.24),(.49,.24),(.50,.25),(.49,.25)]
bell = [(x-.10, y-.07, .20, .14) for x, y in bc]
write(7116, "B", "fire station", "female", [
  ("to slide down a brass pole", "the firefighter in the window", "female", ff),
  ("to pull out of the station", "the fire engine in the middle", "female", eng),
  ("to hang in the bell tower", "the bell", "female", bell)],
  0.2, [("a fire station", .22, .42, "female"), ("a bell", .50, .23, "female"), ("the sky", .80, .08, "female"), ("snow", .50, .85, "female")],
  "What is the fire engine doing?", "It is pulling out of the fire station.", "female",
  "firefighter on the pole is tiny, gender unclear -> defaultVoice; firefighter off at 3.2/3.7 (hidden behind the engine); bell phrase is a state")

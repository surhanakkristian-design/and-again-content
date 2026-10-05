from gen_7777_7778_7779_7780_lib import write
W = [(.33,0,.65,.81),(.30,0,.60,.82),(.31,.05,.54,.80),(.34,.19,.48,.70),(.38,.27,.45,.63),(.41,.32,.42,.60),(.43,.36,.41,.57),(.45,.37,.39,.56)]
C = [(.12,.08,.21,.35),(.12,.10,.17,.35),(.13,.22,.17,.30),(.16,.26,.17,.32),(.19,.30,.18,.32),(.21,.33,.19,.30),(.23,.34,.19,.30),(.24,.35,.20,.30)]
write(7778, "B", "climate change", "female",
  [("to pull on her gloves", "the woman", "female", W),
   ("to spray a cloud of mist", "the snow cannon", "female", C),
   ("to stand on muddy skis", "the woman", "female", W)],
  2.2, [("a glacier", .33, .23, "female"), ("a snow cannon", .29, .44, "female"), ("a wooden hut", .12, .55, "female"), ("a puddle", .70, .92, "female")],
  "What is the woman doing?", "She is pulling on her gloves.", "female",
  "Opening frames (0.2-0.7) show only her body from below the chin, skis lying in mud; she clearly stands on skis from 1.2. Snow-cannon box includes its pole and the start of the mist plume; the plume drifts behind the woman. Key word 'climate change' is abstract, not used as a noun.")

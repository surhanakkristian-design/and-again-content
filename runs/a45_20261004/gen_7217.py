from gen_7217_7218_7219_7220_lib import build
cook = [(0.0,0.20,0.47,0.48),(0.0,0.20,0.47,0.48),(0.02,0.21,0.46,0.47),(0.02,0.21,0.46,0.47),
        (0.0,0.19,0.46,0.49),(0.0,0.19,0.44,0.49),(0.0,0.19,0.39,0.51),(0.06,0.19,0.31,0.53)]
man = [(0.47,0.33,0.40,0.29),(0.47,0.33,0.40,0.29),(0.48,0.33,0.39,0.29),(0.48,0.33,0.39,0.29),
       (0.46,0.31,0.42,0.30),(0.44,0.31,0.44,0.30),(0.39,0.32,0.47,0.30),(0.37,0.32,0.49,0.30)]
build(7217, "B", "help", "female",
 [("to scoop rice onto a plate", "the woman in the apron", "female", cook),
  ("to lean over the table", "the woman in the apron", "female", cook),
  ("to hold up both palms", "the man in the striped shirt", "male", man)],
 0.2,
 [("an apron", 0.22, 0.56, "female"), ("a paella pan", 0.58, 0.68, "female"), ("a water jug", 0.37, 0.84, "female")],
 "What is the standing woman doing?", "She is serving him a generous portion.", "female",
 "Cook and man boxes split vertically between them (her serving arm/spoon crosses into the man's half at 0.2-2.2). The woman on the right also raises a hand briefly around 2.7, but the man holds up both palms throughout. Key word help (verb) not used in the answer; alternative 'She is helping him to more rice.'")

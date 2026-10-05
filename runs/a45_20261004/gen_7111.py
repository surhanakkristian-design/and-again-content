from gen_7102_7110_7111_7116_lib import write
red = [(.17,.25,.57,.57),(.13,.25,.60,.58),(.12,.26,.58,.68),(.13,.26,.57,.68),(.11,.25,.57,.58),(.09,.24,.57,.58),(.07,.22,.50,.60),(.07,.22,.49,.60)]
ref = [None,(.82,.37,.18,.30),(.78,.35,.22,.34),(.71,.34,.25,.35),(.69,.33,.25,.36),(.66,.33,.25,.37),(.62,.33,.26,.37),(.59,.33,.26,.37)]
write(7111, "A", "fighter", "female", [
  ("to throw a punch", "the woman in red", "female", red),
  ("to wear red shorts", "the woman in red", "female", red),
  ("to walk around the ring", "the referee", "male", ref)],
  3.2, [("a fighter", .32, .40, "female"), ("a referee", .74, .44, "male"), ("people", .88, .56, "female"), ("water", .46, .88, "female")],
  "What is the referee doing?", "He is walking around the ring.", "male",
  "opponent in blue left out as a target: she is mostly cut off at the right edge and overlaps the referee at 1.2 s; referee off at 0.2 (hidden), only partly visible at 0.7 behind the opponent")

from lib_w_7137_7138_7140_7141 import write
front = [(.40,.25,.53,.46),(.40,.24,.58,.48),(.40,.23,.53,.48),(.46,.22,.54,.50),(.50,.24,.50,.49),(.48,.24,.52,.48),(.44,.24,.56,.51),(.52,.23,.48,.51)]
woman = [(0,.33,.14,.55),(0,.33,.14,.55),(0,.33,.15,.56),(0,.33,.13,.56),(0,.30,.11,.60),(0,.30,.12,.60),(0,.30,.12,.62),(0,.30,.17,.62)]
desk = [(.14,.37,.24,.25),(.14,.37,.24,.25),(.15,.36,.23,.27),(.13,.37,.25,.26),(.11,.35,.24,.26),(.12,.35,.23,.27),(.12,.34,.26,.30),(.17,.35,.25,.30)]
write(7141, "A", "frame", "male", [
  ("to try on glasses", "the man at the counter", "male", front),
  ("to laugh at his glasses", "the woman", "female", woman),
  ("to work at a desk", "the man at the desk", "male", desk)],
  2.7, [("frames", .78, .12, "male"), ("a window", .12, .15, "male"), ("a cupboard", .39, .33, "male"), ("a counter", .45, .66, "male")],
  "What is the woman doing?", "She is laughing at his glasses.", "female",
  "woman and the man at the desk overlap in the picture: woman box is cut at the line between them (narrow, left edge); both men wear white coats, named by place")

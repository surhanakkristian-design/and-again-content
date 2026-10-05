from gen_6944_6945_6946_6947_lib import write
W = [(0,.32,.54,.82),(0,.32,.54,.82),(0,.32,.54,.88),(0,.30,.55,.84),(0,.28,.55,.90),(0,.27,.55,.92),(0,.26,.55,1),(0,.25,.57,1)]
M = [(.56,.38,1,.82),(.57,.38,1,.82),(.57,.38,1,.86),(.58,.38,1,.88),(.57,.37,1,.92),(.58,.36,1,.92),(.59,.36,1,1),(.59,.35,1,1)]
write(6944, "A", "charge your phone", "female",
 [("to charge her phone", "the woman", "female", W),
  ("to smile at the camera", "the woman", "female", W),
  ("to close his eyes", "the man", "male", M)],
 0.2,
 [("a woman", .20, .62, "female"), ("a man", .74, .60, "male"), ("a cup", .28, .86, "female"), ("a pillow", .70, .89, "female")],
 "What is the woman doing?", "She is charging her phone.", "female",
 "Man also holds a phone (and one lies on the floor), so phone not used as a noun; woman used for two phrases.")

from gen_7365_7367_7368_7370_lib import write
W = [[.20,.31,.40,.90],[.21,.30,.40,.90],[.19,.30,.40,.92],[.20,.30,.40,.92],[.26,.24,.51,.62],[.18,.15,.59,.44],[.26,.29,.48,.56],[.16,.30,.42,.97]]
M = [[.40,.27,.88,.60],[.40,.27,.93,.60],[.40,.26,.76,.60],[.40,.26,.75,.62],[.51,.26,.71,.62],[.59,.22,.82,.44],[.48,.26,.75,.56],[.42,.23,.80,.64]]
D = [[.43,.60,.77,1.0],[.42,.60,.94,1.0],[.42,.60,.90,1.0],[.40,.62,.92,1.0],[.30,.62,.87,1.0],[.32,.44,.84,.97],[.33,.56,.68,1.0],[.42,.64,.74,1.0]]
write(7368, "A", "mommy", "female",
  [("to kiss his cheek", "the woman", "female", W),
   ("to drop his big bag", "the man", "male", M),
   ("to jump up at them", "the dog", "female", D)],
  0.2,
  [("a window", .16, .17, "female"), ("a lamp", .87, .24, "female"), ("a bag", .78, .48, "female"), ("a dog", .58, .82, "female")],
  "What is the woman doing?", "She is kissing his cheek.", "female",
  "woman and man hug, so their boxes are split along the line between them (man's face partly in the woman's box at 0.2-1.2); man and woman boxes cut above the dog where the dog stands in front of their legs; at 2.7 only upper bodies boxed")

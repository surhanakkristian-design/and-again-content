from gen_8045_8046_8047_8048_lib import write
W = [(.31,.18,.58,.68),(.28,.22,.43,.65),(.30,.25,.43,.65),(.30,.31,.42,.67),(.32,.30,.57,.54),(.31,.27,.69,.57),(.33,.30,.38,.59),(.36,.32,.33,.57)]
write(8045, "A", "winter", "female",
 [("to throw snow", "the woman", "female", W),
  ("to wear a red hat", "the woman", "female", W),
  ("to hold a shovel", "the woman", "female", W)],
 2.2,
 [("trees", .80, .12, "female"), ("a hat", .55, .36, "female"), ("a shovel", .70, .78, "female"), ("snow", .20, .90, "female")],
 "What is the woman doing?", "She is throwing snow with a shovel.", "female",
 "Only one person, so all three phrases use the woman (box includes the shovel she holds). Key word 'winter' is tagged verb and is not a placeable noun; not used.")

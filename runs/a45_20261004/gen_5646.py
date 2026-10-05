from gen_5644_5645_5646_5647_lib import write
man = [(.65,.35,.28,.61)]*8
wom = [(.05,.43,.60,.40)]*8
lan = [(.22,.07,.20,.22)]*8
write(5646, "B", "belonging", "female",
 [("to embrace her from behind", "the man", "male", man),
  ("to lean back against him", "the woman", "female", wom),
  ("to glow above the couple", "the lantern", "female", lan)],
 2.2,
 [("a lantern", .32, .18, "female"), ("palm trees", .55, .30, "female"), ("a kingfisher", .17, .51, "female"), ("a cushion", .25, .62, "female")],
 "What is the man doing?", "He is embracing her from behind.", "male",
 "Couple overlaps: boxes split at x=.65 (woman left incl. legs, man right incl. his leg). Static camera, same boxes every frame. Kingfisher only used as a noun. Key word 'belonging' abstract.")

from gen_7365_7367_7368_7370_lib import write
G = [[0,.12,1.0,.50]]*8
M = [[.30,.50,.88,.88],[.30,.50,.95,.89],[.35,.50,.88,.90],[.30,.50,.80,.90],[.28,.50,.76,.89],[.32,.50,.85,.88],[.29,.50,.75,.88],[.25,.50,.68,.88]]
T = "the man in the red helmet"
write(7370, "B", "move back", "male",
  [("to paddle for his life", T, "male", M),
   ("to grip his paddle tightly", T, "male", M),
   ("to crash into the sea", "the glacier", "male", G)],
  2.2,
  [("a glacier", .55, .30, "male"), ("spray", .30, .44, "male"), ("a helmet", .55, .54, "male"), ("a kayak", .57, .84, "male")],
  "What is the man in front doing?", "He is paddling away from the glacier.", "male",
  "only two real targets: the man (2 phrases) and the glacier; other kayakers are far back and all paddle alike; glacier box stops at y .50 above the man's helmet, so the raised paddle blade is outside both boxes in some frames")

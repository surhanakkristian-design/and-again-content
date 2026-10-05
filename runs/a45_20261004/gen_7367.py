from gen_7365_7367_7368_7370_lib import write
W = [[0,.17,.57,.63],[0,.17,.57,.63],[0,.15,.58,.63],[0,.14,.58,.63],[0,.10,.58,.63]]
F = [[.58,.33,.80,.47],[.58,.33,.81,.47],[.61,.31,.84,.45],[.82,.32,1.0,.47],[.64,.33,.97,.49]]
C = [[.31,.63,.60,.80],[.32,.63,.61,.80],[.30,.63,.60,.80],[.32,.65,.61,.81],[.29,.65,.60,.83]]
write(7367, "B", "molly", "female",
  [("to purse her lips", "the woman", "female", W),
   ("to approach the glass", "the black fish", "female", F),
   ("to doze on the sofa", "the cat", "female", C)],
  0.2,
  [("a molly", .68, .40, "female"), ("an aquarium", .80, .18, "female"), ("driftwood", .86, .55, "female"), ("a fish net", .56, .81, "female")],
  "What is the woman doing?", "She is pursing her lips like a fish.", "female",
  "woman's box stops at y .63 so the sleeping cat below her hair gets its own box; black fish swims away right at 1.7 then back, 'to approach the glass' is weakest - check")

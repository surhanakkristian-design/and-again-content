from gen_7878_7879_7881_7882_lib import write
M = [(.02,.23,.54,.69),(.02,.24,.57,.70),(.02,.23,.56,.70),(.02,.24,.57,.70),(.00,.24,.57,.72),(.01,.25,.57,.70),(.00,.24,.59,.73),(.01,.24,.60,.72)]
W = [(.58,.40,.32,.16),(.60,.41,.32,.16),(.62,.42,.30,.16),(.62,.42,.30,.16),(.63,.41,.32,.17),(.63,.42,.33,.16),(.63,.43,.33,.16),(.64,.42,.33,.17)]
C = [(.02,.09,.22,.14),(.02,.10,.20,.14),(.02,.09,.20,.14),(.02,.10,.21,.14),(.02,.10,.29,.14),(.01,.10,.34,.15),(.03,.07,.38,.17),(.04,.07,.40,.17)]
write(7879, "A", "inch", "male",
 [("to touch the wall", "the man", "male", M),
  ("to cover her mouth", "the woman", "female", W),
  ("to walk on the wall", "the cat", "male", C)],
 0.2,
 [("a cat", .13, .21, "male"), ("a lamp", .76, .12, "male"), ("flowers", .64, .34, "male"), ("a car", .72, .80, "male")],
 "What is the woman doing?", "She is covering her mouth.", "female",
 "The cat walks along the wall top toward the man; its box ends where the man's box starts (his head top is cut a little at 1.7-3.7, the cat's lowered head a little at 3.2-3.7). The man presses his hand on the wall the whole clip. Woman box = her face/body seen through the windscreen. The cat also stands on the wall, but 'to touch the wall' is about the man's hand.")

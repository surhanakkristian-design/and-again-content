from gen_6925_6926_6927_6928_lib import build
W = [(.40,.04,.80,.58),(.48,.24,.82,.59),(.44,.24,.78,.57),(.41,.23,.74,.57),(.40,.23,.78,.54),(.39,.23,.76,.52),(.38,.24,.68,.50),(.37,.24,.72,.47)]
H = [(.64,.59,1,1),(.66,.60,1,1),(.63,.58,1,1),(.62,.58,1,1),(.58,.55,1,1),(.55,.53,1,1),(.50,.51,1,1),(.50,.48,1,1)]
D = [(0,.46,.16,.70),(0,.48,.17,.72),(0,.48,.16,.72),(0,.49,.18,.73),(0,.52,.15,.77),(.01,.51,.19,.77),(0,.53,.19,.85),(.01,.54,.21,.85)]
build(6925, "B", "cart", "female",
 [("to catch a heavy watermelon", "the woman", "female", W),
  ("to pull a wooden cart", "the horse", "female", H),
  ("to trot behind the cart", "the dog", "female", D)],
 2.2,
 [("watermelons", .30, .30, "female"), ("a straw hat", .76, .45, "female"), ("a cart", .24, .55, "female"), ("a horse", .80, .76, "female")],
 "What is the horse doing?", "It is pulling a wooden cart.", "female",
 "Catch only at 0.2-0.7 s (melon in the air at 0.2). Woman box stops above the horse (her lower legs sit beside the horse's back, boxes split horizontally). Horse box starts below her lap. Waving farm workers far back not used.")

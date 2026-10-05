from gen_6925_6926_6927_6928_lib import build
G = [(.53,.27,.77,.71),(.46,.27,.70,.71),(.40,.27,.65,.70),(.37,.27,.61,.70),(.32,.27,.55,.72),(.28,.27,.50,.74),(.24,.27,.48,.72),(.22,.28,.42,.72)]
C = [(.87,.21,1,.77),(.80,.21,1,.72),(.73,.21,1,.72),(.79,.21,1,.72),(.78,.22,1,.72),(.79,.22,1,.72),(.75,.23,1,.72),(.73,.23,1,.75)]
T = [None,None,None,(.68,.27,.79,.68),(.58,.24,.78,.72),(.52,.23,.79,.72),(.49,.23,.75,.72),(.42,.22,.72,.72)]
build(6928, "B", "casino", "male",
 [("to laugh behind her hand", "the woman in green", "female", G),
  ("to hold a long rake", "the croupier", "female", C),
  ("to wear a black tuxedo", "the man in the tuxedo", "male", T)],
 2.7,
 [("a card table", .14, .50, "male"), ("a wheelbarrow", .55, .61, "male"), ("a roulette wheel", .74, .82, "male")],
 "What is the woman in green doing?", "She is laughing behind her hand.", "female",
 "Camera arcs right. Croupier only a sliver at the right edge at 0.2 s. Man in the tuxedo hidden behind the croupier until 1.2 s (off), only a narrow strip at 1.7 s; his box is split from the croupier's along her left shoulder, so his right shoulder and her rake hand are cut a little. Velvet-jacket man with cards not used. 'Casino' is the whole place, so no noun pill for the key word; two chandeliers, so no chandelier noun.")

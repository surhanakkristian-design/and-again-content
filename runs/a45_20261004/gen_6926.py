from gen_6925_6926_6927_6928_lib import build
W = [(.10,.25,.66,.73),(.09,.24,.68,.75),(.10,.23,.68,.75),(.10,.23,.72,.75),(.10,.22,.70,.77),(.04,.21,.75,.77),(.12,.21,.73,.78),(.13,.20,.74,.80)]
S = [(.68,.30,.88,.46),(.70,.30,.90,.46),(.69,.30,.88,.46),(.73,.29,.92,.45),(.73,.29,.92,.45),(.77,.29,.96,.45),(.74,.29,.95,.46),(.75,.29,.95,.46)]
build(6926, "B", "case", "female",
 [("to unfold a grey drone", "the woman", "female", W),
  ("to shut a hard case", "the woman", "female", W),
  ("to shovel snow", "the man with the shovel", "male", S)],
 2.2,
 [("a tent", .12, .37, "female"), ("a drone", .52, .55, "female"), ("a sled", .86, .64, "female"), ("a case", .60, .82, "female")],
 "What is the woman doing?", "She is unfolding a grey drone.", "female",
 "Shut the case: 0.7-1.7 s. Woman box excludes her arm reaching to the lid (0.7-1.2) and the drone's rotor tips (2.7-3.7) so it never overlaps the small shoveller box. The man in the tent entrance is not used (posture unclear). Two orange cases: 'a case' sits on the big front one, 'a sled' on the sled carrying the second case.")

from gen_8045_8046_8047_8048_lib import write
WO = [(.11,.27,.54,.49),(.29,.33,.41,.45),(.39,.26,.37,.56),(.39,.24,.32,.61),(.38,.22,.30,.65),(.34,.21,.35,.70),(.36,.21,.35,.77),(.39,.19,.38,.81)]
MA = [(.65,.21,.35,.53),(.70,.20,.30,.55),(.76,.20,.24,.58),(.71,.18,.29,.62),(.68,.16,.32,.66),(.69,.14,.31,.72),(.71,.15,.29,.77),(.77,.34,.23,.66)]
write(8048, "B", "hesitate", "female",
 [("to stare down into the gorge", "the woman in lilac", "female", WO),
  ("to steady her with his hand", "the man", "male", MA),
  ("to lean over the edge", "the woman in lilac", "female", WO)],
 2.2,
 [("a beanie", .90, .21, "female"), ("a railing", .14, .47, "female"), ("a harness", .56, .56, "female"), ("a bungee cord", .48, .88, "female")],
 "What is the woman in lilac doing?", "She is hesitating at the edge of the platform.", "female",
 "The two friends behind the railing stand right behind the man's outstretched arm, so they were not used as targets (boxes would overlap). 'to lean over the edge' is clearest at 0.2-0.7; after that she stands upright at the edge. The man's head leaves the frame at 3.7 (only his arm and legs at the right edge). Woman/man boxes split at his hand on her back (x~0.65-0.77).")

from gen_7242_7243_7244_7245_lib import write
w = [(0,0,.48,.89),(0,.13,.60,.77),(0,.25,.56,.75),(0,.24,.58,.76),(0,.14,.64,.86),(0,.11,.76,.89),(0,.07,.76,.93),(0,.06,.79,.94)]
write(7243, "B", "impact", "female",
 [("to peer into the crater", "the woman", "female", w),
  ("to crouch on a cracked slab", "the woman", "female", w),
  ("to pick up a rock fragment", "the woman", "female", w)],
 2.2,
 [("the sky", .60, .10, "female"), ("a crater", .78, .36, "female"), ("smoke", .48, .48, "female"), ("a boulder", .62, .82, "female")],
 "What is the woman doing?", "She is examining a rock fragment.", "female",
 "Only one person; the rising smoke overlaps her outline early on, so all three phrases use the woman. Peers down 0.2-1.7 s, crouches from 0.7 s, picks up the fragment about 1.2-2.2 s, examines it 2.7-3.7 s. 'a boulder' = the big cracked slab in front of her. Key word 'impact' is abstract, not placed.")

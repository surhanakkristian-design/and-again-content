from gen_8019_8020_8021_8023_lib import build
woman = [(.50,.30,.36,.68),(.51,.30,.38,.68),(.51,.30,.38,.68),(.52,.30,.37,.68),(.52,.30,.37,.68),(.53,.30,.38,.68),(.53,.30,.39,.68),(.55,.30,.38,.68)]
man = [(.06,.31,.32,.44)]*8
build(8019, 'A', 'take your time', 'female',
 [('to take a photo', 'the woman', 'female', woman),
  ('to touch her hair', 'the woman', 'female', woman),
  ('to fold his arms', 'the man in blue', 'male', man)],
 2.2,
 [('a phone', .66, .42, 'female'), ('a rope', .55, .80, 'female'), ('a bench', .30, .89, 'female')],
 'What is the woman doing?', 'She is taking a photo with her phone.', 'female',
 'Woman takes a selfie the whole clip; she touches her hair only from 2.2 s. Man in blue box includes his shoulder bag. The two men moving mats were not used (they overlap). Rope pill on the rope coil on the bench, right of the chalk bag.')

from gen_7103_7104_7105_7106_lib import write
w = [[0,.34,.64,.66],[0,.34,.62,.66],[0,.33,.62,.67],[0,.34,.61,.66],[0,.31,.62,.69],[0,.31,.65,.69],[0,.33,.65,.67],[0,.32,.62,.68]]
h = [None,[.63,.52,.37,.29],[.63,.52,.37,.36],[.62,.51,.38,.36],[.63,.51,.37,.32],[.66,.52,.34,.30],[.66,.58,.34,.25],[.63,.55,.37,.32]]
d = [[.74,.28,.26,.18],[.76,.28,.24,.18],[.76,.31,.24,.18],[.76,.30,.24,.18],[.78,.29,.22,.17],[.80,.28,.20,.18],[.80,.31,.20,.17],[.81,.31,.19,.17]]
write(7105, "B", "feature", "female",
  [("to tilt her chin upwards", "the model", "female", w),
   ("to apply gold leaf", "the hand with the brush", "female", h),
   ("to blow flakes into the air", "the hairdryer", "female", d)],
  2.2,
  [("a gown", .62, .08, "female"), ("a clothes rail", .20, .22, "female"), ("a hairdryer", .86, .36, "female"), ("a make-up brush", .78, .55, "female")],
  "What is the model doing?", "She is tilting her chin upwards.", "female",
  "Brush hand absent at 0.2 s (only a hand holding the gold palette at the bottom right) -> off. At 3.2-3.7 s the hand presses the lips with a finger while holding the brush. Gold flakes from the dryer are small; the dryer itself is clearly visible throughout.")

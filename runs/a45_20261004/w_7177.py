from w_7176_7177_7178_7182_lib import write
w = [(.17,.30,.87,.80),(.12,.30,.87,.83),(.11,.31,.81,.85),(.08,.30,.81,.82),(.10,.31,.76,.89),(.10,.34,.76,.91),(.12,.33,.76,.85),(.11,.32,.77,.81)]
write(7177, "B", "go down", "female",
 [("to abseil down a cliff", "the woman", "female", w),
  ("to grip the rope", "the woman", "female", w),
  ("to push against the rock", "the woman", "female", w)],
 3.7,
 [("a helmet", .40, .38, "female"), ("a waterfall", .68, .24, "female"), ("a cliff", .88, .55, "female"), ("a pool", .45, .86, "female")],
 "What is the woman doing?", "She is abseiling down a cliff.", "female",
 "Only one possible target, so all three phrases use the woman. 'push against the rock' = her boots pressed on the wall. The pool at the bottom only becomes visible from about 2.7; 'a pool' pill on the brown water left of the rocks.")

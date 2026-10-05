from gen_7777_7778_7779_7780_lib import write
W = [(0,.54,.54,.30),(0,.54,.53,.29),(0,.54,.55,.32),(0,.54,.56,.33),(0,.56,.56,.30),(0,.58,.60,.33),(0,.54,.69,.38),(0,.49,.79,.44)]
M = [(.38,.16,.41,.38),(.38,.16,.43,.38),(.38,.16,.44,.38),(.38,.15,.51,.39),(.38,.15,.48,.40),(.36,.14,.48,.43),(.36,.13,.52,.40),(.36,.12,.50,.36)]
B = [(.80,.37,.20,.17),(.82,.37,.18,.17),(.83,.37,.17,.17),(.78,.64,.22,.18),(.76,.76,.23,.16),(.73,.78,.25,.16),(.75,.80,.24,.15),(.80,.80,.20,.15)]
write(7779, "B", "close off", "female",
  [("to reach under the sink", "the woman", "female", W),
   ("to catch water in a saucepan", "the man", "male", M),
   ("to tumble onto the floor", "the plastic bowl", "female", B)],
  2.7, [("a lampshade", .17, .18, "female"), ("a window", .15, .32, "female"), ("a saucepan", .72, .36, "female"), ("a plastic bowl", .85, .86, "female")],
  "What is the man holding?", "He is holding a saucepan over the sink.", "male",
  "Man's legs stand behind the woman: man box = his upper body down to about y .54, woman box below it, so his legs/feet are not in his box. Bowl sits by the sink at 0.2-1.2 (saucepan rim cut at x .80-.83 to keep clear), falls at 1.7, lies on the floor from 2.2. The valve itself is not clearly visible, hence 'reach under the sink'. Key word 'close off' is a verb, not a noun.")

from w_7378_7379_7381_7382_lib import write
wom = [(.47,.29,.93,.87),(.47,.30,.94,.87),(.43,.32,.90,.87),(.47,.32,.97,.87),(.58,.30,1,.87),(.55,.29,.98,.87),(.47,.29,.90,.87),(.49,.30,.95,.88)]
rd  = [(0,.45,.46,.86),(0,.50,.46,.86),(0,.51,.42,.88),(0,.49,.42,.91),(0,.43,.42,.89),(0,.47,.44,.85),(0,.42,.46,.84),(0,.46,.48,.84)]
tent= [(.03,.18,.36,.37),(.05,.18,.36,.37),(.05,.19,.39,.37),(.05,.19,.37,.37),(.06,.18,.39,.37),(.05,.18,.38,.37),(.03,.19,.36,.37),(.02,.19,.35,.37)]
write(7381, "B", "native", "female",
 [("to tug on a lasso", "the young woman", "female", wom),
  ("to get dragged along", "the front reindeer", "female", rd),
  ("to glow with firelight", "the tent", "female", tent)],
 2.2,
 [("a reindeer", .18, .62, "female"), ("a canvas tent", .23, .29, "female"), ("birch trees", .60, .18, "female"), ("a lasso", .67, .54, "female")],
 "What is the young woman doing?", "She is dragging a reindeer through the snow.", "female",
 "key word 'native' (a person) not placed as a noun: nothing in the picture shows who is native, labelling the woman would be guessing; person in orange at the gate is tiny, not used; woman's outstretched arm/hand clipped where it crosses the reindeer box")

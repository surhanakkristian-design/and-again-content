from gen_7878_7879_7881_7882_lib import write
W = [(.17,.31,.35,.65),(.16,.31,.39,.68),(.12,.31,.43,.69),(.12,.31,.44,.69),(.07,.28,.48,.72),(.05,.28,.50,.72),(.01,.27,.48,.73),(.01,.27,.49,.73)]
M = [(.52,.31,.31,.64),(.55,.31,.31,.68),(.55,.31,.33,.69),(.56,.31,.36,.69),(.55,.28,.38,.72),(.55,.28,.43,.72),(.50,.27,.48,.73),(.52,.27,.45,.73)]
C = [(0,.04,.76,.27),(0,.03,.78,.28),(0,.06,.79,.25),(0,.06,.81,.25),(0,0,.80,.28),(0,0,.92,.28),(0,.01,.85,.26),(0,.01,.86,.26)]
write(7878, "B", "in other words", "female",
 [("to hold up a worn part", "the woman", "female", W),
  ("to scratch his head", "the man", "male", M),
  ("to be missing a wheel", "the car", "female", C)],
 1.2,
 [("a vintage car", .30, .17, "female"), ("a tool chest", .43, .60, "female"), ("tyres", .86, .63, "female"), ("a mechanic", .25, .76, "female")],
 "What is the man doing?", "He is scratching his head in confusion.", "male",
 "Woman and man boxes split around x .52-.56 where her phone/hands meet his arm. Car box only covers the body above the people (cut at their head tops); the wheel hub below hangs between their heads. 'a mechanic' pill on the woman's overalls. Woman holds the part next to her phone until 2.7, then lowers the phone.")

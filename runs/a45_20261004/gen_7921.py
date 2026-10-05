from gen_7917_7919_7920_7921_lib import build
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
dog=[(.22,.36,.33,.14),(.20,.39,.29,.11),(.27,.40,.29,.13),(.31,.39,.26,.15),(.31,.36,.26,.18),(.31,.34,.26,.21),(.30,.33,.27,.25),(.32,.33,.28,.26)]
per=[(.00,.50,.76,.50),(.00,.50,.78,.50),(.00,.53,.79,.47),(.00,.54,.81,.46),(.00,.54,.85,.46),(.00,.55,.88,.45),(.00,.58,.89,.42),(.00,.59,.82,.41)]
build(7921,"A","of course","male",T,[
 ("to roll in the mud","the dog","male",dog),
 ("to shake its wet fur","the dog","male",dog),
 ("to hold a big towel","the person","male",per)],
 3.2,[("a house",.65,.13,"male"),("a dog",.42,.47,"male"),("a towel",.18,.80,"male"),("a bucket",.90,.66,"male")],
 "What is the dog doing?","The dog is rolling in the mud.","male",
 "Only the person's arms/hands are visible (gender unclear, so default voice). Dog rolls 0.7-1.2, shakes 2.2-2.7; in the frames it looks almost white again at the end, not brown as the description says. The 'bucket' is a metal tub at the right edge. At 3.7 the towel has dropped out of view; the person box covers the hands/arm.")

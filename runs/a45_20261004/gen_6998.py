from gen_6997_6998_6999_7000_lib import build
pl=[.37,.31,.26,.24,.23,.22,.22,.21]
pale=[(.37,.48,.42,.26),(.31,.48,.45,.27),(.26,.49,.49,.27),(.24,.50,.46,.29),(.23,.48,.40,.32),(.22,.48,.37,.34),(.22,.48,.34,.34),(.21,.48,.36,.35)]
calf=[(.79,.54,.18,.18),(.76,.55,.18,.18),(.75,.57,.19,.19),(.70,.58,.21,.20),(.63,.59,.29,.22),(.59,.60,.33,.23),(.56,.60,.34,.23),(.57,.61,.35,.26)]
spot=[(.03,.41,round(p-.03,2),.18) for p in pl]
build(6998,"B","cows","female",[
 ("to lead a dark calf","the pale cow","female",pale),
 ("to trot beside the pale cow","the calf","female",calf),
 ("to rest on a striped towel","the spotted cow","female",spot)],
 0.7,[("a parasol",.13,.36,"female"),("a beach bar",.25,.27,"female"),("cows",.62,.40,"female"),("a calf",.84,.63,"female")],
 "What is the pale cow doing?","It is leading a dark calf through the surf.","female",
 "From 1.7 the calf walks in front of the pale cow's back legs: boxes split vertically, the pale cow's rump is left out of both boxes. Spotted cow box ends where the pale cow's head starts. 'to lead' = the pale cow walks ahead with the calf at first, later side by side.")

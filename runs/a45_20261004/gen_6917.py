from gen_6916_6917_6918_6919_lib import write
ship=[(.26,.05,.48,.63),(.25,.05,.48,.64),(.22,.05,.52,.65),(.23,.05,.51,.65),(.20,.03,.52,.65),(.19,.02,.53,.66),(.21,.03,.51,.66),(.21,.04,.53,.64)]
man=[(.42,.68,.29,.21),(.53,.69,.21,.19),(.54,.70,.20,.19),(.56,.70,.20,.19),(.56,.68,.18,.18),(.56,.68,.18,.17),(.55,.69,.19,.18),(.55,.68,.19,.18)]
waves=[(.72,.69,.28,.24),(.75,.66,.25,.30),(.76,.66,.24,.32),(.77,.60,.23,.38),(.75,.55,.25,.30),(.75,.58,.25,.25),(.75,.60,.25,.28),(.75,.66,.25,.28)]
write(6917,"B","call at","male",[
 ("to sail into the harbour","the sailing ship","male",ship),
 ("to throw a coil of rope","the man near the lighthouse","male",man),
 ("to crash over the harbour wall","the waves","male",waves)],
 0.2,[("a sailing ship",.48,.32,"male"),("a lighthouse",.80,.44,"male"),("fishing boats",.15,.57,"male"),("a harbour wall",.78,.93,"male")],
 "What is the sailing ship doing?","It is calling at a small harbour.","male",
 "Answer uses the key word 'call at' (the ship coming into port). The thrower is 'the man near the lighthouse'; a bearded man in the foreground (2.2-3.7) catches and hauls in the coil, so no rope phrase is given to him and he is not a target. Waves: box on the spray at the right-hand wall; there is also spray left of the bow, not boxed (it is behind the ship box). Man boxes are small and pushed against the ship box bottom.")

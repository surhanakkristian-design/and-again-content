from gen_7874_7875_7876_7877_lib import build
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
man=[(.05,.51,.50,.91),(.19,.56,.56,.88),(.22,.61,.63,.88),(.26,.58,.81,.90),(.21,.58,.86,.91),(.19,.59,.87,.91),(.19,.59,.83,.92),(.19,.59,.85,.92)]
rig=[(.23,.16,.76,.35),(.22,.17,.75,.34),(.17,.19,.74,.37),(.14,.19,.77,.37),(.16,.19,.76,.37),(.14,.19,.71,.37),(.15,.20,.76,.37),(.20,.21,.76,.38)]
crane=[(r[2]+.01,0,1,.57) for r in rig]
build(7875,"B","in advance","male",[
 ("to spread out a blanket","the man","male",man),
 ("to lift a lighting rig","the crane","male",crane),
 ("to dangle from a hook","the lighting rig","male",rig)],
 2.7,[("a crane",.83,.22,"male"),("a stage",.66,.44,"male"),("a folding chair",.20,.71,"male"),("a tartan blanket",.55,.87,"male")],
 "What is the man doing?","He is sitting on a tartan blanket.","male",
 "spreading the blanket only 0.2-1.2 s, then he sits on it; crane box starts right of the rig so the boom tip is cut at the top",T)

from gen_7064_7065_7066_7068_lib import write
drake=[(.20,.19,.70,.49),(.21,.18,.70,.46),(.35,.17,.68,.45),(.36,.16,.67,.45),(.36,.16,.66,.45),(.37,.16,.65,.46),(.38,.16,.65,.47),(.37,.18,.65,.48)]
hen=[(.01,.75,.36,.95),(.02,.76,.38,.96),(.03,.75,.40,.96),(.05,.75,.42,.96),(.08,.76,.44,.98),(.11,.77,.47,.98),(.15,.78,.48,1.0),(.16,.79,.51,1.0)]
write(7065,"B","drake","male",[
 ("to land on the statue's arm","the drake on the statue","male",drake),
 ("to fold its wings","the drake on the statue","male",drake),
 ("to gaze up from the water","the brown duck","male",hen)],
 3.2,[("a drake",.51,.33,"male"),("a church tower",.85,.22,"male"),("a bakery",.17,.57,"male"),("a statue",.60,.50,"male")],
 "Where is the drake sitting?","It is perching on the statue's arm.","male",
 "evenId false -> male default. A second green-headed drake floats on the right (small); the tap target is named 'the drake on the statue' and phrases fit only him (landing, folding wings). Brown duck = female mallard looking up. Noun 'a drake' sits on the perched drake; the other drake on the right is small and away from the pill.")

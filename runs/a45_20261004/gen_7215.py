from mk_7214_7215_7216_7219 import write
W=[(.35,.31,.35,.38),(.35,.30,.35,.38),(.35,.29,.36,.40),(.34,.29,.40,.43),(.30,.27,.45,.46),(.30,.26,.46,.46),(.28,.24,.47,.49),(.28,.22,.47,.51)]
M=[(.17,.26,.18,.32),(.16,.25,.19,.35),(.15,.25,.20,.34),(.14,.24,.20,.32),(.09,.24,.21,.36),(.11,.18,.19,.44),(.04,.10,.24,.52),(.03,.07,.25,.54)]
write(7215,"B","heir","female",[
 ("to cover her mouth in shock","the red-haired woman","female",W),
 ("to lift a ring of keys","the red-haired woman","female",W),
 ("to rise from his chair","the man getting up","male",M)],
 0.2,[("a grandfather clock",.43,.21,"female"),("law books",.12,.10,"female"),("keys",.42,.72,"female"),("a wax seal",.73,.86,"female")],
 "What is the red-haired woman doing?","She is staring at a ring of keys.","female",
 "The man getting up sits right behind the woman's left shoulder: boxes split at about x .27-.33, so her left elbow/hand is partly outside her box. He rises at 2.7-3.7. The old lawyer (foreground left) is not a target.")

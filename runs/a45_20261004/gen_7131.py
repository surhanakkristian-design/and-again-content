from gen_7131_7132_7134_7136_lib import write
pool=[None,None,(.62,0,.32,.14),(.60,0,.38,.24),(.60,.03,.36,.30),(.60,.10,.34,.27),(.58,.15,.34,.31),(.59,.17,.33,.30)]
cake=[(.34,.23,.18,.20),(.34,.31,.18,.21),(.34,.43,.18,.22),(.34,.53,.18,.22),(.34,.61,.18,.22),(.34,.68,.18,.21),(.34,.71,.18,.23),(.34,.73,.18,.24)]
bride=[(.15,.24,.18,.17),(.14,.32,.18,.18),(.14,.44,.18,.20),(.13,.54,.18,.17),(.13,.62,.18,.17),(.12,.68,.18,.16),(.13,.74,.19,.22),(.14,.74,.19,.22)]
write(7131,"A","fool","male",[
 ("to stand in a pool","the man in the pool","male",pool),
 ("to carry a big cake","the man with the cake","male",cake),
 ("to wear a white dress","the bride","female",bride)],
 3.2,[("a pool",.75,.46,"male"),("a flamingo",.74,.30,"male"),("a cake",.42,.76,"male"),("a bride",.22,.88,"female")],
 "Who is standing in a pool?","A man is standing in a blue pool.","male",
 "Pool man only partly in frame at 1.2 (legs at top edge), off at 0.2/0.7. 'a flamingo' labels the pink flamingo swim ring. Bride phrase is a state (her actions are shared with other guests).")

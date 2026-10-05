from gen_7917_7919_7920_7921_lib import build
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
stick=[(.69,.33,.31,.25),(.67,.33,.33,.25),(.67,.34,.33,.24),(.67,.34,.33,.24),(.67,.34,.33,.24),(.67,.34,.33,.24),(.64,.34,.36,.24),(.64,.34,.36,.24)]
vest=[(.42,.27,.24,.24),(.42,.27,.24,.24),(.42,.28,.24,.23),(.42,.28,.24,.23),(.43,.28,.23,.23),(.43,.28,.23,.23),(.45,.29,.19,.22),(.45,.29,.19,.22)]
hat=[(.72,.58,.28,.24),(.73,.58,.27,.24),(.72,.58,.28,.24),(.72,.58,.28,.24),(.73,.58,.27,.24),(.73,.58,.27,.24),(.72,.58,.28,.24),(.72,.58,.28,.24)]
build(7919,"B","object","male",T,[
 ("to poke the shiny object","the man with the stick","male",stick),
 ("to clutch his head","the man in the vest","male",vest),
 ("to crouch beside the sphere","the woman in the hat","female",hat)],
 0.2,[("an object",.48,.63,"male"),("a stick",.82,.52,"male"),("driftwood",.30,.88,"male"),("the sky",.50,.12,"male")],
 "What is lying on the beach?","A huge silver object is lying on the beach.","male",
 "Woman in green also touches the ball (not used). Vest man box trimmed on the left at 3.2-3.7 to stay clear of the green woman's head. Stick-man box ends above the hat woman's head.")

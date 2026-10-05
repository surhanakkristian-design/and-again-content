from gen_7064_7065_7066_7068_lib import write
tackled=[(.06,.40,.46,.75),(.08,.47,.37,.76),(.10,.55,.30,.76),(.12,.56,.38,.76),(.14,.45,.47,.75),(.15,.45,.60,.77),(.12,.45,.66,.89),(.10,.43,.62,.89)]
tackler=[(.46,.37,.70,.77),(.37,.44,.72,.79),(.30,.61,.99,.80),(.38,.56,.99,.81),(.47,.46,.99,.78),(.60,.45,1.0,.77),(.66,.34,1.0,.89),(.62,.21,1.0,.89)]
ref=[(.70,.38,.88,.61),(.72,.38,.92,.62),(.77,.38,.99,.60),(.77,.34,.99,.56),(.65,.22,.92,.45),(.61,.20,.86,.45),(.56,.15,.80,.33),None]
write(7064,"B","down","female",[
 ("to bring an opponent down","the player with the braid","female",tackler),
 ("to get tackled by an opponent","the player with the bun","female",tackled),
 ("to signal with a raised arm","the referee","male",ref)],
 2.2,[("an umbrella",.34,.29,"female"),("a floodlight",.53,.07,"female"),("a referee",.80,.37,"male"),("a puddle",.45,.87,"female")],
 "What are the two players doing?","They are crashing down into the mud.","female",
 "The two players overlap all the time; boxes split along the line between them (tackled player = dark hair in a bun, left/front; tackler = long braid, number 0). Referee arm only horizontal at 0.2-1.7, raised from 2.2; hidden behind the tackler at 3.7. 'a referee' noun voice male.")

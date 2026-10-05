from lib_5304_5306_5307_5308 import write
W = {0.0:(.02,.12,.93,.78),0.5:(.02,.12,.95,.78),1.0:(.02,.1,.93,.8),1.5:(.3,.26,.55,.74),2.0:(.36,.21,.57,.78),2.5:(.42,.23,.46,.73),
 3.0:(.5,.22,.5,.78),3.5:(.48,.21,.52,.79),4.0:(.47,.15,.53,.85),4.5:(.47,.1,.53,.9),5.0:(.22,.04,.78,.96),5.5:(.28,.08,.72,.92),
 6.0:(.4,.17,.6,.83),6.5:(.6,.17,.4,.83),7.0:(.56,.2,.44,.8),7.5:(.35,.24,.65,.76),8.0:(.3,.22,.62,.78),8.5:(.2,.18,.72,.82),9.0:(.2,.2,.65,.8)}
M = {6.0:(0,.18,.4,.48),6.5:(.07,.22,.5,.44),7.0:(0,.24,.53,.42),7.5:(0,.23,.35,.46),8.0:(0,.22,.28,.46),8.5:(0,.36,.18,.3),9.0:(0,.38,.18,.32)}
write(5308,"A","sunflower","female",[
 ("to eat a cookie","the woman","female",W),
 ("to open the door","the woman","female",W),
 ("to bring big sunflowers","the delivery man","male",M)],
 7.0,[("sunflowers",.3,.45,"female"),("a cookie",.62,.53,"female"),("a helmet",.12,.28,"female"),("a door",.6,.3,"female")],
 "What is the man holding?","He is holding big sunflowers.","male",
 "Two phrases share the woman (eats the cookie 0-1 s, opens the door 5.0-6.0 s). Delivery man only 6.0-9.0, at the left edge; his box includes the sunflowers he holds until 7.5, then she takes them: at 7.5 the boxes split at x .35 (her hand on the stems is cut), at 8.0-9.0 the man is only an orange sleeve at the edge (min-size box 0.18 wide, woman box starts at x .2/.3). Noun 'a cookie' pill is larger than the small cookie in her hand at 7.0.")

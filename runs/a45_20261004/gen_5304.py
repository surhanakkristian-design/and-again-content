from lib_5304_5306_5307_5308 import write
W = {0.0:(0,.07,.97,.93),0.5:(0,.08,1,.92),1.0:(0,.1,.97,.9),1.5:(0,.25,.8,.33),2.0:(0,.29,.78,.29),2.5:(0,.3,.8,.34),
 3.0:(0,.38,.7,.27),3.5:(0,.03,.8,.75),4.0:(0,0,.78,.72),4.5:(0,0,.92,.7),5.0:(0,0,.97,.88),5.5:(0,.02,.97,.9),6.0:(0,0,.95,1),
 6.5:(0,0,.95,1),7.0:(0,.3,.9,.55),7.5:(0,.27,.97,.6),8.0:(0,.31,.92,.4),8.5:(0,.33,.97,.4),9.0:(0,.38,.92,.34),9.5:(0,0,.95,.85),
 10.0:(0,0,.92,.9),10.5:(0,.05,.92,.95),11.0:(0,.08,.82,.92),11.5:(0,.05,.98,.92),12.0:(0,0,.72,1)}
TP = {1.5:(.58,.04,.42,.2),2.0:(.57,.06,.43,.22),2.5:(.58,.05,.42,.24),3.0:(.63,.18,.37,.2),3.5:(.82,.28,.18,.14),
 7.0:(.58,.06,.42,.22),7.5:(.6,.06,.4,.2),8.0:(.6,.08,.4,.22),8.5:(.66,.12,.34,.2),9.0:(.78,.2,.22,.17),12.0:(.74,.36,.26,.15)}
write(5304,"B","dirt","female",[
 ("to show her grimy palms","the woman","female",W),
 ("to scrub off the dirt","the woman","female",W),
 ("to pour water into the basin","the tap","female",TP)],
 0.0,[("dirt",.22,.45,"female"),("a sink",.82,.8,"female"),("tiles",.15,.12,"female"),("a cupboard",.78,.08,"female")],
 "What is the woman doing?","She is scrubbing the dirt from her hands.","female",
 "Only one person; two phrases share the woman (show grimy palms at 0-1 s, scrub/rinse 1.5-9.5 s, mostly only her hands and arms in close-up). Tap = the faucet only (not the water stream, which runs into her hands); off at 4.0-6.5, 9.5-11.5 where it is out of frame or a sliver at the edge. At 12.0 the woman box stops at x .72 so it does not cover the faucet; her hand on the soap dish is partly outside. Soap not used as a target because she holds it.")

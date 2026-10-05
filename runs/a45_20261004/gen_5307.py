from lib_5304_5306_5307_5308 import write
D = {0.0:(.02,.17,.96,.83),0.5:(.02,.17,.96,.83),1.0:(.02,.18,.92,.82),1.5:(.04,.18,.95,.82),2.0:(.04,.16,.9,.75),
 2.5:(.03,.33,.96,.57),3.0:(0,.33,1,.57),3.5:(.22,.35,.38,.55),4.0:(.22,.35,.4,.55),4.5:(.22,.36,.4,.54),
 5.0:(.4,.41,.2,.18),5.5:(.42,.41,.2,.17),6.0:(.41,.38,.18,.14),6.5:(.41,.35,.18,.14),7.0:(.39,.36,.19,.14),7.5:(.38,.37,.19,.14),
 8.0:(.4,.38,.18,.19),8.5:(.38,.37,.19,.2),9.0:(.38,.37,.19,.17),9.5:(.38,.37,.19,.17),10.0:(.38,.37,.2,.18)}
G = {3.5:(.6,.42,.37,.46),4.0:(.62,.45,.31,.31),4.5:(.62,.47,.3,.3)}
R = {5.5:(.7,.52,.25,.14),6.0:(.62,.42,.26,.2),6.5:(.68,.48,.3,.16),7.0:(.63,.49,.35,.16),7.5:(.45,.51,.55,.18),
 8.0:(.58,.5,.42,.22),8.5:(.6,.5,.4,.24),9.0:(.6,.5,.4,.26),9.5:(.6,.53,.4,.24),10.0:(.58,.5,.42,.3)}
write(5307,"B","spacious","male",[
 ("to sip from a white mug","the man in the denim shirt","male",D),
 ("to wear pastel pyjamas","the little girl","female",G),
 ("to lean against a teal cushion","the man in the red T-shirt","male",R)],
 5.0,[("a flat-screen TV",.5,.4,"male"),("a sectional sofa",.5,.72,"male"),("floorboards",.35,.88,"male")],
 "Where are all the people sitting?","They are sitting on a spacious sectional sofa.","male",
 "Denim-shirt man tracked through all three shots (tiny in the middle of the sectional from 5.0). Girl only 3.5-4.5; at 3.5-4.5 the man/girl boxes are split at x .6-.62 (his arm and knee run behind her). Red (pinkish) T-shirt man appears 5.5, leans back on the teal cushion 8.0-10.0 (at 6.0-7.5 he is next to a yellow cushion, so the phrase is only true at the end). At 7.5-8.0 his stretched legs are partly outside his box to keep clear of the denim man's box. Answer subject They (mixed group) -> defaultVoice.")

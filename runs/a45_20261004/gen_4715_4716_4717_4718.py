import json
def keys(times, d):
    out=[]
    for t in times:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else:
            x0,y0,x1,y1=b
            out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
def T(n): return [i*0.5 for i in range(n)]
def dump(o): json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# 4715
t=T(25)
M={0:(0,.11,.30,.71),.5:(0,.13,.59,.43),1:(0,.14,.29,.68),1.5:(0,.14,.29,.68),2:(0,.14,.29,.68),2.5:(0,.14,.29,.68),
3:(0,.15,.29,.67),3.5:(0,.13,.58,.43),4:(0,.13,.57,.42),4.5:(0,.12,.50,.43),5:(0,.12,.28,.64),5.5:(0,.16,.29,.63),
6:(0,.19,.26,.61),6.5:(0,.19,.26,.61),7:(0,.19,.27,.61),7.5:(0,.23,.29,.61),8:(0,.26,.30,.60),8.5:(0,.24,.31,.60),
9:(0,.23,.31,.59),9.5:(0,.23,.31,.59),10:(0,.16,.32,.56),10.5:(0,.26,.32,.57),11:(0,.24,.34,.55),11.5:(0,.24,.35,.53),12:(0,.17,.32,.51)}
W={0:(.53,.14,1,.42),.5:(.73,.17,1,.66),1:(.72,.16,1,.67),1.5:(.73,.16,1,.67),2:(.73,.16,1,.65),2.5:(.73,.16,1,.65),
3:(.53,.19,1,.44),3.5:(.71,.18,1,.64),4:(.72,.16,1,.63),4.5:(.71,.17,1,.63),5:(.72,.16,1,.64),5.5:(.73,.19,1,.63),
6:(.71,.21,1,.63),6.5:(.71,.21,1,.63),7:(.70,.23,1,.62),7.5:(.72,.26,1,.62),8:(.71,.26,1,.60),8.5:(.71,.27,1,.60),
9:(.72,.26,1,.61),9.5:(.71,.26,1,.61),10:(.68,.21,1,.56),10.5:(.70,.27,1,.57),11:(.71,.26,1,.54),11.5:(.64,.28,1,.53),12:(.62,.27,1,.51)}
L={0:(.30,.43,.72,.72),.5:(.30,.44,.72,.72),1:(.30,.45,.71,.74),1.5:(.30,.45,.72,.74),2:(.30,.45,.72,.74),2.5:(.30,.45,.72,.74),
3:(.30,.46,.71,.74),3.5:(.29,.45,.70,.74),4:(.30,.44,.71,.73),4.5:(.29,.45,.70,.72),5:(.29,.42,.71,.72),5.5:(.30,.41,.72,.72),
6:(.27,.40,.70,.70),6.5:(.27,.40,.70,.70),7:(.28,.39,.69,.70),7.5:(.30,.39,.71,.70),8:(.31,.39,.70,.68),8.5:(.32,.38,.70,.68),
9:(.32,.41,.71,.69),9.5:(.32,.39,.70,.69),10:(0,.57,1,.88),10.5:(0,.58,1,.86),11:(0,.56,1,.84),11.5:(0,.54,1,.82),12:(0,.52,1,.78)}
for k in L:
    if k>=10: continue
    x0,y0,x1,y1=L[k]
    if M[k][2]<=x0 and M[k][3]>y0:  # man beside melon
        M[k]=(M[k][0],M[k][1],round(x0+.02,2),M[k][3]); x0=round(x0+.03,2)
    if W[k][0]>=x1 and W[k][3]>y0:
        W[k]=(round(x1-.02,2),W[k][1],W[k][2],W[k][3]); x1=round(x1-.03,2)
    L[k]=(x0,y0,x1,y1)
dump({"mediaId":4715,"level":"A","keyWord":"watermelon","defaultVoice":"male",
"taps":[{"phrase":"to wear a cap","target":"the man","voice":"male","keys":keys(t,M)},
{"phrase":"to wear a blue shirt","target":"the woman","voice":"female","keys":keys(t,W)},
{"phrase":"to break into small pieces","target":"the watermelon","voice":"male","keys":keys(t,L)}],
"stillS":8.5,
"nouns":[{"word":"a watermelon","x":.51,"y":.56,"voice":"male"},{"word":"a table","x":.50,"y":.80,"voice":"male"},
{"word":"a man","x":.14,"y":.45,"voice":"male"},{"word":"a woman","x":.85,"y":.46,"voice":"female"}],
"question":"What happens to the watermelon?",
"answer":["The","watermelon","breaks","into","small","pieces."],"answerVoice":"male",
"notes":"Man and woman do exactly the same things (both put rubber bands on, both jump back), so their phrases are states (cap / blue shirt). People and melon overlap in the picture: boxes split along the melon edge; at 0.0 and 3.0 the woman's box is only head + upper body (arm lies over the melon); at 0.5, 3.5-4.5 the man's box is head + reaching arm. After the burst (10.0+) the watermelon box is the whole table full of pieces. Question in present simple (one sudden event at the end), not continuous."})

# 4716
MAN={0:(.20,.37,.82,.88),.5:(.26,.33,.72,.85),1:(.25,.29,.73,1),1.5:(.36,.30,.76,1),2:(0,.30,.73,1),2.5:(.10,.29,1,1),
3:(.30,.30,1,1),3.5:(.25,.33,1,1),4:(.30,.30,.97,.91),4.5:(.34,.25,.84,.86),5:(.24,.40,.68,.84),5.5:(.17,.40,.66,.85),
6:(.14,.35,.66,.79),6.5:(.11,.35,.67,.82),7:(.07,.33,.70,.93),7.5:(0,.33,.73,.98),8:(0,.30,.85,.95),8.5:(.33,.42,.89,.86),
9:(.32,.41,.78,.97),9.5:(.34,.42,.83,.96),10:(.27,.42,.81,.87),10.5:(.14,.42,.83,.89),11:(.10,.41,.90,1),11.5:(.01,.39,.92,1),12:(0,.36,1,1)}
F={8.5:(.38,.05,.73,.41),9:(.33,.05,.67,.40),9.5:(.25,.05,.60,.41),10:(.23,.05,.60,.41),10.5:(.23,.04,.58,.41),
11:(.23,.05,.60,.40),11.5:(.23,.05,.58,.38),12:(.25,.04,.60,.35)}
mk=keys(t,MAN)
dump({"mediaId":4716,"level":"A","keyWord":"explore","defaultVoice":"male",
"taps":[{"phrase":"to explore the jungle","target":"the man","voice":"male","keys":mk},
{"phrase":"to hold a big knife","target":"the man","voice":"male","keys":mk},
{"phrase":"to fall into the water","target":"the waterfall","voice":"male","keys":keys(t,F)}],
"stillS":10.0,
"nouns":[{"word":"a waterfall","x":.40,"y":.22,"voice":"male"},{"word":"a man","x":.50,"y":.58,"voice":"male"},
{"word":"rocks","x":.55,"y":.87,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","exploring","the","jungle."],"answerVoice":"male",
"notes":"Only two targets: the man (whole clip) and the waterfall (from 8.5 s). The man stands in front of the lower end of the waterfall: split at his head top, the waterfall box is the part above him. The knife is visible from about 3.5 s on. Only 3 nouns: the knife is too close to the man's pill, 'water' could also label the waterfall."})

# 4717
t2=T(21)
MAN2={0:(.30,.39,1,.88),.5:(.15,.39,1,1),1:(.17,.49,1,1),1.5:(.05,.49,1,1),2:(.10,.34,1,1),2.5:(.05,.31,1,1),
3:(.12,.27,.95,1),3.5:(.17,.34,1,1),4:(.12,.32,.75,1),4.5:(.17,.37,.72,1),5:(.07,.37,.72,1),5.5:(.32,.34,.88,1),
6:(0,.34,.93,1),6.5:(.07,.43,.83,1),7:(.12,.42,.82,1),7.5:(.22,.40,.86,1),8:(.25,.39,.78,1),8.5:(.29,.39,.85,.83),
9:(.12,.35,.78,.98),9.5:(.10,.39,.81,1),10:(.11,.40,.81,.95)}
F2={6.5:(.58,.26,.92,.42),7:(.38,.22,.90,.41),7.5:(.28,.08,.97,.39),8:(.08,0,.95,.38),8.5:(.05,0,1,.38),9:(0,0,1,.34),
9.5:(0,0,1,.38),10:(0,0,1,.39)}
mk2=keys(t2,MAN2)
dump({"mediaId":4717,"level":"A","keyWord":"dark","defaultVoice":"male",
"taps":[{"phrase":"to walk in the dark","target":"the man","voice":"male","keys":mk2},
{"phrase":"to open his arms wide","target":"the man","voice":"male","keys":mk2},
{"phrase":"to fall into the water","target":"the waterfall","voice":"male","keys":keys(t2,F2)}],
"stillS":10.0,
"nouns":[{"word":"a waterfall","x":.30,"y":.20,"voice":"male"},{"word":"a man","x":.50,"y":.56,"voice":"male"},
{"word":"a rock","x":.50,"y":.88,"voice":"male"}],
"question":"Where is the man walking?",
"answer":["He","is","walking","in","the","dark."],"answerVoice":"male",
"notes":"Two targets: the man and the waterfall (from 6.5 s, first seen through the cave opening). The waterfall fills the background behind the man from 8.0 s: its box is the part above his head. 3.0-6.0 s are very dark, the man box follows his faint outline. Key word 'dark' is an adjective, so it is in a phrase and the answer, not a noun. Only 3 nouns ('water' could also label the waterfall)."})

# 4718
t3=T(19)
full=(0,0,1,1)
WO={0:full,.5:full,1:full,1.5:full,2:full,2.5:(0,.21,1,1),3:(0,.20,1,1),3.5:(0,.21,1,1),4:(0,.27,1,1),4.5:(.08,.31,1,1),
5:(.22,.37,1,1),5.5:(.32,.07,1,1),6:(.05,.14,1,1),6.5:(.25,.21,1,1),7:(.50,.27,1,1),7.5:(.51,.30,1,1),8:(.51,.31,1,1),
8.5:(.50,.32,1,1),9:(.50,.33,1,1)}
H={2.5:(0,0,.47,.20),3:(0,0,.67,.19),3.5:(0,0,.67,.20),4:(0,0,.64,.26),4.5:(0,0,.64,.30),5:(0,0,.63,.36)}
wk=keys(t3,WO)
dump({"mediaId":4718,"level":"A","keyWord":"eye","defaultVoice":"female",
"taps":[{"phrase":"to smile at the camera","target":"the woman","voice":"female","keys":wk},
{"phrase":"to point with her finger","target":"the woman","voice":"female","keys":wk},
{"phrase":"to hold her eye open","target":"the man's hand","voice":"female","keys":keys(t3,H)}],
"stillS":8.0,
"nouns":[{"word":"an eye","x":.30,"y":.46,"voice":"female"},{"word":"a woman","x":.70,"y":.82,"voice":"female"},
{"word":"glasses","x":.22,"y":.16,"voice":"female"}],
"question":"What is she pointing at?",
"answer":["She","is","pointing","at","a","big","eye."],"answerVoice":"female",
"notes":"0.0-2.0 s are an extreme close-up of the woman's eye: her box is the whole picture. 2.5-5.0 s the optician's thumb/hand pulls the lid up: the hand box is the top-left block, the woman is everything below it. From 6.5 s the eye model takes the left side and is cut out of the woman's box (the model is not a target, the optician is hardly in the picture). She smiles at the camera at 5.5-6.5 s and points at 8.5-9.0 s. Noun 'an eye' sits on the big eye model (her own eyes are small beside it); 'glasses' = the rows of frames on the wall, slightly blurred."})

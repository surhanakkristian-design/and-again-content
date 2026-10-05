import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
def tap(p,tg,v,d): return {"phrase":p,"target":tg,"voice":v,"keys":keys(d)}
def save(c): json.dump(c,open(f'content/{c["mediaId"]}.json','w'),indent=1,ensure_ascii=False)

# 639
man={0:(0,0,.5,.58),.5:(0,0,.52,.52),1:(0,0,.18,.22),1.5:(0,.47,.18,.16),2:(0,.46,.18,.16),2.5:(0,.22,.56,.32),3:(0,.33,.2,.32),3.5:(0,.4,.18,.26),
 7:(0,.03,.18,.48),7.5:(0,.03,.18,.42),8:(0,.06,.18,.38),8.5:(0,.06,.2,.45),9:(0,.16,.2,.44),9.5:(0,.16,.2,.4),10:(0,.08,.2,.38)}
wom={2.5:(.72,0,.28,.54),3:(.74,0,.26,.5),3.5:(.76,0,.24,.47),4:(.5,0,.5,.46),4.5:(.5,0,.5,.46),5:(.33,.03,.67,.46),5.5:(.48,.26,.52,.36),6:(.5,.44,.5,.44),6.5:(.42,0,.58,1),
 7:(.4,.2,.6,.8),7.5:(.4,.16,.6,.84),8:(.4,.13,.6,.87),8.5:(.38,.14,.62,.86),9:(.4,.14,.6,.86),9.5:(.48,.16,.52,.84),10:(.5,.15,.5,.85)}
sau={.5:(.24,.56,.42,.14),1:(.23,.52,.42,.14),1.5:(.27,.5,.4,.14),2:(.24,.52,.42,.14),2.5:(.2,.54,.6,.17),3:(.2,.5,.54,.22),3.5:(.2,.48,.56,.2),4:(.14,.47,.76,.24),4.5:(.14,.47,.76,.24),5:(.1,.5,.8,.24),5.5:(.08,.65,.68,.17),
 7:(0,.86,.24,.14),7.5:(0,.86,.22,.14),8:(0,.86,.24,.14),8.5:(.02,.86,.26,.14),9:(.02,.86,.26,.14),9.5:(.1,.86,.28,.14),10:(0,.84,.4,.16)}
save({"mediaId":639,"level":"A","keyWord":"sausage","defaultVoice":"male",
 "taps":[tap("to turn the sausages","the man","male",man),tap("to eat a hot dog","the woman","female",wom),tap("to lie in a pan","the sausages","male",sau)],
 "stillS":10.0,
 "nouns":[{"word":"a hat","x":.10,"y":.21,"voice":"male"},{"word":"a tent","x":.45,"y":.52,"voice":"male"},{"word":"a bird","x":.26,"y":.69,"voice":"male"},{"word":"sausages","x":.20,"y":.92,"voice":"male"}],
 "question":"What is the woman eating?","answer":["She","is","eating","a","hot dog."],"answerVoice":"female",
 "notes":"Man is mostly a hand at the left edge in 1.0-3.5 (hand with tongs = his; boxes follow the hand). 'the sausages' = those in the pan only; off at 0.0 (still in his hand) and 6.0-6.5 (pan out of frame); the single sausage lifted on the fork (5.5-6.5) is not boxed. Sausage box at 7.0-9.5 is a sliver at the bottom edge. defaultVoice male: mixed couple, odd id."})

# 640
wom={0:(.12,.08,.49,.8),.5:(.16,.03,.7,.84),1:(.2,0,.62,.95),1.5:(.17,0,.66,.95),2:(.18,.15,.6,.67),2.5:(.08,.3,.9,.6),3:(.1,.27,.82,.72),3.5:(.12,.1,.78,.82),4:(.17,0,.66,.84),4.5:(.17,0,.66,.86),5:(.15,0,.66,.98),
 5.5:(.1,.02,.5,.96),6:(0,.07,.36,.77),6.5:(0,.1,.17,.72),7:(0,.16,.14,.76),7.5:(0,.18,.14,.76),8:(0,.25,.22,.63),8.5:(0,.26,.24,.62),9:(0,.27,.23,.71),9.5:(0,.27,.22,.71),10:(0,.25,.23,.62)}
man={0:(.61,.08,.19,.68),2:(.18,0,.6,.15),2.5:(.16,0,.64,.3),3:(.16,0,.64,.27),3.5:(.16,0,.64,.1),5.5:(.6,0,.25,.84),6:(.36,0,.46,.8),6.5:(.17,0,.7,.87),7:(.14,0,.76,.98),7.5:(.14,0,.78,1),
 8:(.22,.03,.72,.89),8.5:(.24,.04,.7,.87),9:(.23,.07,.67,.92),9.5:(.22,.07,.68,.92),10:(.23,.07,.67,.84)}
save({"mediaId":640,"level":"A","keyWord":"scale","defaultVoice":"female",
 "taps":[tap("to pick up two weights","the woman","female",wom),tap("to show his big arms","the man","male",man),tap("to point at the scale","the woman","female",wom)],
 "stillS":10.0,
 "nouns":[{"word":"a man","x":.48,"y":.30,"voice":"male"},{"word":"a woman","x":.12,"y":.47,"voice":"female"},{"word":"the floor","x":.66,"y":.74,"voice":"female"},{"word":"a scale","x":.47,"y":.91,"voice":"female"}],
 "question":"What is the man standing on?","answer":["He","is","standing","on","a","scale."],"answerVoice":"male",
 "notes":"Man stands right behind the woman in 0.0-5.5: his box is only the part above/beside her (0.0, 2.0-3.5, 5.5) and off where he is almost fully hidden (0.5-1.5, 4.0-5.0). At 3.5 his box is only 0.10 high (head above hers). At 8.0-10.0 the split line x~0.23 cuts off the outer part of his raised left arm. Two phrases share the woman (both stand on the scale, so no 'stand on' phrase). Small men in the far background are not targets."})

# 641
wom={0:(0,0,.56,.42),.5:(0,0,.56,.45),1:(0,0,.56,.5),1.5:(0,0,.56,.6),2:(0,.02,.54,.52),2.5:(0,.03,.54,.5),3:(0,0,.52,.52),3.5:(0,0,.48,.5),4:(0,0,.48,.34),4.5:(0,0,.58,.3),5:(0,0,.58,.33),5.5:(0,0,.57,.33),6:(0,0,.56,.33),
 6.5:(0,.06,.52,.48),7:(0,.07,.49,.55),7.5:(0,.07,.41,.78),8:(0,.05,.32,.74),8.5:(0,.08,.3,.72),9:(0,.08,.29,.87),9.5:(0,.07,.29,.88),10:(0,.07,.27,.76)}
man={0:(.57,0,.43,.43),.5:(.57,0,.43,.45),1:(.58,0,.42,.5),1.5:(.58,0,.42,.6),2:(.58,0,.42,.55),2.5:(.6,.05,.4,.55),3:(.55,0,.45,.6),3.5:(.5,0,.5,.5),4:(.5,0,.5,.36),4.5:(.6,0,.4,.33),5:(.6,0,.4,.36),5.5:(.58,0,.42,.37),6:(.58,0,.42,.36),
 6.5:(.55,.03,.45,.5),7:(.5,.05,.5,.57),7.5:(.61,.05,.39,.8),8:(.7,.06,.3,.74),8.5:(.72,.08,.28,.72),9:(.71,.07,.29,.88),9.5:(.72,.07,.28,.88),10:(.71,.05,.29,.82)}
cat={7.5:(.41,.44,.2,.19),8:(.32,.17,.38,.54),8.5:(.3,.12,.42,.62),9:(.29,.12,.42,.74),9.5:(.29,.11,.43,.73),10:(.27,.1,.44,.65)}
save({"mediaId":641,"level":"B","keyWord":"scale","defaultVoice":"male",
 "taps":[tap("to pour some flour","the man","male",man),tap("to wear a long braid","the woman","female",wom),tap("to perch on the scale","the cat","male",cat)],
 "stillS":10.0,
 "nouns":[{"word":"copper pans","x":.42,"y":.05,"voice":"male"},{"word":"a tabby cat","x":.50,"y":.45,"voice":"male"},{"word":"a mixing bowl","x":.86,"y":.80,"voice":"male"},{"word":"a kitchen scale","x":.42,"y":.90,"voice":"male"}],
 "question":"What is the cat doing?","answer":["It","is","perching","on","the","kitchen","scale."],"answerVoice":"male",
 "notes":"Woman has a state phrase (braid): her only own action (helping tilt the jug / a pinch of flour at 4.0-6.0) is unclear in the frames. The jug is in the man's hands (clear at 3.0-3.5). In the close-ups 4.0-6.0 the people are only hands/arms/faces at the top; boxes cover those. 'perch' used for the cat sitting on the small scale tray. defaultVoice male: couple, odd id."})

# 642
wom={0:(.66,.14,.34,.86),.5:(.25,.05,.75,.95),1:(.02,0,.98,1),1.5:(0,0,1,1),3:(0,0,1,1),3.5:(0,0,1,1),4.5:(.78,.1,.22,.9),5:(.82,.1,.18,.9),5.5:(.86,.08,.14,.92),6:(.88,0,.12,.4),
 8:(.64,.24,.36,.6),8.5:(.64,.24,.36,.62),9:(.58,.33,.42,.61),9.5:(.59,.31,.41,.63),10:(.59,.3,.41,.55)}
bman={0:(0,.17,.22,.68),2:(0,.04,1,.96),2.5:(0,.04,1,.96),4:(0,.12,.9,.88),4.5:(0,.1,.18,.74),5:(0,.14,.18,.84),5.5:(0,.08,.18,.55),6:(0,.07,.18,.32),
 8:(0,.24,.36,.63),8.5:(0,.24,.38,.63),9:(0,.33,.4,.65),9.5:(0,.32,.41,.66),10:(0,.32,.41,.56)}
blond={0:(.27,.24,.39,.52),.5:(0,.19,.24,.63),4.5:(.24,.21,.53,.6),5:(.22,.2,.56,.72),5.5:(.28,.18,.57,.74),6:(.2,.12,.66,.76),6.5:(.08,.08,.84,.86),7:(.06,.05,.86,.95),7.5:(.08,.04,.86,.96),
 8:(.38,.32,.25,.32),8.5:(.39,.32,.25,.32),9:(.4,.36,.18,.36),9.5:(.41,.35,.18,.37),10:(.41,.34,.18,.3)}
save({"mediaId":642,"level":"B","keyWord":"scar","defaultVoice":"female",
 "taps":[tap("to point at her forearm","the woman","female",wom),tap("to have a bushy beard","the bearded man","male",bman),tap("to show his scarred shin","the blond man","male",blond)],
 "stillS":7.0,
 "nouns":[{"word":"a trench coat","x":.74,"y":.47,"voice":"female"},{"word":"a light bulb","x":.12,"y":.54,"voice":"female"},{"word":"a scar","x":.53,"y":.64,"voice":"female"},{"word":"mugs","x":.25,"y":.83,"voice":"female"}],
 "question":"What is the blond man showing?","answer":["He","is","showing","a","scar","on","his","shin."],"answerVoice":"male",
 "notes":"The third friend is androgynous; treated as male ('his shin' in the description), named 'the blond man'. Bearded man has a state phrase: his own action (pushing up a sleeve to show a scar) is also done by the woman. Clip has many cuts; in the wide shots (8.0-10.0) the three sit close and the blond man's box is narrow. Slivers of the woman/man at frame edges are off at 4.0, 6.5-7.5. 'a light bulb' at 7.0 is the single lit bulb at the left edge."})

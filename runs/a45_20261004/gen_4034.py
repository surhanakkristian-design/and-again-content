import json
T=[i*0.5 for i in range(31)]
def K(d):
    out=[]
    for t in T:
        v=d.get(t)
        if v is None: out.append({"t":t,"off":True})
        else:
            x1,y1,x2,y2=v
            out.append({"t":t,"x":x1,"y":y1,"w":round(x2-x1,2),"h":round(y2-y1,2)})
    return out
W={0.0:(.43,.16,.65,.56),0.5:(.43,.16,.65,.56),1.0:(.43,.16,.65,.56),1.5:(.43,.16,.65,.56),2.0:(.44,.17,.66,.56),
2.5:(.41,.17,.64,.56),3.0:(.37,.21,.57,.66),3.5:(.20,.19,.62,.69),4.0:(.18,.19,.46,.61),4.5:(.18,.12,.46,.63),
5.0:(.04,.18,.43,.70),5.5:(.09,.18,.43,.70),6.0:(.20,.19,.44,.59),6.5:(.19,.19,.46,.59),7.0:(.10,.19,.48,.70),
7.5:(.10,.19,.50,.69),8.0:(.12,.19,.48,.60),8.5:(.12,.19,.48,.60),9.0:(.17,.19,.49,.70),9.5:(.17,.19,.49,.70),
10.0:(.10,.19,.51,.60),10.5:(.03,.17,.57,.60),11.0:(.05,.19,.58,.72),11.5:(.14,.19,.75,.73),12.0:(.30,.17,.71,.61),
12.5:(.44,.17,.75,.61),13.0:(.44,.19,.71,.73),13.5:(.44,.18,.72,.73),14.0:(.41,.17,.75,.60),14.5:(.42,.17,.63,.59),15.0:(.43,.20,.71,.70)}
B={0.0:(.11,.25,.43,.53),0.5:(.11,.25,.43,.53),1.0:(.11,.25,.43,.53),1.5:(.11,.25,.43,.53),2.0:(.11,.17,.44,.53),
2.5:(.17,.22,.41,.53),3.0:(.13,.24,.37,.55),4.0:(.46,.18,.70,.50),4.5:(.46,.25,.66,.52),
5.0:(.43,.22,.73,.59),5.5:(.43,.23,.78,.61),6.0:(.44,.25,.75,.52),6.5:(.46,.24,.86,.52),7.0:(.48,.23,.90,.60),
7.5:(.50,.23,.91,.62),8.0:(.49,.23,.91,.53),8.5:(.49,.23,.91,.53),9.0:(.49,.25,.87,.63),9.5:(.49,.21,.87,.65),
10.0:(.51,.23,.78,.53),10.5:(.57,.23,.81,.53),11.0:(.58,.27,.74,.64),
12.5:(.24,.33,.44,.53),13.0:(.17,.36,.44,.62),13.5:(.14,.36,.44,.55),14.0:(.08,.37,.41,.54),14.5:(.08,.37,.42,.54),15.0:(.10,.37,.43,.55)}
WB={3.0:.57,3.5:.58,5.0:.59,5.5:.59,7.0:.59,7.5:.59,9.0:.59,9.5:.59,11.0:.60,11.5:.60,13.0:.61,13.5:.61,15.0:.58}
BB={5.0:.52,5.5:.53,7.0:.52,7.5:.53,9.0:.53,9.5:.54,11.0:.53,13.0:.53}
for t,v in WB.items(): W[t]=W[t][:3]+(v,)
for t,v in BB.items(): B[t]=B[t][:3]+(v,)
kw=K(W)
d={"mediaId":4034,"level":"A","keyWord":"trap","defaultVoice":"male",
"taps":[{"phrase":"to hold a red bat","target":"the man in white","voice":"male","keys":kw},
{"phrase":"to fall on the floor","target":"the man in black","voice":"male","keys":K(B)},
{"phrase":"to wear a white shirt","target":"the man in white","voice":"male","keys":kw}],
"stillS":8.0,
"nouns":[{"word":"a trap","x":.49,"y":.83,"voice":"male"},{"word":"a wall","x":.30,"y":.09,"voice":"male"},
{"word":"boxes","x":.85,"y":.13,"voice":"male"},{"word":"a bat","x":.19,"y":.45,"voice":"male"}],
"question":"Where are the two men walking?",
"answer":["They","are","walking","between","the","traps."],"answerVoice":"male",
"notes":"defaultVoice male although evenId is true: both people are men. The two men stand close / overlap in many frames: boxes are split along a vertical line, so an arm, a leg or the bat is cut here and there. Man in black is hidden behind the man in white at 3.5, 11.5 and 12.0 s (off). Third phrase is a state (white shirt) because the other clear actions (walking between traps) fit both men. 'a trap' pill sits on the big foreground trap; many traps are visible. 'a bat' is the thin red foam bat."}
json.dump(d,open("content/4034.json","w"),indent=1)

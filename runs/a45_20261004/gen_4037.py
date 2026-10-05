import json
T=[i*0.5 for i in range(15)]
def K(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
S={0.0:(.32,.40,.34,.23),0.5:(.32,.34,.28,.33),1.0:(.17,.32,.65,.36),1.5:(.18,.32,.60,.36),2.0:(.20,.33,.60,.35),
2.5:(.18,.32,.63,.36),3.0:(.17,.32,.62,.36),3.5:(.18,.32,.64,.36),4.0:(.18,.31,.62,.36),4.5:(.21,.33,.58,.33),
5.0:(.20,.37,.57,.32),5.5:(.18,.35,.59,.33),6.0:(.18,.35,.58,.33),6.5:(.17,.36,.59,.28),7.0:(.18,.34,.58,.31)}
H={0.0:(.38,.02,.62,.37),0.5:(.61,.15,.39,.40),5.5:(.22,0,.78,.34),6.0:(.38,0,.62,.25),6.5:(0,.65,1.0,.33),7.0:(0,.66,1.0,.32)}
B={1.5:(.36,0,.64,.31),2.0:(.03,0,.97,.30),2.5:(.50,0,.50,.22),3.0:(.40,0,.60,.18)}
d={"mediaId":4037,"level":"A","keyWord":"cook","defaultVoice":"male",
"taps":[{"phrase":"to stand in the pan","target":"the sausage","voice":"male","keys":K(S)},
{"phrase":"to drop green onions","target":"the hand","voice":"male","keys":K(H)},
{"phrase":"to pour the eggs","target":"the white bowl","voice":"male","keys":K(B)}],
"stillS":6.5,
"nouns":[{"word":"a sausage","x":.45,"y":.47,"voice":"male"},{"word":"egg","x":.50,"y":.69,"voice":"male"},
{"word":"a plate","x":.50,"y":.80,"voice":"male"},{"word":"a hand","x":.16,"y":.90,"voice":"male"}],
"question":"What is cooking in the pan?",
"answer":["A","sausage","is","cooking","in","the","pan."],"answerVoice":"male",
"notes":"No person in the clip, only a hand (holds the sausage at 0-0.5 s, drops the onions at 5.5-6.0 s, both hands hold the plate at 6.5-7.0 s: one wide box over both hands along the bottom). Hand and sausage overlap at 0-0.5 s: split. 'to pour the eggs' has the bowl as target (no hand is visible while the egg is poured, 1.5-3.0 s) - a thing as the doer, weakest phrase. The egg / pan / plate were not used as tap targets because the sausage sits inside them (boxes would overlap). Noun 'egg' = the cooked egg (omelette) as mass noun; 'omelette' felt above level A. The answer says 'in the pan' although the still for the nouns shows the plate."}
json.dump(d,open("content/4037.json","w"),indent=1)

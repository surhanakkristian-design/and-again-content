import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
H={0.0:(.0,.57,1.0,.43),0.5:(.0,.48,1.0,.52),1.0:(.0,.47,1.0,.53),1.5:(.0,.37,1.0,.63),2.0:(.0,.40,1.0,.60),
2.5:(.0,.44,1.0,.56),3.0:(.0,.45,1.0,.55),3.5:(.0,.56,1.0,.44),4.0:(.0,.56,1.0,.44),4.5:(.0,.56,1.0,.44),
5.0:(.0,.57,1.0,.43),5.5:(.0,.56,1.0,.44),6.0:(.0,.54,1.0,.46),6.5:(.0,.54,1.0,.46),7.0:(.0,.50,1.0,.50),
7.5:(.0,.45,1.0,.55),8.0:(.0,.45,1.0,.55),8.5:(.0,.46,1.0,.54),9.0:(.0,.55,1.0,.45),9.5:(.0,.60,1.0,.38)}
P={3.5:(.38,.41,.24,.15),4.0:(.37,.40,.25,.16),4.5:(.37,.40,.25,.16),5.0:(.42,.43,.22,.14),5.5:(.39,.41,.22,.15),
6.0:(.40,.38,.24,.16),6.5:(.34,.38,.24,.16),7.0:(.37,.29,.24,.17),7.5:(.27,.23,.20,.16),8.0:(.38,.22,.22,.18),
8.5:(.41,.21,.22,.17),9.0:(.39,.34,.20,.16),9.5:(.40,.34,.20,.16),10.0:(.40,.33,.20,.15)}
L={t:(.03,.0,.97,.31) for t in T}
L.update({7.0:(.03,.0,.97,.28),7.5:(.03,.0,.97,.22),8.0:(.03,.0,.97,.21),8.5:(.03,.0,.97,.20)})
c={"mediaId":361,"level":"B","keyWord":"wrap","defaultVoice":"male",
"taps":[{"phrase":"to wrap lollipops in paper","target":"the hands","voice":"male","keys":keys(H)},
{"phrase":"to lie in a heap","target":"the unwrapped lollipops","voice":"male","keys":keys(L)},
{"phrase":"to have a smiley face","target":"the pink lollipop","voice":"male","keys":keys(P)}],
"stillS":10.0,
"nouns":[{"word":"lollipops","x":.50,"y":.10,"voice":"male"},{"word":"a bouquet","x":.50,"y":.37,"voice":"male"},
{"word":"a ribbon","x":.50,"y":.58,"voice":"male"},{"word":"a tablecloth","x":.55,"y":.84,"voice":"male"}],
"question":"What are the hands doing?",
"answer":["They","are","wrapping","lollipops","in","paper."],"answerVoice":"male",
"notes":"Both hands are one target with one box, so the box also covers what lies between the hands (paper, sticks, ribbon - none of them a target). The pink lollipop is boxed only from 3.5 s, when the face is drawn on it (before that it has no face and sits inside the hands); from 3.5 s the hands box starts below it, so the fingertips that reach up beside the lollipop (about 0.04-0.08 of the height, most at 5.0 s) are outside the hands box. Phrase 3 is a state. 7.0-8.5 s the white paper covers the lower part of the heap, its box is shortened. Noun 'lollipops' is on the colourful heap; the bouquet is also made of (wrapped) lollipops, but 'a bouquet' cannot go on the heap, so the placing is still unique. Hands' gender unclear -> default voice (odd id, male)."}
json.dump(c,open("content/361.json","w"),indent=1)

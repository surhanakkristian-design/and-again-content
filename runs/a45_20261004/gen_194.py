import json
def keys(d): return [({"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]}) for t in T]
def tap(p,t,v,d): return {"phrase":p,"target":t,"voice":v,"keys":keys(d)}
def noun(w,x,y,v): return {"word":w,"x":x,"y":y,"voice":v}
T=[i*0.5 for i in range(21)]
W={0.0:(.22,.34,.78,.56),0.5:(.25,.24,.75,.68),1.0:(.12,.14,.88,.86),1.5:(.27,.18,.73,.82),2.0:(.27,.24,.73,.76),2.5:(.24,.03,.76,.97),
3.0:(.28,.10,.72,.90),3.5:(.25,.10,.75,.90),4.0:(.29,.12,.71,.88),4.5:(.34,.17,.66,.83),5.0:(.38,.25,.62,.75),5.5:(.45,.20,.55,.80),
6.0:(.38,.10,.62,.90),6.5:(.28,.58,.72,.42),7.0:(.28,.60,.72,.40),7.5:(.30,.60,.70,.40),8.0:(.51,.57,.49,.43),8.5:(.45,.58,.55,.42),
9.0:(.32,.10,.68,.90),9.5:(.48,.18,.52,.82),10.0:(.40,.15,.60,.85)}
M={2.0:(0,0,.18,.78),2.5:(0,0,.20,.85),3.0:(0,0,.24,.95),3.5:(0,0,.24,.95),4.0:(0,0,.26,1),4.5:(0,.03,.25,.97),5.0:(0,.02,.34,.98),
5.5:(0,.03,.44,.97),6.0:(0,0,.37,1),6.5:(0,0,.60,.57),7.0:(0,0,.66,.58),7.5:(0,0,.68,.58),8.0:(0,0,.50,1),8.5:(0,0,.44,1),
9.0:(0,.03,.31,.97),9.5:(0,.03,.47,.60),10.0:(0,.03,.30,.42)}
c={"mediaId":194,"level":"A","keyWord":"cotton","defaultVoice":"female",
"taps":[tap("to hold some cotton","the woman","female",W),tap("to blow the cotton away","the woman","female",W),tap("to wear a white T-shirt","the man","male",M)],
"stillS":5.5,
"nouns":[noun("the sun",.68,.22,"female"),noun("a hat",.84,.31,"female"),noun("cotton",.60,.50,"female"),noun("a T-shirt",.25,.74,"female")],
"question":"What is the woman holding?","answer":["She","is","holding","some","cotton."],"answerVoice":"female",
"notes":"Two targets only: the cotton ball is always in the woman's hand, so it is not a separate target. 0.0-1.5 only the hands with the cotton are shown: boxed as the woman (assumed hers, same hand as later). The blowing is only at 9.5-10.0. 6.5-8.5 her hands hold the cotton on his shirt: man = upper part, woman = her hands below (her hat at the right edge is outside her box there). 8.0-9.5 a strip of his sleeve next to her hand is in no box. Man's phrase is a state (he only laughs and looks, as she does)."}
json.dump(c,open('content/194.json','w'),indent=1)

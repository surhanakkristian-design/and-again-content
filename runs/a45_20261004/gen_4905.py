import json
T=[i*0.5 for i in range(19)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)})
    return out
man={0.0:(.19,.26,.84,1.0),0.5:(.19,.35,.89,1.0),1.0:(.17,.59,.86,1.0)}
fe={3.0:(0,0,.78,1.0),3.5:(0,0,.78,1.0),4.0:(0,0,.80,1.0),4.5:(.35,0,.75,1.0),5.0:(.36,.06,.70,1.0)}
br={t:(0,.33,1.0,.67) for t in (7.0,7.5,8.0)}; br.update({8.5:(0,.33,1.0,.64),9.0:(0,.34,1.0,.64)})
c={"mediaId":4905,"level":"B","keyWord":"span","defaultVoice":"male",
 "taps":[{"phrase":"to hold an aluminium ladder","target":"the man","voice":"male","keys":keys(man)},
  {"phrase":"to stand in a city street","target":"the fire engine","voice":"male","keys":keys(fe)},
  {"phrase":"to span a deep canyon","target":"the bridge","voice":"male","keys":keys(br)}],
 "stillS":9.0,
 "nouns":[{"word":"the sky","x":.50,"y":.15,"voice":"male"},{"word":"a steel bridge","x":.28,"y":.50,"voice":"male"},
  {"word":"a river","x":.53,"y":.68,"voice":"male"},{"word":"a cliff","x":.78,"y":.86,"voice":"male"}],
 "question":"What is the man holding?","answer":["He","is","holding","an","aluminium","ladder."],"answerVoice":"male",
 "notes":"Fire engine box covers the truck and its raised ladder (4.5-5.0 only the ladder is in frame). The man's ladder keeps extending at 1.5-2.5 s but he is out of frame then (off). Crane shot (5.5-6.5) has no target."}
json.dump(c,open('content/4905.json','w'),indent=1)

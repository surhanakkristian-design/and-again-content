import json
def K(times, d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in times]
def B(x0,y0,x1,y1): return (x0,y0,round(x1-x0,2),round(y1-y0,2))
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
wom={0.2:B(.21,.37,.85,1.0),0.7:B(.20,.37,.90,1.0),1.2:B(.19,.37,.91,1.0),1.7:B(.16,.35,.87,1.0),
     2.2:B(.11,.34,.82,1.0),2.7:B(.12,.34,.82,1.0),3.2:B(.05,.33,.83,1.0),3.7:B(.06,.32,.85,1.0)}
man={0.2:B(.46,.23,.72,.37),0.7:B(.46,.23,.68,.37),1.2:B(.45,.23,.66,.37),1.7:B(.45,.21,.66,.35),
     2.2:B(.48,.20,.72,.34),2.7:B(.49,.20,.68,.34),3.2:B(.48,.19,.68,.33),3.7:B(.48,.18,.74,.32)}
kw=K(T,wom)
c={"mediaId":7043,"level":"A","keyWord":"digital camera","defaultVoice":"female",
 "taps":[
  {"phrase":"to take a selfie","target":"the woman in the blue jacket","voice":"female","keys":kw},
  {"phrase":"to drink from a can","target":"the man at the back","voice":"male","keys":K(T,man)},
  {"phrase":"to stick out her tongue","target":"the woman in the blue jacket","voice":"female","keys":kw}],
 "stillS":0.2,
 "nouns":[{"word":"a digital camera","x":.67,"y":.47,"voice":"female"},{"word":"a fridge","x":.28,"y":.37,"voice":"female"},
          {"word":"crisps","x":.16,"y":.63,"voice":"female"},{"word":"a pizza","x":.12,"y":.73,"voice":"female"}],
 "question":"What are the friends doing?",
 "answer":["They","are","taking","a","selfie."],
 "answerVoice":"female",
 "notes":"The man at the back is mostly hidden behind the group; he drinks from a red can from about 2.2 s (before that he dances with one arm up). His box sits above the woman's box: they are split along her head top (her box starts at her hair line, his ends there), so his chin/the can may be slightly cut at 3.7. Tongue only visible 0.2-1.2 s. Answer: in the second half they look at the camera screen rather than take the selfie."}
json.dump(c,open("content/7043.json","w"),indent=1,ensure_ascii=False)

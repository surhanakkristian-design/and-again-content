import json
def keys(d): return [({"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]}) for t in T]
def tap(p,t,v,d): return {"phrase":p,"target":t,"voice":v,"keys":keys(d)}
def noun(w,x,y,v): return {"word":w,"x":x,"y":y,"voice":v}
T=[i*0.5 for i in range(19)]
M={0.0:(0,.21,.74,.44),0.5:(0,.20,.74,.46),1.0:(0,.19,.82,.58),1.5:(0,.17,1,.70),2.0:(0,.11,1,.67),2.5:(0,.11,1,.65),3.0:(0,.12,1,.72),
3.5:(0,.37,.95,.53),6.0:(0,.38,.95,.62),6.5:(.05,0,.92,.70),7.0:(0,0,1,.80),7.5:(0,.24,1,.58),8.0:(.08,.20,.60,.45),8.5:(.05,.25,.54,.38),9.0:(.06,.28,.60,.36)}
W={0.0:(.75,.05,.25,.95),0.5:(.75,.05,.25,.95),1.0:(.82,.55,.18,.45),4.0:(.10,.04,.88,.96),4.5:(.14,.04,.86,.96),5.0:(0,0,1,1),5.5:(.15,0,.85,1),
6.0:(.15,0,.85,.35),8.0:(.69,.05,.31,.95),8.5:(.60,.08,.40,.92),9.0:(.67,.20,.33,.80)}
c={"mediaId":193,"level":"B","keyWord":"corrupt","defaultVoice":"male",
"taps":[tap("to accept a bribe","the man","male",M),tap("to stamp the document","the man","male",M),tap("to reach into her pocket","the woman","female",W)],
"stillS":9.0,
"nouns":[noun("a stamp",.18,.58,"male"),noun("a moustache",.42,.43,"male"),noun("a document",.86,.68,"male"),noun("an apron",.78,.89,"male")],
"question":"What is the man doing?","answer":["The","corrupt","official","is","accepting","a","bribe."],"answerVoice":"male",
"notes":"Only two targets (the official, the woman); the pouch and the paper always lie in or under someone's hand, so no third target. Close-ups: 3.5 and 6.5 show only the man's hand (boxed as the man), 5.0-5.5 only the woman's body and hand, 6.0 her hand above (woman) and his hand with the pouch below (man), split at y 0.36. 8.0-9.0 the woman stands in front of the desk and partly hides the man: split by x. Answer names the man 'the corrupt official' (key word); 'official' is not in the phrases."}
json.dump(c,open('content/193.json','w'),indent=1)

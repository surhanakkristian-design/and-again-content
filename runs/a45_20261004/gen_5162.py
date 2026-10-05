import json
T=[i*0.5 for i in range(21)]
man={0.0:(.28,.50,.46,.50),0.5:(.43,.50,.50,.50),1.0:(0,.58,1,.42),1.5:(0,.53,1,.47),2.0:(0,.50,1,.50),
 2.5:(.30,.44,.70,.56),3.0:(.28,.44,.72,.56),3.5:(.38,.44,.62,.56),4.0:(.38,.38,.62,.62),4.5:(.38,.38,.62,.62),
 5.0:(.12,0,.88,.62),5.5:(0,0,1,.82)}
for t in T:
    if t>=6.0: man[t]=(0,.05,1,.70) if 7.5<=t<=9.5 else (0,.10,1,.65)
birds={0.0:(0,.72,.27,.27),0.5:(0,.58,.42,.36),1.0:(0,.26,1,.31),1.5:(0,.08,1,.44),2.0:(0,0,1,.49)}
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":round(min(w,1-x),2),"h":round(min(h,1-y),2)})
        else: out.append({"t":t,"off":True})
    return out
mk=keys(man); bk=keys(birds)
c={"mediaId":5162,"level":"A","keyWord":"beautiful","defaultVoice":"male",
 "taps":[{"phrase":"to open his arms","target":"the man","voice":"male","keys":mk},
         {"phrase":"to fly into the sky","target":"the birds","voice":"male","keys":bk},
         {"phrase":"to eat with a fork","target":"the man","voice":"male","keys":mk}],
 "stillS":4.0,
 "nouns":[{"word":"mountains","x":.45,"y":.27,"voice":"male"},{"word":"trees","x":.88,"y":.40,"voice":"male"},
          {"word":"a lake","x":.18,"y":.53,"voice":"male"},{"word":"a man","x":.70,"y":.70,"voice":"male"}],
 "question":"What is the man doing?","answer":["He","is","eating","with","a","fork."],"answerVoice":"male",
 "notes":"Three shots (square, lake, restaurant); birds only in shot 1. At t=0.0 the man's box covers his body only (his outstretched arms span the whole width and the ground birds sit under them), birds box = lower-left group. Key word 'beautiful' is an adjective, not used as a noun."}
json.dump(c,open('content/5162.json','w'),indent=1)

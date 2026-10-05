import json
T=[i*0.5 for i in range(25)]
man={0.0:(.15,.33,.57,.67),0.5:(.15,.33,.60,.67),1.0:(.10,.33,.57,.67),1.5:(.16,.33,.58,.67),2.0:(.10,.33,.56,.67),
 2.5:(.18,.36,.65,.64),3.0:(.08,.35,.62,.65),3.5:(.13,.35,.75,.65),4.0:(0,.37,.76,.63),4.5:(0,.38,.72,.62),
 5.0:(0,.38,.70,.62),5.5:(0,.38,.68,.62),6.0:(0,0,1,.46),6.5:(0,0,1,.46),7.0:(0,0,1,.44),7.5:(0,0,1,.35),8.0:(0,0,1,.30)}
for t in T:
    if t>=8.5: man[t]=(0,0,1,1)
tart={6.0:(.18,.47,.68,.31),6.5:(.18,.47,.70,.31),7.0:(.15,.45,.72,.33),7.5:(.15,.36,.72,.42),8.0:(.15,.31,.72,.48)}
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":round(min(w,1-x),2),"h":round(min(h,1-y),2)})
        else: out.append({"t":t,"off":True})
    return out
mk=keys(man); tk=keys(tart)
c={"mediaId":5167,"level":"B","keyWord":"tile","defaultVoice":"male",
 "taps":[{"phrase":"to touch the tiled wall","target":"the man","voice":"male","keys":mk},
         {"phrase":"to be dusted with sugar","target":"the custard tart","voice":"male","keys":tk},
         {"phrase":"to savour a custard tart","target":"the man","voice":"male","keys":mk}],
 "stillS":3.5,
 "nouns":[{"word":"a window","x":.15,"y":.10,"voice":"male"},{"word":"tiles","x":.70,"y":.22,"voice":"male"},
          {"word":"a shirt","x":.30,"y":.72,"voice":"male"},{"word":"a hand","x":.78,"y":.70,"voice":"male"}],
 "question":"What is the man touching?","answer":["He","is","touching","the","tiled","wall."],"answerVoice":"male",
 "notes":"Three shots: tram (0-2.0), tiled wall (2.5-5.5, palm on the tiles 3.5-5.5), cafe (6.0-12.0). The tart is visible 6.0-8.0 only; in those frames the man's box is the top strip (chest, hand, cup) and the tart box starts below it, so the lower fork tines fall in the tart box. Phrase 2 is a state (the tart cannot act). 'a hand' sits on his palm against the tiles."}
json.dump(c,open('content/5167.json','w'),indent=1)

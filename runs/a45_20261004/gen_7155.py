import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    out=[]
    for t,b in zip(T,boxes):
        if b is None: out.append({"t":t,"off":True}); continue
        x0,y0,x1,y1=b; out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
woman=[(.12,.09,.80,.82),(.17,.20,.80,.90),(.18,.17,.67,1.0),(.18,.29,.70,1.0),(.16,.26,.72,1.0),(.14,.22,.78,1.0),(.10,.19,.73,1.0),(.10,.15,.78,1.0)]
guests=[(.80,.48,1.0,.92),(.80,.50,1.0,.94),(.67,.48,1.0,.96),(.70,.45,1.0,.94),(.72,.40,1.0,.90),(.78,.40,1.0,.92),(.73,.42,1.0,.88),(.78,.42,1.0,.86)]
w=K(woman); g=K(guests)
c={"mediaId":7155,"level":"B","keyWord":"get away","defaultVoice":"female",
"taps":[
 {"phrase":"to clamber over the wall","target":"the woman","voice":"female","keys":w},
 {"phrase":"to hold sandals in her teeth","target":"the woman","voice":"female","keys":w},
 {"phrase":"to watch from the lawn","target":"the guests","voice":"female","keys":g}],
"stillS":2.2,
"nouns":[{"word":"the sky","x":0.60,"y":0.07,"voice":"female"},
 {"word":"ivy","x":0.11,"y":0.50,"voice":"female"},
 {"word":"a satin dress","x":0.38,"y":0.72,"voice":"female"},
 {"word":"guests","x":0.82,"y":0.48,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","climbing","over","an","ivy-covered","wall."],
"answerVoice":"female",
"notes":"Key word 'get away' not used literally (escape intent is not visible). Guests box split from the woman; guests box at 0.2/0.7 s only covers the guests right of x 0.80 to keep her head and hair in her box."}
json.dump(c,open('content/7155.json','w'),indent=1)

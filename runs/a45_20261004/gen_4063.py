import json
def K(times,f):
    o=[]
    for t in times:
        b=f.get(t)
        o.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return o
T=[i*0.5 for i in range(14)]
man={0.0:(0.34,0.26,0.36,0.38),0.5:(0.34,0.26,0.36,0.38),1.0:(0.33,0.26,0.36,0.38),1.5:(0.34,0.26,0.36,0.38),
2.0:(0.32,0.31,0.37,0.39),2.5:(0.38,0.48,0.26,0.27),3.0:(0.40,0.58,0.20,0.16),3.5:(0.41,0.59,0.18,0.15),
4.0:(0.42,0.60,0.18,0.14),4.5:(0.42,0.60,0.18,0.14),5.0:(0.42,0.60,0.18,0.14),5.5:(0.42,0.59,0.18,0.14),6.0:(0.42,0.58,0.18,0.14)}
st={0.0:(0.33,0.0,0.42,0.26),0.5:(0.33,0.0,0.42,0.26),1.0:(0.32,0.0,0.42,0.26),1.5:(0.32,0.0,0.42,0.26),2.0:(0.32,0.0,0.43,0.31)}
mk=K(T,man)
d={"mediaId":4063,"level":"B","keyWord":"release","defaultVoice":"male",
"taps":[
 {"phrase":"to dangle above the clouds","target":"the man","voice":"male","keys":mk},
 {"phrase":"to release the man","target":"the straps","voice":"male","keys":K(T,st)},
 {"phrase":"to plunge towards the clouds","target":"the man","voice":"male","keys":mk}],
"stillS":0.0,
"nouns":[{"word":"straps","x":0.45,"y":0.15,"voice":"male"},{"word":"a harness","x":0.50,"y":0.37,"voice":"male"},{"word":"boots","x":0.50,"y":0.57,"voice":"male"},{"word":"clouds","x":0.50,"y":0.80,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","plunging","towards","the","clouds."],
"answerVoice":"male",
"notes":"Only two tappable targets (man, straps); the clouds fill the frame so they are not a target. Straps visible 0-2.0 s only; at 2.0 s they are already loose and the box is split from the man's at y 0.31. From 4.0 s the man is a small speck, at 6.0 s barely visible (min-size box). 'a harness' pill sits on the man's chest; no 'a man' noun used."}
json.dump(d,open("content/4063.json","w"),indent=1)

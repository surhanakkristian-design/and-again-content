import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    out=[]
    for t,b in zip(T,boxes):
        if b is None: out.append({"t":t,"off":True}); continue
        x1,x2,y1,y2=b; out.append({"t":t,"x":x1,"y":y1,"w":round(x2-x1,2),"h":round(y2-y1,2)})
    return out
man=K([(.36,.79,.29,.85),(.38,.79,.28,.85),(.38,.79,.24,.85),(.42,.79,.16,.85),(.45,.78,.10,.85),(.45,.79,.08,.84),(.47,.79,.07,.84),(.47,.79,.07,.84)])
ewe=K([(0.0,.36,.49,.79),(0.0,.38,.49,.79),(0.0,.38,.48,.79),(0.0,.41,.47,.79),(0.0,.43,.48,.78),(0.0,.44,.47,.79),(0.0,.45,.51,.80),(0.0,.46,.51,.80)])
dog=K([(.79,.97,.50,.72),(.79,.97,.49,.72),(.79,.97,.49,.70),(.79,.97,.49,.71),(.78,.97,.47,.70),(.79,.97,.47,.70),(.79,.99,.47,.70),(.79,.99,.47,.73)])
c={"mediaId":6902,"level":"B","keyWord":"bring in","defaultVoice":"male",
"taps":[{"phrase":"to set a lamb down gently","target":"the young man","voice":"male","keys":man},
{"phrase":"to sniff the newborn lamb","target":"the ewe","voice":"male","keys":ewe},
{"phrase":"to sit by the metal gate","target":"the sheepdog","voice":"male","keys":dog}],
"stillS":2.7,
"nouns":[{"word":"a ewe","x":0.20,"y":0.58,"voice":"male"},{"word":"a lamb","x":0.58,"y":0.72,"voice":"male"},
{"word":"a towel","x":0.64,"y":0.43,"voice":"male"},{"word":"a sheepdog","x":0.86,"y":0.56,"voice":"male"}],
"question":"What is the ewe doing?",
"answer":["The","ewe","is","sniffing","the","newborn","lamb."],
"answerVoice":"male",
"notes":"Man's box split from the ewe at x 0.36-0.38 while he bends (0.2-1.2 s; his head is slightly clipped) and from the sheepdog at x 0.79 (his jacket back is clipped; the dog sits just behind his boots). The man sets the lamb down only in 0.2-1.2 s. Many sheep in the flock behind; only the front ewe sniffs the lamb."}
json.dump(c,open('content/6902.json','w'),indent=1)

import json
T=[i*0.5 for i in range(19)]
boy={0.0:(.05,.24,.90,.76),0.5:(.04,.24,.94,.76),1.0:(.06,.23,.92,.77),1.5:(.02,.21,.94,.79),2.0:(.02,.19,.97,.81),
2.5:(.02,.21,.97,.79),3.0:(.02,.18,.98,.82),3.5:(0,.16,1,.84),4.0:(.06,.21,.94,.79),4.5:(0,.14,1,.86),5.0:(.08,.14,.92,.86),
5.5:(0,.15,1,.85),6.0:(0,.16,1,.84),6.5:(0,.16,1,.84),7.0:(0,.20,1,.80),7.5:(0,.15,1,.85),8.0:(0,0,.72,1),8.5:(0,.02,.65,.98),9.0:(0,.12,.64,.88)}
wag={8.5:(.67,.47,.25,.30),9.0:(.66,.52,.33,.33)}
def keys(d):
    out=[]
    for t in T:
        if t in d: x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
c={"mediaId":5187,"level":"B","keyWord":"wagon","defaultVoice":"male",
"taps":[{"phrase":"to haul a heavy rope","target":"the boy","voice":"male","keys":keys(boy)},
{"phrase":"to grit his teeth","target":"the boy","voice":"male","keys":keys(boy)},
{"phrase":"to stand empty in the field","target":"the wagon","voice":"male","keys":keys(wag)}],
"stillS":9.0,
"nouns":[{"word":"the sky","x":0.60,"y":0.12,"voice":"male"},{"word":"a T-shirt","x":0.24,"y":0.52,"voice":"male"},
{"word":"a wagon","x":0.80,"y":0.63,"voice":"male"},{"word":"grass","x":0.80,"y":0.91,"voice":"male"}],
"question":"What is the boy doing?","answer":["He","is","hauling","a","heavy","rope."],"answerVoice":"male",
"notes":"Description says green wagon rolling; in the frames it is a rusty brown farm wagon, visible clearly only at 8.5-9.0 (a dark edge of it shows at the left border 4.0-7.0, marked off). Wagon never visibly rolls, so its phrase is a state. Boy fills almost the whole frame until 7.5."}
json.dump(c,open('content/5187.json','w'),indent=1)

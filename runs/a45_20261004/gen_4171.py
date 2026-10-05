import json
T=[i*0.5 for i in range(25)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
hen={0.0:(0.34,0.10,0.66,0.74),0.5:(0.33,0.10,0.67,0.74),2.5:(0.20,0.18,0.74,0.64),3.0:(0.0,0.06,1.0,0.88),3.5:(0.0,0.05,1.0,0.93),
 5.5:(0.0,0.0,1.0,1.0),6.0:(0.0,0.0,1.0,1.0),6.5:(0.0,0.0,1.0,1.0),7.0:(0.0,0.0,1.0,1.0),
 7.5:(0.0,0.0,1.0,0.50),8.0:(0.0,0.0,1.0,0.48),8.5:(0.0,0.0,1.0,0.58),9.0:(0.02,0.0,0.98,0.62),
 11.5:(0.0,0.24,0.68,0.38),12.0:(0.02,0.24,0.64,0.44)}
wolf={1.5:(0.18,0.02,0.82,0.95),2.0:(0.0,0.0,1.0,1.0),4.0:(0.03,0.0,0.97,0.90),4.5:(0.0,0.0,1.0,0.88),5.0:(0.0,0.28,1.0,0.70),
 9.5:(0.0,0.0,1.0,0.95),10.0:(0.0,0.0,1.0,0.95),10.5:(0.0,0.0,1.0,0.95),11.0:(0.0,0.0,1.0,0.95),
 11.5:(0.30,0.62,0.70,0.38),12.0:(0.30,0.68,0.70,0.32)}
c={"mediaId":4171,"level":"B","keyWord":"creep","defaultVoice":"male",
"taps":[
 {"phrase":"to creep through the bushes","target":"the wolf","voice":"male","keys":keys(wolf)},
 {"phrase":"to close its amber eyes","target":"the wolf","voice":"male","keys":keys(wolf)},
 {"phrase":"to shield her chicks","target":"the hen","voice":"male","keys":keys(hen)}],
"stillS":2.5,
"nouns":[{"word":"a wildfire","x":0.62,"y":0.06,"voice":"male"},{"word":"a waterfall","x":0.38,"y":0.20,"voice":"male"},
 {"word":"a hen","x":0.55,"y":0.50,"voice":"male"},{"word":"chicks","x":0.45,"y":0.80,"voice":"male"}],
"question":"What is the wolf doing?",
"answer":["It","is","creeping","through","the","bushes."],
"answerVoice":"male",
"notes":"Two phrases share the wolf (the chicks only appear as a group, the bamboo tube does nothing by itself). The wolf comes through the leaves at 1.5-2.0 (1.0 shows only leaves: off) and its eyes are closed at 9.5-10.5 and 11.5-12.0; the hen's eyes look half closed in the tiny last shot, possible doubt. Hen with spread wings over the chicks at 3.0-3.5 = 'to shield her chicks'. In 7.5-9.0 only the hen's body is in the picture (box = upper part). Last shot 11.5-12.0: hen and wolf overlap, split horizontally, part of each lies outside its box."}
json.dump(c,open("content/4171.json","w"),indent=1)

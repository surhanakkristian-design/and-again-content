import json
T=[i*0.5 for i in range(25)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
F=(0.0,0.0,1.0,1.0)
hen={0.0:F,0.5:F,1.0:F,1.5:F,2.0:(0.0,0.26,0.35,0.68),2.5:(0.0,0.41,0.32,0.49),3.0:(0.0,0.43,0.33,0.42),3.5:(0.0,0.40,0.42,0.50),
 4.0:(0.0,0.30,0.45,0.58),4.5:(0.27,0.07,0.73,0.67),5.0:(0.35,0.30,0.65,0.70),5.5:(0.0,0.0,0.75,0.65),6.0:(0.29,0.03,0.64,0.44),
 6.5:(0.17,0.05,0.83,0.85),7.0:(0.0,0.04,0.88,0.94),7.5:(0.0,0.30,1.0,0.70),8.0:(0.0,0.10,1.0,0.67),8.5:(0.0,0.20,1.0,0.52),
 9.0:(0.12,0.08,0.83,0.82),9.5:(0.0,0.17,1.0,0.77),10.0:(0.0,0.19,1.0,0.63),10.5:(0.12,0.08,0.79,0.74),11.0:(0.15,0.13,0.70,0.81),
 11.5:(0.19,0.20,0.62,0.70),12.0:(0.24,0.27,0.51,0.50)}
wolf={2.0:(0.36,0.24,0.36,0.22),2.5:(0.33,0.21,0.38,0.42),3.0:(0.34,0.13,0.50,0.43),3.5:(0.43,0.0,0.57,0.64),
 5.5:(0.17,0.67,0.50,0.33),6.0:(0.24,0.62,0.58,0.25)}
c={"mediaId":4173,"level":"B","keyWord":"chase","defaultVoice":"male",
"taps":[
 {"phrase":"to bare its teeth","target":"the wolf","voice":"male","keys":keys(wolf)},
 {"phrase":"to plunge into the mist","target":"the wolf","voice":"male","keys":keys(wolf)},
 {"phrase":"to cling to the rope","target":"the hen","voice":"male","keys":keys(hen)}],
"stillS":2.5,
"nouns":[{"word":"a wolf","x":0.52,"y":0.32,"voice":"male"},{"word":"a hen","x":0.14,"y":0.60,"voice":"male"},
 {"word":"planks","x":0.58,"y":0.85,"voice":"male"}],
"question":"What is the wolf doing?",
"answer":["It","is","chasing","the","hen","across","the","bridge."],
"answerVoice":"male",
"notes":"Key word 'chase' is used as a verb in the answer. Two phrases share the wolf (chicks only as a group on the hen). Wolf bares its teeth at 3.0-3.5, falls into the mist at 5.5-6.0; at 4.0 it is only a dark motion blur (off). Hen and wolf overlap at 2.0-3.5 (her outstretched wing runs under the wolf): split vertically, the wing tip is outside the hen box. At 5.0 only the hen's wing on the rope is visible (boxed as the hen). Only 3 nouns: ropes/posts exist on both sides, no single clear place."}
json.dump(c,open("content/4173.json","w"),indent=1)

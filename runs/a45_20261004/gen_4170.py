import json
T=[i*0.5 for i in range(24)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
hen={0.0:(0.17,0.0,0.83,0.47),0.5:(0.0,0.0,1.0,0.47),1.0:(0.0,0.0,0.82,0.48),1.5:(0.0,0.08,0.70,0.40),2.0:(0.0,0.13,0.57,0.33),
 4.0:(0.0,0.18,1.0,0.64),4.5:(0.0,0.0,1.0,0.70),5.0:(0.02,0.20,0.88,0.62),5.5:(0.0,0.55,0.82,0.40),
 6.0:(0.0,0.36,0.66,0.48),6.5:(0.0,0.26,0.62,0.46),7.0:(0.0,0.27,0.68,0.23),7.5:(0.0,0.13,0.55,0.64),
 8.0:(0.28,0.44,0.42,0.26),8.5:(0.0,0.12,1.0,0.27),9.0:(0.0,0.0,1.0,0.50),9.5:(0.0,0.0,1.0,0.47),
 10.0:(0.0,0.0,1.0,0.50),10.5:(0.0,0.0,1.0,0.46),11.0:(0.0,0.08,1.0,0.40),11.5:(0.0,0.08,1.0,0.34)}
chick={0.0:(0.49,0.47,0.40,0.23),0.5:(0.49,0.47,0.40,0.23),1.0:(0.49,0.48,0.40,0.23),1.5:(0.50,0.48,0.42,0.24),2.0:(0.53,0.47,0.42,0.23),
 2.5:(0.0,0.0,1.0,0.52),3.0:(0.0,0.0,1.0,0.65),
 6.0:(0.74,0.49,0.26,0.22),6.5:(0.63,0.45,0.32,0.21),7.0:(0.46,0.51,0.38,0.19),7.5:(0.55,0.26,0.28,0.28),
 8.5:(0.22,0.39,0.50,0.28),9.0:(0.20,0.50,0.50,0.43),9.5:(0.20,0.47,0.50,0.46),
 10.0:(0.26,0.52,0.40,0.29),10.5:(0.29,0.47,0.34,0.34),11.0:(0.29,0.48,0.32,0.40),11.5:(0.36,0.42,0.28,0.44)}
c={"mediaId":4170,"level":"A","keyWord":"save","defaultVoice":"female",
"taps":[
 {"phrase":"to save a little chick","target":"the hen","voice":"female","keys":keys(hen)},
 {"phrase":"to jump into the water","target":"the hen","voice":"female","keys":keys(hen)},
 {"phrase":"to carry a white flower","target":"the chick with the flower","voice":"female","keys":keys(chick)}],
"stillS":0.5,
"nouns":[{"word":"a hen","x":0.50,"y":0.25,"voice":"female"},{"word":"chicks","x":0.22,"y":0.54,"voice":"female"},
 {"word":"a flower","x":0.80,"y":0.55,"voice":"female"},{"word":"ice","x":0.50,"y":0.82,"voice":"female"}],
"question":"What is the hen doing?",
"answer":["She","is","saving","a","little","chick."],
"answerVoice":"female",
"notes":"Two phrases share the hen (only two separable targets: hen and the chick with the flower). Close-up 2.5-3.0 shows one chick's body without the flower; assumed to be the flower chick (the one that falls). The chick falls through the ice, the hen jumps in after it (4.0-5.0). Hen and chick overlap in 7.0-11.5: split along the line between them, the hen's lower body/wings are outside her box there. 'chicks' pill sits on the three chicks left, 'a flower' pill on the daisy of the fourth."}
json.dump(c,open("content/4170.json","w"),indent=1)

import json
def K(times, boxes):
    out=[]
    for t,b in zip(times,boxes):
        if b is None: out.append({"t":t,"off":True})
        else:
            x0,y0,x1,y1=b; x0=max(0,x0);y0=max(0,y0);x1=min(1,x1);y1=min(1,y1)
            out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
woman=K(T,[(0.46,0.20,0.88,0.86),(0.50,0.21,0.90,0.94),(0.52,0.26,0.84,1.0),(0.52,0.22,0.99,1.0),
           (0.55,0.20,1.0,1.0),(0.61,0.18,1.0,1.0),(0.64,0.18,1.0,1.0),(0.67,0.17,1.0,1.0)])
crate=K(T,[(0.14,0.30,0.46,0.57),(0.14,0.29,0.50,0.55),(0.12,0.36,0.52,0.61),(0.06,0.43,0.52,0.71),
           (0.05,0.45,0.55,0.75),(0.06,0.45,0.61,0.78),(0.07,0.46,0.64,0.79),(0.06,0.46,0.67,0.79)])
c={"mediaId":5687,"level":"B","keyWord":"bringing","defaultVoice":"female",
"taps":[{"phrase":"to deliver fresh loaves","target":"the cyclist","voice":"female","keys":woman},
{"phrase":"to get off her cargo bike","target":"the cyclist","voice":"female","keys":woman},
{"phrase":"to be packed with loaves","target":"the crate of bread","voice":"female","keys":crate}],
"stillS":3.2,
"nouns":[{"word":"fairy lights","x":0.72,"y":0.14,"voice":"female"},{"word":"a cyclist","x":0.86,"y":0.45,"voice":"female"},
{"word":"loaves","x":0.40,"y":0.52,"voice":"female"},{"word":"a crate","x":0.35,"y":0.66,"voice":"female"}],
"question":"What is the cyclist doing?","answer":["She","is","delivering","fresh","loaves."],"answerVoice":"female",
"notes":"Crate and cyclist split vertically where her arms hold the crate (0.2-2.2): her forearms/hands lie in the crate box. At 2.7-3.2 her raised arm (left of her body) is outside her box to keep it off the crate box. A second, empty crate sits on the cargo bike at 0.2-1.2, hence target 'the crate of bread'; stall baskets hold rolls, not loaves. The onlookers are many and blurred, not used as a target. Key word 'bringing' (noun) is not a visible thing."}
json.dump(c,open('content/5687.json','w'),indent=1)

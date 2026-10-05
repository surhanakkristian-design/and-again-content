import json
T=[i*0.5 for i in range(17)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
woman={0.0:(0.23,0.21,0.43,0.77),0.5:(0.26,0.21,0.41,0.77),1.0:(0.24,0.21,0.42,0.77),1.5:(0.24,0.22,0.42,0.76),2.0:(0.18,0.23,0.45,0.75),
2.5:(0.19,0.25,0.46,0.74),3.0:(0.16,0.24,0.47,0.75),3.5:(0.16,0.22,0.52,0.76),4.0:(0.17,0.24,0.35,0.70),4.5:(0.16,0.22,0.36,0.68),
5.0:(0.05,0.13,0.59,0.66),5.5:(0.0,0.17,0.48,0.56),6.0:(0.0,0.29,0.48,0.35),6.5:(0.0,0.33,0.47,0.34),7.0:(0.0,0.34,0.49,0.43),
7.5:(0.0,0.32,0.53,0.44),8.0:(0.0,0.28,0.52,0.36)}
bottle={4.0:(0.52,0.30,0.30,0.70),4.5:(0.52,0.30,0.33,0.70),5.0:(0.47,0.79,0.24,0.16),5.5:(0.48,0.0,0.30,0.82),6.0:(0.48,0.0,0.30,0.72),
6.5:(0.47,0.0,0.36,0.74),7.0:(0.49,0.03,0.32,0.82),7.5:(0.53,0.06,0.25,0.77),8.0:(0.52,0.10,0.28,0.62)}
wk=keys(woman)
d={"mediaId":4056,"level":"A","keyWord":"celebration","defaultVoice":"female",
"taps":[
{"phrase":"to open a bottle","target":"the woman","voice":"female","keys":wk},
{"phrase":"to laugh a lot","target":"the woman","voice":"female","keys":wk},
{"phrase":"to make the ground wet","target":"the bottle","voice":"female","keys":keys(bottle)}],
"stillS":7.5,
"nouns":[{"word":"a wall","x":0.30,"y":0.15,"voice":"female"},{"word":"a woman","x":0.25,"y":0.50,"voice":"female"},{"word":"a bottle","x":0.57,"y":0.66,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","opening","a","bottle","and","laughing."],
"answerVoice":"female",
"notes":"Key word 'celebration' is abstract, not used as a noun. Only two targets (woman, bottle). The bottle is OFF at 0-3.5 s: she holds it in front of her body, it cannot be separated from her box; from 4.0 s (she lets go, it stands on the ground and sprays) it has its own box, which includes the white jet where that is free of her. At 5.0 s the bottle box is only the bottle (her arm is above it). Her outstretched hand is cut a little at 4.5, 6.0, 8.0 s. She opens the bottle only in the first 3 s."}
json.dump(d,open("content/4056.json","w"),indent=1,ensure_ascii=False)

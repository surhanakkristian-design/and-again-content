import json
T=[i*0.5 for i in range(21)]
def K(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
woman={0.0:(0.05,0.34,0.85,0.66),0.5:(0.0,0.24,0.34,0.76),1.0:(0.0,0.20,0.50,0.80),1.5:(0.0,0.17,0.54,0.83),2.0:(0.0,0.17,0.52,0.70),
2.5:(0.0,0.24,0.49,0.64),3.0:(0.0,0.44,0.50,0.56),3.5:(0.17,0.22,0.41,0.75),4.0:(0.14,0.20,0.42,0.72),4.5:(0.09,0.21,0.46,0.70),
5.0:(0.16,0.22,0.35,0.76),5.5:(0.08,0.17,0.48,0.78),6.0:(0.09,0.20,0.42,0.73),6.5:(0.06,0.29,0.43,0.69),7.0:(0.06,0.27,0.40,0.73),
7.5:(0.06,0.27,0.38,0.73),8.0:(0.08,0.37,0.38,0.53),8.5:(0.02,0.52,0.47,0.30),9.0:(0.0,0.52,0.36,0.34),9.5:(0.02,0.46,0.48,0.42),10.0:(0.0,0.42,0.48,0.44)}
man={0.5:(0.40,0.36,0.58,0.64),1.0:(0.62,0.24,0.38,0.76),1.5:(0.66,0.25,0.34,0.75),2.0:(0.56,0.29,0.44,0.64),
2.5:(0.51,0.27,0.49,0.70),3.0:(0.50,0.39,0.39,0.61),3.5:(0.59,0.36,0.33,0.64),4.0:(0.56,0.36,0.36,0.52),4.5:(0.55,0.29,0.36,0.60),
5.0:(0.52,0.27,0.38,0.72),5.5:(0.57,0.30,0.41,0.68),6.0:(0.57,0.21,0.38,0.70),6.5:(0.58,0.25,0.40,0.68),7.0:(0.57,0.27,0.38,0.73),
7.5:(0.57,0.25,0.41,0.75),8.0:(0.52,0.34,0.43,0.56),8.5:(0.50,0.52,0.50,0.30),9.0:(0.50,0.46,0.50,0.38),9.5:(0.51,0.46,0.49,0.40),10.0:(0.50,0.42,0.50,0.36)}
c={"mediaId":292,"level":"A","keyWord":"fight","defaultVoice":"female",
"taps":[
 {"phrase":"to lift a pillow high","target":"the woman","voice":"female","keys":K(woman)},
 {"phrase":"to wear a grey T-shirt","target":"the woman","voice":"female","keys":K(woman)},
 {"phrase":"to have a beard","target":"the man","voice":"male","keys":K(man)}],
"stillS":6.0,
"nouns":[{"word":"a window","x":0.32,"y":0.13,"voice":"female"},{"word":"a pillow","x":0.58,"y":0.34,"voice":"female"},{"word":"a plant","x":0.53,"y":0.52,"voice":"female"},{"word":"a bed","x":0.50,"y":0.85,"voice":"female"}],
"question":"What are they doing on the bed?",
"answer":["They","are","having","a","pillow","fight."],
"answerVoice":"female",
"notes":"Both people swing pillows, jump, laugh, fall and give a thumbs-up, so the phrases use what is only one person's: the woman lifts her pillow above her head (0.0-2.0 s, 3.5 s) while the man holds his in front of him; grey vs white T-shirt (the man's SHORTS are grey); the beard. At 0.0 s only the woman is in the picture. The two are very close from 2.5 s on (boxes split along a vertical line between them); at 9.0 s they tumble backwards and the legs are tangled - boxes are approximate there. Mixed couple -> defaultVoice from evenId (female); answer subject 'They' -> default voice. Still 6.0 s: more pillows lie on the bed behind them; the pill sits on the one they hold."}
json.dump(c,open("content/292.json","w"),indent=1)

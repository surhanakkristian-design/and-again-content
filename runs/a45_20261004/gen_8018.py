import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,boxes)]
def B(x0,y0,x1,y1): return (round(x0,2),round(y0,2),round(x1-x0,2),round(y1-y0,2))
bride=[B(0.27,0.39,0.46,0.82),B(0.28,0.39,0.45,0.83),B(0.19,0.36,0.44,0.85),B(0.23,0.36,0.45,0.87),B(0.19,0.32,0.46,0.87),B(0.18,0.29,0.45,0.89),B(0.16,0.28,0.46,0.90),B(0.15,0.26,0.47,0.94)]
groom=[B(0.46,0.38,0.69,0.81),B(0.45,0.38,0.70,0.83),B(0.44,0.39,0.69,0.86),B(0.45,0.39,0.70,0.88),B(0.46,0.35,0.72,0.88),B(0.45,0.34,0.73,0.89),B(0.46,0.34,0.78,0.93),B(0.47,0.32,0.81,0.96)]
c={"mediaId":8018,"level":"B","keyWord":"take place","defaultVoice":"female",
"taps":[
 {"phrase":"to lift a bridal bouquet","target":"the bride","voice":"female","keys":K(bride)},
 {"phrase":"to punch the air","target":"the groom","voice":"male","keys":K(groom)},
 {"phrase":"to hold the bride's hand","target":"the groom","voice":"male","keys":K(groom)}],
"stillS":2.2,
"nouns":[{"word":"a glass roof","x":0.50,"y":0.08,"voice":"female"},
 {"word":"a spiral staircase","x":0.50,"y":0.24,"voice":"female"},
 {"word":"a bouquet","x":0.27,"y":0.39,"voice":"female"},
 {"word":"a palm tree","x":0.84,"y":0.36,"voice":"female"}],
"question":"What is the groom doing?",
"answer":["He","is","punching","the","air."],
"answerVoice":"male",
"notes":"Only two clear single targets (bride, groom); the bridesmaids and guests are groups that clap/dance together, so the groom carries two phrases. Bride and groom boxes are split on the line between them (their joined hands sit on the line). The bride's bouquet is clearly raised from 1.2; at 0.2-0.7 her arm is up but the bouquet is hard to see against the flower arch. defaultVoice female: the main pair is mixed, evenId true."}
json.dump(c,open('content/8018.json','w'),indent=1)

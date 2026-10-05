import json
T=[i*0.5 for i in range(24)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
man={0.0:(0.35,0.31,0.18,0.14),0.5:(0.38,0.31,0.18,0.14),1.0:(0.41,0.32,0.18,0.14),1.5:(0.40,0.34,0.20,0.14),2.0:(0.38,0.35,0.26,0.23),
 2.5:(0.40,0.40,0.22,0.16),3.0:(0.23,0.37,0.42,0.21),3.5:(0.15,0.40,0.58,0.19)}
sea={4.0:(0.36,0.38,0.26,0.16),4.5:(0.36,0.38,0.26,0.16),5.0:(0.36,0.38,0.26,0.16),5.5:(0.36,0.38,0.26,0.16),6.0:(0.36,0.37,0.27,0.16)}
road={9.5:(0.30,0.24,0.44,0.70),10.0:(0.05,0.27,0.78,0.60),10.5:(0.25,0.28,0.40,0.58),11.0:(0.07,0.29,0.64,0.66),11.5:(0.28,0.29,0.38,0.67)}
c={"mediaId":4142,"level":"A","keyWord":"rain","defaultVoice":"female",
"taps":[
 {"phrase":"to fall into the water","target":"the man in the water","voice":"male","keys":keys(man)},
 {"phrase":"to swim in the sea","target":"the woman in the sea","voice":"female","keys":keys(sea)},
 {"phrase":"to dance on the road","target":"the woman in the white shirt","voice":"female","keys":keys(road)}],
"stillS":7.5,
"nouns":[{"word":"clouds","x":0.40,"y":0.15,"voice":"female"},{"word":"the sun","x":0.80,"y":0.39,"voice":"female"},
 {"word":"a road","x":0.50,"y":0.75,"voice":"female"}],
"question":"What is the woman in white doing?",
"answer":["She","is","dancing","in","the","rain."],
"answerVoice":"female",
"notes":"Key word 'rain' is a verb; it is used as a noun in the answer. The man is only a faint dark shape inside the wave at 0.0-1.0 and hardly visible in the foam at 2.5 (boxes kept on his place); he drops head first with the wave at 2.0 = 'to fall into the water' (verifier: check it reads as falling, not diving). 'to swim in the sea': the woman only floats with her head above the water; the man is in a pool on the beach, not swimming. Only 3 nouns (sunset road shot); nothing else is clearly nameable there."}
json.dump(c,open("content/4142.json","w"),indent=1)

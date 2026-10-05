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
man=K(T,[(0.03,0.38,0.72,1.0),(0.03,0.35,0.74,1.0),(0.0,0.35,0.70,1.0),(0.0,0.34,0.78,1.0),
         (0.0,0.33,0.80,1.0),(0.0,0.31,0.82,1.0),(0.0,0.34,0.77,1.0),(0.0,0.33,0.72,1.0)])
light=K(T,[(0.74,0.15,0.92,0.29),(0.76,0.14,0.94,0.28),(0.78,0.14,0.96,0.28),(0.79,0.12,0.97,0.26),
           (0.81,0.11,0.99,0.25),(0.82,0.10,1.0,0.24),(0.82,0.09,1.0,0.23),(0.82,0.09,1.0,0.23)])
c={"mediaId":5689,"level":"B","keyWord":"broadcast","defaultVoice":"male",
"taps":[{"phrase":"to adjust the sliders","target":"the man","voice":"male","keys":man},
{"phrase":"to speak into the microphone","target":"the man","voice":"male","keys":man},
{"phrase":"to glow above the door","target":"the red light","voice":"male","keys":light}],
"stillS":2.2,
"nouns":[{"word":"a radio mast","x":0.17,"y":0.31,"voice":"male"},{"word":"headphones","x":0.31,"y":0.48,"voice":"male"},
{"word":"a microphone","x":0.70,"y":0.57,"voice":"male"},{"word":"a mixing desk","x":0.74,"y":0.90,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","speaking","into","a","microphone."],"answerVoice":"male",
"notes":"Only one person; the red light is the second target (small, boxes padded to 0.18 x 0.14). Radio mast not used as a tap target because his head crosses it at 3.2-3.7. He moves the sliders at 0.2-1.7 and speaks at 0.2-2.7; at 3.7 he only touches his headphones. Key word 'broadcast' is a verb, not placed as a noun."}
json.dump(c,open('content/5689.json','w'),indent=1)

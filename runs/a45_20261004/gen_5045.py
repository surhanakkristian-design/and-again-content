import json
T=[i/2 for i in range(19)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)})
    return out
man={0.0:(0.02,0.24,1.0,1.0),0.5:(0.03,0.21,1.0,1.0),1.0:(0.0,0.19,1.0,1.0),1.5:(0.02,0.23,1.0,1.0),2.0:(0.0,0.25,1.0,1.0),
 2.5:(0.0,0.31,1.0,1.0),3.0:(0.0,0.26,1.0,1.0),3.5:(0.0,0.26,1.0,1.0),4.0:(0.0,0.27,1.0,1.0),
 6.5:(0.33,0.23,1.0,1.0),7.0:(0.14,0.36,1.0,1.0),7.5:(0.18,0.42,0.8,1.0),8.0:(0.32,0.44,0.72,0.91),8.5:(0.33,0.49,0.6,0.66),9.0:(0.37,0.49,0.57,0.63)}
radio={5.0:(0.15,0.39,1.0,0.93),5.5:(0.09,0.37,1.0,0.9),6.0:(0.0,0.32,0.93,0.84)}
c={"mediaId":5045,"level":"A","keyWord":"sound","defaultVoice":"male",
"taps":[
 {"phrase":"to touch his ear","target":"the young man","voice":"male","keys":keys(man)},
 {"phrase":"to put on headphones","target":"the young man","voice":"male","keys":keys(man)},
 {"phrase":"to have two big speakers","target":"the radio","voice":"male","keys":keys(radio)}],
"stillS":5.0,
"nouns":[{"word":"a poster","x":0.28,"y":0.13,"voice":"male"},{"word":"a shop","x":0.80,"y":0.12,"voice":"male"},
 {"word":"a radio","x":0.55,"y":0.60,"voice":"male"}],
"question":"What is the young man wearing?",
"answer":["He","is","wearing","big","headphones."],"answerVoice":"male",
"notes":"One man in all person shots (street 0.0-4.0, speaker wall 6.5-7.5, on stage 8.0-9.0, tiny at 8.5-9.0 behind raised hands). 4.5 is a blurred camera swing to a pole (nothing boxed). The boombox is called 'the radio' (A level); the speaker wall is not a target but also has round speakers - 'two big speakers' keeps the radio phrase specific. Key word 'sound' is abstract, not placed. Crowd not used: the man on stage also raises his arms."}
json.dump(c,open('content/5045.json','w'),indent=1)

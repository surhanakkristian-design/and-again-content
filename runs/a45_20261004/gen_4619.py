import json
T=[i*0.5 for i in range(25)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
M={0.0:(0,0,0.80,1.0),0.5:(0,0,0.86,1.0),1.0:(0,0,0.90,1.0),1.5:(0,0,0.90,1.0),2.0:(0,0,0.82,1.0),2.5:(0,0,0.72,1.0),
 3.0:(0,0,0.78,1.0),3.5:(0,0,0.86,0.80),4.0:(0,0,0.82,0.72),4.5:(0,0,0.82,0.70),5.0:(0,0,0.84,0.82),5.5:(0,0,0.82,0.86),
 6.0:(0,0,0.84,0.82),6.5:(0,0,0.86,0.86),7.0:(0,0,1.0,1.0),7.5:(0,0.03,0.92,0.97),8.0:(0,0.05,0.90,0.95),8.5:(0,0.13,0.88,0.87),
 9.0:(0,0.16,0.88,0.84),9.5:(0,0.16,0.88,0.84),10.0:(0,0.12,0.92,0.88),10.5:(0,0.04,1.0,0.96),11.0:(0,0,1.0,0.92),11.5:(0,0,1.0,0.90),12.0:(0,0,1.0,0.80)}
c={"mediaId":4619,"level":"A","keyWord":"raw","defaultVoice":"male",
"taps":[
 {"phrase":"to wash a raw chicken","target":"the man","voice":"male","keys":keys(M)},
 {"phrase":"to hold a big fish","target":"the man","voice":"male","keys":keys(M)},
 {"phrase":"to stand at the sink","target":"the man","voice":"male","keys":keys(M)}],
"stillS":9.5,
"nouns":[{"word":"a window","x":0.85,"y":0.30,"voice":"male"},{"word":"a sweater","x":0.15,"y":0.46,"voice":"male"},
 {"word":"a fish","x":0.44,"y":0.57,"voice":"male"},{"word":"a sink","x":0.70,"y":0.71,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","washing","a","raw","chicken."],
"answerVoice":"male",
"notes":"One target only (the man) for all three phrases: the chicken, the fish and the water are all in his hands / under his arms, so a second target could not get a box that does not overlap his. His box includes what he holds and is close to the whole picture in the close-ups. The answer names the chicken (3.0-6.5); he also rinses a bag of berries (0-2.0) and lifts a fish (7.5-12.0). US 'sweater' (key words in this set are US)."}
json.dump(c,open('content/4619.json','w'),indent=1)

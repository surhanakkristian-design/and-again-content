import json,sys
def keys(times, boxes):
    out=[]
    for t in times:
        b=boxes.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
T=[i*0.5 for i in range(19)]
baby={0.0:(0.0,0.36,1.0,0.62),0.5:(0.10,0.32,0.90,0.66),1.0:(0.08,0.33,0.92,0.65),1.5:(0.08,0.33,0.92,0.65),2.0:(0.02,0.36,0.98,0.62),2.5:(0.02,0.42,0.98,0.56)}
boy={3.0:(0.20,0.23,0.48,0.75),3.5:(0.06,0.15,0.94,0.85),4.0:(0.25,0.16,0.75,0.84)}
man={4.5:(0.05,0.20,0.93,0.80),5.0:(0.08,0.12,0.86,0.88),5.5:(0.06,0.22,0.93,0.78),6.0:(0.15,0.17,0.82,0.83),6.5:(0.0,0.30,1.0,0.70)}
c={"mediaId":5060,"level":"B","keyWord":"male","defaultVoice":"male",
"taps":[
 {"phrase":"to reach for a stacking toy","target":"the baby","voice":"male","keys":keys(T,baby)},
 {"phrase":"to ride a kick scooter","target":"the boy on the scooter","voice":"male","keys":keys(T,boy)},
 {"phrase":"to do pull-ups on a bar","target":"the man in the vest","voice":"male","keys":keys(T,man)}],
"stillS":8.0,
"nouns":[{"word":"a museum","x":0.30,"y":0.31,"voice":"male"},
 {"word":"a playground","x":0.17,"y":0.45,"voice":"male"},
 {"word":"a grandfather","x":0.30,"y":0.75,"voice":"male"},
 {"word":"a bench","x":0.80,"y":0.85,"voice":"male"}],
"question":"What is the man in blue doing?",
"answer":["He","is","carrying","a","toddler","on","his","shoulders."],
"answerVoice":"male",
"notes":"Montage of separate shots. Key word 'male' is not a placeable noun, left out of nouns. The man in the vest (4.5-6.5) looks like the same actor as the father in blue (7.0-9.0) but is boxed only in the vest shots; his pull-up target is off from 7.0. The adult hand holding the toy (0-2.5) lies partly inside the baby box. 'a museum' = colonnaded building in the background."}
json.dump(c,open('content/5060.json','w'),indent=1)

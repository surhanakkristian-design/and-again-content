import json
T=[i*0.5 for i in range(25)]
def K(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
man={0.0:(0.18,0.2,0.72,0.8),0.5:(0.2,0.14,0.8,0.86),1.0:(0.13,0.16,0.85,0.84),1.5:(0.08,0.1,0.92,0.9),
 8.5:(0.18,0.02,0.82,0.86),9.0:(0.12,0.06,0.88,0.94),9.5:(0.15,0.07,0.85,0.93),10.0:(0.12,0.06,0.88,0.9),
 10.5:(0.15,0.06,0.85,0.9),11.0:(0.13,0.09,0.87,0.9),11.5:(0.18,0.09,0.82,0.9),12.0:(0.2,0.1,0.78,0.88)}
wo={2.0:(0,0,0.95,0.6),2.5:(0,0,1,0.6),3.0:(0,0,1,0.58),3.5:(0,0,1,0.55),4.0:(0,0,1,0.55),4.5:(0,0,1,0.65),
 5.0:(0,0,1,0.65),5.5:(0,0,1,0.58),6.0:(0,0,1,0.66),6.5:(0,0,1,0.66),7.0:(0,0,1,0.5),7.5:(0,0,1,0.68),8.0:(0,0,1,0.66)}
c={"mediaId":5455,"level":"B","keyWord":"approval","defaultVoice":"male",
"taps":[{"phrase":"to clutch a black folder","target":"the young man","voice":"male","keys":K(man)},
{"phrase":"to stamp an open passport","target":"the woman","voice":"female","keys":K(wo)},
{"phrase":"to beam at his passport","target":"the young man","voice":"male","keys":K(man)}],
"stillS":10.0,
"nouns":[{"word":"ceiling lights","x":0.8,"y":0.12,"voice":"male"},
{"word":"a score card","x":0.14,"y":0.47,"voice":"male"},
{"word":"a passport","x":0.45,"y":0.6,"voice":"male"},
{"word":"a backpack","x":0.84,"y":0.74,"voice":"male"}],
"question":"What is the young man doing?",
"answer":["He","is","beaming","at","his","passport."],"answerVoice":"male",
"notes":"Woman OFF at 8.5 (only her hand reaches into the frame). Other people in the queue also hold number cards; 'a score card' pill sits on the front woman's card."}
json.dump(c,open('content/5455.json','w'),indent=1)

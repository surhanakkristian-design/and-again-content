import json
T=[i*0.5 for i in range(21)]
def keys(d):
    return [({"t":t,"off":True} if d.get(t) is None else dict(zip(("t","x","y","w","h"),(t,)+d[t]))) for t in T]
# waiter (x0,x1,ytop,ybot) ; glass top y
D={0.0:((0.0,0.96,0.0,0.68),0.68),0.5:((0.08,0.96,0.0,0.69),0.69),1.0:((0.18,0.94,0.0,0.69),0.69),
 1.5:((0.0,0.93,0.0,0.70),0.71),2.0:((0.0,0.83,0.0,0.72),0.72),2.5:((0.02,0.90,0.0,0.73),0.73),
 3.0:((0.0,0.93,0.0,0.73),0.74),3.5:((0.0,0.93,0.0,0.74),0.75),4.0:((0.0,0.93,0.0,0.74),0.75),
 4.5:((0.0,0.93,0.0,0.75),0.76),5.0:((0.0,0.93,0.0,0.76),0.77),5.5:((0.0,0.93,0.0,0.76),0.77),
 6.0:((0.0,0.93,0.0,0.77),0.78),6.5:((0.0,0.93,0.0,0.77),0.78),7.0:((0.0,0.93,0.0,0.77),0.78),
 7.5:((0.0,0.93,0.0,0.77),0.78),8.0:((0.08,0.92,0.0,0.77),0.78),8.5:((0.04,0.94,0.0,0.77),0.78),
 9.0:((0.04,0.94,0.0,0.77),0.78),9.5:((0.06,0.94,0.05,0.77),0.78),10.0:((0.03,0.80,0.0,0.75),0.76)}
WA,GL={},{}
for t,((x0,x1,y0,y1),gy) in D.items():
    WA[t]=(x0,y0,round(x1-x0,2),round(y1-y0,2))
    GL[t]=(0.39 if t==10.0 else 0.36,gy,0.28 if t!=10.0 else 0.27,0.15)
c={"mediaId":5175,"level":"B","keyWord":"moustache","defaultVoice":"male",
"taps":[{"phrase":"to raise the pot overhead","target":"the waiter","voice":"male","keys":keys(WA)},
{"phrase":"to set down a carafe","target":"the waiter","voice":"male","keys":keys(WA)},
{"phrase":"to fill up with tea","target":"the small glass","voice":"male","keys":keys(GL)}],
"stillS":8.0,
"nouns":[{"word":"a moustache","x":0.53,"y":0.15,"voice":"male"},{"word":"a metal jug","x":0.38,"y":0.45,"voice":"male"},
{"word":"an apron","x":0.50,"y":0.63,"voice":"male"},{"word":"a carafe","x":0.82,"y":0.78,"voice":"male"}],
"question":"What is the waiter doing?",
"answer":["He","is","pouring","tea","into","a","small","glass."],"answerVoice":"male",
"notes":"One continuous shot, one main person. The waiter first pours water from the glass carafe into the tulip glass (0-0.5 s) and sets the carafe down on the table (1.0-1.5 s), then lifts the metal pot above his head and pours a long stream of tea (3-7.5 s). Third target = the small tulip glass on its saucer, which fills with dark tea from 3.5 s (it holds only water before). The waiter's box stops just above the glass so the two boxes never overlap. Blurred customers in the background are not targets. 'a metal jug' = the metal tea pot in his hand at 8.0 s (the description calls it a pot); 'a carafe' = the glass water carafe on the table."}
json.dump(c,open('content/5175.json','w'),indent=1)

import json
T=[i*0.5 for i in range(21)]
def K(d):
    return [({"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3])) for t in T]
man={0.0:(0,.06,1,.94),0.5:(.08,.06,.92,.94),1.0:(0,.09,1,.91),1.5:(0,.09,1,.91),2.0:(0,.09,1,.91),2.5:(0,.13,1,.87),
3.0:(.02,.13,.96,.87),3.5:(.08,.15,.88,.85),4.0:(.04,.13,.95,.87),4.5:(.07,.12,.91,.88),5.0:(.10,0,.82,1),
5.5:(.04,.13,.90,.87),6.0:(.10,0,.82,1),6.5:(.06,.13,.93,.87),7.0:(0,.13,.92,.87),7.5:(0,.12,1,.88),8.0:(0,.10,.95,.90),
8.5:(0,.10,1,.90),9.0:(0,.10,1,.90),9.5:(0,.09,.98,.91),10.0:(0,.09,1,.91)}
k=K(man)
c={"mediaId":5442,"level":"B","keyWord":"sleeve","defaultVoice":"male",
"taps":[{"phrase":"to shrug off a parka","target":"the man","voice":"male","keys":k},
{"phrase":"to unwind a knitted scarf","target":"the man","voice":"male","keys":k},
{"phrase":"to strip to his thermals","target":"the man","voice":"male","keys":k}],
"stillS":9.0,
"nouns":[{"word":"a sleeve","x":0.12,"y":0.45,"voice":"male"},{"word":"a beard","x":0.48,"y":0.26,"voice":"male"},
{"word":"clothes","x":0.82,"y":0.76,"voice":"male"},{"word":"a boot","x":0.86,"y":0.92,"voice":"male"}],
"question":"What is the man taking off?","answer":["He","is","removing","his","winter","clothes."],"answerVoice":"male",
"notes":"Only one possible target (the man), so all three phrases share his keys; he fills most of the frame. Parka 0-1.5 s, scarf 2.0-3.0 s, ends in green thermal base layer 7.5-10 s. 'a sleeve' = his left sleeve (green thermal) at 9.0 s; 'clothes' = the heap on the bench at the right; 'a boot' = the snow boot on the floor bottom right. Answer uses 'removing' instead of 'taking off' so the chips allow only one word order."}
json.dump(c,open('content/5442.json','w'),indent=1)

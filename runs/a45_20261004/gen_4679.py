import json
T=[i*0.5 for i in range(21)]
man={0.0:(0,0.03,1,0.67),0.5:(0,0.03,1,0.66),1.0:(0,0.05,1,0.65),1.5:(0,0.03,1,0.66),2.0:(0,0.01,1,0.67),2.5:(0,0.01,1,0.67),3.0:(0,0.02,1,0.70),3.5:(0,0.03,1,0.70),4.0:(0,0.09,1,0.59),4.5:(0,0.09,1,0.59),5.0:(0,0.03,1,0.73),5.5:(0,0,1,0.72),6.0:(0,0,1,0.64),6.5:(0,0.03,1,0.65),7.0:(0,0.03,1,0.76),7.5:(0,0.05,1,0.74),8.0:(0,0.04,1,0.64),8.5:(0,0.02,1,0.66),9.0:(0,0.05,1,0.72),9.5:(0,0.05,1,0.76),10.0:(0,0.05,1,0.68)}
def keys(d):
    return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in T]
c={"mediaId":4679,"level":"A","keyWord":"delicious","defaultVoice":"male",
"taps":[
 {"phrase":"to eat a delicious taco","target":"the young man","voice":"male","keys":keys(man)},
 {"phrase":"to close his eyes","target":"the young man","voice":"male","keys":keys(man)},
 {"phrase":"to lick his fingers","target":"the young man","voice":"male","keys":keys(man)}],
"stillS":0.0,
"nouns":[{"word":"a cap","x":0.28,"y":0.12,"voice":"male"},{"word":"a T-shirt","x":0.35,"y":0.50,"voice":"male"},{"word":"tacos","x":0.55,"y":0.80,"voice":"male"}],
"question":"What is the young man eating?",
"answer":["He","is","eating","a","delicious","taco."],
"answerVoice":"male",
"notes":"One target for all three phrases: the cooks in the background are small, blurred, change between shots and stand behind the man's head, so no clean tap box. The man's box takes the full width and so covers the background cooks (they are not targets). Fingers licked at about 2.5 s. 'tacos' = the two on the paper; he also holds a third one at 0.0 s."}
json.dump(c,open("content/4679.json","w"),indent=1)

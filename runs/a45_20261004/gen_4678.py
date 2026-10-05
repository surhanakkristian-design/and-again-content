import json
T=[i*0.5 for i in range(21)]
wom={2.5:(0,0.05,1,0.63),3.0:(0,0.06,1,0.66),3.5:(0,0.06,1,0.64),4.0:(0,0.05,1,0.62),4.5:(0,0.04,1,0.62),5.0:(0,0.03,1,0.70)}
man={5.5:(0.55,0.34,0.45,0.28),6.0:(0.58,0.12,0.42,0.48),6.5:(0.47,0.10,0.53,0.55),7.0:(0.40,0.03,0.60,0.75),7.5:(0.35,0.02,0.65,0.80)}
boy={8.0:(0,0.02,1,0.68),8.5:(0,0.03,1,0.68),9.0:(0,0.04,1,0.80),9.5:(0,0.05,1,0.80),10.0:(0,0.09,1,0.65)}
def keys(d):
    return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in T]
c={"mediaId":4678,"level":"A","keyWord":"eat","defaultVoice":"female",
"taps":[
 {"phrase":"to eat long noodles","target":"the woman","voice":"female","keys":keys(wom)},
 {"phrase":"to eat with a fork","target":"the man with the fork","voice":"male","keys":keys(man)},
 {"phrase":"to eat with both hands","target":"the boy","voice":"male","keys":keys(boy)}],
"stillS":4.5,
"nouns":[{"word":"hair","x":0.30,"y":0.28,"voice":"female"},{"word":"noodles","x":0.53,"y":0.60,"voice":"female"},{"word":"an egg","x":0.60,"y":0.83,"voice":"female"},{"word":"a bowl","x":0.40,"y":0.94,"voice":"female"}],
"question":"What is the woman eating?",
"answer":["She","is","eating","noodles","from","a","bowl."],
"answerVoice":"female",
"notes":"Four shots: bearded man with burger (0-2.0, no phrase), woman with ramen (2.5-5.0), man with fork in canteen (5.5-7.5; at 5.5-6.0 only his hand and arm are in the picture), boy with giant burger (8.0-10.0). 'to eat with both hands': the bearded man also holds a burger but with one visible hand; verifier may prefer another phrase. Boxes of woman and boy cover the person down to the food. defaultVoice female by evenId (mixed group)."}
json.dump(c,open("content/4678.json","w"),indent=1)

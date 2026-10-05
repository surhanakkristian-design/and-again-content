import json
def K(times, boxes):
    return [{"t":t,"off":True} if boxes.get(t) is None else dict(t=t,x=boxes[t][0],y=boxes[t][1],w=boxes[t][2],h=boxes[t][3]) for t in times]
T=[i*0.5 for i in range(21)]
old={0.0:(0,0.21,0.68,0.79),0.5:(0,0.21,0.7,0.79),1.0:(0,0.23,0.7,0.77),1.5:(0,0.24,0.72,0.76),2.0:(0,0.22,0.68,0.78),2.5:(0,0.19,0.64,0.81),3.0:(0,0.21,0.64,0.79),3.5:(0,0.21,0.72,0.79)}
wom={4.0:(0.25,0.2,0.75,0.7),4.5:(0.3,0.17,0.68,0.74),5.0:(0.28,0.21,0.58,0.76),5.5:(0.3,0.19,0.58,0.76),6.0:(0.22,0.16,0.6,0.71)}
man={6.5:(0.3,0.17,0.62,0.56),7.0:(0.32,0.2,0.54,0.53),7.5:(0.29,0.26,0.6,0.47),8.0:(0.3,0.27,0.56,0.47),8.5:(0.25,0.32,0.55,0.4),9.0:(0.11,0.37,0.78,0.31),9.5:(0.2,0.39,0.62,0.28),10.0:(0.24,0.42,0.5,0.22)}
d={"mediaId":5014,"level":"A","keyWord":"rich","defaultVoice":"female",
"taps":[
 {"phrase":"to taste the soup","target":"the old man","voice":"male","keys":K(T,old)},
 {"phrase":"to carry a hot dish","target":"the woman","voice":"female","keys":K(T,wom)},
 {"phrase":"to open his arms wide","target":"the man in black","voice":"male","keys":K(T,man)}],
"stillS":9.0,
"nouns":[{"word":"pans","x":0.5,"y":0.12,"voice":"female"},{"word":"the city","x":0.3,"y":0.36,"voice":"female"},{"word":"a man","x":0.5,"y":0.55,"voice":"male"},{"word":"a stove","x":0.15,"y":0.68,"voice":"female"}],
"question":"What is the woman carrying?",
"answer":["She","is","carrying","a","hot","dish."],
"answerVoice":"female",
"notes":"Three shots with hard cuts: old man 0-3.5, woman 4.0-6.0, man in black 6.5-10.0. Old man tastes from the spoon at 1.0-1.5 only. 'hot' inferred from oven + oven gloves. Mixed cast -> defaultVoice female (evenId true). Still 9.0: copper pans hang overhead; the frying pan on the board is small and not labelled."}
json.dump(d,open("content/5014.json","w"),indent=1)

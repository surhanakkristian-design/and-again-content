import json
def k(t,b): return {"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
T=[i*0.5 for i in range(19)]
young={0.0:(0.05,0.28,0.95,0.72),0.5:(0.08,0.26,0.92,0.74),1.0:(0.0,0.24,1.0,0.76),1.5:(0.0,0.21,1.0,0.79),2.0:(0.0,0.17,0.88,0.83)}
black={3.0:(0.30,0.30,0.70,0.70),3.5:(0.20,0.17,0.80,0.83),4.0:(0.02,0.21,0.98,0.79),4.5:(0.05,0.23,0.95,0.77),5.0:(0.0,0.27,0.92,0.73),5.5:(0.0,0.29,0.90,0.71),
6.0:(0.0,0.30,0.76,0.70),6.5:(0.0,0.31,0.64,0.69),7.0:(0.0,0.35,0.60,0.65),7.5:(0.0,0.37,0.60,0.63),8.0:(0.0,0.34,0.56,0.66),8.5:(0.0,0.34,0.53,0.66),9.0:(0.0,0.36,0.50,0.64)}
old={6.0:(0.76,0.28,0.24,0.62),6.5:(0.64,0.28,0.36,0.66),7.0:(0.60,0.28,0.40,0.72),7.5:(0.60,0.28,0.40,0.72),8.0:(0.56,0.26,0.44,0.74),8.5:(0.53,0.26,0.47,0.74),9.0:(0.50,0.27,0.50,0.73)}
keys=lambda d:[k(t,d.get(t)) for t in T]
c={"mediaId":4383,"level":"A","keyWord":"thick","defaultVoice":"male",
"taps":[
{"phrase":"to touch his chin","target":"the young man","voice":"male","keys":keys(young)},
{"phrase":"to have a thick black beard","target":"the man with the black beard","voice":"male","keys":keys(black)},
{"phrase":"to walk into the shop","target":"the old man","voice":"male","keys":keys(old)}],
"stillS":3.5,
"nouns":[{"word":"a comb","x":0.27,"y":0.45,"voice":"male"},{"word":"a beard","x":0.50,"y":0.62,"voice":"male"},{"word":"an ear","x":0.73,"y":0.37,"voice":"male"},{"word":"a shirt","x":0.70,"y":0.86,"voice":"male"}],
"question":"What does the old man have?",
"answer":["He","has","a","long","white","beard."],
"answerVoice":"male",
"notes":"Three shots: young man 0-2.0 (2.5 is a pan, off), bearded customer from 3.0, old man from 6.0. Phrase 2 is a state (key word thick): the customer's only action is sitting, which the young man also does. From 6.0 the two men overlap; boxes split on a vertical line. The young man touches his chin, the old man lifts his beard at 7.5-8.5 (hands on beard, not chin)."}
json.dump(c,open("content/4383.json","w"),indent=1,ensure_ascii=False)

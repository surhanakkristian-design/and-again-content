import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def keys(f): return [dict(t=t,**f(t)) for t in T]
woman=keys(lambda t: dict(x=0.12,y=0.31,w=0.68,h=0.69))
lamps=keys(lambda t: dict(x=0.80,y=0.03,w=0.20,h=0.40))
c={"mediaId":7195,"level":"B","keyWord":"greens","defaultVoice":"female",
"taps":[
 {"phrase":"to catch falling greens","target":"the chef","voice":"female","keys":woman},
 {"phrase":"to gaze up at flying leaves","target":"the chef","voice":"female","keys":woman},
 {"phrase":"to glow above the counter","target":"the copper lamps","voice":"female","keys":lamps}],
"stillS":3.2,
"nouns":[{"word":"copper pans","x":0.42,"y":0.10,"voice":"female"},
 {"word":"a chef","x":0.47,"y":0.62,"voice":"female"},
 {"word":"greens","x":0.89,"y":0.70,"voice":"female"},
 {"word":"a steel bowl","x":0.45,"y":0.93,"voice":"female"}],
"question":"What is the chef doing?",
"answer":["She","is","catching","falling","greens","in","a","steel","bowl."],
"answerVoice":"female",
"notes":"Two phrases share the chef (the cooks behind her overlap her box, so they are not targets). Lamp box stops at x .80; the chef's right hand reaches ~.84 at 3.2-3.7 s and is slightly outside her box. 'to gaze up' applies to 0.2-1.2 s only."}
json.dump(c,open('content/7195.json','w'),indent=1)

import json
T=[round(i*0.5,1) for i in range(21)]
def keys(d):
    return [dict(t=t,**dict(zip('xywh',d[t]))) if t in d else {'t':t,'off':True} for t in T]
g={0.0:(0.11,0.34,0.60,0.66),0.5:(0.27,0.36,0.44,0.64),1.0:(0.27,0.37,0.41,0.63),1.5:(0.32,0.36,0.36,0.64)}
d={5.0:(0.36,0.42,0.47,0.16),5.5:(0.29,0.40,0.43,0.16),6.0:(0.31,0.41,0.39,0.16),6.5:(0.23,0.35,0.22,0.14)}
cr={8.0:(0.0,0.38,0.82,0.33),8.5:(0.0,0.37,0.80,0.40),9.0:(0.0,0.37,0.92,0.50),9.5:(0.0,0.36,0.98,0.51),10.0:(0.0,0.36,0.98,0.40)}
c={"mediaId":4866,"level":"B","keyWord":"drone","defaultVoice":"female",
"taps":[
 {"phrase":"to hold a phone gimbal","target":"the man in the street","voice":"male","keys":keys(g)},
 {"phrase":"to hover above the field","target":"the drone","voice":"female","keys":keys(d)},
 {"phrase":"to burst into applause","target":"the crew","voice":"female","keys":keys(cr)}],
"stillS":5.5,
"nouns":[{"word":"the sky","x":0.40,"y":0.20,"voice":"female"},
 {"word":"a drone","x":0.52,"y":0.47,"voice":"female"},
 {"word":"trees","x":0.47,"y":0.61,"voice":"female"},
 {"word":"a field","x":0.50,"y":0.78,"voice":"female"}],
"question":"What is the drone doing?",
"answer":["The","drone","is","hovering","low","over","the","field."],
"answerVoice":"female",
"notes":"Montage of different people, no main person, evenId true -> female default. Gimbal man only 0-1.5 s; drone 5.0-6.5 s (small at 6.5 s, min-size box); crew 8.0-10 s (mixed group; at 8.0 s only a few members visible and not clapping yet; the seated camera operator in front is inside the crew box at 9-10 s since he is not a target). Target named 'the man in the street' because a man in a similar green hoodie stands in the crew at 8-10 s."}
json.dump(c,open('content/4866.json','w'),indent=1)

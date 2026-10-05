import json
def b(x,y,w,h): return {"x":x,"y":y,"w":w,"h":h}
times=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
Wm={0.2:b(0.02,0.39,0.30,0.23),0.7:b(0.04,0.39,0.28,0.23),1.2:b(0.02,0.42,0.27,0.20),1.7:b(0.04,0.40,0.28,0.22),2.2:b(0.02,0.39,0.31,0.23),2.7:b(0.04,0.39,0.30,0.23),3.2:b(0.02,0.40,0.31,0.24),3.7:b(0.04,0.40,0.30,0.23)}
Bf={0.2:b(0.38,0.21,0.62,0.57),0.7:b(0.33,0.19,0.67,0.59),1.2:b(0.30,0.13,0.70,0.69),1.7:b(0.33,0.11,0.67,0.71),2.2:b(0.50,0.20,0.50,0.59),2.7:b(0.58,0.20,0.42,0.60),3.2:b(0.62,0.21,0.38,0.60),3.7:b(0.63,0.22,0.37,0.60)}
Ht={t:b(0.63,0.83,0.37,0.17) for t in times}
def keys(d): return [dict(t=t,**d[t]) for t in times]
c={"mediaId":6908,"level":"B","keyWord":"buffalo","defaultVoice":"female",
"taps":[{"phrase":"to clutch a sandwich","target":"the woman","voice":"female","keys":keys(Wm)},
{"phrase":"to wander past the car","target":"the big buffalo","voice":"female","keys":keys(Bf)},
{"phrase":"to lie on the asphalt","target":"the straw hat","voice":"female","keys":keys(Ht)}],
"stillS":2.2,
"nouns":[{"word":"a buffalo","x":0.75,"y":0.45,"voice":"female"},{"word":"a straw hat","x":0.80,"y":0.93,"voice":"female"},{"word":"a convertible","x":0.24,"y":0.80,"voice":"female"},{"word":"mountains","x":0.55,"y":0.19,"voice":"female"}],
"question":"What is the big buffalo doing?","answer":["It","is","wandering","past","the","convertible."],"answerVoice":"female",
"notes":"More buffalo cross the road far behind; the tap target is the big one next to the car (named 'the big buffalo'), and the noun pill 'a buffalo' sits on the big one. At 1.2 the buffalo's muzzle nearly touches the windscreen: boxes split at x 0.29/0.30."}
json.dump(c,open('content/6908.json','w'),indent=1)

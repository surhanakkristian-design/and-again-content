import json
T=[i*0.5 for i in range(19)]
def keys(d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in T]
sol={0.0:(0.12,0.19,0.88,0.81),0.5:(0.15,0.16,0.85,0.84),1.0:(0.10,0.18,0.90,0.82),1.5:(0.08,0.18,0.92,0.82),
     2.0:(0,0.02,1,0.98),2.5:(0.20,0.17,0.80,0.83),3.0:(0.20,0.26,0.80,0.74),3.5:(0,0.28,1,0.72),
     4.0:(0.38,0.20,0.62,0.80),4.5:(0.14,0.24,0.82,0.76),5.0:(0.02,0.22,0.64,0.78),
     6.0:(0.55,0.20,0.25,0.75),6.5:(0,0.18,0.88,0.82),7.0:(0.10,0.18,0.75,0.82),7.5:(0.05,0.15,0.75,0.85),
     8.0:(0,0.10,0.85,0.90),8.5:(0,0,1,1),9.0:(0,0,1,1)}
wom={5.5:(0.08,0.28,0.82,0.72),6.0:(0,0.20,0.55,0.80)}
c={"mediaId":4942,"level":"B","keyWord":"luggage","defaultVoice":"male",
 "taps":[
  {"phrase":"to carry a duffel bag","target":"the soldier","voice":"male","keys":keys(sol)},
  {"phrase":"to tip his peaked cap","target":"the soldier","voice":"male","keys":keys(sol)},
  {"phrase":"to wear a long cream coat","target":"the woman in the cream coat","voice":"female","keys":keys(wom)}],
 "stillS":0.0,
 "nouns":[{"word":"luggage","x":0.84,"y":0.72,"voice":"male"},
          {"word":"a uniform","x":0.35,"y":0.62,"voice":"male"},
          {"word":"glass doors","x":0.25,"y":0.30,"voice":"male"}],
 "question":"What is the soldier carrying?",
 "answer":["He","is","carrying","a","duffel","bag","over","his","shoulder."],
 "answerVoice":"male",
 "notes":"Third phrase is a state: the cream-coat woman only hugs him (5.5-6.0 s) and the father and another woman also hug him at 7.0-7.5 s, so a hugging phrase would not be unique. Soldier marked off at 5.5 s (almost fully hidden behind her); at 6.0 s his box is only the visible strip right of her (split). Duffel bag visible 0.0-3.0 s."}
json.dump(c,open('content/4942.json','w'),indent=1)

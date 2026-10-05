import json
T=[i*0.5 for i in range(19)]
def k(t,b): return {"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
def keys(d): return [k(t,d.get(t)) for t in T]
man={2.0:(0.0,0.66,0.45,0.34),2.5:(0.42,0.56,0.29,0.44),3.0:(0.59,0.48,0.27,0.47),3.5:(0.6,0.49,0.28,0.36),4.0:(0.72,0.47,0.24,0.38)}
woman={1.5:(0.18,0.58,0.36,0.42),2.0:(0.47,0.52,0.27,0.4),2.5:(0.71,0.5,0.18,0.34)}
bld=dict(zip(T,[(0.04,0.16,0.44,0.17),(0.04,0.16,0.45,0.16),(0.06,0.16,0.45,0.17),(0.08,0.16,0.46,0.17),(0.11,0.15,0.45,0.16),
 (0.11,0.15,0.47,0.16),(0.11,0.16,0.45,0.17),(0.1,0.16,0.46,0.16),(0.06,0.12,0.49,0.18),(0.05,0.1,0.5,0.18),(0.04,0.09,0.5,0.21),
 (0.02,0.08,0.52,0.2),(0.01,0.06,0.53,0.21),(0.06,0.1,0.48,0.18),(0.07,0.09,0.49,0.2),(0.09,0.06,0.51,0.21),(0.12,0.03,0.52,0.2),
 (0.14,0.0,0.55,0.21),(0.15,0.0,0.55,0.21)]))
c={"mediaId":4897,"level":"A","keyWord":"join","defaultVoice":"male",
 "taps":[
  {"phrase":"to wear a white T-shirt","target":"the man in the white T-shirt","voice":"male","keys":keys(man)},
  {"phrase":"to carry a black bag","target":"the woman in the brown jacket","voice":"female","keys":keys(woman)},
  {"phrase":"to have a round roof","target":"the old building","voice":"male","keys":keys(bld)}],
 "stillS":1.0,
 "nouns":[{"word":"the sky","x":0.6,"y":0.08,"voice":"male"},
          {"word":"an old building","x":0.28,"y":0.27,"voice":"male"},
          {"word":"a crowd","x":0.5,"y":0.42,"voice":"male"},
          {"word":"a jacket","x":0.55,"y":0.88,"voice":"male"}],
 "question":"What are the people doing?",
 "answer":["They","are","joining","a","big","hug."],
 "answerVoice":"male",
 "notes":"Big crowd clip, few unique targets. White-T man visible 2.0-4.0 only (later other people in white tops appear - kept off). Brown-jacket woman visible 1.5-2.5 only, merges into the hug after. 'to have a round roof' = the dome on the old building (modern building has a flat roof). 'a jacket' = denim jacket of the man in the foreground at 1.0 s."}
json.dump(c,open("content/4897.json","w"),indent=1)

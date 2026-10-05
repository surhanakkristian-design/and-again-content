import json
W = [(0.18,0.27,0.46,0.67),(0.18,0.27,0.45,0.68),(0.12,0.24,0.45,0.75),(0.06,0.21,0.72,0.77),(0.06,0.0,0.94,1.0),
     (0.0,0.0,1.0,1.0),(0.20,0.09,0.80,0.91),(0.0,0.15,1.0,0.85),(0.0,0.12,0.58,0.88),(0.0,0.19,0.64,0.81),
     (0.0,0.17,0.62,0.83),(0.0,0.14,0.66,0.86),(0.0,0.15,0.55,0.85),(0.0,0.20,0.96,0.80),(0.0,0.28,1.0,0.72),
     (0.03,0.30,0.97,0.70),(0.06,0.18,0.94,0.82),(0.16,0.15,0.80,0.85),(0.03,0.09,0.95,0.91)]
def keys(L): return [dict(t=i*0.5,x=a,y=b,w=c,h=d) for i,(a,b,c,d) in enumerate(L)]
c = {"mediaId":5232,"level":"B","keyWord":"a yacht","defaultVoice":"female",
 "taps":[
  {"phrase":"to haul on a rope","target":"the woman","voice":"female","keys":keys(W)},
  {"phrase":"to crank a winch","target":"the woman","voice":"female","keys":keys(W)},
  {"phrase":"to punch the air","target":"the woman","voice":"female","keys":keys(W)}],
 "stillS":0.0,
 "nouns":[{"word":"a sail","x":0.40,"y":0.15,"voice":"female"},
          {"word":"a mountain","x":0.84,"y":0.51,"voice":"female"},
          {"word":"a yacht","x":0.12,"y":0.63,"voice":"female"},
          {"word":"a coil of rope","x":0.75,"y":0.85,"voice":"female"}],
 "question":"What is the woman holding?",
 "answer":["She","is","holding","a","coil","of","rope."],
 "answerVoice":"female",
 "notes":"All three phrases on the woman: the helmsman at the wheel (t=7.0-9.0) is tiny, blurred and sits right behind her shoulder, so no separate target. 'to haul on a rope' 0.0-1.5, 'to crank a winch' 4.0-5.5, 'to punch the air' 8.0-9.0. 'a yacht' pill sits on the varnished wooden side of the boat at left (the whole scene is the yacht's deck); weakest slot. Question answer refers to 6.0-9.0 (coil of rope in her hands)."}
json.dump(c, open('content/5232.json','w'), indent=1)

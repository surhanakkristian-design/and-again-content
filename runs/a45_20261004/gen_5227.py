import json
W = [(0.19,0.18,0.28,0.62),(0.27,0.18,0.25,0.54),(0.22,0.17,0.27,0.58),(0.21,0.18,0.33,0.34),
     (0.19,0.17,0.35,0.36),(0.19,0.18,0.35,0.34),(0.17,0.18,0.34,0.35),(0.18,0.18,0.33,0.36),
     (0.23,0.21,0.32,0.31),(0.31,0.21,0.29,0.29),(0.44,0.24,0.21,0.54),(0.38,0.25,0.29,0.27),
     (0.39,0.24,0.25,0.29),(0.36,0.24,0.28,0.30),(0.24,0.22,0.41,0.31),(0.21,0.23,0.40,0.29),
     (0.18,0.23,0.43,0.27),(0.17,0.25,0.41,0.26),(0.23,0.26,0.28,0.24),(0.30,0.28,0.23,0.22),(0.36,0.29,0.21,0.20)]
D = [(0.47,0.53,0.26,0.28),(0.52,0.52,0.26,0.24),(0.49,0.51,0.24,0.28),(0.40,0.52,0.25,0.21),
     (0.38,0.53,0.25,0.25),(0.38,0.52,0.27,0.26),(0.35,0.53,0.32,0.29),(0.36,0.54,0.37,0.27),
     (0.33,0.52,0.25,0.31),(0.24,0.50,0.27,0.26),(0.22,0.48,0.22,0.31),(0.29,0.52,0.27,0.30),
     (0.31,0.53,0.36,0.30),(0.35,0.54,0.42,0.37),(0.40,0.53,0.42,0.33),(0.43,0.52,0.44,0.40),
     (0.42,0.50,0.33,0.35),(0.37,0.51,0.25,0.32),(0.30,0.50,0.23,0.27),(0.28,0.50,0.20,0.23),(0.26,0.49,0.20,0.24)]
def keys(L): return [dict(t=i*0.5,x=a,y=b,w=c,h=d) for i,(a,b,c,d) in enumerate(L)]
c = {"mediaId":5227,"level":"B","keyWord":"several","defaultVoice":"female",
 "taps":[
  {"phrase":"to jog with several dogs","target":"the woman","voice":"female","keys":keys(W)},
  {"phrase":"to throw her arms up","target":"the woman","voice":"female","keys":keys(W)},
  {"phrase":"to lead the pack","target":"the border collie","voice":"female","keys":keys(D)}],
 "stillS":8.0,
 "nouns":[{"word":"the sky","x":0.40,"y":0.07,"voice":"female"},
          {"word":"the beach","x":0.82,"y":0.43,"voice":"female"},
          {"word":"a jogger","x":0.38,"y":0.36,"voice":"female"},
          {"word":"paving stones","x":0.50,"y":0.88,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","jogging","with","several","dogs."],
 "answerVoice":"female",
 "notes":"Woman and collie overlap (collie runs in front of her legs): boxes split horizontally at the collie's back, so her lower legs are outside her box in most frames. 'to throw her arms up' only from t=7.0 on. 'to lead the pack': collie stays in front of the other dogs throughout. A second mostly black dog with a white chest (left) also looks collie-like, so no 'border collie' noun slot."}
json.dump(c, open('content/5227.json','w'), indent=1)

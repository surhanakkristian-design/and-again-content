import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) if r else dict(t=t,off=True) for t,r in zip(T,rows)]
man=K([(0.46,0.32,0.30,0.50),(0.47,0.34,0.30,0.47),(0.48,0.36,0.32,0.45),(0.49,0.38,0.33,0.45),
       (0.48,0.41,0.30,0.48),(0.40,0.44,0.32,0.50),(0.30,0.58,0.33,0.42),(0.22,0.51,0.33,0.49)])
horse=K([(0.77,0.14,0.23,0.58),(0.78,0.14,0.22,0.58),(0.81,0.18,0.19,0.55),(0.83,0.17,0.17,0.55),
         (0.79,0.23,0.21,0.57),(0.73,0.26,0.27,0.60),(0.64,0.32,0.36,0.64),(0.57,0.35,0.43,0.60)])
leg=K([(0.0,0.58,0.41,0.40),(0.0,0.58,0.41,0.40),(0.0,0.62,0.32,0.37),(0.0,0.55,0.36,0.45),
       (0.0,0.55,0.25,0.43),None,None,None])
d={"mediaId":6905,"level":"B","keyWord":"bronze","defaultVoice":"male",
 "taps":[{"phrase":"to pour molten metal","target":"the young man","voice":"male","keys":man},
         {"phrase":"to stand on a wooden base","target":"the bronze horse","voice":"male","keys":horse},
         {"phrase":"to rise out of the sand","target":"the horse leg","voice":"male","keys":leg}],
 "stillS":2.7,
 "nouns":[{"word":"bronze","x":0.86,"y":0.45,"voice":"male"},
          {"word":"a crucible","x":0.27,"y":0.63,"voice":"male"},
          {"word":"a bell","x":0.15,"y":0.85,"voice":"male"},
          {"word":"an apron","x":0.55,"y":0.76,"voice":"male"}],
 "question":"What is the young man doing?",
 "answer":["He","is","pouring","molten","metal","into","a","funnel."],
 "answerVoice":"male",
 "notes":"Horse statue stands right behind the man: horse box keeps only the part right of the man (its head at x 0.6-0.75 is outside the box). The horse leg is a blurred foreground leg at the left; its box covers only the lower leg and hoof (also includes the sand mould column), off from 2.7 s where only a sliver remains. A second man enters at the left edge from 2.7 s (not a target). Pouring stops at about 2.5 s."}
json.dump(d,open("content/6905.json","w"),indent=1)

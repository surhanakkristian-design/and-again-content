import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def k(rows): return [dict(t=t,x=r[0],y=r[1],w=round(r[2]-r[0],2),h=round(r[3]-r[1],2)) for t,r in zip(T,rows)]
W=k([(0.02,0.27,0.42,0.66),(0.02,0.27,0.43,0.66),(0.07,0.28,0.45,0.66),(0.01,0.32,0.48,0.66),(0.01,0.33,0.53,0.67),(0.01,0.27,0.43,0.66),(0.02,0.21,0.40,0.67),(0.01,0.20,0.42,0.67)])
M=k([(0.43,0.17,0.93,0.87),(0.44,0.17,0.94,0.87),(0.46,0.16,0.93,0.87),(0.48,0.15,0.98,0.87),(0.53,0.13,0.98,0.87),(0.48,0.12,0.98,0.87),(0.50,0.11,1.0,0.87),(0.51,0.10,1.0,0.87)])
D=k([(0.15,0.66,0.37,0.83),(0.15,0.66,0.37,0.83),(0.15,0.67,0.37,0.83),(0.17,0.67,0.38,0.83),(0.15,0.67,0.39,0.84),(0.16,0.67,0.39,0.84),(0.15,0.67,0.39,0.84),(0.17,0.67,0.39,0.84)])
d={"mediaId":7754,"level":"A","keyWord":"at the same time","defaultVoice":"male",
 "taps":[{"phrase":"to play the guitar","target":"the man","voice":"male","keys":M},
  {"phrase":"to put money in the case","target":"the woman","voice":"female","keys":W},
  {"phrase":"to sit next to the case","target":"the dog","voice":"male","keys":D}],
 "stillS":3.7,
 "nouns":[{"word":"a guitar","x":0.66,"y":0.43,"voice":"male"},{"word":"a dog","x":0.28,"y":0.74,"voice":"male"},
  {"word":"a bike","x":0.45,"y":0.62,"voice":"male"},{"word":"the sky","x":0.30,"y":0.07,"voice":"male"}],
 "question":"What is the man doing?","answer":["He","is","playing","the","guitar."],"answerVoice":"male",
 "notes":"Woman drops a coin into the case at about 2.2 s. Woman box stops above the dog (dog sits in front of her legs). Man is the main person -> defaultVoice male."}
json.dump(d,open('content/7754.json','w'),indent=1)

import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(l): return [ ({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2],2),"h":round(b[3],2)}) for t,b in zip(T,l)]
dog=K([(0.11,0.26,0.37,0.44),(0.12,0.26,0.36,0.44),(0.10,0.25,0.37,0.45),(0.12,0.23,0.33,0.47),(0.10,0.22,0.38,0.48),(0.08,0.22,0.44,0.49),(0.04,0.19,0.44,0.54),(0.03,0.18,0.47,0.55)])
man=K([(0.48,0.17,0.52,0.83),(0.48,0.16,0.52,0.84),(0.47,0.15,0.53,0.85),(0.45,0.12,0.55,0.88),(0.48,0.09,0.52,0.91),(0.52,0.07,0.48,0.93),(0.48,0.04,0.52,0.96),(0.50,0.04,0.50,0.96)])
c={"mediaId":7954,"level":"A","keyWord":"quarter","defaultVoice":"male",
"taps":[{"phrase":"to serve a piece of pie","target":"the dog","voice":"male","keys":dog},
{"phrase":"to hold a white plate","target":"the man","voice":"male","keys":man},
{"phrase":"to laugh at the dog","target":"the man","voice":"male","keys":man}],
"stillS":2.7,
"nouns":[{"word":"a lamp","x":0.26,"y":0.14,"voice":"male"},{"word":"a hat","x":0.39,"y":0.28,"voice":"male"},{"word":"a quarter","x":0.56,"y":0.59,"voice":"male"},{"word":"the floor","x":0.72,"y":0.88,"voice":"male"}],
"question":"What is the dog doing?",
"answer":["It","is","putting","a","quarter","on","the","plate."],"answerVoice":"male",
"notes":"dish is an almond tart, called 'pie' (A level); 'a quarter' pill is on the piece lying on the plate; defaultVoice male = the only human. Dog and man boxes split around x 0.45-0.52 where the plate/server meet."}
json.dump(c,open('content/7954.json','w'),indent=1)

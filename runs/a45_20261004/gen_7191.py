import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(bs): return [({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]}) for t,v in zip(T,bs)]
woman=K([(0.13,0.39,0.45,0.33),(0.17,0.40,0.43,0.32),(0.20,0.44,0.34,0.34),(0.23,0.47,0.33,0.33),(0.24,0.44,0.27,0.30),(0.24,0.43,0.22,0.25),(0.25,0.43,0.21,0.22),(0.26,0.43,0.20,0.19)])
man=K([(0.58,0.26,0.42,0.32),(0.70,0.26,0.30,0.31),(0.82,0.23,0.18,0.28),None,None,None,None,None])
dog=K([(0.39,0.75,0.34,0.19),(0.42,0.73,0.29,0.22),(0.55,0.67,0.23,0.21),(0.62,0.63,0.22,0.18),(0.72,0.56,0.27,0.15),(0.82,0.52,0.18,0.14),(0.82,0.48,0.18,0.14),None])
taps=[{"phrase":"to grab a coffee","target":"the paraglider","voice":"female","keys":woman},
{"phrase":"to hand over a cup","target":"the man","voice":"male","keys":man},
{"phrase":"to leap up excitedly","target":"the dog","voice":"female","keys":dog}]
c={"mediaId":7191,"level":"B","keyWord":"grab a coffee","defaultVoice":"female","taps":taps,"stillS":0.2,
"nouns":[{"word":"an awning","x":0.62,"y":0.26,"voice":"female"},{"word":"a coffee machine","x":0.84,"y":0.51,"voice":"female"},
{"word":"clouds","x":0.55,"y":0.59,"voice":"female"},{"word":"a dog","x":0.57,"y":0.86,"voice":"female"}],
"question":"What is the paraglider doing?","answer":["She","is","grabbing","a","coffee","from","the","hut."],"answerVoice":"female",
"notes":"Paraglider (woman in orange) and the man in the hut touch at the cup at 0.2: boxes split at x 0.58. Man only at 0.2-1.2 (at 1.2 just a sliver at the right edge). Dog leaps at 0.2-1.2, then stands/walks at the right edge, off at 3.7. Paraglider box excludes the canopy lines. Grab happens at 0.2; afterwards she holds the cup."}
json.dump(c,open('content/7191.json','w'),indent=1)

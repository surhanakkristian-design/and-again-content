import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,**dict(zip('xywh',r))) if r else {"t":t,"off":True} for t,r in zip(T,rows)]
M=K([(0.17,0.30,0.43,0.59),(0.15,0.29,0.46,0.60),(0.14,0.27,0.46,0.62),(0.12,0.25,0.47,0.64),(0.10,0.22,0.49,0.67),(0.09,0.20,0.50,0.69),(0.04,0.18,0.40,0.71),(0.03,0.16,0.41,0.74)])
D=K([(0.60,0.57,0.24,0.27),(0.61,0.56,0.26,0.28),(0.60,0.56,0.26,0.29),(0.59,0.54,0.29,0.30),(0.59,0.53,0.29,0.30),(0.59,0.54,0.31,0.30),(0.53,0.58,0.36,0.31),(0.55,0.62,0.38,0.26)])
c={"mediaId":5521,"level":"B","keyWord":"accuse","defaultVoice":"male",
"taps":[{"phrase":"to point an accusing finger","target":"the man","voice":"male","keys":M},
{"phrase":"to sit among white stuffing","target":"the husky","voice":"male","keys":D},
{"phrase":"to break into a smile","target":"the man","voice":"male","keys":M}],
"stillS":2.7,
"nouns":[{"word":"a husky","x":0.73,"y":0.63,"voice":"male"},{"word":"a cushion","x":0.75,"y":0.83,"voice":"male"},
{"word":"a window","x":0.82,"y":0.35,"voice":"male"},{"word":"a pendant lamp","x":0.59,"y":0.09,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","pointing","an","accusing","finger","at","the","husky."],"answerVoice":"male",
"notes":"Only two targets (man, husky); man used twice. Smile is visible from ~3.2 s. Husky lies down at 3.7 s, box follows it."}
json.dump(c,open('content/5521.json','w'),indent=1)

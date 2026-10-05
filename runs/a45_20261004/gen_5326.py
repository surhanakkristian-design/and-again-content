import json
T=[i*0.5 for i in range(21)]
def K(rows):
    return [{"t":t,"off":True} if r is None else dict(zip("txywh",(t,)+tuple(r))) for t,r in zip(T,rows)]
g=[(0.13,0,0.57,0.64),(0.20,0,0.60,0.84),(0.28,0.10,0.72,0.90),(0.10,0.18,0.90,0.80),(0,0.11,0.73,0.62),(0,0.11,0.83,0.60),(0.05,0.12,0.76,0.68),(0.02,0.11,0.76,0.70),
(0,0.05,0.66,0.74),(0,0.02,0.62,0.76),(0,0.02,0.58,0.76),(0,0.02,0.56,0.76),(0,0.02,0.52,0.78),(0,0.03,0.46,0.77),(0,0.04,0.50,0.76),(0,0.04,0.48,0.75),
(0,0.04,0.55,0.78),(0,0.06,0.46,0.78),(0,0.05,0.52,0.88),(0.18,0,0.56,0.95),(0.08,0,0.50,0.90)]
c_=[None]*6+[(0.82,0.05,0.18,0.65),(0.79,0.02,0.21,0.74),(0.67,0,0.33,0.67),(0.63,0,0.37,0.66),(0.59,0,0.41,0.66),(0.57,0,0.43,0.72),(0.53,0,0.47,0.72),(0.47,0,0.53,0.72),
(0.51,0,0.49,0.72),(0.49,0,0.51,0.72),(0.56,0,0.44,0.72),(0.47,0.08,0.53,0.62),(0.53,0.08,0.47,0.62),(0.75,0.02,0.25,0.75),(0.59,0.04,0.41,0.76)]
c={"mediaId":5326,"level":"A","keyWord":"coach","defaultVoice":"female",
"taps":[{"phrase":"to cry in pain","target":"the girl","voice":"female","keys":K(g)},
{"phrase":"to put on a bandage","target":"the coach","voice":"female","keys":K(c_)},
{"phrase":"to wear a grey T-shirt","target":"the coach","voice":"female","keys":K(c_)}],
"stillS":7.0,
"nouns":[{"word":"a girl","x":0.25,"y":0.28,"voice":"female"},{"word":"a coach","x":0.80,"y":0.28,"voice":"female"},
{"word":"a bandage","x":0.60,"y":0.72,"voice":"female"},{"word":"a mat","x":0.40,"y":0.90,"voice":"female"}],
"question":"What is the coach doing?","answer":["She","is","putting","a","bandage","on","the","girl's","foot."],"answerVoice":"female",
"notes":"Gymnast = 'the girl' (young woman), older woman = 'the coach'. Coach enters at 3.0 s (off before; a stray arm at the top right at 1.5-2.5 s ignored). Where the two touch (coach's hands on the girl's ankle, 4.0-8.0 s) the boxes are split vertically, so the girl's foot sits partly in the coach's box. Hug at the end is mutual, so not used as a phrase. Gymnast also wears a blue-grey top; coach's shirt is clearly lighter grey."}
json.dump(c,open('content/5326.json','w'),indent=1)

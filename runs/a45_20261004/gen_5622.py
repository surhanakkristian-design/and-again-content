import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows):
    return [{"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]} for t,r in zip(T,rows)]
wom=K([(0.11,0.35,0.46,0.58),(0.10,0.35,0.48,0.58),(0.10,0.36,0.47,0.58),(0.10,0.36,0.47,0.58),(0.08,0.36,0.48,0.58),(0.07,0.36,0.46,0.59),(0.05,0.36,0.49,0.62),(0.06,0.36,0.50,0.62)])
man=K([(0.58,0.22,0.34,0.72),(0.59,0.22,0.34,0.72),(0.58,0.22,0.35,0.73),(0.58,0.22,0.35,0.73),(0.57,0.21,0.37,0.75),(0.54,0.20,0.44,0.78),(0.55,0.20,0.42,0.79),(0.57,0.19,0.40,0.80)])
c={"mediaId":5622,"level":"A","keyWord":"be interested in","defaultVoice":"female",
"taps":[{"phrase":"to look through a telescope","target":"the woman","voice":"female","keys":wom},
{"phrase":"to cross his arms","target":"the man","voice":"male","keys":man},
{"phrase":"to pull his sleeve","target":"the woman","voice":"female","keys":wom}],
"stillS":0.7,
"nouns":[{"word":"the sky","x":0.50,"y":0.12,"voice":"female"},{"word":"a telescope","x":0.12,"y":0.41,"voice":"female"},
{"word":"a lamp","x":0.16,"y":0.80,"voice":"female"},{"word":"sand","x":0.42,"y":0.95,"voice":"female"}],
"question":"What is the woman looking through?",
"answer":["She","is","looking","through","a","telescope."],"answerVoice":"female",
"notes":"only two people; woman has two phrases. Man uncrosses his arms briefly at 2.7-3.2, crossed again at 3.7. 'a lamp' = the camping lantern on the blanket."}
json.dump(c,open('content/5622.json','w'),indent=1)

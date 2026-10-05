import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,**dict(zip('xywh',r))) if r else {"t":t,"off":True} for t,r in zip(T,rows)]
M=K([(0.19,0.37,0.63,0.39),(0.20,0.36,0.62,0.38),(0.22,0.35,0.58,0.37),(0.20,0.33,0.55,0.39),(0.20,0.37,0.48,0.33),(0.07,0.49,0.73,0.165),(0.00,0.54,0.80,0.10),(0.07,0.53,0.74,0.115)])
W=K([(0.00,0.71,0.18,0.22),(0.00,0.69,0.20,0.24),(0.00,0.67,0.22,0.28),(0.00,0.65,0.20,0.30),(0.00,0.63,0.20,0.30),(0.00,0.655,0.24,0.27),(0.00,0.64,0.26,0.31),(0.00,0.645,0.40,0.295)])
c={"mediaId":5523,"level":"A","keyWord":"acting","defaultVoice":"male",
"taps":[{"phrase":"to open his arms wide","target":"the man","voice":"male","keys":M},
{"phrase":"to lie on the stage","target":"the man","voice":"male","keys":M},
{"phrase":"to cover her face","target":"the woman","voice":"female","keys":W}],
"stillS":2.7,
"nouns":[{"word":"a lamp","x":0.12,"y":0.19,"voice":"male"},{"word":"a man","x":0.50,"y":0.58,"voice":"male"},
{"word":"a sword","x":0.84,"y":0.66,"voice":"male"},{"word":"chairs","x":0.73,"y":0.84,"voice":"male"}],
"question":"Where is the man lying?","answer":["He","is","lying","on","the","stage."],"answerVoice":"male",
"notes":"Only two targets (man, woman). Man's outstretched left hand is cut from his box early on to avoid the woman's box at the left edge; when he lies down his box and the woman's are split horizontally at her head. Woman covers her face at 0.2-1.7 s and 3.7 s, not at 2.2-3.2 s. Key word 'acting' is not a visible noun."}
json.dump(c,open('content/5523.json','w'),indent=1)

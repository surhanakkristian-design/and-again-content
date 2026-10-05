import json
O=None
T=[i/2 for i in range(21)]
W=[(0.05,0.05,0.90,0.48),(0.22,0.06,0.60,0.36),(0.46,0.11,0.36,0.37),(0.46,0.14,0.36,0.56),(0.28,0.14,0.67,0.64),
(0.03,0.14,0.97,0.62),(0.03,0.14,0.92,0.64),(0.03,0.12,0.92,0.66),(0.03,0.08,0.90,0.67),(0.05,0.08,0.88,0.67),
(0.05,0.10,0.88,0.76),(0.05,0.10,0.88,0.75),(0.05,0.09,0.92,0.61),(0.25,0.12,0.55,0.25),(0.27,0.10,0.42,0.37),
(0.32,0.11,0.42,0.39),(0.0,0.30,0.86,0.70),(0.0,0.29,0.85,0.71),(0.17,0.08,0.59,0.31),(0.14,0.09,0.61,0.30),(0.13,0.13,0.62,0.26)]
P=[(0.15,0.53,0.83,0.20),(0.02,0.42,0.80,0.26),(0.0,0.26,0.46,0.50),(0.06,0.22,0.40,0.50),(0.04,0.17,0.24,0.46),
(0.0,0.76,0.93,0.24),(0.0,0.79,0.93,0.21),(0.03,0.78,0.85,0.22),(0.0,0.75,0.92,0.25),(0.0,0.75,0.92,0.24),
(0.0,0.86,0.92,0.14),(0.0,0.85,0.92,0.15),(0.02,0.70,0.88,0.24),(0.25,0.79,0.60,0.19),(0.24,0.89,0.60,0.11),
(0.26,0.91,0.60,0.09),(0.38,0.02,0.62,0.28),(0.36,0.03,0.64,0.26),(0.25,0.89,0.58,0.11),(0.27,0.90,0.58,0.10),(0.25,0.81,0.58,0.18)]
S=[O]*13+[(0.25,0.37,0.50,0.42),(0.20,0.47,0.59,0.42),(0.27,0.50,0.50,0.41),O,O,(0.24,0.39,0.52,0.50),(0.24,0.39,0.54,0.51),(0.24,0.39,0.52,0.41)]
def keys(l): return [({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]}) for t,v in zip(T,l)]
c={"mediaId":187,"level":"A","keyWord":"confused","defaultVoice":"female",
"taps":[{"phrase":"to hold two boards","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to show small pictures","target":"the paper","voice":"female","keys":keys(P)},
{"phrase":"to stand on four legs","target":"the shelf","voice":"female","keys":keys(S)}],
"stillS":10.0,
"nouns":[{"word":"a woman","x":0.42,"y":0.27,"voice":"female"},{"word":"a window","x":0.14,"y":0.40,"voice":"female"},
{"word":"a shelf","x":0.56,"y":0.53,"voice":"female"},{"word":"paper","x":0.52,"y":0.88,"voice":"female"}],
"question":"How does the woman feel?",
"answer":["She","is","confused","by","the","small","pictures."],"answerVoice":"female",
"notes":"'The shelf' = the half-built wooden frame (packet description calls it a shelf; the drawings on the paper look like small tables - a verifier may prefer 'the table'). The paper is held in front of the woman at 0.5-2.0 (blank back side to the camera) and the shelf stands in front of her legs from 6.5: boxes are split, so the woman's box is her upper body there. 8.0-8.5 = close-up of her hand with screws (woman box = the hand; paper blurred behind). Question uses present simple (a feeling)."}

def fix(i,t,v):
    k=c['taps'][i]['keys'][int(t*2)]; k['x'],k['y'],k['w'],k['h']=v
fix(0,5.0,(0.05,0.10,0.88,0.64)); fix(1,5.0,(0.0,0.74,0.92,0.26))
fix(0,5.5,(0.05,0.10,0.88,0.63)); fix(1,5.5,(0.0,0.73,0.92,0.25))
fix(2,7.0,(0.20,0.47,0.59,0.34)); fix(1,7.0,(0.24,0.82,0.60,0.18))
fix(2,7.5,(0.27,0.50,0.50,0.29)); fix(1,7.5,(0.26,0.79,0.60,0.20))
fix(2,9.0,(0.24,0.39,0.52,0.39)); fix(1,9.0,(0.25,0.78,0.58,0.18))
fix(2,9.5,(0.24,0.39,0.54,0.40)); fix(1,9.5,(0.27,0.79,0.58,0.17))
fix(0,7.0,(0.27,0.10,0.42,0.29)); fix(2,7.0,(0.20,0.39,0.59,0.42))
fix(0,7.5,(0.32,0.11,0.42,0.28)); fix(2,7.5,(0.27,0.39,0.50,0.40))
json.dump(c,open('content/187.json','w'),indent=1)

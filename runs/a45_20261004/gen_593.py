import json
O={"off":True}
def r(x0,y0,x1,y1): return {"x":x0,"y":y0,"w":round(x1-x0,2),"h":round(y1-y0,2)}
times=[i*0.5 for i in range(21)]
M={t:O for t in times};W={t:O for t in times};D={t:O for t in times}
def s(t,m=None,w=None,d=None):
    if m: M[t]=r(*m)
    if w: W[t]=r(*w)
    if d: D[t]=r(*d)
s(1.5,(0.66,0,1,0.30))
s(2.0,(0.30,0.10,1,0.58))
s(2.5,(0.55,0,1,1),(0.22,0,0.55,0.47))
s(3.0,(0.55,0,1,1),(0.03,0,0.55,0.92))
s(3.5,(0.59,0,1,1),(0,0,0.59,1))
s(4.0,(0.50,0.06,1,0.94),(0,0,0.50,1))
s(4.5,(0.50,0.13,0.94,0.89),(0,0.07,0.50,1))
s(5.0,(0.50,0.23,1,0.68),(0.04,0.24,0.48,0.68),(0.26,0.68,0.70,0.98))
s(5.5,(0.50,0.27,0.84,0.70),(0.17,0.29,0.49,0.70),(0.26,0.70,0.70,0.98))
s(6.0,(0.50,0.34,0.90,0.54),(0.17,0.34,0.50,0.54),(0.27,0.63,0.69,0.90))
s(6.5,(0.50,0.35,0.93,0.59),(0.15,0.35,0.50,0.59),(0.27,0.61,0.71,0.90))
s(7.0,(0.50,0.37,0.92,0.58),(0.17,0.37,0.50,0.58),(0.28,0.58,0.73,0.89))
s(7.5,(0.50,0.37,0.92,0.55),(0.17,0.37,0.50,0.55),(0.40,0.55,0.74,0.90))
s(8.0,(0.60,0.35,0.92,0.59),(0.17,0.35,0.42,0.59),(0.42,0.46,0.60,0.86))
s(8.5,(0.60,0.35,0.92,0.59),(0.17,0.35,0.42,0.59),(0.42,0.46,0.60,0.81))
s(9.0,(0.60,0.36,0.92,0.60),(0.17,0.36,0.42,0.60),(0.42,0.45,0.60,0.77))
s(9.5,(0.60,0.36,0.92,0.60),(0.17,0.36,0.42,0.60),(0.42,0.44,0.60,0.68))
s(10.0,(0.59,0.35,0.92,0.59),(0.16,0.35,0.41,0.59),(0.41,0.45,0.59,0.59))
def keys(d): return [dict(t=t,**d[t]) for t in times]
c={"mediaId":593,"level":"A","keyWord":"pyjamas","defaultVoice":"male",
"taps":[{"phrase":"to turn off the lamp","target":"the man","voice":"male","keys":keys(M)},
{"phrase":"to have long dark hair","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to jump onto the bed","target":"the dog","voice":"male","keys":keys(D)}],
"stillS":6.0,
"nouns":[{"word":"a window","x":0.48,"y":0.26,"voice":"male"},{"word":"pyjamas","x":0.50,"y":0.46,"voice":"male"},{"word":"a bed","x":0.45,"y":0.60,"voice":"male"},{"word":"a dog","x":0.47,"y":0.77,"voice":"male"}],
"question":"What are the man and woman wearing?","answer":["They","are","wearing","pyjamas."],"answerVoice":"male",
"notes":"The pyjamas swap between the shots: at 2.5-4.5 the woman is in green and the man in blue, from 5.0 the long-haired person (woman, left) is in blue and the curly-haired one (man, right) in green - so no phrase or noun uses a pyjama colour and the people are told apart by hair only. 0.0-1.0 show only hands and the pyjamas on the radiator: all off. 1.5: only the man's hair at the edge. At 2.5 the man is a headless body on the right. The man reaches for the lamp at 8.0-8.5 and the room goes dark. The woman has no action of her own (state phrase). From 8.0 the dog stands / lies between the two on the bed: the dog box is a column between them, which cuts the man's head a little (x 0.55-0.60) and the dog's rump (to x 0.68). The 'pyjamas' pill sits between the two lying people (both wear them); 'a bed' on the front of the mattress. Lamps: two, apart - not used as a noun."}
json.dump(c,open('content/593.json','w'),indent=1)

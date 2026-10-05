import json
O={"off":True}
def r(x0,y0,x1,y1): return {"x":x0,"y":y0,"w":round(x1-x0,2),"h":round(y1-y0,2)}
times=[i*0.5 for i in range(21)]
M={t:O for t in times};W={t:O for t in times};B={t:O for t in times}
def s(t,bg,m,w=None):
    B[t]=r(*bg);M[t]=r(*m)
    if w: W[t]=r(*w)
s(0.0,(0.15,0.33,0.55,1),(0.55,0.44,0.81,1),(0.81,0.44,1,0.84))
s(0.5,(0.08,0.30,0.66,0.97),(0.66,0.45,0.82,1),(0.82,0.50,1,0.98))
s(1.0,(0.10,0.30,0.62,0.98),(0.62,0.45,0.82,1),(0.82,0.56,1,1))
s(1.5,(0.28,0.30,0.66,1),(0.30,0.12,0.66,0.30),(0.75,0.40,1,1))
s(2.0,(0.25,0.35,0.64,1),(0.33,0.13,0.75,0.35),(0.80,0.42,1,1))
s(2.5,(0.25,0.12,0.64,1),(0.64,0.38,1,1))
s(3.0,(0.24,0.08,0.66,1),(0.68,0.53,1,1))
s(3.5,(0.19,0.08,0.57,1),(0.57,0.50,1,1))
s(4.0,(0,0.07,0.62,0.92),(0.64,0.47,1,1))
s(4.5,(0.30,0.05,0.68,0.95),(0.68,0.44,0.98,1))
s(5.0,(0.31,0.04,0.68,0.96),(0.68,0.46,1,1),(0,0.57,0.31,1))
s(5.5,(0.05,0.03,0.43,0.97),(0.43,0.48,1,1))
s(6.0,(0.07,0,0.51,0.92),(0.51,0.46,1,1))
s(6.5,(0.09,0,0.51,0.84),(0.51,0.50,1,1))
s(7.0,(0.19,0.03,0.58,0.88),(0.58,0.48,1,1))
s(7.5,(0.07,0.02,0.57,0.92),(0.58,0.48,1,1))
s(8.0,(0.04,0,0.54,0.83),(0.55,0.50,1,1))
s(8.5,(0,0,0.47,0.90),(0.47,0.45,1,1))
s(9.0,(0.22,0.02,0.62,1),(0.62,0.40,1,1))
s(9.5,(0.23,0,0.61,0.97),(0.61,0.40,0.98,1))
s(10.0,(0.07,0,0.49,0.89),(0.49,0.38,0.82,1))
def keys(d): return [dict(t=t,**d[t]) for t in times]
c={"mediaId":591,"level":"B","keyWord":"punching bag","defaultVoice":"male",
"taps":[{"phrase":"to throw powerful punches","target":"the man","voice":"male","keys":keys(M)},
{"phrase":"to steady the ladder","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to swing from the ceiling","target":"the punching bag","voice":"male","keys":keys(B)}],
"stillS":10.0,
"nouns":[{"word":"a chain","x":0.33,"y":0.13,"voice":"male"},{"word":"a punching bag","x":0.30,"y":0.40,"voice":"male"},{"word":"boxing gloves","x":0.22,"y":0.69,"voice":"male"},{"word":"shorts","x":0.62,"y":0.87,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","throwing","punches","at","the","punching","bag."],"answerVoice":"male",
"notes":"The woman is visible only 0.0-2.0 (hand on the ladder) and at 5.0 (cheering at the left edge); at 2.5 only her hand, off. The man hugs / carries the bag in 0.0-1.0, 4.5-5.0 and 9.0-10.0: boxes split at the line between bag and his body, so his gloves in front of the bag lie in the bag box. At 1.5 and 2.0 he stands behind the bag: his box is only the gloves and arms above the bag (the chains are inside it). Still 10.0: the gloves pill sits on the gloves in front of the bag, the bag pill higher on the bag. The man punches at 5.5-8.5; the bag swings at 4.0 and 6.0-8.5."}
json.dump(c,open('content/591.json','w'),indent=1)

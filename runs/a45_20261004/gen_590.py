import json
O={"off":True}
def b(x,y,w,h): return {"x":x,"y":y,"w":round(w,2),"h":round(h,2)}
def r(x0,y0,x1,y1): return b(x0,y0,x1-x0,y1-y0)
times=[i*0.5 for i in range(21)]
W={};T={};B={}
def s(t,w,tr,bg): W[t]=r(*w);T[t]=r(*tr);B[t]=r(*bg)
s(0.0,(0,0.13,0.63,1),(0.63,0.27,1,0.78),(0.63,0.04,0.87,0.27))
s(0.5,(0,0.13,0.55,1),(0.55,0.28,1,0.80),(0.57,0.04,0.82,0.28))
s(1.0,(0,0.13,0.45,1),(0.45,0.29,1,0.90),(0.50,0.04,0.78,0.29))
s(1.5,(0,0.13,0.54,1),(0.54,0.42,1,0.92),(0.54,0.04,0.74,0.42))
s(2.0,(0,0.14,0.55,1),(0.55,0.29,1,0.77),(0.55,0.04,0.73,0.29))
s(2.5,(0,0.14,0.57,1),(0.57,0.33,1,0.78),(0.57,0.04,0.75,0.33))
s(3.0,(0,0.14,0.55,1),(0.55,0.29,1,0.84),(0.55,0.04,0.73,0.29))
s(3.5,(0,0.14,0.52,1),(0.52,0.29,1,0.87),(0.52,0.04,0.72,0.29))
s(4.0,(0,0.15,0.50,1),(0.50,0.38,1,1.0),(0.50,0.04,0.69,0.38))
s(4.5,(0,0.15,0.55,1),(0.55,0.30,1,0.78),(0.55,0.04,0.73,0.30))
s(5.0,(0,0.15,0.56,1),(0.56,0.30,1,0.82),(0.56,0.04,0.74,0.30))
s(5.5,(0,0.15,0.52,1),(0.52,0.36,1,0.88),(0.52,0.04,0.71,0.36))
s(6.0,(0,0.15,0.45,1),(0.45,0.38,1,0.88),(0.45,0.04,0.64,0.38))
s(6.5,(0,0.15,0.46,1),(0.46,0.37,1,0.87),(0.46,0.04,0.64,0.37))
s(7.0,(0,0.26,0.44,1),(0.66,0.20,1,0.60),(0.44,0.04,0.64,0.58))
s(7.5,(0,0.20,0.46,1),(0.70,0.34,1,0.74),(0.47,0.04,0.68,0.56))
s(8.0,(0,0.15,0.47,1),(0.70,0.33,1,0.80),(0.48,0.04,0.69,0.56))
s(8.5,(0,0.15,0.48,1),(0.70,0.55,1,0.93),(0.49,0.04,0.69,0.51))
s(9.0,(0,0.18,0.48,1),(0.72,0,1,1),(0.49,0.04,0.69,0.44))
s(9.5,(0,0.18,0.50,1),(0.70,0.05,1,1),(0.51,0.04,0.69,0.54))
s(10.0,(0,0.18,0.56,1),(0.80,0.03,1,1),(0.57,0.04,0.77,0.54))
def keys(d): return [dict(t=t,**d[t]) for t in times]
c={"mediaId":590,"level":"B","keyWord":"punch","defaultVoice":"female",
"taps":[{"phrase":"to throw quick punches","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to hold up focus pads","target":"the trainer","voice":"male","keys":keys(T)},
{"phrase":"to hang from a chain","target":"the punching bag","voice":"female","keys":keys(B)}],
"stillS":8.5,
"nouns":[{"word":"a brick wall","x":0.25,"y":0.12,"voice":"female"},{"word":"a punching bag","x":0.60,"y":0.36,"voice":"female"},{"word":"boxing gloves","x":0.48,"y":0.61,"voice":"female"},{"word":"shorts","x":0.25,"y":0.82,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","punching","the","focus","pads."],"answerVoice":"female",
"notes":"Tight close-up: the trainer's pads cover the middle of the hanging bag in most frames 0.0-6.5, so the bag box is only its upper part plus the chain (above the pads) and the trainer box starts at the top of the pads; the bag's lower end below the pads falls into the trainer box. The trainer's head (a sliver at the right edge, above the pads) is outside his box until 9.0. The woman's box is cut at the pads, so a glove that touches a pad can lie in the trainer box. At 9.5 the pad he holds out is in front of her body and lies in her box. 'to hang from a chain' is a state (the bag does nothing else)."}
json.dump(c,open('content/590.json','w'),indent=1)

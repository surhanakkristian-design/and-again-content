import json
T=[i*0.5 for i in range(23)]
def K(rows):
    return [{"t":t,"off":True} if r is None else dict(zip("txywh",(t,)+tuple(r))) for t,r in zip(T,rows)]
s=[(0,0.10,0.30,0.72),(0,0.10,0.32,0.72),(0,0.10,0.34,0.72),(0,0.10,0.35,0.72),(0,0.12,0.32,0.70),(0,0.22,0.40,0.42),(0,0.14,0.28,0.50),(0,0.02,0.62,0.86),
(0,0,0.62,0.95),(0,0.26,0.40,0.70),(0,0.22,0.31,0.50),(0,0.24,0.29,0.48),(0,0.25,0.18,0.34),(0,0.31,0.19,0.34),(0,0.38,0.19,0.34),(0,0.48,0.18,0.34),
(0,0.26,0.20,0.22),(0,0.44,0.36,0.18),None,None,None,None,None]
c_=[(0.31,0.25,0.65,0.75),(0.33,0.25,0.64,0.75),(0.35,0.27,0.61,0.73),(0.36,0.25,0.62,0.75),(0.33,0.28,0.63,0.72),(0.41,0.27,0.59,0.73),(0.29,0.26,0.67,0.74),(0.63,0.27,0.37,0.73),
(0.63,0.26,0.35,0.70),(0.41,0.26,0.53,0.74),(0.32,0.28,0.66,0.72),(0.30,0.28,0.68,0.72),(0.19,0.26,0.78,0.74),(0.20,0.26,0.76,0.74),(0.20,0.27,0.78,0.73),(0.19,0.28,0.78,0.72),
(0.21,0.28,0.77,0.72),(0.37,0.25,0.61,0.75),(0,0.27,1.0,0.73),(0,0.26,1.0,0.74),(0,0.22,1.0,0.78),(0,0.22,1.0,0.78),(0,0.24,1.0,0.76)]
c={"mediaId":5327,"level":"B","keyWord":"cape","defaultVoice":"female",
"taps":[{"phrase":"to spray the client's updo","target":"the stylist","voice":"female","keys":K(s)},
{"phrase":"to grip a styling comb","target":"the stylist","voice":"female","keys":K(s)},
{"phrase":"to wear an elaborate updo","target":"the client","voice":"female","keys":K(c_)}],
"stillS":6.5,
"nouns":[{"word":"an updo","x":0.52,"y":0.38,"voice":"female"},
{"word":"a hoop earring","x":0.37,"y":0.54,"voice":"female"},{"word":"a cape","x":0.55,"y":0.80,"voice":"female"}],
"question":"What is the stylist doing?","answer":["She","is","spraying","the","updo","with","hairspray."],"answerVoice":"female",
"notes":"Stylist overlaps the seated client at 0-4.5 s; boxes split vertically (stylist's comb hand above the client's hair at 0-2.0 s falls into the client's box). Stylist only her hand/arm from 5.0 s, off 9.0-11.0 s (only the client's reflection in the mirror). Comb held 0-3.0 s. Stylist also wears a black smock, so the cape is not used in a phrase (only as a noun on the client's back). Stylist also wears hoop earrings (0-2.0 s), but the noun pill at 6.5 s (mirror left out: two mirrors in view) is on the client's only earring in view."}
json.dump(c,open('content/5327.json','w'),indent=1)

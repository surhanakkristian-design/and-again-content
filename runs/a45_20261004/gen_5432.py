import json
S={0.0:(0.4,0.17,0.6,0.83),0.5:(0.44,0.19,0.56,0.81),1.0:(0.44,0.21,0.56,0.79),1.5:(0.4,0.21,0.6,0.79),
2.0:(0.43,0.25,0.57,0.75),2.5:(0.44,0.22,0.56,0.78),3.0:(0.32,0.12,0.68,0.88),3.5:(0.19,0.11,0.81,0.89),
4.0:(0.25,0.17,0.75,0.83),4.5:(0.3,0.12,0.7,0.88),5.0:(0.38,0.16,0.62,0.84),5.5:(0.38,0.18,0.62,0.82),
6.0:(0.28,0.17,0.72,0.8),6.5:(0.4,0.17,0.6,0.83),7.0:(0.36,0.21,0.64,0.79),7.5:(0.3,0.2,0.7,0.8),
8.0:(0.32,0.2,0.68,0.8),8.5:(0.24,0.27,0.76,0.73),9.0:(0.3,0.26,0.7,0.74),9.5:(0.34,0.48,0.66,0.52),
10.0:(0.32,0.34,0.6,0.66),10.5:(0.16,0.21,0.84,0.79),11.0:(0.04,0.24,0.86,0.76),11.5:(0.33,0.21,0.6,0.79),12.0:(0.27,0.21,0.66,0.79)}
C={3.0:(0.0,0.32,0.2,0.38),3.5:(0.0,0.24,0.18,0.48),4.0:(0.0,0.2,0.24,0.46),7.5:(0.0,0.58,0.28,0.18),
8.0:(0.0,0.27,0.3,0.5),8.5:(0.0,0.4,0.2,0.26)}
def keys(B):
    return [({"t":t,"x":B[t][0],"y":B[t][1],"w":B[t][2],"h":B[t][3]} if t in B else {"t":t,"off":True}) for t in sorted(S)]
ks,kc=keys(S),keys(C)
c={"mediaId":5432,"level":"B","keyWord":"trick","defaultVoice":"male",
"taps":[{"phrase":"to stretch the ice cream","target":"the ice cream seller","voice":"male","keys":ks},
{"phrase":"to reach for the cone","target":"the customer","voice":"male","keys":kc},
{"phrase":"to ring the brass bells","target":"the ice cream seller","voice":"male","keys":ks}],
"stillS":7.0,
"nouns":[{"word":"bells","x":0.15,"y":0.25,"voice":"male"},{"word":"a fez","x":0.75,"y":0.3,"voice":"male"},
{"word":"a waistcoat","x":0.85,"y":0.55,"voice":"male"},{"word":"a cone","x":0.42,"y":0.63,"voice":"male"}],
"question":"What is the ice cream seller doing?","answer":["He","is","tricking","the","customer."],"answerVoice":"male",
"notes":"Customer is only partly visible (face edge + hand at the left) at 3.0-4.0 and 7.5-8.5; off elsewhere. At 3.5/4.0 the seller's outstretched hand and the customer's hand are close; split along x. Seller boxes mostly exclude the ice-cream rope at 1.0/2.0."}
json.dump(c,open('content/5432.json','w'),indent=1)

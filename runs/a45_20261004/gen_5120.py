import json
S = {0.0:(0.18,0.23,0.7,0.4),0.5:(0.17,0.25,0.7,0.38),1.0:(0.22,0.26,0.66,0.38),1.5:(0.33,0.25,0.65,0.37),2.0:(0.58,0.24,0.42,0.33),
4.5:(0.8,0.32,0.2,0.2),5.0:(0.42,0.35,0.38,0.22),5.5:(0.38,0.38,0.35,0.19),6.0:(0.35,0.39,0.3,0.16),6.5:(0.36,0.39,0.3,0.16),
7.0:(0.33,0.37,0.3,0.2),7.5:(0.33,0.37,0.32,0.2),8.0:(0.33,0.36,0.32,0.2),8.5:(0.32,0.36,0.33,0.2),9.0:(0.3,0.36,0.35,0.22)}
M = {2.0:(0.0,0.21,0.24,0.22),2.5:(0.14,0.22,0.52,0.25),3.0:(0.26,0.25,0.53,0.27),3.5:(0.3,0.26,0.56,0.27),4.0:(0.19,0.28,0.49,0.23),4.5:(0.0,0.29,0.36,0.2)}
B = {2.5:(0.0,0.08,0.13,0.6),3.0:(0.0,0.09,0.25,0.91),3.5:(0.0,0.1,0.29,0.9)}
times=[i/2 for i in range(19)]
def ks(d): return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if d.get(t) else {"t":t,"off":True}) for t in times]
c={"mediaId":5120,"level":"B","keyWord":"surgeon","defaultVoice":"female",
"taps":[{"phrase":"to lean over the patient","target":"the surgeon in the middle","voice":"male","keys":ks(S)},
{"phrase":"to display the heart rate","target":"the heart monitor","voice":"female","keys":ks(M)},
{"phrase":"to hold a piece of gauze","target":"the bearded man","voice":"male","keys":ks(B)}],
"stillS":7.5,
"nouns":[{"word":"a surgical lamp","x":0.52,"y":0.33,"voice":"female"},{"word":"a surgeon","x":0.48,"y":0.5,"voice":"female"},
{"word":"a patient","x":0.5,"y":0.75,"voice":"female"}],
"question":"What is the central surgeon doing?","answer":["He","is","leaning","over","the","patient."],"answerVoice":"male",
"notes":"Clip has cuts: surgeon in the middle (man at the head of the table) is visible 0-2.0, 4.5 (right edge) and 5.0-9.0; heart monitor only 2.0-4.5; bearded man (no cap edge, holds white gauze) only 2.5-3.5 -- at 4.0 an arm passes the gauze to the woman on the right but the man is hidden behind another person, so off. At 3.5 his box stops at x 0.29 so it does not overlap the monitor; his hand with the gauze reaches x 0.65 below the monitor. Mixed team -> defaultVoice female (evenId). 'a surgeon' pill sits on the central man; others in scrubs may also be surgeons. Only 3 nouns."}
json.dump(c,open('content/5120.json','w'),indent=1)

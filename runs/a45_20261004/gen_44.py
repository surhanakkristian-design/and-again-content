import json
T=[i*0.5 for i in range(21)]
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if d.get(t) else {"t":t,"off":True}) for t in T]
W={0.0:(0.10,0.15,0.70,0.43),0.5:(0.05,0.12,0.75,0.56),1.0:(0.08,0.10,0.82,0.62),1.5:(0.02,0.10,0.98,0.80),2.0:(0,0.08,1,0.80),
2.5:(0.15,0.15,0.85,0.72),3.0:(0,0.20,1,0.75),3.5:(0,0.15,0.72,0.71),4.0:(0,0.22,0.78,0.65),4.5:(0.05,0.19,0.55,0.69),
5.0:(0,0.24,0.42,0.66),5.5:(0,0.22,0.42,0.68),6.0:(0.08,0.19,0.87,0.48),6.5:(0.08,0.18,0.90,0.50),7.0:(0.14,0.20,0.66,0.64),
7.5:(0.14,0.21,0.66,0.63),8.0:(0.16,0.10,0.62,0.57),8.5:(0.08,0.17,0.92,0.50),9.0:(0.18,0.25,0.64,0.59),9.5:(0.18,0.25,0.62,0.57),10.0:(0.18,0.13,0.58,0.57)}
F={0.5:(0,0.70,1,0.30),1.0:(0,0.74,1,0.26),3.5:(0,0.86,1,0.14),4.0:(0,0.87,1,0.13),4.5:(0,0.88,1,0.12),5.0:(0,0.90,1,0.10),5.5:(0,0.90,1,0.10),
6.0:(0,0.67,1,0.33),6.5:(0,0.68,1,0.32),7.0:(0,0.84,1,0.16),7.5:(0,0.84,1,0.16),8.0:(0,0.67,1,0.33),8.5:(0,0.67,1,0.33),9.0:(0,0.84,1,0.16),9.5:(0,0.82,1,0.18),10.0:(0,0.70,1,0.30)}
c={"mediaId":44,"level":"B","keyWord":"anger","defaultVoice":"female",
"taps":[{"phrase":"to clench her fists","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to clutch her head","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to lie scattered around","target":"the flowers","voice":"female","keys":keys(F)}],
"stillS":8.0,
"nouns":[{"word":"braids","x":0.46,"y":0.18,"voice":"female"},{"word":"an apron","x":0.46,"y":0.40,"voice":"female"},
{"word":"a fist","x":0.24,"y":0.55,"voice":"female"},{"word":"flowers","x":0.50,"y":0.85,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","clenching","her","fists","in","anger."],"answerVoice":"female",
"notes":"Only one person in the clip, so two phrases share the woman; third target = the scattered flowers on the table (hidden by the bag / out of view at 0.0, 1.5-3.0 -> off). Flowers box is thin (0.10-0.14 high, full width) at 3.5-5.5 where only the table edge shows. 'a fist' pill sits on her right fist (screen left); she has two fists."}
json.dump(c,open('content/44.json','w'),indent=1)

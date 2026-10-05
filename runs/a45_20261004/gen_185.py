import json
OFF=None
man={0.0:(0.22,0.26,0.44,0.48),0.5:(0.18,0.23,0.50,0.57),1.0:(0.15,0.01,0.57,0.79),1.5:(0.48,0.41,0.32,0.56),2.0:OFF,
2.5:(0.13,0.05,0.87,0.95),3.0:(0.0,0.14,0.93,0.86),3.5:(0.0,0.17,0.95,0.83),4.0:(0.0,0.17,0.83,0.83),
4.5:(0.42,0.43,0.18,0.25),5.0:(0.46,0.38,0.26,0.49),5.5:(0.28,0.28,0.42,0.70),6.0:(0.27,0.32,0.43,0.67),
6.5:(0.03,0.15,0.85,0.85),7.0:(0.0,0.16,0.83,0.84),7.5:(0.31,0.24,0.42,0.74),8.0:(0.25,0.18,0.62,0.82),
8.5:(0.02,0.27,0.98,0.73),9.0:(0.26,0.19,0.46,0.81),9.5:(0.13,0.17,0.62,0.83),10.0:(0.10,0.16,0.64,0.84)}
tram={0.0:(0.66,0.33,0.34,0.42),0.5:(0.68,0.10,0.32,0.67),1.0:(0.72,0.0,0.28,0.90),1.5:(0.05,0.38,0.43,0.55),
2.0:(0.0,0.02,1.0,0.83),2.5:OFF,3.0:OFF,3.5:OFF,4.0:OFF,4.5:(0.0,0.38,0.42,0.25),5.0:(0.0,0.39,0.46,0.24),
5.5:(0.0,0.40,0.28,0.24),6.0:OFF,6.5:OFF,7.0:OFF,7.5:(0.0,0.12,0.31,0.50),8.0:(0.0,0.12,0.25,0.45),
8.5:(0.0,0.11,1.0,0.16),9.0:(0.72,0.13,0.28,0.57),9.5:OFF,10.0:OFF}
def keys(d): return [({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]}) for t,v in sorted(d.items())]
c={"mediaId":185,"level":"B","keyWord":"commute","defaultVoice":"male",
"taps":[{"phrase":"to dash for the tram","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to grip an overhead strap","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to carry passengers","target":"the tram","voice":"male","keys":keys(tram)}],
"stillS":2.5,
"nouns":[{"word":"a strap","x":0.25,"y":0.09,"voice":"male"},{"word":"passengers","x":0.22,"y":0.60,"voice":"male"},
{"word":"a paper cup","x":0.78,"y":0.62,"voice":"male"},{"word":"a satchel","x":0.38,"y":0.82,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","gripping","a","strap","while","commuting."],"answerVoice":"male",
"notes":"Second target = the tram (exterior shots only; interior shots 2.5-4.0, 6.5-7.0 are off). Where the man stands in front of / inside the tram, the tram box is the part of the tram beside or above him (8.5: only the strip above his raised arms). 'to carry passengers' is only 3 words (to + verb + object) and 'passengers' is B1 at most. Passengers on the still (2.5) are blurred in the background. 1.5: the man is half hidden in the doorway."}
json.dump(c,open('content/185.json','w'),indent=1)

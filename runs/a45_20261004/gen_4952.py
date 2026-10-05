import json
times=[i/2 for i in range(25)]
B=lambda x,y,w,h:dict(x=x,y=y,w=w,h=h)
man={0.0:B(0,0.58,0.60,0.42),0.5:B(0,0.58,0.63,0.42),1.0:B(0,0.52,0.45,0.45),
3.5:B(0.15,0.17,0.62,0.60),4.0:B(0.20,0.16,0.62,0.21),4.5:B(0.22,0.19,0.62,0.25),5.0:B(0.33,0.27,0.61,0.27),5.5:B(0.30,0.33,0.63,0.27),
6.0:B(0.42,0.19,0.56,0.22),6.5:B(0.39,0.23,0.60,0.18),7.0:B(0.52,0.12,0.47,0.88),7.5:B(0.51,0.15,0.43,0.85),8.0:B(0.47,0.15,0.45,0.85),
8.5:B(0.48,0.15,0.44,0.58),9.0:B(0.50,0.16,0.42,0.65)}
for t in times:
    if t>=9.5: man[t]=B(0,0.36,1.0,0.40) if t==9.5 else B(0,0.40,1.0,0.45)
dog={2.0:B(0.43,0.10,0.27,0.29),2.5:B(0.40,0.25,0.30,0.39),3.0:B(0,0.28,0.72,0.72),3.5:B(0.35,0.78,0.37,0.22),
4.0:B(0.30,0.38,0.40,0.62),4.5:B(0.28,0.45,0.44,0.55),5.0:B(0.24,0.55,0.52,0.45),5.5:B(0.33,0.61,0.38,0.39),
6.0:B(0.37,0.42,0.35,0.58),6.5:B(0.37,0.42,0.40,0.58),7.0:B(0.24,0.71,0.27,0.29),7.5:B(0.17,0.67,0.32,0.33),
8.0:B(0.18,0.70,0.28,0.30),8.5:B(0.20,0.74,0.55,0.26),9.0:B(0.38,0.82,0.38,0.18)}
wom={5.5:B(0.16,0.31,0.13,0.55),6.0:B(0.21,0.30,0.15,0.45),6.5:B(0.19,0.27,0.17,0.55),7.0:B(0.19,0.28,0.32,0.42),
7.5:B(0.25,0.33,0.25,0.33),8.0:B(0.18,0.30,0.28,0.38),8.5:B(0.20,0.30,0.27,0.43),9.0:B(0.20,0.30,0.29,0.51)}
def keys(d): return [dict(t=t,**d[t]) if t in d else {"t":t,"off":True} for t in times]
c={"mediaId":4952,"level":"A","keyWord":"bed","defaultVoice":"male",
"taps":[
{"phrase":"to lie on the bed","target":"the young man","voice":"male","keys":keys(man)},
{"phrase":"to jump up at the man","target":"the dog","voice":"male","keys":keys(dog)},
{"phrase":"to wear an apron","target":"the older woman","voice":"female","keys":keys(wom)}],
"stillS":11.0,
"nouns":[{"word":"a lamp","x":0.25,"y":0.30,"voice":"male"},
{"word":"a pillow","x":0.86,"y":0.42,"voice":"male"},
{"word":"a man","x":0.42,"y":0.55,"voice":"male"},
{"word":"a bed","x":0.55,"y":0.76,"voice":"male"}],
"question":"What is the young man doing?",
"answer":["He","is","lying","on","the","bed."],
"answerVoice":"male",
"notes":"Cuts: 0-1.0 only the young man's hand opening the door (boxed as him), 1.5-3.0 hallway with the dog only (man off), 3.5-9.0 doorway, 9.5-12.0 bedroom. The dog stands in front of the man 3.5-6.5: man box = head/shoulders above the dog, his arms are left out. During the hug 7.0-9.0 the man's head is over the woman, so his box covers his body/backpack (x >= ~0.5) and not his head; the woman's box is her upper body, the dog's below her. Woman visible only 5.5-9.0. 'a man' noun: his chest on the bed in the still."}
json.dump(c,open('content/4952.json','w'),indent=1)

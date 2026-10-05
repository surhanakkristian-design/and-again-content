import json
T=[i*0.5 for i in range(21)]
W={0.0:(0.05,0.27,0.45,0.73),0.5:(0,0.29,0.55,0.50),1.0:(0.02,0.36,0.50,0.64),1.5:(0.11,0.39,0.44,0.61),2.0:(0.07,0.42,0.42,0.54),
 2.5:(0.13,0.43,0.34,0.48),3.0:(0.10,0.44,0.37,0.56),6.5:(0.09,0.52,0.44,0.36),7.0:(0.09,0.58,0.44,0.40),7.5:(0.09,0.58,0.42,0.40),
 8.0:(0.05,0.57,0.44,0.36),8.5:(0,0.63,0.49,0.37),9.0:(0.07,0.70,0.41,0.30),9.5:(0.07,0.74,0.41,0.26),10.0:(0.05,0.77,0.42,0.23)}
M={0.0:(0.51,0.18,0.49,0.52),0.5:(0.57,0.26,0.43,0.55),1.0:(0.57,0.29,0.41,0.67),1.5:(0.60,0.33,0.40,0.65),2.0:(0.58,0.37,0.38,0.54),
 2.5:(0.55,0.38,0.39,0.54),3.0:(0.57,0.38,0.39,0.62),6.5:(0.54,0.49,0.46,0.51),7.0:(0.54,0.58,0.42,0.42),7.5:(0.52,0.60,0.46,0.40),
 8.0:(0.50,0.61,0.48,0.39),8.5:(0.50,0.66,0.48,0.34),9.0:(0.49,0.71,0.46,0.29),9.5:(0.49,0.76,0.45,0.24),10.0:(0.48,0.79,0.45,0.21)}
D={3.5:(0.38,0.32,0.46,0.22),4.0:(0.39,0.33,0.45,0.22),4.5:(0.39,0.33,0.47,0.21),5.0:(0.39,0.36,0.47,0.18),5.5:(0.39,0.36,0.48,0.18),6.0:(0.38,0.36,0.46,0.18),
 6.5:(0.53,0.34,0.20,0.14),7.0:(0.54,0.36,0.20,0.14),7.5:(0.54,0.37,0.20,0.14),8.0:(0.55,0.40,0.20,0.14),8.5:(0.55,0.44,0.20,0.14),
 9.0:(0.55,0.49,0.20,0.14),9.5:(0.55,0.53,0.20,0.14),10.0:(0.53,0.55,0.20,0.14)}
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
c={"mediaId":495,"level":"A","keyWord":"nature","defaultVoice":"male",
"taps":[{"phrase":"to eat the grass","target":"the deer","voice":"male","keys":keys(D)},
{"phrase":"to wear a grey jacket","target":"the man","voice":"male","keys":keys(M)},
{"phrase":"to wear a green jacket","target":"the woman","voice":"female","keys":keys(W)}],
"stillS":4.0,
"nouns":[{"word":"deer","x":0.62,"y":0.43,"voice":"male"},{"word":"a river","x":0.30,"y":0.68,"voice":"male"},
{"word":"stones","x":0.72,"y":0.88,"voice":"male"},{"word":"grass","x":0.25,"y":0.27,"voice":"male"}],
"question":"What are the deer doing?",
"answer":["They","are","eating","grass","by","a","river."],"answerVoice":"male",
"notes":"The man and the woman do the same things throughout (climb the fence, walk, sit, lie down), so their phrases are states (jacket colour). 'the deer' = both deer in one box. At 0.0-3.0 s the deer are tiny specks on the far bank right beside / behind the man; a minimum-size box would overlap his box, so they are off there. At 6.5-10.0 they are small in the background and get the minimum box. The key word 'nature' is abstract and not used as a noun. defaultVoice male: mixed couple, evenId false. 'deer' is the bare plural for the two animals standing together."}
json.dump(c,open("content/495.json","w"),indent=1)

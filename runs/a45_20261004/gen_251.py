import json
T=[i*0.5 for i in range(21)]
man=[(0.34,0,0.66,0.70),(0.34,0,0.66,0.72),(0.37,0,0.63,0.95),(0.22,0,0.78,1.0),(0.28,0,0.72,1.0),(0.21,0,0.79,1.0),(0.29,0.05,0.71,0.95),(0.29,0.09,0.71,0.91),(0.26,0.11,0.74,0.89),(0.31,0.11,0.69,0.89),(0.28,0.08,0.72,0.92),(0.36,0.10,0.64,0.90),(0.42,0.12,0.58,0.88),(0.39,0.13,0.61,0.87),(0.42,0,0.58,1.0),(0.46,0,0.54,1.0),(0.35,0.21,0.65,0.79),(0.22,0.32,0.78,0.68),(0.25,0.44,0.75,0.56),(0.31,0.16,0.69,0.84),(0.44,0.11,0.56,0.89)]
woman=[None,None,(0,0.02,0.36,0.20),None,(0,0.36,0.27,0.38),(0,0.33,0.20,0.44),(0,0.38,0.28,0.56),(0.03,0.41,0.26,0.55),(0,0.42,0.25,0.40),(0,0.42,0.30,0.40),(0,0.43,0.27,0.53),(0.02,0.44,0.33,0.52),(0,0.45,0.41,0.40),(0,0.48,0.38,0.40),(0,0.58,0.40,0.42),(0,0.62,0.38,0.38),(0,0.60,0.34,0.38),(0,0.54,0.21,0.42),(0,0.48,0.24,0.52),(0.04,0.44,0.26,0.54),(0,0.43,0.42,0.42)]
def keys(b): return [{"t":t,"off":True} if k is None else {"t":t,"x":k[0],"y":k[1],"w":k[2],"h":k[3]} for t,k in zip(T,b)]
c={"mediaId":251,"level":"B","keyWord":"dumbbell","defaultVoice":"male",
"taps":[{"phrase":"to do biceps curls","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to sip her coffee","target":"the woman","voice":"female","keys":keys(woman)},
{"phrase":"to sit cross-legged","target":"the woman","voice":"female","keys":keys(woman)}],
"stillS":6.0,
"nouns":[{"word":"a dumbbell","x":0.45,"y":0.48,"voice":"male"},{"word":"a palm tree","x":0.25,"y":0.20,"voice":"male"},{"word":"an armchair","x":0.20,"y":0.87,"voice":"male"},{"word":"a window","x":0.72,"y":0.07,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","doing","biceps","curls","with","a","dumbbell."],"answerVoice":"male",
"notes":"Only two people; the woman carries two phrases. First 2 s are a close-up of the man's arm and legs; the woman is only legs at the top left there (off at 0.0, 0.5, 1.5; small leg box at 1.0). Where the man's arm/dumbbell passes in front of the woman (2.5-5.5, 8.5-9.5) the boxes are split on a vertical line, so her right knee is sometimes cut. The armchair pill sits on the seat cushion under her legs."}
json.dump(c,open('content/251.json','w'),indent=1)

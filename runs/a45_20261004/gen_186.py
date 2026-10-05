import json
T=[i/2 for i in range(21)]
dog=[(0.09,0.50,0.18,0.20),(0.12,0.50,0.20,0.20),(0.02,0.52,0.21,0.21),(0.03,0.51,0.20,0.22),(0.10,0.48,0.20,0.20),
(0.15,0.44,0.22,0.14),(0.13,0.48,0.18,0.20),(0.08,0.49,0.19,0.22),(0.08,0.45,0.22,0.14),(0.04,0.49,0.19,0.20),
(0.08,0.48,0.22,0.14),(0.07,0.48,0.22,0.14),(0.07,0.50,0.18,0.21),(0.10,0.52,0.19,0.21),(0.10,0.53,0.19,0.22),
(0.09,0.54,0.19,0.20),(0.07,0.50,0.18,0.18),(0.02,0.50,0.18,0.16),(0.02,0.58,0.18,0.16),(0.0,0.58,0.18,0.17),(0.02,0.39,0.20,0.14)]
wom=[(0.27,0.56,0.23,0.42),(0.32,0.55,0.25,0.43),(0.24,0.58,0.28,0.40),(0.24,0.60,0.30,0.38),(0.30,0.57,0.26,0.41),
(0.05,0.58,0.47,0.40),(0.31,0.55,0.27,0.43),(0.27,0.56,0.24,0.42),(0.0,0.59,0.46,0.39),(0.23,0.56,0.25,0.42),
(0.0,0.62,0.46,0.36),(0.05,0.62,0.42,0.36),(0.25,0.58,0.26,0.40),(0.29,0.58,0.30,0.40),(0.29,0.61,0.27,0.37),
(0.28,0.60,0.28,0.38),(0.25,0.53,0.25,0.45),(0.20,0.48,0.31,0.46),(0.20,0.46,0.28,0.50),(0.18,0.50,0.27,0.48),(0.0,0.53,0.64,0.42)]
man=[(0.58,0.50,0.42,0.50),(0.58,0.49,0.42,0.51),(0.52,0.40,0.48,0.60),(0.55,0.40,0.45,0.60),(0.57,0.40,0.43,0.60),
(0.53,0.40,0.47,0.60),(0.59,0.48,0.41,0.52),(0.54,0.48,0.46,0.52),(0.50,0.48,0.50,0.50),(0.52,0.48,0.48,0.50),
(0.55,0.50,0.45,0.50),(0.55,0.48,0.45,0.50),(0.55,0.50,0.45,0.50),(0.60,0.40,0.40,0.60),(0.57,0.52,0.43,0.48),
(0.60,0.48,0.40,0.52),(0.60,0.48,0.40,0.52),(0.53,0.48,0.47,0.52),(0.48,0.46,0.50,0.54),(0.45,0.50,0.55,0.50),(0.64,0.42,0.36,0.58)]
def keys(l): return [{"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]} for t,v in zip(T,l)]
c={"mediaId":186,"level":"A","keyWord":"concert","defaultVoice":"female",
"taps":[{"phrase":"to sit on a bag","target":"the dog","voice":"female","keys":keys(dog)},
{"phrase":"to shout to the band","target":"the woman","voice":"female","keys":keys(wom)},
{"phrase":"to have a short beard","target":"the man","voice":"male","keys":keys(man)}],
"stillS":3.0,
"nouns":[{"word":"a tree","x":0.45,"y":0.20,"voice":"female"},{"word":"flags","x":0.55,"y":0.41,"voice":"female"},
{"word":"a dog","x":0.27,"y":0.57,"voice":"female"},{"word":"a bag","x":0.20,"y":0.77,"voice":"female"}],
"question":"What are the people watching?",
"answer":["They","are","watching","a","concert","in","a","park."],"answerVoice":"female",
"notes":"Woman = the one with the blue headscarf and braid; man = the bearded man in the white T-shirt next to her (back to the camera until 3.5, beard visible from 4.0; state phrase because every action of his - raising arms, clapping, high five - is also done by others). Dog sits on a backpack right behind the woman's head: dog/woman boxes are split where they touch, so the woman's box often leaves out her left shoulder; at 8.5-10.0 the dog is mostly hidden behind her head/arms. Key word 'a concert' is not a noun slot (no single place); it is in the answer. 'flags' = the bunting line."}

def fix(i,name,v):
    k=c['taps'][i]['keys'][int(name*2)]; k['x'],k['y'],k['w'],k['h']=v
fix(0,3.0,(0.14,0.48,0.19,0.20)); fix(1,3.0,(0.33,0.55,0.25,0.43))
fix(0,4.5,(0.06,0.49,0.19,0.20)); fix(1,4.5,(0.25,0.56,0.23,0.42))
fix(0,6.0,(0.08,0.50,0.18,0.21)); fix(1,6.0,(0.26,0.58,0.25,0.40))
fix(0,9.0,(0.02,0.50,0.18,0.16)); fix(0,9.5,(0.0,0.50,0.18,0.16))
json.dump(c,open('content/186.json','w'),indent=1)

import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]}) for t,r in zip(T,rows)]
nurse=K([(0.26,0.32,0.46,0.46),(0.26,0.32,0.55,0.46),(0.25,0.31,0.57,0.48),(0.25,0.28,0.57,0.51),(0.24,0.29,0.58,0.51),(0.24,0.29,0.59,0.52),(0.24,0.28,0.64,0.54),(0.24,0.29,0.65,0.55)])
old=K([(0.07,0.33,0.19,0.44),(0.07,0.33,0.19,0.44),(0.06,0.33,0.19,0.44),(0.06,0.33,0.19,0.44),(0.05,0.33,0.19,0.44),(0.05,0.33,0.19,0.44),(0.05,0.30,0.19,0.47),(0.05,0.30,0.19,0.47)])
c={"mediaId":7004,"level":"B","keyWord":"cure","defaultVoice":"female",
"taps":[
 {"phrase":"to hold up a vial","target":"the nurse","voice":"female","keys":nurse},
 {"phrase":"to reach into a cool box","target":"the nurse","voice":"female","keys":nurse},
 {"phrase":"to clasp his hands together","target":"the older man","voice":"male","keys":old}],
"stillS":1.2,
"nouns":[{"word":"a vial","x":0.73,"y":0.35,"voice":"female"},
 {"word":"a window","x":0.90,"y":0.48,"voice":"female"},
 {"word":"a nurse","x":0.45,"y":0.56,"voice":"female"},
 {"word":"a cool box","x":0.60,"y":0.85,"voice":"female"}],
"question":"What is the nurse holding up?",
"answer":["She","is","holding","up","a","vial."],
"answerVoice":"female",
"notes":"Nurse reaches into the cool box at 0.2-0.7 and holds the vial up from 0.7. The man in the motorbike helmet stands directly behind the nurse (inside her box), so he is not a target. Older man = grey-haired man in the doorway on the left, hands clasped at his chest 0.2-2.7; at 3.2-3.7 he raises/claps his hands (weak spot). His box is split from the nurse's at x ~0.24-0.26, so his right shoulder/hands are a little cut. Key word 'cure' (noun) shown by the vial, not labelled as 'a cure'."}
json.dump(c,open('content/7004.json','w'),indent=1,ensure_ascii=False)

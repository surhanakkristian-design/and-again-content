import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
M=[(0.02,0.31,0.70,0.60),(0.02,0.31,0.70,0.60),(0.17,0.31,0.65,0.66),(0.13,0.31,0.71,0.62),(0.02,0.18,0.78,0.69),(0.0,0.13,0.84,0.79),(0.0,0.21,0.80,0.79),(0.0,0.34,0.44,0.24)]
P=[(0.33,0.15,0.25,0.16),(0.33,0.15,0.25,0.16),(0.30,0.15,0.32,0.16),(0.28,0.10,0.33,0.21),(0.22,0.0,0.33,0.18),(0.20,0.0,0.30,0.13),(0.03,0.02,0.28,0.19),None]
def k(L): return [dict(t=t,off=True) if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,L)]
m=k(M); p=k(P)
c={"mediaId":7337,"level":"A","keyWord":"mark","defaultVoice":"female",
"taps":[
 {"phrase":"to let a bird fly","target":"the woman in the headband","voice":"female","keys":m},
 {"phrase":"to kneel in the grass","target":"the woman in the headband","voice":"female","keys":m},
 {"phrase":"to sit on her head","target":"the bird on her head","voice":"female","keys":p}],
"stillS":0.2,
"nouns":[{"word":"a bird","x":0.46,"y":0.24,"voice":"female"},{"word":"a jacket","x":0.30,"y":0.50,"voice":"female"},
 {"word":"a box","x":0.78,"y":0.83,"voice":"female"},{"word":"grass","x":0.30,"y":0.94,"voice":"female"}],
"question":"What is the kneeling woman doing?",
"answer":["She","is","holding","a","bird","in","her","hands."],"answerVoice":"female",
"notes":"Laughing colleague not used as a target: her body sits behind the main woman's held bird/arm in most frames, boxes would overlap. Bird-on-head box at 2.7 is cut by the top edge (h 0.13). 'kneeling' in the question = only the main woman kneels (0.2-1.7). Key word 'mark' is a verb (tagging), not used: 'tag' too hard for A."}
json.dump(c,open('content/7337.json','w'),indent=1)

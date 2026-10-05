import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]}) for t,r in zip(T,rows)]
critic=K([(0.23,0.30,0.45,0.51),(0.23,0.30,0.45,0.51),(0.21,0.29,0.47,0.52),(0.20,0.29,0.49,0.52),(0.18,0.27,0.53,0.56),(0.18,0.26,0.53,0.57),(0.16,0.25,0.56,0.62),(0.17,0.24,0.56,0.62)])
man=K([(0.69,0.31,0.31,0.50),(0.69,0.30,0.31,0.51),(0.69,0.30,0.31,0.51),(0.70,0.29,0.30,0.52),(0.72,0.28,0.28,0.54),(0.72,0.28,0.28,0.56),(0.73,0.40,0.27,0.50),(0.74,0.42,0.26,0.53)])
c={"mediaId":7001,"level":"B","keyWord":"critic","defaultVoice":"female",
"taps":[
 {"phrase":"to jot down notes","target":"the critic","voice":"female","keys":critic},
 {"phrase":"to adjust her glasses","target":"the critic","voice":"female","keys":critic},
 {"phrase":"to wipe away his tears","target":"the man on the right","voice":"male","keys":man}],
"stillS":1.7,
"nouns":[{"word":"a balcony","x":0.50,"y":0.10,"voice":"female"},
 {"word":"a critic","x":0.45,"y":0.52,"voice":"female"},
 {"word":"a programme","x":0.37,"y":0.84,"voice":"female"},
 {"word":"a rose","x":0.77,"y":0.86,"voice":"female"}],
"question":"What is the critic doing?",
"answer":["The","critic","is","jotting","down","notes."],
"answerVoice":"female",
"notes":"Critic = woman in black-rimmed glasses, front row; she adjusts her glasses at 1.7. Man on the right wipes his eyes with a tissue 0.2-2.7; at 3.2-3.7 he has leaned forward and only his dark suit at the right edge is visible (box kept on the suit). Laughing not used: everyone laughs. Programme and rose lie close together; pills split by x (0.37 / 0.77)."}
json.dump(c,open('content/7001.json','w'),indent=1,ensure_ascii=False)

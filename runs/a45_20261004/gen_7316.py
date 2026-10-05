import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
off=None
officer=[(0.15,0.37,0.43,0.61),(0.16,0.42,0.74,0.57),(0.22,0.40,0.68,0.59),(0.18,0.40,0.50,0.59),(0.20,0.33,0.50,0.53),(0.30,0.38,0.38,0.54),(0.30,0.39,0.33,0.55),(0.36,0.39,0.34,0.54)]
heli=[(0.08,0.0,0.86,0.36),(0.05,0.0,0.90,0.41),(0.05,0.05,0.90,0.34),(0.05,0.02,0.70,0.37),(0.05,0.12,0.90,0.20),(0.05,0.12,0.70,0.25),(0.05,0.15,0.75,0.23),(0.05,0.15,0.80,0.23)]
sack=[off,off,off,off,(0.0,0.86,0.40,0.14),(0.0,0.86,0.30,0.14),(0.0,0.86,0.30,0.14),(0.0,0.85,0.36,0.15)]
k=lambda L:[({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]}) for t,v in zip(T,L)]
c={"mediaId":7316,"level":"B","keyWord":"major","defaultVoice":"male",
"taps":[{"phrase":"to direct the unloading","target":"the officer","voice":"male","keys":k(officer)},
{"phrase":"to spin its huge rotors","target":"the helicopter","voice":"male","keys":k(heli)},
{"phrase":"to spill rice onto the grass","target":"the torn sack","voice":"male","keys":k(sack)}],
"stillS":3.2,
"nouns":[{"word":"a helicopter","x":0.40,"y":0.30,"voice":"male"},{"word":"a major","x":0.46,"y":0.58,"voice":"male"},
{"word":"a pickup truck","x":0.85,"y":0.68,"voice":"male"},{"word":"a torn sack","x":0.16,"y":0.94,"voice":"male"}],
"question":"What is the officer doing?","answer":["He","is","directing","the","unloading."],"answerVoice":"male",
"notes":"Officer = the man in front throughout (key word 'major' only as a noun label on him; rank not readable). Helicopter box kept to the hub/upper body above the officer's head to avoid overlap. Torn sack only enters at 2.2 s (bottom-left edge); officer box at 2.2 cut at y0.86 to stay off the sack box. Other soldiers also carry sacks, so no carrying phrase."}
json.dump(c,open('content/7316.json','w'),indent=1)

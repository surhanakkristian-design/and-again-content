import json
T=[i*0.5 for i in range(19)]
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
woman={2.0:(0.1,0.27,0.52,0.58),2.5:(0,0.38,0.92,0.32),3.0:(0.33,0.44,0.38,0.18),3.5:(0.51,0.55,0.18,0.15)}
group={4.5:(0,0.25,0.16,0.25),5.0:(0.72,0.18,0.28,0.14),6.0:(0.24,0.22,0.76,0.46),6.5:(0,0.18,1.0,0.8),7.0:(0,0.14,1.0,0.84),7.5:(0.26,0.15,0.74,0.72),8.0:(0.54,0.34,0.38,0.3)}
man={5.0:(0.46,0.69,0.2,0.16)}
c={"mediaId":4901,"level":"A","keyWord":"blue","defaultVoice":"female",
"taps":[
 {"phrase":"to smile at the camera","target":"the woman in the black bikini","voice":"female","keys":keys(woman)},
 {"phrase":"to jump in feet first","target":"the man in red shorts","voice":"male","keys":keys(man)},
 {"phrase":"to dive in together","target":"the group of friends","voice":"female","keys":keys(group)}],
"stillS":5.0,
"nouns":[{"word":"the sky","x":0.30,"y":0.10,"voice":"female"},{"word":"people","x":0.86,"y":0.24,"voice":"female"},
 {"word":"rocks","x":0.62,"y":0.42,"voice":"female"},{"word":"the sea","x":0.35,"y":0.60,"voice":"female"}],
"question":"What are the friends doing?",
"answer":["They","are","diving","into","the","blue","sea."],
"answerVoice":"female",
"notes":"Many divers in several shots. Woman in black bikini only in shot 2.0-3.5 s (smiles at 2.0). Man in red shorts visible only at 5.0 s (feet-first jump; at 5.5 s hidden in splash). Group boxed while standing on the cliff top (4.5 rotated shot, 5.0) and while diving (6.0-8.0). defaultVoice female: main persons are the women divers (evenId false, but a main person exists). The woman in a blue bikini at 0.0-1.5 s is not a target."}
json.dump(c,open('content/4901.json','w'),indent=1)

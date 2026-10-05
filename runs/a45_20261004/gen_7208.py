import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def keys(boxes):
    return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,boxes)]
w=keys([(0.22,0.26,0.56,0.57),(0.21,0.25,0.62,0.62),(0.03,0.20,0.79,0.78),(0.02,0.16,0.88,0.84),
        (0.0,0.11,0.95,0.89),(0.0,0.08,1.0,0.92),(0.0,0.08,1.0,0.92),(0.0,0.07,1.0,0.93)])
c={"mediaId":7208,"level":"A","keyWord":"have a drink","defaultVoice":"female",
"taps":[
 {"phrase":"to drink from her hands","target":"the woman","voice":"female","keys":w},
 {"phrase":"to wipe her mouth","target":"the woman","voice":"female","keys":w},
 {"phrase":"to smile at the water","target":"the woman","voice":"female","keys":w}],
"stillS":0.2,
"nouns":[{"word":"the sky","x":0.22,"y":0.10,"voice":"female"},
 {"word":"a T-shirt","x":0.33,"y":0.50,"voice":"female"},
 {"word":"water","x":0.82,"y":0.48,"voice":"female"},
 {"word":"rocks","x":0.28,"y":0.88,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","drinking","water","from","her","hands."],
"answerVoice":"female",
"notes":"Only one person, so all three phrases use the woman. Drinks from her hands 0.2-0.7 s and 3.7 s, wipes her mouth with her arm 1.7-2.2 s, smiles at the water in her hands 2.7-3.2 s. Key word 'have a drink' is a phrase, not placed. 'water' = the thin stream running down the rock at the right."}
json.dump(c,open('content/7208.json','w'),indent=1)

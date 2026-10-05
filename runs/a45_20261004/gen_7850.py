import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,boxes)]
man=K([None,(0.20,0.23,0.24,0.42),(0.20,0.23,0.22,0.42),(0.17,0.23,0.22,0.42),(0.14,0.28,0.22,0.36),
       (0.12,0.33,0.25,0.27),(0.08,0.33,0.24,0.30),(0.08,0.33,0.24,0.30)])
wom=K([None,None,(0.43,0.40,0.18,0.30),(0.39,0.39,0.24,0.27),(0.36,0.38,0.26,0.28),(0.37,0.38,0.24,0.38),(0.32,0.38,0.27,0.38),(0.32,0.38,0.27,0.38)])
hand=K([(0.29,0.69,0.27,0.31),(0.32,0.67,0.27,0.33),(0.42,0.70,0.25,0.30),(0.48,0.66,0.28,0.34),(0.55,0.66,0.27,0.34),
        (0.62,0.64,0.28,0.36),(0.62,0.65,0.30,0.35),(0.64,0.65,0.30,0.35)])
d={"mediaId":7850,"level":"B","keyWord":"go to","defaultVoice":"female",
"taps":[{"phrase":"to take his seat","target":"the man in navy","voice":"male","keys":man},
{"phrase":"to clutch a canvas bag","target":"the woman in green","voice":"female","keys":wom},
{"phrase":"to shove the door open","target":"the hand on the door","voice":"female","keys":hand}],
"stillS":3.2,
"nouns":[{"word":"an arched window","x":0.30,"y":0.20,"voice":"female"},{"word":"a desk lamp","x":0.76,"y":0.43,"voice":"female"},
{"word":"a tote bag","x":0.49,"y":0.60,"voice":"female"},{"word":"a paper cup","x":0.25,"y":0.74,"voice":"female"}],
"question":"What is the man in navy doing?",
"answer":["He","is","taking","his","seat."],
"answerVoice":"male",
"notes":"Key phrase 'go to' is not a visible noun. Man in navy is hidden by the door at 0.2 s. 'to take his seat': he bends into his row and sits down by 3.2 s; verify. The hand target is the viewer's hand (gender unknown, default voice)."}
json.dump(d,open("content/7850.json","w"),indent=1)

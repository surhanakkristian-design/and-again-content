import json
def K(times, rows):
    return [({"t": t, "off": True} if r is None else {"t": t, "x": r[0], "y": r[1], "w": round(r[2],2), "h": round(r[3],2)}) for t, r in zip(times, rows)]
T8 = [0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
man = [(.41,.25,.27,.51),(.42,.25,.26,.51),(.39,.25,.28,.51),(.39,.24,.28,.52),(.42,.24,.27,.52),(.39,.24,.28,.52),(.38,.24,.29,.53),(.40,.24,.29,.53)]
wom = [(.02,.44,.29,.21),(.02,.44,.27,.21),(.03,.43,.29,.22),(.02,.43,.27,.22),(.02,.42,.30,.22),(.02,.42,.32,.22),(.04,.43,.33,.22),(.09,.43,.30,.22)]
ball = [(.36,.02,.30,.21)]*8
d = {"mediaId":5628,"level":"A","keyWord":"be over","defaultVoice":"male","taps":[
 {"phrase":"to sweep the floor","target":"the man","voice":"male","keys":K(T8,man)},
 {"phrase":"to take off her skates","target":"the woman","voice":"female","keys":K(T8,wom)},
 {"phrase":"to hang from the ceiling","target":"the disco ball","voice":"male","keys":K(T8,ball)}],
 "stillS":0.7,
 "nouns":[{"word":"a disco ball","x":0.52,"y":0.11,"voice":"male"},{"word":"a woman","x":0.17,"y":0.52,"voice":"female"},{"word":"a broom","x":0.52,"y":0.74,"voice":"male"},{"word":"balloons","x":0.20,"y":0.84,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","sweeping","the","floor."],
 "answerVoice":"male",
 "notes":"The woman unties/takes off her roller skates on the bench and stands up from about 3.2 s; the skates stay on the floor. Man's box holds his body down to the feet, the long broom head is partly outside. Key phrase 'be over' (the party is over) cannot be shown as a noun or a tap, so it is not used."}
json.dump(d, open('content/5628.json','w'), indent=1, ensure_ascii=False)

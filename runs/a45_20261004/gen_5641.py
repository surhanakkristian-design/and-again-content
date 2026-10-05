import json
def K(times, rows):
    return [({"t": t, "off": True} if r is None else {"t": t, "x": r[0], "y": r[1], "w": round(r[2],2), "h": round(r[3],2)}) for t, r in zip(times, rows)]
def write(d):
    json.dump(d, open(f'content/{d["mediaId"]}.json', 'w'), indent=1, ensure_ascii=False)
T8 = [0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
wom = [(0.00,0.34,0.49,0.61),(0.00,0.34,0.48,0.62),(0.00,0.33,0.48,0.63),(0.00,0.33,0.47,0.64),(0.00,0.33,0.47,0.64),(0.00,0.33,0.47,0.64),(0.00,0.35,0.50,0.63),(0.00,0.34,0.50,0.64)]
man = [(0.49,0.27,0.47,0.71),(0.48,0.29,0.44,0.69),(0.48,0.31,0.40,0.67),(0.47,0.32,0.41,0.66),(0.47,0.32,0.42,0.66),(0.47,0.32,0.44,0.66),(0.50,0.33,0.42,0.65),(0.50,0.32,0.43,0.66)]
write({"mediaId":5641,"level":"B","keyWord":"be worth the money","defaultVoice":"female","taps":[
 {"phrase":"to stay dry","target":"the woman","voice":"female","keys":K(T8,wom)},
 {"phrase":"to get soaked","target":"the man","voice":"male","keys":K(T8,man)},
 {"phrase":"to hold a broken umbrella","target":"the man","voice":"male","keys":K(T8,man)}],
 "stillS":1.2,
 "nouns":[{"word":"a balcony","x":0.40,"y":0.20,"voice":"female"},{"word":"a street lamp","x":0.80,"y":0.27,"voice":"female"},{"word":"a taxi","x":0.88,"y":0.54,"voice":"female"},{"word":"a leather jacket","x":0.30,"y":0.58,"voice":"female"}],
 "question":"What is the man holding?",
 "answer":["He","is","holding","a","broken","umbrella."],
 "answerVoice":"male",
 "notes":"Only two people, so the man takes two phrases (soaked shirt, broken inside-out umbrella). Each box includes that person's own umbrella. 'to get soaked': his light blue shirt is visibly wet while she stays dry under the big umbrella. Key phrase 'be worth the money' is not visible, not used."})

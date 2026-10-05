import json
def K(times, rows):
    return [({"t": t, "off": True} if r is None else {"t": t, "x": r[0], "y": r[1], "w": round(r[2],2), "h": round(r[3],2)}) for t, r in zip(times, rows)]
def write(d):
    json.dump(d, open(f'content/{d["mediaId"]}.json', 'w'), indent=1, ensure_ascii=False)
T8 = [0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
wom  = [(0.02,0.24,0.39,0.52),(0.02,0.26,0.39,0.50),(0.02,0.26,0.39,0.50),(0.02,0.31,0.40,0.45),(0.00,0.35,0.40,0.40),(0.00,0.38,0.40,0.37),(0.00,0.45,0.40,0.32),(0.00,0.46,0.40,0.31)]
man  = [(0.41,0.44,0.59,0.36),(0.41,0.45,0.59,0.35),(0.41,0.46,0.59,0.34),(0.42,0.47,0.58,0.33),(0.40,0.47,0.60,0.33),(0.40,0.47,0.60,0.33),(0.40,0.48,0.60,0.34),(0.40,0.49,0.60,0.33)]
goat = [(0.76,0.29,0.23,0.15),(0.76,0.31,0.23,0.14),(0.71,0.32,0.23,0.14),(0.68,0.33,0.25,0.14),(0.68,0.33,0.24,0.14),(0.67,0.33,0.25,0.14),(0.66,0.34,0.24,0.14),(0.65,0.35,0.24,0.14)]
write({"mediaId":5640,"level":"B","keyWord":"be worth it","defaultVoice":"female","taps":[
 {"phrase":"to punch the air","target":"the woman","voice":"female","keys":K(T8,wom)},
 {"phrase":"to spread his arms wide","target":"the man","voice":"male","keys":K(T8,man)},
 {"phrase":"to stand on a rocky ledge","target":"the goat","voice":"female","keys":K(T8,goat)}],
 "stillS":2.2,
 "nouns":[{"word":"a mountain goat","x":0.80,"y":0.42,"voice":"female"},{"word":"a water bottle","x":0.58,"y":0.79,"voice":"female"},{"word":"hiking boots","x":0.20,"y":0.87,"voice":"female"},{"word":"backpacks","x":0.72,"y":0.95,"voice":"female"}],
 "question":"What is the man doing?",
 "answer":["He","is","spreading","his","arms","wide."],
 "answerVoice":"male",
 "notes":"The woman punches the air with both fists 0.2-1.7 s, then lowers her arms and lies back. Her bare feet reach into the man's box (her legs lie across in front of him); boxes split at about x 0.41. The goat box bottom is cut at the man's box top so they do not overlap (goat hooves stand just above the man's hand). Key phrase 'be worth it' is not visible, not used."})

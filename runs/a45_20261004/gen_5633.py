import json
def K(times, rows):
    return [({"t": t, "off": True} if r is None else {"t": t, "x": r[0], "y": r[1], "w": round(r[2],2), "h": round(r[3],2)}) for t, r in zip(times, rows)]
def write(d):
    json.dump(d, open(f'content/{d["mediaId"]}.json', 'w'), indent=1, ensure_ascii=False)
T8 = [0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
wom = [(0.09,0.34,0.47,0.55),(0.08,0.34,0.46,0.54),(0.05,0.34,0.51,0.63),(0.05,0.34,0.51,0.62),(0,0.31,0.57,0.60),(0,0.29,0.57,0.64),(0,0.30,0.52,0.68),(0.10,0.25,0.36,0.62)]
man = [(0.56,0.46,0.44,0.46),(0.54,0.46,0.46,0.48),(0.56,0.43,0.44,0.52),(0.56,0.41,0.44,0.55),(0.57,0.39,0.43,0.61),(0.57,0.37,0.43,0.63),(0.52,0.38,0.48,0.62),(0.46,0.38,0.54,0.62)]
lamp = [(0.75,0.09,0.20,0.16),(0.77,0.08,0.20,0.16),(0.78,0.06,0.20,0.16),(0.79,0.02,0.20,0.16),(0.79,0.02,0.20,0.15),(0.79,0,0.20,0.14),(0.79,0,0.20,0.14),(0.80,0,0.20,0.14)]
write({"mediaId":5633,"level":"B","keyWord":"be there for someone","defaultVoice":"female","taps":[
 {"phrase":"to drape a jacket over him","target":"the woman","voice":"female","keys":K(T8,wom)},
 {"phrase":"to sit hunched on a bench","target":"the man","voice":"male","keys":K(T8,man)},
 {"phrase":"to hang from the roof","target":"the lantern","voice":"female","keys":K(T8,lamp)}],
 "stillS":0.2,
 "nouns":[{"word":"a lantern","x":0.85,"y":0.17,"voice":"female"},{"word":"a bench","x":0.40,"y":0.75,"voice":"female"},{"word":"a dog","x":0.87,"y":0.80,"voice":"female"},{"word":"an umbrella","x":0.55,"y":0.90,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","draping","a","jacket","over","him."],
 "answerVoice":"female",
 "notes":"The woman's arms reach over the man, so the boxes are split at about x 0.52-0.57; in the last frame (3.7 s) her head touches his and the split is at x 0.46. The man sits hunched only in the first second, then looks up. The lantern drifts to the top edge as the camera moves (partly cut off at 3.7 s). Key phrase 'be there for someone' is abstract and not placed as a noun; the dog is dark and only at the right edge."})

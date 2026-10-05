import json
def K(times, rows):
    return [({"t": t, "off": True} if r is None else {"t": t, "x": r[0], "y": r[1], "w": round(r[2],2), "h": round(r[3],2)}) for t, r in zip(times, rows)]
def write(d):
    json.dump(d, open(f'content/{d["mediaId"]}.json', 'w'), indent=1, ensure_ascii=False)
T8 = [0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
bm  = [(0.20,0.27,0.33,0.68),(0.20,0.28,0.35,0.68),(0.20,0.27,0.35,0.71),(0.20,0.27,0.36,0.71),(0.19,0.25,0.35,0.73),(0.18,0.25,0.36,0.73),(0.16,0.25,0.38,0.74),(0.14,0.25,0.40,0.74)]
out = [(0.53,0.34,0.18,0.32),(0.55,0.34,0.18,0.33),(0.55,0.34,0.18,0.33),(0.56,0.35,0.18,0.32),(0.54,0.35,0.18,0.31),(0.54,0.34,0.18,0.32),(0.54,0.35,0.18,0.32),(0.54,0.35,0.18,0.32)]
wom = [(0.71,0.27,0.29,0.73),(0.73,0.26,0.27,0.74),(0.73,0.26,0.27,0.74),(0.74,0.26,0.26,0.74),(0.72,0.25,0.28,0.75),(0.72,0.25,0.28,0.75),(0.72,0.26,0.28,0.74),(0.72,0.27,0.28,0.73)]
write({"mediaId":5643,"level":"A","keyWord":"beg","defaultVoice":"male","taps":[
 {"phrase":"to beg the woman","target":"the man in front","voice":"male","keys":K(T8,bm)},
 {"phrase":"to push a cart","target":"the man outside","voice":"male","keys":K(T8,out)},
 {"phrase":"to carry a big bag","target":"the woman with the bag","voice":"female","keys":K(T8,wom)}],
 "stillS":0.2,
 "nouns":[{"word":"an apron","x":0.32,"y":0.58,"voice":"male"},{"word":"boxes","x":0.72,"y":0.55,"voice":"male"},{"word":"a bag","x":0.82,"y":0.74,"voice":"male"},{"word":"a roof","x":0.66,"y":0.22,"voice":"male"}],
 "question":"What is the man in front doing?",
 "answer":["He","is","begging","the","woman."],
 "answerVoice":"male",
 "notes":"Begging is shown by the clasped hands and pleading lean towards the woman. The man outside pushes a trolley (A-level word: cart) with wooden crates (A-level: boxes); his box is cut at x 0.53-0.56 where the front man's elbows are. The woman's bag reaches left of her box (split at about x 0.72). The woman in the apron outside is not used."})

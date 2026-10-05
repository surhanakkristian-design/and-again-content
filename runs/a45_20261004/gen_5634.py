import json
def K(times, rows):
    return [({"t": t, "off": True} if r is None else {"t": t, "x": r[0], "y": r[1], "w": round(r[2],2), "h": round(r[3],2)}) for t, r in zip(times, rows)]
def write(d):
    json.dump(d, open(f'content/{d["mediaId"]}.json', 'w'), indent=1, ensure_ascii=False)
T8 = [0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
wom = [(0.19,0.21,0.36,0.77)]*8
man = [(0.55,0.33,0.30,0.39),(0.55,0.33,0.30,0.39),(0.55,0.33,0.30,0.39),(0.55,0.33,0.31,0.39),(0.55,0.33,0.31,0.39),(0.55,0.30,0.32,0.42),(0.55,0.33,0.32,0.39),(0.55,0.33,0.33,0.39)]
dog = [(0.01,0.40,0.18,0.22)]*8
write({"mediaId":5634,"level":"B","keyWord":"be tired of","defaultVoice":"female","taps":[
 {"phrase":"to take a mirror selfie","target":"the woman","voice":"female","keys":K(T8,wom)},
 {"phrase":"to rummage through a drawer","target":"the man","voice":"male","keys":K(T8,man)},
 {"phrase":"to stand on the duvet","target":"the dog","voice":"female","keys":K(T8,dog)}],
 "stillS":0.2,
 "nouns":[{"word":"a chandelier","x":0.48,"y":0.10,"voice":"female"},{"word":"a dog","x":0.12,"y":0.50,"voice":"female"},{"word":"a towel","x":0.66,"y":0.58,"voice":"female"},{"word":"clothes","x":0.72,"y":0.82,"voice":"female"}],
 "question":"What is the man doing?",
 "answer":["He","is","rummaging","through","a","drawer."],
 "answerVoice":"male",
 "notes":"The whole clip is a mirror reflection; the camera barely moves, so the boxes are almost constant. The woman's coat edge and the man's knees meet at about x 0.55 (split there); the dog's box ends where the woman's coat starts (x 0.19). The man pulls a shirt out at about 2.7 s. Key phrase 'be tired of' is shown only by her flat face, so it is not used in a phrase."})

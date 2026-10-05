import json
def K(times, rows):
    return [({"t": t, "off": True} if r is None else {"t": t, "x": r[0], "y": r[1], "w": round(r[2],2), "h": round(r[3],2)}) for t, r in zip(times, rows)]
def write(d):
    json.dump(d, open(f'content/{d["mediaId"]}.json', 'w'), indent=1, ensure_ascii=False)
T8 = [0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
wom = [(0.64,0.28,0.30,0.57),(0.65,0.28,0.28,0.57),(0.65,0.27,0.29,0.59),(0.66,0.27,0.27,0.59),(0.66,0.25,0.28,0.62),(0.67,0.25,0.28,0.62),(0.67,0.25,0.29,0.62),(0.67,0.24,0.29,0.63)]
man = [(0.07,0.39,0.33,0.43),(0.07,0.39,0.33,0.43),(0.05,0.39,0.35,0.43),(0.05,0.39,0.35,0.43),(0.03,0.38,0.37,0.45),(0.03,0.38,0.37,0.45),(0.01,0.38,0.39,0.45),(0.03,0.38,0.38,0.45)]
cat = [(0.44,0.51,0.20,0.14),(0.45,0.51,0.20,0.14),(0.45,0.51,0.20,0.14),(0.45,0.51,0.21,0.14),(0.44,0.51,0.22,0.14),(0.45,0.51,0.22,0.14),(0.45,0.52,0.22,0.14),(0.45,0.52,0.22,0.14)]
write({"mediaId":5637,"level":"B","keyWord":"be used to","defaultVoice":"female","taps":[
 {"phrase":"to stare at the passing train","target":"the woman","voice":"female","keys":K(T8,wom)},
 {"phrase":"to tuck into his cereal","target":"the man","voice":"male","keys":K(T8,man)},
 {"phrase":"to doze on the windowsill","target":"the cat","voice":"female","keys":K(T8,cat)}],
 "stillS":2.2,
 "nouns":[{"word":"a train","x":0.42,"y":0.30,"voice":"female"},{"word":"a cat","x":0.56,"y":0.57,"voice":"female"},{"word":"a chair","x":0.18,"y":0.74,"voice":"female"},{"word":"floorboards","x":0.55,"y":0.90,"voice":"female"}],
 "question":"What is the woman staring at?",
 "answer":["She","is","staring","at","the","passing","train."],
 "answerVoice":"female",
 "notes":"The woman's hand with the mug reaches just above the cat, so her box starts at x 0.64-0.67 and her foot/hand are slightly cut at the left; the cat's box ends there. In the first frame (0.2 s) she still faces the train while turning, mouth open from 0.7 s. Key phrase 'be used to' is shown only by the calm man, so it is not used as a noun."})

import json
def K(times, rows):
    return [({"t": t, "off": True} if r is None else {"t": t, "x": r[0], "y": r[1], "w": round(r[2],2), "h": round(r[3],2)}) for t, r in zip(times, rows)]
def write(d):
    json.dump(d, open(f'content/{d["mediaId"]}.json', 'w'), indent=1, ensure_ascii=False)
T8 = [0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
red  = [(0.42,0.32,0.50,0.58),(0.42,0.32,0.54,0.60),(0.40,0.32,0.52,0.64),(0.38,0.32,0.56,0.67),(0.35,0.29,0.62,0.71),(0.23,0.27,0.74,0.73),(0.20,0.27,0.72,0.73),(0.19,0.25,0.78,0.75)]
pink = [(0.22,0.27,0.20,0.45),(0.23,0.27,0.19,0.47),(0.21,0.28,0.19,0.47),(0.17,0.27,0.21,0.47),(0.08,0.25,0.27,0.51),(0.00,0.25,0.23,0.40),(0.00,0.24,0.20,0.43),(0.00,0.23,0.19,0.37)]
man  = [(0.00,0.24,0.22,0.50),(0.00,0.23,0.23,0.51),(0.00,0.24,0.21,0.52),(0.00,0.24,0.17,0.50),(0.00,0.22,0.08,0.50),None,None,None]
write({"mediaId":5638,"level":"B","keyWord":"be willing to","defaultVoice":"female","taps":[
 {"phrase":"to trap a spider","target":"the woman in red","voice":"female","keys":K(T8,red)},
 {"phrase":"to wear a pink slip dress","target":"the woman in pink","voice":"female","keys":K(T8,pink)},
 {"phrase":"to wear a green hoodie","target":"the man","voice":"male","keys":K(T8,man)}],
 "stillS":0.2,
 "nouns":[{"word":"a spider","x":0.89,"y":0.41,"voice":"female"},{"word":"a potted plant","x":0.68,"y":0.14,"voice":"female"},{"word":"a shelf","x":0.80,"y":0.23,"voice":"female"},{"word":"a cushion","x":0.28,"y":0.86,"voice":"female"}],
 "question":"What is the woman in red doing?",
 "answer":["She","is","trapping","a","spider","with","a","glass."],
 "answerVoice":"female",
 "notes":"The man and the woman in pink cling to each other and both look scared, so no action fits only one of them; they get clothing states. The man is hidden behind the woman in pink from 2.7 s (OFF). Key phrase 'be willing to' is not visible, not used. Spider pill sits at the right edge (spider at about x 0.91)."})

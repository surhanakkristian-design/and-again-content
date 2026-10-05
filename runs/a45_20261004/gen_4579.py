import json
def K(rows):
    out=[]
    for r in rows:
        if len(r)==1: out.append({"t":r[0],"off":True})
        else: out.append({"t":r[0],"x":r[1],"y":r[2],"w":r[3],"h":r[4]})
    return out
woman=K([(0.0,0,0,1,0.42),(0.5,0,0,1,0.40),(1.0,0,0,1,0.41),(1.5,0,0,1,0.43),(2.0,0,0,1,0.45),
(2.5,0,0.31,1,0.69),(3.0,0,0.40,1,0.60),(3.5,0,0.38,1,0.62),(4.0,0,0.40,1,0.60),
(4.5,0.08,0.27,0.92,0.73),(5.0,0.08,0.30,0.92,0.70),(5.5,0.10,0.33,0.90,0.67),(6.0,0.05,0.32,0.95,0.68),(6.5,0.08,0.31,0.92,0.69),
(7.0,0.29,0.40,0.37,0.44),(7.5,0.38,0.40,0.24,0.43),(8.0,0.27,0.39,0.47,0.31),(8.5,0.28,0.38,0.49,0.33),
(9.0,0.37,0.39,0.30,0.46),(9.5,0.38,0.39,0.34,0.47),(10.0,0.24,0.37,0.56,0.37),(10.5,0.21,0.37,0.63,0.40),
(11.0,0.20,0.38,0.65,0.54),(11.5,0.18,0.38,0.68,0.56),(12.0,0.16,0.37,0.71,0.45)])
globe=K([(0.0,0,0.42,1,0.58),(0.5,0,0.40,1,0.60),(1.0,0,0.41,1,0.59),(1.5,0,0.43,1,0.57),(2.0,0,0.45,1,0.55)]+[(t/2,) for t in range(5,25)])
d={"mediaId":4579,"level":"A","keyWord":"abroad","defaultVoice":"female",
"taps":[
 {"phrase":"to open her arms wide","target":"the woman","voice":"female","keys":woman},
 {"phrase":"to turn very fast","target":"the globe","voice":"female","keys":globe},
 {"phrase":"to stand on the sand","target":"the woman","voice":"female","keys":woman}],
"stillS":4.0,
"nouns":[{"word":"the sky","x":0.78,"y":0.10,"voice":"female"},{"word":"a tower","x":0.50,"y":0.27,"voice":"female"},
 {"word":"a jacket","x":0.52,"y":0.68,"voice":"female"},{"word":"jeans","x":0.52,"y":0.90,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","opening","her","arms","wide."],
"answerVoice":"female",
"notes":"Four shots (cuts at 2.5, 4.5, 7.0 s). The globe = the big school globe of the first shot (0-2 s), it spins from 0.5 s; woman and globe overlap there, boxes split along the top of the globe. A tiny globe trinket hangs on her backpack in the later shots; it is part of her box, the globe target is off there. Arms wide: 2.5-4 s and on the dune. 'to stand on the sand' is true only in the last shot (7-12 s). Key word 'abroad' is an adverb, not placed and not forced into the answer."}
json.dump(d,open("content/4579.json","w"),indent=1,ensure_ascii=False)

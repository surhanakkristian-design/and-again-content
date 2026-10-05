import json
def K(rows):
    out=[]
    for r in rows:
        if len(r)==1: out.append({"t":r[0],"off":True})
        else: out.append({"t":r[0],"x":r[1],"y":r[2],"w":r[3],"h":r[4]})
    return out
boy=K([(0.0,0.01,0.41,0.19,0.15),(0.5,0.20,0.39,0.21,0.19),(1.0,0.25,0.39,0.18,0.31),(1.5,0.30,0.34,0.18,0.59),
(2.0,0.23,0.27,0.24,0.73),(2.5,0.24,0.23,0.32,0.77),(3.0,0,0.31,0.30,0.50),(3.5,0.02,0.24,0.39,0.63),(4.0,0,0.02,0.20,0.96),
(4.5,0.10,0.04,0.47,0.96),(5.0,0.05,0.07,0.45,0.93),(5.5,0.07,0.19,0.41,0.81),(6.0,0.05,0.22,0.42,0.78),(6.5,0.13,0.22,0.41,0.78),
(7.0,0.31,0.30,0.31,0.70),(7.5,0.17,0.39,0.34,0.36),(8.0,0.13,0.38,0.29,0.31),(8.5,0.43,0.39,0.34,0.35),(9.0,0.82,0.37,0.18,0.32)])
girl=K([(0.0,0.60,0.39,0.40,0.33),(0.5,0.44,0.38,0.30,0.32),(1.0,0.43,0.39,0.18,0.31),(1.5,0.48,0.34,0.21,0.59),
(2.0,0.47,0.27,0.29,0.73),(2.5,0.56,0.23,0.31,0.77),(3.0,0.45,0.30,0.26,0.50),(3.5,0.65,0.23,0.35,0.63),(4.0,0.42,0.14,0.58,0.70),
(4.5,0.57,0.04,0.43,0.96),(5.0,0.50,0.07,0.45,0.93),(5.5,0.48,0.19,0.42,0.81),(6.0,0.47,0.22,0.38,0.78),(6.5,0.54,0.22,0.37,0.78),
(7.0,0.62,0.33,0.33,0.67),(7.5,0.60,0.38,0.30,0.35),(8.0,0.82,0.38,0.18,0.32),(8.5,0,0.40,0.28,0.30),(9.0,0.33,0.40,0.33,0.33)])
ruler=K([(t/2,) for t in range(0,11)]+[(5.5,0.10,0.05,0.75,0.14),(6.0,0.08,0.08,0.74,0.14),(6.5,0.15,0.08,0.75,0.14)]+[(t/2,) for t in range(14,19)])
d={"mediaId":4582,"level":"B","keyWord":"measure","defaultVoice":"female",
"taps":[
 {"phrase":"to hug the boy tightly","target":"the girl","voice":"female","keys":girl},
 {"phrase":"to push a green wheelbarrow","target":"the boy","voice":"male","keys":boy},
 {"phrase":"to rest on their heads","target":"the ruler","voice":"female","keys":ruler}],
"stillS":6.5,
"nouns":[{"word":"a house","x":0.78,"y":0.08,"voice":"female"},{"word":"a ruler","x":0.40,"y":0.20,"voice":"female"},
 {"word":"denim shorts","x":0.72,"y":0.86,"voice":"female"},{"word":"a lawn","x":0.14,"y":0.88,"voice":"female"}],
"question":"What is resting on their heads?",
"answer":["A","ruler","is","resting","on","their","heads."],
"answerVoice":"female",
"notes":"Four shots: run + hug (0-2.5), wheelbarrows (3-4), back to back with the ruler (4.5-6.5), children running at the party (7-9). Boy and girl touch or overlap in most frames: boxes split along the line between them. Hug: both hold each other, phrase is worded from the girl's side ('the boy' as object) so it fits only her. Wheelbarrow: at 3.0 the boy pushes the green one, the girl a rust-brown one; at 4.0 the girl runs behind the green wheelbarrow, her box includes part of it. Ruler: clear at 5.5-6.5; at 5.0 only a blurred strip at the top edge, set off. Doubt: in the last shot (7.5-9.0) the generated clip is inconsistent - at 8.5 and 9.0 the girl box is on the running girl in the pink top and denim shorts (she has a ponytail there, may be a different girl; at 8.0 the main girl is at the right edge); the boy = dark T-shirt, grey shorts. Key word 'measure' is a verb, nobody but a hand does it, so it is not a phrase; the ruler scene is the question. Mixed pair, evenId true -> default voice female."}
json.dump(d,open("content/4582.json","w"),indent=1,ensure_ascii=False)

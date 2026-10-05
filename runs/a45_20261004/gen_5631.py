import json
def K(times, rows):
    return [({"t": t, "off": True} if r is None else {"t": t, "x": r[0], "y": r[1], "w": round(r[2],2), "h": round(r[3],2)}) for t, r in zip(times, rows)]
T8 = [0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
two = [(.20,.29,.60,.66),(.21,.30,.55,.66),(.20,.31,.56,.67),(.17,.29,.68,.69),(.16,.28,.72,.69),(.18,.27,.59,.71),(.20,.29,.52,.70),(.17,.29,.57,.70)]
lamp = [(.80,.33,.18,.18),(.76,.33,.21,.17),(.76,.34,.20,.17),None,None,None,None,None]
d = {"mediaId":5631,"level":"A","keyWord":"be similar to","defaultVoice":"female","taps":[
 {"phrase":"to point at each other","target":"the two women in green","voice":"female","keys":K(T8,two)},
 {"phrase":"to hug each other","target":"the two women in green","voice":"female","keys":K(T8,two)},
 {"phrase":"to hold a lamp","target":"the woman in the back","voice":"female","keys":K(T8,lamp)}],
 "stillS":0.2,
 "nouns":[{"word":"lights","x":0.45,"y":0.21,"voice":"female"},{"word":"a door","x":0.13,"y":0.31,"voice":"female"},{"word":"a lamp","x":0.90,"y":0.44,"voice":"female"},{"word":"a sofa","x":0.18,"y":0.69,"voice":"female"}],
 "question":"What are the two women doing?",
 "answer":["They","are","pointing","at","each","other."],
 "answerVoice":"female",
 "notes":"The two look-alike women do everything together (laugh, point, hug), so they are ONE target for two phrases. Pointing is clear 0.2-1.2 s, the hug from about 2.7 s. The third woman (lilac dress, background right) holds a small lantern-lamp only clearly visible 0.2-1.2 s; from 1.7 s she is hidden behind the right woman (only her hands show), so off. 'a sofa' = the wicker daybed with cushions. Key phrase 'be similar to' is not a visible action/noun."}
json.dump(d, open('content/5631.json','w'), indent=1, ensure_ascii=False)

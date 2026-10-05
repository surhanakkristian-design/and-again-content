import json, sys
T = [0.2, 0.7, 1.2, 1.7, 2.2, 2.7, 3.2, 3.7]
def keys(boxes):
    out = []
    for t, b in zip(T, boxes):
        if b is None: out.append({"t": t, "off": True}); continue
        x0, y0, x1, y1 = b
        x0, y0 = max(0, x0), max(0, y0); x1, y1 = min(1, x1), min(1, y1)
        out.append({"t": t, "x": round(x0, 2), "y": round(y0, 2), "w": round(x1 - x0, 2), "h": round(y1 - y0, 2)})
    return out
def tap(phrase, target, voice, boxes): return {"phrase": phrase, "target": target, "voice": voice, "keys": keys(boxes)}
def noun(w, x, y, v): return {"word": w, "x": x, "y": y, "voice": v}
def write(c):
    json.dump(c, open(f"content/{c['mediaId']}.json", "w"), indent=1, ensure_ascii=False)
C = {}
# 5544
W = [(.12,.33,.43,.76),(.12,.33,.42,.76),(.11,.33,.41,.77),(.11,.33,.40,.77),(.10,.33,.38,.77),(.11,.33,.39,.77),(.12,.33,.43,.78),(.11,.33,.42,.78)]
F = [(.43,.25,.62,.87),(.42,.24,.62,.87),(.41,.24,.61,.88),(.40,.21,.61,.88),(.38,.20,.58,.89),(.39,.20,.59,.89),(.43,.19,.62,.89),(.42,.19,.62,.90)]
M = [(.62,.16,1,.47),(.62,.15,1,.47),(.61,.14,1,.45),(.61,.13,1,.45),(.58,.12,1,.46),(.59,.11,1,.46),(.62,.10,1,.45),(.62,.08,1,.46)]
C[5544] = {"mediaId":5544,"level":"A","keyWord":"alive","defaultVoice":"female",
 "taps":[tap("to clap her hands","the woman","female",W),tap("to stand on long legs","the baby horse","female",F),tap("to put its head down","the big horse","female",M)],
 "stillS":2.7,"nouns":[noun("the sky",.30,.16,"female"),noun("a bucket",.12,.44,"female"),noun("a jacket",.24,.55,"female"),noun("straw",.50,.92,"female")],
 "question":"What is the woman doing?","answer":["She","is","clapping","her","hands."],"answerVoice":"female",
 "notes":"Woman claps clearly only from 3.2 s; before that she raises her gloved hands while laughing. Baby horse and big horse boxes split along a vertical line (mare's nose touches the foal's neck), so the foal's right hind leg lies partly outside its box. Avoided the noun 'a horse' (two horses)."}
# 5545
W = [(.23,.25,.68,.84),(.22,.25,.70,.82),(.19,.27,.70,.84),(.19,.28,.70,.83),(.21,.28,.60,.80),(.22,.28,.60,.79),(.29,.27,.62,.85),(.32,.25,.74,.85)]
Y = [(0,.27,.18,.48)]*8
O = [(.82,.29,1,.64),(.82,.29,1,.66),(.82,.29,1,.65),(.82,.30,1,.66),(.80,.29,1,.64),(.80,.30,1,.50),(.80,.31,1,.47),None]
C[5545] = {"mediaId":5545,"level":"A","keyWord":"all","defaultVoice":"female",
 "taps":[tap("to push a shopping trolley","the woman","female",W),tap("to hold some papers","the young man","male",Y),tap("to wear a blue jumper","the old man","male",O)],
 "stillS":0.7,"nouns":[noun("watermelons",.70,.38,"female"),noun("a trolley",.80,.78,"female"),noun("a shelf",.18,.62,"female"),noun("the floor",.55,.93,"female")],
 "question":"What is the woman pushing?","answer":["She","is","pushing","a","trolley","full","of","watermelons."],"answerVoice":"female",
 "notes":"Old man is small at the right edge and hidden behind the melon tower at 3.7 s (off); his box also takes in part of the old woman next to him. Young man = shop worker in green apron holding a clipboard with papers."}
# 5546
M = [(.02,.31,.49,.71),(.02,.31,.51,.70),(.02,.31,.49,.72),(.02,.31,.47,.71),(.02,.30,.48,.71),(.02,.31,.46,.71),(.02,.31,.47,.72),(.02,.31,.46,.72)]
Wo = [(.50,.37,.70,.60),(.51,.37,.70,.60),(.50,.37,.70,.61),(.47,.37,.69,.61),(.49,.37,.70,.60),(.47,.37,.69,.60),(.47,.37,.68,.61),(.46,.37,.68,.61)]
S = [None,(.66,.67,.84,.81),(.69,.67,.87,.81),(.75,.64,.93,.78),(.77,.63,.95,.77),(.78,.62,.96,.76),(.80,.60,.98,.74),(.81,.59,.99,.73)]
C[5546] = {"mediaId":5546,"level":"B","keyWord":"alternative","defaultVoice":"male",
 "taps":[tap("to empty a cooking pot","the man","male",M),tap("to hold a wooden paddle","the woman","female",Wo),tap("to drift on the water","the wooden spoon","male",S)],
 "stillS":2.7,"nouns":[noun("a canoe",.20,.74,"male"),noun("a cooking pot",.70,.63,"male"),noun("pine trees",.80,.33,"male"),noun("a raincoat",.60,.51,"male")],
 "question":"What is the man doing?","answer":["He","is","paddling","with","a","cooking","pot."],"answerVoice":"male",
 "notes":"Man and woman split along a vertical line; man's hands and pot on the pole reach past the split (x ~0.6) so his box covers head and body only. Spoon not visible at 0.2 s (off). 'to empty a cooking pot': he lifts the pot and water pours out (0.7-2.2 s)."}
# 5547
W = [(.35,.39,.65,.79),(.38,.39,.66,.79),(.35,.38,.65,.79),(.35,.38,.65,.79),(.35,.38,.64,.79),(.35,.37,.66,.80),(.34,.37,.64,.81),(.35,.37,.66,.82)]
L = [(.40,.03,.58,.28),(.41,.02,.58,.28),(.40,.02,.59,.28),(.41,.01,.58,.28),(.40,.01,.59,.27),(.40,0,.58,.26),(.40,0,.59,.26),(.40,0,.58,.26)]
R = [(0,.80,1,1),(0,.80,1,1),(0,.80,1,1),(0,.80,1,1),(0,.80,1,1),(0,.81,1,1),(0,.82,1,1),(0,.83,1,1)]
C[5547] = {"mediaId":5547,"level":"B","keyWord":"amber","defaultVoice":"female",
 "taps":[tap("to gaze at the light","the woman","female",W),tap("to glow a steady amber","the traffic light","female",L),tap("to reflect the amber light","the wet road","female",R)],
 "stillS":1.7,"nouns":[noun("a traffic light",.50,.12,"female"),noun("a balcony",.20,.24,"female"),noun("a bicycle",.20,.60,"female"),noun("a scooter",.72,.66,"female")],
 "question":"What is the woman doing?","answer":["She","is","gazing","at","the","amber","traffic","light."],"answerVoice":"female",
 "notes":"Wet road box is the lower band under the scooter (the amber streak reflection); road around the scooter left out to keep clear of the woman's box. Woman's box covers her, not the whole scooter."}
for i in (sys.argv[1:] or C):
    write(C[int(i)])

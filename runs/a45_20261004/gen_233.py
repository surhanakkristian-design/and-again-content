import json, os
RUN = os.path.dirname(os.path.abspath(__file__))
def keys(n, d):
    out = []
    for i in range(n):
        t = i * 0.5
        b = d.get(t)
        if b is None: out.append({"t": t, "off": True})
        else:
            x0, y0, x1, y1 = b
            out.append({"t": t, "x": round(x0, 2), "y": round(y0, 2), "w": round(x1 - x0, 2), "h": round(y1 - y0, 2)})
    return out
docs = {}
# 233
n = 13
man = {0.0: (.02,.13,.92,.72), 0.5: (0,.09,.79,.88), 1.0: (0,.41,1,1), 1.5: (0,.41,1,1), 2.0: (0,.20,.74,1),
       2.5: (0,.02,.70,.98), 3.0: (0,0,.72,1), 3.5: (0,.03,.71,1), 4.0: (0,.05,.66,1), 4.5: (0,.02,.66,1),
       5.0: (0,.02,.67,1), 5.5: (0,.02,.66,1), 6.0: (0,.02,.65,1)}
woman = {2.5: (.70,.12,1,.33), 3.0: (.72,0,1,.90), 3.5: (.71,.02,1,.92), 4.0: (.66,0,1,.82), 4.5: (.66,0,1,.82),
         5.0: (.67,0,1,.92), 5.5: (.66,.05,1,.95), 6.0: (.65,.05,1,.85)}
rope = {0.0: (.66,.72,1,.87), 0.5: (.79,.27,1,.42), 1.0: (.76,.25,1,.41), 1.5: (.76,.25,1,.41), 2.0: (.74,.29,1,.43),
        2.5: (.72,.33,1,.47)}
docs[233] = {"mediaId": 233, "level": "B", "keyWord": "dislocate", "defaultVoice": "male",
  "taps": [
    {"phrase": "to clutch his injured shoulder", "target": "the man", "voice": "male", "keys": keys(n, man)},
    {"phrase": "to kneel beside the climber", "target": "the woman", "voice": "female", "keys": keys(n, woman)},
    {"phrase": "to lie coiled on the grass", "target": "the rope", "voice": "male", "keys": keys(n, rope)}],
  "stillS": 4.5,
  "nouns": [{"word": "a helmet", "x": .25, "y": .13, "voice": "male"}, {"word": "a shoulder", "x": .54, "y": .38, "voice": "male"},
            {"word": "a jacket", "x": .84, "y": .47, "voice": "male"}, {"word": "grass", "x": .62, "y": .90, "voice": "male"}],
  "question": "What is the man doing?",
  "answer": ["He", "is", "clutching", "his", "injured", "shoulder."], "answerVoice": "male",
  "notes": "Key word 'dislocate' cannot be read from the picture alone, so the texts use 'injured shoulder'. Rope: visible 0-2.5 s only; after that only slivers behind the woman (set off). Rope and man overlap in the picture at 0.5-2.5 s: man box trimmed (right arm edge at 0.5/2.0 s, strip of his back at 1.0/1.5 s). Woman at 2.5 s = only her hand and sleeve at the right edge. Man/woman split along the line between his shoulder and her jacket; her hands on his arm (5.5-6.0 s) fall into his box."}
# 235
n = 21
dog = {0.0: (.27,.20,.80,.70), 0.5: (.24,.31,.96,.90), 1.0: (0,.45,.72,.86), 1.5: (.20,.47,.70,1), 2.0: (.42,.45,.70,.70),
       2.5: (.43,.41,.82,.58), 3.0: (.42,.38,.82,.55), 3.5: (.38,.38,.72,.56), 4.0: (.31,.35,.64,.60), 4.5: (.30,.24,.75,.68),
       5.0: (.25,.02,.86,.86), 5.5: (0,0,1,.73), 6.0: (.10,0,.92,.73), 6.5: (.05,.15,.82,.67), 7.0: (.06,.15,1,.51),
       7.5: (.31,.26,.92,.86), 8.0: (.42,.28,.90,.80), 8.5: (.45,.22,1,.80), 9.0: (.30,.27,1,1), 9.5: (.30,.24,.96,.98),
       10.0: (.26,.21,.92,.84)}
woman = {0.0: (0,.70,.62,1), 1.0: (.14,.86,.50,1), 5.5: (0,.73,.37,1), 6.0: (0,.74,.20,1), 6.5: (0,.67,.68,1),
         7.0: (0,.51,.58,1), 7.5: (0,.05,.31,1), 8.0: (0,0,.42,1), 8.5: (0,0,.45,1), 9.0: (0,0,.30,1), 9.5: (0,0,.30,1),
         10.0: (0,0,.26,1)}
tree = {1.0: (.15,0,1,.42), 1.5: (0,0,1,.45), 2.0: (0,0,1,.44), 2.5: (0,0,1,.40), 3.0: (0,0,1,.37), 3.5: (0,0,1,.37),
        4.0: (0,0,1,.33), 4.5: (0,0,1,.24)}
docs[235] = {"mediaId": 235, "level": "B", "keyWord": "fetch", "defaultVoice": "female",
  "taps": [
    {"phrase": "to fetch a red ball", "target": "the dog", "voice": "female", "keys": keys(n, dog)},
    {"phrase": "to rub the dog's belly", "target": "the woman", "voice": "female", "keys": keys(n, woman)},
    {"phrase": "to bear red apples", "target": "the tree", "voice": "female", "keys": keys(n, tree)}],
  "stillS": 4.0,
  "nouns": [{"word": "an apple tree", "x": .35, "y": .12, "voice": "female"}, {"word": "a fence", "x": .72, "y": .31, "voice": "female"},
            {"word": "a dog", "x": .47, "y": .46, "voice": "female"}, {"word": "a lawn", "x": .50, "y": .80, "voice": "female"}],
  "question": "What is the dog doing?",
  "answer": ["The", "dog", "is", "fetching", "a", "red", "ball."], "answerVoice": "female",
  "notes": "Woman: only her hand (0.0, 1.0 s) and shoes/knee (5.5-6.0 s) before she kneels down at 6.5 s. From 7.0 s she and the dog overlap heavily; split by a straight line, so her arm reaching over the dog falls into the dog's box and at 7.0 s the dog's hindquarters (below y .51) are outside its box. Tree box = crown + trunk above the dog, includes some fence; tree off at 0.0-0.5 (not recognisable) and from 5.0 s."}
# 237
donkey = {0.0: (.38,.04,1,1), 0.5: (.34,.04,1,1), 1.0: (.34,.05,1,1), 1.5: (.32,.05,1,1), 2.0: (.29,.03,1,1), 2.5: (.27,.07,1,1),
          3.0: (.23,.15,.92,1), 3.5: (.24,.11,.90,1), 4.0: (.20,.24,.90,1), 4.5: (0,.18,.90,1), 5.0: (.03,.47,1,.97),
          5.5: (.10,.40,1,.98), 6.0: (0,.21,1,.78), 6.5: (0,.19,1,.82), 7.0: (0,.23,1,.85), 7.5: (0,.28,1,.95),
          8.0: (0,0,1,.90), 8.5: (.12,.12,1,.97), 9.0: (.30,.02,1,1), 9.5: (.28,.03,.95,1), 10.0: (.17,.09,.92,1)}
birds = {0.0: (.10,.61,.38,.85), 0.5: (.10,.61,.34,.85), 1.0: (.08,.62,.34,.86), 1.5: (.06,.63,.32,.87), 2.0: (.03,.64,.29,.88),
         2.5: (.03,.66,.27,.90), 3.0: (.02,.68,.23,.92), 3.5: (0,.70,.24,.86), 4.0: (.02,.59,.20,.76)}
docs[237] = {"mediaId": 237, "level": "A", "keyWord": "donkey", "defaultVoice": "male",
  "taps": [
    {"phrase": "to open its mouth wide", "target": "the donkey", "voice": "male", "keys": keys(n, donkey)},
    {"phrase": "to roll on the ground", "target": "the donkey", "voice": "male", "keys": keys(n, donkey)},
    {"phrase": "to look for food", "target": "the birds", "voice": "male", "keys": keys(n, birds)}],
  "stillS": 1.5,
  "nouns": [{"word": "oranges", "x": .58, "y": .06, "voice": "male"}, {"word": "a house", "x": .14, "y": .46, "voice": "male"},
            {"word": "a donkey", "x": .62, "y": .55, "voice": "male"}, {"word": "birds", "x": .20, "y": .75, "voice": "male"}],
  "question": "What is the donkey doing?",
  "answer": ["The", "donkey", "is", "rolling", "on", "the", "ground."], "answerVoice": "male",
  "notes": "Only two targets (donkey, small birds on the left 0-4.0 s). 'to look for food' = the birds pecking at the cobbles; slight inference. One birds box holds all three birds. The birds stand right next to the donkey's legs, so the donkey box starts at their right edge and its left ear tip is outside the box at 0-2.5 s. Birds off from 4.5 s (only a speck far back)."}
# 238
n = 19
B = (.04,.30,.33,.67)
bush = {i*0.5: B for i in range(n)}
bush[2.5] = (.04,.30,.30,.67); bush[1.0] = (.04,.30,.30,.67); bush[8.0] = (.04,.30,.29,.67)
man = {1.0: (.30,.34,.50,.62), 1.5: (.33,.32,.52,.65), 2.0: (.34,.27,.62,.62), 2.5: (.30,.25,.80,.68), 3.0: (.34,.28,.87,.80),
       3.5: (.33,.31,.84,.84), 4.0: (.36,.28,.85,.72), 4.5: (.38,.24,.86,.72), 5.0: (.37,.28,.82,.84), 5.5: (.37,.26,.83,.84),
       6.0: (.36,.24,.80,.69), 6.5: (.47,.29,.77,.66), 7.0: (.42,.32,.66,.68), 7.5: (.33,.33,.53,.63), 8.0: (.29,.33,.47,.50)}
docs[238] = {"mediaId": 238, "level": "A", "keyWord": "steal", "defaultVoice": "male",
  "taps": [
    {"phrase": "to steal a can", "target": "the man", "voice": "male", "keys": keys(n, man)},
    {"phrase": "to carry a white bag", "target": "the man", "voice": "male", "keys": keys(n, man)},
    {"phrase": "to have pink flowers", "target": "the bush", "voice": "male", "keys": keys(n, bush)}],
  "stillS": 0.0,
  "nouns": [{"word": "the sky", "x": .55, "y": .10, "voice": "male"}, {"word": "flowers", "x": .19, "y": .43, "voice": "male"},
            {"word": "grass", "x": .80, "y": .56, "voice": "male"}, {"word": "cans", "x": .52, "y": .74, "voice": "male"}],
  "question": "What is the man doing?",
  "answer": ["He", "is", "stealing", "a", "can."], "answerVoice": "male",
  "notes": "One person only; second target = the bush with pink flowers (a state, no other thing acts). Pack of cans not used as a tap target because the man bends over it for 3 s. Man passes right beside the bush at 1.0-2.5 s and is half behind it at 8.0 s: boxes split at the bush's right edge. The cans carry a drink-brand logo (not named)."}
for i, d in docs.items():
    json.dump(d, open(os.path.join(RUN, "content", f"{i}.json"), "w"), indent=1, ensure_ascii=False)

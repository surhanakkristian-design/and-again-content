import json
def K(times, rows):
    out=[]
    assert len(times)==len(rows)
    for t,r in zip(times,rows):
        if r is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]})
    return out
def W(d): json.dump(d,open(f"content/{d['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# 795
T=[i*0.5 for i in range(19)]
man=K(T,[(0.02,0.25,0.78,0.68),(0,0.17,0.8,0.79),(0,0.12,0.82,0.88),(0,0.15,1,0.85),(0,0.1,0.72,0.86),
 (0,0.17,1,0.83),(0,0.17,1,0.83),(0,0.03,1,0.97),(0,0.03,1,0.97),(0,0,1,1),(0,0,1,1),(0,0,0.79,1),
 (0,0.07,0.53,0.88),(0,0.15,0.56,0.78),(0,0.14,0.57,0.84),(0,0.14,0.57,0.84),
 (0.15,0.2,0.72,0.25),(0.1,0.17,0.72,0.2),(0.1,0.17,0.7,0.3)])
dog=K(T,[None]*11+[(0.80,0.68,0.20,0.32),(0.53,0.38,0.43,0.6),(0.56,0.44,0.44,0.52),(0.57,0.44,0.38,0.56),(0.57,0.44,0.38,0.56),
 (0.5,0.45,0.45,0.5),(0.45,0.37,0.43,0.55),(0.43,0.47,0.45,0.53)])
W({"mediaId":795,"level":"A","keyWord":"towel","defaultVoice":"male",
 "taps":[{"phrase":"to climb out of the pool","target":"the man","voice":"male","keys":man},
         {"phrase":"to dry his hair","target":"the man","voice":"male","keys":man},
         {"phrase":"to shake its wet head","target":"the dog","voice":"male","keys":dog}],
 "stillS":7.0,
 "nouns":[{"word":"a man","x":0.30,"y":0.33,"voice":"male"},{"word":"a towel","x":0.28,"y":0.74,"voice":"male"},
          {"word":"a dog","x":0.72,"y":0.60,"voice":"male"},{"word":"a tree","x":0.80,"y":0.18,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","drying","his","hair","with","a","towel."],"answerVoice":"male",
 "notes":"Dog at 5.5 s is only a dark blur in the bottom right corner (box given). From 8.0 s man and dog overlap: the man's box is his head and shoulders above the dog, the dog's box holds the towel wrapped round it. 'a man' pill on his chest and 'a towel' pill on the hanging towel below his arm are on the same figure but 0.41 apart in y."})

# 7212
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
wom=K(T,[(0.33,0.24,0.62,0.66),(0.27,0.24,0.7,0.68),(0.26,0.24,0.74,0.76),(0.30,0.22,0.70,0.78),
 (0.37,0.18,0.63,0.82),(0.43,0.12,0.57,0.88),(0.43,0.12,0.57,0.88),(0.45,0.1,0.55,0.9)])
bird=K(T,[(0.04,0.40,0.29,0.17),(0.04,0.41,0.23,0.17),(0.02,0.41,0.24,0.18),(0.02,0.43,0.28,0.17),
 (0,0.48,0.37,0.15),(0,0.46,0.43,0.2),(0,0.44,0.43,0.22),(0,0.3,0.45,0.33)])
W({"mediaId":7212,"level":"A","keyWord":"have breakfast","defaultVoice":"female",
 "taps":[{"phrase":"to have breakfast","target":"the woman","voice":"female","keys":wom},
         {"phrase":"to hold a fork","target":"the woman","voice":"female","keys":wom},
         {"phrase":"to look at the cup","target":"the black bird","voice":"female","keys":bird}],
 "stillS":2.7,
 "nouns":[{"word":"a bird","x":0.22,"y":0.57,"voice":"female"},{"word":"a cup","x":0.52,"y":0.37,"voice":"female"},
          {"word":"a plate","x":0.52,"y":0.72,"voice":"female"},{"word":"a hat","x":0.87,"y":0.25,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","having","breakfast","above","the","clouds."],"answerVoice":"female",
 "notes":"The woman's legs and boots run under/left of the bird; her box is cut at the bird's right edge, so her lower legs on the left are outside it. 'to have breakfast' has no object (key phrase, 3 words). Tiny birds fly in the background, hence target 'the black bird'; the 'a bird' pill sits on the raven."})

# 385
T=[i*0.5 for i in range(9)]
girl=K(T,[(0,0.03,1,0.97),(0,0.1,1,0.38),(0.08,0.12,0.73,0.88),(0,0.2,0.78,0.8),(0,0.18,0.9,0.82),
 (0,0.2,0.85,0.8),(0.02,0.35,0.68,0.65),(0.35,0.40,0.65,0.60),None])
ball=K(T,[None,(0.4,0.48,0.3,0.18),(0.82,0.07,0.18,0.15),(0.78,0,0.2,0.14),(0.73,0,0.2,0.14),
 (0.69,0.02,0.2,0.15),(0.66,0.06,0.2,0.14),(0.65,0.08,0.2,0.14),(0.66,0.09,0.2,0.14)])
W({"mediaId":385,"level":"A","keyWord":"hit","defaultVoice":"female",
 "taps":[{"phrase":"to hit the ball","target":"the girl","voice":"female","keys":girl},
         {"phrase":"to hold a bat","target":"the girl","voice":"female","keys":girl},
         {"phrase":"to fly through the air","target":"the ball","voice":"female","keys":ball}],
 "stillS":2.0,
 "nouns":[{"word":"a ball","x":0.80,"y":0.06,"voice":"female"},{"word":"a bat","x":0.16,"y":0.30,"voice":"female"},
          {"word":"a cap","x":0.42,"y":0.40,"voice":"female"}],
 "question":"What is the girl doing?",
 "answer":["She","is","hitting","the","ball","with","a","bat."],"answerVoice":"female",
 "notes":"At 0.5 s the ball is in front of the girl's body: ball box in the middle, girl box = head and shoulders above it. Ball is very small from 3.0 s (minimum-size box). Girl is out of frame at 4.0 s. Only 3 nouns: nothing else is sharp and apart."})

# 7773
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
wom=K(T,[(0.1,0.3,0.34,0.32),(0.07,0.3,0.34,0.32),(0.07,0.29,0.32,0.34),(0.07,0.29,0.35,0.36),
 (0.07,0.28,0.39,0.34),(0.07,0.28,0.36,0.36),(0.07,0.27,0.31,0.48),(0.07,0.27,0.33,0.5)])
bear=K(T,[(0.45,0.26,0.53,0.62),(0.41,0.25,0.57,0.65),(0.39,0.25,0.53,0.75),(0.42,0.26,0.56,0.74),
 (0.46,0.22,0.54,0.78),(0.43,0.2,0.57,0.8),(0.38,0.2,0.62,0.8),(0.40,0.19,0.60,0.81)])
W({"mediaId":7773,"level":"A","keyWord":"carefully","defaultVoice":"female",
 "taps":[{"phrase":"to carry the cups carefully","target":"the bear","voice":"female","keys":bear},
         {"phrase":"to sit at a table","target":"the woman","voice":"female","keys":wom},
         {"phrase":"to hold up her hands","target":"the woman","voice":"female","keys":wom}],
 "stillS":2.2,
 "nouns":[{"word":"cups","x":0.55,"y":0.38,"voice":"female"},{"word":"a woman","x":0.25,"y":0.50,"voice":"female"},
          {"word":"a table","x":0.25,"y":0.80,"voice":"female"},{"word":"a bear","x":0.78,"y":0.78,"voice":"female"}],
 "question":"What is the bear doing?",
 "answer":["It","is","carrying","cups","to","the","table."],"answerVoice":"female",
 "notes":"defaultVoice female = the only person (the woman); the bear is the main actor. The tower of cups stands between the two; it is put in the bear's box (the bear carries it), the woman's box ends at the cups, so at 3.2/3.7 s her far hand and the right edge of her face fall outside. 'carefully' is left out of the model answer because the adverb could stand in two places."})

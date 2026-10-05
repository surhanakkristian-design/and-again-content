import json
T10=[i*0.5 for i in range(21)]
def keys(times, d):
    out=[]
    for t in times:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def save(c): json.dump(c, open(f'content/{c["mediaId"]}.json','w'), indent=1, ensure_ascii=False)

# ---------- 145
man={0.0:(0.52,0.72,0.46,0.28),0.5:(0.27,0.45,0.48,0.54),1.0:(0.48,0.39,0.30,0.61),3.0:(0.42,0.38,0.46,0.62),
 3.5:(0.61,0.38,0.23,0.62),4.0:(0.61,0.41,0.35,0.42),4.5:(0.66,0.36,0.34,0.44),5.0:(0.48,0.69,0.29,0.31),
 5.5:(0.40,0.61,0.32,0.34),6.0:(0.33,0.44,0.34,0.44),6.5:(0.32,0.44,0.42,0.19),7.0:(0.30,0.28,0.48,0.11),
 7.5:(0.31,0.40,0.27,0.36),8.0:(0.38,0.34,0.48,0.23),8.5:(0.65,0.30,0.35,0.55),9.0:(0.55,0.28,0.37,0.19),
 9.5:(0.37,0.36,0.58,0.64),10.0:(0.50,0.29,0.29,0.61)}
woman={1.5:(0.05,0.63,0.57,0.37),2.0:(0.20,0.44,0.52,0.56),2.5:(0.02,0.39,0.55,0.61),4.0:(0.0,0.37,0.43,0.52),
 4.5:(0.21,0.39,0.42,0.51),5.0:(0.0,0.71,0.19,0.29),5.5:(0.0,0.62,0.18,0.28),6.5:(0.0,0.23,0.18,0.30),
 7.0:(0.0,0.17,0.18,0.30),7.5:(0.0,0.25,0.18,0.40),8.0:(0.0,0.24,0.25,0.46),8.5:(0.12,0.30,0.31,0.53),
 9.0:(0.17,0.31,0.37,0.68),9.5:(0.0,0.35,0.36,0.65),10.0:(0.0,0.34,0.30,0.50)}
ball={0.0:(0.38,0.09,0.24,0.16),0.5:(0.49,0.31,0.24,0.14),1.0:(0.30,0.40,0.18,0.15),1.5:(0.45,0.28,0.22,0.16),
 2.0:(0.46,0.30,0.20,0.14),2.5:(0.44,0.20,0.22,0.16),3.0:(0.41,0.23,0.20,0.14),3.5:(0.43,0.40,0.18,0.14),
 4.0:(0.43,0.50,0.18,0.14),4.5:(0.02,0.34,0.19,0.14),5.0:(0.36,0.02,0.18,0.14),6.0:(0.36,0.10,0.18,0.14),
 6.5:(0.44,0.63,0.18,0.14),7.0:(0.43,0.39,0.18,0.11),7.5:(0.58,0.44,0.18,0.14),8.0:(0.53,0.57,0.18,0.14),
 8.5:(0.47,0.49,0.18,0.14),9.0:(0.54,0.47,0.18,0.13),9.5:(0.72,0.22,0.20,0.14),10.0:(0.79,0.43,0.18,0.14)}
save({"mediaId":145,"level":"A","keyWord":"catching","defaultVoice":"male",
 "taps":[{"phrase":"to fall on the sand","target":"the man","voice":"male","keys":keys(T10,man)},
         {"phrase":"to wear a black swimsuit","target":"the woman","voice":"female","keys":keys(T10,woman)},
         {"phrase":"to fly through the air","target":"the ball","voice":"male","keys":keys(T10,ball)}],
 "stillS":10.0,
 "nouns":[{"word":"the sky","x":0.50,"y":0.15,"voice":"male"},{"word":"the sea","x":0.38,"y":0.50,"voice":"male"},
          {"word":"a ball","x":0.86,"y":0.50,"voice":"male"},{"word":"sand","x":0.50,"y":0.90,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","catching","the","ball."],"answerVoice":"male",
 "notes":"Clip has many cuts; man and ball overlap whenever he holds it, boxes split along one line (7.0 and 9.0: man box = head/shoulders only, ball in front of his chest). Both people throw and catch, so the woman's phrase is a state (swimsuit). The man catches several times (0.5, 3.5, 6.5)."})

# ---------- 146
cat={0.0:(0.32,0.40,0.62,0.31),0.5:(0.28,0.40,0.70,0.32),1.0:(0.34,0.41,0.62,0.30),1.5:(0.29,0.40,0.70,0.32),
 2.0:(0.32,0.40,0.64,0.29),2.5:(0.34,0.39,0.64,0.31),3.0:(0.30,0.39,0.70,0.31),3.5:(0.33,0.38,0.64,0.29),
 4.0:(0.24,0.38,0.72,0.30),4.5:(0.26,0.39,0.68,0.30),5.0:(0.32,0.38,0.63,0.31),5.5:(0.34,0.34,0.60,0.36),
 6.0:(0.40,0.33,0.54,0.38),6.5:(0.41,0.33,0.52,0.38),7.0:(0.39,0.34,0.53,0.39),7.5:(0.39,0.35,0.53,0.38),
 8.0:(0.32,0.39,0.59,0.33),8.5:(0.27,0.45,0.64,0.28),9.0:(0.26,0.45,0.65,0.28),9.5:(0.27,0.45,0.66,0.28),
 10.0:(0.28,0.43,0.65,0.28)}
coc={0.0:(0.02,0.0,0.36,0.21),0.5:(0.08,0.0,0.36,0.23),1.0:(0.13,0.0,0.36,0.24),1.5:(0.16,0.0,0.37,0.25),
 2.0:(0.20,0.0,0.36,0.26),2.5:(0.24,0.0,0.37,0.26),3.0:(0.27,0.0,0.37,0.26),3.5:(0.29,0.0,0.37,0.27),
 4.0:(0.29,0.0,0.37,0.28),4.5:(0.29,0.0,0.36,0.28),5.0:(0.31,0.0,0.36,0.30),5.5:(0.30,0.0,0.36,0.30),
 6.0:(0.30,0.0,0.35,0.31),6.5:(0.29,0.0,0.35,0.32),7.0:(0.32,0.02,0.31,0.30),7.5:(0.28,0.02,0.31,0.30),
 8.0:(0.27,0.02,0.36,0.32),8.5:(0.28,0.03,0.35,0.32),9.0:(0.28,0.03,0.35,0.33),9.5:(0.29,0.03,0.35,0.32),
 10.0:(0.29,0.02,0.35,0.32)}
but={7.0:(0.03,0.20,0.29,0.22),7.5:(0.59,0.13,0.26,0.21),8.0:(0.82,0.04,0.18,0.24)}
save({"mediaId":146,"level":"A","keyWord":"caterpillar","defaultVoice":"female",
 "taps":[{"phrase":"to walk on a leaf","target":"the caterpillar","voice":"female","keys":keys(T10,cat)},
         {"phrase":"to fly through the forest","target":"the butterfly","voice":"female","keys":keys(T10,but)},
         {"phrase":"to hang from a branch","target":"the cocoon","voice":"female","keys":keys(T10,coc)}],
 "stillS":7.5,
 "nouns":[{"word":"a branch","x":0.20,"y":0.11,"voice":"female"},{"word":"a butterfly","x":0.70,"y":0.24,"voice":"female"},
          {"word":"a caterpillar","x":0.66,"y":0.55,"voice":"female"},{"word":"a leaf","x":0.66,"y":0.78,"voice":"female"}],
 "question":"What is the caterpillar doing?",
 "answer":["The","caterpillar","is","walking","on","a","leaf."],"answerVoice":"female",
 "notes":"The butterfly is in the picture only at 7.0-8.0 s (off elsewhere). Target 3 is the green chrysalis, named 'the cocoon' for level A. The caterpillar moves little (it shifts along the leaf and lifts its front at 5.5-8.0); 'walk' used instead of 'crawl' for level A."})

# ---------- 147
red={0.0:(0.50,0.50,0.50,0.50),0.5:(0.50,0.52,0.47,0.48),1.0:(0.03,0.55,0.92,0.45),1.5:(0.0,0.52,0.80,0.48),
 2.0:(0.02,0.48,0.93,0.52),2.5:(0.10,0.49,0.68,0.51),3.0:(0.05,0.55,0.80,0.45),3.5:(0.08,0.56,0.64,0.44),
 4.0:(0.12,0.56,0.86,0.44),4.5:(0.15,0.57,0.62,0.43),5.0:(0.0,0.52,0.53,0.48),5.5:(0.02,0.55,0.50,0.45),
 6.0:(0.0,0.54,0.48,0.46),6.5:(0.0,0.55,0.46,0.45),7.0:(0.0,0.56,0.45,0.44),7.5:(0.0,0.58,0.46,0.42),
 8.0:(0.0,0.59,0.46,0.41),8.5:(0.0,0.61,0.45,0.39),9.0:(0.0,0.63,0.44,0.37),9.5:(0.0,0.63,0.44,0.37),
 10.0:(0.0,0.62,0.44,0.38)}
blue={0.0:(0.19,0.49,0.31,0.26),0.5:(0.21,0.50,0.29,0.24),
 3.5:(0.72,0.50,0.18,0.37),4.0:(0.52,0.46,0.28,0.10),4.5:(0.77,0.48,0.20,0.37),
 5.0:(0.53,0.47,0.38,0.53),5.5:(0.52,0.48,0.46,0.52),6.0:(0.50,0.50,0.50,0.50),6.5:(0.50,0.52,0.50,0.48),
 7.0:(0.50,0.53,0.50,0.47),7.5:(0.50,0.55,0.50,0.45),8.0:(0.50,0.56,0.50,0.44),8.5:(0.50,0.58,0.50,0.42),
 9.0:(0.50,0.62,0.50,0.38),9.5:(0.50,0.62,0.50,0.38),10.0:(0.50,0.61,0.50,0.39)}
save({"mediaId":147,"level":"A","keyWord":"cave","defaultVoice":"male",
 "taps":[{"phrase":"to walk in front","target":"the person in blue","voice":"male","keys":keys(T10,blue)},
         {"phrase":"to wear a yellow helmet","target":"the person in red","voice":"male","keys":keys(T10,red)},
         {"phrase":"to wear a blue jacket","target":"the person in blue","voice":"male","keys":keys(T10,blue)}],
 "stillS":0.0,
 "nouns":[{"word":"leaves","x":0.72,"y":0.14,"voice":"male"},{"word":"a cave","x":0.50,"y":0.37,"voice":"male"},
          {"word":"a rock","x":0.15,"y":0.62,"voice":"male"}],
 "question":"Where are the two people going?",
 "answer":["They","are","walking","into","a","dark","cave."],"answerVoice":"male",
 "notes":"Both hikers are seen from behind most of the time; gender not certain (red: ponytail, blue: probably a man), so targets are 'the person in ...' and the voice is the default (male, odd id). From 1.0 to 4.5 s the person in blue is mostly hidden behind the one in red: blue is off at 1.0-3.0 and its box at 3.5-4.5 covers only the visible part (helmet top or one arm). 'to walk in front' holds for 0-5 s; afterwards they stand side by side. Only 3 nouns: helmets, backpacks and jackets come in pairs."})

# ---------- 148
T5=[i*0.5 for i in range(11)]
boy={0.0:(0.0,0.33,0.35,0.45),0.5:(0.0,0.33,0.34,0.44),1.0:(0.0,0.32,0.32,0.56),1.5:(0.0,0.32,0.31,0.56),
 2.0:(0.0,0.31,0.29,0.48),2.5:(0.0,0.30,0.28,0.49),3.0:(0.0,0.30,0.31,0.60),3.5:(0.0,0.30,0.35,0.52),
 4.0:(0.0,0.30,0.40,0.50),4.5:(0.0,0.30,0.40,0.50),5.0:(0.0,0.30,0.40,0.50)}
mid={0.0:(0.35,0.26,0.30,0.37),0.5:(0.34,0.26,0.29,0.40),1.0:(0.33,0.26,0.34,0.46),1.5:(0.33,0.27,0.36,0.46),
 2.0:(0.29,0.30,0.41,0.40),2.5:(0.28,0.30,0.44,0.40),3.0:(0.31,0.34,0.39,0.46),3.5:(0.35,0.25,0.29,0.48),
 4.0:(0.40,0.24,0.18,0.30),4.5:(0.40,0.24,0.18,0.30),5.0:(0.40,0.24,0.18,0.30)}
pink={0.0:(0.65,0.34,0.35,0.44),0.5:(0.63,0.34,0.37,0.44),1.0:(0.68,0.34,0.32,0.54),1.5:(0.70,0.33,0.30,0.55),
 2.0:(0.70,0.32,0.30,0.47),2.5:(0.72,0.32,0.28,0.47),3.0:(0.72,0.33,0.28,0.57),3.5:(0.65,0.32,0.35,0.58),
 4.0:(0.58,0.32,0.42,0.48),4.5:(0.58,0.31,0.42,0.50),5.0:(0.58,0.34,0.42,0.46)}
save({"mediaId":148,"level":"A","keyWord":"celebrate","defaultVoice":"female",
 "taps":[{"phrase":"to blow out the candles","target":"the girl in the middle","voice":"female","keys":keys(T5,mid)},
         {"phrase":"to bring the cake","target":"the girl with pink hair","voice":"female","keys":keys(T5,pink)},
         {"phrase":"to wear a shirt","target":"the boy","voice":"male","keys":keys(T5,boy)}],
 "stillS":1.5,
 "nouns":[{"word":"lamps","x":0.55,"y":0.17,"voice":"female"},{"word":"a boy","x":0.14,"y":0.46,"voice":"male"},
          {"word":"a cake","x":0.50,"y":0.73,"voice":"female"},{"word":"a table","x":0.40,"y":0.87,"voice":"female"}],
 "question":"What are the three friends doing?",
 "answer":["They","are","celebrating","a","birthday","with","a","cake."],"answerVoice":"female",
 "notes":"Boy's phrase is a state: his only own action is firing the confetti popper (3.0-3.5 s), no level-A wording for it; clapping is done by the pink-haired girl too. She wears a white T-shirt under overalls, he is the only one in a shirt. Paper lanterns named 'lamps' for level A. From 4.0 s the three hug: boxes split by the faces, the middle girl's box is narrow (face only)."})

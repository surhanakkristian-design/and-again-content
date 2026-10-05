import json
T=[i*0.5 for i in range(21)]
def keys(boxes):
    out=[]
    for t,b in zip(T,boxes):
        if b is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":b[0],"y":b[1],"w":round(b[2],2),"h":round(b[3],2)})
    assert len(out)==21
    return out
def split(rows, wy, my_):
    # rows: (split, wtop, mtop) -> left box, right box
    L=[];R=[]
    for s,a,b in rows:
        L.append((0,a,s,round(1-a,2))); R.append((s,b,round(1-s,2),round(1-b,2)))
    return L,R
def write(i,d):
    json.dump(d,open(f"content/{i}.json","w"),indent=1,ensure_ascii=False)

# ---------- 180
w=[(0,0,0.85,0.9),(0,0,0.85,0.9),(0,0,0.87,0.95),(0,0,1,0.95),(0,0,1,0.75),(0,0,1,0.5),(0,0,1,0.9),(0,0,1,0.62),
   (0,0,1,0.68),(0,0,1,0.76),(0.02,0,0.96,0.92),(0.05,0.07,0.82,0.87),(0.1,0.12,0.78,0.72),(0.08,0,0.82,0.83),
   (0.16,0.16,0.7,0.76),(0.2,0.14,0.66,0.78),(0.18,0.12,0.68,0.69),(0.18,0.1,0.64,0.7),(0.16,0.11,0.63,0.8),
   (0.14,0.08,0.7,0.84),(0.11,0.07,0.73,0.76)]
k=keys(w)
write(180,{"mediaId":180,"level":"A","keyWord":"cold","defaultVoice":"female",
 "taps":[{"phrase":p,"target":"the woman","voice":"female","keys":k} for p in
   ["to make a hole","to pull up her scarf","to cross her arms"]],
 "stillS":8.5,
 "nouns":[{"word":"a hat","x":0.5,"y":0.21,"voice":"female"},{"word":"a scarf","x":0.5,"y":0.35,"voice":"female"},
          {"word":"boots","x":0.5,"y":0.69,"voice":"female"},{"word":"a hole","x":0.5,"y":0.84,"voice":"female"}],
 "question":"How does the woman feel?",
 "answer":["She","feels","very","cold","on","the","ice."],"answerVoice":"female",
 "notes":"Only one target (the woman); all three phrases share her keys. Hole drilling 0-1.5 s, scarf pulled up 6.5-7.5 s, arms crossed 8-10 s. 2-4.5 s are close shots of her hands/boots: the box covers the visible parts of her. Question is about a state (key word 'cold' is an adjective), so present simple."})

# ---------- 181
rows=[(0.76,0.18,0.2),(0.76,0.18,0.2),(0.74,0.17,0.2),(0.72,0.17,0.2),(0.72,0.17,0.2),(0.72,0.17,0.2),(0.69,0.17,0.2),
      (0.66,0.17,0.19),(0.63,0.17,0.18),(0.58,0.17,0.19),(0.52,0.2,0.2),(0.67,0.18,0.2),(0.68,0.17,0.2),(0.66,0.14,0.17),
      (0.66,0.17,0.2),(0.6,0.18,0.2),(0.5,0.16,0.16),(0.47,0.17,0.16),(0.5,0.18,0.2),(0.55,0.2,0.2),(0.54,0.18,0.18)]
L,R=split(rows,0,0)
kw=keys(L);kb=keys(R)
write(181,{"mediaId":181,"level":"A","keyWord":"collar","defaultVoice":"male",
 "taps":[{"phrase":"to pull his collar up","target":"the man in white","voice":"male","keys":kw},
         {"phrase":"to open his mouth wide","target":"the blond man","voice":"male","keys":kb},
         {"phrase":"to point at the collar","target":"the blond man","voice":"male","keys":kb}],
 "stillS":3.5,
 "nouns":[{"word":"a cat","x":0.13,"y":0.41,"voice":"male"},{"word":"a collar","x":0.47,"y":0.49,"voice":"male"},
          {"word":"a shirt","x":0.45,"y":0.75,"voice":"male"}],
 "question":"What is the man in white doing?",
 "answer":["He","is","holding","his","collar","with","both","hands."],"answerVoice":"male",
 "notes":"The two men stand close and overlap; boxes are split by a vertical line between the heads, so the white sleeve sometimes reaches into the blond man's box. Blond man: mouth wide open 4.5-7.5 s, points at the collar 8-9 s. Answer avoids 'pulling his collar up' because 'pulling up his collar' would be a second word order. A second cat lies bottom left in the first seconds; the noun slot is on the cat on the dresser (at 3.5 s only that one is visible)."})

# ---------- 182
D=[(0.36,0,0.64,1.0),(0.08,0.36,0.92,0.64),(0.5,0,0.5,1.0),(0.56,0,0.44,1.0),(0.56,0.42,0.44,0.58),(0.56,0.42,0.44,0.58),
   (0,0.18,1.0,0.82),(0,0.2,1.0,0.8),(0.24,0.2,0.56,0.8),(0.2,0.28,0.52,0.72),(0.2,0.27,0.4,0.73),(0.18,0.38,0.38,0.62),
   (0.2,0.28,0.34,0.72),(0.18,0.26,0.34,0.74),(0,0.29,0.53,0.71),(0,0.28,0.54,0.72),(0,0.14,0.33,0.86),(0,0.3,0.54,0.7),
   (0,0.16,0.27,0.84),(0,0.16,0.36,0.84),(0,0.14,0.33,0.86)]
S=[(0.10,0,0.26,0.76),(0.25,0.06,0.3,0.29),(0.18,0.15,0.3,0.42),(0.16,0.14,0.36,0.52),(0.14,0.12,0.38,0.42),(0.12,0.12,0.4,0.4),
   None,None,(0.02,0.3,0.22,0.5),(0,0.3,0.2,0.52),(0,0.27,0.2,0.45),(0,0.24,0.32,0.14),
   (0,0.22,0.2,0.3),(0,0.2,0.18,0.3),(0,0.15,0.22,0.14),(0.03,0.14,0.3,0.14),(0.33,0.2,0.18,0.3),(0.2,0.14,0.2,0.16),
   (0.27,0.18,0.25,0.4),(0.36,0.18,0.18,0.4),(0.33,0.18,0.2,0.44)]
M=[None,None,None,None,(0.78,0.16,0.22,0.26),(0.78,0.17,0.22,0.25),None,None,(0.8,0.46,0.2,0.22),(0.72,0.37,0.28,0.36),
   (0.6,0.34,0.4,0.48),(0.56,0.3,0.44,0.5),(0.54,0.26,0.44,0.4),(0.52,0.25,0.46,0.4),(0.53,0.25,0.45,0.4),(0.54,0.25,0.46,0.38),
   (0.52,0.24,0.46,0.4),(0.54,0.24,0.46,0.4),(0.53,0.24,0.45,0.4),(0.55,0.24,0.45,0.4),(0.55,0.22,0.45,0.42)]
write(182,{"mediaId":182,"level":"A","keyWord":"comb","defaultVoice":"male",
 "taps":[{"phrase":"to comb his hair","target":"the dark-haired man","voice":"male","keys":keys(D)},
         {"phrase":"to wear an orange scarf","target":"the man in the scarf","voice":"male","keys":keys(S)},
         {"phrase":"to hang on the wall","target":"the mirror","voice":"male","keys":keys(M)}],
 "stillS":8.0,
 "nouns":[{"word":"hair","x":0.14,"y":0.28,"voice":"male"},{"word":"a mirror","x":0.74,"y":0.42,"voice":"male"},
          {"word":"a comb","x":0.42,"y":0.6,"voice":"male"},{"word":"a shirt","x":0.16,"y":0.76,"voice":"male"}],
 "question":"What is the dark-haired man doing?",
 "answer":["He","is","combing","his","hair","with","an","orange","comb."],"answerVoice":"male",
 "notes":"Hand-held clip, the camera moves a lot and the three targets overlap; boxes are split where they touch. The man in the scarf: a state phrase, because his only action (hands together at 9-10 s) is short and unclear; he is hidden at 3-3.5 s and only a strip of his scarf shows at 7-8.5 s (small boxes). The mirror: off until 1.5 s and at 3-3.5 s (only a blurred sliver at the edge), boxed from 4 s on; at 2-2.5 s a blurred mirror is at the right edge. At 0.5-2.5 s the dark-haired man's box leaves out his hand with the comb where it covers the other man. The orange thing in the mirror at 8 s is the comb's reflection; the noun slot is on the real comb."})

# ---------- 183
rows=[(0.5,0.33,0.04),(0.54,0.33,0),(0.5,0.34,0),(0.53,0.33,0.23),(0.53,0.27,0.19),(0.55,0.26,0.15),(0.5,0.3,0.13),
      (0.53,0.28,0.13),(0.57,0.26,0.13),(0.57,0.25,0.13),(0.55,0.28,0.13),(0.57,0.3,0.11),(0.54,0.23,0.13),(0.58,0.25,0.13),
      (0.53,0.27,0.14),(0.57,0.28,0.15),(0.52,0.22,0.13),(0.57,0.25,0.14),(0.52,0.28,0.15),(0.57,0.3,0.16),(0.52,0.26,0.17)]
L,R=split(rows,0,0)
kw=keys(L);km=keys(R)
write(183,{"mediaId":183,"level":"B","keyWord":"comfort","defaultVoice":"male",
 "taps":[{"phrase":"to sob into her sleeve","target":"the woman","voice":"female","keys":kw},
         {"phrase":"to comfort a crying friend","target":"the man","voice":"male","keys":km},
         {"phrase":"to wipe away her tears","target":"the woman","voice":"female","keys":kw}],
 "stillS":4.0,
 "nouns":[{"word":"a potted plant","x":0.22,"y":0.24,"voice":"male"},{"word":"freckles","x":0.7,"y":0.37,"voice":"male"},
          {"word":"a tissue","x":0.42,"y":0.53,"voice":"male"},{"word":"keys","x":0.67,"y":0.84,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","comforting","his","crying","friend."],"answerVoice":"male",
 "notes":"Animated clip. The friend who comforts is drawn as a man (the description does not say). The two sit pressed together: boxes split by a vertical line between the heads, so his hand on her shoulder lies in her box and part of his hair can cross the line. Sobbing into the sleeve 0-2.5 s; wiping tears with the tissue 4 s, with her hands 7-7.5 s. defaultVoice male: mixed pair, evenId false. Fairy lights and mugs not used as nouns (several places)."})

import json
T=[i*0.5 for i in range(25)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
man={t:(.05,.52,.75,.16) for t in T[:6]}
man.update({5.0:(.48,.28,.24,.36),5.5:(.46,.61,.38,.22),6.0:(.45,.69,.43,.22),6.5:(.45,.69,.46,.22),7.0:(.43,.66,.47,.28),7.5:(.50,.56,.38,.39),
8.0:(.49,.56,.34,.33),8.5:(.50,.53,.38,.30),9.0:(.50,.44,.39,.40),9.5:(.50,.34,.40,.55),10.0:(.52,.31,.40,.50),10.5:(.55,.31,.41,.48),
11.0:(.53,.30,.37,.60),11.5:(.55,.29,.38,.60),12.0:(.55,.28,.35,.50)})
spr={3.0:(.27,.18,.30,.60),3.5:(.27,.15,.30,.63),4.0:(.26,.08,.32,.68),4.5:(.27,.10,.30,.60),5.0:(.26,.08,.22,.60),5.5:(.27,.08,.30,.53),
6.0:(.27,.06,.30,.63),6.5:(.27,.06,.30,.63),7.0:(.27,.06,.30,.60),7.5:(.27,.06,.23,.63),8.0:(.27,.06,.22,.63),8.5:(.27,.06,.23,.63),
9.0:(.27,.06,.23,.63),9.5:(.27,.06,.23,.63),10.0:(.27,.06,.25,.63),10.5:(.27,.06,.28,.63),11.0:(.27,.06,.26,.63),11.5:(.27,.06,.28,.63),12.0:(.27,.06,.28,.63)}
cur={t:((0,.23,.20,.29) if t<3 else (0,.23,.20,.36)) for t in T}
c={"mediaId":4100,"level":"A","keyWord":"hole","defaultVoice":"male",
"taps":[{"phrase":"to lie on the bed","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to make a big hole","target":"the spring","voice":"male","keys":keys(spr)},
{"phrase":"to hang at the window","target":"the curtain","voice":"male","keys":keys(cur)}],
"stillS":12.0,
"nouns":[{"word":"a hole","x":.33,"y":.09,"voice":"male"},{"word":"a spring","x":.42,"y":.30,"voice":"male"},
{"word":"a man","x":.72,"y":.45,"voice":"male"},{"word":"a curtain","x":.12,"y":.42,"voice":"male"}],
"question":"What is there in the ceiling?",
"answer":["There","is","a","big","hole","in","the","ceiling."],"answerVoice":"male",
"notes":"'spring' (the giant coil) and 'ceiling' are above A1 but are the things shown; no simpler true word. The man is not in the picture 3.0-4.5 s (off; the bed vanishes when the spring comes down) and is a blur at 5.0 s. Man and spring boxes are split where he lands next to it. Curtain box is shortened at the bottom 0-2.5 s to stay clear of the man's feet. A second hole (in the floor) is visible only 3.0-4.0 s; the noun slot is on the ceiling hole."}
json.dump(c,open('content/4100.json','w'),indent=1)

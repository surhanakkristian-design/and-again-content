import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":round(w,2),"h":round(h,2)})
        else: out.append({"t":t,"off":True})
    return out
woman={0.0:(0,0,.82,.92),0.5:(0,0,.63,.83),1.0:(0,0,.52,.58),1.5:(0,.10,.62,.44),2.0:(0,.18,.22,.46),2.5:(0,0,.30,.68),
3.0:(0,0,.40,.80),3.5:(0,0,.62,.56),4.0:(0,0,.62,.52),4.5:(0,0,.62,.52),5.0:(0,0,.60,.54),5.5:(0,0,.48,.46),
6.0:(0,0,.52,.40),6.5:(0,0,.40,.40),7.0:(0,0,.32,.78),7.5:(0,.03,.46,.39),8.0:(0,.09,.50,.35),8.5:(0,.09,.51,.35),
9.0:(0,.12,.51,.35),9.5:(0,.14,.51,.33),10.0:(0,.14,.51,.33)}
man={2.0:(.72,0,.28,.40),2.5:(.68,0,.32,.42),3.0:(.66,0,.34,.60),3.5:(.66,0,.34,.55),4.0:(.66,0,.34,.55),4.5:(.66,0,.34,.55),
5.0:(.66,0,.34,.62),6.5:(.64,.22,.36,.18),7.0:(.56,.03,.44,.38),7.5:(.54,.03,.46,.39),8.0:(.53,.05,.47,.39),
8.5:(.53,.06,.47,.38),9.0:(.53,.09,.47,.38),9.5:(.53,.10,.47,.37),10.0:(.53,.11,.47,.36)}
red={5.5:(.26,.46,.64,.42),6.0:(.30,.40,.46,.32),6.5:(.33,.40,.45,.28),7.0:(.33,.42,.40,.26),7.5:(.30,.43,.42,.24),
8.0:(.30,.45,.40,.22),8.5:(.31,.45,.38,.22),9.0:(.32,.48,.36,.20),9.5:(.32,.48,.36,.20),10.0:(.32,.48,.36,.20)}
c={"mediaId":489,"level":"A","keyWord":"mushroom","defaultVoice":"female",
"taps":[
{"phrase":"to point at a mushroom","target":"the woman","voice":"female","keys":keys(woman)},
{"phrase":"to hold a basket","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to have white spots","target":"the red mushroom","voice":"female","keys":keys(red)}],
"stillS":8.5,
"nouns":[{"word":"a hat","x":.15,"y":.20,"voice":"female"},{"word":"a mushroom","x":.50,"y":.50,"voice":"female"},
{"word":"a basket","x":.78,"y":.67,"voice":"female"},{"word":"leaves","x":.40,"y":.87,"voice":"female"}],
"question":"What is the woman pointing at?",
"answer":["She","is","pointing","at","a","mushroom."],
"answerVoice":"female",
"notes":"Cut at 5.5 s (brown mushrooms before, red mushroom after). Woman is only an arm/hand/boot at 0-2.5 s; man is only jacket + basket at 2.0-2.5 s and off at 5.5-6.0 s. From 6.0 s the woman's and man's boxes hold only the upper body so they do not overlap the red mushroom's box. 'to have white spots' is a state: the brown mushrooms carry water drops, not spots. A squirrel appears at 9.0-9.5 s only (too short for a target). Man holds the basket clearly from 8.0 s."}
json.dump(c,open("content/489.json","w"),indent=1,ensure_ascii=False)

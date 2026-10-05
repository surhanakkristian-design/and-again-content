import json
def keys(rows):
    out=[]
    for r in rows:
        if r[1] is None: out.append({"t":r[0],"off":True})
        else: out.append({"t":r[0],"x":r[1],"y":r[2],"w":r[3],"h":r[4]})
    return out
T=[i/2 for i in range(25)]
def fill(d): return [(t,)+d[t] if t in d else (t,None) for t in T]
man=fill({0.0:(.35,.05,.65,.65),0.5:(.22,.05,.76,.65),1.0:(.14,.02,.80,.68),1.5:(.19,.02,.78,.68),2.0:(.18,0,.80,.70),
 2.5:(.17,.05,.73,.65),3.0:(.20,.05,.66,.62),3.5:(.12,.04,.73,.63),4.0:(.10,.03,.70,.64),4.5:(.18,.01,.77,.68),
 5.0:(.27,.02,.68,.69),5.5:(.33,.15,.67,.55),6.0:(.55,.13,.45,.50),6.5:(.60,.12,.40,.55),7.0:(.45,.10,.53,.55),
 7.5:(.46,.08,.54,.58),8.0:(.02,.08,.80,.78),8.5:(0,.05,.96,.95),9.0:(0,.05,1.0,.95),9.5:(0,.06,.97,.94),
 10.0:(0,.05,.97,.95),10.5:(0,.13,.97,.87),11.0:(.30,.22,.55,.78),11.5:(.30,.25,.50,.75),12.0:(.26,.28,.42,.68)})
fl=fill({6.0:(0,0,.55,.82),6.5:(.08,.05,.52,.80),7.0:(0,0,.45,.82),7.5:(0,.05,.46,.80)})
blk=fill({4.5:(0,.22,.18,.38),5.0:(0,.22,.20,.38),5.5:(0,.23,.20,.38),11.0:(.10,.35,.20,.38),11.5:(.10,.32,.20,.40),12.0:(.08,.32,.18,.40)})
d={"mediaId":5312,"level":"B","keyWord":"backyard","defaultVoice":"male",
"taps":[{"phrase":"to grill a coiled sausage","target":"the man in green","voice":"male","keys":keys(man)},
{"phrase":"to leap above the skewers","target":"the flames","voice":"male","keys":keys(fl)},
{"phrase":"to sip from a can","target":"the man in the black T-shirt","voice":"male","keys":keys(blk)}],
"stillS":5.0,
"nouns":[{"word":"a cool box","x":0.27,"y":0.52,"voice":"male"},{"word":"tongs","x":0.58,"y":0.60,"voice":"male"},
{"word":"skewers","x":0.22,"y":0.80,"voice":"male"},{"word":"a sausage","x":0.72,"y":0.74,"voice":"male"}],
"question":"What is the man in green doing?","answer":["He","is","grilling","a","coiled","sausage."],"answerVoice":"male",
"notes":"Key word 'backyard' is the whole setting, not placeable, so not a noun. Flames 6.0-7.5 cover the left of the frame and overlap the man in green: split at his left edge (flames box left, man box right). The bearded man in the black T-shirt drinks from a can 4.5-5.5 (left edge) and raises it 11.0-12.0; off 6.0-10.5 (hidden by flames or behind the main man). The man in the white T-shirt also holds a can but is not seen drinking - verifier may check 4.5-5.5. At 12.0 the black-T-shirt box is split from the main man at x 0.26."}
json.dump(d,open("content/5312.json","w"),indent=1)

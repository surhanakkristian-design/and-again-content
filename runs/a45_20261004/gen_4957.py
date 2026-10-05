import json
T=[i*0.5 for i in range(19)]
def K(d):
    out=[]
    for t in T:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else:
            x,y,x2,y2=b; out.append({"t":t,"x":round(x,2),"y":round(y,2),"w":round(x2-x,2),"h":round(y2-y,2)})
    return out
Y={0.0:(.26,.48,.68,.82),0.5:(.22,.45,.74,1.0),1.0:(.0,.37,.77,1.0),1.5:(.06,.28,1.0,1.0),2.0:(.0,.19,1.0,1.0),2.5:(.0,.15,1.0,1.0)}
W={3.0:(.19,.30,.64,.99),3.5:(.18,.29,.74,1.0),4.0:(.04,.22,.82,1.0),4.5:(.03,.22,.78,1.0),5.0:(.18,.22,.90,1.0)}
O={5.5:(.15,.35,.44,.99),6.0:(.09,.33,.43,.93),6.5:(.08,.28,.42,1.0),7.0:(.02,.28,.46,1.0),7.5:(.06,.27,.53,1.0),
8.0:(.07,.29,.63,1.0),8.5:(.12,.29,.65,1.0),9.0:(.08,.29,.66,1.0)}
c={"mediaId":4957,"level":"A","keyWord":"hotel","defaultVoice":"male",
"taps":[
 {"phrase":"to carry a big backpack","target":"the backpacker","voice":"male","keys":K(Y)},
 {"phrase":"to pull a suitcase","target":"the woman","voice":"female","keys":K(W)},
 {"phrase":"to walk with a stick","target":"the old man","voice":"male","keys":K(O)}],
"stillS":6.0,
"nouns":[{"word":"a hotel","x":0.40,"y":0.18,"voice":"male"},
 {"word":"a fountain","x":0.46,"y":0.48,"voice":"male"},
 {"word":"a stick","x":0.37,"y":0.78,"voice":"male"},
 {"word":"a carpet","x":0.70,"y":0.90,"voice":"male"}],
"question":"What is the old man doing?",
"answer":["He","is","walking","with","a","stick."],
"answerVoice":"male",
"notes":"Three-shot montage, one target per shot (backpacker 0-2.5 s, woman 3.0-5.0 s, old man 5.5-9.0 s). defaultVoice male: no single main person, evenId false. Doorman / bellboy not used as targets. Price captions (30/150/2,000 EUR) ignored."}
json.dump(c,open("content/4957.json","w"),indent=1)

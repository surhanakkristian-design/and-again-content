import json
T=[i*0.5 for i in range(15)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
man={0.0:(0,.44,1,.56),0.5:(0,.44,1,.56),1.0:(0,.44,1,.56),1.5:(0,.42,1,.58),2.0:(0,.43,1,.57),2.5:(0,.37,1,.63),
3.0:(0,.44,1,.56),3.5:(0,.45,1,.55),4.0:(0,.55,1,.45),4.5:(0,.68,1,.32),5.0:(0,.68,1,.32),5.5:(0,.68,1,.32),
6.0:(0,.42,1,.58),6.5:(0,.33,1,.67),7.0:(0,.34,1,.66)}
bird={3.5:(.10,.04,.30,.20),4.0:(.25,.35,.31,.19),4.5:(.31,.52,.28,.15),5.0:(.31,.52,.28,.15),5.5:(.33,.49,.30,.18)}
c={"mediaId":301,"level":"A","keyWord":"float","defaultVoice":"male",
"taps":[
{"phrase":"to float on the lake","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to give a thumbs up","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to sit on the man","target":"the bird","voice":"male","keys":keys(bird)}],
"stillS":3.5,
"nouns":[{"word":"a bird","x":.26,"y":.14,"voice":"male"},{"word":"a man","x":.62,"y":.70,"voice":"male"},{"word":"a lake","x":.50,"y":.38,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","floating","on","the","lake."],
"answerVoice":"male",
"notes":"While the bird sits on the man's chest (4.5-5.5 s) the two overlap in the picture: the man's box is cut to the body below the bird (y from 0.68), so his head is outside the man box in those frames; at 4.0 s the man box starts at 0.55 under the flying bird. The bird is visible only 3.5-5.5 s (not on the sampled frames after 6.0 s)."}
json.dump(c,open("content/301.json","w"),indent=1,ensure_ascii=False)

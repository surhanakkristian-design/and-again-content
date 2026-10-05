import json
T=[round(i*0.5,1) for i in range(21)]
def keys(d):
    return [dict(t=t,**dict(zip('xywh',d[t]))) if t in d else {'t':t,'off':True} for t in T]
man={2.0:(.18,0,.68,.56),2.5:(.15,0,.72,.5),3.0:(.22,0,.68,.57)}
steam={3.5:(0,.28,.5,.72),4.0:(0,.18,.46,.82),4.5:(0,0,.48,.98)}
old={5.0:(.14,.03,.82,.68),5.5:(.14,.03,.82,.68),6.0:(.1,0,.86,.62)}
c={"mediaId":4846,"level":"B","keyWord":"iron","defaultVoice":"female",
"taps":[
 {"phrase":"to press a pair of trousers","target":"the man","voice":"male","keys":keys(man)},
 {"phrase":"to steam a silk dress","target":"the woman with the steamer","voice":"female","keys":keys(steam)},
 {"phrase":"to iron a stack of napkins","target":"the older woman","voice":"female","keys":keys(old)}],
"stillS":2.0,
"nouns":[{"word":"a bedside lamp","x":0.22,"y":0.27,"voice":"female"},
 {"word":"a framed picture","x":0.78,"y":0.10,"voice":"female"},
 {"word":"an iron","x":0.55,"y":0.47,"voice":"female"},
 {"word":"trousers","x":0.45,"y":0.78,"voice":"female"}],
"question":"What is the man doing?",
"answer":["He","is","pressing","a","pair","of","trousers."],
"answerVoice":"male",
"notes":"Five shots, mostly women; evenId true -> defaultVoice female. The kitchen woman (0-1.5 s) and the two women with the sheet (6.5-10 s) are not targets. The steamer shot (3.5-4.5 s) is a garment steamer, not an iron, so 'to steam' fits only that woman; the dress looks silky (satin) - verifier may prefer 'a satin dress'. 'iron' also used as a noun on the still (key word is a verb)."}
json.dump(c,open('content/4846.json','w'),indent=1)

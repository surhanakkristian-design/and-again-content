import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows):
    out=[]
    for t,r in zip(T,rows):
        if r is None: out.append({"t":t,"off":True})
        else:
            x,y,x2,y2=r; out.append({"t":t,"x":round(x,2),"y":round(y,2),"w":round(x2-x,2),"h":round(y2-y,2)})
    return out
woman=K([(.42,.13,.88,.87),(.44,.09,.95,.89),(.50,.06,.98,.94),(.40,.02,1,.99),(.31,0,1,.99),(.34,0,1,.99),(.38,0,1,1),(.45,0,1,1)])
man=K([(0,.18,.27,.53),(0,.15,.32,.52),(0,.13,.32,.51),(0,.11,.35,.49),(0,.07,.30,.48),(0,.05,.33,.43),(0,.02,.36,.45),(0,.01,.40,.42)])
c={"mediaId":7123,"level":"B","keyWord":"flesh","defaultVoice":"female",
"taps":[{"phrase":"to open a whole salmon","target":"the woman","voice":"female","keys":woman},
{"phrase":"to smooth the flesh flat","target":"the woman","voice":"female","keys":woman},
{"phrase":"to lean on the counter","target":"the man","voice":"male","keys":man}],
"stillS":3.2,
"nouns":[{"word":"a knife","x":.58,"y":.38,"voice":"female"},{"word":"a rubber glove","x":.30,"y":.51,"voice":"female"},
{"word":"flesh","x":.50,"y":.64,"voice":"female"},{"word":"a fish head","x":.25,"y":.82,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","smoothing","the","bright","orange","flesh."],"answerVoice":"female",
"notes":"Only two people are clear targets; woman used for two phrases. Woman box includes her reaching arm, so it is wide from 1.7 s."}
json.dump(c,open('content/7123.json','w'),indent=1)

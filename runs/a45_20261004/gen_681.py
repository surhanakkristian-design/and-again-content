import json
def keys(d):
    out=[]
    for t in sorted(d):
        b=d[t]
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2],2),"h":round(b[3],2)})
    return out
M={0.0:(0,.27,.29,.58),0.5:(0,.26,.29,.58),1.0:(0,.27,.29,.58),1.5:(0,.27,.29,.58),2.0:(0,.27,.29,.58),2.5:(0,.28,.34,.58),
3.0:(0,.30,.35,.58),3.5:(0,.28,.53,.58),4.0:(0,.27,.46,.59),4.5:(0,.25,.37,.60),5.0:(0,.27,.37,.59),5.5:(0,.28,.36,.58),
6.0:(0,.28,.37,.58),6.5:(0,.28,.35,.58),7.0:(0,.30,.35,.58),7.5:(0,.30,.34,.58),8.0:(0,.30,.35,.58),8.5:(0,.42,.34,.44),
9.0:(0,.56,.32,.34),9.5:(0,.56,.35,.34),10.0:(0,.31,.29,.55)}
R={0.0:(.30,.40,.26,.12),0.5:(.30,.40,.27,.12),1.0:(.30,.41,.26,.12),1.5:(.30,.41,.27,.12),2.0:(.30,.40,.26,.12),2.5:(.35,.40,.24,.12),
3.0:(.36,.40,.24,.12),3.5:(.54,.40,.18,.12),4.0:(.47,.40,.20,.12),4.5:(.38,.40,.26,.12),5.0:(.38,.41,.24,.12),5.5:(.37,.41,.24,.12),
6.0:(.38,.41,.24,.12),6.5:(.36,.41,.26,.12),7.0:(.36,.41,.25,.12),7.5:(.35,.41,.26,.12),8.0:(.36,.41,.26,.12),8.5:(.35,.40,.27,.12),
9.0:(.20,.41,.38,.12),9.5:(.22,.41,.38,.12),10.0:(.30,.40,.28,.12)}
W={0.0:(.57,.33,.43,.55),0.5:(.58,.32,.42,.55),1.0:(.57,.34,.43,.56),1.5:(.58,.34,.42,.56),2.0:(.57,.34,.43,.55),2.5:(.60,.34,.40,.55),
3.0:(.61,.35,.39,.55),3.5:(.73,.35,.27,.55),4.0:(.70,.34,.30,.54),4.5:(.66,.33,.34,.55),5.0:(.64,.34,.36,.55),5.5:(.64,.34,.36,.55),
6.0:(.64,.33,.36,.56),6.5:(.64,.33,.36,.56),7.0:(.63,.35,.37,.55),7.5:(.63,.35,.37,.55),8.0:(.63,.34,.37,.55),8.5:(.63,.34,.37,.55),
9.0:(.62,.34,.38,.56),9.5:(.63,.34,.37,.56),10.0:(.60,.33,.40,.55)}
c={"mediaId":681,"level":"A","keyWord":"singing","defaultVoice":"male",
"taps":[
{"phrase":"to look at the camera","target":"the man","voice":"male","keys":keys(M)},
{"phrase":"to drive the car","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to be long and straight","target":"the road","voice":"male","keys":keys(R)}],
"stillS":10.0,
"nouns":[{"word":"a mirror","x":.50,"y":.38,"voice":"male"},{"word":"a road","x":.40,"y":.48,"voice":"male"},
{"word":"a man","x":.18,"y":.66,"voice":"male"},{"word":"a woman","x":.82,"y":.64,"voice":"female"}],
"question":"What are they doing?",
"answer":["They","are","singing","in","the","car."],
"answerVoice":"male",
"notes":"Seen from the back seat: the man (beard, left) turns round and looks into the camera at 2.5-3.5 s; the woman holds the wheel all the time. Third target is the road seen through the windscreen (a state phrase: the road does nothing; 'to go through the desert' would also fit the car). The road box is small and is cut on the left where the man's raised arm and fist are in front of the windscreen (3.5-8.5 s), so the man's box does not hold his hand on the gear stick at 0.0-2.0 s. At 9.0-9.5 s only the man's shoulder and arm are in the picture. Singing is seen only from the wide open mouths (key word); default voice male because the pair is mixed and the id is odd. 'a mirror' and 'a road' pills are 0.10 apart in y."}
json.dump(c,open('content/681.json','w'),indent=1,ensure_ascii=False)

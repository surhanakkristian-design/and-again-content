import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def keys(bs): return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)} for t,b in zip(T,bs)]
goose=[(.04,.56,.49,.78),(.10,.57,.50,.79),(.09,.57,.52,.80),(.12,.56,.55,.80),(.16,.56,.58,.81),(.18,.57,.68,.82),(.26,.62,.60,.83),(.31,.58,.64,.84)]
man=[(.49,.35,.64,.70),(.50,.35,.69,.70),(.52,.34,.75,.73),(.55,.33,.87,.75),(.62,.32,.92,.78),(.68,.31,1.0,.80),(.79,.30,1.0,.80),None]
woman=[(.64,.35,1.0,.75),(.71,.35,1.0,.77),(.82,.35,1.0,.77),(.87,.35,1.0,.72),(.92,.36,1.0,.58),None,(.44,.35,.79,.62),(.06,.34,.31,.76)]
c={"mediaId":8001,"level":"B","keyWord":"stay away","defaultVoice":"female",
"taps":[
{"phrase":"to spread its wings","target":"the goose","voice":"female","keys":keys(goose)},
{"phrase":"to cycle past the goose","target":"the man on the bicycle","voice":"male","keys":keys(man)},
{"phrase":"to leap onto the grass","target":"the woman in shorts","voice":"female","keys":keys(woman)}],
"stillS":2.2,
"nouns":[{"word":"a goose","x":0.38,"y":0.70,"voice":"female"},{"word":"a bicycle","x":0.74,"y":0.64,"voice":"female"},{"word":"ivy","x":0.62,"y":0.27,"voice":"female"},{"word":"a gravel path","x":0.45,"y":0.90,"voice":"female"}],
"question":"What is the woman in shorts doing?",
"answer":["She","is","staying","away","from","the","goose."],
"answerVoice":"female",
"notes":"Woman in shorts is only a sliver at the right edge at 1.7 and 2.2 (narrow box) and hidden behind the cyclist at 2.7 (off). Goose and cyclist / woman overlap in the picture at 0.7 and 3.2-3.7: boxes split between them. Cyclist is out of frame at 3.7 (only a wheel). A second, tiny bicycle stands far back at the left edge."}
json.dump(c,open('content/8001.json','w'),indent=1)

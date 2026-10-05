import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
W={0.0:(.08,.19,.44,.23),0.5:(.21,.27,.29,.41),1.0:(.21,.22,.38,.42),1.5:(.18,.22,.33,.42),2.0:(.31,.20,.41,.50),2.5:(.19,0,.64,.63),
3.0:(.03,0,.94,.58),3.5:(0,0,1,.97),4.0:(0,0,1,.65),4.5:(0,0,1,.65),5.0:(0,0,1,.52),5.5:(0,0,1,.62),6.0:(0,0,1,.45),6.5:(0,0,.90,.62),
7.0:(0,0,.84,.70),7.5:(0,0,.86,.75),8.0:(.18,.05,.50,.63),8.5:(.20,.14,.46,.52),9.0:(.20,.19,.42,.60),9.5:(.20,.17,.30,.58),10.0:(0,.14,.47,.26)}
M={0.0:(.55,.17,.45,.50),0.5:(.52,.27,.48,.43),1.0:(.60,.37,.40,.30),1.5:(.52,.38,.48,.26),
8.0:(.69,.15,.31,.53),8.5:(.67,.20,.33,.48),9.0:(.63,.27,.37,.54),9.5:(.58,.25,.42,.60),10.0:(.48,.14,.52,.58)}
F={0.0:(0,.42,.31,.31),0.5:(0,.40,.20,.36),1.0:(0,.37,.20,.36),1.5:(0,.36,.18,.34),2.0:(0,.36,.30,.40),2.5:(0,.22,.18,.55),
8.0:(0,.28,.18,.60),8.5:(0,.32,.20,.48),9.0:(0,.38,.20,.56),9.5:(0,.40,.20,.52),10.0:(0,.40,.18,.44)}
c={"mediaId":525,"level":"B","keyWord":"paperclip","defaultVoice":"female",
"taps":[
{"phrase":"to clip the pages together","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to wear rectangular glasses","target":"the man","voice":"male","keys":keys(M)},
{"phrase":"to blow the sheets away","target":"the fan","voice":"female","keys":keys(F)}],
"stillS":10.0,
"nouns":[{"word":"a paperclip","x":.36,"y":.67,"voice":"female"},{"word":"a glass dish","x":.32,"y":.81,"voice":"female"},
{"word":"a desk fan","x":.13,"y":.52,"voice":"female"},{"word":"a hanging plant","x":.55,"y":.10,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","fastening","the","pages","with","a","paperclip."],
"answerVoice":"female",
"notes":"The man's phrase is a state (glasses): every action he does (reaching for the sheets, the high five) the woman does too. The fan stands in front of the woman in the wide shots, so her box is cut along the fan's edge (0.0 and 10.0: only her upper part above the fan; 9.5: without the back of her head). Fan off at 3.0-7.5 (only a sliver at 3.0, then out of frame); man off at 2.0-7.5 (only a dark sliver or a faceless torso at the right edge). The paperclip pill at 10.0 sits on the clip on top of the paper stack."}
json.dump(c,open("content/525.json","w"),indent=1)

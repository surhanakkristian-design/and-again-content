import json
T=[i*0.5 for i in range(13)]
def keys(rows):
    out=[]
    for t,r in zip(T,rows):
        out.append({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]})
    return out
W=[(.10,.22,.48,.76),(.10,.22,.48,.76),(.14,.24,.44,.76),(.22,.24,.38,.76),(.22,0,.42,.98),(.22,0,.42,.98),(.22,0,.42,.98),(.22,0,.42,.98),(.22,.02,.41,.96),(.05,.15,.45,.85),(.02,.30,.52,.70),(.02,.30,.57,.70),(.02,.18,.57,.82)]
M=[(.59,.19,.41,.68),(.59,.19,.41,.68),(.59,.20,.41,.75),(.61,.19,.39,.78),(.65,.15,.35,.72),(.65,.15,.35,.72),(.65,.52,.35,.46),(.65,.52,.35,.48),(.64,.28,.36,.64),(.51,.30,.49,.70),(.55,.33,.45,.67),(.60,.33,.40,.67),(.60,.29,.40,.71)]
d={"mediaId":584,"level":"B","keyWord":"prove","defaultVoice":"female",
"taps":[
 {"phrase":"to perform a handstand","target":"the woman","voice":"female","keys":keys(W)},
 {"phrase":"to prove him wrong","target":"the woman","voice":"female","keys":keys(W)},
 {"phrase":"to gasp in amazement","target":"the man","voice":"male","keys":keys(M)}],
"stillS":2.5,
"nouns":[{"word":"bare feet","x":.50,"y":.08,"voice":"female"},{"word":"leggings","x":.50,"y":.40,"voice":"female"},{"word":"a bench","x":.20,"y":.64,"voice":"female"},{"word":"a knitted vest","x":.82,"y":.72,"voice":"female"}],
"question":"What is the young woman doing?",
"answer":["She","is","performing","a","handstand","to","prove","him","wrong."],
"answerVoice":"female",
"notes":"'to prove him wrong' is read from the story (he doubts with crossed arms, she does the handstand, he gasps and applauds). Boxes split along x~0.6 where the two stand close; at 1.5 s her right hand crosses into the man's box."}
json.dump(d,open("content/584.json","w"),indent=1)

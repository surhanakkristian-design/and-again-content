import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":round(w,2),"h":round(h,2)})
        else: out.append({"t":t,"off":True})
    return out
boy={0.0:(0,.22,.78,.78),0.5:(0,.25,.79,.75),1.0:(0,.24,.78,.76),1.5:(.13,.24,.69,.76),2.0:(.13,.21,.65,.79),
2.5:(0,.20,.42,.80),3.0:(0,.21,.27,.79),3.5:(0,.22,.27,.78),4.0:(0,.22,.31,.78),4.5:(0,.23,.30,.77),
5.0:(0,.27,.39,.37),9.0:(0,.34,.18,.66),9.5:(.36,.36,.40,.64),10.0:(.26,.42,.42,.58)}
woman={2.5:(.42,.27,.58,.73),3.0:(.27,.26,.45,.74),3.5:(.27,.26,.55,.74),4.0:(.31,.26,.51,.74),4.5:(.30,.27,.52,.73),
5.0:(0,.64,.22,.36),9.0:(.18,.30,.62,.70),9.5:(.76,.50,.24,.50),10.0:(.68,.40,.32,.60)}
man={0.0:(.78,.50,.22,.50),0.5:(.79,.52,.21,.48),1.0:(.78,.52,.22,.48),1.5:(.82,.62,.18,.38),2.0:(.78,.36,.22,.60),
3.0:(.72,.28,.28,.72),3.5:(.82,.45,.18,.55),4.0:(.82,.40,.18,.60),4.5:(.82,.42,.18,.58),
5.0:(.39,.24,.61,.76),5.5:(.10,.22,.90,.78),6.0:(0,.22,1.0,.78),6.5:(0,.21,1.0,.79),7.0:(0,.23,1.0,.77),
7.5:(0,.19,1.0,.81),8.0:(0,.18,1.0,.82),8.5:(0,.17,1.0,.83),9.5:(0,.22,.34,.65),10.0:(0,.12,.18,.66)}
c={"mediaId":488,"level":"A","keyWord":"muscle","defaultVoice":"male",
"taps":[
{"phrase":"to have red hair","target":"the boy","voice":"male","keys":keys(boy)},
{"phrase":"to clap her hands","target":"the woman","voice":"female","keys":keys(woman)},
{"phrase":"to wear a black top","target":"the man in black","voice":"male","keys":keys(man)}],
"stillS":8.0,
"nouns":[{"word":"a muscle","x":.12,"y":.46,"voice":"male"},{"word":"a beard","x":.52,"y":.40,"voice":"male"},{"word":"weights","x":.84,"y":.80,"voice":"male"}],
"question":"What is the man in black doing?",
"answer":["He","is","showing","his","big","muscles."],
"answerVoice":"male",
"notes":"All three people flex, so no flexing phrase is unique; two phrases are states. The woman claps only at 9.0-10.0 s (blurry at 9.0). The man in black is half out of frame at 0-2 s and 3.5-4.5 s (right edge, no head) and his reflection (back view, black top) shows in the mirror at 2.5-4.5 s without a box. At 9.5-10 s the man in the black top has dark hair (AI inconsistency), other men in grey tops laugh and point. Arms of the woman at 3.0-4.5 s cross the boy's and man's boxes; boxes are split vertically. At 5.0 s boy/woman split horizontally at y .64."}
json.dump(c,open("content/488.json","w"),indent=1,ensure_ascii=False)

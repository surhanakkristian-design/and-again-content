import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)})
    return out
G={1.5:(.35,.27,.88,1),2.0:(.23,.30,.90,1),2.5:(.03,.27,1,1),3.0:(.24,.15,1,1),3.5:(.12,.10,.92,.95),4.0:(.06,.10,.94,.93),
   4.5:(.08,.08,.94,.93),5.0:(.06,.10,.94,.93),5.5:(.07,.10,.95,.95),6.0:(.05,.37,.47,.83),6.5:(.07,.37,.46,.83),
   7.0:(.04,.37,.47,.93),7.5:(.08,.37,.62,.93),8.0:(.33,.43,.78,.83),8.5:(.33,.36,.77,.87),9.0:(.40,.27,.60,.83),
   9.5:(.24,.16,.67,.74),10.0:(.22,.14,.68,.77)}
O={0.0:(.25,.33,.90,.72),0.5:(.10,.36,.88,.76),6.0:(.52,.36,1,.83),6.5:(.50,.34,1,.82),7.0:(.47,.34,1,.90),7.5:(.63,.55,1,.80)}
Wm={1.0:(.42,.18,.92,1),1.5:(.17,.19,.35,.68),2.0:(.13,.16,.31,.30),2.5:(.10,.11,.30,.27),3.0:(.02,.08,.24,.30),
    8.5:(.30,.22,.48,.36),9.0:(.60,.31,.83,.88),9.5:(.67,.44,1,1),10.0:(.68,.44,1,1)}
c={"mediaId":112,"level":"A","keyWord":"brave","defaultVoice":"female",
 "taps":[{"phrase":"to open its wings","target":"the goose","voice":"female","keys":keys(O)},
         {"phrase":"to walk to the goose","target":"the girl","voice":"female","keys":keys(G)},
         {"phrase":"to hold the man","target":"the woman","voice":"female","keys":keys(Wm)}],
 "stillS":7.0,
 "nouns":[{"word":"a goose","x":.72,"y":.58,"voice":"female"},{"word":"a girl","x":.20,"y":.55,"voice":"female"},
          {"word":"a tree","x":.30,"y":.20,"voice":"female"},{"word":"a basket","x":.86,"y":.76,"voice":"female"}],
 "question":"What is the girl doing?","answer":["She","is","walking","to","the","goose."],"answerVoice":"female",
 "notes":"Cartoon with many cuts. 'to hold the man': the woman carries the man in her arms at 1.0 s; at 1.5-3.0 s the two cling to each other behind the fence (small, top left) - weakest phrase. Woman boxes at 1.5-3.0 and 8.5 s are small and include part of the man (he is not a target); they are cut against the girl's box, so the girl's box loses a strip of hair/hand there. Girl walks to the goose at 6.0-7.5 s. Key word brave is an adjective, not placed as a noun. Basket at 7.0 s is cut by the right edge."}
json.dump(c,open("content/112.json","w"),indent=1)

import json
T=[i*0.5 for i in range(31)]
def K(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
M={0.0:(.20,.32,.34,.21),0.5:(.20,.33,.34,.21),1.0:(.19,.34,.35,.20),1.5:(.19,.34,.35,.20),2.0:(.10,.33,.44,.23),
2.5:(.07,.32,.47,.24),3.0:(.07,.34,.48,.25),3.5:(.04,.34,.50,.26),4.0:(.12,.32,.41,.26),4.5:(.14,.32,.42,.26),
5.0:(.14,.33,.40,.25),5.5:(.12,.31,.41,.25),6.0:(.07,.30,.44,.29),6.5:(.02,.30,.46,.31),7.0:(0,.30,.40,.30),
7.5:(0,.30,.45,.30),8.0:(0,.25,.44,.35),8.5:(0,.17,.38,.42),9.0:(0,.17,.26,.42),9.5:(0,.30,.13,.29),
10.0:(0,.10,.18,.55),10.5:(0,.04,.28,.70),11.0:(0,.05,.35,.70),11.5:(.03,.05,.40,.74),12.0:(.18,.04,.42,.78),
12.5:(.43,.04,.44,.80),13.0:(.68,0,.32,.86),13.5:(.82,.08,.18,.76),14.0:(.82,.08,.18,.68),14.5:(.82,.03,.18,.76)}
W={0.0:(.55,.32,.30,.21),0.5:(.55,.33,.30,.21),1.0:(.55,.35,.30,.19),1.5:(.55,.35,.30,.19),2.0:(.56,.33,.31,.24),
2.5:(.55,.32,.35,.26),3.0:(.56,.34,.34,.25),3.5:(.55,.34,.36,.26),4.0:(.54,.33,.37,.26),4.5:(.57,.32,.39,.27),
5.0:(.55,.32,.41,.27),5.5:(.54,.31,.44,.27),6.0:(.52,.30,.46,.27),6.5:(.49,.30,.44,.29),7.0:(.41,.32,.49,.26),
7.5:(.46,.32,.50,.27),8.0:(.45,.34,.52,.26),8.5:(.39,.33,.61,.27),9.0:(.27,.34,.58,.34),9.5:(.14,.37,.66,.34),
10.0:(.22,.40,.70,.30),10.5:(.36,.44,.64,.26),11.0:(.37,.47,.63,.20),11.5:(.44,.46,.56,.20),12.0:(.61,.45,.32,.18),
12.5:(.17,.43,.25,.20),13.0:(.17,.40,.50,.26),13.5:(.34,.35,.46,.30),14.0:(.40,.33,.35,.34),14.5:(.38,.31,.36,.38),
15.0:(.29,.30,.40,.43)}
d={"mediaId":4039,"level":"B","keyWord":"crawl","defaultVoice":"male",
"taps":[{"phrase":"to get to his feet","target":"the man","voice":"male","keys":K(M)},
{"phrase":"to collapse onto her stomach","target":"the woman","voice":"female","keys":K(W)},
{"phrase":"to clutch her knees","target":"the woman","voice":"female","keys":K(W)}],
"stillS":14.5,
"nouns":[{"word":"a pillar","x":.22,"y":.14,"voice":"male"},{"word":"treadmills","x":.66,"y":.24,"voice":"male"},
{"word":"leggings","x":.56,"y":.52,"voice":"male"},{"word":"a resistance band","x":.24,"y":.61,"voice":"male"}],
"question":"What are the two people doing?",
"answer":["They","are","crawling","along","a","running","track."],"answerVoice":"male",
"notes":"Both crawl, so the key word is in the question only, not in a tap phrase. Only two targets (the red band joins both, its box would overlap them), so two phrases share the woman. 'to collapse onto her stomach': in fact the band drags her down (8.0-9.0 s). 'to clutch her knees': she sits holding her knees at 14.0-15.0 s. Side by side from 4.0 s the two touch: boxes split between them, a hand or shoe is cut in places. 9.5 s: the man is nearly out of frame (one leg and shoe at the left edge), his box is narrow and her outstretched hand is cut. 12.0 s: the man walks in front of her, her box covers only her legs; 12.5 s his left shoe is cut. 15.0 s: only a sliver of the man's shoe -> off. defaultVoice: a man and a woman, no single main person -> evenId false -> male."}
json.dump(d,open("content/4039.json","w"),indent=1)

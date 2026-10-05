import json
times=[i*0.5 for i in range(24)]
D={0.0:(.15,.0,.85,.65),0.5:(.15,.0,.85,.66),1.0:(.15,.02,.85,.68),1.5:(.15,.02,.85,.72),2.0:(.15,.0,.85,.74),2.5:(.15,.0,.85,.75),
4.5:(.25,.0,.37,.72),5.0:(.22,.0,.40,.78),5.5:(.15,.21,.85,.63),6.0:(.07,.16,.72,.36),6.5:(.38,.11,.47,.57),7.0:(.55,.13,.45,.62),
7.5:(.26,.30,.38,.60),8.0:(.28,.34,.46,.64),8.5:(.30,.38,.40,.59),9.0:(.30,.36,.38,.60),9.5:(.15,.40,.56,.44),
10.0:(.26,.44,.40,.18),10.5:(.37,.36,.23,.26),11.0:(.40,.38,.18,.20),11.5:(.40,.40,.18,.18)}
C={3.0:(.03,.28,.86,.52),3.5:(.0,.28,1.0,.58),4.0:(.0,.24,1.0,.56),4.5:(.62,.0,.38,.60),5.0:(.62,.0,.38,.78),
6.0:(.66,.52,.34,.14),6.5:(.05,.26,.33,.22),7.0:(.30,.34,.25,.14),7.5:(.0,.05,1.0,.25),8.0:(.08,.0,.75,.34),8.5:(.20,.14,.65,.24),
9.0:(.20,.14,.62,.22),9.5:(.30,.20,.50,.20),10.0:(.44,.30,.34,.14),10.5:(.60,.36,.18,.26),11.0:(.58,.38,.18,.20),11.5:(.58,.40,.18,.18)}
F={0.0:(.0,.0,.15,.50),0.5:(.0,.0,.15,.50),1.0:(.0,.0,.15,.50),1.5:(.0,.0,.15,.50),2.0:(.0,.0,.15,.50),2.5:(.0,.0,.15,.50),
4.5:(.0,.0,.25,.33),5.0:(.0,.05,.22,.67),5.5:(.05,.0,.50,.20),6.0:(.03,.0,.50,.16),6.5:(.03,.0,.35,.25),7.0:(.03,.0,.47,.33),
7.5:(.06,.30,.20,.32),8.0:(.06,.34,.22,.40),8.5:(.06,.38,.24,.34),9.0:(.12,.0,.48,.14),9.5:(.15,.0,.50,.20),
10.0:(.26,.0,.38,.30),10.5:(.30,.0,.36,.36),11.0:(.35,.0,.30,.38),11.5:(.36,.0,.28,.40)}
def keys(m):
    out=[]
    for t in times:
        if t in m:
            x,y,w,h=m[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
c={"mediaId":4226,"level":"B","keyWord":"hunt","defaultVoice":"female",
"taps":[{"phrase":"to crouch by the river","target":"the dinosaur","voice":"female","keys":keys(D)},
{"phrase":"to cling to the dinosaur","target":"the first crocodile","voice":"female","keys":keys(C)},
{"phrase":"to plunge down the cliff","target":"the waterfall","voice":"female","keys":keys(F)}],
"stillS":9.0,
"nouns":[{"word":"a dinosaur","x":.47,"y":.63,"voice":"female"},{"word":"a crocodile","x":.60,"y":.28,"voice":"female"},
{"word":"a waterfall","x":.32,"y":.07,"voice":"female"},{"word":"foam","x":.50,"y":.88,"voice":"female"}],
"question":"What are the crocodiles hunting?",
"answer":["The","crocodiles","are","hunting","a","huge","dinosaur."],
"answerVoice":"female",
"notes":"Hard clip for boxes: dinosaur, crocodile and waterfall overlap in almost every shot, so all boxes are split and partial. The waterfall is mostly behind the dinosaur; its box is only the clearly free part (left strip 0-2.5 s, 0.15 wide; top band or left column later; full column in the wide shots 10-11.5 s). The crocodile is the one that attacks (alone under water 3.0-4.0 s, then on the dinosaur); at 5.5 s it cannot be made out in the dinosaur's mouth (off); at 6.5-9.0 s its box is the head / upper body, the hanging tail falls into the dinosaur's box or outside; in the wide shots 10.5-11.5 s dinosaur and crocodile are tiny and split on a vertical line. More crocodiles swim in at 10.0-11.5 s, hence target name 'the first crocodile' and the plural question. Phrase 1 is true for 0-2.5 s only (later the dinosaur rears up)."}
json.dump(c,open("content/4226.json","w"),indent=1,ensure_ascii=False)

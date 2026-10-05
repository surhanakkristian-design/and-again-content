import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else:
            x0,y0,x1,y1=b
            out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
W={0:(.18,.50,.78,1),.5:(.08,.52,.82,1),1:(.05,.50,.95,1),1.5:(0,.50,.88,1),2:(0,.50,.58,1),2.5:(0,.55,.56,1),
3:(.10,.60,.56,1),3.5:(.15,.70,.58,1),4:(.15,.74,.55,1),4.5:(.15,.75,.55,1),5:(.24,.74,.64,1),5.5:(.25,.72,.62,1),
6:(.28,.70,.60,1),6.5:(.28,.67,.61,1),7:(.22,.66,.59,1),7.5:(.20,.65,.56,1),8:(.22,.64,.47,1),8.5:(.30,.64,.49,1),
9:(.21,.64,.47,1),9.5:(.13,.64,.47,1),10:(.06,.64,.44,1)}
M={0:(.50,.36,.72,.50),.5:(.54,.38,.76,.52),1:(.56,.36,.82,.50),1.5:(.56,.36,.80,.50),2:(.59,.44,.82,.68),2.5:(.57,.50,.90,.74),
3:(.56,.55,1,1),3.5:(.64,.63,1,1),4:(.64,.66,1,1),4.5:(.66,.68,1,1),5:(.70,.67,1,1),5.5:(.64,.66,1,1),
6:(.60,.65,1,1),6.5:(.62,.62,.95,1),7:(.59,.61,.88,1),7.5:(.56,.61,.88,1),8:(.47,.61,.80,1),8.5:(.49,.61,.70,1),
9:(.47,.61,.77,1),9.5:(.47,.61,.88,1),10:(.44,.60,.90,1)}
S={1.5:(.15,.12,.52,.42),2:(.20,.10,.58,.47),2.5:(.28,.15,.76,.50),3:(.30,.22,.62,.55),3.5:(.36,.30,.63,.68),
4:(.36,.28,.63,.72),4.5:(.38,.26,.65,.73),5:(.36,.32,.68,.72),5.5:(.36,.32,.63,.70),6:(.35,.20,.72,.64),
6.5:(.38,.18,.82,.61),7:(.38,.22,.72,.60),7.5:(.38,.20,.75,.60),8:(.30,.20,.80,.60),8.5:(.35,.20,.85,.60),
9:(.35,.20,.85,.60),9.5:(.35,.20,.88,.60),10:(.35,.20,.90,.59)}
c={"mediaId":310,"level":"A","keyWord":"forest","defaultVoice":"female",
"taps":[
{"phrase":"to touch a big tree","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to wear a grey jacket","target":"the man","voice":"male","keys":keys(M)},
{"phrase":"to shine through the trees","target":"the sun","voice":"female","keys":keys(S)}],
"stillS":0.0,
"nouns":[{"word":"the sky","x":.70,"y":.12,"voice":"female"},{"word":"trees","x":.78,"y":.40,"voice":"female"},
{"word":"grass","x":.80,"y":.58,"voice":"female"},{"word":"a woman","x":.50,"y":.78,"voice":"female"}],
"question":"Where are they walking?",
"answer":["They","are","walking","in","a","forest."],
"answerVoice":"female",
"notes":"0-1.5 s the man is half hidden behind the woman: his box is only head/shoulders above hers (split by a horizontal line). The man has no action of his own (both walk, look up, spread arms), so a state phrase. The sun = the burst of sunbeams between the trunks (disc visible from 8.5 s); off before 1.5 s. 'forest' is not a noun slot (the whole picture), it is in the answer. 'trees' = the group of firs on the right at 0.0 s; the big trunk on the left is also a tree."}
json.dump(c,open("content/310.json","w"),indent=1,ensure_ascii=False)

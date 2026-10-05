import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)})
    return out
woman={0.0:(0,.42,.4,1),0.5:(0,.42,.4,1),1.0:(0,.44,.4,1),1.5:(0,.44,.4,1),2.0:(0,.43,.38,1),2.5:(0,.42,.38,1),
3.0:(0,.45,.42,1),3.5:(0,.46,.42,1),4.0:(0,.46,.42,1),4.5:(0,.46,.42,1),5.0:(0,.46,.42,1),5.5:(0,.46,.42,1),
6.0:(0,.5,.44,1),6.5:(0,.55,.5,1),7.0:(0,.6,.5,1),7.5:(0,.58,.5,1),8.0:(0,.53,.53,1),8.5:(0,.53,.5,1),
9.0:(0,.54,.48,1),9.5:(0,.54,.48,1),10.0:(0,.5,.47,1)}
man={0.0:(.69,.4,1,1),0.5:(.69,.4,1,1),1.0:(.62,.42,1,1),1.5:(.62,.42,1,1),2.0:(.58,.42,1,1),2.5:(.58,.41,1,1),
3.0:(.6,.41,1,1),3.5:(.6,.41,1,1),4.0:(.6,.42,1,1),4.5:(.6,.42,1,1),5.0:(.6,.42,1,1),5.5:(.6,.42,1,1),
6.0:(.58,.43,1,1),6.5:(.52,.47,1,1),7.0:(.5,.48,1,1),7.5:(.5,.45,1,1),8.0:(.55,.42,1,1),8.5:(.5,.41,1,1),
9.0:(.48,.4,1,1),9.5:(.48,.4,1,1),10.0:(.47,.38,1,1)}
li={0.0:(.5,.4,.69,.55),0.5:(.5,.4,.69,.55),1.0:(.42,.42,.62,.56),1.5:(.42,.42,.62,.56),2.0:(.44,.2,.68,.42),2.5:(.44,.2,.68,.41),
3.0:(.44,.22,.68,.41),3.5:(.44,.22,.68,.41),4.0:(.44,.22,.7,.42),4.5:(.44,.22,.7,.42),5.0:(.3,.18,.68,.42),5.5:(.36,.2,.68,.42),
6.0:(.44,.22,.68,.43),6.5:(.4,.22,.66,.44),7.0:(.4,.22,.66,.44),7.5:(.4,.2,.66,.43),8.0:(.4,.2,.66,.42),8.5:(.4,.2,.64,.41),
9.0:(.38,.2,.64,.4),9.5:(.38,.18,.64,.4),10.0:(.38,.17,.64,.38)}
c={"mediaId":444,"level":"A","keyWord":"lightning","defaultVoice":"female",
"taps":[
{"phrase":"to hide her face","target":"the woman","voice":"female","keys":keys(woman)},
{"phrase":"to wear a grey T-shirt","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to light up the sky","target":"the lightning","voice":"female","keys":keys(li)}],
"stillS":2.0,
"nouns":[{"word":"lightning","x":.54,"y":.31,"voice":"female"},{"word":"clouds","x":.25,"y":.40,"voice":"female"},
{"word":"a tree","x":.80,"y":.17,"voice":"female"},{"word":"glasses","x":.47,"y":.73,"voice":"female"}],
"question":"What are they looking at?",
"answer":["They","are","looking","at","the","lightning."],
"answerVoice":"female",
"notes":"Both people point at the sky (3.0-5.5 s), so pointing is not used. The woman hides her face in her hand while laughing from about 7.0 s to the end. Lightning box = the big bolt in the middle of the sky (0-1.5 s only a small flash at the horizon beside the man's head, box split from the man at x 0.62-0.69; at 5.0-5.5 s the whole cloud lights up, no bolt). Small second flashes at the horizon are not boxed from 2.0 s. Man/lightning are split by a horizontal line at y ~0.41. 'a tree' is the big palm on the right; dark palms also stand at the left edge. A third glass stands on the small table at the bottom, apart from the two on the rail."}
json.dump(c,open("content/444.json","w"),indent=1,ensure_ascii=False)

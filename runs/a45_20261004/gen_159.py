import json
T=[i*0.5 for i in range(19)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
cook={0.0:(.03,.06,.97,.66),0.5:(.05,.07,.92,.50),1.0:(0,0,.72,.68),1.5:(0,0,.53,.45),2.0:(0,.30,.68,.70),2.5:(0,.60,1,.40),
3.0:(.38,.64,.62,.36),3.5:(.84,.26,.16,.74),4.0:(.83,.22,.17,.58),4.5:(.72,0,.28,.30),5.0:(.78,.08,.22,.36)}
red={2.5:(.55,.47,.22,.13),3.0:(.12,.50,.26,.45),3.5:(0,.40,.42,.56),4.0:(0,.34,.42,.64),6.0:(0,.12,1,.76),6.5:(0,.30,.48,.44),
7.0:(0,.34,.50,.40),7.5:(0,.33,.49,.40),8.0:(0,.24,.50,.46),8.5:(0,.18,.51,.48),9.0:(0,.18,.52,.42)}
man={3.0:(.58,.48,.16,.16),3.5:(.64,.38,.20,.30),4.0:(.64,.35,.19,.35),6.5:(.51,.31,.49,.42),7.0:(.55,.31,.45,.42),7.5:(.54,.31,.46,.42),
8.0:(.50,.24,.50,.46),8.5:(.51,.13,.49,.50),9.0:(.52,.14,.48,.46)}
c={"mediaId":159,"level":"A","keyWord":"chicken","defaultVoice":"female",
"taps":[
 {"phrase":"to carry the chicken","target":"the woman in white","voice":"female","keys":keys(cook)},
 {"phrase":"to wear a blue jacket","target":"the woman with red hair","voice":"female","keys":keys(red)},
 {"phrase":"to wear a green T-shirt","target":"the man","voice":"male","keys":keys(man)}],
"stillS":4.0,
"nouns":[{"word":"a chicken","x":.55,"y":.68,"voice":"female"},{"word":"a table","x":.28,"y":.88,"voice":"female"},
 {"word":"a jacket","x":.14,"y":.60,"voice":"female"},{"word":"leaves","x":.25,"y":.10,"voice":"female"}],
"question":"What is the woman in white carrying?",
"answer":["She","is","carrying","a","chicken","to","the","table."],
"answerVoice":"female",
"notes":"PACKET DESCRIPTION DOES NOT MATCH THE CLIP: the frames show a cartoon of a bald woman in a white shirt grilling a whole roast chicken, carrying it on a board to a table where a red-haired woman and a man sit, cutting it, and the two eating chicken legs. Content is written from the frames. The two guests do the same actions (eat, thumbs up), so their phrases are states (clothes). Cook's box: at 3.0 only her back/torso (her head and raised arm sit next to the man / red-haired woman), at 3.5-4.0 cut at x .84 next to the man, at 4.5-5.0 only her hand with the knife. Red-haired woman at 2.5 is small in the background."}
json.dump(c,open("content/159.json","w"),indent=1)

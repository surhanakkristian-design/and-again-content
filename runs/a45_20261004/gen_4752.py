import json
OFF=None
def keys(times, d):
    out=[]
    for t in times:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
times=[i*0.5 for i in range(21)]
man={1.0:(.15,.10,.85,.90),1.5:(0,.10,1,.90),2.0:(0,.10,1,.90),2.5:(.08,.15,.92,.85),
3.0:(.48,.08,.52,.56),3.5:(.58,.02,.42,.62),4.0:(.48,.06,.52,.60),4.5:(.74,.16,.26,.60),
5.0:(.28,.06,.72,.94),5.5:(.38,.08,.62,.86),6.0:(.66,0,.34,.82),6.5:(.38,0,.62,1.0),
7.0:(.18,0,.82,.88),7.5:(.38,.05,.62,.88),8.0:(.03,.10,.97,.90),8.5:(.05,.14,.95,.86),
9.0:(.03,.17,.97,.83),9.5:(0,.12,1,.85),10.0:(0,.07,1,.90)}
toaster={0.0:(0,.45,1,.55),0.5:(0,.42,1,.58),3.0:(.08,.46,.30,.16),4.0:(.05,.47,.30,.16),4.5:(0,.46,.28,.17)}
pan={3.0:(.02,.64,.96,.34),3.5:(.03,.64,.97,.34),4.0:(0,.66,1,.30),4.5:(0,.64,.74,.32)}
c={"mediaId":4752,"level":"B","keyWord":"failure","defaultVoice":"male",
"taps":[
{"phrase":"to grimace in disappointment","target":"the man","voice":"male","keys":keys(times,man)},
{"phrase":"to pop up burnt toast","target":"the toaster","voice":"male","keys":keys(times,toaster)},
{"phrase":"to sit on the hob","target":"the frying pan","voice":"male","keys":keys(times,pan)}],
"stillS":3.0,
"nouns":[{"word":"a toaster","x":.24,"y":.53,"voice":"male"},{"word":"an apron","x":.72,"y":.47,"voice":"male"},
{"word":"a spatula","x":.76,"y":.70,"voice":"male"},{"word":"a frying pan","x":.27,"y":.83,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","grimacing","at","his","burnt","biscuits."],
"answerVoice":"male",
"notes":"Key word 'failure' is abstract, so it is not a noun slot and not in the answer. Toaster: boxed in the opening close-up (0.0-0.5) and where it stands small in the background (3.0, 4.0, 4.5); marked off at 1.0/1.5 (only a sliver at the bottom edge, under the man's box), 3.5 (behind smoke) and 7.0 (unclear appliance at the left edge). Frying pan and man are split along y~0.64-0.66 in 3.0-4.5; the man's spatula arm reaches slightly below that line at 3.0."}
json.dump(c,open("content/4752.json","w"),indent=1,ensure_ascii=False)

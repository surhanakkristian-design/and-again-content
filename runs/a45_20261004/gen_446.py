import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)})
    return out
lion={0.0:(.14,.24,.84,.85),0.5:(.1,.2,.85,.9),1.0:(.14,.17,.84,.9),1.5:(.15,.17,.85,.92),2.0:(.08,.2,.82,.9),2.5:(.08,.22,.8,.9),
3.0:(.02,.22,.9,1),3.5:(0,.24,.9,1),4.0:(0,.2,.9,1),4.5:(0,.2,.84,1),5.0:(0,.24,.82,1),5.5:(0,.21,.8,1),
6.0:(0,.2,.8,1),6.5:(0,.2,.82,1),7.0:(0,.2,.9,1),7.5:(.05,.2,.95,1),8.0:(.04,.22,.92,.95),8.5:(.04,.24,.92,.95),
9.0:(.02,.31,.92,.9),9.5:(.04,.28,.94,.9),10.0:(.04,.24,.95,.85)}
tree={0.0:(.45,0,.95,.15),0.5:(.3,0,1,.18),1.0:(.3,0,1,.17),1.5:(.3,.02,1,.17),2.0:(.25,.06,1,.2),2.5:(.22,.06,.97,.22),
3.0:(.12,.06,.85,.22),3.5:(0,.06,.7,.24),4.0:(0,.07,.46,.2),4.5:(0,.06,.3,.2),5.0:(0,.08,.2,.23),5.5:(0,.07,.2,.21),
6.0:(0,.07,.32,.2),6.5:(0,.07,.52,.2),7.0:(.04,.06,.7,.2),7.5:(.06,.07,.8,.2),8.0:(.08,.08,.82,.22),8.5:(.08,.07,.83,.24),
9.0:(.1,.04,.85,.3),9.5:(.12,0,.87,.27),10.0:(.13,0,.87,.23)}
c={"mediaId":446,"level":"A","keyWord":"lion","defaultVoice":"female",
"taps":[
{"phrase":"to open its mouth wide","target":"the lion","voice":"female","keys":keys(lion)},
{"phrase":"to walk through the grass","target":"the lion","voice":"female","keys":keys(lion)},
{"phrase":"to have a flat top","target":"the tree","voice":"female","keys":keys(tree)}],
"stillS":10.0,
"nouns":[{"word":"a lion","x":.5,"y":.52,"voice":"female"},{"word":"a tree","x":.5,"y":.06,"voice":"female"},
{"word":"grass","x":.5,"y":.88,"voice":"female"}],
"question":"What is the lion doing?",
"answer":["It","is","opening","its","mouth","wide."],
"answerVoice":"female",
"notes":"Two targets only: the lion and the flat tree far behind it (the animals at the horizon are small and blurred, not used). The lion walks 0-4.5 s, opens its mouth (roars) 5.0-9.0 s, then lies in the grass. 'the tree' = the far tree with the flat top; a second tree trunk stands close on the right at 4.0-6.0 s and is not boxed. Where the lion's mane reaches up into the tree (1.0-8.0 s) the two boxes are split by a horizontal line at the top of the mane, so the lowest bit of the far trunk falls in the lion's box. At 5.0-5.5 s only the edge of the far tree is seen at the left. Only 3 nouns: nothing else is clear and apart at 10.0 s."}
json.dump(c,open("content/446.json","w"),indent=1,ensure_ascii=False)

import json
T=[i*0.5 for i in range(11)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
w={0.0:(0,.15,.95,.85),0.5:(0,.14,.95,.86),1.0:(.36,.28,.64,.72),1.5:(.40,.55,.60,.45),2.0:(0,.05,1,.95),
2.5:(.03,.02,.97,.98),3.0:(0,.02,1,.98),3.5:(0,.02,.90,.98),4.0:(0,0,.90,1),4.5:(0,.16,1,.84),5.0:(0,.32,.40,.68)}
ph=["to hold some flowers","to sit by the window","to wear big glasses"]
c={"mediaId":303,"level":"A","keyWord":"flower","defaultVoice":"female",
"taps":[{"phrase":p,"target":"the woman","voice":"female","keys":keys(w)} for p in ph],
"stillS":0.5,
"nouns":[{"word":"a window","x":.35,"y":.07,"voice":"female"},{"word":"flowers","x":.70,"y":.56,"voice":"female"},{"word":"a woman","x":.25,"y":.38,"voice":"female"}],
"question":"What is the woman holding?",
"answer":["She","is","holding","some","flowers."],
"answerVoice":"female",
"notes":"Only one possible target (the woman), used for all three phrases; 'to wear big glasses' is a state. At 1.0 and 1.5 s only her hand is in the picture (close-up of the flowers): the box is the hand. At 3.0 s she is blurred behind the flower held to the lens (box = whole picture); at 5.0 s only her head and a bit of sweater show beside the bouquet."}
json.dump(c,open("content/303.json","w"),indent=1,ensure_ascii=False)
